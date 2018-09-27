# -*- coding: utf-8 -*-
import pymysql
import os
from subprocess import call
import io, json
from collections import OrderedDict
import subprocess
from pprint import pprint
from decimal import *
import json, boto3, uuid, datetime
import sys
import logging
import time
from pyathena import connect
from config import conf

def callLog(logfile_name):

    logger=logging.getLogger('Binlog Gathering Log')
    fileHandler = logging.FileHandler(logfile_name)
    fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
    streamHandler = logging.StreamHandler()
    fileHandler.setFormatter(fomatter)
    logger.addHandler(fileHandler)
    loggerLevel=logging.INFO
    logger.setLevel(loggerLevel)
    return logger

def readJsonfile(filename):
    f=open(filename,'r')
    js = json.loads(f.read())
    f.close()
    return js
def getBinlog(vhost,vuser,vport,vpassword,vcharset,vcluster):
    conn= pymysql.connect(
                   host = vhost,
                   user = vuser,
                   password=vpassword,
                   port = vport,
                   #db='jmktest',
                   charset=vcharset
               )
    try:
        cur=conn.cursor()
        cur.execute('show binary logs;')
        binloglist = cur.fetchall()
    except pymysql.err.InternalError as err:
        errmsg='InternalError:' + vcluster + ' ' + format(err)
        print(errmsg)
        return ''
    finally:
        cur.close()
        conn.close()
    return binloglist

#def makeGetBinlogCommand(password,host,port,user,cluster,binlog,position,path):
def makeGetBinlogCommand(password,host,port,user,cluster,binlog,path):
    binlog_command='MYSQL_PWD='+password
    binlog_command=binlog_command + ' mysqlbinlog -R --raw --host=' + host + ' --port ' + str(port) + ' --user ' + user + ' --result-file='+path
    binlog_command=binlog_command + cluster+'_'#+str(position)+'_'
    #binlog_command=binlog_command + ' --start_position='+str(position)
    binlog_command=binlog_command + ' ' + binlog
    return binlog_command

#def makeParsingCommand(user,password,host,port,binlog,position,cluster,binlog_raw_path,binlog_json_path,source_path):
def makeParsingCommand(user,password,host,port,binlog,cluster,binlog_raw_path,binlog_json_path,source_path):
    parsing_command='DB_DSN="'+user+':'+password+'@tcp('+host+':'+str(port)+')/information_schema" '+source_path+'binlog-parser/bin/binlog-parser '
    #parsing_command=parsing_command + binlog_raw_path+cluster+'_'+str(position)+'_'+binlog
    #parsing_command=parsing_command + '> '+binlog_json_path+cluster+'_'+str(position)+'_'+binlog+'.json'
    parsing_command=parsing_command + binlog_raw_path+cluster+'_'+binlog
    parsing_command=parsing_command + '> '+binlog_json_path+cluster+'_'+binlog+'.json'
    return parsing_command

def changeDataType(kvData):
    for key in kvData:
        #print 'before: '+ str(kvData[key]) + str(isinstance(kvData[key],str))
        #print type(kvData[key])
        if isinstance(kvData[key], str) and kvData[key] == '':
            kvData[key] = None
            #print 'after: ' + str(kvData[key])
        elif isinstance(kvData[key], unicode) and kvData[key] == '':
            kvData[key] = None
        elif isinstance(kvData[key], float):
            kvData[key] = Decimal(str(kvData[key]))
    return kvData

# 인자값으로 DB 이름이 필요함!

