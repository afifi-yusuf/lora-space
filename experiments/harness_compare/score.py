"""Score a harness run's answer against the hidden ground truth."""
import json
import os
import sys
from pathlib import Path

import numpy as np


def score(root: Path, rank, scale, columns) -> dict:
    # Ground truth lives outside the editor-visible tree (LSO_TRUTH_DIR); defaults to <root> for local use.
    truth_dir = Path(os.environ.get("LSO_TRUTH_DIR", root))
    truth = json.loads((truth_dir / "truth.json").read_text())
    if isinstance(columns, str):
        columns = [int(x) for x in columns.replace(" ", "").split(",") if x]
    res = {
        "rank_ok": int(rank) == truth["rank"],
        "scale_ok": abs(float(scale) - truth["scale"]) < 0.05,
        "columns_ok": sorted(int(c) for c in columns) == truth["columns"],
    }
    p = root / "task/out/r_hat.npy"
    if p.exists():
        r_hat = np.load(p).ravel().astype(np.float64)
        true = np.load(truth_dir / "truth_r_hat.npy")
        res["r_hat_abs_cos"] = float(abs(r_hat @ true) / (np.linalg.norm(r_hat) * np.linalg.norm(true)))
        res["r_hat_ok"] = res["r_hat_abs_cos"] > 0.999
    else:
        res["r_hat_ok"] = False
    res["all_ok"] = all(v for k, v in res.items() if k.endswith("_ok"))
    return res


if __name__ == "__main__":
    a = json.loads(sys.argv[2])
    print(json.dumps(score(Path(sys.argv[1]), a["rank"], a["scale"], a["columns"]), indent=1))
