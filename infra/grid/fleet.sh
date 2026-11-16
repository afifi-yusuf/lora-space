#!/bin/bash
# Grid fleet control (run from the Mac). Registry: infra/grid/workers.txt  "<id> <type> <region>"
#   fleet.sh l4                 launch L4 boxes (L4_TYPE, default g6.xlarge: 4 vCPU = most GPUs per G vCPU quota) in
#                               us-east-1 until the quota is full; set each up, then rebalance
#   fleet.sh h100 [hours]       hunt p5.4xlarge (1 per region with P quota) every 5 min; set each up, then rebalance
#   fleet.sh setup <id> <region> <listfile>   start a worker on a new box with that run list
#   fleet.sh rebalance          pool every worker's remaining runs and redistribute (an H100 counts as 2 slots)
#   fleet.sh status             each worker's last log lines and remaining list
set -u
cd "$(dirname "$0")"
REG=workers.txt; touch $REG
SRC_AMI=ami-00618b5dbb3dec5f6
cfg() {  # region -> "VPC SG KEYFILE"
  case $1 in
    us-east-1)  echo vpc-0821ce817c411c1bb sg-063eb383597b39d48 warply-gpu-us-east-1.pem ;;
    us-east-2)  echo vpc-06881b0c466976323 sg-0ac977503bdd46463 warply-gpu-us-east-2.pem ;;
    us-west-2)  echo vpc-091815783621a3dbd sg-0e560435701f939e2 warply-gpu-us-west-2.pem ;;
    eu-north-1) echo vpc-0e96cb22f573ecaba sg-04c99aee22e2e0c6e warply-gpu-eu-north-1.pem ;;
  esac
}
ami() {  # region -> available worker AMI id or empty (copies are recorded in amis.txt)
  local id
  if [ "$1" = us-east-1 ]; then id=$SRC_AMI; else id=$(awk -v r=$1 '$1==r{print $2}' amis.txt 2>/dev/null); fi
  [ -z "$id" ] && return
  [ "$(aws ec2 describe-images --region $1 --image-ids $id --query 'Images[0].State' --output text 2>/dev/null)" = available ] && echo $id
}
ip_of() { aws ec2 describe-instances --region $2 --instance-ids $1 --query 'Reservations[0].Instances[0].PublicIpAddress' --output text; }
key_of() { read -r _ _ k <<< "$(cfg $1)"; echo ~/.ssh/$k; }
ssh_w() {  # id region cmd...
  local id=$1 r=$2; shift 2
  ssh -o StrictHostKeyChecking=no -o ConnectTimeout=15 -o BatchMode=yes -i "$(key_of $r)" ubuntu@"$(ip_of $id $r)" "$@"
}
allow_me() {  # region: open SSH to this Mac's current IP
  read -r _ sg _ <<< "$(cfg $1)"
  aws ec2 authorize-security-group-ingress --region $1 --group-id $sg --protocol tcp --port 22 \
    --cidr "$(curl -s https://checkip.amazonaws.com)/32" >/dev/null 2>&1 || true
}
launch() {  # type region az -> id or empty; reason in /tmp/lsb_launch_err.$$
  read -r vpc sg _ <<< "$(cfg $2)"
  local subnet a
  a=$(ami $2); [ -z "$a" ] && { echo NoAMI > /tmp/lsb_launch_err.$$; return; }
  subnet=$(aws ec2 describe-subnets --region $2 --filters Name=vpc-id,Values=$vpc Name=availability-zone,Values=$3 \
           Name=default-for-az,Values=true --query 'Subnets[0].SubnetId' --output text)
  [ "$subnet" = None ] && { echo NoSubnet > /tmp/lsb_launch_err.$$; return; }
  aws ec2 run-instances --region $2 --image-id $a --instance-type $1 --key-name warply-gpu --security-group-ids $sg \
    --subnet-id $subnet --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=lsbench-$1},{Key=project,Value=lso}]" \
    --query 'Instances[0].InstanceId' --output text 2>/tmp/lsb_launch_err.$$ || true
}
reason() { grep -o 'InsufficientInstanceCapacity\|VcpuLimitExceeded\|Unsupported\|NoAMI\|NoSubnet\|InvalidAMIID[.A-Za-z]*' /tmp/lsb_launch_err.$$ | head -1; }
azs() { aws ec2 describe-instance-type-offerings --region $2 --location-type availability-zone \
          --filters Name=instance-type,Values=$1 --query 'InstanceTypeOfferings[].Location' --output text; }
log() { echo "$(date -u +%FT%TZ) $*"; }

setup() {  # id region listfile
  local id=$1 r=$2 list=$3 ip
  aws ec2 wait instance-status-ok --region $r --instance-ids $id
  allow_me $r; ip=$(ip_of $id $r)
  for i in $(seq 30); do ssh_w $id $r true 2>/dev/null && break; sleep 10; done
  scp -o StrictHostKeyChecking=no -i "$(key_of $r)" grid_worker.sh ubuntu@$ip:/home/ubuntu/lsb_grid_worker.sh
  scp -o StrictHostKeyChecking=no -i "$(key_of $r)" "$list" ubuntu@$ip:/home/ubuntu/lsb_grid_list.txt
  # small boxes (16 GB RAM): add swap so a scoring-time memory spike cannot OOM-kill a run
  ssh_w $id $r '[ $(free -g | awk "/Mem:/{print \$2}") -lt 20 ] && ! swapon --show | grep -q . && sudo fallocate -l 16G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile >/dev/null && sudo swapon /swapfile; free -g | tail -1'
  ssh_w $id $r 'chmod +x ~/lsb_grid_worker.sh; nohup setsid ~/lsb_grid_worker.sh >/dev/null 2>&1 < /dev/null & sleep 2; tail -1 ~/lsb_grid.log'
  log "SETUP $id $r ($ip) list=$list"
}

