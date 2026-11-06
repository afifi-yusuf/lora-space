# Chess diagnosis, 2026-11-06 (Qwen3.5-0.8B and 2B, `scripts/chess_diag.py`)

300 mate-in-1 and 300 other Lichess puzzles (rating 800–2000). The prompt gives the FEN and asks for one UCI move.
Thinking off is greedy; thinking on uses the think35 sampling with a 4,096-token budget. Stockfish depth 12.

| | 0.8B off | 2B off | 0.8B think 4K | 2B think 4K | Random legal move |
|---|---|---|---|---|---|
| Reply is one move, UCI or SAN | 99.7% | 100% | 0% | 0% | |
| Reply is one UCI move (as asked) | 4.3% | 40.0% | 0% | 0% | |
| Legal move (mate1 / puzzles) | 10.3 / 11.3% | 13.3 / 13.3% | 0 / 0% | 0 / 0% | 100% |
| Mate in 1 found | 0.0% | 0.3% | 0% | 0% | 5.3% |
| Puzzle's first move found | 0.0% | 0.3% | 0% | 0% | 6.0% |
| Blunders (≥ 300 cp) among legal moves | 97% | 95% | | | |
| Thinking finished within 4K tokens | | | 0 / 600 | 1 / 600 | |

- Thinking off, both models answer with a stock opening move whatever the position: 0.8B `e4` 133/300 and `e6` 64/300;
  2B `e2e4` 104/300 and `Qf6` 59/300. They do not read the board.
- Thinking on, they spend the whole budget trying to parse the FEN rank by rank and get it wrong (the 2B often loops on
  `/R/R/R...`). Parsing the FEN is the bottleneck, not search.
- So "make it good at chess" is skill-tier from level 2 (legal moves) onward. Only the UCI format (level 1) is rule-tier.
