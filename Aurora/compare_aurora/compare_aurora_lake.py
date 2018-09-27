# -*- coding: utf-8 -*-
from sshtunnel import SSHTunnelForwarder 
import pymysql,sys
from base64 import b64encode,b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import blake2b
import json


def encrypt_mytext(mytext,input_key):
    h = blake2b(digest_size=16)
    h.update(input_key.encode())
    key=h.hexdigest()
    #print(key)
    data=str(mytext)+" "
    cipher = AES.new(b64decode(key), AES.MODE_CBC, iv=b'0123456789abcdef')
    padded_data = pad(data.encode("utf-8"), cipher.block_size)
    encrypt_text = cipher.encrypt(padded_data)
    #print(encrypt_text)    
    return b64encode(encrypt_text).decode("utf-8")


def decrypt_mytext(encrypt_text,input_key):
    #print(ciphertext)    
    h = blake2b(digest_size=16)
    h.update(input_key.encode())
    key=h.hexdigest()
    #print(key)
    ciphertext = b64decode(encrypt_text.encode("utf-8"))
    cipher= AES.new(b64decode(key), AES.MODE_CBC, iv=b'0123456789abcdef')
    decrypt_text=str(cipher.decrypt(ciphertext).decode("utf-8")).split(' ')[0]
    return decrypt_text

def read_conn_info(file_name):
    f = open(file_name, 'r')
    line = f.readline()
    encrypt_json=json.loads(line)
    input_enc_key=input("enc key: ")
    server_infos_dec={}
    for key,value1 in encrypt_json.items():
        #print(key)
        
        dec_key=decrypt_mytext(key,input_enc_key)
        server_infos_dec[dec_key]={}
        for key2,value2 in value1.items():
            dec_key2=decrypt_mytext(key2,input_enc_key)
            dec_value2=decrypt_mytext(value2,input_enc_key)
            server_infos_dec[dec_key][dec_key2]=dec_value2
    
    return server_infos_dec

def get_input_val(input_type):
    while True:
        input_val=input(input_type+" 입력하세요: ")
        if(input_val != ''):
            return input_val
        print("공백입력은 안됩니다. 다시 입력해주세요.")

def InputNumber(min_number,max_number):
    while True:
        try:
            number = int(input("숫자를 입력하세요: "))
            if(number >=min_number and number <= max_number):
                return number
            
            print(str(min_number)+"~"+str(max_number)+"까지 입력")
        except Exception as ex:
            continue
def IsUseTunnel():
    print("###################################################################")
    print("  1. 터널링사용")
    print("  2. 터널링사용 안함")
    input_val = InputNumber(1,2)
    print("###################################################################")
    return input_val 
def MakeTunnel(bastion_ip,bastion_user,bastion_pwd,endpoint):
    tunnel=SSHTunnelForwarder(
        (bastion_ip, 22),
        ssh_username=bastion_user,
        ssh_password=bastion_pwd,
        remote_bind_address=(endpoint, 3306)
    )
    return tunnel

