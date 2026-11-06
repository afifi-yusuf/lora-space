#!/bin/bash
# Set up a fresh GPU box (DLAMI Ubuntu 24.04) for LSO, matching the g6 used for M0/M0.5:
#   main venv ~/lso/.venv (vLLM 0.33, torch 2.14, transformers 5.20 — pinned in infra/requirements-gpu.lock),
#   the editor sandbox (Unix user `editor`, /opt/editor-venv with numpy/scipy/safetensors only, /srv/lso-editor),
#   and /opt/code-venv (EvalPlus) for scoring model-written code as `editor`.
# Run on the box from ~/lso after rsyncing the repo:  bash infra/setup_gpu.sh
set -euo pipefail
sudo apt-get update -qq && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3.12-dev >/dev/null  # Triton builds need Python.h
command -v ~/.local/bin/uv >/dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh >/dev/null
UV=~/.local/bin/uv
cd ~/lso
$UV venv -q --python /usr/bin/python3 .venv
$UV pip install -q --python .venv/bin/python -r infra/requirements-gpu.lock
id editor >/dev/null 2>&1 || sudo useradd --system --create-home --shell /usr/sbin/nologin editor
sudo $UV venv -q --python /usr/bin/python3 /opt/editor-venv
sudo $UV pip install -q --python /opt/editor-venv/bin/python numpy==2.5.4 scipy==1.18.1 safetensors==0.8.0
sudo $UV venv -q --python /usr/bin/python3 /opt/code-venv
sudo $UV pip install -q --python /opt/code-venv/bin/python evalplus==0.3.1
sudo mkdir -p /srv/lso-editor/code/cache && sudo chmod 755 /srv/lso-editor
# Code-benchmark problems (download only; no code is executed here)
sudo chown -R "$USER" /srv/lso-editor/code
XDG_CACHE_HOME=/srv/lso-editor/code/cache /opt/code-venv/bin/python scripts/code_diag.py prepare --out benchmarks/code
sudo cp -r benchmarks/code /srv/lso-editor/code/problems && sudo chown -R editor:editor /srv/lso-editor/code
.venv/bin/python -c "import torch, vllm, transformers; print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), 'vllm', vllm.__version__, 'transformers', transformers.__version__)"
echo SETUP_DONE
