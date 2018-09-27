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

    
    alarm_config={
                    "ELLT_SNS_TOPIC":"rds_cw_alarm", #SNS그룹
                    "B2_SNS_TOPIC":"rds_cw_alarm", #SNS그룹
                    "Configure":
                    [
                        {
                            "postfix":"-Over-CPU-Utilization",
                            "metric_name":"CPUUtilization",
                            "threshold":"60",#Percent
                            "period":"300",
                            "statistic":"Maximum",
                            "comparison_operator":"GreaterThanOrEqualToThreshold",
                            "unit":"Percent",
                            "evaluation_periods":"1"
                        },
                        {
                            "postfix":"-Low-FreeableMemory",
                            "metric_name":"FreeableMemory",
                            "threshold":"3221225472",#byte (104857600, 100MB, 1073741824 1G)
                            "period":"300",
                            "statistic":"Minimum",
                            "comparison_operator":"LessThanOrEqualToThreshold",
                            "unit":"Bytes",
                            "evaluation_periods":"1"
                        },
                        {
                            "postfix":"-Low-DB-Connections",
                            "metric_name":"DatabaseConnections",
                            "threshold":"100",#connect count
                            "period":"300",
                            "statistic":"Minimum",
                            "comparison_operator":"LessThanOrEqualToThreshold",
                            "unit":"Count",
                            "evaluation_periods":"1"
                        },
                        {
                            "postfix":"-Over-DB-Connections",
                            "metric_name":"DatabaseConnections",
                            "threshold":"2000",#connect count
                            "period":"300",
                            "statistic":"Maximum",
                            "comparison_operator":"GreaterThanOrEqualToThreshold",
                            "unit":"Count",
                            "evaluation_periods":"1"
                        },
                        {
                            "postfix":"-Low-FreeLocalStorage",
                            "metric_name":"FreeLocalStorage",
                            "threshold":"2147483648",#Bytes(1073741824, 1GB)
                            "period":"300",
                            "statistic":"Minimum",
                            "comparison_operator":"LessThanOrEqualToThreshold",
                            "unit":"Bytes",
                            "evaluation_periods":"1"
                        }
                    ]
                }

    
    
    print("1. PRD")
    print("2. TEST")
    print("3. DEV")
    print("4. 종료")
    #env_menu=InputNumber(1,4)
    env_menu=1
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

    result=subprocess.Popen("aws --profile "+ ellt_profile +" rds describe-db-instances",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    ellt_rds_list=json.loads(result)

    result=subprocess.Popen("aws --profile "+ b2_profile +" rds describe-db-instances",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    b2_rds_list=json.loads(result)

    result=subprocess.Popen("aws --profile "+ ellt_profile +" sns list-topics",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    ellt_topic_list=json.loads(result)

    result=subprocess.Popen("aws --profile "+ b2_profile +" sns list-topics",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    b2_topic_list=json.loads(result)

    exists_topic=0
    
    for ellt_topic in ellt_topic_list["Topics"]:
        #print(ellt_topic["TopicArn"])
        if ":"+ alarm_config["ELLT_SNS_TOPIC"] in ellt_topic["TopicArn"]:
            ellt_alarm_actions_arn=ellt_topic["TopicArn"]
            #print(ellt_alarm_actions_arn)
            exists_topic=1
            break
    
    if(exists_topic==0):
        for ellt_topic in ellt_topic_list["Topics"]:
            print(ellt_topic)
        print("ELLT SNS 없음")
        sys.exit()
    
    exists_topic=0
    
    for b2_topic in b2_topic_list["Topics"]:
        #print(ellt_topic["TopicArn"])
        if ":"+ alarm_config["B2_SNS_TOPIC"] in b2_topic["TopicArn"]:
            b2_alarm_actions_arn=b2_topic["TopicArn"]
            #print(ellt_alarm_actions_arn)
            exists_topic=1
            break
    
    if(exists_topic==0):
        for b2_topic in b2_topic_list["Topics"]:
            print(b2_topic)
        print("B2 SNS 없음")
        sys.exit()


    print(ellt_alarm_actions_arn+","+b2_alarm_actions_arn)
    b2_rds_instance=[]
    for b2_instance in b2_rds_list["DBInstances"]:
        print(b2_instance["DBInstanceIdentifier"])
        b2_rds_instance.extend([b2_instance["DBInstanceIdentifier"]])

    

    ellt_rds_instance=[]
    for ellt_instance in ellt_rds_list["DBInstances"]:
        print(ellt_instance["DBInstanceIdentifier"])
        ellt_rds_instance.extend([ellt_instance["DBInstanceIdentifier"]])

    print("1. 제거안함")
    print("2. 인스턴스제거")
    #remove_menu=InputNumber(1,2)
    remove_menu=1
    if remove_menu==2 :
        print("B2 RDS 제거")
        b2_remove_rds=getRemoveList(b2_rds_instance)
        print("ellt RDS 제거")
        ellt_remove_rds=getRemoveList(ellt_rds_instance)

        for b2_remove in b2_remove_rds:
            b2_rds_instance.remove(b2_remove)

        for ellt_remove in ellt_remove_rds:
            ellt_rds_instance.remove(ellt_remove)    

        print("###### config 대상 ###########")

    alarm_command="aws --profile %s cloudwatch put-metric-alarm --alarm-name %s --alarm-description \"%s\" "
    alarm_command=alarm_command+ "--metric-name %s --namespace AWS/RDS --statistic %s  --period %s  --threshold %s "
    alarm_command=alarm_command+ "--comparison-operator %s --dimensions Name=DBInstanceIdentifier,Value=%s --evaluation-periods %s "
    alarm_command=alarm_command+ "--alarm-actions %s --unit %s"

    print("########## B2 RDS ###########")
    for b2_rds in b2_rds_instance:
        for alarm_config_det in alarm_config["Configure"]:
            alarm_name="RDS-"+ b2_rds + alarm_config_det["postfix"]
            print("####################"+alarm_name+"#######################")
            print(alarm_command%(b2_profile,alarm_name,alarm_name,alarm_config_det["metric_name"]
                                ,alarm_config_det["statistic"],alarm_config_det["period"],alarm_config_det["threshold"]
                                ,alarm_config_det["comparison_operator"],b2_rds,alarm_config_det["evaluation_periods"]
                                ,b2_alarm_actions_arn,alarm_config_det["unit"])
                 )
            
    
    print("########## Ellt RDS ###########")
    for ellt_rds in ellt_rds_instance:
        for alarm_config_det in alarm_config["Configure"]:
            alarm_name="RDS-"+ ellt_rds + alarm_config_det["postfix"]
            print("####################"+alarm_name+"#######################")
            print(alarm_command%(ellt_profile,alarm_name,alarm_name,alarm_config_det["metric_name"]
                                ,alarm_config_det["statistic"],alarm_config_det["period"],alarm_config_det["threshold"]
                                ,alarm_config_det["comparison_operator"],ellt_rds,alarm_config_det["evaluation_periods"]
                                ,ellt_alarm_actions_arn,alarm_config_det["unit"])
                 )


    
    result=subprocess.Popen("aws --profile "+ ellt_profile +" cloudwatch describe-alarms",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    ellt_alarm_list=json.loads(result)

    result=subprocess.Popen("aws --profile "+ b2_profile +" cloudwatch describe-alarms",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    b2_alarm_list=json.loads(result)

    print("######## ELLT Exists Alarm List ##############")
    for ellt_alarm in ellt_alarm_list["MetricAlarms"]:
        if ellt_alarm["Namespace"] == "AWS/RDS":
            print(ellt_alarm["Dimensions"])
            print(ellt_alarm["AlarmName"])
            print(ellt_alarm["MetricName"])
            print("aws --profile %s cloudwatch delete-alarms --alarm-names %s"%(ellt_profile,ellt_alarm["AlarmName"]))
    
    print("######## B2 Exists Alarm List ##############")
    for b2_alarm in b2_alarm_list["MetricAlarms"]:
        if b2_alarm["Namespace"] == "AWS/RDS":
            print(b2_alarm["Dimensions"])
            print(b2_alarm["AlarmName"])
            print(b2_alarm["MetricName"])
            print("aws --profile %s cloudwatch delete-alarms --alarm-names %s"%(b2_profile,b2_alarm["AlarmName"]))