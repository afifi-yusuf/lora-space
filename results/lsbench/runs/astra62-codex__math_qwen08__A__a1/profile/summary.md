# agprof summary

- Duration: **2280.205 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **41 calls**, 41 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1017.277 s total wait
- Tools: **111/112 completed**, 0 failed, 1 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **211203** at 1.973 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2276708.037 / 2276708.037 ms |
| LLM latency p50 / p95 | 21362.362 / 57652.559 ms |
| LLM TTFT p50 / p95 | 8506.495 / 10844.891 ms |
| LLM input / output tokens | 3315081 / 93824 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 41 total, 41 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {"unmatched_completions": 1}
- codex: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 41/42 | 41 | 0 | 1 | n/a | n/a |
| mcp__agency__attribution | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 25/25 | 25 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 29/29 | 29 | 0 | 0 | n/a | n/a |
| update_plan | 6/6 | 6 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 27.581% | 181.602% | 629.511 s | 10251.488 MB | 11556.660 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 2241 |  | 2262 | 1.384% | 5.958% | 31.590 s | 1789.779 MB | 1790.355 MB | 11060.092 MB | 11061.582 MB | 0.007812 MB | 0.191406 MB |
| lsb_grid_worker | 2172 |  | 2262 | 0.000% | 0.000% | 0.000 s | 3.312 MB | 3.312 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| docker | 2645 |  | 1 | n/a% | n/a% | n/a s | 29.148 MB | 29.148 MB | 1843.520 MB | 1843.520 MB | n/a MB | n/a MB |
| python | 2181 |  | 2262 | 11.044% | 181.813% | 252.000 s | 3311.365 MB | 4495.473 MB | 16643.186 MB | 19378.805 MB | 171.261719 MB | 4028.558594 MB |
| python | 2409 |  | 2262 | 0.000% | 0.000% | 0.000 s | 12.191 MB | 12.191 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 2410 |  | 2262 | 15.136% | 43.680% | 345.500 s | 2327.926 MB | 2328.668 MB | 21238.868 MB | 21239.301 MB | 0.000000 MB | 0.011719 MB |
| docker-buildx | 2655 |  | 1 | n/a% | n/a% | n/a s | 38.027 MB | 38.027 MB | 1298.227 MB | 1298.227 MB | n/a MB | n/a MB |
| docker-init | 2753 | sandbox_agent_lsb-codex_0000_0000 | 2258 | 0.002% | 0.995% | 0.040 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2787 | sandbox_agent_lsb-codex_0000_0000 | 2258 | 0.002% | 0.995% | 0.050 s | 1.246 MB | 1.246 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 2878 | sandbox_agent_lsb-codex_0000_0000 | 2258 | 27.463% | 95.332% | 624.710 s | 117.999 MB | 137.395 MB | 989.813 MB | 1046.566 MB | n/a MB | n/a MB |
| python3 | 2884 | sandbox_agent_lsb-codex_0000_0000 | 3 | 57.643% | 67.592% | 1.160 s | 42.884 MB | 72.961 MB | 53.128 MB | 90.941 MB | n/a MB | n/a MB |
| codex | 2893 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.535 MB | 0.535 MB | 246.516 MB | 246.516 MB | n/a MB | n/a MB |
| codex | 2902 | sandbox_agent_lsb-codex_0000_0000 | 2230 | 3.336% | 23.841% | 75.000 s | 139.625 MB | 150.578 MB | 392.224 MB | 495.590 MB | n/a MB | n/a MB |
| git | 2980 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.695 MB | 6.695 MB | 224.297 MB | 224.297 MB | n/a MB | n/a MB |
| python3 | 2984 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.527 MB | 8.527 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| git | 2975 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.859 MB | 3.859 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| sort | 3067 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.426 MB | 1.426 MB | 15.051 MB | 15.051 MB | n/a MB | n/a MB |
| bash | 3063 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| rg | 3066 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.504 MB | 0.504 MB | 5.617 MB | 5.617 MB | n/a MB | n/a MB |
| python3 | 3166 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.113 MB | 10.113 MB | 14.977 MB | 14.977 MB | n/a MB | n/a MB |
| python3 | 3305 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.117 MB | 20.117 MB | 25.070 MB | 25.070 MB | n/a MB | n/a MB |
| tokio-rt-worker | 3384 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 128.609 MB | 128.609 MB | 390.156 MB | 390.156 MB | n/a MB | n/a MB |
| python3 | 3954 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.500 MB | 21.500 MB | 27.059 MB | 27.059 MB | n/a MB | n/a MB |
| python3 | 4571 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.539 MB | 10.539 MB | 15.188 MB | 15.188 MB | n/a MB | n/a MB |
| find | 4575 | sandbox_agent_lsb-codex_0000_0000 | 2 | 21.868% | 21.868% | 0.220 s | 2.711 MB | 2.711 MB | 4.918 MB | 4.918 MB | n/a MB | n/a MB |
| head | 4576 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.457 MB | 1.457 MB | 2.859 MB | 2.859 MB | n/a MB | n/a MB |
| bash | 4572 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 4653 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.750 MB | 4.750 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 4861 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.668 MB | 9.668 MB | 13.609 MB | 13.609 MB | n/a MB | n/a MB |
| python | 4936 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.742 MB | 13.742 MB | 207.363 MB | 207.363 MB | n/a MB | n/a MB |
| bash | 4934 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.973 MB | 2.973 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 4944 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.160 MB | 17.160 MB | 22.355 MB | 22.355 MB | n/a MB | n/a MB |
| python3 | 4949 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.703 MB | 11.703 MB | 19.828 MB | 19.828 MB | n/a MB | n/a MB |
| python | 5098 | sandbox_agent_lsb-codex_0000_0000 | 20 | 170.936% | 179.064% | 32.840 s | 199.374 MB | 325.332 MB | 1865.757 MB | 1959.020 MB | n/a MB | n/a MB |
| python3 | 5108 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.262 MB | 14.262 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python3 | 5109 | sandbox_agent_lsb-codex_0000_0000 | 4 | 3.294% | 5.958% | 0.100 s | 14.622 MB | 20.375 MB | 19.890 MB | 25.582 MB | n/a MB | n/a MB |
| python3 | 5347 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.660 MB | 5.660 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| python3 | 5416 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.547 MB | 19.547 MB | 24.805 MB | 24.805 MB | n/a MB | n/a MB |
| python3 | 5475 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.367 MB | 19.367 MB | 24.938 MB | 24.938 MB | n/a MB | n/a MB |
| bash | 5513 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.918 MB | 2.918 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5515 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 71.934 MB | 71.934 MB | 1929.219 MB | 1929.219 MB | n/a MB | n/a MB |
| python3 | 5595 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.609 MB | 9.609 MB | 13.738 MB | 13.738 MB | n/a MB | n/a MB |
| python3 | 5658 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.836 MB | 14.836 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python3 | 5676 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.609 MB | 15.609 MB | 20.504 MB | 20.504 MB | n/a MB | n/a MB |
| python | 5681 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 158.137 MB | 158.137 MB | 2018.352 MB | 2018.352 MB | n/a MB | n/a MB |
| bash | 5710 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.008 MB | 3.008 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5711 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.477 MB | 7.477 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 5740 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.766 MB | 14.766 MB | 210.047 MB | 210.047 MB | n/a MB | n/a MB |
| python3 | 5754 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.828 MB | 10.828 MB | 15.215 MB | 15.215 MB | n/a MB | n/a MB |
| bash | 5768 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.000 MB | 3.000 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5769 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.711 MB | 14.711 MB | 128.445 MB | 128.445 MB | n/a MB | n/a MB |
| python3 | 5771 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.160 MB | 16.160 MB | 20.852 MB | 20.852 MB | n/a MB | n/a MB |
| python3 | 5777 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.395 MB | 8.395 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python | 5797 | sandbox_agent_lsb-codex_0000_0000 | 65 | 168.418% | 176.712% | 108.750 s | 539.617 MB | 613.188 MB | 2081.135 MB | 2144.551 MB | n/a MB | n/a MB |
| python3 | 5806 | sandbox_agent_lsb-codex_0000_0000 | 5 | 3.468% | 6.937% | 0.140 s | 13.814 MB | 21.496 MB | 18.894 MB | 27.055 MB | n/a MB | n/a MB |
| python3 | 5807 | sandbox_agent_lsb-codex_0000_0000 | 3 | 2.486% | 2.983% | 0.050 s | 13.652 MB | 16.711 MB | 18.664 MB | 22.145 MB | n/a MB | n/a MB |
| python3 | 5808 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.859 MB | 20.859 MB | 25.836 MB | 25.836 MB | n/a MB | n/a MB |
| python3 | 5823 | sandbox_agent_lsb-codex_0000_0000 | 4 | 2.647% | 3.976% | 0.080 s | 13.327 MB | 18.590 MB | 18.514 MB | 24.684 MB | n/a MB | n/a MB |
| python3 | 5830 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.602 MB | 14.602 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python | 5833 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.539 MB | 5.539 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| bash | 5832 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.055 MB | 3.055 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 5834 | sandbox_agent_lsb-codex_0000_0000 | 5 | 3.480% | 5.968% | 0.140 s | 13.906 MB | 21.273 MB | 18.972 MB | 27.078 MB | n/a MB | n/a MB |
| bash | 5846 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.754 MB | 2.754 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5847 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 148.016 MB | 148.016 MB | 1928.484 MB | 1928.484 MB | n/a MB | n/a MB |
| python3 | 5852 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.691 MB | 10.691 MB | 15.281 MB | 15.281 MB | n/a MB | n/a MB |
| python3 | 5865 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.660 MB | 14.660 MB | 20.000 MB | 20.000 MB | n/a MB | n/a MB |
| python3 | 5867 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.539 MB | 14.539 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| bash | 5868 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.762 MB | 2.762 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5870 | sandbox_agent_lsb-codex_0000_0000 | 2 | 55.571% | 55.571% | 0.560 s | 311.742 MB | 477.750 MB | 2009.404 MB | 2133.480 MB | n/a MB | n/a MB |
| python | 5869 | sandbox_agent_lsb-codex_0000_0000 | 10 | 133.786% | 174.754% | 12.170 s | 404.007 MB | 750.000 MB | 2305.958 MB | 2819.191 MB | n/a MB | n/a MB |
| bash | 5942 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.172 MB | 3.172 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5943 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 151.211 MB | 151.211 MB | 2010.840 MB | 2010.840 MB | n/a MB | n/a MB |
| python3 | 5997 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.270 MB | 7.270 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| python3 | 6003 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.312 MB | 20.312 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| python | 6050 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.250 MB | 18.250 MB | 209.898 MB | 209.898 MB | n/a MB | n/a MB |
| bash | 6045 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.820 MB | 2.820 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 6086 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.328 MB | 10.328 MB | 13.977 MB | 13.977 MB | n/a MB | n/a MB |
| bash | 6218 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.707 MB | 2.707 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 6224 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.039 MB | 3.039 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6228 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 48.305 MB | 48.305 MB | 1921.102 MB | 1921.102 MB | n/a MB | n/a MB |
| bash | 6252 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.008 MB | 3.008 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6254 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.664 MB | 7.664 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 6279 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.504 MB | 21.504 MB | 26.984 MB | 26.984 MB | n/a MB | n/a MB |
| python3 | 6300 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.562 MB | 18.562 MB | 24.176 MB | 24.176 MB | n/a MB | n/a MB |
| python3 | 6302 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.945 MB | 6.945 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python3 | 6332 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.047 MB | 5.047 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| tokio-rt-worker | 6333 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 142.457 MB | 142.457 MB | 392.207 MB | 392.207 MB | n/a MB | n/a MB |
| bash | 6338 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.977 MB | 2.977 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6337 | sandbox_agent_lsb-codex_0000_0000 | 7 | 125.281% | 176.810% | 7.570 s | 550.827 MB | 1191.156 MB | 2406.464 MB | 3469.562 MB | n/a MB | n/a MB |
| bash | 6335 | sandbox_agent_lsb-codex_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 3.102 MB | 3.102 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6340 | sandbox_agent_lsb-codex_0000_0000 | 2 | 89.260% | 89.260% | 0.900 s | 163.955 MB | 217.035 MB | 1994.814 MB | 2058.566 MB | n/a MB | n/a MB |
| python3 | 6366 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.820 MB | 21.820 MB | 27.055 MB | 27.055 MB | n/a MB | n/a MB |
| python3 | 6375 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.770 MB | 19.770 MB | 24.938 MB | 24.938 MB | n/a MB | n/a MB |
| bash | 6376 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.898 MB | 2.898 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6379 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 151.055 MB | 151.055 MB | 1929.812 MB | 1929.812 MB | n/a MB | n/a MB |
| python3 | 6409 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.180 MB | 7.180 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 6447 | sandbox_agent_lsb-codex_0000_0000 | 2 | 124.283% | 124.283% | 1.250 s | 265.756 MB | 512.148 MB | 1090.832 MB | 2009.309 MB | n/a MB | n/a MB |
| bash | 6445 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.801 MB | 2.801 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 6457 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.430 MB | 21.430 MB | 26.984 MB | 26.984 MB | n/a MB | n/a MB |
| python | 6470 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 116.664 MB | 116.664 MB | 1935.852 MB | 1935.852 MB | n/a MB | n/a MB |
| bash | 6468 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.008 MB | 3.008 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| bash | 6505 | sandbox_agent_lsb-codex_0000_0000 | 13 | 6.773% | 81.275% | 0.820 s | 10.398 MB | 99.590 MB | 170.773 MB | 2168.949 MB | n/a MB | n/a MB |
| python | 6507 | sandbox_agent_lsb-codex_0000_0000 | 12 | 154.539% | 176.217% | 17.110 s | 525.805 MB | 845.957 MB | 2384.866 MB | 2941.996 MB | n/a MB | n/a MB |
| python3 | 6540 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.191 MB | 20.191 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| docker | 6586 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.441 MB | 30.441 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 46.403% | 100.000% | 11974.099 MB | 13268.000 MB | 49.228 W | 79.816 W | 112273.466 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 40.935% | 208.274% | 931.429 s | 545.240 MB | 1723.008 MB | 237.207031 MB | 192.855469 MB | 25.040910 MB | 1.739074 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2643 | 2280.140 | interrupted |
| tool:Bash | -1 | 778.089 | interrupted |
| harness:retire | -1 | 0.385 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2276.708 | n/a | n/a | 237.207 | 2276708.037 | 2276708.037 | 2276708.037 |
| engine:execute | 1/1 | 0 | 0 | 2276.706 | 2.984 | 2273.712 | 237.207 | 2276706.052 | 2276706.052 | 2276706.052 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2248.070 | 0.004 | 2248.065 | 195.857 | 2248069.707 | 2248069.707 | 2248069.707 |
| harness:await_cli | 1/1 | 0 | 0 | 2244.447 | n/a | n/a | 58.906 | 2244446.971 | 2244446.971 | 2244446.971 |
| llm:attempt | 41/41 | 0 | 0 | 1017.277 | 5.132 | 1012.070 | 10.793 | 24811.635 | 21362.362 | 57652.559 |
| tool:mcp__agency__generate | 25/25 | 0 | 0 | 937.727 | n/a | n/a | 3.767 | 37509.068 | 26236.563 | 95389.750 |
| tool:Bash | 41/42 | 0 | 1 | 411.598 | n/a | n/a | 57.334 | 10038.978 | 893.142 | 71129.729 |
| tool:mcp__agency__trace | 29/29 | 0 | 0 | 143.545 | n/a | n/a | 0.120 | 4949.837 | 4208.835 | 11494.480 |
| tool:mcp__agency__token_stats | 1/1 | 0 | 0 | 48.141 | n/a | n/a | 0.000 | 48140.688 | 48140.688 | 48140.688 |
| run:container_call | 13/13 | 0 | 0 | 23.126 | 0.002 | 23.124 | 0.000 | 1778.921 | 36.725 | 9137.194 |
| teardown:commit | 1/1 | 0 | 0 | 22.468 | 0.004 | 22.463 | 0.000 | 22467.504 | 22467.504 | 22467.504 |
| sandbox:commit | 1/1 | 0 | 0 | 22.279 | 0.003 | 22.276 | 0.000 | 22278.587 | 22278.587 | 22278.587 |
| checkpoint.total | 1/1 | 0 | 0 | 22.278 | 0.002 | 22.276 | 0.000 | 22278.422 | 22278.422 | 22278.422 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.278 | 0.002 | 22.276 | 0.000 | 22278.258 | 22278.258 | 22278.258 |
| tool:mcp__agency__attribution | 2/2 | 0 | 0 | 5.944 | n/a | n/a | 0.042 | 2971.759 | 2971.759 | 5354.944 |
| tool:mcp__agency__logit_lens | 2/2 | 0 | 0 | 5.007 | n/a | n/a | 0.008 | 2503.301 | 2503.301 | 2849.071 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.713 | 1.063 | 3.650 | 41.196 | 4713.256 | 4713.256 | 4713.256 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.713 | 1.063 | 3.650 | 41.196 | 4712.957 | 4712.957 | 4712.957 |
| syscall:connect | 930/930 | 0 | 0 | 2.593 | n/a | n/a | 5.440 | 2.788 | 2.145 | 4.798 |
| tool:mcp__agency__inspect_module_inputs | 2/2 | 0 | 0 | 1.973 | n/a | n/a | 0.046 | 986.662 | 986.662 | 1168.436 |
| syscall:sendto | 620/620 | 0 | 0 | 1.691 | n/a | n/a | 3.647 | 2.728 | 2.375 | 4.701 |
| syscall:execve | 972/972 | 0 | 0 | 1.685 | n/a | n/a | 7.072 | 1.734 | 1.289 | 3.086 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.427 | n/a | n/a | 85.730 | 1426.799 | 1426.799 | 1426.799 |
| harness:submit | 1/1 | 0 | 0 | 1.212 | n/a | n/a | 18.410 | 1212.292 | 1212.292 | 1212.292 |
| sandbox:create | 1/1 | 0 | 0 | 1.096 | 0.245 | 0.851 | 0.000 | 1095.524 | 1095.524 | 1095.524 |
| tool:update_plan | 6/6 | 0 | 0 | 1.080 | n/a | n/a | 1.132 | 180.030 | 177.813 | 198.021 |
| harness:snapshot | 1/1 | 0 | 0 | 0.798 | n/a | n/a | 0.181 | 798.026 | 798.026 | 798.026 |
| run:detect | 1/1 | 0 | 0 | 0.789 | 0.001 | 0.788 | 0.000 | 788.943 | 788.943 | 788.943 |
| tool:mcp__agency__inspect | 1/1 | 0 | 0 | 0.648 | n/a | n/a | 0.000 | 647.669 | 647.669 | 647.669 |
| sandbox:start | 1/1 | 0 | 0 | 0.590 | 0.002 | 0.588 | 0.000 | 589.884 | 589.884 | 589.884 |
| runtime.container_create | 1/1 | 0 | 0 | 0.590 | 0.002 | 0.588 | 0.000 | 589.737 | 589.737 | 589.737 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.303 | n/a | n/a | 0.000 | 302.998 | 302.998 | 302.998 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.246 | n/a | n/a | 0.000 | 246.283 | 246.283 | 246.283 |
| sandbox:stop | 1/1 | 0 | 0 | 0.189 | 0.001 | 0.187 | 0.000 | 188.663 | 188.663 | 188.663 |
| agency:services_close | 1/1 | 0 | 0 | 0.146 | 0.000 | 0.145 | 0.008 | 145.849 | 145.849 | 145.849 |
| agency:services_start | 1/1 | 0 | 0 | 0.104 | 0.045 | 0.060 | 0.000 | 104.225 | 104.225 | 104.225 |
| harness:launch | 1/1 | 0 | 0 | 0.051 | n/a | n/a | 2.953 | 51.098 | 51.098 | 51.098 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.008 | 0.040 | 0.000 | 48.627 | 48.627 | 48.627 |
| syscall:bind | 7/7 | 0 | 0 | 0.018 | n/a | n/a | 0.455 | 2.505 | 2.876 | 3.149 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.006 | 0.006 | 0.000 | 0.001 | 5.619 | 5.619 | 5.619 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.264 | 1.264 | 1.264 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.072 | 0.073 | 0.103 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.177 | 0.177 | 0.177 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.077 | 0.077 | 0.077 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2260 | 0.395 | 0.033 | 46.440 | 0.038 | 8.980385 CPU seconds | n/a |
| GPU 0 memory | MB | 2262 | 11974.099 | 11670.000 | 13268.000 | 11898.000 | n/a | n/a |
| GPU 0 power | W | 2262 | 49.228 | 27.854 | 79.816 | 28.155 | n/a | 112273.466 J |
| GPU 0 proc / 2181-24083 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 memory | MB | 2262 | 3294.789 | 3118.000 | 4584.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 2181-24083 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 estimated power | W | 868 | 12.292 | 0.000 | 79.018 | 0.000 | n/a | n/a |
| GPU 0 proc / 2181-24083 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 utilization | percent | 868 | 14.922 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2410-28048 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 memory | MB | 2262 | 8197.310 | 8070.000 | 8202.000 | 8202.000 | n/a | n/a |
| GPU 0 proc / 2410-28048 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 estimated power | W | 1367 | 46.865 | 0.000 | 73.812 | 0.000 | n/a | n/a |
| GPU 0 proc / 2410-28048 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 utilization | percent | 1367 | 64.873 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2262 | 11492.099 | 11188.000 | 12786.000 | 11416.000 | n/a | n/a |
| GPU 0 utilization | percent | 2262 | 46.403 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2262 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2261 | 4.059 | 0.087 | 80.142 | 0.232 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2261 | 17.169 | 0.000 | 65.337 | 0.251 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2261 | 0.907 | 0.000 | 197.949 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2261 | 1.963 | 0.000 | 238.192 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2261 | 0.614 | 0.000 | 39.720 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2261 | 0.635 | 0.000 | 39.800 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 2262 | 15363.539 | 15363.539 | 15363.539 | 15363.539 | n/a | n/a |
| host mem_used_mb | MB | 2262 | 7467.288 | 6709.027 | 9059.340 | 7746.914 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2261 | 0.003 | 0.000 | 3.031 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2261 | 0.003 | 0.000 | 3.092 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2261 | 0.015 | 0.000 | 25.140 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2261 | 0.009 | 0.000 | 1.051 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2172) CPU | percent | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2172) io read MB/s | MB/s | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2172) io write MB/s | MB/s | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2172) rss_mb | MB | 2262 | 3.312 | 3.312 | 3.312 | 3.312 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2172) main thread run-queue wait | percent | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2172) vms_mb | MB | 2262 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2181) CPU | percent | 2261 | 11.044 | 0.000 | 181.813 | 0.000 | 252.000000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2181) io read MB/s | MB/s | 2261 | 0.075 | 0.000 | 94.174 | 0.000 | 171.261719 MB | n/a |
| Agency harness — python -m lsbench (PID 2181) io write MB/s | MB/s | 2261 | 1.766 | 0.000 | 251.443 | 0.027 | 4028.558594 MB | n/a |
| Agency harness — python -m lsbench (PID 2181) rss_mb | MB | 2262 | 3311.365 | 2541.250 | 4495.473 | 3737.820 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2181) main thread run-queue wait | percent | 2261 | 0.000 | 0.000 | 0.020 | 0.000 | 0.000332 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2181) vms_mb | MB | 2262 | 16643.186 | 14158.961 | 19378.805 | 16886.820 | n/a | n/a |
| Python — vllm (PID 2241) CPU | percent | 2261 | 1.384 | 0.000 | 5.958 | 0.000 | 31.590000 CPU seconds | n/a |
| Python — vllm (PID 2241) io read MB/s | MB/s | 2261 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 2241) io write MB/s | MB/s | 2261 | 0.000 | 0.000 | 0.008 | 0.000 | 0.191406 MB | n/a |
| Python — vllm (PID 2241) rss_mb | MB | 2262 | 1789.779 | 1786.730 | 1790.355 | 1789.145 | n/a | n/a |
| Python — vllm (PID 2241) main thread run-queue wait | percent | 2261 | 0.037 | 0.000 | 3.174 | 0.000 | 0.850596 run-queue seconds | n/a |
| Python — vllm (PID 2241) vms_mb | MB | 2262 | 11060.092 | 10986.562 | 11061.582 | 11061.582 | n/a | n/a |
| Python — python -c (PID 2409) CPU | percent | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2409) io read MB/s | MB/s | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2409) io write MB/s | MB/s | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2409) rss_mb | MB | 2262 | 12.191 | 12.191 | 12.191 | 12.191 | n/a | n/a |
| Python — python -c (PID 2409) main thread run-queue wait | percent | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2409) vms_mb | MB | 2262 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2410) CPU | percent | 2261 | 15.136 | 0.000 | 43.680 | 0.996 | 345.500000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2410) io read MB/s | MB/s | 2261 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 2410) io write MB/s | MB/s | 2261 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 2410) rss_mb | MB | 2262 | 2327.926 | 2324.020 | 2328.668 | 2327.449 | n/a | n/a |
| VLLM::EngineCore (PID 2410) main thread run-queue wait | percent | 2261 | 0.163 | 0.000 | 14.554 | 0.000 | 3.735242 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2410) vms_mb | MB | 2262 | 21238.868 | 21235.242 | 21239.301 | 21239.301 | n/a | n/a |
| docker info (PID 2645) rss_mb | MB | 1 | 29.148 | 29.148 | 29.148 | 29.148 | n/a | n/a |
| docker info (PID 2645) vms_mb | MB | 1 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker-buildx (PID 2655) rss_mb | MB | 1 | 38.027 | 38.027 | 38.027 | 38.027 | n/a | n/a |
| docker-buildx (PID 2655) vms_mb | MB | 1 | 1298.227 | 1298.227 | 1298.227 | 1298.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 2753) CPU | percent | 2257 | 0.002 | 0.000 | 0.995 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 2753) rss_mb | MB | 2258 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 2753) main thread run-queue wait | percent | 2257 | 0.003 | 0.000 | 2.344 | 0.000 | 0.068755 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 2753) vms_mb | MB | 2258 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 2787) CPU | percent | 2257 | 0.002 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 2787) rss_mb | MB | 2258 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 2787) main thread run-queue wait | percent | 2257 | 0.005 | 0.000 | 3.184 | 0.000 | 0.113177 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 2787) vms_mb | MB | 2258 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2878) CPU | percent | 2257 | 27.463 | 0.000 | 95.332 | 0.000 | 624.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2878) rss_mb | MB | 2258 | 117.999 | 2.926 | 137.395 | 137.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2878) main thread run-queue wait | percent | 2257 | 0.000 | 0.000 | 0.011 | 0.000 | 0.000155 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2878) vms_mb | MB | 2258 | 989.813 | 4.262 | 1046.566 | 1045.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 2884) CPU | percent | 2 | 57.643 | 47.695 | 67.592 | 67.592 | 1.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 2884) rss_mb | MB | 3 | 42.884 | 8.652 | 72.961 | 72.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 2884) main thread run-queue wait | percent | 2 | 0.022 | 0.016 | 0.028 | 0.016 | 0.000452 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 2884) vms_mb | MB | 3 | 53.128 | 13.281 | 90.941 | 90.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2893) rss_mb | MB | 1 | 0.535 | 0.535 | 0.535 | 0.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2893) vms_mb | MB | 1 | 246.516 | 246.516 | 246.516 | 246.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2902) CPU | percent | 2229 | 3.336 | 0.000 | 23.841 | 4.973 | 75.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2902) rss_mb | MB | 2230 | 139.625 | 42.672 | 150.578 | 145.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2902) main thread run-queue wait | percent | 2229 | 0.000 | 0.000 | 0.192 | 0.000 | 0.007319 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2902) vms_mb | MB | 2230 | 392.224 | 348.844 | 495.590 | 399.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 2975) rss_mb | MB | 1 | 3.859 | 3.859 | 3.859 | 3.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 2975) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 2980) rss_mb | MB | 1 | 6.695 | 6.695 | 6.695 | 6.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 2980) vms_mb | MB | 1 | 224.297 | 224.297 | 224.297 | 224.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — lifecycle_hook.py (PID 2984) rss_mb | MB | 1 | 8.527 | 8.527 | 8.527 | 8.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — lifecycle_hook.py (PID 2984) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3063) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3063) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — rg (PID 3066) rss_mb | MB | 1 | 0.504 | 0.504 | 0.504 | 0.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — rg (PID 3066) vms_mb | MB | 1 | 5.617 | 5.617 | 5.617 | 5.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — sort (PID 3067) rss_mb | MB | 1 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — sort (PID 3067) vms_mb | MB | 1 | 15.051 | 15.051 | 15.051 | 15.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3166) rss_mb | MB | 1 | 10.113 | 10.113 | 10.113 | 10.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3166) vms_mb | MB | 1 | 14.977 | 14.977 | 14.977 | 14.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3305) rss_mb | MB | 1 | 20.117 | 20.117 | 20.117 | 20.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3305) vms_mb | MB | 1 | 25.070 | 25.070 | 25.070 | 25.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 3384) rss_mb | MB | 1 | 128.609 | 128.609 | 128.609 | 128.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 3384) vms_mb | MB | 1 | 390.156 | 390.156 | 390.156 | 390.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3954) rss_mb | MB | 1 | 21.500 | 21.500 | 21.500 | 21.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3954) vms_mb | MB | 1 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4571) rss_mb | MB | 1 | 10.539 | 10.539 | 10.539 | 10.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4571) vms_mb | MB | 1 | 15.188 | 15.188 | 15.188 | 15.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4572) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4572) rss_mb | MB | 2 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4572) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4572) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 4575) CPU | percent | 1 | 21.868 | 21.868 | 21.868 | 21.868 | 0.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 4575) rss_mb | MB | 2 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 4575) main thread run-queue wait | percent | 1 | 0.050 | 0.050 | 0.050 | 0.050 | 0.000502 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 4575) vms_mb | MB | 2 | 4.918 | 4.918 | 4.918 | 4.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 4576) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 4576) rss_mb | MB | 2 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 4576) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 4576) vms_mb | MB | 2 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4653) rss_mb | MB | 1 | 4.750 | 4.750 | 4.750 | 4.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4653) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4861) rss_mb | MB | 1 | 9.668 | 9.668 | 9.668 | 9.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4861) vms_mb | MB | 1 | 13.609 | 13.609 | 13.609 | 13.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4934) rss_mb | MB | 1 | 2.973 | 2.973 | 2.973 | 2.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4934) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 4936) rss_mb | MB | 1 | 13.742 | 13.742 | 13.742 | 13.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 4936) vms_mb | MB | 1 | 207.363 | 207.363 | 207.363 | 207.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4944) rss_mb | MB | 1 | 17.160 | 17.160 | 17.160 | 17.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4944) vms_mb | MB | 1 | 22.355 | 22.355 | 22.355 | 22.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4949) rss_mb | MB | 1 | 11.703 | 11.703 | 11.703 | 11.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4949) vms_mb | MB | 1 | 19.828 | 19.828 | 19.828 | 19.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 5098) CPU | percent | 19 | 170.936 | 158.825 | 179.064 | 175.090 | 32.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 5098) rss_mb | MB | 20 | 199.374 | 21.676 | 325.332 | 325.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 5098) main thread run-queue wait | percent | 19 | 64.748 | 54.514 | 75.596 | 64.177 | 12.440150 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 5098) vms_mb | MB | 20 | 1865.757 | 213.699 | 1959.020 | 1947.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5108) rss_mb | MB | 1 | 14.262 | 14.262 | 14.262 | 14.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5108) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5109) CPU | percent | 3 | 3.294 | 0.991 | 5.958 | 5.958 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5109) rss_mb | MB | 4 | 14.622 | 8.969 | 20.375 | 20.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5109) main thread run-queue wait | percent | 3 | 53.616 | 47.309 | 61.586 | 47.309 | 1.629342 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5109) vms_mb | MB | 4 | 19.890 | 13.551 | 25.582 | 25.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5347) rss_mb | MB | 1 | 5.660 | 5.660 | 5.660 | 5.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5347) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5416) rss_mb | MB | 1 | 19.547 | 19.547 | 19.547 | 19.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5416) vms_mb | MB | 1 | 24.805 | 24.805 | 24.805 | 24.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5475) rss_mb | MB | 1 | 19.367 | 19.367 | 19.367 | 19.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5475) vms_mb | MB | 1 | 24.938 | 24.938 | 24.938 | 24.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5513) rss_mb | MB | 1 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5513) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5515) rss_mb | MB | 1 | 71.934 | 71.934 | 71.934 | 71.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5515) vms_mb | MB | 1 | 1929.219 | 1929.219 | 1929.219 | 1929.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5595) rss_mb | MB | 1 | 9.609 | 9.609 | 9.609 | 9.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5595) vms_mb | MB | 1 | 13.738 | 13.738 | 13.738 | 13.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5658) rss_mb | MB | 1 | 14.836 | 14.836 | 14.836 | 14.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5658) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5676) rss_mb | MB | 1 | 15.609 | 15.609 | 15.609 | 15.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5676) vms_mb | MB | 1 | 20.504 | 20.504 | 20.504 | 20.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — frozen_traces.py (PID 5681) rss_mb | MB | 1 | 158.137 | 158.137 | 158.137 | 158.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — frozen_traces.py (PID 5681) vms_mb | MB | 1 | 2018.352 | 2018.352 | 2018.352 | 2018.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5710) rss_mb | MB | 1 | 3.008 | 3.008 | 3.008 | 3.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5710) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5711) rss_mb | MB | 1 | 7.477 | 7.477 | 7.477 | 7.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5711) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — frozen_traces.py (PID 5740) rss_mb | MB | 1 | 14.766 | 14.766 | 14.766 | 14.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — frozen_traces.py (PID 5740) vms_mb | MB | 1 | 210.047 | 210.047 | 210.047 | 210.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5754) rss_mb | MB | 1 | 10.828 | 10.828 | 10.828 | 10.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5754) vms_mb | MB | 1 | 15.215 | 15.215 | 15.215 | 15.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5768) rss_mb | MB | 1 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5768) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5769) rss_mb | MB | 1 | 14.711 | 14.711 | 14.711 | 14.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5769) vms_mb | MB | 1 | 128.445 | 128.445 | 128.445 | 128.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5771) rss_mb | MB | 1 | 16.160 | 16.160 | 16.160 | 16.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5771) vms_mb | MB | 1 | 20.852 | 20.852 | 20.852 | 20.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5777) rss_mb | MB | 1 | 8.395 | 8.395 | 8.395 | 8.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5777) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — frozen_traces.py (PID 5797) CPU | percent | 64 | 168.418 | 118.328 | 176.712 | 173.102 | 108.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — frozen_traces.py (PID 5797) rss_mb | MB | 65 | 539.617 | 15.168 | 613.188 | 613.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — frozen_traces.py (PID 5797) main thread run-queue wait | percent | 64 | 54.647 | 19.181 | 74.759 | 51.778 | 35.287484 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — frozen_traces.py (PID 5797) vms_mb | MB | 65 | 2081.135 | 210.059 | 2144.551 | 2144.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5806) CPU | percent | 4 | 3.468 | 0.991 | 6.937 | 6.937 | 0.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5806) rss_mb | MB | 5 | 13.814 | 6.957 | 21.496 | 21.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5806) main thread run-queue wait | percent | 4 | 61.901 | 57.399 | 67.190 | 67.190 | 2.498684 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5806) vms_mb | MB | 5 | 18.894 | 11.660 | 27.055 | 27.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5807) CPU | percent | 2 | 2.486 | 1.988 | 2.983 | 2.983 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5807) rss_mb | MB | 3 | 13.652 | 9.707 | 16.711 | 16.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5807) main thread run-queue wait | percent | 2 | 56.803 | 52.139 | 61.467 | 52.139 | 1.142656 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5807) vms_mb | MB | 3 | 18.664 | 13.738 | 22.145 | 22.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5808) rss_mb | MB | 1 | 20.859 | 20.859 | 20.859 | 20.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5808) vms_mb | MB | 1 | 25.836 | 25.836 | 25.836 | 25.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5823) CPU | percent | 3 | 2.647 | 1.980 | 3.976 | 3.976 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5823) rss_mb | MB | 4 | 13.327 | 8.844 | 18.590 | 18.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5823) main thread run-queue wait | percent | 3 | 58.351 | 51.343 | 62.199 | 61.509 | 1.764728 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5823) vms_mb | MB | 4 | 18.514 | 13.551 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5830) rss_mb | MB | 1 | 14.602 | 14.602 | 14.602 | 14.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5830) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5832) rss_mb | MB | 1 | 3.055 | 3.055 | 3.055 | 3.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5832) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5833) rss_mb | MB | 1 | 5.539 | 5.539 | 5.539 | 5.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5833) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5834) CPU | percent | 4 | 3.480 | 1.984 | 5.968 | 5.968 | 0.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5834) rss_mb | MB | 5 | 13.906 | 7.305 | 21.273 | 21.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5834) main thread run-queue wait | percent | 4 | 61.504 | 46.074 | 71.895 | 71.895 | 2.475491 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5834) vms_mb | MB | 5 | 18.972 | 11.789 | 27.078 | 27.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5846) rss_mb | MB | 1 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5846) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5847) rss_mb | MB | 1 | 148.016 | 148.016 | 148.016 | 148.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5847) vms_mb | MB | 1 | 1928.484 | 1928.484 | 1928.484 | 1928.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5852) rss_mb | MB | 1 | 10.691 | 10.691 | 10.691 | 10.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5852) vms_mb | MB | 1 | 15.281 | 15.281 | 15.281 | 15.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5865) rss_mb | MB | 1 | 14.660 | 14.660 | 14.660 | 14.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5865) vms_mb | MB | 1 | 20.000 | 20.000 | 20.000 | 20.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5867) rss_mb | MB | 1 | 14.539 | 14.539 | 14.539 | 14.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5867) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5868) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5868) rss_mb | MB | 2 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5868) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5868) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — signal_probe.py (PID 5869) CPU | percent | 9 | 133.786 | 55.571 | 174.754 | 171.140 | 12.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — signal_probe.py (PID 5869) rss_mb | MB | 10 | 404.007 | 42.223 | 750.000 | 750.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — signal_probe.py (PID 5869) main thread run-queue wait | percent | 9 | 31.867 | 6.172 | 56.399 | 35.927 | 2.898615 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — signal_probe.py (PID 5869) vms_mb | MB | 10 | 2305.958 | 423.953 | 2819.191 | 2819.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5870) CPU | percent | 1 | 55.571 | 55.571 | 55.571 | 55.571 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5870) rss_mb | MB | 2 | 311.742 | 145.734 | 477.750 | 477.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5870) main thread run-queue wait | percent | 1 | 27.187 | 27.187 | 27.187 | 27.187 | 0.273968 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5870) vms_mb | MB | 2 | 2009.404 | 1885.328 | 2133.480 | 2133.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5942) rss_mb | MB | 1 | 3.172 | 3.172 | 3.172 | 3.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5942) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5943) rss_mb | MB | 1 | 151.211 | 151.211 | 151.211 | 151.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5943) vms_mb | MB | 1 | 2010.840 | 2010.840 | 2010.840 | 2010.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5997) rss_mb | MB | 1 | 7.270 | 7.270 | 7.270 | 7.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5997) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6003) rss_mb | MB | 1 | 20.312 | 20.312 | 20.312 | 20.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6003) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6045) rss_mb | MB | 1 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6045) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6050) rss_mb | MB | 1 | 18.250 | 18.250 | 18.250 | 18.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6050) vms_mb | MB | 1 | 209.898 | 209.898 | 209.898 | 209.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6086) rss_mb | MB | 1 | 10.328 | 10.328 | 10.328 | 10.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6086) vms_mb | MB | 1 | 13.977 | 13.977 | 13.977 | 13.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6218) rss_mb | MB | 1 | 2.707 | 2.707 | 2.707 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6218) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6224) rss_mb | MB | 1 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6224) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6228) rss_mb | MB | 1 | 48.305 | 48.305 | 48.305 | 48.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6228) vms_mb | MB | 1 | 1921.102 | 1921.102 | 1921.102 | 1921.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6252) rss_mb | MB | 1 | 3.008 | 3.008 | 3.008 | 3.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6252) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6254) rss_mb | MB | 1 | 7.664 | 7.664 | 7.664 | 7.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6254) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6279) rss_mb | MB | 1 | 21.504 | 21.504 | 21.504 | 21.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6279) vms_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6300) rss_mb | MB | 1 | 18.562 | 18.562 | 18.562 | 18.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6300) vms_mb | MB | 1 | 24.176 | 24.176 | 24.176 | 24.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6302) rss_mb | MB | 1 | 6.945 | 6.945 | 6.945 | 6.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6302) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6332) rss_mb | MB | 1 | 5.047 | 5.047 | 5.047 | 5.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6332) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 6333) rss_mb | MB | 1 | 142.457 | 142.457 | 142.457 | 142.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 6333) vms_mb | MB | 1 | 392.207 | 392.207 | 392.207 | 392.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6335) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6335) rss_mb | MB | 7 | 3.102 | 3.102 | 3.102 | 3.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6335) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6335) vms_mb | MB | 7 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6337) CPU | percent | 6 | 125.281 | 48.597 | 176.810 | 155.849 | 7.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6337) rss_mb | MB | 7 | 550.827 | 35.473 | 1191.156 | 1191.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6337) main thread run-queue wait | percent | 6 | 30.481 | 0.972 | 52.284 | 35.538 | 1.841995 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6337) vms_mb | MB | 7 | 2406.464 | 415.332 | 3469.562 | 3469.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6338) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6338) rss_mb | MB | 2 | 2.977 | 2.977 | 2.977 | 2.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6338) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6338) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6340) CPU | percent | 1 | 89.260 | 89.260 | 89.260 | 89.260 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6340) rss_mb | MB | 2 | 163.955 | 110.875 | 217.035 | 217.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6340) main thread run-queue wait | percent | 1 | 45.903 | 45.903 | 45.903 | 45.903 | 0.462838 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6340) vms_mb | MB | 2 | 1994.814 | 1931.062 | 2058.566 | 2058.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6366) rss_mb | MB | 1 | 21.820 | 21.820 | 21.820 | 21.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6366) vms_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6375) rss_mb | MB | 1 | 19.770 | 19.770 | 19.770 | 19.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6375) vms_mb | MB | 1 | 24.938 | 24.938 | 24.938 | 24.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6376) rss_mb | MB | 1 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6376) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6379) rss_mb | MB | 1 | 151.055 | 151.055 | 151.055 | 151.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6379) vms_mb | MB | 1 | 1929.812 | 1929.812 | 1929.812 | 1929.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6409) rss_mb | MB | 1 | 7.180 | 7.180 | 7.180 | 7.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6409) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6445) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6445) rss_mb | MB | 2 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6445) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6445) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6447) CPU | percent | 1 | 124.283 | 124.283 | 124.283 | 124.283 | 1.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6447) rss_mb | MB | 2 | 265.756 | 19.363 | 512.148 | 512.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6447) main thread run-queue wait | percent | 1 | 20.440 | 20.440 | 20.440 | 20.440 | 0.205583 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6447) vms_mb | MB | 2 | 1090.832 | 172.355 | 2009.309 | 2009.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6457) rss_mb | MB | 1 | 21.430 | 21.430 | 21.430 | 21.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6457) vms_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6468) rss_mb | MB | 1 | 3.008 | 3.008 | 3.008 | 3.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6468) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6470) rss_mb | MB | 1 | 116.664 | 116.664 | 116.664 | 116.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6470) vms_mb | MB | 1 | 1935.852 | 1935.852 | 1935.852 | 1935.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6505) CPU | percent | 12 | 6.773 | 0.000 | 81.275 | 81.275 | 0.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6505) rss_mb | MB | 13 | 10.398 | 2.965 | 99.590 | 99.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6505) main thread run-queue wait | percent | 12 | 1.641 | 0.000 | 19.696 | 19.696 | 0.198717 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6505) vms_mb | MB | 13 | 170.773 | 4.258 | 2168.949 | 2168.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 6507) CPU | percent | 11 | 154.539 | 91.311 | 176.217 | 176.217 | 17.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 6507) rss_mb | MB | 12 | 525.805 | 10.770 | 845.957 | 720.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 6507) main thread run-queue wait | percent | 11 | 42.572 | 1.065 | 71.839 | 71.839 | 4.715172 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 6507) vms_mb | MB | 12 | 2384.866 | 15.203 | 2941.996 | 2331.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6540) rss_mb | MB | 1 | 20.191 | 20.191 | 20.191 | 20.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6540) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| docker commit (PID 6586) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6586) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6586) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6586) rss_mb | MB | 22 | 30.441 | 30.441 | 30.441 | 30.441 | n/a | n/a |
| docker commit (PID 6586) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6586) vms_mb | MB | 22 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 2257 | 40.935 | 0.000 | 208.274 | 0.000 | 931.428569 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2257 | 2.632 | 0.000 | 50.612 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2257 | 3.683 | 0.000 | 79.599 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 2257 | 0.079 | 0.000 | 51.058 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 2257 | 0.081 | 0.000 | 51.058 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 2257 | 0.104 | 0.000 | 61.131 | 0.000 | 237.207031 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 2257 | 0.085 | 0.000 | 68.326 | 0.000 | 192.855469 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 2258 | 545.240 | 18.414 | 1723.008 | 383.965 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2257 | 0.002 | 0.000 | 2.201 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2257 | 0.002 | 0.000 | 2.201 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 2257 | 0.011 | 0.000 | 24.322 | 0.000 | 25.040910 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 2257 | 0.001 | 0.000 | 0.280 | 0.000 | 1.739074 MB | n/a |
| workload total CPU | percent | 2261 | 27.581 | 1.572 | 181.602 | 2.072 | 629.510871 CPU seconds | n/a |
| workload total memory | MB | 2262 | 10251.488 | 8458.863 | 11556.660 | 11134.156 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
