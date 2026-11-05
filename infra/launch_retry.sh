#!/bin/bash
# Retry launching an LSO GPU instance across us-east-1 AZs until capacity appears.
# Each attempt tries every instance type (in priority order) in every AZ before sleeping.
# Usage: infra/launch_retry.sh <comma-separated types> <max-attempts> <sleep-seconds>
#   e.g. infra/launch_retry.sh g6e.xlarge,g6.2xlarge,g5.2xlarge,g6.xlarge,g5.xlarge 24 300
# On success writes "<instance-id> <type> <az>" to infra/instance_<type>.txt and exits 0.
# Env: VOL (root volume GB, default 200), NAME (instance Name tag, default lso-gpu).
# Only us-east-1 has GPU quota on this account (G: 8 vCPUs, P: 16 vCPUs; us-east-2 / us-west-2 are 0).
set -u
TYPES=${1:-g6e.xlarge}; MAX=${2:-24}; SLEEP=${3:-300}; VOL=${VOL:-200}; NAME=${NAME:-lso-gpu}
cd "$(dirname "$0")/.."
AMI=ami-03f629219d17f1cc0   # Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.12 (Ubuntu 24.04) 20261102
IFS=',' read -ra TYPE_LIST <<< "$TYPES"
for attempt in $(seq 1 "$MAX"); do
  for type in "${TYPE_LIST[@]}"; do
    for az in us-east-1a us-east-1b us-east-1c us-east-1d us-east-1e us-east-1f; do
      subnet=$(aws ec2 describe-subnets --region us-east-1 --filters Name=vpc-id,Values=vpc-0821ce817c411c1bb \
        Name=availability-zone,Values=$az Name=default-for-az,Values=true --query "Subnets[0].SubnetId" --output text)
      [ "$subnet" = "None" ] && continue
      out=$(aws ec2 run-instances --region us-east-1 --image-id $AMI --instance-type "$type" \
        --key-name warply-gpu --security-group-ids sg-063eb383597b39d48 --subnet-id "$subnet" \
        --block-device-mappings "DeviceName=/dev/sda1,Ebs={VolumeSize=$VOL,VolumeType=gp3,DeleteOnTermination=true}" \
        --instance-initiated-shutdown-behavior stop --user-data file://infra/user-data.sh \
        --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$NAME},{Key=project,Value=lso}]" \
          "ResourceType=volume,Tags=[{Key=Name,Value=$NAME-root},{Key=project,Value=lso}]" \
        --query "Instances[0].InstanceId" --output text 2>&1)
      if [[ "$out" == i-* ]]; then
        echo "$out $type $az" > "infra/instance_${type}.txt"
        echo "$(date -u +%FT%TZ) LAUNCHED $type $out in $az (attempt $attempt)"
        exit 0
      fi
      reason=$(echo "$out" | grep -o 'InsufficientInstanceCapacity\|Unsupported\|VcpuLimitExceeded\|InvalidParameter[A-Za-z]*' | head -1)
      echo "$(date -u +%FT%TZ) attempt $attempt $type $az: ${reason:-$(echo "$out" | tail -1 | cut -c1-120)}"
    done
  done
  [ "$attempt" -lt "$MAX" ] && sleep "$SLEEP"
done
echo "$(date -u +%FT%TZ) GAVE UP after $MAX attempts"
exit 1
