#!/bin/bash
# Pull finished run records (result.json present) from every grid worker into results/lsbench/runs/.
# Skips bulky files: sandbox work dirs, traces, vLLM logs, profiler DBs, temp arrays.
cd "$(dirname "$0")/../.."
DST=results/lsbench/runs; mkdir -p $DST
REG=infra/grid/workers_all.txt; [ -f $REG ] || REG=infra/grid/workers.txt
while read -r id type r <&3; do
  st=$(aws ec2 describe-instances --region $r --instance-ids $id --query 'Reservations[0].Instances[0].[State.Name,PublicIpAddress]' --output text)
  read -r state ip <<< "$st"
  [ "$state" = running ] || { echo "$id: $state, skipped"; continue; }
  n=$(ssh -n -o ConnectTimeout=15 -o StrictHostKeyChecking=no -i ~/.ssh/warply-gpu-$r.pem ubuntu@$ip \
      'cd ~/lso/runs/lsbench && ls -d */ 2>/dev/null | while read d; do [ -f "$d/result.json" ] && echo "${d%/}"; done | tr "\n" " "')
  [ -z "$n" ] && { echo "$id: no finished runs"; continue; }
  ssh -n -i ~/.ssh/warply-gpu-$r.pem ubuntu@$ip "cd ~/lso/runs/lsbench && tar czf - --exclude='*/work' --exclude='*.trace.json' \
      --exclude='*/vllm_*.log' --exclude='*/profile/profile_data.sqlite3*' --exclude='*/tmp_*' --exclude='*/last_adapter.npz' $n" \
    | tar xzf - -C $DST
  echo "$id: $(echo $n | wc -w | tr -d ' ') runs"
done 3< $REG
ls $DST | wc -l
