#!/bin/bash
# Overnight queue (2026-11-06, ~14 h) on the g6 next to the MATH-500 runs (which hold ~14 GB of the L4's 23 GB).
# One job at a time (each <= ~7 GB GPU), most important first; a failed job is logged and the queue moves on.
#   ~/overnight/queue.log   one line per job: start / end / exit code / headline result
#   ~/overnight/<job>.log   full output
set -u
set -a; . ~/lso/secrets.env; set +a
cd ~/lso
Q=~/overnight; mkdir -p $Q
CODE=/srv/lso-editor/code   # model-written code is executed only by the unprivileged `editor` user, in here

log() { echo "$(date -u +%FT%TZ) $*" | tee -a $Q/queue.log; }
run() {  # run <job> <target> <cmd...>
  local job=$1 tgt=$2; shift 2
  log "START $job"
  LSO_TARGET=$tgt "$@" > $Q/$job.log 2>&1; local rc=$?
  log "END   $job rc=$rc :: $(grep -vE 'it/s|s/it|^\s*$|Warning|falling back' $Q/$job.log | tail -1 | cut -c1-240)"
}
editor() { run "$1" "$2" .venv/bin/python scripts/m05_editor.py --effort xhigh --max-turns 60 --v3 "${@:3}"; }
base()   { run "$1" "$2" .venv/bin/python scripts/m05_baselines.py "${@:3}"; }
code() {  # code <tag> <model dir> [gen flags...]: generate (main venv, GPU) then score as `editor`
  local tag=$1 model=$2; shift 2
  run code_gen_$tag qwen .venv/bin/python scripts/code_diag.py gen --model "$model" --tag "$tag" --gpu-mem 0.3 "$@"
  sudo mkdir -p $CODE/$tag && sudo cp results/code_diag/$tag/*.jsonl results/code_diag/$tag/gen_meta.json $CODE/$tag/ \
    && sudo install -m 644 scripts/code_diag.py $CODE/code_diag.py && sudo chown -R editor:editor $CODE
  log "START code_eval_$tag"
  (cd $CODE && sudo -u editor env XDG_CACHE_HOME=$CODE/cache HOME=$CODE /opt/code-venv/bin/python code_diag.py eval \
     --dir $CODE/$tag --problems $CODE/problems) > $Q/code_eval_$tag.log 2>&1; local rc=$?
  cp $CODE/$tag/*_buckets.json $CODE/$tag/summary.json results/code_diag/$tag/ 2>/dev/null
  log "END   code_eval_$tag rc=$rc :: $(tail -2 $Q/code_eval_$tag.log | tr '\n' ' ' | cut -c1-400)"
}
gate_2b() {  # spend Astra calls on the 2B only if it is sycophantic enough to measure a fix
  python3 -c "import json,sys; f=json.load(open('results/m05_qwen2b/base.json'))['heldout']['wrong_follow_known']; \
print('2B base wrong_follow_known', f); sys.exit(0 if f >= 0.10 else 1)" >> $Q/queue.log 2>&1  # no pipe: keep the exit code
}

log "QUEUE START"
# 1. Qwen 0.8B Mode A v3: 3 repeats -> mean +- s.d. with the 2026-11-05 run (n = 4)
for i in 2 3 4; do editor q08_modeA_v3_rep$i qwen; done
# 2. Qwen 2B: facts it knows, then the cheap baselines and the gradient reference
run  q2b_data qwen2b .venv/bin/python scripts/m05_qwen_data.py
base q2b_base qwen2b base
base q2b_scripted qwen2b scripted
base q2b_random qwen2b random
base q2b_lora_grad_r8 qwen2b lora_grad --rank 8
if gate_2b; then ASTRA_2B=1; else ASTRA_2B=0; log "SKIP 2B Astra runs (too little sycophancy to fix)"; fi
# 3. Astra on the 2B, and Mode B (10 scored candidates) on both sizes
[ $ASTRA_2B = 1 ] && editor q2b_modeA_v3_rep1 qwen2b
editor q08_modeB10_v3_rep1 qwen --feedback 10
[ $ASTRA_2B = 1 ] && editor q2b_modeB10_v3_rep1 qwen2b --feedback 10
# 4. Code diagnosis, non-thinking greedy (HumanEval+ / MBPP+ failure buckets)
code q08_nothink models/Qwen3.5-0.8B
code q2b_nothink models/Qwen3.5-2B
# 5. Layer-selected scripted baseline on the 2B; more repeats
base q2b_scripted_select qwen2b scripted_select
[ $ASTRA_2B = 1 ] && { editor q2b_modeA_v3_rep2 qwen2b; editor q2b_modeA_v3_rep3 qwen2b; }
editor q08_modeB10_v3_rep2 qwen --feedback 10
[ $ASTRA_2B = 1 ] && editor q2b_modeB10_v3_rep2 qwen2b --feedback 10
# 6. How much rank does the gradient need? (Astra's best Qwen edit used rank 1 + rank 8)
for r in 1 2 4; do base q08_lora_grad_r$r qwen lora_grad --rank $r; done
base q2b_lora_grad_r1 qwen2b lora_grad --rank 1
# 7. Code diagnosis with thinking on (8K-token budget, the paper's sampling)
code q08_think8k models/Qwen3.5-0.8B --think --max-tokens 8192
code q2b_think8k models/Qwen3.5-2B --think --max-tokens 8192
# 8. Hint ablation: 0.8B Mode A v3 without the method hint
for i in 1 2; do editor q08_modeA_v3_nohint_rep$i qwen --no-hint; done
log "QUEUE DONE"
