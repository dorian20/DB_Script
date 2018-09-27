# -*- coding: utf-8 -*-
from sshtunnel import SSHTunnelForwarder 
import pymysql,sys

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

def get_server_info():
    print("다시 입력은 AGAIN_")
    input_list=["source_bastion_ip",
                "source_bastion_user",
                "source_bastion_pwd",
                "source_endpoint",
                "source_db_user",
                "source_db_pwd",
                "source_schema",
                "target_bastion_ip",
                "target_bastion_user",
                "target_bastion_pwd",
                "target_endpoint",
                "target_db_user",
                "target_db_pwd",
                "target_schema"]
    i=0
    server_info={}
    while i < len(input_list) :
        input_val=get_input_val(input_list[i])
        if(input_val=="AGAIN_"):
            i=0
            continue
        server_info[input_list[i]] = input_val
        i=i+1
    
    return server_info

def get_connect_info():
    print("다시 입력은 AGAIN_")
    input_list=["source_endpoint",
                "source_db_user",
                "source_db_pwd",
                "source_schema"
                "target_endpoint",
                "target_db_user",
                "target_db_pwd",
                "target_schema"]
    i=0
    server_info={}
    while i < len(input_list) :
        input_val=get_input_val(input_list[i])
        if(input_val=="AGAIN_"):
            i=0
            continue
        server_info[input_list[i]] = input_val
        i=i+1
    
    return server_info

def compare_table(source_table_list,target_table_list):
    if len(source_table_list)==0:
        print("소스테이블없음")
        return "",""
    elif len(target_table_list)==0:
        print("타겟테이블없음")
        return "",""

    print("###### 테이블 비교 ##########")
    #print("table_name,engine,row_format,table_collation,table_comment")
    target_not_exists = "''"
    source_not_exists = "''"
    for source_table in source_table_list:
        sametable_flag=0
        for target_table in target_table_list:
            if source_table[0] == target_table[0]:
                sametable_flag=1
                if source_table != target_table:
                    print("소스: "+source_table[0] + ',' + source_table[1] + ',' + source_table[2] + ','+ source_table[3] + ',' + source_table[4])
                    print("타겟: "+target_table[0] + ',' + target_table[1] + ',' + target_table[2] + ','+ target_table[3] + ',' + target_table[4])
        if sametable_flag==0:
            target_not_exists=target_not_exists+",'"+source_table[0]+"'"
            print(source_table[0] + " 테이블 타겟에 없음")
    
    for target_table in target_table_list:
        sametable_flag=0
        for source_table in source_table_list:
            if source_table[0] == target_table[0]:
                sametable_flag=1
        if sametable_flag==0:
            source_not_exists=source_not_exists+",'"+target_table[0]+"'"
            print(target_table[0] + " 테이블 소스에 없음")
    print("###### 테이블 비교 종료##########")
    return target_not_exists,source_not_exists

def compare_column(source_column_list,target_column_list):
    
    print("###### 컬럼 비교 ##########")
    #print("table_name,column_name,column_type,collation_name,column_comment,column_default")
    for source_column in source_column_list:
        samecolumn_flag=0
        for target_column in target_column_list:
            if source_column[0] == target_column[0] and source_column[1] == target_column[1]:
                samecolumn_flag=1
                if source_column != target_column:
                    print("소스: "+source_column[0] + ',' + source_column[1] + ',' + source_column[2] + ','+ source_column[3] + ',' + source_column[4]+ ',' + source_column[5])
                    print("타겟: "+target_column[0] + ',' + target_column[1] + ',' + target_column[2] + ','+ target_column[3] + ',' + target_column[4]+ ',' + source_column[5])
        if samecolumn_flag==0:
            print(source_column[0] + ":"+source_column[1] + " 컬럼 타겟에 없음")
    
    for target_column in target_column_list:
        samecolumn_flag=0
        for source_column in source_column_list:
            if source_column[0] == target_column[0] and source_column[1] == target_column[1]:
                samecolumn_flag=1
        if samecolumn_flag==0:
            print(target_column[0] + ":"+target_column[1] +" 컬럼 소스에 없음")
    print("###### 컬럼 비교 종료##########")

