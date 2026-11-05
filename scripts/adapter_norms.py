"""Report rank and relative update size ||B A|| / ||W|| per module for an adapter (.npz) on the configured target.

Usage: LSO_TARGET=gemma|qwen python scripts/adapter_norms.py <adapter.npz>
"""
import sys
from pathlib import Path

import numpy as np
import torch
from safetensors import safe_open

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from lso import gemma_syco as G  # noqa: E402

z = np.load(sys.argv[1])
names = sorted({k.rsplit("::", 1)[0] for k in z.files})
with safe_open(str(G.MODEL_DIR / G.WEIGHTS_FILE), framework="pt") as f:
    for n in names:
        W = f.get_tensor(n.replace("model.", G.WEIGHT_PREFIX, 1) + ".weight").double().numpy()
        B, A = z[n + "::B"].astype(np.float64), z[n + "::A"].astype(np.float64)
        print(f"{G.TARGET} {n}: rank {A.shape[0]}, ||dW||/||W|| = {np.linalg.norm(B @ A) / np.linalg.norm(W):.3f}")
