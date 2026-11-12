"""Task and entry specs (TOML), run naming and the settings hash (only runs with equal hashes are ranked together)."""
from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path

PKG = Path(__file__).resolve().parent
ROOT = PKG.parent
RULES_VERSION = "lsbench-v0.3"  # v0.3: interpretability toolkit (trace, token_stats, logit_lens, attribution,
#   attention, top_activations, patch; intervene in Track B), generate from a reply prefix, one analysis budget
#   v0.2: model description no longer says "used in non-thinking mode"


def load_task(task_id: str) -> dict:
    return tomllib.loads((PKG / "config/tasks" / f"{task_id}.toml").read_text())


def all_tasks() -> list[str]:
    return sorted(p.stem for p in (PKG / "config/tasks").glob("*.toml"))


def load_entries() -> tuple[dict[str, dict], dict]:
    cfg = tomllib.loads((PKG / "config/entries.toml").read_text())
    return {e["id"]: e for e in cfg["entry"]}, cfg["limits"]


def run_name(entry_id: str, task_id: str, track: str, attempt: int) -> str:
    return f"{entry_id}__{task_id}__{track}__a{attempt}"


def run_dir(name: str) -> Path:
    return ROOT / "runs/lsbench" / name


def settings_hash(task: dict, entry: dict, limits: dict, track: str, prompt_template: str) -> str:
    """Everything that should be equal for runs to be comparable (not the attempt index or the entry's id/label)."""
    keep = {k: v for k, v in entry.items() if k not in ("id", "label")}
    blob = json.dumps({"rules": RULES_VERSION, "task": task, "entry": keep, "limits": limits, "track": track,
                       "prompt": prompt_template}, sort_keys=True)
    return hashlib.sha256(blob.encode()).hexdigest()[:16]
