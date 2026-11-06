#!/bin/bash
# First request-harness runs ("make it better at Python coding") on Qwen3.5-0.8B, on the g6.4xlarge.
set -u
set -a; . ~/lso/secrets.env; set +a
cd ~/lso
Q=~/code_edit; mkdir -p $Q
log() { echo "$(date -u +%FT%TZ) $*" | tee -a $Q/queue.log; }
run() { local job=$1; shift; log "START $job"; "$@" > $Q/$job.log 2>&1; local rc=$?
        log "END   $job rc=$rc :: $(grep -E '"pass@1_base"|pass@1' $Q/$job.log | tail -2 | tr '\n' ' ' | cut -c1-300)"; }
log "QUEUE START"
run base_score_q08 env LSO_TARGET=qwen .venv/bin/python -c "
import sys; sys.argv=['x']; sys.path[:0]=['scripts','src']
import lso_request as R; from pathlib import Path
R.RUN_DIR = Path('runs/code_edit/base_q08'); R.RUN_DIR.mkdir(parents=True, exist_ok=True)
import json; print(json.dumps(R.score(R.G.MODEL_DIR, 'base_q08')))"
run q08_modeA_rep1 env LSO_TARGET=qwen .venv/bin/python scripts/lso_request.py --request code
run q08_modeA_rep2 env LSO_TARGET=qwen .venv/bin/python scripts/lso_request.py --request code
run q08_modeB5_rep1 env LSO_TARGET=qwen .venv/bin/python scripts/lso_request.py --request code --feedback 5
log "QUEUE DONE"
