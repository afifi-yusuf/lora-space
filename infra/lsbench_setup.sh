#!/bin/bash
# One-time setup of a GPU box for lsbench (after infra/setup_gpu.sh). Run from ~ on the box.
set -euo pipefail
cd ~/lso
# Agency (local checkout synced to ~/agency) into the project venv
~/.local/bin/uv pip install --python .venv/bin/python -e ~/agency anthropic >/tmp/lsb_agency_install.log 2>&1 \
  && echo "agency installed" || { tail -20 /tmp/lsb_agency_install.log; exit 1; }
.venv/bin/python -c "import agency, anthropic; print('agency import ok')"
# Docker access for the ubuntu user (Agency sandboxes)
if ! docker info >/dev/null 2>&1; then sudo usermod -aG docker ubuntu; echo "added ubuntu to docker group (re-login needed)"; fi
sudo docker build -q -t lsbench-sandbox:latest lsbench/sandbox && echo "sandbox image built"
# Held-out and practice data
[ -f bench/math500.jsonl ] || .venv/bin/python scripts/m0_eval.py prepare
LSO_TARGET=qwen .venv/bin/python -c "
from lsbench import data; data.ensure_math()
from lsbench.target import load_target_module; data.ensure_syco(load_target_module('qwen'))
import subprocess; print(subprocess.run(['wc','-l','bench/lsbench/math_practice.jsonl','bench/lsbench/math_dev.jsonl','bench/lsbench/syco_diagnostics.jsonl','bench/lsbench/syco_dev.jsonl'],capture_output=True,text=True).stdout)"
echo LSBENCH_SETUP_DONE