def get_server_info(server_infos):
    server_info={}
    print("1. PRD")
    print("2. TEST")
    print("3. DEV")
    env_menu=InputNumber(1,3)
    #env_menu=1
    if env_menu==1:    
        server_info["type"] = "prd" 
        server_info["bastion_ip"]=server_infos["elltprd1"]["source_bastion_ip"]
        server_info["bastion_user"]=server_infos["elltprd1"]["source_bastion_user"]
        server_info["bastion_pwd"]=server_infos["elltprd1"]["source_bastion_pwd"]
        server_info["ellt1_endpoint"] = server_infos["elltprd1"]["source_endpoint"]
        server_info["ellt2_endpoint"] = server_infos["elltprd2"]["source_endpoint"]
        server_info["ellt3_endpoint"] = server_infos["elltprd3"]["source_endpoint"]
        server_info["ellt4_endpoint"] = server_infos["elltprd4"]["source_endpoint"]
        server_info["ellt5_endpoint"] = server_infos["elltprd5"]["source_endpoint"]
        server_info["ellt6_endpoint"] = server_infos["elltprd6"]["source_endpoint"]
        server_info["ltcm1_endpoint"] = server_infos["ltcmprd1"]["source_endpoint"]
        server_info["db_user"] = server_infos["elltprd1"]["source_db_user"]
        server_info["db_pwd"] = server_infos["elltprd1"]["source_db_pwd"]
    elif env_menu==2:    
        server_info["type"] = "tst"
        server_info["bastion_ip"]=server_infos["ellttst1"]["source_bastion_ip"]
        server_info["bastion_user"]=server_infos["ellttst1"]["source_bastion_user"]
        server_info["bastion_pwd"]=server_infos["ellttst1"]["source_bastion_pwd"]
        server_info["ellt1_endpoint"] = server_infos["ellttst1"]["source_endpoint"]
        server_info["ellt2_endpoint"] = server_infos["ellttst2"]["source_endpoint"]
        server_info["ellt3_endpoint"] = server_infos["ellttst3"]["source_endpoint"]
        server_info["ellt4_endpoint"] = server_infos["ellttst4"]["source_endpoint"]
        server_info["ellt5_endpoint"] = server_infos["ellttst5"]["source_endpoint"]
        server_info["ellt6_endpoint"] = server_infos["ellttst6"]["source_endpoint"]
        server_info["ltcm1_endpoint"] = server_infos["ltcmtst1"]["source_endpoint"]
        server_info["db_user"] = server_infos["ellttst1"]["source_db_user"]
        server_info["db_pwd"] = server_infos["ellttst1"]["source_db_pwd"]
    elif env_menu==3:    
        server_info["type"] = "dev"
        server_info["bastion_ip"]=server_infos["elltdev"]["source_bastion_ip"]
        server_info["bastion_user"]=server_infos["elltdev"]["source_bastion_user"]
        server_info["bastion_pwd"]=server_infos["elltdev"]["source_bastion_pwd"]
        server_info["ellt1_endpoint"] = server_infos["elltdev"]["source_endpoint"]
        server_info["ltcm1_endpoint"] = server_infos["ltcmdev"]["source_endpoint"]
        server_info["db_user"] = server_infos["elltdev"]["source_db_user"]
        server_info["db_pwd"] = server_infos["elltdev"]["source_db_pwd"]
    return server_info

def get_connect_info():
    #print("다시 입력은 AGAIN_")

    server_info={}
    print("1. PRD")
    print("2. TEST")
    print("3. DEV")
    env_menu=InputNumber(1,3)
    #env_menu=2
    if env_menu==1:    
        server_info["type"] = "prd" 
        server_info["ellt1_endpoint"] = "elltprd1.cluster-ci9foimk0hp1.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt2_endpoint"] = "elltprd2.cluster-ci9foimk0hp1.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt3_endpoint"] = "elltprd3.cluster-ci9foimk0hp1.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt4_endpoint"] = "elltprd4.cluster-ci9foimk0hp1.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt5_endpoint"] = "elltprd5.cluster-ci9foimk0hp1.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt6_endpoint"] = "elltprd6.cluster-ci9foimk0hp1.ap-northeast-2.rds.amazonaws.com"
        server_info["ltcm1_endpoint"] = "ltcmprd1.cluster-c5szlalpckan.ap-northeast-2.rds.amazonaws.com"
        server_info["db_user"] = "b2_dba"
        server_info["db_pwd"] = "qwer1234"
    elif env_menu==2:    
        server_info["type"] = "tst"
        server_info["ellt1_endpoint"] = "ellttst1.cluster-cncbkablkgnk.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt2_endpoint"] = "ellttst2.cluster-cncbkablkgnk.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt3_endpoint"] = "ellttst3.cluster-cncbkablkgnk.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt4_endpoint"] = "ellttst4.cluster-cncbkablkgnk.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt5_endpoint"] = "ellttst5.cluster-cncbkablkgnk.ap-northeast-2.rds.amazonaws.com"
        server_info["ellt6_endpoint"] = "ellttst6.cluster-cncbkablkgnk.ap-northeast-2.rds.amazonaws.com"
        server_info["ltcm1_endpoint"] = "ltcmtst1.cluster-coq9a9jwz0c5.ap-northeast-2.rds.amazonaws.com"
        server_info["db_user"] = "b2_dba"
        server_info["db_pwd"] = "qwer1234"
    elif env_menu==3:    
        server_info["type"] = "dev"
        server_info["ellt1_endpoint"] = "elltdev.cluster-cbue0iqm0djc.ap-northeast-2.rds.amazonaws.com"
        server_info["ltcm1_endpoint"] = "ltcmdev.cluster-c0xgcmsoxdvu.ap-northeast-2.rds.amazonaws.com"
        server_info["db_user"] = "b2_dba"
        server_info["db_pwd"] = "qwer1234"

    
    
    return server_info

