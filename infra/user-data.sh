#!/bin/bash
# Idle auto-stop: stop the instance after 60 min with no GPU use, no python/vllm/codex process and no interactive SSH.
cat > /usr/local/bin/idle-stop.sh <<'EOS'
#!/bin/bash
STATE=/var/run/lso_last_busy
[ -f "$STATE" ] || date +%s > "$STATE"
util=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits 2>/dev/null | head -1 | tr -d ' ')
busy=0
[ "${util:-0}" -gt 5 ] 2>/dev/null && busy=1
pgrep -u ubuntu -f "python|vllm|codex" >/dev/null && busy=1
who | grep -q pts && busy=1
[ $busy -eq 1 ] && date +%s > "$STATE"
idle=$(( $(date +%s) - $(cat "$STATE") ))
if [ "$idle" -gt 3600 ]; then logger "lso idle-stop: idle ${idle}s, shutting down"; shutdown -h now; fi
EOS
chmod +x /usr/local/bin/idle-stop.sh
echo "*/5 * * * * root /usr/local/bin/idle-stop.sh" > /etc/cron.d/lso-idle-stop
