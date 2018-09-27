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
    mon_user = "b2_mon"
    mon_pwd="monDB_2019"

    result=subprocess.Popen("aws --profile "+ ellt_profile +" rds describe-db-instances",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    ellt_rds_list=json.loads(result)

    result=subprocess.Popen("aws --profile "+ b2_profile +" rds describe-db-instances",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    b2_rds_list=json.loads(result)

    result=subprocess.Popen("aws --profile "+ ellt_profile +" elasticache describe-cache-clusters",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    ellt_ec_list=json.loads(result)

    result=subprocess.Popen("aws --profile "+ b2_profile +" elasticache describe-cache-clusters",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    b2_ec_list=json.loads(result)



    b2_rds_instance=[]
    for b2_instance in b2_rds_list["DBInstances"]:
        print(b2_instance["DBInstanceIdentifier"])
        b2_rds_instance.extend([b2_instance["DBInstanceIdentifier"]])

    

    ellt_rds_instance=[]
    for ellt_instance in ellt_rds_list["DBInstances"]:
        print(ellt_instance["DBInstanceIdentifier"])
        ellt_rds_instance.extend([ellt_instance["DBInstanceIdentifier"]])

    b2_ec_instance=[]
    for b2_instance in b2_ec_list["CacheClusters"]:
        print(b2_instance["CacheClusterId"])
        b2_ec_instance.extend([b2_instance["CacheClusterId"]])

    ellt_ec_instance=[]
    for ellt_instance in ellt_ec_list["CacheClusters"]:
        print(ellt_instance["CacheClusterId"])
        ellt_ec_instance.extend([ellt_instance["CacheClusterId"]])


    print("1. 제거안함")
    print("2. 인스턴스제거")
    remove_menu=InputNumber(1,2)

    if remove_menu==2 :
        print("B2 RDS 제거")
        b2_remove_rds=getRemoveList(b2_rds_instance)
        print("ellt RDS 제거")
        ellt_remove_rds=getRemoveList(ellt_rds_instance)
        print("B2 ElastiCache 제거")
        b2_remove_ec=getRemoveList(b2_ec_instance)
        print("ellt ElastiCache 제거")
        ellt_remove_ec=getRemoveList(ellt_ec_instance)

    #if len(b2_remove_rds) >= 1:
        for b2_remove in b2_remove_rds:
            b2_rds_instance.remove(b2_remove)
    #if len(ellt_remove_rds) >= 1:
        for ellt_remove in ellt_remove_rds:
            ellt_rds_instance.remove(ellt_remove)
    #if len(b2_remove_ec) >= 1:
        for b2_remove in b2_remove_ec:
            b2_ec_instance.remove(b2_remove)
    #if len(ellt_remove_ec) >= 1:   
        for ellt_remove in ellt_remove_ec:
            ellt_ec_instance.remove(ellt_remove)

    print("###### config 대상 ###########")

    print("########## B2 RDS ###########")
    for b2_rds in b2_rds_instance:
        print(b2_rds)
    
    print("########## Ellt RDS ###########")
    for ellt_rds in ellt_rds_instance:
        print(ellt_rds)

    print("########## B2 ElastiCache ###########")
    for b2_ec in b2_ec_instance:
        print(b2_ec)

    print("########## Ellt ElastiCache ###########")
    for ellt_ec in ellt_ec_instance:
        print(ellt_ec)


    print("###########################################################")
    print("###########################################################")
    print("###########################################################")
    

    print("# my global config")
    print("global:")
    print("  scrape_interval:     60s # Set the scrape interval to every 15 seconds. Default is every 1 minute.")
    print("  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.")
    print("  # scrape_timeout is set to the global default (10s).")
    print("")
    print("# Alertmanager configuration")
    print("alerting:")
    print("  alertmanagers:")
    print("  - static_configs:")
    print("    - targets:")
    print("      # - alertmanager:9093")
    print("")
    print("# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.")
    print("rule_files:")
    print("  # - \"first_rules.yml\"")
    print("  # - \"second_rules.yml\"")
    print("")
    print("# A scrape configuration containing exactly one endpoint to scrape:")
    print("# Here it's Prometheus itself.")
    print("scrape_configs:")
    print("  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.")
    print("  - job_name: 'prometheus'")
    print("    scrape_interval:   15s")
    print("    # metrics_path defaults to '/metrics'")
    print("    # scheme defaults to 'http'.")
    print("")
    print("    static_configs:")
    print("      - targets: ['localhost:9090']")
    print("")
    print("  - job_name: 'aurora_exporter'")
    print("    scrape_interval:    60s")
    print("    static_configs:")

    port=9105
    for b2_rds in b2_rds_instance:      
        print("      - targets: ['localhost:" + str(port) + "']" )
        print("        labels:")
        print("                alias: \"" + b2_rds + "\"" )
        port=port+1
    for ellt_rds in ellt_rds_instance:
        print("      - targets: ['localhost:" + str(port) + "']" )
        print("        labels:")
        print("                alias: \"" + ellt_rds + "\"" )
        port=port+1


    print("  - job_name: 'cloudwatch_exporter'")
    print("    metrics_path: '/scrape'")
    print("    params:")
    print("      region: [ap-northeast-2]")
    print("    relabel_configs:")
    print("      - source_labels: [alias]")
    print("        target_label: __param_target")
    print("      - source_labels: [task]")
    print("        target_label: __param_task")
    print("    static_configs:")
    for b2_rds in b2_rds_instance:      
        print("        - targets: ['localhost:9042']" )
        print("          labels:")
        print("            alias: \"" + b2_rds + "\"" )
        print("            task: \"rds_cloudwatch\"")
    for b2_ec in b2_ec_instance:
        print("        - targets: ['localhost:9042']" )
        print("          labels:")
        print("            alias: \"" + b2_ec + "\"" )
        print("            task: \"elasticache_cloudwatch\"")  
    for ellt_rds in ellt_rds_instance:
        print("        - targets: ['localhost:9043']" )
        print("          labels:")
        print("            alias: \"" + ellt_rds + "\"" )
        print("            task: \"rds_cloudwatch\"")        
    for ellt_ec in ellt_ec_instance:
        print("        - targets: ['localhost:9043']" )
        print("          labels:")
        print("            alias: \"" + ellt_ec + "\"" )
        print("            task: \"elasticache_cloudwatch\"")        


    print("###########################################################")
    print("###########################################################")
    print("###########################################################")
    print("#"+"docker kill $(docker ps -q)")
    print("#"+"docker rm $(docker ps -a -q)")
    
    port=9105
    for b2_rds in b2_rds_instance:      
        for b2_instance in b2_rds_list["DBInstances"]:
            if b2_rds == b2_instance["DBInstanceIdentifier"]:
                print("docker run -d -p " + str(port) + ":9104 --restart unless-stopped --name mysqld_exporter_"
                      + b2_rds + " -e 'DATA_SOURCE_NAME="+mon_user+":"+mon_pwd+"@(" 
                      + b2_instance["Endpoint"]["Address"] + ":3306)/' mysqld_exporter:0.1")
        port=port+1
    
    for ellt_rds in ellt_rds_instance:      
        for ellt_instance in ellt_rds_list["DBInstances"]:
            if ellt_rds == ellt_instance["DBInstanceIdentifier"]:
                print("docker run -d -p " + str(port) + ":9104 --restart unless-stopped --name mysqld_exporter_"
                      + ellt_rds + " -e 'DATA_SOURCE_NAME="+mon_user+":"+mon_pwd+"@(" 
                      + ellt_instance["Endpoint"]["Address"] + ":3306)/' mysqld_exporter:0.1")
        port=port+1

    print("docker run --name cloudwatch_exporter_ltcm --restart unless-stopped -v ~/.aws/:/root/.aws/ -e AWS_PROFILE='" + b2_profile + "' -d -p 9042:9042 cloudwatch_exporter:0.1")
    print("docker run --name cloudwatch_exporter_ellt --restart unless-stopped -v ~/.aws/:/root/.aws/ -e AWS_PROFILE='" + ellt_profile + "' -d -p 9043:9042 cloudwatch_exporter:0.1")