"""Agency harness: the same task, run by Agency's native or Codex harness on GPT-6 Astra (Azure, Responses API).

Usage: python run_agency.py <root> <effort> <native|codex>
Profiling is on; Agency writes its run directory (data log, profile records) and we add result.json.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

from agency import Agent, agdata, agprof, agskill
from agency.configs.agconfig import agconfig, harnessadapterconfig, llmconfig, resourcesconfig, sandboxconfig

sys.path.insert(0, str(Path(__file__).parent))
from score import score  # noqa: E402


def main(root: str, effort: str, harness: str) -> None:
    root_p = Path(root)
    run_dir = root_p / "runs" / f"agency_{harness}_{time.strftime('%Y%m%dT%H%M%S')}"
    run_dir.mkdir(parents=True)
    cfg = agconfig(
        llmconfig(provider="openai_responses", base_url="https://principle.openai.azure.com/openai/v1",
                  model="gpt-6-astra", api_key=os.environ["AZURE_OPENAI_API_KEY"],
                  reasoning_effort=effort, max_completion_tokens=32000),
        sandboxconfig(base_image="lso-sandbox:latest", gpu_passthrough=False),
        resourcesconfig(idle_cpus=1),
        # Codex is installed in the sandbox image, not on the host: give Agency its absolute in-image path.
        harnessadapterconfig(binary_path="/usr/local/bin/codex" if harness == "codex" else None),
    )
    cfg.sandbox.add_mount("task", str(root_p / "task"), "/workspace/task", mode="rw")
    skill = agskill(
        name="recover_rank1_edit",
        prompt=(Path(__file__).parent / "task.md").read_text()
        + "\nAfter submitting all output fields, finish with a short confirmation.",
        input_schema=agdata(note=str),
        output_schema=agdata(rank=int, scale=float, columns=str, notes=str),
    )
    t0 = time.time()
    with agprof.session(run_dir / "profile", sample_hz=2, sample_gpu=False, auto_functions=False):
        worker = Agent(f"lso-{harness}", agconfig=cfg, harness=harness)
        res = worker.run(skill, agdata(note="Work in /workspace/task."))
        res.wait()
    wall = time.time() - t0
    answer = {"rank": res.rank, "scale": res.scale, "columns": res.columns, "notes": res.notes}
    out = {"harness": f"agency-{harness}", "effort": effort, "wall_s": round(wall, 1), "answer": answer,
           "score": score(root_p, answer["rank"], answer["scale"], answer["columns"]),
           "agency_run_dir": str(Path(worker.data_logger.db_path).parent.parent)}
    try:
        out["profile_summary"] = agprof.summary_table(row_limit=12)
    except Exception as e:  # noqa: BLE001
        out["profile_summary"] = f"unavailable: {e}"
    (run_dir / "result.json").write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
