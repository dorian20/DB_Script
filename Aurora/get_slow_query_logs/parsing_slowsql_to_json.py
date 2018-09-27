# -*- coding: utf-8 -*-
import mysql.utilities.common.parser as parser
import sys,io
import json
from collections import OrderedDict
import re
from pprint import pprint

filename=str(sys.argv[1])
slow_log=open(filename)
log=parser.SlowQueryLog(slow_log)

query_list_json=json.loads('{"querylist":[]}')
query_json={}
#query_json[0]=json.loads('{}')

#query_json=OrderedDict()

i=0

re.escape("\n\^stack\.\*/overflo\\w\$arr=1")

try:
    for entry in log:
        try:
            #pprint(entry)
            #print '#'+entry["datetime"]+'\n'+entry["query"]
 
            if entry['user'] == 'b2_dba' or entry['user']=='rdsadmin' or entry['user']=='b2_dev' or entry['user']=='b2_etl' or entry['user']==None:
                continue
            
            '''
            if entry['user'] != 'stuser':
                continue
            '''
            #pprint(entry)
            #print entry['user']
            #print entry['query_time']
            ''' 
            if int(entry['query_time']) < 1:
                continue
            '''
            pprint(entry)
            #print entry["query"]
            query_json[i]=json.loads('{}')
            query_json[i]["database"]=entry["database"]
            query_json[i]["user"]=entry["user"]
            #print '#'+entry["datetime"]+'\n'+entry["query"]
            query_json[i]["query"]='#'+str(entry["datetime"])+'\n'+entry["query"]
            #query_json["query1"]=entry["query"].split(';\n')[0]
            #query_json["query2"]=entry["query"].split(';\n')[1]
            #query_json["query3"]=entry["query"].split(';\n')[2]
    
            query_list_json["querylist"].append(query_json[i])
            #i=i+1
    
            for query in query_json[i]["query"].split(';'):
                #print (repr(query))
                #print query.encode('string_escape')
                #print query
                #print (repr(query))
                save=query.encode('string_escape').replace('\\\'','\'')
                with io.open('slow_'+entry["user"]+".sql",'a') as f:
                    f.write(unicode(save))
                    f.write(u'\n')

            i=i+1
        except (Exception) as err:
            i=0 
            print str(err)
except (Exception) as err:
    i=0
    print str(err)

#print query_list_json
#print query_list_json["querylist"][1]["query"]
#print unicode(json.dumps(query_list_json),indent=4))