def compare_index(source_index_list,target_index_list):
    print("###### 인덱스 비교 ##########")
    #print("table_name,index_name,max(NON_UNIQUE) unique_flag,GROUP_CONCAT(index_name order by seq_in_index,',') index_list")
    for source_index in source_index_list:
        sameindex_flag=0
        for target_index in target_index_list:
            if source_index[0] == target_index[0] and source_index[1] == target_index[1]:
                sameindex_flag=1
                if source_index != target_index:
                    print("소스: "+source_index[0] + ',' + source_index[1] + ',' + str(source_index[2]) + ','+ source_index[3] )
                    print("타겟: "+target_index[0] + ',' + target_index[1] + ',' + str(target_index[2]) + ','+ target_index[3] )
        if sameindex_flag==0:
            print(source_index[0] + ":"+source_index[1] + " 인덱스 타겟에 없음")
    
    for target_index in target_index_list:
        sameindex_flag=0
        for source_index in source_index_list:
            if source_index[0] == target_index[0] and source_index[1] == target_index[1]:
                sameindex_flag=1
        if sameindex_flag==0:
            print(target_index[0] + ":"+target_index[1] +" 인덱스 소스에 없음")
    print("###### 인덱스비교 종료##########")

def compare_routine(source_routine_list,target_routine_list):

    if len(source_routine_list)==0 and len(target_routine_list)==0:
        return 0

    print("###### 루틴 비교(function,procedure) ##########")

    for source_routine in source_routine_list:
        sameroutine_flag=0
        for target_routine in target_routine_list:
            if source_routine[0] == target_routine[0]:
                sameroutine_flag=1
                if source_routine != target_routine:
                    print("소스: "+source_routine[0] + ',' + source_routine[1] + ',' + source_routine[2] )
                    print("타겟: "+target_routine[0] + ',' + target_routine[1] + ',' + target_routine[2] )
        if sameroutine_flag==0:
            print(source_routine[0] + " 타겟에 없음")
    
    for target_routine in target_routine_list:
        sameroutine_flag=0
        for source_routine in source_routine_list:
            #print(source_routine[0] + "," + target_routine[0])
            if source_routine[0] == target_routine[0]:
                sameroutine_flag=1
                
        if sameroutine_flag==0:
            print(target_routine[0] + " 소스에 없음")

def compare_colpriv(source_colpriv_list,target_colpriv_list):
    print("###### 컬럼권한 비교(function,procedure) ##########")

    for source_colpriv in source_colpriv_list:
        samecolpriv_flag=0
        for target_colpriv in target_colpriv_list:
            if (source_colpriv[0] == target_colpriv[0] 
            and source_colpriv[1] == target_colpriv[1]
            and source_colpriv[2] == target_colpriv[2]):
                samecolpriv_flag=1
                if source_colpriv != target_colpriv:
                    print("소스: "+source_colpriv[0] + ',' + source_colpriv[1] + ',' + source_colpriv[2]+ ',' + source_colpriv[3]+ ',' + source_colpriv[4] )
                    print("타겟: "+target_colpriv[0] + ',' + target_colpriv[1] + ',' + target_colpriv[2]+ ',' + target_colpriv[3]+ ',' + target_colpriv[4] )
        if samecolpriv_flag==0:
            print(source_colpriv[0] + ',' + source_colpriv[1] + ',' + source_colpriv[2]+ ',' + source_colpriv[3]+ ',' + source_colpriv[4] + " 타겟에 없음")
    
    for target_colpriv in target_colpriv_list:
        samecolpriv_flag=0
        for source_colpriv in source_colpriv_list:
            if (source_colpriv[0] == target_colpriv[0] 
            and source_colpriv[1] == target_colpriv[1]
            and source_colpriv[2] == target_colpriv[2]):
                samecolpriv_flag=1
        if samecolpriv_flag==0:
            print(target_colpriv[0] + ',' + target_colpriv[1] + ',' + target_colpriv[2]+ ',' + target_colpriv[3]+ ',' + target_colpriv[4] + " 소스에 없음")

def compare_schpriv(source_schpriv_list,target_schpriv_list):
    print("###### 스키마권한 비교(function,procedure) ##########")

    for source_schpriv in source_schpriv_list:
        sameschpriv_flag=0
        for target_schpriv in target_schpriv_list:
            if (source_schpriv[0] == target_schpriv[0] 
            and source_schpriv[1] == target_schpriv[1]):
                sameschpriv_flag=1
                if source_schpriv != target_schpriv:
                    print("소스: "+source_schpriv[0] + ',' + source_schpriv[1] + ',' + source_schpriv[2] )
                    print("타겟: "+target_schpriv[0] + ',' + target_schpriv[1] + ',' + target_schpriv[2] )
        if sameschpriv_flag==0:
            print(source_schpriv[0] + ',' + source_schpriv[1] + ',' + source_schpriv[2] + " 타겟에 없음")
    
    for target_schpriv in target_schpriv_list:
        sameschpriv_flag=0
        for source_schpriv in source_schpriv_list:
            if (source_schpriv[0] == target_schpriv[0] 
            and source_schpriv[1] == target_schpriv[1]):
                sameschpriv_flag=1
        if sameschpriv_flag==0:
            print(target_schpriv[0] + ',' + target_schpriv[1] + ',' + target_schpriv[2] + " 소스에 없음")

