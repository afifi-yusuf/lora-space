# Paper — LoRA-Space Optimization (arXiv preprint draft)

```
paper/
  main.tex            document root (article class, natbib/plainnat, hyperref, cleveref)
  macros.tex          notation + writing aids: \todo{}, \pending{} (number awaiting a run), \yusuf{}
  sections/           one file per section; A_/B_/C_ are appendices
  figures/            figures (PDF/PNG) — generate from results/ with scripts, don't hand-edit
  references.bib      bibliography — verified 2026-11-05 (arXiv, Semantic Scholar/DBLP, NeurIPS proceedings)
  verify_refs.py      re-checks every entry against Semantic Scholar
```

**Build locally:** `cd paper && tectonic main.tex` (or `latexmk -pdf main.tex`).

**Numbers** in the draft come from `results/` (README files and JSON) as of 2026-11-05 and are single runs. Every
number that will change is near a `\todo{}`; search for `TODO` before submitting.

**Before arXiv submission**
1. Replace single runs with multi-seed means ± s.d.; finish MATH-500 sampled accuracy (`\pending`).
2. Re-run `python3 verify_refs.py` for any newly added references (existing entries verified 2026-11-05).
3. Remove writing aids: in `macros.tex`, `\renewcommand{\todo}[1]{}` (and check none remain).
4. arXiv compiles with pdflatex + bibtex: upload `main.tex`, `macros.tex`, `sections/`, `figures/`, and the generated
   `main.bbl` (arXiv prefers the .bbl over running bibtex).
5. Decide what to release (code, prompts, logs) and add the public URL to the conclusion.
