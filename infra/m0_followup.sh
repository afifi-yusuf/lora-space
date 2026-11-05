#!/bin/bash
# After the full rank-1 LoRA MATH-500 eval (4 samples, 500 problems) finishes, run the cheaper cross-checks
# on a fixed 200-problem subset: exact edit (2 samples) and base (1 sample).
cd ~/lso
while pgrep -f "m0_eval[.]py run p50c_r1" >/dev/null; do sleep 60; done
grep "p50c_r1 math500" ~/m0_p50c_r1.log
for job in "p50c_exact 2 200" "base 1 200"; do
  set -- $job
  echo "=== $1 samples=$2 limit=$3 start $(date -u +%T)"
  .venv/bin/python scripts/m0_eval.py run "$1" --sets math500 --samples "$2" --limit "$3" --gpu-mem 0.6 > ~/m0_"$1".log 2>&1
  grep "$1 math500" ~/m0_"$1".log || tail -3 ~/m0_"$1".log
done
echo M0_EVAL_DONE "$(date -u +%T)"