def compare_tabpriv(source_tabpriv_list,target_tabpriv_list):
    print("###### 테이블권한 비교(function,procedure) ##########")

    for source_tabpriv in source_tabpriv_list:
        sametabpriv_flag=0
        for target_tabpriv in target_tabpriv_list:
            if (source_tabpriv[0] == target_tabpriv[0] 
            and source_tabpriv[1] == target_tabpriv[1]
            and source_tabpriv[2] == target_tabpriv[2]):
                sametabpriv_flag=1
                if source_tabpriv != target_tabpriv:
                    print("소스: "+source_tabpriv[0] + ',' + source_tabpriv[1] + ',' + source_tabpriv[2] + ',' + source_tabpriv[3])
                    print("타겟: "+target_tabpriv[0] + ',' + target_tabpriv[1] + ',' + target_tabpriv[2] + ',' + target_tabpriv[3])
        if sametabpriv_flag==0:
            print(source_tabpriv[0] + ',' + source_tabpriv[1] + ',' + source_tabpriv[2]+ ',' + source_tabpriv[3] + " 타겟에 없음")
    
    for target_tabpriv in target_tabpriv_list:
        sametabpriv_flag=0
        for source_tabpriv in source_tabpriv_list:
            if (source_tabpriv[0] == target_tabpriv[0] 
            and source_tabpriv[1] == target_tabpriv[1]
            and source_tabpriv[2] == target_tabpriv[2]):
                sametabpriv_flag=1
        if sametabpriv_flag==0:
            print(target_tabpriv[0] + ',' + target_tabpriv[1] + ',' + target_tabpriv[2]+ ',' + target_tabpriv[3] + " 소스에 없음")

