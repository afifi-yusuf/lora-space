# agprof summary

- Duration: **3708.004 s**
- Runs: **0/1 completed**, 0 succeeded, 0 failed, 1 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **87 calls**, 87 succeeded, 0 failed, 0 interrupted, n/a reported retries, 2563.842 s total wait
- Tools: **96/96 completed**, 1 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **340647** at 1.94 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | n/a / n/a ms |
| LLM latency p50 / p95 | 17152.413 / 93617.614 ms |
| LLM TTFT p50 / p95 | 5712.712 / 85716.349 ms |
| LLM input / output tokens | 194 / 261479 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 87 total, 87 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- claude_code: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 58/58 | 57 | 1 | 0 | n/a | n/a |
| Read | 1/1 | 1 | 0 | 0 | n/a | n/a |
| ToolSearch | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 5/5 | 5 | 0 | 0 | n/a | n/a |
| mcp__agency__get_current_resources | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 4/4 | 4 | 0 | 0 | n/a | n/a |
| mcp__agency__reserve_resource | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__submitted_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 18/18 | 18 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 3.427% | 832.017% | 148.365 s | 5654.347 MB | 6238.688 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 8010 |  | 3621 | 1.972% | 166.482% | 76.630 s | 2663.679 MB | 3035.695 MB | 16271.204 MB | 16540.699 MB | 965.820312 MB | 1434.687500 MB |
| tail | 8387 | sandbox_agent_lsb-claude_code_0000_0000 | 3621 | 0.007% | 15.731% | 0.690 s | 1.070 MB | 1.473 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 8069 |  | 3621 | 0.000% | 0.000% | 0.000 s | 10.302 MB | 12.207 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python3 | 8498 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 99.612% | 99.612% | 1.010 s | 56.129 MB | 84.195 MB | 66.793 MB | 98.051 MB | n/a MB | n/a MB |
| bash | 8492 | sandbox_agent_lsb-claude_code_0000_0000 | 3621 | 25.355% | 120.601% | 927.120 s | 101.106 MB | 107.844 MB | 973.004 MB | 974.969 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 8070 |  | 3621 | 1.342% | 572.068% | 64.940 s | 2108.891 MB | 2326.254 MB | 21828.801 MB | 21828.816 MB | 1906.238281 MB | 0.023438 MB |
| lsb_grid_worker | 7027 |  | 3621 | 0.000% | 0.000% | 0.000 s | 2.820 MB | 3.383 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 8348 | sandbox_agent_lsb-claude_code_0000_0000 | 3621 | 0.003% | 5.506% | 0.280 s | 0.439 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| vllm | 8019 |  | 3621 | 0.114% | 92.548% | 6.770 s | 1619.802 MB | 1795.402 MB | 12003.700 MB | 12004.305 MB | 520.656250 MB | 0.031250 MB |
| claude | 8511 | sandbox_agent_lsb-claude_code_0000_0000 | 3311 | 2.735% | 69.528% | 91.140 s | 292.386 MB | 343.766 MB | 5499.870 MB | 5499.910 MB | n/a MB | n/a MB |
| sh | 8586 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.363 MB | 1.363 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8562 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.238 MB | 18.238 MB | 24.098 MB | 24.098 MB | n/a MB | n/a MB |
| python3 | 8587 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.242 MB | 14.242 MB | 19.836 MB | 19.836 MB | n/a MB | n/a MB |
| sh | 8560 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8607 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.668 MB | 18.668 MB | 24.148 MB | 24.148 MB | n/a MB | n/a MB |
| sh | 8606 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 8748 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8749 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.629 MB | 18.629 MB | 24.098 MB | 24.098 MB | n/a MB | n/a MB |
| python3 | 8798 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.215 MB | 18.215 MB | 23.098 MB | 23.098 MB | n/a MB | n/a MB |
| sh | 8797 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 9028 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.816 MB | 2.816 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9031 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.461 MB | 14.461 MB | 367.199 MB | 367.199 MB | n/a MB | n/a MB |
| head | 9078 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.246 MB | 1.246 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 9075 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.754 MB | 2.754 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| pip | 9077 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.316 MB | 11.316 MB | 14.895 MB | 14.895 MB | n/a MB | n/a MB |
| python3 | 9137 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.051 MB | 22.051 MB | 373.633 MB | 373.633 MB | n/a MB | n/a MB |
| bash | 9135 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.035 MB | 3.035 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9156 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 126.906 MB | 126.906 MB | 476.934 MB | 476.934 MB | n/a MB | n/a MB |
| bash | 9154 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.883 MB | 2.883 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 9173 | sandbox_agent_lsb-claude_code_0000_0000 | 139 | 0.000% | 0.000% | 0.000 s | 3.090 MB | 3.090 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9175 | sandbox_agent_lsb-claude_code_0000_0000 | 139 | 179.972% | 192.973% | 249.940 s | 156.762 MB | 226.293 MB | 535.977 MB | 607.395 MB | n/a MB | n/a MB |
| sh | 9283 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9284 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 4.972% | 8.951% | 0.100 s | 13.516 MB | 21.703 MB | 18.033 MB | 26.988 MB | n/a MB | n/a MB |
| python3 | 9405 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.840 MB | 20.840 MB | 25.504 MB | 25.504 MB | n/a MB | n/a MB |
| sh | 9404 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| claude | 9414 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 285.398 MB | 285.398 MB | 5499.879 MB | 5499.879 MB | n/a MB | n/a MB |
| sh | 9428 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9429 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.500 MB | 15.500 MB | 20.176 MB | 20.176 MB | n/a MB | n/a MB |
| python3 | 9488 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 182.857% | 182.857% | 1.840 s | 162.311 MB | 189.188 MB | 547.191 MB | 568.848 MB | n/a MB | n/a MB |
| bash | 9486 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.922 MB | 2.922 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| sh | 9501 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9502 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.621 MB | 10.621 MB | 15.203 MB | 15.203 MB | n/a MB | n/a MB |
| python3 | 9504 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 142.188 MB | 142.188 MB | 521.293 MB | 521.293 MB | n/a MB | n/a MB |
| bash | 9503 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.922 MB | 2.922 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9578 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.672 MB | 18.672 MB | 24.098 MB | 24.098 MB | n/a MB | n/a MB |
| sh | 9577 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9588 | sandbox_agent_lsb-claude_code_0000_0000 | 80 | 180.375% | 191.507% | 143.410 s | 206.067 MB | 259.559 MB | 584.508 MB | 635.355 MB | n/a MB | n/a MB |
| bash | 9586 | sandbox_agent_lsb-claude_code_0000_0000 | 80 | 0.000% | 0.000% | 0.000 s | 2.824 MB | 2.824 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 9609 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.949 MB | 2.949 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9610 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 178.153% | 187.952% | 10.750 s | 175.677 MB | 226.578 MB | 553.063 MB | 625.938 MB | n/a MB | n/a MB |
| python3 | 9689 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.484 MB | 9.484 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| sh | 9688 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.367 MB | 1.367 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9735 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.398 MB | 21.398 MB | 25.758 MB | 25.758 MB | n/a MB | n/a MB |
| sh | 9734 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 9886 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9887 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.453 MB | 14.453 MB | 19.836 MB | 19.836 MB | n/a MB | n/a MB |
| sh | 9890 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9891 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.617 MB | 15.617 MB | 20.426 MB | 20.426 MB | n/a MB | n/a MB |
| python3 | 9910 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.762 MB | 9.762 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| sh | 9909 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 9921 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.934 MB | 2.934 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9923 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.734 MB | 8.734 MB | 13.281 MB | 13.281 MB | n/a MB | n/a MB |
| bash | 9942 | sandbox_agent_lsb-claude_code_0000_0000 | 62 | 0.000% | 0.000% | 0.000 s | 2.914 MB | 2.914 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9944 | sandbox_agent_lsb-claude_code_0000_0000 | 62 | 181.087% | 195.973% | 111.160 s | 300.498 MB | 349.035 MB | 682.496 MB | 725.082 MB | n/a MB | n/a MB |
| sh | 9972 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9973 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.148 MB | 21.148 MB | 25.762 MB | 25.762 MB | n/a MB | n/a MB |
| bash | 9983 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.910 MB | 2.910 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9986 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.465 MB | 13.465 MB | 367.176 MB | 367.176 MB | n/a MB | n/a MB |
| bash | 10030 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.750 MB | 2.750 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 10031 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.117 MB | 14.117 MB | 367.285 MB | 367.285 MB | n/a MB | n/a MB |
| python3 | 10049 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 89.304% | 89.304% | 0.900 s | 254.613 MB | 502.070 MB | 432.568 MB | 853.480 MB | n/a MB | n/a MB |
| bash | 10048 | sandbox_agent_lsb-claude_code_0000_0000 | 24 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 10058 | sandbox_agent_lsb-claude_code_0000_0000 | 22 | 177.842% | 187.622% | 37.570 s | 303.528 MB | 356.336 MB | 680.663 MB | 731.668 MB | n/a MB | n/a MB |
| python3 | 10083 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 172.482% | 183.032% | 8.670 s | 751.714 MB | 1320.082 MB | 1110.347 MB | 1679.352 MB | n/a MB | n/a MB |
| bash | 10081 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.914 MB | 2.914 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 10105 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 179.032% | 180.939% | 5.400 s | 786.312 MB | 1098.578 MB | 1187.444 MB | 1623.348 MB | n/a MB | n/a MB |
| bash | 10104 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.004 MB | 3.004 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 10218 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.332 MB | 19.332 MB | 24.605 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 10217 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.570 MB | 1.570 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10223 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 176.332% | 183.928% | 14.200 s | 617.291 MB | 790.941 MB | 987.898 MB | 1159.258 MB | n/a MB | n/a MB |
| bash | 10221 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.965 MB | 2.965 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 10231 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| bash | 10372 | sandbox_agent_lsb-claude_code_0000_0000 | 30 | 0.000% | 0.000% | 0.000 s | 2.500 MB | 2.906 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 10374 | sandbox_agent_lsb-claude_code_0000_0000 | 30 | 67.770% | 82.560% | 19.830 s | 13398.649 MB | 23641.848 MB | 14263.602 MB | 24006.137 MB | n/a MB | n/a MB |
| python3 | 10446 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.031 MB | 15.031 MB | 20.324 MB | 20.324 MB | n/a MB | n/a MB |
| sh | 10445 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 10593 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.855 MB | 2.855 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 10595 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 24.856% | 24.856% | 0.250 s | 46.896 MB | 72.227 MB | 415.617 MB | 457.480 MB | n/a MB | n/a MB |
| bash | 10616 | sandbox_agent_lsb-claude_code_0000_0000 | 49 | 0.000% | 0.000% | 0.000 s | 2.832 MB | 2.832 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 10618 | sandbox_agent_lsb-claude_code_0000_0000 | 49 | 180.529% | 193.615% | 87.220 s | 270.408 MB | 320.078 MB | 654.025 MB | 705.016 MB | n/a MB | n/a MB |
| python3 | 10640 | sandbox_agent_lsb-claude_code_0000_0000 | 38 | 181.756% | 189.880% | 67.700 s | 261.313 MB | 319.859 MB | 641.687 MB | 696.977 MB | n/a MB | n/a MB |
| bash | 10639 | sandbox_agent_lsb-claude_code_0000_0000 | 38 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.715 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 10750 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 160.438% | 184.039% | 8.070 s | 363.348 MB | 552.520 MB | 730.887 MB | 918.629 MB | n/a MB | n/a MB |
| bash | 10748 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 3.047 MB | 3.047 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 11028 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 175.021% | 191.800% | 8.810 s | 366.326 MB | 552.535 MB | 739.983 MB | 918.828 MB | n/a MB | n/a MB |
| bash | 11026 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 11052 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 178.506% | 182.834% | 10.770 s | 338.746 MB | 554.762 MB | 706.664 MB | 923.051 MB | n/a MB | n/a MB |
| bash | 11050 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.695 MB | 2.695 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| bash | 11074 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.637 MB | 1.637 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| claude | 11076 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 6.848 MB | 6.848 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| bash | 11071 | sandbox_agent_lsb-claude_code_0000_0000 | 35 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 11073 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 176.722% | 186.416% | 10.680 s | 358.671 MB | 554.875 MB | 726.340 MB | 923.051 MB | n/a MB | n/a MB |
| tail | 11075 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.152 MB | 1.152 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 11085 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.637 MB | 1.637 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| tail | 11086 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.000 MB | 1.000 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python3 | 11084 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 173.747% | 183.867% | 10.490 s | 341.693 MB | 554.977 MB | 709.340 MB | 923.051 MB | n/a MB | n/a MB |
| claude | 11087 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 6.684 MB | 6.684 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| python3 | 11097 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 177.140% | 186.391% | 10.710 s | 339.781 MB | 555.250 MB | 708.453 MB | 923.047 MB | n/a MB | n/a MB |
| claude | 11100 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 6.773 MB | 6.773 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| tail | 11099 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.035 MB | 1.035 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 11098 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.637 MB | 1.637 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 11108 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 179.378% | 195.644% | 10.830 s | 329.741 MB | 555.086 MB | 700.994 MB | 923.047 MB | n/a MB | n/a MB |
| tail | 11110 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.211 MB | 1.211 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 11109 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.637 MB | 1.637 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| claude | 11111 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 6.785 MB | 6.785 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| bash | 11120 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.637 MB | 1.637 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 11119 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 178.555% | 183.067% | 10.790 s | 358.485 MB | 554.727 MB | 726.338 MB | 923.047 MB | n/a MB | n/a MB |
| tail | 11121 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.102 MB | 1.102 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| claude | 11122 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 6.887 MB | 6.887 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| claude | 11204 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 274.469 MB | 274.469 MB | 5499.879 MB | 5499.879 MB | n/a MB | n/a MB |
| sh | 11226 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11227 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.320 MB | 16.320 MB | 21.770 MB | 21.770 MB | n/a MB | n/a MB |
| python3 | 11239 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.250 MB | 20.250 MB | 24.988 MB | 24.988 MB | n/a MB | n/a MB |
| sh | 11238 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| claude | 11248 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 6.723 MB | 6.723 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| python3 | 11246 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 176.913% | 183.814% | 10.680 s | 354.909 MB | 554.852 MB | 722.889 MB | 923.062 MB | n/a MB | n/a MB |
| bash | 11247 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.719 MB | 1.719 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 11245 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.820 MB | 2.820 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 11359 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.801 MB | 6.801 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| bash | 11358 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.781 MB | 2.781 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| bash | 11386 | sandbox_agent_lsb-claude_code_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 11388 | sandbox_agent_lsb-claude_code_0000_0000 | 11 | 181.923% | 184.943% | 18.300 s | 384.515 MB | 480.141 MB | 773.235 MB | 855.395 MB | n/a MB | n/a MB |
| python3 | 11407 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.121 MB | 13.121 MB | 19.836 MB | 19.836 MB | n/a MB | n/a MB |
| sh | 11406 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11440 | sandbox_agent_lsb-claude_code_0000_0000 | 19 | 179.092% | 184.839% | 32.440 s | 391.952 MB | 466.977 MB | 769.770 MB | 841.605 MB | n/a MB | n/a MB |
| bash | 11438 | sandbox_agent_lsb-claude_code_0000_0000 | 19 | 0.000% | 0.000% | 0.000 s | 2.898 MB | 2.898 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 11525 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.266 MB | 7.266 MB | 11.926 MB | 11.926 MB | n/a MB | n/a MB |
| sh | 11524 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11531 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 190.841% | 190.841% | 1.930 s | 452.764 MB | 495.738 MB | 830.461 MB | 871.980 MB | n/a MB | n/a MB |
| bash | 11529 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 11541 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 11540 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 172.536% | 174.937% | 8.680 s | 309.730 MB | 554.109 MB | 675.683 MB | 919.910 MB | n/a MB | n/a MB |
| claude | 11542 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 6.715 MB | 6.715 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| sh | 11572 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11573 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.582 MB | 20.582 MB | 25.633 MB | 25.633 MB | n/a MB | n/a MB |
| bash | 11576 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.750 MB | 2.750 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 11577 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 236.312 MB | 236.312 MB | 608.742 MB | 608.742 MB | n/a MB | n/a MB |
| python3 | 11606 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.246 MB | 18.246 MB | 24.148 MB | 24.148 MB | n/a MB | n/a MB |
| sh | 11605 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.418 MB | 1.418 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 11699 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11700 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.039 MB | 10.039 MB | 14.648 MB | 14.648 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.484% | 100.000% | 11824.330 MB | 12090.000 MB | 28.209 W | 62.615 W | 104542.443 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-claude_code_0000_0000 | 54.870% | 215.241% | 2003.550 s | 755.712 MB | 23997.039 MB | 1953.277344 MB | 499.792969 MB | 8.504320 MB | 0.054212 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 8218 | 3707.940 | interrupted |
| run0:write_lora_adapter:agent_lsb-claude_code_0000 | -1 | 3707.939 | interrupted |
| engine:execute | 8219 | 3707.937 | interrupted |
| harness:retire | -1 | 308.740 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| harness:attempt_rpc | 1/1 | 0 | 0 | 3396.012 | 0.006 | 3396.005 | 1950.179 | 3396011.566 | 3396011.566 | 3396011.566 |
| harness:await_cli | 1/1 | 0 | 0 | 3393.503 | n/a | n/a | 1947.971 | 3393502.507 | 3393502.507 | 3393502.507 |
| llm:attempt | 87/87 | 0 | 0 | 2563.842 | 4.450 | 2559.391 | 48.343 | 29469.447 | 17152.413 | 93617.614 |
| tool:Bash | 58/58 | 1 | 0 | 631.529 | n/a | n/a | 1870.535 | 10888.429 | 653.955 | 65845.564 |
| tool:mcp__agency__reserve_resource | 1/1 | 0 | 0 | 120.252 | n/a | n/a | 3.726 | 120252.438 | 120252.438 | 120252.438 |
| tool:mcp__agency__trace | 18/18 | 0 | 0 | 33.082 | n/a | n/a | 0.200 | 1837.900 | 1902.129 | 2511.585 |
| tool:mcp__agency__generate | 5/5 | 0 | 0 | 3.845 | n/a | n/a | 1.831 | 769.072 | 722.890 | 1195.782 |
| tool:mcp__agency__inspect | 1/1 | 0 | 0 | 3.812 | n/a | n/a | 0.000 | 3811.733 | 3811.733 | 3811.733 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.090 | 0.721 | 2.369 | 0.000 | 3089.558 | 3089.558 | 3089.558 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.089 | 0.720 | 2.369 | 0.000 | 3089.268 | 3089.268 | 3089.268 |
| tool:mcp__agency__patch | 4/4 | 0 | 0 | 1.570 | n/a | n/a | 0.243 | 392.588 | 391.351 | 407.027 |
| syscall:sendto | 719/719 | 0 | 0 | 1.520 | n/a | n/a | 0.775 | 2.114 | 1.951 | 4.119 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.414 | n/a | n/a | 0.000 | 1413.722 | 1413.722 | 1413.722 |
| syscall:execve | 633/633 | 0 | 0 | 0.979 | n/a | n/a | 0.821 | 1.547 | 1.358 | 2.674 |
| syscall:connect | 271/271 | 0 | 0 | 0.740 | n/a | n/a | 0.494 | 2.729 | 2.129 | 4.105 |
| tool:mcp__agency__attribution | 2/2 | 0 | 0 | 0.573 | n/a | n/a | 0.000 | 286.492 | 286.492 | 289.897 |
| tool:ToolSearch | 2/2 | 0 | 0 | 0.564 | n/a | n/a | 0.491 | 282.159 | 282.159 | 388.917 |
| harness:submit | 1/1 | 0 | 0 | 0.433 | n/a | n/a | 0.000 | 433.068 | 433.068 | 433.068 |
| run:container_call | 6/6 | 0 | 0 | 0.406 | 0.001 | 0.405 | 0.000 | 67.619 | 50.785 | 169.108 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.376 | n/a | n/a | 0.041 | 376.434 | 376.434 | 376.434 |
| sandbox:create | 1/1 | 0 | 0 | 0.347 | 0.258 | 0.089 | 0.000 | 347.459 | 347.459 | 347.459 |
| sandbox:start | 1/1 | 0 | 0 | 0.340 | 0.002 | 0.338 | 0.000 | 339.968 | 339.968 | 339.968 |
| runtime.container_create | 1/1 | 0 | 0 | 0.340 | 0.002 | 0.338 | 0.000 | 339.834 | 339.834 | 339.834 |
| tool:mcp__agency__get_current_resources | 1/1 | 0 | 0 | 0.249 | n/a | n/a | 2.616 | 249.059 | 249.059 | 249.059 |
| tool:Read | 1/1 | 0 | 0 | 0.211 | n/a | n/a | 0.013 | 211.295 | 211.295 | 211.295 |
| tool:mcp__agency__submitted_output | 1/1 | 0 | 0 | 0.203 | n/a | n/a | 0.003 | 203.420 | 203.420 | 203.420 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.190 | n/a | n/a | 0.003 | 189.867 | 189.867 | 189.867 |
| agency:services_start | 1/1 | 0 | 0 | 0.071 | 0.040 | 0.031 | 0.000 | 70.918 | 70.918 | 70.918 |
| run:detect | 1/1 | 0 | 0 | 0.051 | 0.001 | 0.051 | 0.000 | 51.221 | 51.221 | 51.221 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.009 | 0.039 | 0.000 | 48.109 | 48.109 | 48.109 |
| harness:launch | 1/1 | 0 | 0 | 0.047 | n/a | n/a | 0.000 | 47.260 | 47.260 | 47.260 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.005 | 0.005 | 0.000 | 0.031 | 5.108 | 5.108 | 5.108 |
| harness:snapshot | 1/1 | 0 | 0 | 0.004 | n/a | n/a | 0.025 | 4.195 | 4.195 | 4.195 |
| syscall:bind | 2/2 | 0 | 0 | 0.003 | n/a | n/a | 0.000 | 1.291 | 1.291 | 1.472 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.265 | 1.265 | 1.265 |
| sync:container | 6/6 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.071 | 0.076 | 0.089 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.180 | 0.180 | 0.180 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.063 | 0.063 | 0.063 |
| run:write_lora_adapter | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| engine:execute | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 3620 | 0.246 | 0.024 | 576.328 | 0.140 | 25.155982 CPU seconds | n/a |
| GPU 0 memory | MB | 3621 | 11824.330 | 11670.000 | 12090.000 | 11844.000 | n/a | n/a |
| GPU 0 power | W | 3621 | 28.209 | 27.445 | 62.615 | 28.203 | n/a | 104542.443 J |
| GPU 0 proc / 8010-850126 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e memory | MB | 3621 | 3197.205 | 3118.000 | 3464.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 8010-850126 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e estimated power | W | 3244 | 0.574 | 0.000 | 61.337 | 0.000 | n/a | n/a |
| GPU 0 proc / 8010-850126 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e utilization | percent | 3244 | 0.439 | 0.000 | 49.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 8070-851874 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e memory | MB | 3621 | 8145.125 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 8070-851874 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e estimated power | W | 326 | 0.724 | 0.000 | 61.050 | 0.000 | n/a | n/a |
| GPU 0 proc / 8070-851874 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e utilization | percent | 326 | 0.583 | 0.000 | 71.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 3621 | 11342.330 | 11188.000 | 11608.000 | 11362.000 | n/a | n/a |
| GPU 0 utilization | percent | 3621 | 0.484 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 3621 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 3620 | 11.004 | 0.017 | 82.710 | 0.137 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 3620 | 7.228 | 0.000 | 36.973 | 0.250 | n/a | n/a |
| host disk_read_mb_s | MB/s | 3620 | 0.920 | 0.000 | 2169.617 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 3620 | 0.554 | 0.000 | 157.100 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 3620 | 0.115 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 3620 | 0.119 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 3621 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 3621 | 7328.226 | 6415.680 | 30863.832 | 7160.613 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 3620 | 0.052 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 3620 | 0.052 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 3620 | 0.003 | 0.000 | 8.512 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 3620 | 0.007 | 0.000 | 0.463 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10030) rss_mb | MB | 1 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10030) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10031) rss_mb | MB | 1 | 14.117 | 14.117 | 14.117 | 14.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10031) vms_mb | MB | 1 | 367.285 | 367.285 | 367.285 | 367.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10048) CPU | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10048) rss_mb | MB | 24 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10048) main thread run-queue wait | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10048) vms_mb | MB | 24 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10049) CPU | percent | 1 | 89.304 | 89.304 | 89.304 | 89.304 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10049) rss_mb | MB | 2 | 254.613 | 7.156 | 502.070 | 502.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10049) main thread run-queue wait | percent | 1 | 10.228 | 10.228 | 10.228 | 10.228 | 0.103073 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10049) vms_mb | MB | 2 | 432.568 | 11.656 | 853.480 | 853.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10058) CPU | percent | 21 | 177.842 | 167.137 | 187.622 | 180.045 | 37.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10058) rss_mb | MB | 22 | 303.528 | 21.379 | 356.336 | 354.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10058) main thread run-queue wait | percent | 21 | 72.238 | 56.592 | 78.208 | 70.470 | 15.260026 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10058) vms_mb | MB | 22 | 680.663 | 372.297 | 731.668 | 730.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10081) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10081) rss_mb | MB | 6 | 2.914 | 2.914 | 2.914 | 2.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10081) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10081) vms_mb | MB | 6 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — neur.py (PID 10083) CPU | percent | 5 | 172.482 | 155.123 | 183.032 | 173.096 | 8.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — neur.py (PID 10083) rss_mb | MB | 6 | 751.714 | 13.574 | 1320.082 | 1320.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — neur.py (PID 10083) main thread run-queue wait | percent | 5 | 63.267 | 40.284 | 73.651 | 72.116 | 3.180100 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — neur.py (PID 10083) vms_mb | MB | 6 | 1110.347 | 367.074 | 1679.352 | 1679.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10104) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10104) rss_mb | MB | 4 | 3.004 | 3.004 | 3.004 | 3.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10104) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10104) vms_mb | MB | 4 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10105) CPU | percent | 3 | 179.032 | 178.061 | 180.939 | 178.061 | 5.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10105) rss_mb | MB | 4 | 786.312 | 457.883 | 1098.578 | 1098.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10105) main thread run-queue wait | percent | 3 | 73.072 | 71.337 | 74.097 | 74.097 | 2.203984 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10105) vms_mb | MB | 4 | 1187.444 | 818.602 | 1623.348 | 1623.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 10217) rss_mb | MB | 1 | 1.570 | 1.570 | 1.570 | 1.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 10217) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 10218) rss_mb | MB | 1 | 19.332 | 19.332 | 19.332 | 19.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 10218) vms_mb | MB | 1 | 24.605 | 24.605 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10221) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10221) rss_mb | MB | 9 | 2.965 | 2.965 | 2.965 | 2.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10221) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10221) vms_mb | MB | 9 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — scan.py (PID 10223) CPU | percent | 8 | 176.332 | 170.085 | 183.928 | 170.085 | 14.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — scan.py (PID 10223) rss_mb | MB | 9 | 617.291 | 297.301 | 790.941 | 705.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — scan.py (PID 10223) main thread run-queue wait | percent | 8 | 67.634 | 59.315 | 74.173 | 64.336 | 5.446388 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — scan.py (PID 10223) vms_mb | MB | 9 | 987.898 | 676.699 | 1159.258 | 1073.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 10231) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 10231) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10372) CPU | percent | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10372) rss_mb | MB | 30 | 2.500 | 0.617 | 2.906 | 0.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10372) main thread run-queue wait | percent | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10372) vms_mb | MB | 30 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data5.py (PID 10374) CPU | percent | 29 | 67.770 | 0.262 | 82.560 | 0.262 | 19.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data5.py (PID 10374) rss_mb | MB | 30 | 13398.649 | 24.504 | 23641.848 | 8395.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data5.py (PID 10374) main thread run-queue wait | percent | 29 | 0.076 | 0.000 | 0.254 | 0.000 | 0.022175 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data5.py (PID 10374) vms_mb | MB | 30 | 14263.602 | 375.742 | 24006.137 | 24006.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 10445) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 10445) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 10446) rss_mb | MB | 1 | 15.031 | 15.031 | 15.031 | 15.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 10446) vms_mb | MB | 1 | 20.324 | 20.324 | 20.324 | 20.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10593) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10593) rss_mb | MB | 2 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10593) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10593) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data5.py (PID 10595) CPU | percent | 1 | 24.856 | 24.856 | 24.856 | 24.856 | 0.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data5.py (PID 10595) rss_mb | MB | 2 | 46.896 | 21.566 | 72.227 | 72.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data5.py (PID 10595) main thread run-queue wait | percent | 1 | 0.027 | 0.027 | 0.027 | 0.027 | 0.000275 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data5.py (PID 10595) vms_mb | MB | 2 | 415.617 | 373.754 | 457.480 | 457.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10616) CPU | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10616) rss_mb | MB | 49 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10616) main thread run-queue wait | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10616) vms_mb | MB | 49 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det5.py (PID 10618) CPU | percent | 48 | 180.529 | 168.991 | 193.615 | 179.925 | 87.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det5.py (PID 10618) rss_mb | MB | 49 | 270.408 | 170.309 | 320.078 | 312.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det5.py (PID 10618) main thread run-queue wait | percent | 48 | 70.922 | 64.583 | 78.632 | 71.720 | 34.265208 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det5.py (PID 10618) vms_mb | MB | 49 | 654.025 | 577.000 | 705.016 | 689.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10639) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10639) rss_mb | MB | 38 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10639) main thread run-queue wait | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10639) vms_mb | MB | 38 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10640) CPU | percent | 37 | 181.756 | 170.032 | 189.880 | 182.046 | 67.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10640) rss_mb | MB | 38 | 261.313 | 21.004 | 319.859 | 240.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10640) main thread run-queue wait | percent | 37 | 70.216 | 54.725 | 77.260 | 70.090 | 26.153513 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 10640) vms_mb | MB | 38 | 641.687 | 373.469 | 696.977 | 617.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10748) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10748) rss_mb | MB | 6 | 3.047 | 3.047 | 3.047 | 3.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10748) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 10748) vms_mb | MB | 6 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — stage.py (PID 10750) CPU | percent | 5 | 160.438 | 115.337 | 184.039 | 179.695 | 8.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — stage.py (PID 10750) rss_mb | MB | 6 | 363.348 | 229.148 | 552.520 | 475.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — stage.py (PID 10750) main thread run-queue wait | percent | 5 | 52.909 | 22.109 | 74.602 | 68.055 | 2.661504 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — stage.py (PID 10750) vms_mb | MB | 6 | 730.887 | 596.219 | 918.629 | 840.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11026) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11026) rss_mb | MB | 6 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11026) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11026) vms_mb | MB | 6 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pick.py (PID 11028) CPU | percent | 5 | 175.021 | 137.625 | 191.800 | 191.800 | 8.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pick.py (PID 11028) rss_mb | MB | 6 | 366.326 | 229.449 | 552.535 | 475.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pick.py (PID 11028) main thread run-queue wait | percent | 5 | 61.715 | 30.255 | 81.169 | 73.702 | 3.106060 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pick.py (PID 11028) vms_mb | MB | 6 | 739.983 | 596.418 | 918.828 | 841.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11050) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11050) rss_mb | MB | 7 | 2.695 | 2.695 | 2.695 | 2.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11050) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11050) vms_mb | MB | 7 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11052) CPU | percent | 6 | 178.506 | 172.080 | 182.834 | 181.012 | 10.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11052) rss_mb | MB | 7 | 338.746 | 229.160 | 554.762 | 310.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11052) main thread run-queue wait | percent | 6 | 72.798 | 67.239 | 78.921 | 77.653 | 4.392172 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11052) vms_mb | MB | 7 | 706.664 | 596.469 | 923.051 | 678.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11071) CPU | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11071) rss_mb | MB | 35 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11071) main thread run-queue wait | percent | 34 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11071) vms_mb | MB | 35 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11073) CPU | percent | 6 | 176.722 | 165.976 | 186.416 | 178.018 | 10.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11073) rss_mb | MB | 7 | 358.671 | 229.605 | 554.875 | 449.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11073) main thread run-queue wait | percent | 6 | 69.074 | 59.146 | 74.474 | 71.999 | 4.174420 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11073) vms_mb | MB | 7 | 726.340 | 596.465 | 923.051 | 817.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11074) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11074) rss_mb | MB | 7 | 1.637 | 1.637 | 1.637 | 1.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11074) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11074) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11075) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11075) rss_mb | MB | 7 | 1.152 | 1.152 | 1.152 | 1.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11075) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11075) vms_mb | MB | 7 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11076) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11076) rss_mb | MB | 7 | 6.848 | 6.848 | 6.848 | 6.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11076) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11076) vms_mb | MB | 7 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11084) CPU | percent | 6 | 173.747 | 166.990 | 183.867 | 176.927 | 10.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11084) rss_mb | MB | 7 | 341.693 | 222.738 | 554.977 | 449.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11084) main thread run-queue wait | percent | 6 | 70.224 | 60.331 | 79.303 | 73.093 | 4.239808 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11084) vms_mb | MB | 7 | 709.340 | 590.516 | 923.051 | 817.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11085) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11085) rss_mb | MB | 7 | 1.637 | 1.637 | 1.637 | 1.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11085) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11085) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11086) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11086) rss_mb | MB | 7 | 1.000 | 1.000 | 1.000 | 1.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11086) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11086) vms_mb | MB | 7 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11087) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11087) rss_mb | MB | 7 | 6.684 | 6.684 | 6.684 | 6.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11087) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11087) vms_mb | MB | 7 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11097) CPU | percent | 6 | 177.140 | 167.988 | 186.391 | 174.945 | 10.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11097) rss_mb | MB | 7 | 339.781 | 208.648 | 555.250 | 449.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11097) main thread run-queue wait | percent | 6 | 68.515 | 62.583 | 74.027 | 65.783 | 4.142509 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11097) vms_mb | MB | 7 | 708.453 | 584.320 | 923.047 | 817.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11098) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11098) rss_mb | MB | 7 | 1.637 | 1.637 | 1.637 | 1.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11098) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11098) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11099) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11099) rss_mb | MB | 7 | 1.035 | 1.035 | 1.035 | 1.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11099) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11099) vms_mb | MB | 7 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11100) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11100) rss_mb | MB | 7 | 6.773 | 6.773 | 6.773 | 6.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11100) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11100) vms_mb | MB | 7 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11108) CPU | percent | 6 | 179.378 | 170.985 | 195.644 | 178.912 | 10.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11108) rss_mb | MB | 7 | 329.741 | 159.797 | 555.086 | 449.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11108) main thread run-queue wait | percent | 6 | 71.105 | 64.327 | 79.521 | 79.521 | 4.292903 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11108) vms_mb | MB | 7 | 700.994 | 544.254 | 923.047 | 817.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11109) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11109) rss_mb | MB | 7 | 1.637 | 1.637 | 1.637 | 1.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11109) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11109) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11110) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11110) rss_mb | MB | 7 | 1.211 | 1.211 | 1.211 | 1.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11110) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11110) vms_mb | MB | 7 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11111) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11111) rss_mb | MB | 7 | 6.785 | 6.785 | 6.785 | 6.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11111) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11111) vms_mb | MB | 7 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11119) CPU | percent | 6 | 178.555 | 171.046 | 183.067 | 177.036 | 10.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11119) rss_mb | MB | 7 | 358.485 | 229.375 | 554.727 | 449.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11119) main thread run-queue wait | percent | 6 | 66.993 | 45.245 | 74.360 | 73.341 | 4.048266 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11119) vms_mb | MB | 7 | 726.338 | 596.465 | 923.047 | 817.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11120) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11120) rss_mb | MB | 7 | 1.637 | 1.637 | 1.637 | 1.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11120) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11120) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11121) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11121) rss_mb | MB | 7 | 1.102 | 1.102 | 1.102 | 1.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11121) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11121) vms_mb | MB | 7 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11122) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11122) rss_mb | MB | 7 | 6.887 | 6.887 | 6.887 | 6.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11122) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11122) vms_mb | MB | 7 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 11204) rss_mb | MB | 1 | 274.469 | 274.469 | 274.469 | 274.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 11204) vms_mb | MB | 1 | 5499.879 | 5499.879 | 5499.879 | 5499.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11226) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11226) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11227) rss_mb | MB | 1 | 16.320 | 16.320 | 16.320 | 16.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11227) vms_mb | MB | 1 | 21.770 | 21.770 | 21.770 | 21.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11238) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11238) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11239) rss_mb | MB | 1 | 20.250 | 20.250 | 20.250 | 20.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11239) vms_mb | MB | 1 | 24.988 | 24.988 | 24.988 | 24.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11245) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11245) rss_mb | MB | 7 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11245) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11245) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11246) CPU | percent | 6 | 176.913 | 170.942 | 183.814 | 174.920 | 10.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11246) rss_mb | MB | 7 | 354.909 | 229.680 | 554.852 | 311.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11246) main thread run-queue wait | percent | 6 | 69.962 | 60.045 | 74.418 | 74.418 | 4.223543 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11246) vms_mb | MB | 7 | 722.889 | 596.477 | 923.062 | 678.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11247) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11247) rss_mb | MB | 7 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11247) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11247) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11248) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11248) rss_mb | MB | 7 | 6.723 | 6.723 | 6.723 | 6.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11248) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11248) vms_mb | MB | 7 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11358) rss_mb | MB | 1 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11358) vms_mb | MB | 1 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 11359) rss_mb | MB | 1 | 6.801 | 6.801 | 6.801 | 6.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 11359) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11386) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11386) rss_mb | MB | 11 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11386) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11386) vms_mb | MB | 11 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det6.py (PID 11388) CPU | percent | 10 | 181.923 | 178.925 | 184.943 | 182.905 | 18.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det6.py (PID 11388) rss_mb | MB | 11 | 384.515 | 210.559 | 480.141 | 384.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det6.py (PID 11388) main thread run-queue wait | percent | 10 | 72.756 | 68.890 | 80.962 | 74.296 | 7.318664 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det6.py (PID 11388) vms_mb | MB | 11 | 773.235 | 662.867 | 855.395 | 759.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11406) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11406) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11407) rss_mb | MB | 1 | 13.121 | 13.121 | 13.121 | 13.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11407) vms_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11438) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11438) rss_mb | MB | 19 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11438) main thread run-queue wait | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11438) vms_mb | MB | 19 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det7.py (PID 11440) CPU | percent | 18 | 179.092 | 172.093 | 184.839 | 173.931 | 32.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det7.py (PID 11440) rss_mb | MB | 19 | 391.952 | 169.957 | 466.977 | 438.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det7.py (PID 11440) main thread run-queue wait | percent | 18 | 71.817 | 68.622 | 77.160 | 74.445 | 13.008555 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det7.py (PID 11440) vms_mb | MB | 19 | 769.770 | 545.617 | 841.605 | 841.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11524) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11524) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11525) rss_mb | MB | 1 | 7.266 | 7.266 | 7.266 | 7.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11525) vms_mb | MB | 1 | 11.926 | 11.926 | 11.926 | 11.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11529) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11529) rss_mb | MB | 8 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11529) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11529) vms_mb | MB | 8 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det8.py (PID 11531) CPU | percent | 1 | 190.841 | 190.841 | 190.841 | 190.841 | 1.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det8.py (PID 11531) rss_mb | MB | 2 | 452.764 | 409.789 | 495.738 | 495.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det8.py (PID 11531) main thread run-queue wait | percent | 1 | 69.149 | 69.149 | 69.149 | 69.149 | 0.699312 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det8.py (PID 11531) vms_mb | MB | 2 | 830.461 | 788.941 | 871.980 | 871.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11540) CPU | percent | 5 | 172.536 | 169.990 | 174.937 | 174.040 | 8.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11540) rss_mb | MB | 6 | 309.730 | 69.707 | 554.109 | 69.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11540) main thread run-queue wait | percent | 5 | 68.156 | 51.852 | 75.219 | 73.803 | 3.428841 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 11540) vms_mb | MB | 6 | 675.683 | 434.660 | 919.910 | 434.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11541) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11541) rss_mb | MB | 6 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11541) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11541) vms_mb | MB | 6 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11542) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11542) rss_mb | MB | 6 | 6.715 | 6.715 | 6.715 | 6.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11542) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 11542) vms_mb | MB | 6 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11572) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11572) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11573) rss_mb | MB | 1 | 20.582 | 20.582 | 20.582 | 20.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11573) vms_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11576) rss_mb | MB | 1 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11576) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 11577) rss_mb | MB | 1 | 236.312 | 236.312 | 236.312 | 236.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 11577) vms_mb | MB | 1 | 608.742 | 608.742 | 608.742 | 608.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11605) rss_mb | MB | 1 | 1.418 | 1.418 | 1.418 | 1.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11605) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11606) rss_mb | MB | 1 | 18.246 | 18.246 | 18.246 | 18.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11606) vms_mb | MB | 1 | 24.148 | 24.148 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11699) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11699) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude_lifecycle_hook.py (PID 11700) rss_mb | MB | 1 | 10.039 | 10.039 | 10.039 | 10.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude_lifecycle_hook.py (PID 11700) vms_mb | MB | 1 | 14.648 | 14.648 | 14.648 | 14.648 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 7027) CPU | percent | 3620 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 7027) io read MB/s | MB/s | 3620 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 7027) io write MB/s | MB/s | 3620 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 7027) rss_mb | MB | 3621 | 2.820 | 2.121 | 3.383 | 2.121 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 7027) main thread run-queue wait | percent | 3620 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 7027) vms_mb | MB | 3621 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 8010) CPU | percent | 3620 | 1.972 | 0.000 | 166.482 | 0.995 | 76.630000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 8010) io read MB/s | MB/s | 3620 | 0.086 | 0.000 | 227.658 | 0.000 | 965.820312 MB | n/a |
| Agency harness — python -m lsbench (PID 8010) io write MB/s | MB/s | 3620 | 0.393 | 0.002 | 286.215 | 0.023 | 1434.687500 MB | n/a |
| Agency harness — python -m lsbench (PID 8010) rss_mb | MB | 3621 | 2663.679 | 1996.844 | 3035.695 | 2670.168 | n/a | n/a |
| Agency harness — python -m lsbench (PID 8010) main thread run-queue wait | percent | 3620 | 0.000 | 0.000 | 0.547 | 0.000 | 0.022142 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 8010) vms_mb | MB | 3621 | 16271.204 | 14083.883 | 16540.699 | 16540.699 | n/a | n/a |
| Python — vllm (PID 8019) CPU | percent | 3620 | 0.114 | 0.000 | 92.548 | 0.000 | 6.770000 CPU seconds | n/a |
| Python — vllm (PID 8019) io read MB/s | MB/s | 3620 | 0.040 | 0.000 | 133.230 | 0.000 | 520.656250 MB | n/a |
| Python — vllm (PID 8019) io write MB/s | MB/s | 3620 | 0.000 | 0.000 | 0.008 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 8019) rss_mb | MB | 3621 | 1619.802 | 1397.773 | 1795.402 | 1407.555 | n/a | n/a |
| Python — vllm (PID 8019) main thread run-queue wait | percent | 3620 | 0.005 | 0.000 | 1.391 | 0.000 | 0.223425 run-queue seconds | n/a |
| Python — vllm (PID 8019) vms_mb | MB | 3621 | 12003.700 | 11931.285 | 12004.305 | 12004.305 | n/a | n/a |
| Python — python -c (PID 8069) CPU | percent | 3620 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 8069) io read MB/s | MB/s | 3620 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 8069) io write MB/s | MB/s | 3620 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 8069) rss_mb | MB | 3621 | 10.302 | 7.938 | 12.207 | 7.938 | n/a | n/a |
| Python — python -c (PID 8069) main thread run-queue wait | percent | 3620 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 8069) vms_mb | MB | 3621 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 8070) CPU | percent | 3620 | 1.342 | 0.000 | 572.068 | 1.990 | 64.940000 CPU seconds | n/a |
| VLLM::EngineCore (PID 8070) io read MB/s | MB/s | 3620 | 0.144 | 0.000 | 491.161 | 0.000 | 1906.238281 MB | n/a |
| VLLM::EngineCore (PID 8070) io write MB/s | MB/s | 3620 | 0.000 | 0.000 | 0.004 | 0.000 | 0.023438 MB | n/a |
| VLLM::EngineCore (PID 8070) rss_mb | MB | 3621 | 2108.891 | 1825.125 | 2326.254 | 1864.777 | n/a | n/a |
| VLLM::EngineCore (PID 8070) main thread run-queue wait | percent | 3620 | 0.000 | 0.000 | 0.007 | 0.000 | 0.000230 run-queue seconds | n/a |
| VLLM::EngineCore (PID 8070) vms_mb | MB | 3621 | 21828.801 | 21828.801 | 21828.816 | 21828.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 8348) CPU | percent | 3620 | 0.003 | 0.000 | 5.506 | 0.000 | 0.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 8348) rss_mb | MB | 3621 | 0.439 | 0.145 | 0.551 | 0.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 8348) main thread run-queue wait | percent | 3620 | 0.028 | 0.000 | 8.057 | 0.000 | 1.031806 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 8348) vms_mb | MB | 3621 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8387) CPU | percent | 3620 | 0.007 | 0.000 | 15.731 | 0.000 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8387) rss_mb | MB | 3621 | 1.070 | 0.223 | 1.473 | 0.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8387) main thread run-queue wait | percent | 3620 | 0.029 | 0.000 | 7.675 | 0.000 | 1.095510 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8387) vms_mb | MB | 3621 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8492) CPU | percent | 3620 | 25.355 | 0.000 | 120.601 | 0.000 | 927.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8492) rss_mb | MB | 3621 | 101.106 | 3.086 | 107.844 | 98.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8492) main thread run-queue wait | percent | 3620 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000180 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8492) vms_mb | MB | 3621 | 973.004 | 4.262 | 974.969 | 974.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 8498) CPU | percent | 1 | 99.612 | 99.612 | 99.612 | 99.612 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 8498) rss_mb | MB | 2 | 56.129 | 28.062 | 84.195 | 84.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 8498) main thread run-queue wait | percent | 1 | 0.007 | 0.007 | 0.007 | 0.007 | 0.000067 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 8498) vms_mb | MB | 2 | 66.793 | 35.535 | 98.051 | 98.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 8511) CPU | percent | 3310 | 2.735 | 0.000 | 69.528 | 4.974 | 91.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 8511) rss_mb | MB | 3311 | 292.386 | 70.898 | 343.766 | 301.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 8511) main thread run-queue wait | percent | 3310 | 7.421 | 0.000 | 91.874 | 0.021 | 247.322977 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 8511) vms_mb | MB | 3311 | 5499.870 | 5484.289 | 5499.910 | 5499.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8560) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8560) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8562) rss_mb | MB | 1 | 18.238 | 18.238 | 18.238 | 18.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8562) vms_mb | MB | 1 | 24.098 | 24.098 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8586) rss_mb | MB | 1 | 1.363 | 1.363 | 1.363 | 1.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8586) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8587) rss_mb | MB | 1 | 14.242 | 14.242 | 14.242 | 14.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8587) vms_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8606) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8606) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8607) rss_mb | MB | 1 | 18.668 | 18.668 | 18.668 | 18.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8607) vms_mb | MB | 1 | 24.148 | 24.148 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8748) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8748) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8749) rss_mb | MB | 1 | 18.629 | 18.629 | 18.629 | 18.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8749) vms_mb | MB | 1 | 24.098 | 24.098 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8797) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8797) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8798) rss_mb | MB | 1 | 18.215 | 18.215 | 18.215 | 18.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8798) vms_mb | MB | 1 | 23.098 | 23.098 | 23.098 | 23.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9028) rss_mb | MB | 1 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9028) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 9031) rss_mb | MB | 1 | 14.461 | 14.461 | 14.461 | 14.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 9031) vms_mb | MB | 1 | 367.199 | 367.199 | 367.199 | 367.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9075) rss_mb | MB | 1 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9075) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pip (PID 9077) rss_mb | MB | 1 | 11.316 | 11.316 | 11.316 | 11.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pip (PID 9077) vms_mb | MB | 1 | 14.895 | 14.895 | 14.895 | 14.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 9078) rss_mb | MB | 1 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 9078) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9135) rss_mb | MB | 1 | 3.035 | 3.035 | 3.035 | 3.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9135) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 9137) rss_mb | MB | 1 | 22.051 | 22.051 | 22.051 | 22.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 9137) vms_mb | MB | 1 | 373.633 | 373.633 | 373.633 | 373.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9154) rss_mb | MB | 1 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9154) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 9156) rss_mb | MB | 1 | 126.906 | 126.906 | 126.906 | 126.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 9156) vms_mb | MB | 1 | 476.934 | 476.934 | 476.934 | 476.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9173) CPU | percent | 138 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9173) rss_mb | MB | 139 | 3.090 | 3.090 | 3.090 | 3.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9173) main thread run-queue wait | percent | 138 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9173) vms_mb | MB | 139 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det.py (PID 9175) CPU | percent | 138 | 179.972 | 163.017 | 192.973 | 191.390 | 249.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det.py (PID 9175) rss_mb | MB | 139 | 156.762 | 62.430 | 226.293 | 203.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det.py (PID 9175) main thread run-queue wait | percent | 138 | 74.382 | 63.752 | 86.879 | 69.687 | 103.298065 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det.py (PID 9175) vms_mb | MB | 139 | 535.977 | 439.855 | 607.395 | 607.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9283) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9283) rss_mb | MB | 3 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9283) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9283) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9284) CPU | percent | 2 | 4.972 | 0.994 | 8.951 | 8.951 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9284) rss_mb | MB | 3 | 13.516 | 9.172 | 21.703 | 21.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9284) main thread run-queue wait | percent | 2 | 43.582 | 41.416 | 45.748 | 41.416 | 0.876679 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9284) vms_mb | MB | 3 | 18.033 | 13.492 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9404) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9404) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9405) rss_mb | MB | 1 | 20.840 | 20.840 | 20.840 | 20.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9405) vms_mb | MB | 1 | 25.504 | 25.504 | 25.504 | 25.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 9414) rss_mb | MB | 1 | 285.398 | 285.398 | 285.398 | 285.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 9414) vms_mb | MB | 1 | 5499.879 | 5499.879 | 5499.879 | 5499.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9428) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9428) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9429) rss_mb | MB | 1 | 15.500 | 15.500 | 15.500 | 15.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9429) vms_mb | MB | 1 | 20.176 | 20.176 | 20.176 | 20.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9486) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9486) rss_mb | MB | 2 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9486) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9486) vms_mb | MB | 2 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9488) CPU | percent | 1 | 182.857 | 182.857 | 182.857 | 182.857 | 1.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9488) rss_mb | MB | 2 | 162.311 | 135.434 | 189.188 | 189.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9488) main thread run-queue wait | percent | 1 | 81.457 | 81.457 | 81.457 | 81.457 | 0.819664 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9488) vms_mb | MB | 2 | 547.191 | 525.535 | 568.848 | 568.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9501) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9501) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9502) rss_mb | MB | 1 | 10.621 | 10.621 | 10.621 | 10.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9502) vms_mb | MB | 1 | 15.203 | 15.203 | 15.203 | 15.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9503) rss_mb | MB | 1 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9503) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9504) rss_mb | MB | 1 | 142.188 | 142.188 | 142.188 | 142.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9504) vms_mb | MB | 1 | 521.293 | 521.293 | 521.293 | 521.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9577) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9577) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9578) rss_mb | MB | 1 | 18.672 | 18.672 | 18.672 | 18.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9578) vms_mb | MB | 1 | 24.098 | 24.098 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9586) CPU | percent | 79 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9586) rss_mb | MB | 80 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9586) main thread run-queue wait | percent | 79 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9586) vms_mb | MB | 80 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det2.py (PID 9588) CPU | percent | 79 | 180.375 | 173.682 | 191.507 | 180.950 | 143.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det2.py (PID 9588) rss_mb | MB | 80 | 206.067 | 102.176 | 259.559 | 257.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det2.py (PID 9588) main thread run-queue wait | percent | 79 | 72.378 | 64.619 | 82.348 | 74.969 | 57.545265 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det2.py (PID 9588) vms_mb | MB | 80 | 584.508 | 478.070 | 635.355 | 632.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9609) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9609) rss_mb | MB | 7 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9609) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9609) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9610) CPU | percent | 6 | 178.153 | 155.079 | 187.952 | 181.938 | 10.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9610) rss_mb | MB | 7 | 175.677 | 13.820 | 226.578 | 191.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9610) main thread run-queue wait | percent | 6 | 69.139 | 56.860 | 73.863 | 70.742 | 4.171922 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9610) vms_mb | MB | 7 | 553.063 | 367.324 | 625.938 | 567.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9688) rss_mb | MB | 1 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9688) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9689) rss_mb | MB | 1 | 9.484 | 9.484 | 9.484 | 9.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9689) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9734) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9734) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9735) rss_mb | MB | 1 | 21.398 | 21.398 | 21.398 | 21.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9735) vms_mb | MB | 1 | 25.758 | 25.758 | 25.758 | 25.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9886) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9886) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9887) rss_mb | MB | 1 | 14.453 | 14.453 | 14.453 | 14.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9887) vms_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9890) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9890) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9891) rss_mb | MB | 1 | 15.617 | 15.617 | 15.617 | 15.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9891) vms_mb | MB | 1 | 20.426 | 20.426 | 20.426 | 20.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9909) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9909) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9910) rss_mb | MB | 1 | 9.762 | 9.762 | 9.762 | 9.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9910) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9921) rss_mb | MB | 1 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9921) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data3.py (PID 9923) rss_mb | MB | 1 | 8.734 | 8.734 | 8.734 | 8.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — data3.py (PID 9923) vms_mb | MB | 1 | 13.281 | 13.281 | 13.281 | 13.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9942) CPU | percent | 61 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9942) rss_mb | MB | 62 | 2.914 | 2.914 | 2.914 | 2.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9942) main thread run-queue wait | percent | 61 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9942) vms_mb | MB | 62 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det3.py (PID 9944) CPU | percent | 61 | 181.087 | 169.044 | 195.973 | 181.979 | 111.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det3.py (PID 9944) rss_mb | MB | 62 | 300.498 | 178.660 | 349.035 | 283.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det3.py (PID 9944) main thread run-queue wait | percent | 61 | 72.881 | 69.930 | 82.003 | 71.056 | 44.737731 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det3.py (PID 9944) vms_mb | MB | 62 | 682.496 | 577.211 | 725.082 | 659.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9972) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9972) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9973) rss_mb | MB | 1 | 21.148 | 21.148 | 21.148 | 21.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9973) vms_mb | MB | 1 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9983) rss_mb | MB | 1 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9983) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 9986) rss_mb | MB | 1 | 13.465 | 13.465 | 13.465 | 13.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 9986) vms_mb | MB | 1 | 367.176 | 367.176 | 367.176 | 367.176 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 CPU | percent | 3620 | 54.870 | 0.175 | 215.241 | 0.205 | 2003.549663 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 3620 | 10.126 | 0.000 | 75.214 | 0.013 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 3620 | 10.845 | 0.000 | 82.313 | 0.013 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_full_pct | percent of wall time stalled | 3620 | 0.075 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_some_pct | percent of wall time stalled | 3620 | 0.075 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io read MB/s | MB/s | 3620 | 0.311 | 0.000 | 254.174 | 0.000 | 1953.277344 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io write MB/s | MB/s | 3620 | 0.137 | 0.000 | 161.573 | 0.000 | 499.792969 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory | MB | 3621 | 755.712 | 18.113 | 23997.039 | 745.566 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_full_pct | percent of wall time stalled | 3620 | 0.030 | 0.000 | 26.321 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_some_pct | percent of wall time stalled | 3620 | 0.030 | 0.000 | 26.328 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net rx MB/s | MB/s | 3620 | 0.002 | 0.000 | 8.222 | 0.000 | 8.504320 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net tx MB/s | MB/s | 3620 | 0.000 | 0.000 | 0.011 | 0.000 | 0.054212 MB | n/a |
| workload total CPU | percent | 3620 | 3.427 | 0.104 | 832.017 | 2.278 | 148.364574 CPU seconds | n/a |
| workload total memory | MB | 3621 | 5654.347 | 4654.508 | 6238.688 | 5773.059 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
