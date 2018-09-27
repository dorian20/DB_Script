# -*- coding: utf-8 -*-
import sys
import subprocess
import json

def getRemoveList(all_list):
    remove_list=[]
    if len(all_list) == 0:
        print("제거할 목록 없음")
        return remove_list

    for element in all_list:
        print(element)
    
    print("제외할 값을 입력해주세요.")
    print("더 이상 입력하지 않으시려면 QUIT_ 를 입력해주세요.")
    while True:
        check_flag=0
        input_val=input("제외할 리스트 입력: ")

        if(input_val == "QUIT_"):
            return remove_list

        for database in all_list:
            if(database == input_val):
                check_flag=1
                remove_list.extend([input_val])
        
        if(check_flag==0):
            print("리스트에 없는 값을 입력하였습니다.")
def InputNumber(min_number,max_number):
    while True:
        try:
            number = int(input("숫자를 입력하세요: "))
            if(number >=min_number and number <= max_number):
                return number
            
            print(str(min_number)+"~"+str(max_number)+"까지 입력")
        except Exception as ex:
            continue







if __name__=='__main__':

    modify_config = {
        "cluster":[
            {
                "--new-db-cluster-identifier":"",
                "--apply-immediately | --no-apply-immediately":"",
                "--backup-retention-period":"",
                "--db-cluster-parameter-group-name":"",
                "--vpc-security-group-ids":"",
                "--port":"",
                "--master-user-password":"",
                "--option-group-name":"",
                "--preferred-backup-window":"",
                "--preferred-maintenance-window":"",#Format: ddd:hh24:mi-ddd:hh24:mi Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
                "--enable-iam-database-authentication | --no-enable-iam-database-authentication":"",
                "--backtrack-window":"",
                "--cloudwatch-logs-export-configuration":"",
                "--engine-version":"",
                "--cli-input-json":"",
                "--generate-cli-skeleton":""
            }
        ],
        "instance":[
            {
                "--allocated-storage":"",
                "--db-instance-class":"db.r4.large",
                "--db-subnet-group-name":"",
                "--db-security-groups":"",
                "--vpc-security-group-ids":"",
                "--apply-immediately | --no-apply-immediately":"--apply-immediately",
                "--master-user-password":"",
                "--db-parameter-group-name":"",
                "--backup-retention-period":"",
                "--preferred-backup-window":"",
                "--preferred-maintenance-window":"",#Format: ddd:hh24:mi-ddd:hh24:mi Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun
                "--multi-az | --no-multi-a":"",
                "--engine-version":"",
                "--allow-major-version-upgrade | --no-allow-major-version-upgrad":"",
                "--auto-minor-version-upgrade | --no-auto-minor-version-upgrad":"",
                "--license-model":"",
                "--iops":"",
                "--option-group-name":"",
                "--new-db-instance-identifier":"",
                "--storage-type":"",
                "--tde-credential-arn":"",
                "--tde-credential-password":"",
                "--ca-certificate-identifier":"",
                "--domain":"",
                "--copy-tags-to-snapshot | --no-copy-tags-to-snapsho":"",
                "--monitoring-interval":"",
                "--db-port-number":"",
                "--publicly-accessible | --no-publicly-accessibl":"",
                "--monitoring-role-arn":"",
                "--domain-iam-role-name":"",
                "--promotion-tier":"",
                "--enable-iam-database-authentication | --no-enable-iam-database-authenticatio":"",
                "--enable-performance-insights | --no-enable-performance-insight":"",
                "--performance-insights-kms-key-id":"",
                "--cloudwatch-logs-export-configuration":"",
                "--cli-input-json":"",
                "--generate-cli-skeleton":""
            }
        ],
        "pending-maintenance":[
            {
                "--apply-action":"",#db-upgrade,system-update
                "--opt-in-type":""#immediate,next-maintenance
            }
        ],
        "restore-db":[
            {
                "--restore-type":"",#copy-on-write
                "--restore-to-time":"",
                "--use-latest-restorable-time | --no-use-latest-restorable-time":"",
                "--port":"",
                "--db-subnet-group-name":"",
                "--option-group-name":"",
                "--vpc-security-group-ids":"",
                "--tags":"",
                "--kms-key-id":"",
                "--enable-iam-database-authentication | --no-enable-iam-database-authentication":"",
                "--backtrack-window":"",
                "--enable-cloudwatch-logs-exports":"",
                "--cli-input-json":"",
                "--generate-cli-skeleton":""
            }
        ]

    }

    next_line_continue="^"

    instance_flag = 0
    cluster_flag=0
    pending_flag=0
    restore_flag=0

    for config in modify_config["instance"][0]:
        if str(modify_config["instance"][0][config]) != "":
            instance_flag = 1

    for config in modify_config["cluster"][0]:
        if str(modify_config["cluster"][0][config]) != "":
            cluster_flag = 1

    for config in modify_config["pending-maintenance"][0]:
        if str(modify_config["pending-maintenance"][0][config]) != "":
            pending_flag = 1
    
    for config in modify_config["restore-db"][0]:
        if str(modify_config["restore-db"][0][config]) != "":
            restore_flag = 1

    

    print("1. PRD")
    print("2. TEST")
    print("3. DEV")
    print("4. 종료")
    env_menu=InputNumber(1,4)
    if env_menu==4:
        sys.exit()
    elif env_menu==1:    
        env = "prd" 
    elif env_menu==2:    
        env = "tst"
    elif env_menu==3:    
        env = "dev" 


    b2_profile="l-b2-" + env
    ellt_profile="l-ellotte-" + env        

    result=subprocess.Popen("aws --profile "+ ellt_profile +" rds describe-db-clusters",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    ellt_rds_cluster_list=json.loads(result)

    result=subprocess.Popen("aws --profile "+ b2_profile +" rds describe-db-clusters",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    b2_rds_cluster_list=json.loads(result)

    b2_rds_cluster=[]
    for b2_cluster in b2_rds_cluster_list["DBClusters"]:
        print(b2_cluster["DBClusterIdentifier"])
        b2_rds_cluster.extend([b2_cluster["DBClusterIdentifier"]])

    

    ellt_rds_cluster=[]
    for ellt_cluster in ellt_rds_cluster_list["DBClusters"]:
        print(ellt_cluster["DBClusterIdentifier"])
        ellt_rds_cluster.extend([ellt_cluster["DBClusterIdentifier"]])

    print("1. 제거안함")
    print("2. 인스턴스제거")
    remove_menu=InputNumber(1,2)

    if remove_menu==2 :
        print("B2 RDS 제거")
        b2_remove_rds=getRemoveList(b2_rds_cluster)
        print("ellt RDS 제거")
        ellt_remove_rds=getRemoveList(ellt_rds_cluster)

        for b2_remove in b2_remove_rds:
            b2_rds_cluster.remove(b2_remove)

        for ellt_remove in ellt_remove_rds:
            ellt_rds_cluster.remove(ellt_remove)  

    b2_rds_instance = []
    for b2_cluster in b2_rds_cluster_list["DBClusters"]:
        for b2_cluster_target in b2_rds_cluster:
            if b2_cluster["DBClusterIdentifier"] ==  b2_cluster_target:
                for b2_member in b2_cluster["DBClusterMembers"]:
                    print(b2_member["DBInstanceIdentifier"])
                    b2_rds_instance.extend([b2_member["DBInstanceIdentifier"]])


    ellt_rds_instance = []
    for ellt_cluster in ellt_rds_cluster_list["DBClusters"]:
        for ellt_cluster_target in ellt_rds_cluster:
            if ellt_cluster["DBClusterIdentifier"] ==  ellt_cluster_target:
                for ellt_member in ellt_cluster["DBClusterMembers"]:
                    print(ellt_member["DBInstanceIdentifier"])
                    ellt_rds_instance.extend([ellt_member["DBInstanceIdentifier"]])

    

    if cluster_flag == 1:
        aws_command="aws --profile %s rds modify-db-cluster --db-cluster-identifier %s %s" 
        print("############ CLUSTER ###################")
        for b2_rds in b2_rds_cluster:
            print("######## " + b2_rds + " #######")
            print(aws_command%(b2_profile,b2_rds,next_line_continue))
            for modify in modify_config["cluster"][0]:
                if (str(modify_config["cluster"][0][modify]) != "" and "|" not in modify):
                    print(modify + " " + str(modify_config["cluster"][0][modify]) + " " + next_line_continue)
                elif (str(modify_config["cluster"][0][modify]) != "" and "|" in modify):
                    print(str(modify_config["cluster"][0][modify]) +" " + next_line_continue)
        
        for ellt_rds in ellt_rds_cluster:
            print("######## " + ellt_rds + " #######")
            print(aws_command%(ellt_profile,ellt_rds,next_line_continue))
            for modify in modify_config["cluster"][0]:
                if (str(modify_config["cluster"][0][modify]) != "" and "|" not in modify):
                    print(modify + " " + str(modify_config["cluster"][0][modify]) + " " + next_line_continue)
                elif (str(modify_config["cluster"][0][modify]) != "" and "|" in modify):
                    print(str(modify_config["cluster"][0][modify]) +" " + next_line_continue)

    if instance_flag == 1:
        aws_command="aws --profile %s rds modify-db-instance --db-instance-identifier %s %s" 
        print("############ INSTANCE ###################")
        for b2_rds in b2_rds_instance:
            print("######## " + b2_rds + " #######")
            print(aws_command%(b2_profile,b2_rds,next_line_continue))
            for modify in modify_config["instance"][0]:
                if (str(modify_config["instance"][0][modify]) != "" and "|" not in modify):
                    print(modify + " " + str(modify_config["instance"][0][modify]) + " " + next_line_continue)
                elif (str(modify_config["instance"][0][modify]) != "" and "|" in modify):
                    print(str(modify_config["instance"][0][modify]) +" " + next_line_continue)
        
        for ellt_rds in ellt_rds_instance:
            print("######## " + ellt_rds + " #######")
            print(aws_command%(ellt_profile,ellt_rds,next_line_continue))
            for modify in modify_config["instance"][0]:
                if (str(modify_config["instance"][0][modify]) != "" and "|" not in modify):
                    print(modify + " " + str(modify_config["instance"][0][modify]) + " " + next_line_continue)
                elif (str(modify_config["instance"][0][modify]) != "" and "|" in modify):
                    print(str(modify_config["instance"][0][modify]) +" " + next_line_continue)

        
    if pending_flag == 1:
        aws_command="aws --profile %s rds apply-pending-maintenance-action %s\n--resource-identifier %s %s" 
        print("############ PENDING ACTION ###################")
        for b2_rds in b2_rds_cluster:
            for b2_cluster in b2_rds_cluster_list["DBClusters"]:
                if b2_rds == b2_cluster["DBClusterIdentifier"]:
                    print("#############" + b2_cluster["DBClusterIdentifier"] + "#############")
                    print(aws_command%(b2_profile,next_line_continue,b2_cluster["DBClusterArn"],next_line_continue))
                    for modify in modify_config["pending-maintenance"][0]:
                        if (str(modify_config["pending-maintenance"][0][modify]) != "" and "|" not in modify):
                            print(modify + " " + str(modify_config["pending-maintenance"][0][modify]) + " " + next_line_continue)
                        elif (str(modify_config["pending-maintenance"][0][modify]) != "" and "|" in modify):
                            print(str(modify_config["pending-maintenance"][0][modify]) +" " + next_line_continue)

        for ellt_rds in ellt_rds_cluster:
            for ellt_cluster in ellt_rds_cluster_list["DBClusters"]:
                if ellt_rds == ellt_cluster["DBClusterIdentifier"]:
                    print("#############" + ellt_cluster["DBClusterIdentifier"] + "#############")
                    print(aws_command%(ellt_profile,next_line_continue,ellt_cluster["DBClusterArn"],next_line_continue))
                    for modify in modify_config["pending-maintenance"][0]:
                        if (str(modify_config["pending-maintenance"][0][modify]) != "" and "|" not in modify):
                            print(modify + " " + str(modify_config["pending-maintenance"][0][modify]) + " " + next_line_continue)
                        elif (str(modify_config["pending-maintenance"][0][modify]) != "" and "|" in modify):
                            print(str(modify_config["pending-maintenance"][0][modify]) +" " + next_line_continue)

    if restore_flag == 1:
        print("############ RESTORE ###################")
        
        aws_command="aws --profile %s rds restore-db-cluster-to-point-in-time --source-db-cluster-identifier %s -db-cluster-identifier %s %s"
        
        for b2_rds in b2_rds_cluster:
            for b2_cluster in b2_rds_cluster_list["DBClusters"]:
                if b2_rds == b2_cluster["DBClusterIdentifier"]:
                    print("######## " + b2_rds + " #######")
                    
                    db_cluster_identifier = b2_rds + "-" + str(len(b2_cluster["DBClusterMembers"]))
                    print(aws_command%(b2_profile,b2_rds,db_cluster_identifier,next_line_continue))

                    for modify in modify_config["restore-db"][0]:
                        if (str(modify_config["restore-db"][0][modify]) != "" and "|" not in modify):
                            print(modify + " " + str(modify_config["restore-db"][0][modify]) + " " + next_line_continue)
                        elif (str(modify_config["restore-db"][0][modify]) != "" and "|" in modify):
                            print(str(modify_config["restore-db"][0][modify]) +" " + next_line_continue)

        for ellt_rds in ellt_rds_cluster:
            for ellt_cluster in ellt_rds_cluster_list["DBClusters"]:
                if ellt_rds == ellt_cluster["DBClusterIdentifier"]:
                    print("######## " + ellt_rds + " #######")
                    
                    db_cluster_identifier = ellt_rds + "-" + str(len(ellt_cluster["DBClusterMembers"]))
                    print(aws_command%(ellt_profile,ellt_rds,db_cluster_identifier,next_line_continue))

                    for modify in modify_config["restore-db"][0]:
                        if (str(modify_config["restore-db"][0][modify]) != "" and "|" not in modify):
                            print(modify + " " + str(modify_config["restore-db"][0][modify]) + " " + next_line_continue)
                        elif (str(modify_config["restore-db"][0][modify]) != "" and "|" in modify):
                            print(str(modify_config["restore-db"][0][modify]) +" " + next_line_continue)
        