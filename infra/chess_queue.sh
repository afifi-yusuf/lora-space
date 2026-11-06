#!/bin/bash
# Chess base diagnosis on the g6's spare GPU memory (next to the base MATH run). Each generation retried up to 3x
# (vLLM start-up can race with the MATH job freeing memory).
cd ~/lso; Q=~/chess; mkdir -p $Q
log() { echo "$(date -u +%FT%TZ) $*" | tee -a $Q/queue.log; }
job() {  # job <tag> <model dir> [gen flags]
  local tag=$1 model=$2; shift 2
  for try in 1 2 3; do
    log "START gen $tag (try $try)"
    .venv/bin/python scripts/chess_diag.py gen --model "$model" --tag "$tag" "$@" > $Q/gen_$tag.log 2>&1 && break
    sleep 60
  done
  .venv/bin/python scripts/chess_diag.py eval --tag "$tag" > $Q/eval_$tag.log 2>&1
  log "END $tag :: $(grep -E "^$tag" $Q/eval_$tag.log | tr '\n' ' ' | cut -c1-500)"
}
log "QUEUE START"
job q08_nothink models/Qwen3.5-0.8B
job q2b_nothink models/Qwen3.5-2B
job q08_think4k models/Qwen3.5-0.8B --think --max-tokens 4096
job q2b_think4k models/Qwen3.5-2B --think --max-tokens 4096
log "QUEUE DONE"
