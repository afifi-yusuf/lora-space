# Sandbox image for the harness comparison: Agency's harness recipe (Codex 0.147.0) + numpy.
FROM docker.io/library/node:24-bookworm-slim AS node
FROM docker.io/library/python:3.12-slim-bookworm
COPY --from=node /usr/local/bin/node /usr/local/bin/node
COPY --from=node /usr/local/lib/node_modules/npm /usr/local/lib/node_modules/npm
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
    && apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl git procps libseccomp2 libstdc++6 \
    && rm -rf /var/lib/apt/lists/*
RUN npm install -g @openai/codex@0.147.0 && npm cache clean --force
RUN pip install --no-cache-dir fastapi uvicorn openai httpx httpx2 mcp pyseccomp cloudpickle pyte html2text numpy
RUN codex --version && python -c "import numpy; print(numpy.__version__)"
