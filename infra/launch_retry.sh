#!/bin/bash
# Retry launching an LSO GPU instance across us-east-1 AZs until capacity appears.
# Usage: infra/launch_retry.sh <instance-type> <max-attempts> <sleep-seconds>
# On success writes the instance id to infra/instance_<type>.txt and exits 0.
set -u
TYPE=${1:-g6e.xlarge}; MAX=${2:-24}; SLEEP=${3:-300}
cd "$(dirname "$0")/.."
AMI=ami-03f629219d17f1cc0
for attempt in $(seq 1 "$MAX"); do
  for az in us-east-1a us-east-1b us-east-1c us-east-1d; do
    subnet=$(aws ec2 describe-subnets --region us-east-1 --filters Name=vpc-id,Values=vpc-0821ce817c411c1bb \
      Name=availability-zone,Values=$az Name=default-for-az,Values=true --query "Subnets[0].SubnetId" --output text)
    out=$(aws ec2 run-instances --region us-east-1 --image-id $AMI --instance-type "$TYPE" \
      --key-name warply-gpu --security-group-ids sg-063eb383597b39d48 --subnet-id "$subnet" \
      --block-device-mappings 'DeviceName=/dev/sda1,Ebs={VolumeSize=200,VolumeType=gp3,DeleteOnTermination=true}' \
      --instance-initiated-shutdown-behavior stop --user-data file://infra/user-data.sh \
      --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=lso-g6e},{Key=project,Value=lso}]' \
        'ResourceType=volume,Tags=[{Key=Name,Value=lso-g6e-root},{Key=project,Value=lso}]' \
      --query "Instances[0].InstanceId" --output text 2>&1)
    if [[ "$out" == i-* ]]; then
      echo "$out" > "infra/instance_${TYPE}.txt"
      echo "$(date -u +%FT%TZ) LAUNCHED $TYPE $out in $az (attempt $attempt)"
      exit 0
    fi
    echo "$(date -u +%FT%TZ) attempt $attempt $az: $(echo "$out" | grep -o 'InsufficientInstanceCapacity\|error.*' | head -1)"
  done
  [ "$attempt" -lt "$MAX" ] && sleep "$SLEEP"
done
echo "$(date -u +%FT%TZ) GAVE UP after $MAX attempts"
exit 1
