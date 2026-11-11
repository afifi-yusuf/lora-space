"""Leaderboard: main board = each model with its selected harness; harness view = every (model, harness) entry;
headline chart = normalized score against cost. Writes results/lsbench/leaderboard.{md,csv,json} and .png."""
from __future__ import annotations

import csv
import json
import statistics
from collections import defaultdict

from . import spec

OUT = spec.ROOT / "results/lsbench"


def _collect() -> list[dict]:
    rows = []
    for f in sorted((spec.ROOT / "runs/lsbench").glob("*/result.json")):
        r = json.loads(f.read_text())
        rows.append(r)
    return rows


def build() -> None:
    rows = _collect()
    OUT.mkdir(parents=True, exist_ok=True)
    cells: dict[tuple, list] = defaultdict(list)
    for r in rows:
        cells[(r["entry"], r["label"], r["task"], r["track"], r["settings_hash"])].append(r)
    table = []
    for (entry, label, task, track, h), rs in sorted(cells.items()):
        norms = [(r["score"] or {}).get("normalized") for r in rs]
        norms = [0.0 if n is None else n for n in norms]  # no commit / failed scoring counts as the unedited model
        vals = [(r["score"] or {}).get("value") for r in rs]
        table.append({"entry": entry, "label": label, "task": task, "track": track, "settings_hash": h,
                      "attempts": len(rs), "normalized_mean": round(statistics.mean(norms), 1),
                      "values": vals, "gpu_hours_mean": round(statistics.mean(r["cost"]["gpu_hours"] for r in rs), 2),
                      "audit_clean": all(r["audit"]["clean"] for r in rs)})
    per_entry: dict[tuple, list] = defaultdict(list)
    for t in table:
        per_entry[(t["label"], t["track"])].append(t)
    board = sorted(({"label": k[0], "track": k[1], "median_normalized": statistics.median(x["normalized_mean"] for x in v),
                     "tasks": len(v), "gpu_hours_per_run": round(statistics.mean(x["gpu_hours_mean"] for x in v), 2),
                     "audit_clean": all(x["audit_clean"] for x in v)} for k, v in per_entry.items()),
                   key=lambda b: (b["track"], -b["median_normalized"]))
    (OUT / "leaderboard.json").write_text(json.dumps({"board": board, "cells": table}, indent=1, default=str))
    with open(OUT / "leaderboard.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(table[0]) if table else ["entry"])
        w.writeheader()
        w.writerows(table)
    md = ["# LoRA-Space Bench leaderboard", "", f"Rules {spec.RULES_VERSION}. 0 = unedited model, 100 = the task's best "
          "reference (paper edit or gradient LoRA). Median over tasks of the mean over attempts.", "",
          "| # | Entry | Track | Median score | Tasks | GPU-h / run | Audit |", "|---|---|---|---|---|---|---|"]
    md += [f"| {i} | {b['label']} | {b['track']} | {b['median_normalized']} | {b['tasks']} | {b['gpu_hours_per_run']} | "
           f"{'ok' if b['audit_clean'] else 'FLAGGED'} |" for i, b in enumerate(board, 1)]
    md += ["", "## Per task", "", "| Entry | Task | Track | Attempts | Mean score | Raw values | GPU-h |", "|---|---|---|---|---|---|---|"]
    md += [f"| {t['label']} | {t['task']} | {t['track']} | {t['attempts']} | {t['normalized_mean']} | {t['values']} | "
           f"{t['gpu_hours_mean']} |" for t in table]
    (OUT / "leaderboard.md").write_text("\n".join(md) + "\n")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7, 4.5))
        for t in table:
            ax.scatter(t["gpu_hours_mean"], t["normalized_mean"], label=f"{t['label']} · {t['task']} · {t['track']}")
        ax.axhline(100, ls="--", lw=1, c="gray")
        ax.set_xlabel("GPU-hours per run (session + scoring)")
        ax.set_ylabel("Normalized score (100 = best reference)")
        ax.legend(fontsize=6, loc="best")
        fig.tight_layout()
        fig.savefig(OUT / "leaderboard.png", dpi=150)
    except Exception as e:  # noqa: BLE001
        print("plot skipped:", e)
    print((OUT / "leaderboard.md").read_text())
