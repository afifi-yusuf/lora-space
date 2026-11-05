import numpy as np

from lso.primitives import input_side_ablation, lora_from_delta, output_side_ablation, relative_error

rng = np.random.default_rng(0)
W = rng.standard_normal((64, 96))


def test_input_side_ablation_zeroes_direction():
    u = rng.standard_normal(96)
    B, A = input_side_ablation(W, u)
    assert B.shape == (64, 1) and A.shape == (1, 96)
    assert np.allclose((W + B @ A) @ u, 0.0, atol=1e-10)


def test_output_side_ablation_removes_written_direction():
    r = rng.standard_normal(64)
    B, A = output_side_ablation(W, r)
    r_hat = r / np.linalg.norm(r)
    assert np.allclose(r_hat @ (W + B @ A), 0.0, atol=1e-10)
    # everything orthogonal to r is untouched
    P = np.eye(64) - np.outer(r_hat, r_hat)
    assert np.allclose(P @ (W + B @ A), P @ W)


def test_output_side_ablation_column_restricted_is_rank_one():
    r = rng.standard_normal(64)
    cols = np.arange(10)
    B, A = output_side_ablation(W, r, scale=1.5, columns=cols)
    delta = B @ A
    assert np.linalg.matrix_rank(delta) == 1
    assert np.allclose(delta[:, 10:], 0.0)


def test_lora_from_delta_exact_for_low_rank():
    delta = rng.standard_normal((64, 3)) @ rng.standard_normal((3, 96))
    B, A, s = lora_from_delta(delta, 3)
    assert relative_error(delta, B @ A) < 1e-10
    assert s[3] < 1e-10 * s[0]
