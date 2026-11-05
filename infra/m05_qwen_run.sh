#!/bin/bash
# Qwen3.5-0.8B sycophancy control: baselines (sequential) and Astra Mode A v3 (in parallel).
set -a; . ~/lso/secrets.env; set +a
export LSO_TARGET=qwen
cd ~/lso
(
  for step in scripted random scripted_select lora_grad; do
    echo "=== $step $(date -u +%T)"
    .venv/bin/python scripts/m05_baselines.py "$step" 2>&1 | grep -v -E "it/s\]|^\s*$|falling back|Loading weights" | tail -6
  done
  echo QWEN_BASELINES_DONE "$(date -u +%T)"
) > ~/m05_qwen_baselines.log 2>&1 &
.venv/bin/python scripts/m05_editor.py --effort xhigh --max-turns 60 --v3 > ~/m05_qwen_editor_v3.log 2>&1
echo QWEN_EDITOR_DONE "$(date -u +%T)" >> ~/m05_qwen_editor_v3.log
wait
echo QWEN_ALL_DONE "$(date -u +%T)"
