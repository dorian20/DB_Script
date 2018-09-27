import pymysql
import io, json
import os,sys
from collections import OrderedDict
def readJsonfile(filename):
    f=open(filename,'r')
    js = json.loads(f.read())
    f.close()
    return js
def getBinlogfile(vhost,vuser,vport,vpassword,vcharset,vcluster):
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
        cur.execute('show master status;')
        binloglist = cur.fetchall()
    except pymysql.err.InternalError as err:
        errmsg='InternalError:' + vcluster + ' ' + format(err)
        print(errmsg)
        return ''
    finally:
        cur.close()
        conn.close()
    return binloglist

iJsonfile = {}
iJsonfile = readJsonfile('rds_list.json')

#binlog_group=OrderedDict()
binlog_cluster=OrderedDict()
source_path=os.path.dirname(os.path.realpath(sys.argv[0]))+'/binlog_last_position/'


for rds_list in iJsonfile['DBClusters']:
    
    cluster=rds_list['DBClusterIdentifier']
    host=rds_list['Endpoint']
    user=rds_list['MasterUsername']
    engine=rds_list['Engine']
    port=rds_list['Port']
    
    if rds_list['MasterUsername']=='b2_dba' and rds_list['Engine']=='aurora':
        binloglist=getBinlogfile(host,user,port,'qwer1234','utf8mb4',cluster)
        i=0
        for data in binloglist:
            print data[0]
            i=i+1
            binlog_cluster[i]=OrderedDict()
            if data[0] != '':
                binlog_cluster[i]['Cluster']=cluster
                binlog_cluster[i]['Binlogfile']=data[0]
                binlog_cluster[i]['LastPosition']=data[1]
                binlog_cluster[i]['CheckPosition']=data[1]
                with io.open(source_path+'rds_last_position_'+cluster+'.json','w') as f:
                    f.write(unicode(json.dumps(binlog_cluster[i],indent=4)))
