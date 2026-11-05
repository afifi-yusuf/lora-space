"""Generate the harness-comparison task: recover a column-restricted rank-1 output-side ablation.

A miniature of Milestone 0: W' = bf16(W - c · r̂ (r̂ᵀ W) on a subset of columns). The editor must find the rank,
the changed columns, the scale c and the direction r̂ from base.npy / edited.npy.

Usage: python make_task.py <task_dir>
"""
import json
import sys
from pathlib import Path

import numpy as np


def bf16_round(x: np.ndarray) -> np.ndarray:
    u = np.ascontiguousarray(x, dtype=np.float32).view(np.uint32).astype(np.uint64)
    u = (u + 0x7FFF + ((u >> 16) & 1)) >> 16
    return (u.astype(np.uint32) << 16).view(np.float32)


def main(task_dir: str) -> None:
    rng = np.random.default_rng(20261105)
    d_out, d_in, n_cols, c = 256, 512, 32, 6.0
    W = rng.standard_normal((d_out, d_in)) * 0.02
    r = rng.standard_normal(d_out)
    r_hat = r / np.linalg.norm(r)
    cols = np.sort(rng.choice(d_in, n_cols, replace=False))
    W_edit = W.copy()
    W_edit[:, cols] -= c * np.outer(r_hat, r_hat @ W[:, cols])
    out = Path(task_dir)
    (out / "out").mkdir(parents=True, exist_ok=True)
    np.save(out / "base.npy", bf16_round(W))
    np.save(out / "edited.npy", bf16_round(W_edit))
    truth = {"rank": 1, "scale": c, "columns": cols.tolist()}
    (out.parent / "truth.json").write_text(json.dumps(truth))
    np.save(out.parent / "truth_r_hat.npy", r_hat)
    print("task written:", out, "| truth kept outside the task dir")


if __name__ == "__main__":
    main(sys.argv[1])
