# Editor sandbox for Agency harnesses: Codex + Claude Code CLIs, Agency's in-sandbox deps, numpy/scipy/safetensors.
# Deliberately no torch, jax or GPU libraries. Build on the GPU host:  docker build -t lsbench-sandbox:latest lsbench/sandbox
FROM docker.io/library/node:24-bookworm-slim AS node
FROM docker.io/library/python:3.12-slim-bookworm
COPY --from=node /usr/local/bin/node /usr/local/bin/node
COPY --from=node /usr/local/lib/node_modules/npm /usr/local/lib/node_modules/npm
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
    && apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl git procps libseccomp2 libstdc++6 \
    && rm -rf /var/lib/apt/lists/*
RUN npm install -g @openai/codex@0.147.0 @anthropic-ai/claude-code && npm cache clean --force
RUN pip install --no-cache-dir fastapi uvicorn openai httpx httpx2 mcp pyseccomp cloudpickle pyte html2text \
    numpy==2.5.4 scipy==1.18.1 safetensors==0.8.0
RUN codex --version && claude --version && python -c "import numpy, scipy, safetensors; print('ok')"
