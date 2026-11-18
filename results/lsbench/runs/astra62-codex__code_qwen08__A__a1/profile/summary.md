# agprof summary

- Duration: **1710.180 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **43 calls**, 43 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1385.140 s total wait
- Tools: **114/115 completed**, 0 failed, 1 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **157697** at 1.978 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1688473.663 / 1688473.663 ms |
| LLM latency p50 / p95 | 37052.475 / 56934.640 ms |
| LLM TTFT p50 / p95 | 9057.391 / 10257.249 ms |
| LLM input / output tokens | 3710977 / 146673 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 43 total, 43 succeeded, 0 failed, 0 interrupted |
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
| Bash | 35/36 | 35 | 0 | 1 | n/a | n/a |
| mcp__agency__attention | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 25/25 | 25 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 5/5 | 5 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 21/21 | 21 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 13/13 | 13 | 0 | 0 | n/a | n/a |
| update_plan | 7/7 | 7 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 10.128% | 218.618% | 173.397 s | 13928.561 MB | 15921.102 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 7172 |  | 1699 | 4.335% | 217.240% | 74.180 s | 2846.196 MB | 4192.043 MB | 16213.531 MB | 17613.129 MB | 0.089844 MB | 2401.703125 MB |
| docker-init | 7495 | sandbox_agent_lsb-codex_0000_0000 | 1678 | 0.003% | 0.995% | 0.050 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 7643 | sandbox_agent_lsb-codex_0000_0000 | 2 | 99.599% | 99.599% | 1.010 s | 56.379 MB | 83.648 MB | 67.438 MB | 98.051 MB | n/a MB | n/a MB |
| python | 7231 |  | 1699 | 0.000% | 0.000% | 0.000 s | 12.340 MB | 12.340 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| lsb_grid_worker | 2203 |  | 1699 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| tail | 7534 | sandbox_agent_lsb-codex_0000_0000 | 1678 | 0.002% | 0.995% | 0.040 s | 1.562 MB | 1.562 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 7232 |  | 1699 | 5.262% | 56.451% | 90.130 s | 2327.343 MB | 2327.414 MB | 21828.864 MB | 21828.953 MB | 0.000000 MB | 0.007812 MB |
| bash | 7637 | sandbox_agent_lsb-codex_0000_0000 | 1678 | 26.255% | 101.474% | 443.080 s | 115.981 MB | 128.902 MB | 1002.041 MB | 1056.160 MB | n/a MB | n/a MB |
| vllm | 7181 |  | 1699 | 0.520% | 6.932% | 8.900 s | 1805.137 MB | 1805.461 MB | 12014.132 MB | 12015.684 MB | 0.000000 MB | 0.121094 MB |
| git-remote-http | 7735 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.309 MB | 19.309 MB | 100.590 MB | 100.590 MB | n/a MB | n/a MB |
| git | 7744 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.309 MB | 5.309 MB | 8.426 MB | 8.426 MB | n/a MB | n/a MB |
| git | 7734 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.945 MB | 3.945 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 7733 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.379 MB | 4.379 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| codex | 7660 | sandbox_agent_lsb-codex_0000_0000 | 1670 | 2.576% | 14.685% | 43.300 s | 147.143 MB | 159.355 MB | 399.611 MB | 571.078 MB | n/a MB | n/a MB |
| git | 7756 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 28.328 MB | 28.328 MB | 35.523 MB | 35.523 MB | n/a MB | n/a MB |
| head | 7815 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| ls | 7814 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| bash | 7812 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.930 MB | 2.930 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 7846 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.406 MB | 9.406 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| python3 | 7888 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.980 MB | 14.980 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python3 | 7939 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.258 MB | 18.258 MB | 23.176 MB | 23.176 MB | n/a MB | n/a MB |
| python3 | 8028 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.645 MB | 4.645 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| bash | 8047 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.469 MB | 2.469 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 8051 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.625 MB | 2.625 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 8064 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.355 MB | 15.355 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python3 | 8081 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.090 MB | 10.090 MB | 13.738 MB | 13.738 MB | n/a MB | n/a MB |
| python3 | 8100 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| bash | 8102 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.953 MB | 2.953 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 8104 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.777 MB | 14.777 MB | 18.402 MB | 18.402 MB | n/a MB | n/a MB |
| python3 | 8234 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.953 MB | 15.953 MB | 20.504 MB | 20.504 MB | n/a MB | n/a MB |
| bash | 8278 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 8279 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.309 MB | 12.309 MB | 15.891 MB | 15.891 MB | n/a MB | n/a MB |
| python | 8315 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.980 MB | 19.980 MB | 371.852 MB | 371.852 MB | n/a MB | n/a MB |
| bash | 8314 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.121 MB | 3.121 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 8396 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.719 MB | 15.719 MB | 18.703 MB | 18.703 MB | n/a MB | n/a MB |
| python | 8455 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 80.328 MB | 80.328 MB | 221.047 MB | 221.047 MB | n/a MB | n/a MB |
| bash | 8452 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.047 MB | 3.047 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python3 | 8461 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.973 MB | 20.973 MB | 25.582 MB | 25.582 MB | n/a MB | n/a MB |
| python3 | 8493 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.785 MB | 9.785 MB | 13.738 MB | 13.738 MB | n/a MB | n/a MB |
| bash | 8514 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.164 MB | 3.164 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 8517 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.617 MB | 15.617 MB | 18.711 MB | 18.711 MB | n/a MB | n/a MB |
| python | 8568 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.012 MB | 16.012 MB | 19.715 MB | 19.715 MB | n/a MB | n/a MB |
| bash | 8567 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.000 MB | 3.000 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 8582 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.000 MB | 22.000 MB | 27.074 MB | 27.074 MB | n/a MB | n/a MB |
| python3 | 8599 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.043 MB | 9.043 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| python3 | 8623 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.973 MB | 21.973 MB | 26.980 MB | 26.980 MB | n/a MB | n/a MB |
| bash | 8691 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| bash | 8704 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.215 MB | 3.215 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 8710 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.254 MB | 10.254 MB | 13.785 MB | 13.785 MB | n/a MB | n/a MB |
| python3 | 8815 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.941 MB | 10.941 MB | 15.215 MB | 15.215 MB | n/a MB | n/a MB |
| python | 8860 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.914 MB | 15.914 MB | 19.715 MB | 19.715 MB | n/a MB | n/a MB |
| bash | 8857 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.141 MB | 3.141 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 8872 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.773 MB | 20.773 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| python3 | 8875 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.934 MB | 15.934 MB | 20.539 MB | 20.539 MB | n/a MB | n/a MB |
| bash | 8901 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.234 MB | 3.234 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 8904 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.180 MB | 16.180 MB | 20.039 MB | 20.039 MB | n/a MB | n/a MB |
| python | 8911 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.379 MB | 14.379 MB | 17.449 MB | 17.449 MB | n/a MB | n/a MB |
| python3 | 8926 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.832 MB | 16.832 MB | 22.145 MB | 22.145 MB | n/a MB | n/a MB |
| python3 | 8927 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.402 MB | 17.402 MB | 22.145 MB | 22.145 MB | n/a MB | n/a MB |
| bash | 8953 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.004 MB | 3.004 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 8955 | sandbox_agent_lsb-codex_0000_0000 | 3 | 93.000% | 98.439% | 1.870 s | 14.310 MB | 14.602 MB | 17.829 MB | 18.344 MB | n/a MB | n/a MB |
| python3 | 8975 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.125 MB | 15.125 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python3 | 8973 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.012 MB | 15.012 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| bash | 9294 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.750 MB | 2.750 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 9299 | sandbox_agent_lsb-codex_0000_0000 | 4 | 139.259% | 144.558% | 4.210 s | 145.678 MB | 205.547 MB | 409.421 MB | 476.520 MB | n/a MB | n/a MB |
| python3 | 9343 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.754 MB | 9.754 MB | 13.738 MB | 13.738 MB | n/a MB | n/a MB |
| python3 | 9346 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.320 MB | 19.320 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python3 | 9363 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.250 MB | 15.250 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python3 | 9399 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.422 MB | 9.422 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| python | 9404 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 44.973 MB | 44.973 MB | 265.152 MB | 265.152 MB | n/a MB | n/a MB |
| bash | 9402 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.852 MB | 2.852 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| bash | 9446 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.188 MB | 3.188 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 9453 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.090 MB | 20.090 MB | 371.812 MB | 371.812 MB | n/a MB | n/a MB |
| python | 9473 | sandbox_agent_lsb-codex_0000_0000 | 5 | 150.591% | 171.084% | 6.140 s | 218.850 MB | 385.227 MB | 476.550 MB | 652.125 MB | n/a MB | n/a MB |
| bash | 9506 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.062 MB | 3.062 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 9509 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.277 MB | 16.277 MB | 20.039 MB | 20.039 MB | n/a MB | n/a MB |
| python | 9512 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.758 MB | 12.758 MB | 16.613 MB | 16.613 MB | n/a MB | n/a MB |
| python3 | 9529 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.168 MB | 9.168 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| python | 9538 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 100.668 MB | 100.668 MB | 348.547 MB | 348.547 MB | n/a MB | n/a MB |
| bash | 9536 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.277 MB | 3.277 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 9556 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.898 MB | 20.898 MB | 25.324 MB | 25.324 MB | n/a MB | n/a MB |
| python3 | 9562 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.523 MB | 15.523 MB | 20.504 MB | 20.504 MB | n/a MB | n/a MB |
| docker | 9611 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.383 MB | 30.383 MB | 1988.027 MB | 1988.027 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 11.504% | 100.000% | 12047.338 MB | 12838.000 MB | 33.931 W | 73.500 W | 57999.954 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 32.109% | 201.856% | 542.031 s | 283.463 MB | 666.180 MB | 0.535156 MB | 214.984375 MB | 25.390617 MB | 1.762104 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 7364 | 1710.116 | interrupted |
| tool:Bash | -1 | 598.861 | interrupted |
| harness:retire | -1 | 0.408 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1688.474 | n/a | n/a | 0.535 | 1688473.663 | 1688473.663 | 1688473.663 |
| engine:execute | 1/1 | 0 | 0 | 1688.472 | 2.136 | 1686.336 | 0.535 | 1688472.025 | 1688472.025 | 1688472.025 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1682.667 | 0.012 | 1682.655 | 0.535 | 1682666.595 | 1682666.595 | 1682666.595 |
| harness:await_cli | 1/1 | 0 | 0 | 1678.982 | n/a | n/a | 0.535 | 1678981.610 | 1678981.610 | 1678981.610 |
| llm:attempt | 43/43 | 0 | 0 | 1385.140 | 5.488 | 1379.650 | 0.161 | 32212.553 | 37052.475 | 56934.640 |
| tool:Bash | 35/36 | 0 | 1 | 255.209 | n/a | n/a | 0.131 | 7291.692 | 669.040 | 46868.988 |
| tool:mcp__agency__generate | 25/25 | 0 | 0 | 184.055 | n/a | n/a | 0.000 | 7362.199 | 5747.276 | 10262.747 |
| tool:mcp__agency__trace | 13/13 | 0 | 0 | 29.744 | n/a | n/a | 0.000 | 2288.004 | 2121.364 | 4210.315 |
| tool:mcp__agency__inspect_module_inputs | 5/5 | 0 | 0 | 9.131 | n/a | n/a | 0.000 | 1826.117 | 1876.353 | 1879.954 |
| tool:mcp__agency__patch | 21/21 | 0 | 0 | 8.071 | n/a | n/a | 0.000 | 384.319 | 383.160 | 396.826 |
| tool:mcp__agency__token_stats | 2/2 | 0 | 0 | 4.491 | n/a | n/a | 0.096 | 2245.607 | 2245.607 | 2409.185 |
| tool:mcp__agency__inspect | 2/2 | 0 | 0 | 3.457 | n/a | n/a | 0.000 | 1728.455 | 1728.455 | 1884.800 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.124 | 0.708 | 2.416 | 0.000 | 3124.318 | 3124.318 | 3124.318 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.124 | 0.708 | 2.416 | 0.000 | 3123.987 | 3123.987 | 3123.987 |
| run:container_call | 13/13 | 0 | 0 | 2.486 | 0.002 | 2.484 | 0.000 | 191.258 | 36.007 | 844.077 |
| syscall:connect | 955/955 | 0 | 0 | 2.223 | n/a | n/a | 0.017 | 2.328 | 1.958 | 4.015 |
| teardown:commit | 1/1 | 0 | 0 | 2.087 | 0.004 | 2.082 | 0.000 | 2086.605 | 2086.605 | 2086.605 |
| sandbox:commit | 1/1 | 0 | 0 | 1.890 | 0.002 | 1.888 | 0.000 | 1890.237 | 1890.237 | 1890.237 |
| checkpoint.total | 1/1 | 0 | 0 | 1.890 | 0.002 | 1.888 | 0.000 | 1890.103 | 1890.103 | 1890.103 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.890 | 0.002 | 1.888 | 0.000 | 1889.963 | 1889.963 | 1889.963 |
| syscall:sendto | 624/624 | 0 | 0 | 1.538 | n/a | n/a | 0.009 | 2.466 | 2.147 | 4.295 |
| syscall:execve | 1008/1008 | 0 | 0 | 1.432 | n/a | n/a | 0.011 | 1.421 | 1.222 | 2.533 |
| tool:update_plan | 7/7 | 0 | 0 | 1.103 | n/a | n/a | 0.007 | 157.548 | 157.356 | 159.828 |
| harness:submit | 1/1 | 0 | 0 | 1.009 | n/a | n/a | 0.000 | 1008.935 | 1008.935 | 1008.935 |
| harness:snapshot | 1/1 | 0 | 0 | 0.828 | n/a | n/a | 0.007 | 828.168 | 828.168 | 828.168 |
| harness:startup_ready | 1/1 | 0 | 0 | 0.818 | n/a | n/a | 0.000 | 818.128 | 818.128 | 818.128 |
| tool:mcp__agency__attention | 2/2 | 0 | 0 | 0.523 | n/a | n/a | 0.026 | 261.488 | 261.488 | 270.469 |
| sandbox:create | 1/1 | 0 | 0 | 0.336 | 0.251 | 0.085 | 0.000 | 335.836 | 335.836 | 335.836 |
| sandbox:start | 1/1 | 0 | 0 | 0.335 | 0.002 | 0.332 | 0.000 | 334.542 | 334.542 | 334.542 |
| runtime.container_create | 1/1 | 0 | 0 | 0.334 | 0.002 | 0.332 | 0.000 | 334.400 | 334.400 | 334.400 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.331 | n/a | n/a | 0.000 | 331.403 | 331.403 | 331.403 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.200 | n/a | n/a | 0.000 | 200.365 | 200.365 | 200.365 |
| sandbox:stop | 1/1 | 0 | 0 | 0.196 | 0.002 | 0.195 | 0.000 | 196.124 | 196.124 | 196.124 |
| agency:services_close | 1/1 | 0 | 0 | 0.106 | 0.000 | 0.106 | 0.000 | 106.249 | 106.249 | 106.249 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.032 | 0.000 | 72.570 | 72.570 | 72.570 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.010 | 0.040 | 0.000 | 49.405 | 49.405 | 49.405 |
| run:detect | 1/1 | 0 | 0 | 0.048 | 0.001 | 0.048 | 0.000 | 48.258 | 48.258 | 48.258 |
| harness:launch | 1/1 | 0 | 0 | 0.044 | n/a | n/a | 0.000 | 43.834 | 43.834 | 43.834 |
| syscall:bind | 5/5 | 0 | 0 | 0.011 | n/a | n/a | 0.000 | 2.266 | 1.774 | 3.673 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.010 | 0.010 | 0.000 | 0.000 | 9.953 | 9.953 | 9.953 |
| sync:container | 13/13 | 0 | 0 | 0.002 | 0.001 | 0.000 | 0.000 | 0.119 | 0.081 | 0.345 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.395 | 1.395 | 1.395 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.216 | 0.216 | 0.216 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.061 | 0.061 | 0.061 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1698 | 0.267 | 0.040 | 169.722 | 0.082 | 4.559049 CPU seconds | n/a |
| GPU 0 memory | MB | 1699 | 12047.338 | 11670.000 | 12838.000 | 12308.000 | n/a | n/a |
| GPU 0 power | W | 1699 | 33.931 | 28.156 | 73.500 | 28.233 | n/a | 57999.954 J |
| GPU 0 proc / 7172-489919 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb memory | MB | 1699 | 3241.701 | 3118.000 | 4010.000 | 3480.000 | n/a | n/a |
| GPU 0 proc / 7172-489919 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb estimated power | W | 951 | 2.788 | 0.000 | 71.452 | 0.000 | n/a | n/a |
| GPU 0 proc / 7172-489919 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb utilization | percent | 951 | 2.034 | 0.000 | 87.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 7232-491709 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb memory | MB | 1699 | 8323.637 | 8070.000 | 8346.000 | 8346.000 | n/a | n/a |
| GPU 0 proc / 7232-491709 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb estimated power | W | 731 | 16.697 | 0.000 | 73.500 | 0.000 | n/a | n/a |
| GPU 0 proc / 7232-491709 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb utilization | percent | 731 | 22.713 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1699 | 11565.338 | 11188.000 | 12356.000 | 11826.000 | n/a | n/a |
| GPU 0 utilization | percent | 1699 | 11.504 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1699 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1698 | 0.618 | 0.049 | 25.248 | 0.133 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1698 | 5.105 | 0.000 | 37.811 | 0.498 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1698 | 0.001 | 0.000 | 0.214 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1698 | 1.577 | 0.000 | 221.327 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1698 | 0.204 | 0.000 | 61.391 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1698 | 0.205 | 0.000 | 61.958 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1699 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1699 | 7124.657 | 6475.109 | 8452.117 | 7472.004 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1698 | 0.021 | 0.000 | 22.359 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1698 | 0.015 | 0.000 | 1.228 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2203) CPU | percent | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2203) io read MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2203) io write MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2203) rss_mb | MB | 1699 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2203) main thread run-queue wait | percent | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2203) vms_mb | MB | 1699 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 7172) CPU | percent | 1698 | 4.335 | 0.000 | 217.240 | 0.000 | 74.180000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 7172) io read MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.089 | 0.000 | 0.089844 MB | n/a |
| Agency harness — python -m lsbench (PID 7172) io write MB/s | MB/s | 1698 | 1.403 | 0.015 | 437.163 | 0.023 | 2401.703125 MB | n/a |
| Agency harness — python -m lsbench (PID 7172) rss_mb | MB | 1699 | 2846.196 | 2175.895 | 4192.043 | 3356.516 | n/a | n/a |
| Agency harness — python -m lsbench (PID 7172) main thread run-queue wait | percent | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 7172) vms_mb | MB | 1699 | 16213.531 | 14276.898 | 17613.129 | 16913.215 | n/a | n/a |
| Python — vllm (PID 7181) CPU | percent | 1698 | 0.520 | 0.000 | 6.932 | 0.000 | 8.900000 CPU seconds | n/a |
| Python — vllm (PID 7181) io read MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 7181) io write MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.008 | 0.000 | 0.121094 MB | n/a |
| Python — vllm (PID 7181) rss_mb | MB | 1699 | 1805.137 | 1803.086 | 1805.461 | 1805.461 | n/a | n/a |
| Python — vllm (PID 7181) main thread run-queue wait | percent | 1698 | 0.001 | 0.000 | 0.159 | 0.001 | 0.009176 run-queue seconds | n/a |
| Python — vllm (PID 7181) vms_mb | MB | 1699 | 12014.132 | 11942.664 | 12015.684 | 12015.684 | n/a | n/a |
| Python — python -c (PID 7231) CPU | percent | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 7231) io read MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 7231) io write MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 7231) rss_mb | MB | 1699 | 12.340 | 12.340 | 12.340 | 12.340 | n/a | n/a |
| Python — python -c (PID 7231) main thread run-queue wait | percent | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 7231) vms_mb | MB | 1699 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 7232) CPU | percent | 1698 | 5.262 | 0.000 | 56.451 | 0.000 | 90.130000 CPU seconds | n/a |
| VLLM::EngineCore (PID 7232) io read MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 7232) io write MB/s | MB/s | 1698 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 7232) rss_mb | MB | 1699 | 2327.343 | 2326.789 | 2327.414 | 2327.414 | n/a | n/a |
| VLLM::EngineCore (PID 7232) main thread run-queue wait | percent | 1698 | 0.001 | 0.000 | 0.016 | 0.000 | 0.010296 run-queue seconds | n/a |
| VLLM::EngineCore (PID 7232) vms_mb | MB | 1699 | 21828.864 | 21827.691 | 21828.953 | 21828.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 7495) CPU | percent | 1677 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 7495) rss_mb | MB | 1678 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 7495) main thread run-queue wait | percent | 1677 | 0.000 | 0.000 | 0.227 | 0.000 | 0.002637 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 7495) vms_mb | MB | 1678 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7534) CPU | percent | 1677 | 0.002 | 0.000 | 0.995 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7534) rss_mb | MB | 1678 | 1.562 | 1.562 | 1.562 | 1.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7534) main thread run-queue wait | percent | 1677 | 0.000 | 0.000 | 0.162 | 0.000 | 0.001769 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7534) vms_mb | MB | 1678 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7637) CPU | percent | 1677 | 26.255 | 0.000 | 101.474 | 0.000 | 443.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7637) rss_mb | MB | 1678 | 115.981 | 3.113 | 128.902 | 126.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7637) main thread run-queue wait | percent | 1677 | 0.000 | 0.000 | 0.009 | 0.000 | 0.000116 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7637) vms_mb | MB | 1678 | 1002.041 | 4.262 | 1056.160 | 1045.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7643) CPU | percent | 1 | 99.599 | 99.599 | 99.599 | 99.599 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7643) rss_mb | MB | 2 | 56.379 | 29.109 | 83.648 | 83.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7643) main thread run-queue wait | percent | 1 | 0.004 | 0.004 | 0.004 | 0.004 | 0.000046 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7643) vms_mb | MB | 2 | 67.438 | 36.824 | 98.051 | 98.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7660) CPU | percent | 1669 | 2.576 | 0.000 | 14.685 | 3.980 | 43.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7660) rss_mb | MB | 1670 | 147.143 | 101.816 | 159.355 | 156.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7660) main thread run-queue wait | percent | 1669 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7660) vms_mb | MB | 1670 | 399.611 | 362.625 | 571.078 | 406.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7733) rss_mb | MB | 1 | 4.379 | 4.379 | 4.379 | 4.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7733) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 7734) rss_mb | MB | 1 | 3.945 | 3.945 | 3.945 | 3.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 7734) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 7735) rss_mb | MB | 1 | 19.309 | 19.309 | 19.309 | 19.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 7735) vms_mb | MB | 1 | 100.590 | 100.590 | 100.590 | 100.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 7744) rss_mb | MB | 1 | 5.309 | 5.309 | 5.309 | 5.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 7744) vms_mb | MB | 1 | 8.426 | 8.426 | 8.426 | 8.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7756) rss_mb | MB | 1 | 28.328 | 28.328 | 28.328 | 28.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7756) vms_mb | MB | 1 | 35.523 | 35.523 | 35.523 | 35.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7812) rss_mb | MB | 1 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7812) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — ls (PID 7814) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — ls (PID 7814) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 7815) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 7815) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7846) rss_mb | MB | 1 | 9.406 | 9.406 | 9.406 | 9.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7846) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7888) rss_mb | MB | 1 | 14.980 | 14.980 | 14.980 | 14.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7888) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7939) rss_mb | MB | 1 | 18.258 | 18.258 | 18.258 | 18.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7939) vms_mb | MB | 1 | 23.176 | 23.176 | 23.176 | 23.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8028) rss_mb | MB | 1 | 4.645 | 4.645 | 4.645 | 4.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8028) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8047) rss_mb | MB | 1 | 2.469 | 2.469 | 2.469 | 2.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8047) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8051) rss_mb | MB | 1 | 2.625 | 2.625 | 2.625 | 2.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8051) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8064) rss_mb | MB | 1 | 15.355 | 15.355 | 15.355 | 15.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8064) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8081) rss_mb | MB | 1 | 10.090 | 10.090 | 10.090 | 10.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8081) vms_mb | MB | 1 | 13.738 | 13.738 | 13.738 | 13.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8100) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8100) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8102) rss_mb | MB | 1 | 2.953 | 2.953 | 2.953 | 2.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8102) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8104) rss_mb | MB | 1 | 14.777 | 14.777 | 14.777 | 14.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8104) vms_mb | MB | 1 | 18.402 | 18.402 | 18.402 | 18.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8234) rss_mb | MB | 1 | 15.953 | 15.953 | 15.953 | 15.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8234) vms_mb | MB | 1 | 20.504 | 20.504 | 20.504 | 20.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8278) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8278) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8279) rss_mb | MB | 1 | 12.309 | 12.309 | 12.309 | 12.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8279) vms_mb | MB | 1 | 15.891 | 15.891 | 15.891 | 15.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8314) rss_mb | MB | 1 | 3.121 | 3.121 | 3.121 | 3.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8314) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8315) rss_mb | MB | 1 | 19.980 | 19.980 | 19.980 | 19.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8315) vms_mb | MB | 1 | 371.852 | 371.852 | 371.852 | 371.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8396) rss_mb | MB | 1 | 15.719 | 15.719 | 15.719 | 15.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8396) vms_mb | MB | 1 | 18.703 | 18.703 | 18.703 | 18.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8452) rss_mb | MB | 1 | 3.047 | 3.047 | 3.047 | 3.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8452) vms_mb | MB | 1 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — signals.py (PID 8455) rss_mb | MB | 1 | 80.328 | 80.328 | 80.328 | 80.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — signals.py (PID 8455) vms_mb | MB | 1 | 221.047 | 221.047 | 221.047 | 221.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8461) rss_mb | MB | 1 | 20.973 | 20.973 | 20.973 | 20.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8461) vms_mb | MB | 1 | 25.582 | 25.582 | 25.582 | 25.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8493) rss_mb | MB | 1 | 9.785 | 9.785 | 9.785 | 9.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8493) vms_mb | MB | 1 | 13.738 | 13.738 | 13.738 | 13.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8514) rss_mb | MB | 1 | 3.164 | 3.164 | 3.164 | 3.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8514) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8517) rss_mb | MB | 1 | 15.617 | 15.617 | 15.617 | 15.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8517) vms_mb | MB | 1 | 18.711 | 18.711 | 18.711 | 18.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8567) rss_mb | MB | 1 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8567) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8568) rss_mb | MB | 1 | 16.012 | 16.012 | 16.012 | 16.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8568) vms_mb | MB | 1 | 19.715 | 19.715 | 19.715 | 19.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8582) rss_mb | MB | 1 | 22.000 | 22.000 | 22.000 | 22.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8582) vms_mb | MB | 1 | 27.074 | 27.074 | 27.074 | 27.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8599) rss_mb | MB | 1 | 9.043 | 9.043 | 9.043 | 9.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8599) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8623) rss_mb | MB | 1 | 21.973 | 21.973 | 21.973 | 21.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8623) vms_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8691) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8691) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8704) rss_mb | MB | 1 | 3.215 | 3.215 | 3.215 | 3.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8704) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8710) rss_mb | MB | 1 | 10.254 | 10.254 | 10.254 | 10.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8710) vms_mb | MB | 1 | 13.785 | 13.785 | 13.785 | 13.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8815) rss_mb | MB | 1 | 10.941 | 10.941 | 10.941 | 10.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8815) vms_mb | MB | 1 | 15.215 | 15.215 | 15.215 | 15.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8857) rss_mb | MB | 1 | 3.141 | 3.141 | 3.141 | 3.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8857) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8860) rss_mb | MB | 1 | 15.914 | 15.914 | 15.914 | 15.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8860) vms_mb | MB | 1 | 19.715 | 19.715 | 19.715 | 19.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8872) rss_mb | MB | 1 | 20.773 | 20.773 | 20.773 | 20.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8872) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8875) rss_mb | MB | 1 | 15.934 | 15.934 | 15.934 | 15.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8875) vms_mb | MB | 1 | 20.539 | 20.539 | 20.539 | 20.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8901) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8901) rss_mb | MB | 2 | 3.234 | 3.234 | 3.234 | 3.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8901) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8901) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8904) rss_mb | MB | 1 | 16.180 | 16.180 | 16.180 | 16.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 8904) vms_mb | MB | 1 | 20.039 | 20.039 | 20.039 | 20.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8911) rss_mb | MB | 1 | 14.379 | 14.379 | 14.379 | 14.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8911) vms_mb | MB | 1 | 17.449 | 17.449 | 17.449 | 17.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8926) rss_mb | MB | 1 | 16.832 | 16.832 | 16.832 | 16.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8926) vms_mb | MB | 1 | 22.145 | 22.145 | 22.145 | 22.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8927) rss_mb | MB | 1 | 17.402 | 17.402 | 17.402 | 17.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8927) vms_mb | MB | 1 | 22.145 | 22.145 | 22.145 | 22.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8953) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8953) rss_mb | MB | 3 | 3.004 | 3.004 | 3.004 | 3.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8953) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8953) vms_mb | MB | 3 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8955) CPU | percent | 2 | 93.000 | 87.560 | 98.439 | 87.560 | 1.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8955) rss_mb | MB | 3 | 14.310 | 13.852 | 14.602 | 14.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8955) main thread run-queue wait | percent | 2 | 6.459 | 0.003 | 12.915 | 12.915 | 0.129836 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8955) vms_mb | MB | 3 | 17.829 | 16.930 | 18.344 | 18.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8973) rss_mb | MB | 1 | 15.012 | 15.012 | 15.012 | 15.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8973) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8975) rss_mb | MB | 1 | 15.125 | 15.125 | 15.125 | 15.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8975) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9294) rss_mb | MB | 1 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9294) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 9299) CPU | percent | 3 | 139.259 | 135.991 | 144.558 | 144.558 | 4.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 9299) rss_mb | MB | 4 | 145.678 | 63.777 | 205.547 | 134.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 9299) main thread run-queue wait | percent | 3 | 29.499 | 21.460 | 35.938 | 21.460 | 0.891427 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 9299) vms_mb | MB | 4 | 409.421 | 310.695 | 476.520 | 402.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9343) rss_mb | MB | 1 | 9.754 | 9.754 | 9.754 | 9.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9343) vms_mb | MB | 1 | 13.738 | 13.738 | 13.738 | 13.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9346) rss_mb | MB | 1 | 19.320 | 19.320 | 19.320 | 19.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9346) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9363) rss_mb | MB | 1 | 15.250 | 15.250 | 15.250 | 15.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9363) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9399) rss_mb | MB | 1 | 9.422 | 9.422 | 9.422 | 9.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9399) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9402) rss_mb | MB | 1 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9402) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 9404) rss_mb | MB | 1 | 44.973 | 44.973 | 44.973 | 44.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 9404) vms_mb | MB | 1 | 265.152 | 265.152 | 265.152 | 265.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9446) rss_mb | MB | 1 | 3.188 | 3.188 | 3.188 | 3.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9446) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 9453) rss_mb | MB | 1 | 20.090 | 20.090 | 20.090 | 20.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 9453) vms_mb | MB | 1 | 371.812 | 371.812 | 371.812 | 371.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 9473) CPU | percent | 4 | 150.591 | 131.354 | 171.084 | 171.084 | 6.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 9473) rss_mb | MB | 5 | 218.850 | 46.977 | 385.227 | 149.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 9473) main thread run-queue wait | percent | 4 | 17.312 | 9.219 | 20.564 | 20.311 | 0.706535 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 9473) vms_mb | MB | 5 | 476.550 | 266.934 | 652.125 | 413.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9506) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9506) rss_mb | MB | 2 | 3.062 | 3.062 | 3.062 | 3.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9506) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9506) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 9509) rss_mb | MB | 1 | 16.277 | 16.277 | 16.277 | 16.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 9509) vms_mb | MB | 1 | 20.039 | 20.039 | 20.039 | 20.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 9512) rss_mb | MB | 1 | 12.758 | 12.758 | 12.758 | 12.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bench.py (PID 9512) vms_mb | MB | 1 | 16.613 | 16.613 | 16.613 | 16.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9529) rss_mb | MB | 1 | 9.168 | 9.168 | 9.168 | 9.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9529) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9536) rss_mb | MB | 1 | 3.277 | 3.277 | 3.277 | 3.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9536) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 9538) rss_mb | MB | 1 | 100.668 | 100.668 | 100.668 | 100.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 9538) vms_mb | MB | 1 | 348.547 | 348.547 | 348.547 | 348.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9556) rss_mb | MB | 1 | 20.898 | 20.898 | 20.898 | 20.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9556) vms_mb | MB | 1 | 25.324 | 25.324 | 25.324 | 25.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9562) rss_mb | MB | 1 | 15.523 | 15.523 | 15.523 | 15.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9562) vms_mb | MB | 1 | 20.504 | 20.504 | 20.504 | 20.504 | n/a | n/a |
| docker commit (PID 9611) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 9611) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 9611) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 9611) rss_mb | MB | 2 | 30.383 | 30.383 | 30.383 | 30.383 | n/a | n/a |
| docker commit (PID 9611) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 9611) vms_mb | MB | 2 | 1988.027 | 1988.027 | 1988.027 | 1988.027 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 1677 | 32.109 | 0.000 | 201.856 | 0.000 | 542.031086 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1677 | 0.572 | 0.000 | 26.540 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1677 | 0.576 | 0.000 | 26.541 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 1677 | 0.002 | 0.000 | 0.661 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 1677 | 0.002 | 0.000 | 0.661 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 1677 | 0.000 | 0.000 | 0.201 | 0.000 | 0.535156 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 1677 | 0.127 | 0.000 | 67.523 | 0.000 | 214.984375 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 1678 | 283.463 | 19.848 | 666.180 | 114.914 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1677 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1677 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 1677 | 0.015 | 0.000 | 21.812 | 0.000 | 25.390617 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 1677 | 0.001 | 0.000 | 0.287 | 0.000 | 1.762104 MB | n/a |
| workload total CPU | percent | 1698 | 10.128 | 1.431 | 218.618 | 2.146 | 173.396822 CPU seconds | n/a |
| workload total memory | MB | 1699 | 13928.561 | 12835.938 | 15921.102 | 15092.660 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
