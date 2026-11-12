"""Task-neutral interpretability tools over the UNEDITED target (plus `intervene`, Track B only). Read-only by design:
no tool returns weight gradients (a gradient step would be training); causal tools change activations, never weights.

Texts are "items": {user, reply, gen_ref}. gen_ref "gen/3.json:5" loads prompt and reply of saved generation 5 of
gen/3.json (so long replies need not be pasted); otherwise user (+ optional reply = assistant text so far) is used.
Positions index the REPLY: 0 = first reply token, -1 = last token of the whole text; with an empty reply, -1 is the
last prompt token (where the reply starts). Sites:
  resid.L        residual stream entering layer L (L = 0..N-1; resid.0 = embeddings); resid.N = after the last layer,
                 before the final norm
  <module>       input of a submodule under model.layers (e.g. model.layers.15.mlp.down_proj = the 3,584 MLP neurons)
  <module>:out   output of that submodule (e.g. model.layers.15.self_attn.o_proj:out = that attention block's output)
"""
from __future__ import annotations

import json
import re
from contextlib import contextmanager

import numpy as np

MAX_TOKENS = 16384
ATTN_MAX_TOKENS = 4096


class Interp:
    def __init__(self, svc):
        self.svc, self.tok, self.model, self.G = svc, svc.tok, svc.model, svc.G
        self.mods = dict(self.model.named_modules())
        self.n_layers = self.G.N_LAYERS
        self.layers = [self.mods[f"model.layers.{i}"] for i in range(self.n_layers)]
        self.norm = self.mods["model.norm"]
        self.W_U = self.model.get_output_embeddings().weight  # (vocab, hidden), tied
        self.dev = next(self.model.parameters()).device

    # ------------------------------------------------------------------ inputs
    def items(self, items: list[dict], thinking: bool, max_tokens: int = MAX_TOKENS) -> list[dict]:
        out = []
        for it in items:
            user, reply = it.get("user", ""), it.get("reply", "")
            ref = (it.get("gen_ref") or "").strip()
            if ref:
                f, _, i = ref.rpartition(":")
                rows = json.loads(self.svc._resolve(f).read_text())
                row = rows[int(i)]
                user, reply = row["prompt"], row["reply"]
                if reply.startswith("<think>") and thinking:  # server-split format -> raw continuation of the prompt
                    reply = reply[len("<think>"):]
            p = self.tok(self.svc._chat_text(user, thinking), add_special_tokens=False).input_ids
            r = self.tok(reply, add_special_tokens=False).input_ids if reply else []
            ids = (p + r)[:max_tokens]
            out.append({"ids": ids, "start": len(p), "n_reply": max(0, len(ids) - len(p))})
        return out

    @staticmethod
    def abs_pos(x: dict, p: int) -> int:
        q = x["start"] + p if p >= 0 else len(x["ids"]) + p
        if not 0 <= q < len(x["ids"]):
            raise ValueError(f"position {p} is outside this text (reply has {x['n_reply']} tokens)")
        return q

    def tokstr(self, ids, q: int, ctx: int = 0) -> str:
        return self.tok.decode(ids[max(0, q - ctx): q + 1]) if ctx else self.tok.decode([ids[q]])

    # ------------------------------------------------------------------ hooks
    def _site(self, s: str):
        if s.startswith("resid."):
            L = int(s.split(".")[1])
            if not 0 <= L <= self.n_layers:
                raise ValueError(f"{s}: L must be 0..{self.n_layers}")
            return ("pre", self.layers[L] if L < self.n_layers else self.norm)
        name, out = (s[:-4], True) if s.endswith(":out") else (s, False)
        if not name.startswith("model.layers.") or name not in self.mods:
            raise ValueError(f"unknown site {s}")
        return ("out" if out else "pre", self.mods[name])

    @contextmanager
    def hooked(self, sites: list[str], fn):
        """fn(site, tensor (T, d)) -> replacement tensor or None (read-only)."""
        hs = []
        try:
            for s in sites:
                kind, m = self._site(s)
                if kind == "pre":
                    def pre(mod, args, kwargs, s=s):
                        x = args[0] if args else kwargs["hidden_states"]
                        new = fn(s, x[0])
                        if new is None:
                            return None
                        x2 = x.clone()
                        x2[0] = new.to(x.dtype)
                        if args:
                            return (x2, *args[1:]), kwargs
                        kwargs["hidden_states"] = x2
                        return args, kwargs
                    hs.append(m.register_forward_pre_hook(pre, with_kwargs=True))
                else:
                    def post(mod, args, output, s=s):
                        y = output[0] if isinstance(output, tuple) else output
                        new = fn(s, y[0])
                        if new is None:
                            return None
                        y2 = y.clone()
                        y2[0] = new.to(y.dtype)
                        return (y2, *output[1:]) if isinstance(output, tuple) else y2
                    hs.append(m.register_forward_hook(post))
            yield
        finally:
            for h in hs:
                h.remove()

    def forward(self, ids, sites: list[str], positions: list[int] | None, edit=None, logits_at: list[int] | None = None):
        """Run one text; capture sites at absolute positions (None = all). edit(site, x) may return a replacement.
        Returns (captures {site: (n_pos, d) float32}, logits at `logits_at` (n, vocab) float32 or None)."""
        import torch
        cap: dict[str, np.ndarray] = {}

        def fn(s, x):
            if s in sites:
                sel = x if positions is None else x[positions]
                cap[s] = sel.float().cpu().numpy()
            return edit(s, x) if edit else None
        all_sites = sorted(set(sites) | (set(getattr(edit, "sites", [])) if edit else set()))
        with torch.no_grad(), self.hooked(all_sites, fn):
            t = torch.tensor([ids], device=self.dev)
            if logits_at is None:
                self.model(input_ids=t, logits_to_keep=1)
                return cap, None
            out = self.model(input_ids=t, logits_to_keep=torch.tensor(logits_at, device=self.dev))
            return cap, out.logits[0].float().cpu().numpy()

    def reply_logprobs(self, x: dict, edit=None, limit: int = MAX_TOKENS):
        """Teacher-forced log-prob, entropy and top-1 of every reply token (one forward pass; unembedding in chunks)."""
        import torch
        pos = list(range(x["start"] - 1, len(x["ids"]) - 1))[:limit]
        cap, _ = self.forward(x["ids"], [f"resid.{self.n_layers}"], pos, edit=edit)
        r = cap[f"resid.{self.n_layers}"]
        lp, ent, top1 = [], [], []
        for c in range(0, len(pos), 512):
            lsm = torch.log_softmax(torch.tensor(self.lens(r[c:c + 512])), -1)
            nxt = torch.tensor([x["ids"][q + 1] for q in pos[c:c + 512]])
            lp += lsm[torch.arange(len(nxt)), nxt].tolist()
            ent += (-(lsm.exp() * lsm).sum(-1)).tolist()
            top1 += lsm.argmax(-1).tolist()
        return np.array(lp), np.array(ent), top1

    def lens(self, r: np.ndarray):
        """Final norm + unembedding of residual vectors r (n, d) -> logits (n, vocab)."""
        import torch
        with torch.no_grad():
            x = torch.tensor(r, device=self.dev, dtype=self.W_U.dtype)
            return (self.norm(x) @ self.W_U.T).float().cpu().numpy()

    def top(self, logits: np.ndarray, k: int = 5) -> list:
        p = np.exp(logits - logits.max())
        p /= p.sum()
        i = np.argsort(-p)[:k]
        return [(self.tok.decode([int(j)]), round(float(p[j]), 4)) for j in i]

    def token_ids(self, words: list[str]) -> list[int]:
        """First token of each target string (as it would appear mid-text, i.e. without a leading space unless given)."""
        out = []
        for w in words:
            t = self.tok(w, add_special_tokens=False).input_ids
            if not t:
                raise ValueError(f"empty token for {w!r}")
            out.append(t[0])
        return out

    # ------------------------------------------------------------------ tools
    def trace(self, items, thinking, sites, positions, spans, stride) -> str:
        xs = self.items(items, thinking)
        res, meta = {s: [] for s in sites}, []
        for k, x in enumerate(xs):
            if stride and stride > 0:
                pos = list(range(x["start"], len(x["ids"]), stride))
            else:
                pos = [self.abs_pos(x, p) for p in positions]
            sp = [(x["start"] + a, min(len(x["ids"]), x["start"] + b)) for a, b in spans]
            need = sorted(set(pos) | {q for a, b in sp for q in range(a, b)})
            cap, _ = self.forward(x["ids"], sites, need)
            idx = {q: i for i, q in enumerate(need)}
            for s in sites:
                a = cap[s]
                rows = [a[idx[q]] for q in pos] + [a[[idx[q] for q in range(lo, hi)]].mean(0) if hi > lo
                                                   else np.full(a.shape[1], np.nan) for lo, hi in sp]
                res[s].append(np.stack(rows) if rows else np.zeros((0, a.shape[1])))
            meta.append({"item": k, "n_reply_tokens": x["n_reply"],
                         "positions": [{"abs": q, "reply_pos": q - x["start"], "token": self.tokstr(x["ids"], q)} for q in pos[:400]],
                         "spans": [[a - x["start"], b - x["start"]] for a, b in sp]})
        k = self.svc.n["analysis"]
        arrays = {}
        for s, lst in res.items():
            n = max(len(a) for a in lst)
            arr = np.full((len(lst), n, lst[0].shape[1]), np.nan, np.float32)
            for i, a in enumerate(lst):
                arr[i, :len(a)] = a
            arrays[s] = arr
        self.svc.save_npz(f"acts/trace_{k}.npz", arrays)
        self.svc.write(f"acts/trace_{k}.json", json.dumps(meta, indent=1).encode())
        return (f"saved acts/trace_{k}.npz (" + ", ".join(f"{s}: {a.shape}" for s, a in arrays.items()) +
                ") as (item, position [then spans], width); positions, tokens and spans in acts/trace_{k}.json. "
                f"Reply lengths: {[x['n_reply'] for x in xs]} tokens.")

    def token_stats(self, items, thinking) -> str:
        xs = self.items(items, thinking)
        k, summ, dump = self.svc.n["analysis"], [], []
        for i, x in enumerate(xs):
            if x["n_reply"] < 1:
                raise ValueError("token_stats needs a reply (or gen_ref) to score")
            lp, ent, top1 = self.reply_logprobs(x)
            toks = [self.tok.decode([t]) for t in x["ids"][x["start"]:]]
            dump.append({"item": i, "tokens": toks, "logprob": np.round(lp, 3).tolist(), "entropy": np.round(ent, 3).tolist(),
                         "top1": [self.tok.decode([t]) for t in top1]})
            worst = np.argsort(lp)[:8]
            summ.append(f"[{i}] {x['n_reply']} reply tokens; mean logprob {lp.mean():.3f}, mean entropy {ent.mean():.3f}; "
                        f"by quarter entropy {[round(float(q.mean()), 3) for q in np.array_split(ent, 4)]}; "
                        "least likely tokens (reply pos, token, logprob): " +
                        ", ".join(f"({int(j)}, {toks[j]!r}, {lp[j]:.2f})" for j in worst))
        self.svc.write(f"acts/token_stats_{k}.json", json.dumps(dump).encode())
        return f"saved acts/token_stats_{k}.json (per reply token: token, logprob, entropy, model's top-1)\n" + "\n".join(summ)

    def logit_lens(self, items, thinking, positions, layers, targets) -> str:
        xs = self.items(items, thinking)
        layers = layers or list(range(0, self.n_layers + 1, 2)) + ([self.n_layers] if self.n_layers % 2 else [])
        sites = [f"resid.{L}" for L in layers]
        tids = self.token_ids(targets) if targets else []
        lines, k, store = [], self.svc.n["analysis"], {}
        for i, x in enumerate(xs):
            pos = [self.abs_pos(x, p) for p in positions][:16]
            cap, _ = self.forward(x["ids"], sites, pos)
            for j, q in enumerate(pos):
                lines.append(f"[{i}] reply pos {q - x['start']} token {self.tokstr(x['ids'], q)!r} (context "
                             f"{self.tokstr(x['ids'], q, 12)!r}):")
                for s, L in zip(sites, layers):
                    lg = self.lens(cap[s][j:j + 1])[0]
                    extra = ""
                    if tids:
                        rk = (-lg).argsort().argsort()
                        extra = "  targets " + ", ".join(f"{t!r}: rank {int(rk[tid])}" for t, tid in zip(targets, tids))
                    lines.append(f"   L{L:>2}: {self.top(lg, 5)}{extra}")
                    store[f"item{i}_pos{q - x['start']}_L{L}"] = lg[tids] if tids else np.zeros(0)
        return "\n".join(lines)[:20000]

    def attribution(self, item, thinking, position, targets) -> str:
        """Direct logit attribution: each attention/MLP block's output (and the embeddings), passed through the final
        norm's per-coordinate scale at this position, dotted with the unembedding of each target token."""
        x = self.items([item], thinking)[0]
        q = self.abs_pos(x, position)
        tids = self.token_ids(targets)
        attn = [f"model.layers.{L}.{'self_attn.o_proj' if 'self_attn' in self._mixer(L) else 'linear_attn.out_proj'}:out"
                for L in range(self.n_layers)]
        mlp = [f"model.layers.{L}.mlp.down_proj:out" for L in range(self.n_layers)]
        sites = ["resid.0", f"resid.{self.n_layers}"] + attn + mlp
        cap, lg = self.forward(x["ids"], sites, [q], logits_at=[q])
        r = cap[f"resid.{self.n_layers}"][0]
        import torch
        with torch.no_grad():
            y = self.norm(torch.tensor(r[None], device=self.dev, dtype=self.W_U.dtype))[0].float().cpu().numpy()
        scale = np.where(np.abs(r) > 1e-8, y / np.where(np.abs(r) > 1e-8, r, 1), 0.0)
        U = self.W_U[tids].detach().float().cpu().numpy()  # (n_targets, d)
        contrib = lambda v: (U @ (v * scale)).round(3).tolist()  # noqa: E731
        recon = cap["resid.0"][0] + sum(cap[s][0] for s in attn + mlp)
        lines = [f"position {position} token {self.tokstr(x['ids'], q)!r}, context {self.tokstr(x['ids'], q, 16)!r}",
                 f"model's next-token top-5 here: {self.top(lg[0])}",
                 f"targets {targets}; total logits {(U @ y).round(3).tolist()}; decomposition error "
                 f"{float(np.linalg.norm(recon - r) / (np.linalg.norm(r) + 1e-9)):.2e}",
                 f"embeddings: {contrib(cap['resid.0'][0])}"]
        for L in range(self.n_layers):
            lines.append(f"layer {L:>2} {'attn ' if 'self_attn' in attn[L] else 'lin-attn'}: {contrib(cap[attn[L]][0])}"
                         f"   mlp: {contrib(cap[mlp[L]][0])}")
        return "\n".join(lines)

    def _mixer(self, L: int) -> str:
        return "self_attn" if f"model.layers.{L}.self_attn" in self.mods else "linear_attn"

    def attention(self, item, thinking, layers, positions, top_k) -> str:
        import torch
        x = self.items([item], thinking, max_tokens=ATTN_MAX_TOKENS)[0]
        full = [L for L in range(self.n_layers) if self._mixer(L) == "self_attn"]
        layers = [L for L in (layers or full) if L in full]
        if not layers:
            return f"no full-attention layers selected; full attention is in layers {full}"
        qs = [self.abs_pos(x, p) for p in positions][:8]
        prev = getattr(self.model.config, "_attn_implementation", "sdpa")
        self.model.set_attn_implementation("eager")
        try:
            with torch.no_grad():
                out = self.model(input_ids=torch.tensor([x["ids"]], device=self.dev), output_attentions=True,
                                 logits_to_keep=1)
        finally:
            self.model.set_attn_implementation(prev)
        att = out.attentions
        if att is not None and len(att) == len(full) != self.n_layers:  # only the full-attention layers returned
            att = {L: att[i] for i, L in enumerate(full)}
        elif att is not None:
            att = {L: att[L] for L in range(len(att))}
        else:
            return "attention weights unavailable for this model"
        lines = [f"text truncated to {len(x['ids'])} tokens; reply starts at abs {x['start']}"]
        # sentence/line segmentation of the reply for a "which earlier parts receive attention" summary
        bounds, cur = [], x["start"]
        for i in range(x["start"], len(x["ids"])):
            if re.search(r"[.\n?!]", self.tok.decode([x["ids"][i]])):
                bounds.append((cur, i + 1))
                cur = i + 1
        if cur < len(x["ids"]):
            bounds.append((cur, len(x["ids"])))
        for L in layers:
            a = att.get(L)
            if a is None:
                lines.append(f"layer {L}: attention weights unavailable")
                continue
            a = a[0].float().cpu().numpy()  # (heads, T, T)
            for q in qs:
                w = a[:, q, : q + 1]
                mean = w.mean(0)
                top = np.argsort(-mean)[:top_k]
                lines.append(f"layer {L} query reply pos {q - x['start']} ({self.tokstr(x['ids'], q)!r}): top keys "
                             + ", ".join(f"{int(j) - x['start']}:{self.tokstr(x['ids'], int(j))!r}={mean[j]:.3f}" for j in top)
                             + f"; prompt share {mean[:x['start']].sum():.2f}")
            if bounds:
                lo = max(x["start"], len(x["ids"]) - 256)
                recv = [(a[:, lo:, s:e].sum(-1).mean()) for s, e in bounds]
                best = np.argsort(recv)[::-1][:5]
                lines.append(f"layer {L}: reply segments receiving most attention from the last {len(x['ids']) - lo} "
                             "tokens: " + "; ".join(f"[{bounds[b][0] - x['start']}:{bounds[b][1] - x['start']}] "
                                                    f"{self.tok.decode(x['ids'][bounds[b][0]:bounds[b][1]])[:80]!r} "
                                                    f"({recv[b]:.3f})" for b in best))
        return "\n".join(lines)[:20000]

    def top_activations(self, site, neuron, direction, thinking, top_k) -> str:
        """Scan your generations so far (gen/*.json replies) and examples.jsonl problems for the token positions where
        a neuron (index into the site's vector) or a direction (.npy of the site's width) is most active."""
        corpus = []
        for f in sorted(self.svc.work.glob("gen/*.json")):
            for i, row in enumerate(json.loads(f.read_text()) if f.stat().st_size < 50_000_000 else []):
                if isinstance(row, dict) and "prompt" in row:
                    corpus.append({"user": row["prompt"], "reply": row.get("reply", ""), "gen_ref": "",
                                   "src": f"{f.parent.name}/{f.name}:{i}"})
        ex = self.svc.work / "examples.jsonl"
        if ex.exists():
            for i, l in enumerate(ex.read_text().splitlines()[:32]):
                d = json.loads(l)
                u = d.get("problem") or d.get("question") or d.get("user") or ""
                corpus.append({"user": u, "reply": "", "gen_ref": "", "src": f"examples.jsonl:{i}"})
        corpus = corpus[-64:]
        vec = None
        if direction:
            vec = np.load(self.svc._resolve(direction)).astype(np.float32).ravel()
        hits = []
        for c in corpus:
            x = self.items([c], thinking, max_tokens=4096)[0]
            cap, _ = self.forward(x["ids"], [site], None)
            a = cap[site]
            sc = a @ vec if vec is not None else a[:, int(neuron)]
            for q in np.argsort(-sc)[:3]:
                hits.append((float(sc[q]), c["src"], int(q) - x["start"], self.tokstr(x["ids"], int(q), 16)))
        hits.sort(key=lambda h: -h[0])
        return (f"scanned {len(corpus)} texts (your generations and examples, <= 4,096 tokens each) at {site}\n" +
                "\n".join(f"{s:.3f}  {src} reply pos {p}: ...{ctx!r}" for s, src, p, ctx in hits[:top_k]))

    def patch(self, source, target, thinking, sites, source_positions, target_positions, targets) -> str:
        """Copy activations at `sites` from the source text (at source_positions) into the target text (at
        target_positions) and report how the target's next-token prediction at its last position changes."""
        xs, xt = self.items([source], thinking)[0], self.items([target], thinking)[0]
        sp = [self.abs_pos(xs, p) for p in source_positions]
        tp = [self.abs_pos(xt, p) for p in target_positions]
        if len(sp) != len(tp):
            raise ValueError("source_positions and target_positions must have the same length")
        cap, _ = self.forward(xs["ids"], sites, sp)
        import torch

        def edit(s, x):
            if s not in cap:
                return None
            y = x.clone()
            y[tp] = torch.tensor(cap[s], device=x.device, dtype=x.dtype)
            return y
        edit.sites = sites  # type: ignore[attr-defined]
        last = len(xt["ids"]) - 1
        _, before = self.forward(xt["ids"], [], None, logits_at=[last])
        _, after = self.forward(xt["ids"], [], None, edit=edit, logits_at=[last])
        return self._compare(before[0], after[0], targets, "patched")

    def _compare(self, b, a, targets, what) -> str:
        pb, pa = np.exp(b - b.max()), np.exp(a - a.max())
        pb, pa = pb / pb.sum(), pa / pa.sum()
        kl = float((pb * (np.log(pb + 1e-12) - np.log(pa + 1e-12))).sum())
        out = [f"next token before: {self.top(b)}", f"next token {what}: {self.top(a)}", f"KL(before || {what}) = {kl:.4f}"]
        if targets:
            for t, tid in zip(targets, self.token_ids(targets)):
                out.append(f"  {t!r}: logit {b[tid]:.3f} -> {a[tid]:.3f}, prob {pb[tid]:.4f} -> {pa[tid]:.4f}")
        return "\n".join(out)

    def intervene(self, items, thinking, interventions, positions, targets) -> str:
        """Track B: zero/scale neurons or add a direction at sites (all positions), then report the next-token change
        at `positions` and the change in mean log-probability of each item's reply (teacher-forced)."""
        import torch
        specs = []
        for iv in interventions:
            d = None
            if iv.get("direction"):
                d = torch.tensor(np.load(self.svc._resolve(iv["direction"])).astype(np.float32).ravel())
            specs.append((iv["site"], iv["kind"], [int(n) for n in iv.get("neurons", [])], d, float(iv.get("alpha", 0.0))))

        def edit(s, x):
            y = None
            for site, kind, neurons, d, alpha in specs:
                if site != s:
                    continue
                y = x.clone() if y is None else y
                if kind == "zero":
                    y[:, neurons] = 0
                elif kind == "scale":
                    y[:, neurons] = y[:, neurons] * alpha
                elif kind == "add":
                    y = y + alpha * d.to(y.device, y.dtype)
                else:
                    raise ValueError(f"unknown kind {kind}")
            return y
        edit.sites = sorted({s[0] for s in specs})  # type: ignore[attr-defined]
        xs, lines = self.items(items, thinking), []
        for i, x in enumerate(xs):
            pos = [self.abs_pos(x, p) for p in positions][:8]
            _, b = self.forward(x["ids"], [], None, logits_at=pos)
            _, a = self.forward(x["ids"], [], None, edit=edit, logits_at=pos)
            for j, q in enumerate(pos):
                lines.append(f"[{i}] reply pos {q - x['start']} ({self.tokstr(x['ids'], q, 8)!r}):\n" +
                             self._compare(b[j], a[j], targets, "intervened"))
            if x["n_reply"] > 0:
                (b_lp, _, _), (a_lp, _, _) = self.reply_logprobs(x), self.reply_logprobs(x, edit=edit)
                lines.append(f"[{i}] reply mean logprob ({len(b_lp)} tokens): {b_lp.mean():.4f} -> {a_lp.mean():.4f}; "
                             f"by quarter {[round(float(q.mean()), 3) for q in np.array_split(b_lp, 4)]} -> "
                             f"{[round(float(q.mean()), 3) for q in np.array_split(a_lp, 4)]}")
        return "\n".join(lines)[:20000]
