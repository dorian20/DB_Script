sysbench --db-driver=mysql --mysql-host=jmkltcm2.cluster-c0xgcmsoxdvu.ap-northeast-2.rds.amazonaws.com --mysql-port=3306 \
--mysql-user=b2_dba --mysql-db=ltcmstdev --mysql-password=qwer1234 --threads=$1 --time=$2 \
/home/b2-dba/DB_Script/Aurora/get_slow_query_logs/sysbench_lua/my_read.lua run
