#!/bin/bash
# Launch grid workers from the lsbench worker AMI in us-east-1: one p5.4xlarge (H100) if any AZ has capacity, then
# g6.2xlarge (L4) boxes up to N_L4. Prints "instance_id type az" per launched worker to infra/grid/workers.txt.
#   infra/grid/launch_workers.sh <ami-id> <n_l4>
set -u
AMI=$1; N_L4=${2:-3}; R=us-east-1; VPC=vpc-0821ce817c411c1bb; SG=sg-063eb383597b39d48
OUT=$(dirname "$0")/workers.txt
launch() {  # type az name -> instance id or empty
  local subnet
  subnet=$(aws ec2 describe-subnets --region $R --filters Name=vpc-id,Values=$VPC Name=availability-zone,Values=$2 \
           --query 'Subnets[0].SubnetId' --output text)
  [ "$subnet" = "None" ] && return
  aws ec2 run-instances --region $R --image-id "$AMI" --instance-type "$1" --key-name warply-gpu \
    --security-group-ids $SG --subnet-id "$subnet" \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$3},{Key=project,Value=lso}]" \
    --query 'Instances[0].InstanceId' --output text 2>/tmp/lsb_launch_err || true
}
azs() { aws ec2 describe-instance-type-offerings --region $R --location-type availability-zone \
          --filters Name=instance-type,Values=$1 --query 'InstanceTypeOfferings[].Location' --output text; }
h100=""
for az in $(azs p5.4xlarge); do
  id=$(launch p5.4xlarge "$az" lsbench-h100)
  if [[ "$id" == i-* ]]; then h100=$id; echo "$id p5.4xlarge $az" | tee -a "$OUT"; break; fi
  echo "p5.4xlarge $az: $(grep -o 'InsufficientInstanceCapacity\|VcpuLimitExceeded\|Unsupported' /tmp/lsb_launch_err | head -1)"
done
[ -n "$h100" ] && N_L4=$((N_L4 - 1))  # the H100 takes one of the worker shares
n=0
for round in 1 2 3; do
  for az in $(azs g6.2xlarge); do
    [ $n -ge "$N_L4" ] && break 2
    id=$(launch g6.2xlarge "$az" lsbench-l4)
    if [[ "$id" == i-* ]]; then n=$((n + 1)); echo "$id g6.2xlarge $az" | tee -a "$OUT"
    else echo "g6.2xlarge $az: $(grep -o 'InsufficientInstanceCapacity\|VcpuLimitExceeded' /tmp/lsb_launch_err | head -1)"; fi
  done
  [ $n -ge "$N_L4" ] || sleep 60
done
echo "launched: h100=${h100:-none} l4=$n"