def insertDDB(cluster,json_file,Mylogger):
    ddb = boto3.resource(service_name='dynamodb',
                              aws_access_key_id = 'AKIAJ5WLSHU225P7S2EQ',
                              aws_secret_access_key = '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',
                              region_name = 'ap-northeast-2')
    
    table = ddb.Table('AURORA_BINARY_LOG')
    dbName = cluster
    t = {}
    #print(json_file)
    Mylogger.info("START INSERT DDB")

    with table.batch_writer() as batch:
        with open(json_file, 'r') as json_data:
            documents = json_data.readlines()
            i = 0
            for document in documents:
                newMap = json.loads(document)
                #print('##########'+newMap['Type'])  
                # Null => None /// ''(empty string) => None
                if newMap['Type'] == 'Insert' or newMap['Type'] == 'Delete':
                    #print('#####before###########' + str(newMap['Data']['Row']))
                    newMap['Data']['Row']=changeDataType(newMap['Data']['Row'])
                    #print('#####after###########' + str(newMap['Data']['Row']))
                    if newMap['Data']['MappingNotice'] == '':
                        newMap['Data']['MappingNotice'] = None
    
                elif newMap['Type'] == 'Update':
                    newMap['OldData']['Row']=changeDataType(newMap['OldData']['Row'])
                    newMap['NewData']['Row']=changeDataType(newMap['NewData']['Row'])
    
                    if newMap['OldData']['MappingNotice'] == '':
                        newMap['OldData']['MappingNotice'] = None
                    if newMap['NewData']['MappingNotice'] == '':
                        newMap['NewData']['MappingNotice'] = None
    
                if newMap['Header']['Schema'] == '':
                    newMap['Header']['Schema'] = "(unknown)"
    
                newMap['BinlogMessageTime'] = newMap['Header']['BinlogMessageTime']
                newMap['BinlogPosition'] = newMap['Header']['BinlogPosition']
                newMap['Schema'] = newMap['Header']['Schema']
                newMap['Table'] = newMap['Header']['Table']
                newMap['XId'] = newMap['Header']['XId']
                newMap['DbName'] = dbName
    
                newMap['LOG_NO'] = str(uuid.uuid4())
                #GSI01 : LOG_TABLE_NM = dbname + schema + table                        | BinlogMessageTime
                #GSI02 : LOG_TABLE_OP = dbname + schema + table + operation            | BinlogMessageTime
                newMap['LOG_TABLE_NM'] = "{0}:{1}:{2}".format(dbName,newMap['Schema'],newMap['Table'])
                newMap['LOG_TABLE_OP'] = "{0}:{1}:{2}:{3}".format(dbName,newMap['Schema'],newMap['Table'],newMap['Type'])
                #print newMap   
                if i%100 == 0:
                    Mylogger.info("WRITE : " + str(i))
    
                batch.put_item(Item=newMap)
                i = i + 1

            Mylogger.info("END "+str(i)+ "ROWS INSERT DDB ")

def insertS3(filepath,filename,cluster,binlog_date):
    profile=conf.s3_profile
    #s3_path='jmk-athena-test/binlog/json/'
    s3_path=conf.s3_path
    d_yyyy=binlog_date[:4]
    d_mm=binlog_date[5:7]
    d_dd=binlog_date[8:10]

    athena_partition_path= cluster + '/' + d_yyyy + '/' + d_mm + '/' + d_dd + '/'

    command='aws  --profile '+ profile +' s3 cp ' + filepath + filename + 's3://' + s3_path + athena_partition_path + filename
    Mylogger.info("INSERT S3:" + command)
    os.system(command)
    
    return_value = {}
    return_value["cluster"]=cluster
    return_value["yyyy"]=d_yyyy
    return_value["mm"]=d_mm
    return_value["dd"]=d_dd

    return return_value


def athena_add_partition(cluster,d_yyyy,d_mm,d_dd):
    cursor = connect(aws_access_key_id=conf.athena_access_key,
                     aws_secret_access_key=conf.athena_secret_access_key,
                     s3_staging_dir=conf.s3_staging_dir,
                     region_name=conf.region_name).cursor()

    command= "ALTER TABLE " + conf.athena_schema + "." + conf.athena_table + " ADD IF NOT EXISTS PARTITION "
    command= command + "(cluster='" + cluster + "', yyyy='"+ d_yyyy + "', mm='" + d_mm + "', dd='" + d_dd + "') "
    command= command + "location 's3://" + conf.s3_path + cluster + "/" + d_yyyy + "/" + d_mm + "/" + d_dd + "'"
    Mylogger.info("Athena_add_partition:" + command)
    cursor.execute(command)

