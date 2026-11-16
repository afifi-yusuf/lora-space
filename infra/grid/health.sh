#!/bin/bash
# One line per worker: current run, its tool-call count and age, harness errors in its log; plus runs ended since $SINCE.
cd "$(dirname "$0")"; SINCE=${SINCE:-2026-11-12T21:35}
while read -r id type r <&3; do
  ip=$(aws ec2 describe-instances --region $r --instance-ids $id --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)
  ssh -n -o ConnectTimeout=15 -o StrictHostKeyChecking=no -i ~/.ssh/warply-gpu-$r.pem ubuntu@$ip "
    cur=\$(grep -E ' START ' ~/lsb_grid.log | tail -1 | awk '{print \$3, \$4}'); last=\$(tail -1 ~/lsb_grid.log)
    e=\${cur% *}; t=\${cur#* }; d=~/lso/runs/lsbench/\${e}__\${t}__A__a1; f=~/lsb_grid_\${e}_\${t}.log
    busy=\$(pgrep -f '[l]sbench run' >/dev/null && echo running || echo idle)
    n=\$(wc -l < \$d/tool_calls.jsonl 2>/dev/null || echo -); err=\$(grep -cE 'SKILL ✗|Traceback' \$f 2>/dev/null)
    echo \"$id | \$busy \$cur | tool_calls=\$n harness_errors=\$err | queue=\$(grep -c . ~/lsb_grid_list.txt)\"
    awk -v s=$SINCE '\$1>=s && / END /' ~/lsb_grid.log | sed 's/^/      /'"
done 3< workers.txt