def compare_column(source_column_list,target_column_list):
    
    #print("###### 컬럼 비교 ##########")
    #print("table_name,column_name,column_type,collation_name,column_comment,column_default")
    i=0
    for source_column in source_column_list:
        samecolumn_flag=0
        #print(target_column_list)
        for target_column in target_column_list:
            #print(str(source_column[8]) + "." + str(source_column[0]) + " : " + str(target_column[8]) + "." +  str(target_column[0]) )
            if source_column[1] == target_column[1]:                
                samecolumn_flag=1
                if (source_column[2] != target_column[2] or
                   source_column[3] != target_column[3] or 
                   source_column[4] != target_column[4] or 
                   source_column[5] != target_column[5] or 
                   source_column[6] != target_column[6] or 
                   source_column[7] != target_column[7] ):
                    
                    print("#소스: "+ str(source_column[8]) + ', 테이블 - ' + str(source_column[0]) + ', 컬럼- ' + str(source_column[1]) + ', type- ' + str(source_column[2]) + ', CHARSET- '+ str(source_column[3]) + ', 커맨트- ' + str(source_column[4])+ ', ' + ', IS_NULLABLE- ' + str(source_column[6]) )
                    print("#타겟: "+ str(target_column[8]) + ', 테이블 - ' + str(target_column[0]) + ', 컬럼- ' + str(target_column[1]) + ', type- ' + str(target_column[2]) + ', CHARSET- '+ str(target_column[3]) + ', 커맨트- ' + str(target_column[4])+ ', ' + ', IS_NULLABLE- ' + str(target_column[6]) )
                    #print("#소스: {0}, 테이블 - {1}".format(str(source_column[8]),"a"))
                    if(str(source_column[6]) == "YES"):
                        null_option=" NULL"
                    else:
                        null_option="NOT NULL"
                    print("ALTER TABLE "+ str(target_column[8])+ "." + target_column[0] + " CHANGE COLUMN `"+ source_column[1] + "` "   )
                    print("`" + source_column[1] + "` "+ str(source_column[2]) + " " + null_option + " " + str(source_column[7]))
                    if(str(source_column[5]) !=  "None" ):
                        print("default " + str(source_column[5]) )
                    print("comment '" + str(source_column[4]) + "';" )
                    
        '''
        if samecolumn_flag==0:
            print("#"+source_column[0] + ":"+source_column[1] + " 컬럼 타겟에 없음")
            
            if(str(source_column[6]) == "YES"):
                null_option=" NULL"
            else:
                null_option="NOT NULL"

            print('ALTER TABLE '+ target_column[8] + "." + source_column[0] + " ADD COLUMN "+ source_column[1] + " " + str(source_column[2]) + " " + null_option + " " + str(target_column[7]))
            if(str(source_column[5]) !=  "None" ):
                print("default " + str(source_column[5]) )

            print("comment '" + str(source_column[4]) + "'" )
            print("AFTER `" + source_column_list[i-1][1] + "`;")
            '''

        i=i+1
        '''
    '''
    for target_column in target_column_list:
        samecolumn_flag=0
        for source_column in source_column_list:
            if (source_column[1] == target_column[1] or target_column[1] == "ETL_LOAD_DTTM" or target_column[1] == "ADJU_CRT_DT"):
                samecolumn_flag=1
        if samecolumn_flag==0:
            print("#"+target_column[0] + ":"+target_column[1] +" 컬럼 소스에 없음")
            
            print("ALTER TABLE "+target_column[8]+"."+target_column[0] + " drop column `" + target_column[1] + "`;")
              
    print("")
    
