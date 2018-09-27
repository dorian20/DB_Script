# -*- coding: utf-8 -*-
import sys
import subprocess
import json
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

if __name__=='__main__':

    source_profile=get_input_val("Source AWS Profile")
    target_profile=get_input_val("Target AWS Profile")
    source_cluster_name=get_input_val("Source Cluster Name")
    target_cluster_name=get_input_val("Target Cluster Name")

    result=subprocess.Popen("aws --profile "+ source_profile +" rds describe-db-clusters --db-cluster-identifier "+source_cluster_name,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    source_cluster=json.loads(result)
    result=subprocess.Popen("aws --profile "+ target_profile +" rds describe-db-clusters --db-cluster-identifier "+target_cluster_name,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    target_cluster=json.loads(result)

    result=subprocess.Popen("aws --profile "+ source_profile +" rds describe-db-instances --db-instance-identifier "+source_cluster_name,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    source_instance=json.loads(result)
    result=subprocess.Popen("aws --profile "+ target_profile +" rds describe-db-instances --db-instance-identifier "+target_cluster_name,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    target_instance=json.loads(result)

    source_cluster_parameter=source_cluster["DBClusters"][0]["DBClusterParameterGroup"]
    source_cluster_parameter_stat=source_cluster["DBClusters"][0]["DBClusterMembers"][0]["DBClusterParameterGroupStatus"]
    target_cluster_parameter=target_cluster["DBClusters"][0]["DBClusterParameterGroup"]
    target_cluster_parameter_stat=target_cluster["DBClusters"][0]["DBClusterMembers"][0]["DBClusterParameterGroupStatus"]

    source_parameter=source_instance["DBInstances"][0]["DBParameterGroups"][0]["DBParameterGroupName"]
    source_parameter_stat=source_instance["DBInstances"][0]["DBParameterGroups"][0]["ParameterApplyStatus"]
    target_parameter=target_instance["DBInstances"][0]["DBParameterGroups"][0]["DBParameterGroupName"]
    target_parameter_stat=target_instance["DBInstances"][0]["DBParameterGroups"][0]["ParameterApplyStatus"]

    print("소스클러스터:" + source_cluster_parameter)
    print("소스클러스터 상태:" + source_cluster_parameter_stat)
    print("소스인스턴스:" +source_parameter)
    print("소스인스턴스 상태:" +source_parameter_stat)
    
    print("타겟클러스터:" + target_cluster_parameter)
    print("타겟클러스터 상태:" + target_cluster_parameter_stat)
    print("타겟인스턴스:" +target_parameter)
    print("타겟인스턴스 상태:" +target_parameter_stat)

    result=subprocess.Popen("aws --profile "+ source_profile +" rds describe-db-parameters --db-parameter-group-name "+source_parameter,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    source_parameter_desc=json.loads(result)
    result=subprocess.Popen("aws --profile "+ target_profile +" rds describe-db-parameters --db-parameter-group-name "+target_parameter,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    target_parameter_desc=json.loads(result)

    result=subprocess.Popen("aws --profile "+ source_profile +" rds describe-db-cluster-parameters --db-cluster-parameter-group-name "+source_cluster_parameter,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    source_cluster_parameter_desc=json.loads(result)
    result=subprocess.Popen("aws --profile "+ target_profile +" rds describe-db-cluster-parameters --db-cluster-parameter-group-name "+target_cluster_parameter,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    target_cluster_parameter_desc=json.loads(result)

    #print(source_parameter_desc)
    #print(target_parameter_desc)

    


    for s_param in source_cluster_parameter_desc["Parameters"]:
        for t_param in target_cluster_parameter_desc["Parameters"]:
            if s_param["ParameterName"] == t_param["ParameterName"]:
                if "ParameterValue" in s_param and "ParameterValue" in t_param:
                    if s_param["ParameterValue"] != t_param["ParameterValue"]:
                        print("#################################")
                        print(s_param["ParameterName"]  )
                        print("ApplyMethod :" + s_param["ApplyMethod"]  )
                        print("IsModifiable :" + str(s_param["IsModifiable"])  )
                        print("Description :" + s_param["Description"]  )
                        print("소스파라미터:" + str(s_param["ParameterValue"])  )
                        print("타겟파라미터:" + str(t_param["ParameterValue"])  )

                        print("aws --profile " + target_profile + " rds modify-db-cluster-parameter-group ^")
                        print("--db-cluster-parameter-group-name " + target_parameter + " ^")
                        print("--parameters \"ParameterName=" + str(s_param["ParameterName"]) + ",ParameterValue="+ s_param["ParameterValue"] + ",ApplyMethod=pending-reboot\"")
                elif "ParameterValue" in s_param and "ParameterValue" not in t_param:
                    print("#################################")
                    print(s_param["ParameterName"]  )
                    print("ApplyMethod :" + s_param["ApplyMethod"]  )
                    print("IsModifiable :" + str(s_param["IsModifiable"])  )
                    print("Description :" + s_param["Description"]  )
                    print("소스파라미터:" + s_param["ParameterValue"]  )
                    print("aws --profile " + target_profile + " rds modify-db-cluster-parameter-group ^")
                    print("--db-cluster-parameter-group-name " + target_parameter + " ^")
                    print("--parameters \"ParameterName=" + str(s_param["ParameterName"]) + ",ParameterValue="+ s_param["ParameterValue"] + ",ApplyMethod=pending-reboot\"")
                elif "ParameterValue" not in s_param and "ParameterValue" in t_param:
                    print("#################################")
                    print(s_param["ParameterName"]  )
                    print("ApplyMethod :" + s_param["ApplyMethod"]  )
                    print("IsModifiable :" + str(s_param["IsModifiable"])  )
                    print("Description :" + s_param["Description"]  )
                    print("타겟파라미터:" + t_param["ParameterValue"]  )
                    print("aws --profile " + target_profile + " rds modify-db-cluster-parameter-group ^")
                    print("--db-cluster-parameter-group-name " + target_parameter + " ^")
                    print("--parameters \"ParameterName=" + str(s_param["ParameterName"]) + ",ParameterValue="+ s_param["ParameterValue"] + ",ApplyMethod=pending-reboot\"")

    for s_param in source_parameter_desc["Parameters"]:
        for t_param in target_parameter_desc["Parameters"]:
            if s_param["ParameterName"] == t_param["ParameterName"]:
                if "ParameterValue" in s_param and "ParameterValue" in t_param:
                    if s_param["ParameterValue"] != t_param["ParameterValue"]:
                        print("#################################")
                        print(s_param["ParameterName"]  )
                        print("ApplyType :" + s_param["ApplyType"]  )
                        print("IsModifiable :" + str(s_param["IsModifiable"])  )
                        print("Description :" + s_param["Description"]  )
                        print("소스파라미터:" + str(s_param["ParameterValue"])  )
                        print("타겟파라미터:" + str(t_param["ParameterValue"])  )
                elif "ParameterValue" in s_param and "ParameterValue" not in t_param:
                    print("#################################")
                    print(s_param["ParameterName"]  )
                    print("ApplyType :" + s_param["ApplyType"]  )
                    print("IsModifiable :" + str(s_param["IsModifiable"])  )
                    print("Description :" + s_param["Description"]  )
                    print("소스파라미터:" + str(s_param["ParameterValue"])  )
                elif "ParameterValue" not in s_param and "ParameterValue" in t_param:
                    print("#################################")
                    print(s_param["ParameterName"]  )
                    print("ApplyType :" + s_param["ApplyType"]  )
                    print("IsModifiable :" + str(s_param["IsModifiable"])  )
                    print("Description :" + s_param["Description"]  )
                    print("타겟파라미터:" + str(t_param["ParameterValue"])  )

    
    
    #source_parameter_desc["Parameters"]


