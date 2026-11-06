"""Chess diagnosis: where does a small Qwen fail at chess? (Decides whether "make it good at chess" is editable.)

Positions come from the Lichess puzzle database (each puzzle's position after the opponent's first move). Four levels:
  1 format   the reply is a single move (format_ok: UCI or SAN; uci_format: UCI as the prompt asks), nothing else
  2 legal    the move it gives (first move found in the reply) is legal in the position
  3 mate1    on mate-in-1 puzzles: the move delivers checkmate (any mating move counts)
  4 quality  on other puzzles: solves the puzzle's first move; centipawn loss vs Stockfish's best (depth 12)
Rule-tier failures (1-2) are the kind a one-shot edit might fix; 3-4 are skill.

  .venv/bin/python scripts/chess_diag.py prepare                        # bench/chess/{mate1,puzzles}.jsonl
  .venv/bin/python scripts/chess_diag.py gen --model DIR --tag T [--think] [--max-tokens N]
  .venv/bin/python scripts/chess_diag.py eval --tag T                   # needs `stockfish` on PATH
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "bench/chess"
OUT = ROOT / "results/chess_diag"
N_EACH = 300
PROMPT = ("You are playing chess. Here is the position in FEN notation:\n{fen}\n{side} to move. What is the best "
          "move? Reply with the move in UCI notation (for example e2e4 or g1f3) and nothing else.")
UCI = re.compile(r"\b([a-h][1-8][a-h][1-8][qrbn]?)\b")
SAN = re.compile(r"\b(O-O-O|O-O|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](?:=[QRBN])?[+#]?)")


def prepare() -> None:
    import chess
    from datasets import load_dataset
    BENCH.mkdir(parents=True, exist_ok=True)
    ds = load_dataset("Lichess/chess-puzzles", split="train", streaming=True)
    mate1, other = [], []
    for r in ds:
        themes = r["Themes"] if isinstance(r["Themes"], list) else str(r["Themes"]).split()
        if r.get("Popularity", 0) < 80 or r.get("NbPlays", 0) < 500:
            continue
        board = chess.Board(r["FEN"])
        moves = r["Moves"].split()
        board.push_uci(moves[0])  # the opponent's move; the puzzle starts after it
        row = {"id": r["PuzzleId"], "fen": board.fen(), "solution": moves[1], "rating": r["Rating"], "themes": themes}
        if "mateIn1" in themes and len(mate1) < N_EACH:
            mate1.append(row)
        elif "mateIn1" not in themes and len(other) < N_EACH and 800 <= r["Rating"] <= 2000:
            other.append(row)
        if len(mate1) >= N_EACH and len(other) >= N_EACH:
            break
    for name, rows in (("mate1", mate1), ("puzzles", other)):
        (BENCH / f"{name}.jsonl").write_text("".join(json.dumps(x) + "\n" for x in rows))
        print(name, len(rows))


def gen(model: str, tag: str, think: bool, max_tokens: int, gpu_mem: float, max_num_seqs: int) -> None:
    os.environ.setdefault("VLLM_USE_FLASHINFER_SAMPLER", "0")
    from vllm import LLM, SamplingParams
    out = OUT / tag
    out.mkdir(parents=True, exist_ok=True)
    llm = LLM(model=model, dtype="bfloat16", gpu_memory_utilization=gpu_mem, max_model_len=max_tokens + 1024, seed=0,
              max_num_seqs=max_num_seqs, limit_mm_per_prompt={"image": 0, "video": 0})
    tok = llm.get_tokenizer()
    sp = (SamplingParams(temperature=0.6, top_p=0.95, top_k=20, presence_penalty=1.5, max_tokens=max_tokens, seed=0)
          if think else SamplingParams(temperature=0.0, max_tokens=max_tokens))
    meta = {"model": model, "think": think, "max_tokens": max_tokens, "sets": {}}
    for s in ("mate1", "puzzles"):
        rows = [json.loads(line) for line in open(BENCH / f"{s}.jsonl")]
        prompts = [tok.apply_chat_template([{"role": "user", "content": PROMPT.format(
            fen=r["fen"], side="White" if " w " in r["fen"] else "Black")}], tokenize=False, add_generation_prompt=True,
            enable_thinking=think) for r in rows]
        t0 = time.time()
        res = llm.generate(prompts, sp)
        with open(out / f"{s}_samples.jsonl", "w") as f:
            for r, o in zip(rows, res):
                c = o.outputs[0]
                f.write(json.dumps({"id": r["id"], "raw": c.text, "finish": c.finish_reason}) + "\n")
        meta["sets"][s] = {"n": len(rows), "seconds": round(time.time() - t0)}
        print(tag, s, meta["sets"][s], flush=True)
    (out / "gen_meta.json").write_text(json.dumps(meta, indent=1))


def parse_move(board, text: str):
    """(move or None, how): the first UCI-looking move in the answer, else the first parseable SAN move."""
    import chess
    ans = text.split("</think>")[-1]
    for m in UCI.findall(ans):
        try:
            mv = chess.Move.from_uci(m)
            return mv, "uci"
        except ValueError:
            continue
    for m in SAN.findall(ans):
        try:
            return board.parse_san(m), "san"
        except ValueError:
            continue
    return None, "none"


def evaluate(tag: str, depth: int = 12) -> None:
    import chess
    import chess.engine
    out = OUT / tag
    think = json.loads((out / "gen_meta.json").read_text()).get("think", False)
    eng = chess.engine.SimpleEngine.popen_uci("stockfish")
    summary = {}
    for s in ("mate1", "puzzles"):
        rows = {json.loads(l)["id"]: json.loads(l) for l in open(BENCH / f"{s}.jsonl")}
        samples = [json.loads(l) for l in open(out / f"{s}_samples.jsonl")]
        c, cpl, per = Counter(), [], []
        for x in samples:
            r = rows[x["id"]]
            board = chess.Board(r["fen"])
            # thinking mode: the chat template opens <think> in the prompt, so an answer exists only after </think>
            unfinished = think and "</think>" not in x["raw"]
            ans = "" if unfinished else x["raw"].split("</think>")[-1].strip()
            truncated = x["finish"] == "length" and (unfinished or not ans)
            only_move = bool(re.fullmatch(r"\s*`?\s*([a-h][1-8][a-h][1-8][qrbn]?|O-O-O|O-O|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](=[QRBN])?[+#]?)\s*`?\.?\s*", ans))
            uci_only = bool(re.fullmatch(r"\s*`?\s*[a-h][1-8][a-h][1-8][qrbn]?\s*`?\.?\s*", ans))
            mv, how = parse_move(board, ans) if ans else (None, "none")
            legal = mv is not None and mv in board.legal_moves
            rec = {"id": x["id"], "format_ok": only_move, "uci_format": uci_only, "found": how, "legal": legal, "truncated": truncated}
            c["n"] += 1; c["format_ok"] += only_move; c["uci_format"] += uci_only; c["move_found"] += mv is not None; c["legal"] += legal
            c["truncated"] += truncated
            if legal:
                c["solved"] += mv.uci() == r["solution"]
                if s == "mate1":
                    board.push(mv)
                    c["mate"] += board.is_checkmate()
                    board.pop()
                else:
                    info = eng.analyse(board, chess.engine.Limit(depth=depth))
                    best = info["score"].pov(board.turn).score(mate_score=10000)
                    board.push(mv)
                    after = -eng.analyse(board, chess.engine.Limit(depth=depth))["score"].pov(board.turn).score(mate_score=10000)
                    board.pop()
                    loss = max(0, min(1000, best - after))
                    cpl.append(loss); rec["cp_loss"] = loss
            per.append(rec)
        n = c["n"]
        sm = {"n": n, "format_ok": round(c["format_ok"] / n, 4), "uci_format": round(c["uci_format"] / n, 4), "move_found": round(c["move_found"] / n, 4),
              "legal": round(c["legal"] / n, 4), "solved_puzzle_move": round(c["solved"] / n, 4),
              "truncated": round(c["truncated"] / n, 4)}
        if s == "mate1":
            sm["mate_in_1"] = round(c["mate"] / n, 4)
        else:
            sm["mean_cp_loss_legal"] = round(sum(cpl) / len(cpl), 1) if cpl else None
            sm["blunder_rate_legal"] = round(sum(x >= 300 for x in cpl) / len(cpl), 4) if cpl else None
        summary[s] = sm
        (out / f"{s}_scored.json").write_text(json.dumps(per))
        print(tag, s, sm, flush=True)
    eng.quit()
    # reference: a uniformly random legal move, same positions (seeded)
    import random
    random.seed(0)
    ref = {}
    for s in ("mate1", "puzzles"):
        rows = [json.loads(l) for l in open(BENCH / f"{s}.jsonl")]
        hits = 0
        for r in rows:
            b = chess.Board(r["fen"])
            mv = random.choice(list(b.legal_moves))
            if s == "mate1":
                b.push(mv); hits += b.is_checkmate()
            else:
                hits += mv.uci() == r["solution"]
        ref[s] = round(hits / len(rows), 4)
    summary["random_legal_move_reference"] = ref
    (out / "summary.json").write_text(json.dumps(summary, indent=1))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["prepare", "gen", "eval"])
    ap.add_argument("--model")
    ap.add_argument("--tag")
    ap.add_argument("--think", action="store_true")
    ap.add_argument("--max-tokens", type=int, default=256)
    ap.add_argument("--gpu-mem", type=float, default=0.3)
    ap.add_argument("--max-num-seqs", type=int, default=128)
    a = ap.parse_args()
    if a.cmd == "prepare":
        prepare()
    elif a.cmd == "gen":
        gen(a.model, a.tag, a.think, a.max_tokens, a.gpu_mem, a.max_num_seqs)
    else:
        evaluate(a.tag)


if __name__ == "__main__":
    main()
