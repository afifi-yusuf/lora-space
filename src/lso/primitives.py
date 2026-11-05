"""Closed-form low-rank edit primitives (numpy, float64).

Conventions: a linear layer computes y = W x with W of shape (d_out, d_in). A LoRA update is
ΔW = B @ A with B: (d_out, r), A: (r, d_in) (the LoRA scale is folded into B).
"""
from __future__ import annotations

import numpy as np


def input_side_ablation(W: np.ndarray, u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Rank-1 update making the layer ignore input direction u: (W + ΔW) u = 0.

    ΔW = -(W u) uᵀ / (uᵀ u). Returns LoRA factors (B, A) with ΔW = B @ A.
    """
    u = np.asarray(u, dtype=np.float64).reshape(-1)
    B = -(W @ u).reshape(-1, 1)
    A = (u / (u @ u)).reshape(1, -1)
    return B, A


def output_side_ablation(W: np.ndarray, r: np.ndarray, scale: float = 1.0,
                         columns: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Rank-1 update removing output direction r from what the layer writes: r̂ᵀ (W + ΔW) = (1 - scale) r̂ᵀ W.

    ΔW = -scale · r̂ (r̂ᵀ W), optionally restricted to a subset of input columns (as in the paper's 50-pass edit).
    scale=1 removes the direction exactly; scale>1 overshoots (flips its sign). Returns (B, A).
    """
    r_hat = np.asarray(r, dtype=np.float64).reshape(-1)
    r_hat = r_hat / np.linalg.norm(r_hat)
    a = r_hat @ W  # (d_in,)
    if columns is not None:
        mask = np.zeros_like(a)
        mask[np.asarray(columns)] = 1.0
        a = a * mask
    return (-scale * r_hat).reshape(-1, 1), a.reshape(1, -1)


def lora_from_delta(delta: np.ndarray, rank: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Best rank-`rank` LoRA factors of a dense update (truncated SVD, Eckart–Young).

    Returns (B, A, singular_values) with B = U_r diag(s_r), A = V_rᵀ.
    """
    U, s, Vt = np.linalg.svd(delta, full_matrices=False)
    return U[:, :rank] * s[:rank], Vt[:rank], s


def relative_error(delta: np.ndarray, approx: np.ndarray) -> float:
    return float(np.linalg.norm(delta - approx) / max(np.linalg.norm(delta), 1e-30))
