#!/bin/bash
# Runs grid entries (Track A, attempt 1) one at a time, popping the first line of ~/lsb_grid_list.txt under a lock
# each time, so the remaining list can be edited (rebalanced) while the worker runs. Exits when the list is empty.
cd ~/lso; set -a; . ./secrets.env; set +a
LOG=~/lsb_grid.log; LIST=~/lsb_grid_list.txt; LOCK=~/lsb_grid_list.lock
# A run started by a previous worker process may still be going: wait for it rather than share the GPU.
while pgrep -f "python -m lsbench run" >/dev/null; do sleep 30; done
echo "$(date -u +%FT%TZ) WORKER START $(hostname)" >> $LOG
while :; do
  line=$(flock $LOCK -c "head -1 $LIST; sed -i 1d $LIST")
  if [ -z "$line" ]; then  # empty: a rebalance may be refilling it; give up after 10 idle minutes
    idle=$((${idle:-0} + 1)); [ $idle -gt 20 ] && break; sleep 30; continue
  fi
  idle=0
  read -r entry task <<< "$line"
  echo "$(date -u +%FT%TZ) START $entry $task" >> $LOG
  .venv/bin/python -m lsbench run --entry "$entry" --task "$task" --track A --attempt 1 > ~/lsb_grid_${entry}_${task}.log 2>&1
  rc=$?
  r=runs/lsbench/${entry}__${task}__A__a1/result.json
  s=$(python3 -c "import json;r=json.load(open('$r'));s=r['score'] or {};print(r['status'], s.get('value'), s.get('normalized'), (s.get('damage') or {}).get('flagged'))" 2>/dev/null || echo "no-result")
  echo "$(date -u +%FT%TZ) END $entry $task rc=$rc :: $s" >> $LOG
  # A stalled session (no model or tool call for stall_minutes) is an infrastructure fault: archive it and requeue,
  # at most twice per run.
  # The provider rejected a call for account credit (an account fault, not the editor): archive, wait, requeue (max 3).
  if [[ "$s" != committed* ]] && grep -qiE "billing_error|credit balance is too low|prepayment credits are depleted" ~/lsb_grid_${entry}_${task}.log; then
    name=${entry}__${task}__A__a1; mkdir -p runs/lsbench_failed
    tries=$(ls -d runs/lsbench_failed/${name}.credit_* 2>/dev/null | wc -l)
    mv runs/lsbench/$name runs/lsbench_failed/${name}.credit_$(date -u +%H%M%S)
    if [ "$tries" -lt 3 ]; then
      echo "$(date -u +%FT%TZ) REQUEUE $entry $task (account credit; retry in 10 min)" >> $LOG; sleep 600
      flock $LOCK -c "echo '$entry $task' >> $LIST"
    fi
    continue
  fi
  if [[ "$s" == stalled* ]]; then
    name=${entry}__${task}__A__a1; mkdir -p runs/lsbench_failed
    tries=$(ls -d runs/lsbench_failed/${name}.stalled_* 2>/dev/null | wc -l)
    mv runs/lsbench/$name runs/lsbench_failed/${name}.stalled_$(date -u +%H%M%S)
    if [ "$tries" -lt 2 ]; then
      flock $LOCK -c "echo '$entry $task' >> $LIST"; echo "$(date -u +%FT%TZ) REQUEUE $entry $task (stalled)" >> $LOG
    fi
  fi
done
echo "$(date -u +%FT%TZ) WORKER DONE" >> $LOG
