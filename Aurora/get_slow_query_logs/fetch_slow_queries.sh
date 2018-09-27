#!/bin/bash

set -ex

instanceID=$1
profileID=$2
date=$(date +%Y-%m-%d)

function downloadLog () {
  local log=$1

  aws rds download-db-log-file-portion \
    --profile $profileID \
    --output text \
    --db-instance-identifier $instanceID \
    --starting-token 0 \
    --log-file-name $log
}

downloadLog slowquery/mysql-slowquery.log > slow-$instanceID-$date.log

for i in $(seq 0 23); do
  downloadLog slowquery/mysql-slowquery.log.$3.`printf "%02d" "$i"` >> slow-$instanceID-$3.log
done

zip -r slow-$instanceID-$date.log.zip slow-$instanceID-$date.log
