#!/bin/bash
# Retry launching an LSO GPU instance across regions/AZs until capacity appears.
# Each attempt tries every instance type (in priority order) in every AZ of every region before sleeping.
# Usage: infra/launch_retry.sh <comma-separated types> <max-attempts> <sleep-seconds>
#   e.g. infra/launch_retry.sh g6e.xlarge,g6.2xlarge,g5.2xlarge,g6.xlarge,g5.xlarge 24 300
# On success writes "<instance-id> <type> <az>" to infra/instance_<type>.txt and exits 0.
# Env: VOL (root volume GB, default 200), NAME (instance Name tag, default lso-gpu),
#      REGIONS (space-separated, default "us-east-1"; each needs an entry in the table below).
# On success also writes "<region> <ip-file key>" to infra/instance_<type>.txt; ssh key: ~/.ssh/<KEYFILE[region]>.
set -u
TYPES=${1:-g6e.xlarge}; MAX=${2:-24}; SLEEP=${3:-300}; VOL=${VOL:-200}; NAME=${NAME:-lso-gpu}
REGIONS=${REGIONS:-us-east-1}
cd "$(dirname "$0")/.."
# Per region: DLAMI "Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.12 (Ubuntu 24.04) 20261102", default VPC,
# SSH security group warply-gpu-ssh, key pair name and local key file.
cfg() {  # cfg <region> -> "AMI VPC SG KEYFILE"   (plain function: macOS /bin/bash 3.2 has no associative arrays)
  case $1 in
    us-east-1)  echo ami-03f629219d17f1cc0 vpc-0821ce817c411c1bb sg-063eb383597b39d48 warply-gpu-us-east-1.pem ;;
    us-east-2)  echo ami-0e552322d1dd56de0 vpc-06881b0c466976323 sg-0ac977503bdd46463 warply-gpu-us-east-2.pem ;;
    us-west-2)  echo ami-052d4203797b42569 vpc-091815783621a3dbd sg-0e560435701f939e2 warply-gpu-us-west-2.pem ;;
    eu-north-1) echo ami-0d168f6b812f15806 vpc-0e96cb22f573ecaba sg-04c99aee22e2e0c6e warply-gpu-eu-north-1.pem ;;
    *) echo "no config for region $1" >&2; exit 2 ;;
  esac
}
IFS=',' read -ra TYPE_LIST <<< "$TYPES"
for attempt in $(seq 1 "$MAX"); do
  for type in "${TYPE_LIST[@]}"; do
   for region in $REGIONS; do
    read -r ami vpc sg keyfile <<< "$(cfg $region)"
    azs=$(aws ec2 describe-instance-type-offerings --region $region --location-type availability-zone \
      --filters Name=instance-type,Values=$type --query "InstanceTypeOfferings[].Location" --output text)
    for az in $azs; do
      subnet=$(aws ec2 describe-subnets --region $region --filters Name=vpc-id,Values=$vpc \
        Name=availability-zone,Values=$az Name=default-for-az,Values=true --query "Subnets[0].SubnetId" --output text)
      [ "$subnet" = "None" ] && continue
      out=$(aws ec2 run-instances --region $region --image-id $ami --instance-type "$type" \
        --key-name warply-gpu --security-group-ids $sg --subnet-id "$subnet" \
        --block-device-mappings "DeviceName=/dev/sda1,Ebs={VolumeSize=$VOL,VolumeType=gp3,DeleteOnTermination=true}" \
        --instance-initiated-shutdown-behavior stop --user-data file://infra/user-data.sh \
        --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$NAME},{Key=project,Value=lso}]" \
          "ResourceType=volume,Tags=[{Key=Name,Value=$NAME-root},{Key=project,Value=lso}]" \
        --query "Instances[0].InstanceId" --output text 2>&1)
      if [[ "$out" == i-* ]]; then
        echo "$out $type $az $region $keyfile" > "infra/instance_${type}.txt"
        echo "$(date -u +%FT%TZ) LAUNCHED $type $out in $az (attempt $attempt)"
        exit 0
      fi
      reason=$(echo "$out" | grep -o 'InsufficientInstanceCapacity\|Unsupported\|VcpuLimitExceeded\|InvalidParameter[A-Za-z]*' | head -1)
      echo "$(date -u +%FT%TZ) attempt $attempt $type $az: ${reason:-$(echo "$out" | tail -1 | cut -c1-120)}"
      [ "$reason" = VcpuLimitExceeded ] && break  # no quota in this region: skip its other AZs
    done
   done
  done
  [ "$attempt" -lt "$MAX" ] && sleep "$SLEEP"
done
echo "$(date -u +%FT%TZ) GAVE UP after $MAX attempts"
exit 1