try:
    #Arguments
    cluster=str(sys.argv[1])
    host=sys.argv[2]
    user=conf.rds_user
    port=int(sys.argv[3])
    source_path=sys.argv[4]
    password=conf.rds_password
    binlog_gather_log_path=conf.binlog_gather_log_path
    logfile_name = binlog_gather_log_path+cluster+'_binlog_gather.log'
    Mylogger=callLog(logfile_name)
    binlog_raw_path=conf.binlog_raw_path
    binlog_json_path=conf.binlog_json_path
    binlog_last_position_path=source_path+'binlog_last_position/'
    
    
    binlog_list=getBinlog(host,user,port,password,'utf8mb4',cluster)
    
    rds_position = {}
    Mylogger.info('readJsonfile '+'rds_last_position_'+cluster+'.json')
    rds_position = readJsonfile(binlog_last_position_path+'rds_last_position_'+cluster+'.json')
    
    before_binlog=rds_position['Binlogfile']
    check_position=rds_position["CheckPosition"]
    before_position = rds_position["LastPosition"]
    Mylogger.info('readJsonfile:'+before_binlog+','+str(check_position)+','+str(before_position))
    binlog_cluster=OrderedDict()
    binlog_cluster=rds_position
    Mylogger.info('binlg_cluster OrderedDict before for..') 
    for binlog_data in binlog_list:
        #Mylogger.info('binlg_cluster OrderedDict in for..')
        if binlog_data[0] == '':
            break;
    
        if binlog_data[0] < before_binlog:
            continue;
    
        if binlog_data[0] == before_binlog and binlog_data[1] <= max(before_position,check_position):
            continue;

        if binlog_data[1] <= 120:
            Mylogger.warning(binlog_data[0] + ' is empty!!!!')
            continue;
    
        cur_binlog=binlog_data[0]
        cur_position=binlog_data[1]
        start_position=1
        command_binlog=cur_binlog
        #Mylogger.info('Before if:'+cur_binlog)
        Mylogger.info(rds_position['Cluster']+rds_position['Binlogfile']+str(cur_position)+str(check_position)) 

        if rds_position['Cluster']==cluster and rds_position['Binlogfile']==cur_binlog and cur_position > check_position:
            start_position=check_position
            command_binlog=before_binlog
        
        Mylogger.info( '################ get binlog command #############################')
        #binlog_command=makeGetBinlogCommand(password,host,port,user,cluster,command_binlog,start_position,binlog_raw_path)
        binlog_command=makeGetBinlogCommand(password,host,port,user,cluster,command_binlog,binlog_raw_path)
        Mylogger.info( binlog_command)
        Mylogger.info( '################ parsing command ################################')
        #parsing_command=makeParsingCommand(user,password,host,port,command_binlog,start_position,cluster,binlog_raw_path,binlog_json_path,source_path)
        parsing_command=makeParsingCommand(user,password,host,port,command_binlog,cluster,binlog_raw_path,binlog_json_path,source_path)
        Mylogger.info( parsing_command)
        os.system(binlog_command)
        os.system(parsing_command)
        #insertDDB(cluster,binlog_json_path+cluster+'_'+str(start_position)+'_'+before_binlog+'.json',Mylogger)
        print(binlog_command)
        print(parsing_command)

        #print start_position
        #print binlog_json_path+cluster+'_'+str(start_position)+'_'+cur_binlog+'.json'
    
        #json_tail=subprocess.check_output(['tail', '-1', binlog_json_path+cluster+'_'+str(start_position)+'_'+cur_binlog+'.json'])
        #json_tail=subprocess.Popen('tail -1 '+binlog_json_path+cluster+'_'+str(start_position)+'_'+cur_binlog+'.json',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
        json_head=subprocess.Popen('head -1 '+binlog_json_path+cluster+'_'+cur_binlog+'.json',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
        json_tail=subprocess.Popen('tail -1 '+binlog_json_path+cluster+'_'+cur_binlog+'.json',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
        #print json_tail
        #Mylogger.info(json_tail)
        json_head=json.loads(json_head)
        json_tail=json.loads(json_tail)
        binlog_cluster['Cluster']=cluster
        binlog_cluster['Binlogfile']=cur_binlog
        binlog_cluster['LastPosition']=cur_position
        binlog_cluster['CheckPosition']=json_tail["Header"]["BinlogPosition"]
        #print binlog_cluster

        r_val=insertS3(binlog_json_path,cluster+'_'+cur_binlog+'.json ',cluster,json_head["Header"]["BinlogMessageTime"])
        
        athena_add_partition(r_val["cluster"],r_val["yyyy"],r_val["mm"],r_val["dd"])    

        Mylogger.info('rds_last_position jsonfile write')
        with io.open(binlog_last_position_path+'rds_last_position_'+cluster+'.json','w') as f:
            f.write(unicode(json.dumps(binlog_cluster,indent=4)))

    #time.sleep(30)

except (Exception) as err:
    print err
    Mylogger.error(str(err))
    sys.exit(1)
            