cmd_l4() {
  until [ -n "$(ami us-east-1)" ]; do sleep 60; done
  local lists=(w2.txt w3.txt w4.txt) n=0 full="" T=${L4_TYPE:-g6.xlarge}
  for round in $(seq 1 30); do
    for az in $(azs $T us-east-1); do
      id=$(launch $T us-east-1 $az)
      if [[ "$id" == i-* ]]; then
        echo "$id $T us-east-1" >> $REG; log "LAUNCHED $id $T $az"
        l=${lists[$n]:-empty.txt}; touch empty.txt; n=$((n + 1))
        setup $id us-east-1 $l &
      else
        r=$(reason); log "$T $az: ${r:-$(tail -1 /tmp/lsb_launch_err.$$)}"
        [ "$r" = VcpuLimitExceeded ] && { full=1; break 2; }
      fi
    done
    sleep 120
  done
  wait; log "L4 DONE launched=$n quota_full=${full:-no}"
  "$0" rebalance
}

cmd_h100() {
  local hours=${1:-6} end=$(( $(date +%s) + ${1:-6} * 3600 ))
  while [ $(date +%s) -lt $end ]; do
    if [ -n "$(ami us-east-1)" ]; then  # copy the worker AMI to the other P-quota regions once it exists
      for r in us-east-2 us-west-2 eu-north-1; do
        grep -q "^$r " amis.txt 2>/dev/null && continue
        id=$(aws ec2 copy-image --region $r --source-region us-east-1 --source-image-id $SRC_AMI --name lsbench-worker \
             --query ImageId --output text) && echo "$r $id" >> amis.txt && log "AMI COPY $r $id"
      done
    fi
    for r in us-east-1 us-east-2 us-west-2 eu-north-1; do
      grep -q "p5.4xlarge $r" $REG && continue  # 16 vCPU quota per region = one H100
      for az in $(azs p5.4xlarge $r); do
        id=$(launch p5.4xlarge $r $az)
        if [[ "$id" == i-* ]]; then
          echo "$id p5.4xlarge $r" >> $REG; log "LAUNCHED H100 $id $r $az"
          touch empty.txt; ( setup $id $r empty.txt && "$0" rebalance ) &
          break
        fi
        rr=$(reason); [ "$rr" != InsufficientInstanceCapacity ] && log "p5.4xlarge $r $az: ${rr:-$(tail -1 /tmp/lsb_launch_err.$$)}"
        [ "$rr" = VcpuLimitExceeded ] || [ "$rr" = NoAMI ] && break
      done
    done
    [ "$(grep -c p5.4xlarge $REG)" -ge 4 ] && break
    sleep 300
  done
  wait; log "H100 HUNT END: $(grep -c p5.4xlarge $REG) launched"
}

cmd_rebalance() {
  until mkdir /tmp/lsb_rebalance.lock 2>/dev/null; do sleep 5; done
  local pool=rebalance_$(date -u +%Y%m%dT%H%M%S).txt ids=() regs=() w=()  # pool kept for recovery
  while read -r id type r <&3; do  # fd 3: ssh in the loop would otherwise eat the registry from stdin
    st=$(aws ec2 describe-instances --region $r --instance-ids $id --query 'Reservations[0].Instances[0].State.Name' --output text)
    [ "$st" = running ] || continue
    busy=$(ssh_w $id $r 'pgrep -f "[l]sbench run" >/dev/null && echo 1 || echo 0') || continue
    ssh_w $id $r 'flock ~/lsb_grid_list.lock -c "cat ~/lsb_grid_list.txt; : > ~/lsb_grid_list.txt"' >> $pool || continue
    # idle boxes go first in the dealing order, so the next runs start now rather than after a running session
    if [ "$busy" = 0 ]; then ids=($id "${ids[@]}"); regs=($r "${regs[@]}"); [ $type = p5.4xlarge ] && w=(2 "${w[@]}") || w=(1 "${w[@]}")
    else ids+=($id); regs+=($r); [ $type = p5.4xlarge ] && w+=(2) || w+=(1); fi
  done 3< $REG
  # deal runs in order: H100s get two per round
  local i=0 k
  declare -a out; for k in "${!ids[@]}"; do out[$k]=""; done
  slots=(); for k in "${!ids[@]}"; do for j in $(seq ${w[$k]}); do slots+=($k); done; done
  while read -r line; do
    [ -z "$line" ] && continue
    k=${slots[$((i % ${#slots[@]}))]}; out[$k]+="$line"$'\n'; i=$((i + 1))
  done < $pool
  for k in "${!ids[@]}"; do
    printf '%s' "${out[$k]}" | ssh_w ${ids[$k]} ${regs[$k]} 'flock ~/lsb_grid_list.lock -c "cat >> ~/lsb_grid_list.txt"'
    log "REBALANCE ${ids[$k]} gets $(printf '%s' "${out[$k]}" | grep -c .) runs"
  done
  rmdir /tmp/lsb_rebalance.lock
}

cmd_status() {
  while read -r id type r <&3; do
    echo "== $id $type $r"
    ssh_w $id $r 'tail -2 ~/lsb_grid.log; echo "remaining: $(grep -c . ~/lsb_grid_list.txt)"' 2>&1 | sed 's/^/   /'
  done 3< $REG
}

c=$1; shift
case $c in
  l4) cmd_l4 ;; h100) cmd_h100 "$@" ;; setup) setup "$@" ;; rebalance) cmd_rebalance ;; status) cmd_status ;;
esac
