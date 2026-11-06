#!/bin/bash
# Restart the stopped g6.4xlarge, copy the code-edit results back, stop it again.
ID=i-04d16fabefd1104e2; K=~/.ssh/warply-gpu-us-east-1.pem; R=us-east-1
for i in $(seq 1 36); do
  if aws ec2 start-instances --region $R --instance-ids $ID >/dev/null 2>&1; then echo "$(date -u +%FT%TZ) started (try $i)"; break; fi
  echo "$(date -u +%FT%TZ) try $i: no capacity"; sleep 300
done
aws ec2 wait instance-running --region $R --instance-ids $ID || exit 1
IP=$(aws ec2 describe-instances --region $R --instance-ids $ID --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)
until ssh -i $K -o ConnectTimeout=10 -o StrictHostKeyChecking=no ubuntu@$IP true 2>/dev/null; do sleep 10; done
mkdir -p results/code_edit/logs
ssh -i $K ubuntu@$IP 'cd lso && tar cz results/code_edit runs/code_edit' | tar xz
scp -q -i $K "ubuntu@$IP:code_edit/*.log" results/code_edit/logs/ 2>/dev/null
scp -q -i $K "ubuntu@$IP:*.out" results/code_edit/logs/ 2>/dev/null
aws ec2 stop-instances --region $R --instance-ids $ID >/dev/null && echo "$(date -u +%FT%TZ) fetched from $IP, stopped"
ls results/code_edit
