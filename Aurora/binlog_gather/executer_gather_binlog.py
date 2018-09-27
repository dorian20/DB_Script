#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pymysql
import os
from subprocess import call
import io, json
from collections import OrderedDict
import subprocess
from pprint import pprint
from decimal import *
import json, boto3, uuid, datetime
import logging
import time

def readJsonfile(filename):
    f=open(filename,'r')
    js = json.loads(f.read())
    f.close()
    return js
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

source_path=os.path.dirname(os.path.realpath(sys.argv[0]))+'/'
binlog_gather_log_path = source_path+'binlog_gather_log/'
source_name='gather_binlogfile.py'
logfile_name = binlog_gather_log_path+'executer.log' 
Mylogger=callLog(logfile_name)
try:
    source_name='gather_binlogfile.py'
    source_path=os.path.dirname(os.path.realpath(sys.argv[0]))+'/'
    binlog_gather_log_path = source_path+'binlog_gather_log/'
    #print source_path
    rds_list_file = {}
    rds_list_file = readJsonfile(source_path+'rds_list.json')
    '''
    if len(sys.argv) < 2:
        usage='Usage: python executer_gather_binlog.py'
        print usage
        Mylogger.info(usage)
    '''
    try:
        #check_arg=0

        for rds_list in rds_list_file['DBClusters']:
            '''
            if sys.argv[1] != 'ALL' and rds_list['DBClusterIdentifier'] != sys.argv[1]:
                continue;
            '''

            if rds_list["getbinlog"]!="YES":
                Mylogger.info(rds_list['DBClusterIdentifier'] + '`s getbinlog value is not YES')
                continue;

            #check_arg=1
 
            cluster=rds_list['DBClusterIdentifier']
            host=rds_list['Endpoint']
            user=rds_list['MasterUsername']
            engine=rds_list['Engine']
            port=rds_list['Port']
            logfile_name = binlog_gather_log_path+cluster+'_binlog_gather.log'
            process_check=int(subprocess.Popen("ps -ef|grep -v grep|grep "+source_name+"|grep "+cluster+"|wc -l",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0])
            #print process_check
    
            if user=='b2_dba' and engine=='aurora' and process_check==0:
                argms=cluster+' '+host+' '+str(port)+' '+source_path
                #print argms
                Mylogger.info('##################'+cluster + ' start###################')
                Mylogger.info('nohup python '+source_path+source_name+' '+argms+'> /dev/null 2>&1 &')
                os.system('nohup python '+source_path+source_name+' '+argms+'> /dev/null 2>&1 &')
                
                #Mylogger.info('##################'+cluster + ' start###################')
                #callLog( cluster + ' start',logfile_name,'info')
                #print logfile_name
            else :
                #callLog( cluster + ' is still running!!!!!!!',logfile_name,'info')
                
                Mylogger.warning('!!!!!!!!!!!!!!!!!!!!'+cluster + ' is still running!!!!!!!!!!!!!!!')
        '''
        if check_arg==0:
            Mylogger.warning(sys.argv[1]+' is not in rds_lists')
        '''
    except (Exception) as err:
        #logfile_name = binlog_gather_log_path+cluster+'_binlog_gather.log'
        callLog(str(err),logfile_name,'error')

except (Exception) as err:
    logfile_name = binlog_gather_log_path+'executer.log'
    Mylogger.error(str(err))