if __name__=='__main__':
    try:

        TUNNEL_FLAG=0
        CONNECT_FLAG=0
        use_tunnel_flag = IsUseTunnel()
        if(use_tunnel_flag == 1):
            server_info=get_server_info()

            source_tunnel = MakeTunnel(server_info["source_bastion_ip"],server_info["source_bastion_user"],server_info["source_bastion_pwd"],server_info["source_endpoint"])
            target_tunnel = MakeTunnel(server_info["target_bastion_ip"],server_info["target_bastion_user"],server_info["target_bastion_pwd"],server_info["target_endpoint"])
            source_tunnel.start()
            TUNNEL_FLAG=1
            target_tunnel.start()
            server_info["source_connect_ip"]='127.0.0.1'
            server_info["target_connect_ip"]='127.0.0.1'
            server_info["source_connect_port"]=source_tunnel.local_bind_port
            server_info["target_connect_port"]=target_tunnel.local_bind_port
            print("ASIS 터널링포트: "+str(source_tunnel.local_bind_port)+" ,TOBE 터널링포트: " + str(target_tunnel.local_bind_port))
            #터널링 커넥션
            source_conn = pymysql.connect(host='127.0.0.1', port=server_info["source_connect_port"], user=server_info["source_db_user"], password=server_info['source_db_pwd'], charset='UTF8')
            target_conn = pymysql.connect(host='127.0.0.1', port=server_info["target_connect_port"], user=server_info["target_db_user"], password=server_info['target_db_pwd'], charset='UTF8')
            #Source 스키마 리스트 저장
            source_cursor = source_conn.cursor()
            target_cursor = target_conn.cursor()
            CONNECT_FLAG=1
        elif(use_tunnel_flag == 2):
            server_info=get_connect_info()
            server_info["source_connect_ip"]=server_info["source_endpoint"]
            server_info["target_connect_ip"]=server_info["target_endpoint"]
            server_info["source_connect_port"]=3306
            server_info["target_connect_port"]=3306
            source_conn = pymysql.connect(host=server_info["source_endpoint"], port=3306, user=server_info["source_db_user"], password=server_info['source_db_pwd'], charset='UTF8')
            target_conn = pymysql.connect(host=server_info["target_endpoint"], port=3306, user=server_info["target_db_user"], password=server_info['target_db_pwd'], charset='UTF8')
            #Source 스키마 리스트 저장
            source_cursor = source_conn.cursor()
            target_cursor = target_conn.cursor()
            CONNECT_FLAG=1

        table_list_query = "select table_name,engine,row_format,table_collation,table_comment from information_schema.tables where table_schema='%s'"
        column_list_query = "select table_name,column_name,column_type,collation_name,column_comment,column_default from information_schema.columns where table_schema='%s' and table_name not in (%s)"
        count_query='select count(1) from %s.%s'
        index_list_query="select table_name,index_name,max(NON_UNIQUE) unique_flag,GROUP_CONCAT(column_name order by seq_in_index,',') column_list\n" 
        index_list_query=index_list_query + "from information_schema.STATISTICS\n"
        index_list_query=index_list_query + "where table_schema='%s' and table_name not in (%s)\n"
        index_list_query=index_list_query + "group by table_name,index_name"
        routine_list_query="select routine_name,routine_type,md5(ROUTINE_DEFINITION) routine_md5 from information_schema.ROUTINES where routine_schema='%s'"
        column_privilege_query="select grantee,table_name,column_name,privilege_type,is_grantable from information_schema.COLUMN_PRIVILEGES where table_schema='%s'"
        schema_privilege_query="select grantee,privilege_type,is_grantable from information_schema.SCHEMA_PRIVILEGES where table_schema='%s'"
        table_privilege_query="select grantee,table_name,privilege_type,is_grantable from information_schema.TABLE_PRIVILEGES where table_schema='%s'"
        
        #테이블리스트
        source_cursor.execute(table_list_query%(server_info["source_schema"]))  
        source_table_list=source_cursor.fetchall()
        target_cursor.execute(table_list_query%(server_info["target_schema"]))  
        target_table_list=target_cursor.fetchall()

        target_not_exists,source_not_exists=compare_table(source_table_list,target_table_list)

        if(target_not_exists!=""):
            #카운트비교
            print("########건수비교##########")
            for source_table in  source_table_list:
                not_exists_flag=0
                for target_not_exists_table in target_not_exists.replace("'","").split(","):
                    if source_table[0]==target_not_exists_table:
                        not_exists_flag=1
                
                if not_exists_flag==0:
                    source_cursor.execute(count_query%(server_info["source_schema"],source_table[0]))
                    source_count=source_cursor.fetchall()
                    target_cursor.execute(count_query%(server_info["target_schema"],source_table[0]))
                    target_count=target_cursor.fetchall()
                    if source_count != target_count:
                        print(source_table[0] + " 소스건수:" + str(source_count[0][0]) + " , 타겟건수:" + str(target_count[0][0]))

            #컬럼비교
            source_cursor.execute(column_list_query%(server_info["source_schema"],target_not_exists))  
            source_column_list=source_cursor.fetchall()
            target_cursor.execute(column_list_query%(server_info["target_schema"],source_not_exists))  
            target_column_list=target_cursor.fetchall()
            compare_column(source_column_list,target_column_list)
            #인덱스비교
            source_cursor.execute(index_list_query%(server_info["source_schema"],target_not_exists))  
            source_index_list=source_cursor.fetchall()
            target_cursor.execute(index_list_query%(server_info["target_schema"],source_not_exists))  
            target_index_list=target_cursor.fetchall()
            compare_index(source_index_list,target_index_list)
            #루틴비교
            source_cursor.execute(routine_list_query%(server_info["source_schema"]))  
            source_routine_list=source_cursor.fetchall()
            target_cursor.execute(routine_list_query%(server_info["target_schema"]))  
            target_routine_list=target_cursor.fetchall()
            compare_routine(source_routine_list,target_routine_list)

            #컬럼권한비교
            source_cursor.execute(column_privilege_query%(server_info["source_schema"]))  
            source_colpriv_list=source_cursor.fetchall()
            target_cursor.execute(column_privilege_query%(server_info["target_schema"]))  
            target_colpriv_list=target_cursor.fetchall()
            compare_colpriv(source_colpriv_list,target_colpriv_list)

            #스키마권한비교
            source_cursor.execute(schema_privilege_query%(server_info["source_schema"]))  
            source_schpriv_list=source_cursor.fetchall()
            target_cursor.execute(schema_privilege_query%(server_info["target_schema"]))  
            target_schpriv_list=target_cursor.fetchall()
            compare_schpriv(source_schpriv_list,target_schpriv_list)

            #테이블권한비교
            source_cursor.execute(table_privilege_query%(server_info["source_schema"]))  
            source_tabpriv_list=source_cursor.fetchall()
            target_cursor.execute(table_privilege_query%(server_info["target_schema"]))  
            target_tabpriv_list=target_cursor.fetchall()
            compare_tabpriv(source_tabpriv_list,target_tabpriv_list)

        if(TUNNEL_FLAG==1):
            source_tunnel.stop()
            target_tunnel.stop()
        


    except Exception as ex:
        if(TUNNEL_FLAG==1):
            source_tunnel.stop()
            target_tunnel.stop()
        print(ex)
        sys.exit()