if __name__=='__main__':
    try:

        TUNNEL_FLAG=0
        CONNECT_FLAG=0
        use_tunnel_flag = IsUseTunnel()
        file_name = "conn_info.json"
        server_infos=read_conn_info(file_name)
        #use_tunnel_flag = 1
        if(use_tunnel_flag == 1):
            server_info=get_server_info(server_infos)
            ellt1_tunnel = MakeTunnel(server_info["bastion_ip"],server_info["bastion_user"],server_info["bastion_pwd"],server_info["ellt1_endpoint"])
            ellt1_tunnel.start()            
            TUNNEL_FLAG=1
            ltcm1_tunnel = MakeTunnel(server_info["bastion_ip"],server_info["bastion_user"],server_info["bastion_pwd"],server_info["ltcm1_endpoint"])
            ltcm1_tunnel.start()
            if server_info["type"] != "dev":
                ellt2_tunnel = MakeTunnel(server_info["bastion_ip"],server_info["bastion_user"],server_info["bastion_pwd"],server_info["ellt2_endpoint"])
                ellt2_tunnel.start()
                ellt3_tunnel = MakeTunnel(server_info["bastion_ip"],server_info["bastion_user"],server_info["bastion_pwd"],server_info["ellt3_endpoint"])
                ellt3_tunnel.start()
                ellt4_tunnel = MakeTunnel(server_info["bastion_ip"],server_info["bastion_user"],server_info["bastion_pwd"],server_info["ellt4_endpoint"])
                ellt4_tunnel.start()
                ellt5_tunnel = MakeTunnel(server_info["bastion_ip"],server_info["bastion_user"],server_info["bastion_pwd"],server_info["ellt5_endpoint"])
                ellt5_tunnel.start()
                ellt6_tunnel = MakeTunnel(server_info["bastion_ip"],server_info["bastion_user"],server_info["bastion_pwd"],server_info["ellt6_endpoint"])
                ellt6_tunnel.start()
            
            
            
            server_info["connect_ip"]='127.0.0.1'
            server_info["ellt1_connect_port"]=ellt1_tunnel.local_bind_port
            server_info["ltcm1_connect_port"]=ltcm1_tunnel.local_bind_port
            if server_info["type"] != "dev":
                server_info["ellt2_connect_port"]=ellt2_tunnel.local_bind_port
                server_info["ellt3_connect_port"]=ellt3_tunnel.local_bind_port
                server_info["ellt4_connect_port"]=ellt4_tunnel.local_bind_port
                server_info["ellt5_connect_port"]=ellt5_tunnel.local_bind_port
                server_info["ellt6_connect_port"]=ellt6_tunnel.local_bind_port            
            

            
            print("터널링포트 ellt1: "+str(ellt1_tunnel.local_bind_port))
            print("터널링포트 ltcm1: "+str(ltcm1_tunnel.local_bind_port))
            if server_info["type"] != "dev":
                print("터널링포트 ellt2: "+str(ellt2_tunnel.local_bind_port))
                print("터널링포트 ellt3: "+str(ellt3_tunnel.local_bind_port))
                print("터널링포트 ellt4: "+str(ellt4_tunnel.local_bind_port))
                print("터널링포트 ellt5: "+str(ellt5_tunnel.local_bind_port))
                print("터널링포트 ellt6: "+str(ellt6_tunnel.local_bind_port))
            

            #터널링 커넥션
            ellt1_conn = pymysql.connect(host='127.0.0.1', port=server_info["ellt1_connect_port"], user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')
            ltcm1_conn = pymysql.connect(host='127.0.0.1', port=server_info["ltcm1_connect_port"], user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')            
            if server_info["type"] != "dev":
                ellt2_conn = pymysql.connect(host='127.0.0.1', port=server_info["ellt2_connect_port"], user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')
                ellt3_conn = pymysql.connect(host='127.0.0.1', port=server_info["ellt3_connect_port"], user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')
                ellt4_conn = pymysql.connect(host='127.0.0.1', port=server_info["ellt4_connect_port"], user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')
                ellt5_conn = pymysql.connect(host='127.0.0.1', port=server_info["ellt5_connect_port"], user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')
                ellt6_conn = pymysql.connect(host='127.0.0.1', port=server_info["ellt6_connect_port"], user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')
            
            #Source 스키마 리스트 저장
            ellt1_cursor = ellt1_conn.cursor()            
            ltcm1_cursor = ltcm1_conn.cursor()
            if server_info["type"] != "dev":
                ellt2_cursor = ellt2_conn.cursor()
                ellt3_cursor = ellt3_conn.cursor()
                ellt4_cursor = ellt4_conn.cursor()
                ellt5_cursor = ellt5_conn.cursor()
                ellt6_cursor = ellt6_conn.cursor()
            CONNECT_FLAG=1
        

        '''
        elif(use_tunnel_flag == 2):
            server_info=get_connect_info()
            server_info["ellt_connect_ip"]=server_info["ellt_endpoint"]
            server_info["ltcm_connect_ip"]=server_info["ltcm_endpoint"]
            server_info["connect_port"]=3306
            ellt_conn = pymysql.connect(host=server_info["ellt_endpoint"], port=3306, user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')
            ltcm_conn = pymysql.connect(host=server_info["ltcm_endpoint"], port=3306, user=server_info["db_user"], password=server_info['db_pwd'], charset='UTF8')
            
            #Source 스키마 리스트 저장
            ellt_cursor = ellt_conn.cursor()
            ltcm_cursor = ltcm_conn.cursor()
            CONNECT_FLAG=1
        '''
        #origin_list_query = "select upper(table_name),upper(column_name),column_type,collation_name,column_comment,column_default,is_nullable,ifnull(extra,''),upper(table_schema)   from information_schema.columns  where table_name in (select substr(table_name,1,length(table_name)-4) from information_Schema.tables where table_name like '%_out' and (table_schema like 'ellt%' or table_schema like 'ltcm%'))  order by table_schema,table_name,ordinal_position;"
        
        out_table_list_query = "select table_schema,table_name from information_Schema.tables where (table_schema like 'ellt%' or table_schema like 'ltcm%') and table_name like '%_out' and table_schema not like '%_dba%' and table_schema <> 'elltetldev';"
        column_list_query = "select upper(table_name),upper(column_name),column_type,collation_name,column_comment,null column_default,is_nullable,/*ifnull(extra,'')*/ '',upper(table_schema)  from information_schema.columns where table_schema = '%s' and table_name='%s' and table_schema <> 'elltetldev' order by table_schema,table_name,ordinal_position ;"


        #컬럼비교
        out_table_list=[]
        ellt1_cursor.execute(out_table_list_query)  
        ellt1_table_list=ellt1_cursor.fetchall()
        ltcm1_cursor.execute(out_table_list_query)  
        ltcm1_table_list = ltcm1_cursor.fetchall()
        out_table_list.extend(ellt1_table_list)
        out_table_list.extend(ltcm1_table_list)
        if server_info["type"] != "dev":
            ellt2_cursor.execute(out_table_list_query)  
            ellt2_table_list=ellt2_cursor.fetchall()
            ellt3_cursor.execute(out_table_list_query)  
            ellt3_table_list=ellt3_cursor.fetchall()
            ellt4_cursor.execute(out_table_list_query)  
            ellt4_table_list=ellt4_cursor.fetchall()
            ellt5_cursor.execute(out_table_list_query)  
            ellt5_table_list=ellt5_cursor.fetchall()
            ellt6_cursor.execute(out_table_list_query)  
            ellt6_table_list=ellt6_cursor.fetchall()
            out_table_list.extend(ellt2_table_list)
            out_table_list.extend(ellt3_table_list)
            out_table_list.extend(ellt4_table_list)
            out_table_list.extend(ellt5_table_list)
            out_table_list.extend(ellt6_table_list)
        
        out_table_list=sorted(out_table_list,key=lambda x:x[1])
        print(out_table_list)
        
        
        for out_table in out_table_list:
            if(out_table[1][:2] in ("st","at")):
                server_type = "ltcm1"
            elif(out_table[1] in ("pr_dc_gsgr_pol_out")):
                server_type = "ltcm1"
            elif(out_table[1][:2] in ("dp","gd") and server_info["type"] != "dev"):
                server_type="ellt1"
            elif(out_table[1][:2] in ("ch","mb","pr") and server_info["type"] != "dev"):
                server_type="ellt2"
            elif(out_table[1][:2] in ("et","lo","om","py") and server_info["type"] != "dev"):
                server_type="ellt3"
            elif(out_table[1][:2] in ("cc","cm","se") and server_info["type"] != "dev"):
                server_type="ellt4"
            else:
                server_type="ellt1"
            origin_schema = server_type[:-1] + out_table[1][:2] + server_info["type"] 
            origin_table = out_table[1][:-4]


            print("############ " + origin_schema + "."+origin_table + " -> " + out_table[0] + "." + out_table[1] + "##############")
            #print(server_type)
            if server_type=="ltcm1":
                ltcm1_cursor.execute(column_list_query%(origin_schema,origin_table))  
                origin_column_list=ltcm1_cursor.fetchall()
            elif server_type=="ellt1":
                ellt1_cursor.execute(column_list_query%(origin_schema,origin_table))  
                origin_column_list=ellt1_cursor.fetchall()
            elif server_type=="ellt2":
                ellt2_cursor.execute(column_list_query%(origin_schema,origin_table))  
                origin_column_list=ellt2_cursor.fetchall()
            elif server_type=="ellt3":
                ellt3_cursor.execute(column_list_query%(origin_schema,origin_table))  
                origin_column_list=ellt3_cursor.fetchall()
            elif server_type=="ellt4":
                ellt4_cursor.execute(column_list_query%(origin_schema,origin_table))  
                origin_column_list=ellt4_cursor.fetchall()
            elif server_type=="ellt5":
                ellt5_cursor.execute(column_list_query%(origin_schema,origin_table))  
                origin_column_list=ellt5_cursor.fetchall()
            
            #print(origin_column_list)

            if out_table[0][4:-3] in ("st","at") :   
                #print(out_table[0][4:-3]+ " ltcm1") 
                ltcm1_cursor.execute(column_list_query%(out_table[0],out_table[1]))
                out_column_list=ltcm1_cursor.fetchall()
            elif (out_table[0][4:-3] in ("dp","gd") and server_info["type"] != "dev"):
                #print(out_table[0][4:-3]+ " ellt1") 
                ellt1_cursor.execute(column_list_query%(out_table[0],out_table[1]))
                out_column_list=ellt1_cursor.fetchall()
            elif (out_table[0][4:-3] in ("ch","mb","pr") and server_info["type"] != "dev"):
                #print(out_table[0][4:-3]+ " ellt2") 
                ellt2_cursor.execute(column_list_query%(out_table[0],out_table[1]))
                out_column_list=ellt2_cursor.fetchall()
            elif (out_table[0][4:-3] in ("et","lo","om","py") and server_info["type"] != "dev"):
                #print(out_table[0][4:-3]+ " ellt3") 
                ellt3_cursor.execute(column_list_query%(out_table[0],out_table[1]))
                out_column_list=ellt3_cursor.fetchall()
            elif (out_table[0][4:-3] in ("cc","cm","se") and server_info["type"] != "dev"):
                #print(out_table[0][4:-3]+ " ellt4") 
                ellt4_cursor.execute(column_list_query%(out_table[0],out_table[1]))
                out_column_list=ellt4_cursor.fetchall()
            elif (out_table[0][4:-3] in ("ombq") and server_info["type"] != "dev"):
                #print(out_table[0][4:-3]+ " ellt6") 
                ellt6_cursor.execute(column_list_query%(out_table[0],out_table[1]))
                out_column_list=ellt6_cursor.fetchall()
            else:
                #print(out_table[0][4:-3]+ " ellt") 
                ellt1_cursor.execute(column_list_query%(out_table[0],out_table[1]))
                out_column_list=ellt1_cursor.fetchall()
            
            #print(origin_column_list)
            #print(out_column_list)
            compare_column(origin_column_list,out_column_list)
        
        if(TUNNEL_FLAG==1):
            ellt1_tunnel.stop()
            ltcm1_tunnel.stop()
            if server_info["type"] != "dev":
                ellt2_tunnel.stop()
                ellt3_tunnel.stop()
                ellt4_tunnel.stop()
                ellt5_tunnel.stop()
                ellt6_tunnel.stop()

    except Exception as ex:
        if(TUNNEL_FLAG==1):
            ellt1_tunnel.stop()
            ltcm1_tunnel.stop()
            if server_info["type"] != "dev":
                ellt2_tunnel.stop()
                ellt3_tunnel.stop()
                ellt4_tunnel.stop()
                ellt5_tunnel.stop()
                ellt6_tunnel.stop()
        print(ex)
        sys.exit()            