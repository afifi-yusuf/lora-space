# agprof summary

- Duration: **4201.542 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **123 calls**, 123 succeeded, 0 failed, 0 interrupted, n/a reported retries, 2774.516 s total wait
- Tools: **135/135 completed**, 3 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **405718** at 1.97 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 4196007.033 / 4196007.033 ms |
| LLM latency p50 / p95 | 15139.452 / 66679.676 ms |
| LLM TTFT p50 / p95 | 8559.613 / 45508.130 ms |
| LLM input / output tokens | 290 / 277767 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 123 total, 123 succeeded, 0 failed, 0 interrupted |
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
| Bash | 95/95 | 92 | 3 | 0 | n/a | n/a |
| ToolSearch | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 15/15 | 15 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 15/15 | 15 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 6.652% | 176.738% | 286.013 s | 7826.278 MB | 11164.066 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 2662 |  | 4168 | 4.742% | 176.074% | 200.490 s | 3195.811 MB | 4624.148 MB | 16468.178 MB | 18585.648 MB | 318.218750 MB | 5100.261719 MB |
| tail | 3079 | sandbox_agent_lsb-claude_code_0000_0000 | 4162 | 0.004% | 5.233% | 0.320 s | 0.702 MB | 1.426 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 3177 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 99.911% | 99.911% | 1.010 s | 53.967 MB | 82.133 MB | 65.354 MB | 96.672 MB | n/a MB | n/a MB |
| lsb_grid_worker | 1698 |  | 4168 | 0.000% | 0.000% | 0.000 s | 2.678 MB | 3.414 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 3171 | sandbox_agent_lsb-claude_code_0000_0000 | 4162 | 29.946% | 108.443% | 1255.680 s | 100.782 MB | 108.949 MB | 973.196 MB | 978.234 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 2776 |  | 4168 | 1.732% | 110.689% | 77.270 s | 2086.443 MB | 2320.238 MB | 21204.363 MB | 21204.363 MB | 330.917969 MB | 0.027344 MB |
| python | 2775 |  | 4168 | 0.000% | 0.000% | 0.000 s | 9.675 MB | 12.188 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 3048 | sandbox_agent_lsb-claude_code_0000_0000 | 4162 | 0.003% | 2.818% | 0.200 s | 0.350 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| vllm | 2667 |  | 4168 | 0.174% | 17.405% | 8.050 s | 1610.266 MB | 1803.953 MB | 11042.694 MB | 11044.586 MB | 73.593750 MB | 0.074219 MB |
| claude | 3190 | sandbox_agent_lsb-claude_code_0000_0000 | 4131 | 3.129% | 69.474% | 130.620 s | 292.125 MB | 344.441 MB | 5499.871 MB | 5499.879 MB | n/a MB | n/a MB |
| sh | 3238 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3240 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.465 MB | 9.465 MB | 13.617 MB | 13.617 MB | n/a MB | n/a MB |
| bash | 3272 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.758 MB | 2.758 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| head | 3278 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.418 MB | 0.418 MB | n/a MB | n/a MB |
| free | 3277 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.156 MB | 0.156 MB | n/a MB | n/a MB |
| python3 | 3297 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.637 MB | 16.637 MB | 22.066 MB | 22.066 MB | n/a MB | n/a MB |
| sh | 3296 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 3301 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3302 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.906 MB | 9.906 MB | 13.617 MB | 13.617 MB | n/a MB | n/a MB |
| python3 | 3366 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.656 MB | 8.656 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| bash | 3342 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.703 MB | 2.703 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 3344 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.121 MB | 12.121 MB | 15.809 MB | 15.809 MB | n/a MB | n/a MB |
| python3 | 3409 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.477 MB | 12.477 MB | 15.980 MB | 15.980 MB | n/a MB | n/a MB |
| bash | 3385 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.957 MB | 2.957 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 3387 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 3.969% | 3.969% | 0.040 s | 12.477 MB | 12.477 MB | 15.980 MB | 15.980 MB | n/a MB | n/a MB |
| python3 | 3446 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.363 MB | 8.363 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| sh | 3484 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| bash | 3764 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.711 MB | 2.711 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 3765 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 7.192% | 11.906% | 0.290 s | 12.780 MB | 13.438 MB | 16.495 MB | 17.527 MB | n/a MB | n/a MB |
| python3 | 3784 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 3820 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 3841 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.457 MB | 9.457 MB | 13.246 MB | 13.246 MB | n/a MB | n/a MB |
| python3 | 3843 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.738 MB | 7.738 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 3856 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.352 MB | 7.352 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 3901 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.398 MB | 20.398 MB | 25.246 MB | 25.246 MB | n/a MB | n/a MB |
| sh | 3900 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.426 MB | 1.426 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3929 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 2.978% | 3.971% | 0.060 s | 12.500 MB | 12.500 MB | 15.918 MB | 15.918 MB | n/a MB | n/a MB |
| python3 | 3930 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| bash | 3928 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.785 MB | 2.785 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 3968 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.672 MB | 6.672 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 4002 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.984 MB | 6.984 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 4049 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.605 MB | 10.605 MB | 15.230 MB | 15.230 MB | n/a MB | n/a MB |
| sh | 4048 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4068 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.512 MB | 21.512 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 4067 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 4161 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4162 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.336 MB | 15.336 MB | 20.426 MB | 20.426 MB | n/a MB | n/a MB |
| sh | 4235 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.285 MB | 1.285 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4236 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.219 MB | 21.219 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python3 | 4251 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.441 MB | 9.441 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| sh | 4250 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 4291 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4292 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.660 MB | 5.660 MB | 11.645 MB | 11.645 MB | n/a MB | n/a MB |
| bash | 4335 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 4337 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 145.828% | 145.828% | 1.470 s | 269.154 MB | 516.629 MB | 515.723 MB | 817.633 MB | n/a MB | n/a MB |
| python3 | 4342 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.016 MB | 18.016 MB | 24.098 MB | 24.098 MB | n/a MB | n/a MB |
| sh | 4341 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 4350 | sandbox_agent_lsb-claude_code_0000_0000 | 340 | 0.000% | 0.000% | 0.000 s | 2.855 MB | 2.855 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4351 | sandbox_agent_lsb-claude_code_0000_0000 | 340 | 104.749% | 126.313% | 357.280 s | 2066.431 MB | 3019.371 MB | 3220.773 MB | 3243.488 MB | n/a MB | n/a MB |
| sh | 4391 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4392 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.438 MB | 15.438 MB | 20.324 MB | 20.324 MB | n/a MB | n/a MB |
| sh | 4414 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| sh | 4435 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 4434 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 4444 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.840 MB | 2.840 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 4449 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.730 MB | 1.730 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| ps | 4448 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| claude | 4450 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.645 MB | 6.645 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| python3 | 4466 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.883 MB | 8.883 MB | 13.410 MB | 13.410 MB | n/a MB | n/a MB |
| sh | 4465 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 4496 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4497 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.328 MB | 16.328 MB | 21.770 MB | 21.770 MB | n/a MB | n/a MB |
| python3 | 4535 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.754 MB | 20.754 MB | 25.758 MB | 25.758 MB | n/a MB | n/a MB |
| sh | 4534 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4621 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 66.494% | 66.494% | 0.670 s | 204.289 MB | 349.875 MB | 458.531 MB | 666.125 MB | n/a MB | n/a MB |
| bash | 4619 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 3.016 MB | 3.016 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4627 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 149.142% | 168.975% | 4.500 s | 1911.892 MB | 2029.477 MB | 2459.800 MB | 2702.023 MB | n/a MB | n/a MB |
| sh | 4631 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4632 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.027 MB | 8.027 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python3 | 4758 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 2.480% | 2.976% | 0.050 s | 12.352 MB | 12.352 MB | 15.801 MB | 15.801 MB | n/a MB | n/a MB |
| bash | 4756 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.750 MB | 2.750 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4767 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.902 MB | 7.902 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| head | 4759 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 4804 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.590 MB | 7.590 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 4841 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.680 MB | 7.680 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 4873 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 158.910% | 175.101% | 14.450 s | 1779.222 MB | 2402.113 MB | 2178.768 MB | 2702.016 MB | n/a MB | n/a MB |
| bash | 4871 | sandbox_agent_lsb-claude_code_0000_0000 | 13 | 0.000% | 0.000% | 0.000 s | 2.941 MB | 2.941 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4877 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 2.963% | 3.968% | 0.060 s | 12.414 MB | 12.414 MB | 15.793 MB | 15.793 MB | n/a MB | n/a MB |
| awk | 4878 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.629 MB | 1.629 MB | 3.504 MB | 3.504 MB | n/a MB | n/a MB |
| tr | 4879 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.113 MB | 1.113 MB | 2.465 MB | 2.465 MB | n/a MB | n/a MB |
| python3 | 4906 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.008 MB | 8.008 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 4938 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sh | 4987 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4988 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.812 MB | 19.812 MB | 24.859 MB | 24.859 MB | n/a MB | n/a MB |
| bash | 4990 | sandbox_agent_lsb-claude_code_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 2.988 MB | 2.988 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4992 | sandbox_agent_lsb-claude_code_0000_0000 | 12 | 170.225% | 175.652% | 18.870 s | 830.619 MB | 887.305 MB | 1527.746 MB | 1577.094 MB | n/a MB | n/a MB |
| python3 | 5008 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 163.666% | 174.074% | 8.230 s | 593.297 MB | 778.102 MB | 1359.376 MB | 1688.020 MB | n/a MB | n/a MB |
| bash | 5006 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.887 MB | 2.887 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 5022 | sandbox_agent_lsb-claude_code_0000_0000 | 187 | 0.000% | 0.000% | 0.000 s | 2.739 MB | 2.754 MB | 3.964 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 5024 | sandbox_agent_lsb-claude_code_0000_0000 | 186 | 170.521% | 177.515% | 318.270 s | 2586.002 MB | 2867.129 MB | 2873.418 MB | 3136.867 MB | n/a MB | n/a MB |
| sh | 5035 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5036 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 2.982% | 2.982% | 0.060 s | 13.178 MB | 16.977 MB | 18.336 MB | 22.066 MB | n/a MB | n/a MB |
| awk | 5040 | sandbox_agent_lsb-claude_code_0000_0000 | 114 | 0.000% | 0.000% | 0.000 s | 1.523 MB | 1.523 MB | 3.504 MB | 3.504 MB | n/a MB | n/a MB |
| tr | 5041 | sandbox_agent_lsb-claude_code_0000_0000 | 114 | 0.000% | 0.000% | 0.000 s | 1.113 MB | 1.113 MB | 2.465 MB | 2.465 MB | n/a MB | n/a MB |
| bash | 5038 | sandbox_agent_lsb-claude_code_0000_0000 | 116 | 0.000% | 0.000% | 0.000 s | 2.711 MB | 2.711 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 5039 | sandbox_agent_lsb-claude_code_0000_0000 | 114 | 0.227% | 1.988% | 0.260 s | 12.315 MB | 12.758 MB | 15.812 MB | 16.156 MB | n/a MB | n/a MB |
| python3 | 5042 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 5043 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.355 MB | 4.355 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 5044 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.133 MB | 12.133 MB | 15.758 MB | 15.758 MB | n/a MB | n/a MB |
| python3 | 5045 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.395 MB | 4.395 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 5046 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.949 MB | 6.949 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5047 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.137 MB | 7.137 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5048 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.590 MB | 7.590 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5049 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.652 MB | 7.652 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5050 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.816 MB | 7.816 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5051 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.852 MB | 7.852 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5052 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.574 MB | 7.574 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5053 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.895 MB | 7.895 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5054 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.004 MB | 8.004 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5055 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.172 MB | 8.172 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5059 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.258 MB | 12.258 MB | 15.758 MB | 15.758 MB | n/a MB | n/a MB |
| python3 | 5061 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.699 MB | 7.699 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5063 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.371 MB | 7.371 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5064 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.820 MB | 6.820 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5065 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.703 MB | 6.703 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5066 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.039 MB | 8.039 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5067 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.105 MB | 8.105 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5070 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.824 MB | 6.824 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5071 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.152 MB | 7.152 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5072 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.301 MB | 7.301 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5073 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.352 MB | 7.352 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5074 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.387 MB | 4.387 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 5075 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.258 MB | 12.258 MB | 15.758 MB | 15.758 MB | n/a MB | n/a MB |
| python3 | 5076 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.383 MB | 7.383 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5077 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.891 MB | 7.891 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5078 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.219 MB | 8.219 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5095 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.047 MB | 8.047 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5096 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.355 MB | 8.355 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5101 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.496 MB | 7.496 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5102 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.953 MB | 7.953 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5104 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.199 MB | 7.199 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5105 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.676 MB | 6.676 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5106 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.742 MB | 7.742 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5108 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.199 MB | 7.199 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5110 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.051 MB | 7.051 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5111 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.008 MB | 7.008 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5112 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.199 MB | 7.199 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5113 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.387 MB | 7.387 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5114 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.637 MB | 7.637 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5115 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.824 MB | 7.824 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5117 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.027 MB | 7.027 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5118 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.172 MB | 7.172 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5119 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.383 MB | 7.383 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5120 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.438 MB | 7.438 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5121 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.852 MB | 7.852 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5122 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.020 MB | 8.020 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5123 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.215 MB | 8.215 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5124 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.125 MB | 8.125 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5127 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.375 MB | 4.375 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 5128 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.203 MB | 1.203 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| python3 | 5129 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.258 MB | 12.258 MB | 15.758 MB | 15.758 MB | n/a MB | n/a MB |
| python3 | 5130 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.367 MB | 7.367 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5131 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.438 MB | 7.438 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5132 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.871 MB | 7.871 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5133 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.867 MB | 7.867 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5134 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.527 MB | 7.527 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5135 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.699 MB | 7.699 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5136 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.891 MB | 7.891 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5137 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 1.211% | 2.973% | 0.110 s | 9.266 MB | 9.402 MB | 13.227 MB | 13.250 MB | n/a MB | n/a MB |
| python3 | 5138 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 1.322% | 2.974% | 0.120 s | 9.096 MB | 9.227 MB | 13.223 MB | 13.246 MB | n/a MB | n/a MB |
| python3 | 5139 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 1.099% | 1.987% | 0.100 s | 9.204 MB | 9.340 MB | 13.223 MB | 13.246 MB | n/a MB | n/a MB |
| python3 | 5140 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.312 MB | 8.312 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5141 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.188 MB | 8.188 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5142 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.469 MB | 8.469 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5145 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.473 MB | 5.473 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| python3 | 5146 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.512 MB | 5.512 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| python3 | 5147 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.988% | 0.988% | 0.010 s | 6.748 MB | 8.297 MB | 12.320 MB | 13.000 MB | n/a MB | n/a MB |
| python3 | 5149 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.223 MB | 6.223 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5150 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.266 MB | 6.266 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5151 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.938 MB | 6.938 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5152 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.199 MB | 7.199 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5153 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.074 MB | 7.074 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5154 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.805 MB | 6.805 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5155 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.812 MB | 6.812 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 5156 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.258 MB | 7.258 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5157 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.199 MB | 7.199 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5158 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 1.972% | 1.972% | 0.020 s | 8.197 MB | 9.125 MB | 12.473 MB | 13.160 MB | n/a MB | n/a MB |
| python3 | 5160 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.975% | 6.960% | 0.120 s | 13.493 MB | 20.398 MB | 18.585 MB | 25.633 MB | n/a MB | n/a MB |
| sh | 5159 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 5198 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.957 MB | 0.957 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 5196 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.758 MB | 2.758 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 5212 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 5214 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 161.957 MB | 161.957 MB | 899.047 MB | 899.047 MB | n/a MB | n/a MB |
| python3 | 5232 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.516 MB | 10.516 MB | 14.992 MB | 14.992 MB | n/a MB | n/a MB |
| sh | 5231 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 5235 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.353 MB | 2.859 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 5237 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 130.601% | 143.804% | 3.950 s | 2789.370 MB | 3778.844 MB | 3667.684 MB | 5282.871 MB | n/a MB | n/a MB |
| sh | 5242 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.324 MB | 1.324 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5243 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.574 MB | 20.574 MB | 26.996 MB | 26.996 MB | n/a MB | n/a MB |
| python3 | 5258 | sandbox_agent_lsb-claude_code_0000_0000 | 18 | 167.824% | 175.597% | 28.920 s | 1950.719 MB | 2058.254 MB | 2680.397 MB | 3249.504 MB | n/a MB | n/a MB |
| bash | 5256 | sandbox_agent_lsb-claude_code_0000_0000 | 18 | 0.000% | 0.000% | 0.000 s | 2.816 MB | 2.816 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 5308 | sandbox_agent_lsb-claude_code_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.676 MB | 2.676 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 5310 | sandbox_agent_lsb-claude_code_0000_0000 | 11 | 162.444% | 177.870% | 16.450 s | 531.929 MB | 703.984 MB | 1532.671 MB | 1698.082 MB | n/a MB | n/a MB |
| python3 | 5532 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.855 MB | 9.855 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| sh | 5531 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.336 MB | 1.336 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 5536 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.859 MB | 2.859 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 5538 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1970.965 MB | 1970.965 MB | 2702.086 MB | 2702.086 MB | n/a MB | n/a MB |
| bash | 5618 | sandbox_agent_lsb-claude_code_0000_0000 | 53 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 5620 | sandbox_agent_lsb-claude_code_0000_0000 | 53 | 168.443% | 174.471% | 88.220 s | 2176.767 MB | 2354.062 MB | 2728.665 MB | 2948.141 MB | n/a MB | n/a MB |
| bash | 5658 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.746 MB | 2.746 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 5660 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 158.602% | 173.489% | 14.370 s | 3907.639 MB | 4598.309 MB | 4217.311 MB | 5127.113 MB | n/a MB | n/a MB |
| python3 | 5730 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.250 MB | 21.250 MB | 26.996 MB | 26.996 MB | n/a MB | n/a MB |
| sh | 5729 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.336 MB | 1.336 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 5739 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.336 MB | 1.336 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5740 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.684 MB | 4.684 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| bash | 5742 | sandbox_agent_lsb-claude_code_0000_0000 | 81 | 0.000% | 0.000% | 0.000 s | 2.590 MB | 2.766 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 5744 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 158.187% | 173.349% | 14.350 s | 4256.246 MB | 4861.371 MB | 4702.847 MB | 5693.996 MB | n/a MB | n/a MB |
| python3 | 5749 | sandbox_agent_lsb-claude_code_0000_0000 | 71 | 150.785% | 182.127% | 107.010 s | 5124.718 MB | 7926.957 MB | 5824.943 MB | 8339.582 MB | n/a MB | n/a MB |
| python3 | 5756 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.070 MB | 10.070 MB | 14.992 MB | 14.992 MB | n/a MB | n/a MB |
| sh | 5755 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.371 MB | 1.371 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| claude | 5766 | sandbox_agent_lsb-claude_code_0000_0000 | 67 | 0.000% | 0.000% | 0.000 s | 6.682 MB | 269.004 MB | 86.005 MB | 5499.879 MB | n/a MB | n/a MB |
| python3 | 5768 | sandbox_agent_lsb-claude_code_0000_0000 | 66 | 159.386% | 174.336% | 104.920 s | 2128.409 MB | 2406.543 MB | 2669.619 MB | 3092.465 MB | n/a MB | n/a MB |
| python3 | 5873 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.691 MB | 8.691 MB | 13.250 MB | 13.250 MB | n/a MB | n/a MB |
| tail | 5860 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.055 MB | 1.055 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 5858 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.711 MB | 2.711 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 5859 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 2.434% | 2.931% | 0.050 s | 12.176 MB | 12.176 MB | 15.801 MB | 15.801 MB | n/a MB | n/a MB |
| python3 | 5940 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.188 MB | 8.188 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5977 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 5957 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 2.886% | 2.931% | 0.060 s | 12.068 MB | 12.109 MB | 15.793 MB | 15.793 MB | n/a MB | n/a MB |
| tail | 5958 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.086 MB | 1.086 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python3 | 6012 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.242 MB | 8.242 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 6047 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.973 MB | 6.973 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 6175 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.246 MB | 20.246 MB | 25.246 MB | 25.246 MB | n/a MB | n/a MB |
| sh | 6174 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6203 | sandbox_agent_lsb-claude_code_0000_0000 | 30 | 0.000% | 0.000% | 0.000 s | 2.926 MB | 2.926 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6206 | sandbox_agent_lsb-claude_code_0000_0000 | 30 | 169.703% | 174.900% | 49.570 s | 2462.601 MB | 2727.031 MB | 2684.229 MB | 2948.551 MB | n/a MB | n/a MB |
| python3 | 6225 | sandbox_agent_lsb-claude_code_0000_0000 | 17 | 166.116% | 177.968% | 26.780 s | 370.458 MB | 464.223 MB | 1022.911 MB | 1115.246 MB | n/a MB | n/a MB |
| bash | 6223 | sandbox_agent_lsb-claude_code_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 2.836 MB | 2.836 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6230 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.629 MB | 6.629 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 6229 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.246 MB | 1.246 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6343 | sandbox_agent_lsb-claude_code_0000_0000 | 145 | 0.000% | 0.000% | 0.000 s | 2.945 MB | 2.945 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6346 | sandbox_agent_lsb-claude_code_0000_0000 | 145 | 171.253% | 177.038% | 248.450 s | 2150.261 MB | 2315.984 MB | 2373.361 MB | 2703.555 MB | n/a MB | n/a MB |
| python3 | 6419 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 4.474% | 4.971% | 0.090 s | 13.646 MB | 18.488 MB | 18.849 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 6418 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.469 MB | 1.469 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6447 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.984 MB | 2.984 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 6449 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 162.409% | 175.377% | 11.460 s | 642.875 MB | 868.488 MB | 1400.998 MB | 1630.281 MB | n/a MB | n/a MB |
| claude | 6474 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 6.473 MB | 6.473 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| bash | 6470 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 6473 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.758 MB | 1.758 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6472 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 171.869% | 171.869% | 1.730 s | 478.010 MB | 725.902 MB | 1479.059 MB | 1484.527 MB | n/a MB | n/a MB |
| bash | 6487 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.730 MB | 2.730 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 6489 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.691 MB | 1.691 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| claude | 6493 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 6.410 MB | 6.410 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| bash | 6490 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| cut | 6491 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 6488 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 160.316% | 174.333% | 3.240 s | 273.225 MB | 718.738 MB | 665.073 MB | 1477.395 MB | n/a MB | n/a MB |
| claude | 6492 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 6.855 MB | 6.855 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| sh | 6605 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.250 MB | 1.250 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6606 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.227 MB | 5.227 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| python3 | 6620 | sandbox_agent_lsb-claude_code_0000_0000 | 80 | 169.303% | 177.445% | 134.750 s | 2212.757 MB | 2245.410 MB | 2435.321 MB | 2467.309 MB | n/a MB | n/a MB |
| bash | 6618 | sandbox_agent_lsb-claude_code_0000_0000 | 80 | 0.000% | 0.000% | 0.000 s | 2.777 MB | 2.777 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6632 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.313% | 3.977% | 0.100 s | 12.797 MB | 18.512 MB | 17.655 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 6631 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 6635 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.414 MB | 1.414 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6637 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.965% | 4.967% | 0.120 s | 13.688 MB | 20.398 MB | 18.507 MB | 25.246 MB | n/a MB | n/a MB |
| python3 | 6642 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.651% | 2.983% | 0.080 s | 12.271 MB | 18.102 MB | 17.348 MB | 24.098 MB | n/a MB | n/a MB |
| sh | 6641 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6644 | sandbox_agent_lsb-claude_code_0000_0000 | 21 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.930 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6646 | sandbox_agent_lsb-claude_code_0000_0000 | 21 | 64.489% | 173.056% | 13.040 s | 2155.489 MB | 7654.312 MB | 2788.913 MB | 8088.027 MB | n/a MB | n/a MB |
| sh | 6775 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6776 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.078 MB | 21.078 MB | 26.906 MB | 26.906 MB | n/a MB | n/a MB |
| sh | 6786 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.285 MB | 1.285 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6787 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.402 MB | 20.402 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| python3 | 6790 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 118.743% | 173.054% | 10.760 s | 1436.384 MB | 2056.152 MB | 1802.512 MB | 2277.027 MB | n/a MB | n/a MB |
| bash | 6788 | sandbox_agent_lsb-claude_code_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 2.766 MB | 2.766 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6794 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 138.253% | 172.500% | 6.990 s | 393.378 MB | 507.094 MB | 1758.624 MB | 1855.434 MB | n/a MB | n/a MB |
| sh | 6807 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6808 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.457 MB | 20.457 MB | 25.246 MB | 25.246 MB | n/a MB | n/a MB |
| cut | 6814 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 6811 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.938 MB | 2.938 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6813 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 154.087% | 163.027% | 10.860 s | 495.959 MB | 738.414 MB | 1600.976 MB | 1745.391 MB | n/a MB | n/a MB |
| bash | 6829 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.684 MB | 2.684 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6830 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.453 MB | 23.453 MB | 215.684 MB | 215.684 MB | n/a MB | n/a MB |
| bash | 6941 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.805 MB | 2.805 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| head | 6946 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.418 MB | 0.418 MB | n/a MB | n/a MB |
| bash | 6945 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.172 MB | 1.172 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 6954 | sandbox_agent_lsb-claude_code_0000_0000 | 63 | 0.000% | 0.000% | 0.000 s | 2.711 MB | 2.711 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 6957 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.469 MB | 1.469 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6956 | sandbox_agent_lsb-claude_code_0000_0000 | 63 | 154.830% | 174.975% | 96.710 s | 2156.270 MB | 2292.105 MB | 2478.546 MB | 3187.066 MB | n/a MB | n/a MB |
| python3 | 6958 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.406 MB | 20.406 MB | 25.504 MB | 25.504 MB | n/a MB | n/a MB |
| sh | 6966 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6967 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 7.920% | 7.920% | 0.080 s | 11.736 MB | 18.016 MB | 17.805 MB | 24.098 MB | n/a MB | n/a MB |
| python3 | 6969 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 43.365% | 97.389% | 3.490 s | 68.227 MB | 163.562 MB | 468.750 MB | 1238.043 MB | n/a MB | n/a MB |
| bash | 6968 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.715 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 6974 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.398 MB | 1.398 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6975 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 6.448% | 8.921% | 0.130 s | 15.480 MB | 21.441 MB | 20.310 MB | 26.910 MB | n/a MB | n/a MB |
| python3 | 6982 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 6.888% | 10.802% | 0.140 s | 14.361 MB | 21.293 MB | 19.573 MB | 26.906 MB | n/a MB | n/a MB |
| sh | 6981 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6983 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.766 MB | 2.766 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6984 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 42.593% | 87.518% | 2.570 s | 56.076 MB | 116.016 MB | 415.005 MB | 837.422 MB | n/a MB | n/a MB |
| sh | 6988 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6989 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 5.842% | 5.842% | 0.060 s | 13.713 MB | 18.008 MB | 18.820 MB | 24.148 MB | n/a MB | n/a MB |
| bash | 7001 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.941 MB | 2.941 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7003 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 165.164% | 173.700% | 3.330 s | 130.577 MB | 159.754 MB | 353.193 MB | 379.078 MB | n/a MB | n/a MB |
| sh | 7045 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7046 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.508 MB | 21.508 MB | 26.902 MB | 26.902 MB | n/a MB | n/a MB |
| bash | 7132 | sandbox_agent_lsb-claude_code_0000_0000 | 80 | 0.000% | 0.000% | 0.000 s | 2.969 MB | 2.969 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 7134 | sandbox_agent_lsb-claude_code_0000_0000 | 80 | 168.026% | 182.765% | 134.510 s | 2230.076 MB | 2628.148 MB | 2534.276 MB | 2905.105 MB | n/a MB | n/a MB |
| python3 | 7145 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 2.969% | 2.969% | 0.030 s | 14.840 MB | 15.598 MB | 20.303 MB | 20.770 MB | n/a MB | n/a MB |
| sh | 7144 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 7146 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.801 MB | 2.801 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| claude | 7149 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.488 MB | 5.488 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| python3 | 7150 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.754 MB | 8.754 MB | 13.176 MB | 13.176 MB | n/a MB | n/a MB |
| cut | 7151 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.105 MB | 1.105 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 7153 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 3.977% | 3.977% | 0.040 s | 12.250 MB | 15.582 MB | 16.936 MB | 20.461 MB | n/a MB | n/a MB |
| sh | 7152 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.555 MB | 1.555 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7180 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7181 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 3.480% | 3.976% | 0.070 s | 13.493 MB | 17.941 MB | 19.013 MB | 24.098 MB | n/a MB | n/a MB |
| sh | 7201 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7202 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.646% | 5.967% | 0.110 s | 13.758 MB | 20.855 MB | 18.640 MB | 25.633 MB | n/a MB | n/a MB |
| python3 | 7220 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.379 MB | 5.379 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| sh | 7219 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7227 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7228 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.934 MB | 8.934 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| sort | 7248 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.297 MB | 1.297 MB | 14.641 MB | 14.641 MB | n/a MB | n/a MB |
| head | 7251 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.180 MB | 1.180 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| sort | 7250 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.211 MB | 1.211 MB | 14.641 MB | 14.641 MB | n/a MB | n/a MB |
| claude | 7252 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.227 MB | 7.227 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| bash | 7247 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.664 MB | 1.664 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| uniq | 7249 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.117 MB | 1.117 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 7246 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.664 MB | 2.664 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 7282 | sandbox_agent_lsb-claude_code_0000_0000 | 110 | 27.147% | 175.523% | 29.830 s | 363.634 MB | 2419.633 MB | 411.304 MB | 2672.020 MB | n/a MB | n/a MB |
| bash | 7280 | sandbox_agent_lsb-claude_code_0000_0000 | 110 | 0.000% | 0.000% | 0.000 s | 2.930 MB | 2.930 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 7283 | sandbox_agent_lsb-claude_code_0000_0000 | 92 | 169.660% | 176.179% | 155.660 s | 2196.294 MB | 2322.145 MB | 2420.328 MB | 2740.930 MB | n/a MB | n/a MB |
| sh | 7293 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.305 MB | 1.305 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7294 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 2.485% | 2.983% | 0.050 s | 11.197 MB | 15.172 MB | 16.185 MB | 20.426 MB | n/a MB | n/a MB |
| python3 | 7299 | sandbox_agent_lsb-claude_code_0000_0000 | 29 | 0.319% | 2.982% | 0.090 s | 11.581 MB | 11.848 MB | 15.513 MB | 15.727 MB | n/a MB | n/a MB |
| bash | 7297 | sandbox_agent_lsb-claude_code_0000_0000 | 29 | 0.000% | 0.000% | 0.000 s | 2.656 MB | 2.656 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7303 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.230 MB | 6.230 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 7304 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.676 MB | 6.676 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 7305 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.074 MB | 7.074 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 7306 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.254 MB | 7.254 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 7307 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.176 MB | 7.176 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7308 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.637 MB | 7.637 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 7309 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.891 MB | 7.891 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 7310 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.852 MB | 7.852 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 7311 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.875 MB | 7.875 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 7312 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.590 MB | 7.590 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7313 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.941 MB | 7.941 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7314 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.109 MB | 8.109 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7315 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.105 MB | 8.105 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7316 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.395 MB | 8.395 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7317 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.484 MB | 8.484 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7318 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.547 MB | 8.547 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7320 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.711 MB | 6.711 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 7321 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.051 MB | 7.051 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 7322 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.086 MB | 7.086 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 7324 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.340 MB | 7.340 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 7325 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.445 MB | 7.445 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7326 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.582 MB | 7.582 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7327 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.336 MB | 7.336 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7328 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.582 MB | 7.582 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7329 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.984 MB | 7.984 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7331 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.650% | 3.977% | 0.080 s | 12.548 MB | 18.145 MB | 17.414 MB | 24.098 MB | n/a MB | n/a MB |
| sh | 7330 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.391 MB | 1.391 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7338 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.286% | 3.977% | 0.100 s | 12.863 MB | 18.453 MB | 17.987 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 7337 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.391 MB | 1.391 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7343 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.367 MB | 1.367 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7344 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.109 MB | 7.109 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 7374 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.469 MB | 1.469 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7375 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.562 MB | 7.562 MB | 11.926 MB | 11.926 MB | n/a MB | n/a MB |
| bash | 7421 | sandbox_agent_lsb-claude_code_0000_0000 | 99 | 0.000% | 0.000% | 0.000 s | 2.801 MB | 2.801 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7423 | sandbox_agent_lsb-claude_code_0000_0000 | 78 | 166.884% | 176.905% | 129.510 s | 2191.889 MB | 2242.934 MB | 2419.925 MB | 2735.930 MB | n/a MB | n/a MB |
| python3 | 7425 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.113 MB | 20.113 MB | 25.117 MB | 25.117 MB | n/a MB | n/a MB |
| sh | 7424 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 7422 | sandbox_agent_lsb-claude_code_0000_0000 | 99 | 34.401% | 175.363% | 33.960 s | 455.347 MB | 2324.973 MB | 509.643 MB | 2624.879 MB | n/a MB | n/a MB |
| sh | 7432 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.398 MB | 1.398 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7433 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.910 MB | 9.910 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| sh | 7434 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.391 MB | 1.391 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7435 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.250 MB | 20.250 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| python3 | 7439 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 4.308% | 6.960% | 0.130 s | 13.719 MB | 20.363 MB | 18.914 MB | 25.633 MB | n/a MB | n/a MB |
| sh | 7438 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7441 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.982% | 3.977% | 0.090 s | 12.494 MB | 18.309 MB | 17.419 MB | 24.254 MB | n/a MB | n/a MB |
| sh | 7440 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.422 MB | 1.422 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7444 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.311% | 4.970% | 0.100 s | 13.522 MB | 20.297 MB | 18.333 MB | 24.988 MB | n/a MB | n/a MB |
| sh | 7443 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.305 MB | 1.305 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7449 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.391 MB | 1.391 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7450 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.982% | 3.977% | 0.090 s | 12.352 MB | 18.137 MB | 17.393 MB | 24.148 MB | n/a MB | n/a MB |
| bash | 7452 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.805 MB | 2.805 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7453 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.992 MB | 7.992 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| python3 | 7455 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.969% | 3.962% | 0.090 s | 12.321 MB | 18.102 MB | 17.360 MB | 24.148 MB | n/a MB | n/a MB |
| sh | 7454 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7460 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.387 MB | 1.387 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7461 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.972% | 3.966% | 0.090 s | 12.321 MB | 18.062 MB | 17.419 MB | 24.254 MB | n/a MB | n/a MB |
| sh | 7466 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 4.308% | 6.959% | 0.130 s | 11.474 MB | 20.309 MB | 15.514 MB | 25.504 MB | n/a MB | n/a MB |
| sh | 7465 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7468 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.968% | 3.961% | 0.090 s | 12.352 MB | 18.137 MB | 17.380 MB | 24.098 MB | n/a MB | n/a MB |
| sh | 7467 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.488 MB | 1.488 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7470 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7471 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 3.479% | 6.960% | 0.140 s | 13.157 MB | 21.281 MB | 18.513 MB | 26.992 MB | n/a MB | n/a MB |
| sh | 7472 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7473 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 2.980% | 2.980% | 0.030 s | 8.631 MB | 9.797 MB | 12.795 MB | 13.664 MB | n/a MB | n/a MB |
| bash | 7492 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7494 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 161.104% | 174.970% | 11.340 s | 1661.688 MB | 2028.031 MB | 1898.941 MB | 2249.074 MB | n/a MB | n/a MB |
| sh | 7549 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7548 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7551 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.305 MB | 1.305 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7550 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.305 MB | 1.305 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| cut | 7570 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 7569 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 161.227% | 174.616% | 14.640 s | 2000.257 MB | 2215.109 MB | 2247.065 MB | 2438.215 MB | n/a MB | n/a MB |
| bash | 7567 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.941 MB | 2.941 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7589 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.004 MB | 10.004 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| sh | 7588 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.387 MB | 1.387 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 7614 | sandbox_agent_lsb-claude_code_0000_0000 | 31 | 0.000% | 0.000% | 0.000 s | 2.953 MB | 2.953 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| cut | 7617 | sandbox_agent_lsb-claude_code_0000_0000 | 31 | 0.000% | 0.000% | 0.000 s | 1.086 MB | 1.086 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 7616 | sandbox_agent_lsb-claude_code_0000_0000 | 31 | 168.460% | 175.206% | 50.920 s | 2024.319 MB | 2175.625 MB | 2474.849 MB | 2854.180 MB | n/a MB | n/a MB |
| python3 | 7624 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.379 MB | 19.379 MB | 24.859 MB | 24.859 MB | n/a MB | n/a MB |
| sh | 7623 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7632 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7633 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.660 MB | 18.660 MB | 24.609 MB | 24.609 MB | n/a MB | n/a MB |
| bash | 7635 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.953 MB | 2.953 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| cut | 7638 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 7637 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 162.183% | 170.051% | 9.800 s | 1439.223 MB | 1733.480 MB | 1765.714 MB | 2702.250 MB | n/a MB | n/a MB |
| sh | 7642 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7643 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.781 MB | 21.781 MB | 26.926 MB | 26.926 MB | n/a MB | n/a MB |
| cut | 7656 | sandbox_agent_lsb-claude_code_0000_0000 | 24 | 0.000% | 0.000% | 0.000 s | 1.125 MB | 1.125 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 7655 | sandbox_agent_lsb-claude_code_0000_0000 | 24 | 168.213% | 176.238% | 39.000 s | 2045.736 MB | 2361.797 MB | 2400.109 MB | 3038.191 MB | n/a MB | n/a MB |
| bash | 7653 | sandbox_agent_lsb-claude_code_0000_0000 | 24 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| cut | 7689 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 7687 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.949 MB | 2.949 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7688 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 159.299% | 171.990% | 11.220 s | 1718.779 MB | 2027.309 MB | 1990.870 MB | 2250.453 MB | n/a MB | n/a MB |
| cut | 7708 | sandbox_agent_lsb-claude_code_0000_0000 | 20 | 0.000% | 0.000% | 0.000 s | 1.086 MB | 1.086 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 7707 | sandbox_agent_lsb-claude_code_0000_0000 | 20 | 167.417% | 179.200% | 32.100 s | 1899.454 MB | 2026.016 MB | 2144.912 MB | 2249.008 MB | n/a MB | n/a MB |
| bash | 7705 | sandbox_agent_lsb-claude_code_0000_0000 | 20 | 0.000% | 0.000% | 0.000 s | 2.855 MB | 2.855 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 7712 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7713 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.215 MB | 13.215 MB | 19.836 MB | 19.836 MB | n/a MB | n/a MB |
| python3 | 7724 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 165.199% | 172.077% | 9.970 s | 131.935 MB | 189.098 MB | 319.650 MB | 407.102 MB | n/a MB | n/a MB |
| bash | 7722 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.848 MB | 2.848 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7776 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.852 MB | 20.852 MB | 25.762 MB | 25.762 MB | n/a MB | n/a MB |
| sh | 7775 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.422 MB | 1.422 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| docker | 7794 |  | 1 | n/a% | n/a% | n/a s | 2.637 MB | 2.637 MB | 69.043 MB | 69.043 MB | n/a MB | n/a MB |
| docker | 7811 |  | 25 | 0.000% | 0.000% | 0.000 s | 29.090 MB | 29.090 MB | 1699.199 MB | 1699.199 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.058% | 100.000% | 11954.933 MB | 12980.000 MB | 28.835 W | 73.228 W | 121127.365 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-claude_code_0000_0000 | 92.443% | 218.809% | 3878.819 s | 2076.036 MB | 8271.016 MB | 3730.761719 MB | 1990.699219 MB | 8.505226 MB | 0.056931 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2937 | 4201.477 | interrupted |
| harness:retire | -1 | 1.561 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 4196.007 | n/a | n/a | 3730.762 | 4196007.033 | 4196007.033 | 4196007.033 |
| engine:execute | 1/1 | 0 | 0 | 4196.005 | 4.123 | 4191.677 | 3730.762 | 4196005.423 | 4196005.423 | 4196005.423 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 4166.179 | 0.004 | 4166.174 | 3730.469 | 4166178.577 | 4166178.577 | 4166178.577 |
| harness:await_cli | 1/1 | 0 | 0 | 4162.070 | n/a | n/a | 3728.528 | 4162069.669 | 4162069.669 | 4162069.669 |
| llm:attempt | 123/123 | 0 | 0 | 2774.516 | 7.329 | 2767.126 | 135.424 | 22557.040 | 15139.452 | 66679.676 |
| tool:Bash | 95/95 | 3 | 0 | 1049.186 | n/a | n/a | 3506.813 | 11044.063 | 925.391 | 57873.910 |
| tool:mcp__agency__generate | 15/15 | 0 | 0 | 88.283 | n/a | n/a | 6.457 | 5885.528 | 5466.168 | 12004.662 |
| tool:mcp__agency__token_stats | 3/3 | 0 | 0 | 72.705 | n/a | n/a | 0.149 | 24235.016 | 31587.586 | 39060.735 |
| tool:mcp__agency__trace | 15/15 | 0 | 0 | 48.104 | n/a | n/a | 0.690 | 3206.907 | 3145.637 | 7736.535 |
| run:container_call | 13/13 | 0 | 0 | 26.463 | 0.003 | 26.461 | 0.180 | 2035.646 | 53.529 | 10253.841 |
| teardown:commit | 1/1 | 0 | 0 | 26.049 | 0.005 | 26.044 | 0.180 | 26048.685 | 26048.685 | 26048.685 |
| sandbox:commit | 1/1 | 0 | 0 | 25.692 | 0.003 | 25.689 | 0.180 | 25691.570 | 25691.570 | 25691.570 |
| checkpoint.total | 1/1 | 0 | 0 | 25.691 | 0.003 | 25.689 | 0.180 | 25691.424 | 25691.424 | 25691.424 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 25.691 | 0.003 | 25.689 | 0.180 | 25691.274 | 25691.274 | 25691.274 |
| syscall:execve | 1770/1770 | 0 | 0 | 5.283 | n/a | n/a | 8.206 | 2.985 | 1.316 | 6.072 |
| syscall:sendto | 999/999 | 0 | 0 | 3.386 | n/a | n/a | 3.087 | 3.389 | 2.191 | 6.711 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.095 | 0.711 | 2.383 | 0.000 | 3094.591 | 3094.591 | 3094.591 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.094 | 0.711 | 2.383 | 0.000 | 3094.297 | 3094.297 | 3094.297 |
| syscall:connect | 391/391 | 0 | 0 | 1.735 | n/a | n/a | 1.569 | 4.437 | 2.308 | 8.467 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.614 | n/a | n/a | 0.221 | 1613.822 | 1613.822 | 1613.822 |
| tool:mcp__agency__attention | 2/2 | 0 | 0 | 0.908 | n/a | n/a | 0.061 | 454.075 | 454.075 | 519.018 |
| tool:mcp__agency__attribution | 2/2 | 0 | 0 | 0.807 | n/a | n/a | 0.000 | 403.345 | 403.345 | 454.564 |
| harness:submit | 1/1 | 0 | 0 | 0.608 | n/a | n/a | 0.099 | 607.739 | 607.739 | 607.739 |
| tool:ToolSearch | 1/1 | 0 | 0 | 0.417 | n/a | n/a | 0.529 | 416.915 | 416.915 | 416.915 |
| sandbox:stop | 1/1 | 0 | 0 | 0.357 | 0.002 | 0.355 | 0.000 | 356.846 | 356.846 | 356.846 |
| sandbox:start | 1/1 | 0 | 0 | 0.347 | 0.002 | 0.344 | 0.000 | 346.883 | 346.883 | 346.883 |
| runtime.container_create | 1/1 | 0 | 0 | 0.347 | 0.002 | 0.344 | 0.000 | 346.733 | 346.733 | 346.733 |
| sandbox:create | 1/1 | 0 | 0 | 0.346 | 0.255 | 0.092 | 0.000 | 346.191 | 346.191 | 346.191 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.339 | n/a | n/a | 0.000 | 338.600 | 338.600 | 338.600 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.224 | n/a | n/a | 0.029 | 223.539 | 223.539 | 223.539 |
| agency:services_close | 1/1 | 0 | 0 | 0.196 | 0.001 | 0.196 | 0.104 | 196.499 | 196.499 | 196.499 |
| agency:services_start | 1/1 | 0 | 0 | 0.070 | 0.040 | 0.030 | 0.000 | 70.491 | 70.491 | 70.491 |
| run:detect | 1/1 | 0 | 0 | 0.051 | 0.001 | 0.051 | 0.000 | 51.257 | 51.257 | 51.257 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.007 | 0.042 | 0.000 | 49.397 | 49.397 | 49.397 |
| harness:launch | 1/1 | 0 | 0 | 0.044 | n/a | n/a | 0.000 | 44.448 | 44.448 | 44.448 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.005 | 0.005 | 0.000 | 0.003 | 5.452 | 5.452 | 5.452 |
| harness:snapshot | 1/1 | 0 | 0 | 0.004 | n/a | n/a | 0.022 | 4.459 | 4.459 | 4.459 |
| syscall:bind | 2/2 | 0 | 0 | 0.003 | n/a | n/a | 0.000 | 1.430 | 1.430 | 1.703 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.396 | 1.396 | 1.396 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.076 | 0.078 | 0.100 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.214 | 0.214 | 0.214 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.062 | 0.062 | 0.062 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 4167 | 0.276 | 0.027 | 42.820 | 0.051 | 12.927411 CPU seconds | n/a |
| GPU 0 memory | MB | 4168 | 11954.933 | 11670.000 | 12980.000 | 11962.000 | n/a | n/a |
| GPU 0 power | W | 4168 | 28.835 | 27.100 | 73.228 | 27.626 | n/a | 121127.365 J |
| GPU 0 proc / 2662-99866 / sandbox / ~ / device / GPU-3e5f09dc-e903-190c-c9ae-db86a7268e05 memory | MB | 4168 | 3214.505 | 3118.000 | 4232.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 2662-99866 / sandbox / ~ / device / GPU-3e5f09dc-e903-190c-c9ae-db86a7268e05 estimated power | W | 3504 | 1.188 | 0.000 | 73.204 | 0.000 | n/a | n/a |
| GPU 0 proc / 2662-99866 / sandbox / ~ / device / GPU-3e5f09dc-e903-190c-c9ae-db86a7268e05 utilization | percent | 3504 | 0.782 | 0.000 | 89.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2776-101639 / sandbox / ~ / device / GPU-3e5f09dc-e903-190c-c9ae-db86a7268e05 memory | MB | 4168 | 8258.428 | 8070.000 | 8266.000 | 8266.000 | n/a | n/a |
| GPU 0 proc / 2776-101639 / sandbox / ~ / device / GPU-3e5f09dc-e903-190c-c9ae-db86a7268e05 estimated power | W | 605 | 6.675 | 0.000 | 73.228 | 0.000 | n/a | n/a |
| GPU 0 proc / 2776-101639 / sandbox / ~ / device / GPU-3e5f09dc-e903-190c-c9ae-db86a7268e05 utilization | percent | 605 | 8.721 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 4168 | 11472.933 | 11188.000 | 12498.000 | 11480.000 | n/a | n/a |
| GPU 0 utilization | percent | 4168 | 2.058 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 4168 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 4167 | 20.260 | 0.071 | 96.622 | 0.230 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 4167 | 24.798 | 0.000 | 67.958 | 0.000 | n/a | n/a |
| host disk_read_mb_s | MB/s | 4167 | 1.461 | 0.000 | 211.177 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 4167 | 1.711 | 0.000 | 235.478 | 0.023 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 4167 | 0.691 | 0.000 | 94.319 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 4167 | 0.826 | 0.000 | 94.873 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 4168 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 4168 | 8445.289 | 6780.387 | 15327.562 | 7756.684 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 4167 | 0.086 | 0.000 | 86.404 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 4167 | 0.088 | 0.000 | 88.501 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 4167 | 0.003 | 0.000 | 8.690 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 4167 | 0.008 | 0.000 | 0.454 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1698) CPU | percent | 4167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1698) io read MB/s | MB/s | 4167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1698) io write MB/s | MB/s | 4167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1698) rss_mb | MB | 4168 | 2.678 | 2.164 | 3.414 | 2.164 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1698) main thread run-queue wait | percent | 4167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1698) vms_mb | MB | 4168 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2662) CPU | percent | 4167 | 4.742 | 0.000 | 176.074 | 0.000 | 200.490000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2662) io read MB/s | MB/s | 4167 | 0.058 | 0.000 | 46.799 | 0.000 | 318.218750 MB | n/a |
| Agency harness — python -m lsbench (PID 2662) io write MB/s | MB/s | 4167 | 1.215 | 0.000 | 573.535 | 0.000 | 5100.261719 MB | n/a |
| Agency harness — python -m lsbench (PID 2662) rss_mb | MB | 4168 | 3195.811 | 2553.402 | 4624.148 | 3477.832 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2662) main thread run-queue wait | percent | 4167 | 0.001 | 0.000 | 1.386 | 0.000 | 0.047825 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2662) vms_mb | MB | 4168 | 16468.178 | 14051.867 | 18585.648 | 16803.523 | n/a | n/a |
| Python — vllm (PID 2667) CPU | percent | 4167 | 0.174 | 0.000 | 17.405 | 0.000 | 8.050000 CPU seconds | n/a |
| Python — vllm (PID 2667) io read MB/s | MB/s | 4167 | 0.007 | 0.000 | 12.644 | 0.000 | 73.593750 MB | n/a |
| Python — vllm (PID 2667) io write MB/s | MB/s | 4167 | 0.000 | 0.000 | 0.008 | 0.000 | 0.074219 MB | n/a |
| Python — vllm (PID 2667) rss_mb | MB | 4168 | 1610.266 | 1407.410 | 1803.953 | 1416.859 | n/a | n/a |
| Python — vllm (PID 2667) main thread run-queue wait | percent | 4167 | 0.015 | 0.000 | 3.806 | 0.000 | 0.768422 run-queue seconds | n/a |
| Python — vllm (PID 2667) vms_mb | MB | 4168 | 11042.694 | 10971.566 | 11044.586 | 11044.586 | n/a | n/a |
| Python — python -c (PID 2775) CPU | percent | 4167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2775) io read MB/s | MB/s | 4167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2775) io write MB/s | MB/s | 4167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2775) rss_mb | MB | 4168 | 9.675 | 7.922 | 12.188 | 7.922 | n/a | n/a |
| Python — python -c (PID 2775) main thread run-queue wait | percent | 4167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2775) vms_mb | MB | 4168 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2776) CPU | percent | 4167 | 1.732 | 0.000 | 110.689 | 0.996 | 77.270000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2776) io read MB/s | MB/s | 4167 | 0.040 | 0.000 | 47.815 | 0.000 | 330.917969 MB | n/a |
| VLLM::EngineCore (PID 2776) io write MB/s | MB/s | 4167 | 0.000 | 0.000 | 0.004 | 0.000 | 0.027344 MB | n/a |
| VLLM::EngineCore (PID 2776) rss_mb | MB | 4168 | 2086.443 | 1821.367 | 2320.238 | 1858.828 | n/a | n/a |
| VLLM::EngineCore (PID 2776) main thread run-queue wait | percent | 4167 | 0.021 | 0.000 | 9.951 | 0.000 | 0.903026 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2776) vms_mb | MB | 4168 | 21204.363 | 21204.363 | 21204.363 | 21204.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 3048) CPU | percent | 4161 | 0.003 | 0.000 | 2.818 | 0.000 | 0.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 3048) rss_mb | MB | 4162 | 0.350 | 0.074 | 0.551 | 0.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 3048) main thread run-queue wait | percent | 4161 | 0.015 | 0.000 | 5.363 | 0.000 | 0.655890 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 3048) vms_mb | MB | 4162 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 3079) CPU | percent | 4161 | 0.004 | 0.000 | 5.233 | 0.000 | 0.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 3079) rss_mb | MB | 4162 | 0.702 | 0.035 | 1.426 | 0.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 3079) main thread run-queue wait | percent | 4161 | 0.017 | 0.000 | 5.757 | 0.000 | 0.760175 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 3079) vms_mb | MB | 4162 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3171) CPU | percent | 4161 | 29.946 | 0.000 | 108.443 | 0.000 | 1255.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3171) rss_mb | MB | 4162 | 100.782 | 2.949 | 108.949 | 106.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3171) main thread run-queue wait | percent | 4161 | 0.000 | 0.000 | 0.011 | 0.000 | 0.000200 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3171) vms_mb | MB | 4162 | 973.196 | 4.262 | 978.234 | 974.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3177) CPU | percent | 1 | 99.911 | 99.911 | 99.911 | 99.911 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3177) rss_mb | MB | 2 | 53.967 | 25.801 | 82.133 | 82.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3177) main thread run-queue wait | percent | 1 | 0.017 | 0.017 | 0.017 | 0.017 | 0.000171 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3177) vms_mb | MB | 2 | 65.354 | 34.035 | 96.672 | 96.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 3190) CPU | percent | 4130 | 3.129 | 0.000 | 69.474 | 0.994 | 130.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 3190) rss_mb | MB | 4131 | 292.125 | 55.789 | 344.441 | 307.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 3190) main thread run-queue wait | percent | 4130 | 15.133 | 0.001 | 86.245 | 0.014 | 630.620524 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 3190) vms_mb | MB | 4131 | 5499.871 | 5484.289 | 5499.879 | 5499.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3238) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3238) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3240) rss_mb | MB | 1 | 9.465 | 9.465 | 9.465 | 9.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3240) vms_mb | MB | 1 | 13.617 | 13.617 | 13.617 | 13.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3272) rss_mb | MB | 1 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3272) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — free (PID 3277) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — free (PID 3277) vms_mb | MB | 1 | 0.156 | 0.156 | 0.156 | 0.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 3278) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 3278) vms_mb | MB | 1 | 0.418 | 0.418 | 0.418 | 0.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3296) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3296) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3297) rss_mb | MB | 1 | 16.637 | 16.637 | 16.637 | 16.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3297) vms_mb | MB | 1 | 22.066 | 22.066 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3301) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3301) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3302) rss_mb | MB | 1 | 9.906 | 9.906 | 9.906 | 9.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3302) vms_mb | MB | 1 | 13.617 | 13.617 | 13.617 | 13.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3342) rss_mb | MB | 1 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3342) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — run_eval.py (PID 3344) rss_mb | MB | 1 | 12.121 | 12.121 | 12.121 | 12.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — run_eval.py (PID 3344) vms_mb | MB | 1 | 15.809 | 15.809 | 15.809 | 15.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp7m24ptte.py (PID 3366) rss_mb | MB | 1 | 8.656 | 8.656 | 8.656 | 8.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp7m24ptte.py (PID 3366) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3385) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3385) rss_mb | MB | 2 | 2.957 | 2.957 | 2.957 | 2.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3385) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3385) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3387) CPU | percent | 1 | 3.969 | 3.969 | 3.969 | 3.969 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3387) rss_mb | MB | 2 | 12.477 | 12.477 | 12.477 | 12.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3387) main thread run-queue wait | percent | 1 | 0.014 | 0.014 | 0.014 | 0.014 | 0.000145 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3387) vms_mb | MB | 2 | 15.980 | 15.980 | 15.980 | 15.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3409) rss_mb | MB | 1 | 12.477 | 12.477 | 12.477 | 12.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3409) vms_mb | MB | 1 | 15.980 | 15.980 | 15.980 | 15.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmplq8lc2z6.py (PID 3446) rss_mb | MB | 1 | 8.363 | 8.363 | 8.363 | 8.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmplq8lc2z6.py (PID 3446) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3484) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3484) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3764) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3764) rss_mb | MB | 5 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3764) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3764) vms_mb | MB | 5 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3765) CPU | percent | 4 | 7.192 | 1.962 | 11.906 | 7.940 | 0.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3765) rss_mb | MB | 5 | 12.780 | 12.332 | 13.438 | 13.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3765) main thread run-queue wait | percent | 4 | 0.084 | 0.011 | 0.156 | 0.108 | 0.003380 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3765) vms_mb | MB | 5 | 16.495 | 15.754 | 17.527 | 17.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpllctcr1d.py (PID 3784) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpllctcr1d.py (PID 3784) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpq1pgeyft.py (PID 3820) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpq1pgeyft.py (PID 3820) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpklr8xfo_.py (PID 3841) rss_mb | MB | 1 | 9.457 | 9.457 | 9.457 | 9.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpklr8xfo_.py (PID 3841) vms_mb | MB | 1 | 13.246 | 13.246 | 13.246 | 13.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpahapy817.py (PID 3843) rss_mb | MB | 1 | 7.738 | 7.738 | 7.738 | 7.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpahapy817.py (PID 3843) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpgsgxp8q7.py (PID 3856) rss_mb | MB | 1 | 7.352 | 7.352 | 7.352 | 7.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpgsgxp8q7.py (PID 3856) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3900) rss_mb | MB | 1 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3900) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3901) rss_mb | MB | 1 | 20.398 | 20.398 | 20.398 | 20.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3901) vms_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3928) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3928) rss_mb | MB | 3 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3928) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3928) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3929) CPU | percent | 2 | 2.978 | 1.984 | 3.971 | 3.971 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3929) rss_mb | MB | 3 | 12.500 | 12.500 | 12.500 | 12.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3929) main thread run-queue wait | percent | 2 | 0.015 | 0.013 | 0.018 | 0.013 | 0.000305 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 3929) vms_mb | MB | 3 | 15.918 | 15.918 | 15.918 | 15.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmprjkrhcn_.py (PID 3930) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmprjkrhcn_.py (PID 3930) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppxuj2028.py (PID 3968) rss_mb | MB | 1 | 6.672 | 6.672 | 6.672 | 6.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppxuj2028.py (PID 3968) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp6fw0css1.py (PID 4002) rss_mb | MB | 1 | 6.984 | 6.984 | 6.984 | 6.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp6fw0css1.py (PID 4002) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4048) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4048) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4049) rss_mb | MB | 1 | 10.605 | 10.605 | 10.605 | 10.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4049) vms_mb | MB | 1 | 15.230 | 15.230 | 15.230 | 15.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4067) rss_mb | MB | 1 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4067) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4068) rss_mb | MB | 1 | 21.512 | 21.512 | 21.512 | 21.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4068) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4161) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4161) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4162) rss_mb | MB | 1 | 15.336 | 15.336 | 15.336 | 15.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4162) vms_mb | MB | 1 | 20.426 | 20.426 | 20.426 | 20.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4235) rss_mb | MB | 1 | 1.285 | 1.285 | 1.285 | 1.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4235) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4236) rss_mb | MB | 1 | 21.219 | 21.219 | 21.219 | 21.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4236) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4250) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4250) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4251) rss_mb | MB | 1 | 9.441 | 9.441 | 9.441 | 9.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4251) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4291) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4291) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4292) rss_mb | MB | 1 | 5.660 | 5.660 | 5.660 | 5.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4292) vms_mb | MB | 1 | 11.645 | 11.645 | 11.645 | 11.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4335) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4335) rss_mb | MB | 2 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4335) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4335) vms_mb | MB | 2 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4337) CPU | percent | 1 | 145.828 | 145.828 | 145.828 | 145.828 | 1.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4337) rss_mb | MB | 2 | 269.154 | 21.680 | 516.629 | 516.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4337) main thread run-queue wait | percent | 1 | 34.216 | 34.216 | 34.216 | 34.216 | 0.344908 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4337) vms_mb | MB | 2 | 515.723 | 213.812 | 817.633 | 817.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4341) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4341) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4342) rss_mb | MB | 1 | 18.016 | 18.016 | 18.016 | 18.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4342) vms_mb | MB | 1 | 24.098 | 24.098 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4350) CPU | percent | 339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4350) rss_mb | MB | 340 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4350) main thread run-queue wait | percent | 339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4350) vms_mb | MB | 340 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4351) CPU | percent | 339 | 104.749 | 80.484 | 126.313 | 109.375 | 357.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4351) rss_mb | MB | 340 | 2066.431 | 8.727 | 3019.371 | 3019.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4351) main thread run-queue wait | percent | 339 | 3.065 | 0.001 | 21.398 | 0.006 | 10.457092 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4351) vms_mb | MB | 340 | 3220.773 | 13.227 | 3243.488 | 3243.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4391) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4391) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4392) rss_mb | MB | 1 | 15.438 | 15.438 | 15.438 | 15.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4392) vms_mb | MB | 1 | 20.324 | 20.324 | 20.324 | 20.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4414) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4414) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4434) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4434) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4435) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4435) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4444) rss_mb | MB | 1 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4444) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ps (PID 4448) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ps (PID 4448) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4449) rss_mb | MB | 1 | 1.730 | 1.730 | 1.730 | 1.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4449) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 4450) rss_mb | MB | 1 | 6.645 | 6.645 | 6.645 | 6.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 4450) vms_mb | MB | 1 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4465) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4465) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4466) rss_mb | MB | 1 | 8.883 | 8.883 | 8.883 | 8.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4466) vms_mb | MB | 1 | 13.410 | 13.410 | 13.410 | 13.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4496) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4496) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4497) rss_mb | MB | 1 | 16.328 | 16.328 | 16.328 | 16.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4497) vms_mb | MB | 1 | 21.770 | 21.770 | 21.770 | 21.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4534) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4534) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4535) rss_mb | MB | 1 | 20.754 | 20.754 | 20.754 | 20.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4535) vms_mb | MB | 1 | 25.758 | 25.758 | 25.758 | 25.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4619) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4619) rss_mb | MB | 6 | 3.016 | 3.016 | 3.016 | 3.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4619) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4619) vms_mb | MB | 6 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — prep.py (PID 4621) CPU | percent | 1 | 66.494 | 66.494 | 66.494 | 66.494 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — prep.py (PID 4621) rss_mb | MB | 2 | 204.289 | 58.703 | 349.875 | 58.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — prep.py (PID 4621) main thread run-queue wait | percent | 1 | 0.079 | 0.079 | 0.079 | 0.079 | 0.000793 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — prep.py (PID 4621) vms_mb | MB | 2 | 458.531 | 250.938 | 666.125 | 250.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — eofa.py (PID 4627) CPU | percent | 3 | 149.142 | 113.341 | 168.975 | 168.975 | 4.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — eofa.py (PID 4627) rss_mb | MB | 4 | 1911.892 | 1561.004 | 2029.477 | 2029.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — eofa.py (PID 4627) main thread run-queue wait | percent | 3 | 45.827 | 2.600 | 67.959 | 66.921 | 1.382668 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — eofa.py (PID 4627) vms_mb | MB | 4 | 2459.800 | 2379.059 | 2702.023 | 2379.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4631) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4631) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4632) rss_mb | MB | 1 | 8.027 | 8.027 | 8.027 | 8.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4632) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4756) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4756) rss_mb | MB | 3 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4756) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4756) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 4758) CPU | percent | 2 | 2.480 | 1.984 | 2.976 | 1.984 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 4758) rss_mb | MB | 3 | 12.352 | 12.352 | 12.352 | 12.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 4758) main thread run-queue wait | percent | 2 | 0.009 | 0.007 | 0.010 | 0.007 | 0.000173 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 4758) vms_mb | MB | 3 | 15.801 | 15.801 | 15.801 | 15.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 4759) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 4759) rss_mb | MB | 3 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 4759) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 4759) vms_mb | MB | 3 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpaexruf5l.py (PID 4767) rss_mb | MB | 1 | 7.902 | 7.902 | 7.902 | 7.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpaexruf5l.py (PID 4767) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpd7prygzo.py (PID 4804) rss_mb | MB | 1 | 7.590 | 7.590 | 7.590 | 7.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpd7prygzo.py (PID 4804) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpea_mcyhr.py (PID 4841) rss_mb | MB | 1 | 7.680 | 7.680 | 7.680 | 7.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpea_mcyhr.py (PID 4841) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4871) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4871) rss_mb | MB | 13 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4871) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4871) vms_mb | MB | 13 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — eofb.py (PID 4873) CPU | percent | 9 | 158.910 | 87.260 | 175.101 | 175.101 | 14.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — eofb.py (PID 4873) rss_mb | MB | 10 | 1779.222 | 13.473 | 2402.113 | 1104.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — eofb.py (PID 4873) main thread run-queue wait | percent | 9 | 60.160 | 6.847 | 75.907 | 73.476 | 5.471677 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — eofb.py (PID 4873) vms_mb | MB | 10 | 2178.768 | 207.262 | 2702.016 | 2340.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 4877) CPU | percent | 2 | 2.963 | 1.958 | 3.968 | 3.968 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 4877) rss_mb | MB | 3 | 12.414 | 12.414 | 12.414 | 12.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 4877) main thread run-queue wait | percent | 2 | 0.012 | 0.008 | 0.016 | 0.008 | 0.000245 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 4877) vms_mb | MB | 3 | 15.793 | 15.793 | 15.793 | 15.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — awk (PID 4878) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — awk (PID 4878) rss_mb | MB | 3 | 1.629 | 1.629 | 1.629 | 1.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — awk (PID 4878) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — awk (PID 4878) vms_mb | MB | 3 | 3.504 | 3.504 | 3.504 | 3.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tr (PID 4879) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tr (PID 4879) rss_mb | MB | 3 | 1.113 | 1.113 | 1.113 | 1.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tr (PID 4879) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tr (PID 4879) vms_mb | MB | 3 | 2.465 | 2.465 | 2.465 | 2.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpuvze9sc2.py (PID 4906) rss_mb | MB | 1 | 8.008 | 8.008 | 8.008 | 8.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpuvze9sc2.py (PID 4906) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp89pus4nw.py (PID 4938) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp89pus4nw.py (PID 4938) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4987) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4987) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4988) rss_mb | MB | 1 | 19.812 | 19.812 | 19.812 | 19.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4988) vms_mb | MB | 1 | 24.859 | 24.859 | 24.859 | 24.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4990) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4990) rss_mb | MB | 12 | 2.988 | 2.988 | 2.988 | 2.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4990) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4990) vms_mb | MB | 12 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det.py (PID 4992) CPU | percent | 11 | 170.225 | 153.849 | 175.652 | 165.755 | 18.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det.py (PID 4992) rss_mb | MB | 12 | 830.619 | 786.523 | 887.305 | 811.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det.py (PID 4992) main thread run-queue wait | percent | 11 | 51.678 | 43.408 | 60.755 | 50.059 | 5.728742 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det.py (PID 4992) vms_mb | MB | 12 | 1527.746 | 1478.398 | 1577.094 | 1577.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5006) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5006) rss_mb | MB | 6 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5006) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5006) vms_mb | MB | 6 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det2.py (PID 5008) CPU | percent | 5 | 163.666 | 141.078 | 174.074 | 170.026 | 8.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det2.py (PID 5008) rss_mb | MB | 6 | 593.297 | 8.645 | 778.102 | 582.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det2.py (PID 5008) main thread run-queue wait | percent | 5 | 50.453 | 42.352 | 58.265 | 52.085 | 2.537031 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — det2.py (PID 5008) vms_mb | MB | 6 | 1359.376 | 13.281 | 1688.020 | 1491.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5022) CPU | percent | 186 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5022) rss_mb | MB | 187 | 2.739 | 0.000 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5022) main thread run-queue wait | percent | 186 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5022) vms_mb | MB | 187 | 3.964 | 1.617 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps.py (PID 5024) CPU | percent | 185 | 170.521 | 146.445 | 177.515 | 172.115 | 318.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps.py (PID 5024) rss_mb | MB | 186 | 2586.002 | 1982.012 | 2867.129 | 2727.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps.py (PID 5024) main thread run-queue wait | percent | 185 | 61.330 | 44.073 | 78.599 | 51.563 | 114.470934 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps.py (PID 5024) vms_mb | MB | 186 | 2873.418 | 2506.578 | 3136.867 | 2948.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5035) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5035) rss_mb | MB | 3 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5035) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5035) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5036) CPU | percent | 2 | 2.982 | 2.982 | 2.982 | 2.982 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5036) rss_mb | MB | 3 | 13.178 | 7.863 | 16.977 | 16.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5036) main thread run-queue wait | percent | 2 | 39.388 | 35.441 | 43.335 | 35.441 | 0.792470 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5036) vms_mb | MB | 3 | 18.336 | 12.926 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5038) CPU | percent | 115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5038) rss_mb | MB | 116 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5038) main thread run-queue wait | percent | 115 | 0.002 | 0.000 | 0.263 | 0.000 | 0.002652 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5038) vms_mb | MB | 116 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5039) CPU | percent | 113 | 0.227 | 0.000 | 1.988 | 0.000 | 0.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5039) rss_mb | MB | 114 | 12.315 | 7.355 | 12.758 | 12.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5039) main thread run-queue wait | percent | 113 | 12.066 | 0.011 | 60.785 | 0.130 | 13.774022 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5039) vms_mb | MB | 114 | 15.812 | 11.922 | 16.156 | 16.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — awk (PID 5040) CPU | percent | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — awk (PID 5040) rss_mb | MB | 114 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — awk (PID 5040) main thread run-queue wait | percent | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — awk (PID 5040) vms_mb | MB | 114 | 3.504 | 3.504 | 3.504 | 3.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tr (PID 5041) CPU | percent | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tr (PID 5041) rss_mb | MB | 114 | 1.113 | 1.113 | 1.113 | 1.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tr (PID 5041) main thread run-queue wait | percent | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tr (PID 5041) vms_mb | MB | 114 | 2.465 | 2.465 | 2.465 | 2.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmprzwb7hq0.py (PID 5042) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmprzwb7hq0.py (PID 5042) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwx4jkvs9.py (PID 5043) rss_mb | MB | 1 | 4.355 | 4.355 | 4.355 | 4.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwx4jkvs9.py (PID 5043) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5044) rss_mb | MB | 1 | 12.133 | 12.133 | 12.133 | 12.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5044) vms_mb | MB | 1 | 15.758 | 15.758 | 15.758 | 15.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppgiuczq0.py (PID 5045) rss_mb | MB | 1 | 4.395 | 4.395 | 4.395 | 4.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppgiuczq0.py (PID 5045) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvahhhob7.py (PID 5046) rss_mb | MB | 1 | 6.949 | 6.949 | 6.949 | 6.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvahhhob7.py (PID 5046) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1dwy2zoe.py (PID 5047) rss_mb | MB | 1 | 7.137 | 7.137 | 7.137 | 7.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1dwy2zoe.py (PID 5047) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpsxa7ic54.py (PID 5048) rss_mb | MB | 1 | 7.590 | 7.590 | 7.590 | 7.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpsxa7ic54.py (PID 5048) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp685_n_72.py (PID 5049) rss_mb | MB | 1 | 7.652 | 7.652 | 7.652 | 7.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp685_n_72.py (PID 5049) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvxu592yp.py (PID 5050) rss_mb | MB | 1 | 7.816 | 7.816 | 7.816 | 7.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvxu592yp.py (PID 5050) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmptaykpls3.py (PID 5051) rss_mb | MB | 1 | 7.852 | 7.852 | 7.852 | 7.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmptaykpls3.py (PID 5051) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpf7hwn0h5.py (PID 5052) rss_mb | MB | 1 | 7.574 | 7.574 | 7.574 | 7.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpf7hwn0h5.py (PID 5052) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp3vf3kcog.py (PID 5053) rss_mb | MB | 1 | 7.895 | 7.895 | 7.895 | 7.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp3vf3kcog.py (PID 5053) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpu7pu88b3.py (PID 5054) rss_mb | MB | 1 | 8.004 | 8.004 | 8.004 | 8.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpu7pu88b3.py (PID 5054) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpa0m_ucac.py (PID 5055) rss_mb | MB | 1 | 8.172 | 8.172 | 8.172 | 8.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpa0m_ucac.py (PID 5055) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5059) rss_mb | MB | 1 | 12.258 | 12.258 | 12.258 | 12.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5059) vms_mb | MB | 1 | 15.758 | 15.758 | 15.758 | 15.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpz00m2cvy.py (PID 5061) rss_mb | MB | 1 | 7.699 | 7.699 | 7.699 | 7.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpz00m2cvy.py (PID 5061) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpewu5_i14.py (PID 5063) rss_mb | MB | 1 | 7.371 | 7.371 | 7.371 | 7.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpewu5_i14.py (PID 5063) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpc9uewjru.py (PID 5064) rss_mb | MB | 1 | 6.820 | 6.820 | 6.820 | 6.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpc9uewjru.py (PID 5064) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpfc2av7f3.py (PID 5065) rss_mb | MB | 1 | 6.703 | 6.703 | 6.703 | 6.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpfc2av7f3.py (PID 5065) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpo48ob28x.py (PID 5066) rss_mb | MB | 1 | 8.039 | 8.039 | 8.039 | 8.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpo48ob28x.py (PID 5066) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpghn3nicc.py (PID 5067) rss_mb | MB | 1 | 8.105 | 8.105 | 8.105 | 8.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpghn3nicc.py (PID 5067) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp8k64vhct.py (PID 5070) rss_mb | MB | 1 | 6.824 | 6.824 | 6.824 | 6.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp8k64vhct.py (PID 5070) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpyy86wrya.py (PID 5071) rss_mb | MB | 1 | 7.152 | 7.152 | 7.152 | 7.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpyy86wrya.py (PID 5071) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpdp61pzo1.py (PID 5072) rss_mb | MB | 1 | 7.301 | 7.301 | 7.301 | 7.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpdp61pzo1.py (PID 5072) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmplru7ywu_.py (PID 5073) rss_mb | MB | 1 | 7.352 | 7.352 | 7.352 | 7.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmplru7ywu_.py (PID 5073) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmplj8okg8t.py (PID 5074) rss_mb | MB | 1 | 4.387 | 4.387 | 4.387 | 4.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmplj8okg8t.py (PID 5074) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5075) rss_mb | MB | 1 | 12.258 | 12.258 | 12.258 | 12.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5075) vms_mb | MB | 1 | 15.758 | 15.758 | 15.758 | 15.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpa4kpd2rl.py (PID 5076) rss_mb | MB | 1 | 7.383 | 7.383 | 7.383 | 7.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpa4kpd2rl.py (PID 5076) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpksdoct12.py (PID 5077) rss_mb | MB | 1 | 7.891 | 7.891 | 7.891 | 7.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpksdoct12.py (PID 5077) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1dkreb7l.py (PID 5078) rss_mb | MB | 1 | 8.219 | 8.219 | 8.219 | 8.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1dkreb7l.py (PID 5078) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpcyqzvx2v.py (PID 5095) rss_mb | MB | 1 | 8.047 | 8.047 | 8.047 | 8.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpcyqzvx2v.py (PID 5095) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp4rydv4fx.py (PID 5096) rss_mb | MB | 1 | 8.355 | 8.355 | 8.355 | 8.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp4rydv4fx.py (PID 5096) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0f5wu29d.py (PID 5101) rss_mb | MB | 1 | 7.496 | 7.496 | 7.496 | 7.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0f5wu29d.py (PID 5101) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpnbx_c61y.py (PID 5102) rss_mb | MB | 1 | 7.953 | 7.953 | 7.953 | 7.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpnbx_c61y.py (PID 5102) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpzbyks1dx.py (PID 5104) rss_mb | MB | 1 | 7.199 | 7.199 | 7.199 | 7.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpzbyks1dx.py (PID 5104) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpd261gm6q.py (PID 5105) rss_mb | MB | 1 | 6.676 | 6.676 | 6.676 | 6.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpd261gm6q.py (PID 5105) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwmoyoru8.py (PID 5106) rss_mb | MB | 1 | 7.742 | 7.742 | 7.742 | 7.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwmoyoru8.py (PID 5106) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp42xrq1ek.py (PID 5108) rss_mb | MB | 1 | 7.199 | 7.199 | 7.199 | 7.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp42xrq1ek.py (PID 5108) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp83mhqjiz.py (PID 5110) rss_mb | MB | 1 | 7.051 | 7.051 | 7.051 | 7.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp83mhqjiz.py (PID 5110) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpqnknk2ak.py (PID 5111) rss_mb | MB | 1 | 7.008 | 7.008 | 7.008 | 7.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpqnknk2ak.py (PID 5111) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpbmyiccjt.py (PID 5112) rss_mb | MB | 1 | 7.199 | 7.199 | 7.199 | 7.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpbmyiccjt.py (PID 5112) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp6kuyl_91.py (PID 5113) rss_mb | MB | 1 | 7.387 | 7.387 | 7.387 | 7.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp6kuyl_91.py (PID 5113) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmprx03x5iu.py (PID 5114) rss_mb | MB | 1 | 7.637 | 7.637 | 7.637 | 7.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmprx03x5iu.py (PID 5114) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpk03x3l20.py (PID 5115) rss_mb | MB | 1 | 7.824 | 7.824 | 7.824 | 7.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpk03x3l20.py (PID 5115) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpb2nnun2e.py (PID 5117) rss_mb | MB | 1 | 7.027 | 7.027 | 7.027 | 7.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpb2nnun2e.py (PID 5117) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvph_joy_.py (PID 5118) rss_mb | MB | 1 | 7.172 | 7.172 | 7.172 | 7.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvph_joy_.py (PID 5118) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmps03awyys.py (PID 5119) rss_mb | MB | 1 | 7.383 | 7.383 | 7.383 | 7.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmps03awyys.py (PID 5119) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwtyv9pfi.py (PID 5120) rss_mb | MB | 1 | 7.438 | 7.438 | 7.438 | 7.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwtyv9pfi.py (PID 5120) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpcxmbvkeg.py (PID 5121) rss_mb | MB | 1 | 7.852 | 7.852 | 7.852 | 7.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpcxmbvkeg.py (PID 5121) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmps4eas8db.py (PID 5122) rss_mb | MB | 1 | 8.020 | 8.020 | 8.020 | 8.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmps4eas8db.py (PID 5122) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpzw66jtc8.py (PID 5123) rss_mb | MB | 1 | 8.215 | 8.215 | 8.215 | 8.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpzw66jtc8.py (PID 5123) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpsatl0c1v.py (PID 5124) rss_mb | MB | 1 | 8.125 | 8.125 | 8.125 | 8.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpsatl0c1v.py (PID 5124) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpfnb0s6oa.py (PID 5127) rss_mb | MB | 1 | 4.375 | 4.375 | 4.375 | 4.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpfnb0s6oa.py (PID 5127) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpjc7qby4b.py (PID 5128) rss_mb | MB | 1 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpjc7qby4b.py (PID 5128) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5129) rss_mb | MB | 1 | 12.258 | 12.258 | 12.258 | 12.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5129) vms_mb | MB | 1 | 15.758 | 15.758 | 15.758 | 15.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvjer289v.py (PID 5130) rss_mb | MB | 1 | 7.367 | 7.367 | 7.367 | 7.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvjer289v.py (PID 5130) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp5j4resjd.py (PID 5131) rss_mb | MB | 1 | 7.438 | 7.438 | 7.438 | 7.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp5j4resjd.py (PID 5131) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpz544q0fq.py (PID 5132) rss_mb | MB | 1 | 7.871 | 7.871 | 7.871 | 7.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpz544q0fq.py (PID 5132) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp6ma6qoxx.py (PID 5133) rss_mb | MB | 1 | 7.867 | 7.867 | 7.867 | 7.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp6ma6qoxx.py (PID 5133) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0sn9rkjy.py (PID 5134) rss_mb | MB | 1 | 7.527 | 7.527 | 7.527 | 7.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0sn9rkjy.py (PID 5134) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppe89_j65.py (PID 5135) rss_mb | MB | 1 | 7.699 | 7.699 | 7.699 | 7.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppe89_j65.py (PID 5135) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvdwkm6v4.py (PID 5136) rss_mb | MB | 1 | 7.891 | 7.891 | 7.891 | 7.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvdwkm6v4.py (PID 5136) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0zg945lg.py (PID 5137) CPU | percent | 9 | 1.211 | 0.000 | 2.973 | 1.987 | 0.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0zg945lg.py (PID 5137) rss_mb | MB | 10 | 9.266 | 8.043 | 9.402 | 9.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0zg945lg.py (PID 5137) main thread run-queue wait | percent | 9 | 50.739 | 34.337 | 57.447 | 45.432 | 4.608541 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0zg945lg.py (PID 5137) vms_mb | MB | 10 | 13.227 | 13.016 | 13.250 | 13.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpn3gfrx3s.py (PID 5138) CPU | percent | 9 | 1.322 | 0.000 | 2.974 | 0.988 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpn3gfrx3s.py (PID 5138) rss_mb | MB | 10 | 9.096 | 7.922 | 9.227 | 9.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpn3gfrx3s.py (PID 5138) main thread run-queue wait | percent | 9 | 53.470 | 42.194 | 63.205 | 47.622 | 4.854246 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpn3gfrx3s.py (PID 5138) vms_mb | MB | 10 | 13.223 | 13.016 | 13.246 | 13.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpugb2mjq2.py (PID 5139) CPU | percent | 9 | 1.099 | 0.000 | 1.987 | 0.954 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpugb2mjq2.py (PID 5139) rss_mb | MB | 10 | 9.204 | 7.980 | 9.340 | 9.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpugb2mjq2.py (PID 5139) main thread run-queue wait | percent | 9 | 51.281 | 39.516 | 68.715 | 68.715 | 4.674074 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpugb2mjq2.py (PID 5139) vms_mb | MB | 10 | 13.223 | 13.016 | 13.246 | 13.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpqeuk18dl.py (PID 5140) rss_mb | MB | 1 | 8.312 | 8.312 | 8.312 | 8.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpqeuk18dl.py (PID 5140) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1bp6iqvl.py (PID 5141) rss_mb | MB | 1 | 8.188 | 8.188 | 8.188 | 8.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1bp6iqvl.py (PID 5141) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpyeeahs8k.py (PID 5142) rss_mb | MB | 1 | 8.469 | 8.469 | 8.469 | 8.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpyeeahs8k.py (PID 5142) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp2pyvr2x5.py (PID 5145) rss_mb | MB | 1 | 5.473 | 5.473 | 5.473 | 5.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp2pyvr2x5.py (PID 5145) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpsc56ck0m.py (PID 5146) rss_mb | MB | 1 | 5.512 | 5.512 | 5.512 | 5.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpsc56ck0m.py (PID 5146) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwwmto51q.py (PID 5147) CPU | percent | 1 | 0.988 | 0.988 | 0.988 | 0.988 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwwmto51q.py (PID 5147) rss_mb | MB | 2 | 6.748 | 5.199 | 8.297 | 8.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwwmto51q.py (PID 5147) main thread run-queue wait | percent | 1 | 56.394 | 56.394 | 56.394 | 56.394 | 0.570777 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpwwmto51q.py (PID 5147) vms_mb | MB | 2 | 12.320 | 11.641 | 13.000 | 13.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpmm2gcphy.py (PID 5149) rss_mb | MB | 1 | 6.223 | 6.223 | 6.223 | 6.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpmm2gcphy.py (PID 5149) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpthf4l2gx.py (PID 5150) rss_mb | MB | 1 | 6.266 | 6.266 | 6.266 | 6.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpthf4l2gx.py (PID 5150) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpjz5qkz29.py (PID 5151) rss_mb | MB | 1 | 6.938 | 6.938 | 6.938 | 6.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpjz5qkz29.py (PID 5151) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp4x_oxa7a.py (PID 5152) rss_mb | MB | 1 | 7.199 | 7.199 | 7.199 | 7.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp4x_oxa7a.py (PID 5152) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpfd399bac.py (PID 5153) rss_mb | MB | 1 | 7.074 | 7.074 | 7.074 | 7.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpfd399bac.py (PID 5153) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp083wbjoq.py (PID 5154) rss_mb | MB | 1 | 6.805 | 6.805 | 6.805 | 6.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp083wbjoq.py (PID 5154) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpinhn61oo.py (PID 5155) rss_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpinhn61oo.py (PID 5155) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpgbx5xfph.py (PID 5156) rss_mb | MB | 1 | 7.258 | 7.258 | 7.258 | 7.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpgbx5xfph.py (PID 5156) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpmic78n4b.py (PID 5157) rss_mb | MB | 1 | 7.199 | 7.199 | 7.199 | 7.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpmic78n4b.py (PID 5157) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 5158) CPU | percent | 1 | 1.972 | 1.972 | 1.972 | 1.972 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 5158) rss_mb | MB | 2 | 8.197 | 7.270 | 9.125 | 9.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 5158) main thread run-queue wait | percent | 1 | 65.149 | 65.149 | 65.149 | 65.149 | 0.660605 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 5158) vms_mb | MB | 2 | 12.473 | 11.785 | 13.160 | 13.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5159) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5159) rss_mb | MB | 4 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5159) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5159) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5160) CPU | percent | 3 | 3.975 | 1.981 | 6.960 | 6.960 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5160) rss_mb | MB | 4 | 13.493 | 7.957 | 20.398 | 20.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5160) main thread run-queue wait | percent | 3 | 54.339 | 41.603 | 66.100 | 66.100 | 1.641589 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5160) vms_mb | MB | 4 | 18.585 | 13.023 | 25.633 | 25.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5196) rss_mb | MB | 1 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5196) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5198) rss_mb | MB | 1 | 0.957 | 0.957 | 0.957 | 0.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5198) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5212) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5212) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr.py (PID 5214) rss_mb | MB | 1 | 161.957 | 161.957 | 161.957 | 161.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr.py (PID 5214) vms_mb | MB | 1 | 899.047 | 899.047 | 899.047 | 899.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5231) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5231) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5232) rss_mb | MB | 1 | 10.516 | 10.516 | 10.516 | 10.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5232) vms_mb | MB | 1 | 14.992 | 14.992 | 14.992 | 14.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5235) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5235) rss_mb | MB | 4 | 2.353 | 0.832 | 2.859 | 0.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5235) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5235) vms_mb | MB | 4 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir.py (PID 5237) CPU | percent | 3 | 130.601 | 115.851 | 143.804 | 115.851 | 3.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir.py (PID 5237) rss_mb | MB | 4 | 2789.370 | 1556.969 | 3778.844 | 3778.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir.py (PID 5237) main thread run-queue wait | percent | 3 | 26.070 | 3.561 | 46.746 | 3.561 | 0.788149 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir.py (PID 5237) vms_mb | MB | 4 | 3667.684 | 2372.863 | 5282.871 | 5282.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5242) rss_mb | MB | 1 | 1.324 | 1.324 | 1.324 | 1.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5242) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5243) rss_mb | MB | 1 | 20.574 | 20.574 | 20.574 | 20.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5243) vms_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5256) CPU | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5256) rss_mb | MB | 18 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5256) main thread run-queue wait | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5256) vms_mb | MB | 18 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capmargin.py (PID 5258) CPU | percent | 17 | 167.824 | 116.378 | 175.597 | 170.316 | 28.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capmargin.py (PID 5258) rss_mb | MB | 18 | 1950.719 | 158.125 | 2058.254 | 2058.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capmargin.py (PID 5258) main thread run-queue wait | percent | 17 | 58.578 | 5.402 | 76.846 | 60.295 | 10.090716 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capmargin.py (PID 5258) vms_mb | MB | 18 | 2680.397 | 763.699 | 3249.504 | 2674.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5308) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5308) rss_mb | MB | 11 | 2.676 | 2.676 | 2.676 | 2.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5308) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5308) vms_mb | MB | 11 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — namedet.py (PID 5310) CPU | percent | 10 | 162.444 | 134.524 | 177.870 | 177.870 | 16.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — namedet.py (PID 5310) rss_mb | MB | 11 | 531.929 | 60.418 | 703.984 | 628.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — namedet.py (PID 5310) main thread run-queue wait | percent | 10 | 47.331 | 26.200 | 56.877 | 48.921 | 4.790983 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — namedet.py (PID 5310) vms_mb | MB | 11 | 1532.671 | 314.031 | 1698.082 | 1698.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5531) rss_mb | MB | 1 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5531) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5532) rss_mb | MB | 1 | 9.855 | 9.855 | 9.855 | 9.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5532) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5536) rss_mb | MB | 1 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5536) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capthr.py (PID 5538) rss_mb | MB | 1 | 1970.965 | 1970.965 | 1970.965 | 1970.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capthr.py (PID 5538) vms_mb | MB | 1 | 2702.086 | 2702.086 | 2702.086 | 2702.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5618) CPU | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5618) rss_mb | MB | 53 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5618) main thread run-queue wait | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5618) vms_mb | MB | 53 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit.py (PID 5620) CPU | percent | 52 | 168.443 | 147.164 | 174.471 | 169.337 | 88.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit.py (PID 5620) rss_mb | MB | 53 | 2176.767 | 1119.977 | 2354.062 | 2179.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit.py (PID 5620) main thread run-queue wait | percent | 52 | 61.541 | 48.265 | 78.228 | 60.017 | 32.229875 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit.py (PID 5620) vms_mb | MB | 53 | 2728.665 | 2217.055 | 2948.141 | 2449.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5658) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5658) rss_mb | MB | 10 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5658) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5658) vms_mb | MB | 10 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir2.py (PID 5660) CPU | percent | 9 | 158.602 | 100.375 | 173.489 | 172.285 | 14.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir2.py (PID 5660) rss_mb | MB | 10 | 3907.639 | 442.113 | 4598.309 | 4400.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir2.py (PID 5660) main thread run-queue wait | percent | 9 | 45.215 | 0.006 | 64.984 | 59.019 | 4.097371 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir2.py (PID 5660) vms_mb | MB | 10 | 4217.311 | 762.102 | 5127.113 | 4685.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5729) rss_mb | MB | 1 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5729) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5730) rss_mb | MB | 1 | 21.250 | 21.250 | 21.250 | 21.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5730) vms_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5739) rss_mb | MB | 1 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5739) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5740) rss_mb | MB | 1 | 4.684 | 4.684 | 4.684 | 4.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5740) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5742) CPU | percent | 80 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5742) rss_mb | MB | 81 | 2.590 | 0.504 | 2.766 | 0.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5742) main thread run-queue wait | percent | 80 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5742) vms_mb | MB | 81 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir3.py (PID 5744) CPU | percent | 9 | 158.187 | 98.267 | 173.349 | 165.527 | 14.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir3.py (PID 5744) rss_mb | MB | 10 | 4256.246 | 1797.148 | 4861.371 | 3810.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir3.py (PID 5744) main thread run-queue wait | percent | 9 | 41.614 | 0.007 | 56.087 | 50.901 | 3.775735 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir3.py (PID 5744) vms_mb | MB | 10 | 4702.847 | 2702.078 | 5693.996 | 5003.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit2.py (PID 5749) CPU | percent | 70 | 150.785 | 10.594 | 182.127 | 10.594 | 107.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit2.py (PID 5749) rss_mb | MB | 71 | 5124.718 | 0.000 | 7926.957 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit2.py (PID 5749) main thread run-queue wait | percent | 70 | 34.876 | 4.035 | 63.860 | 4.035 | 24.802218 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit2.py (PID 5749) vms_mb | MB | 71 | 5824.943 | 2702.156 | 8339.582 | 8339.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5755) rss_mb | MB | 1 | 1.371 | 1.371 | 1.371 | 1.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5755) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5756) rss_mb | MB | 1 | 10.070 | 10.070 | 10.070 | 10.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5756) vms_mb | MB | 1 | 14.992 | 14.992 | 14.992 | 14.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5766) CPU | percent | 66 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5766) rss_mb | MB | 67 | 6.682 | 2.707 | 269.004 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5766) main thread run-queue wait | percent | 66 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5766) vms_mb | MB | 67 | 86.005 | 3.977 | 5499.879 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit2.py (PID 5768) CPU | percent | 65 | 159.386 | 11.782 | 174.336 | 145.843 | 104.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit2.py (PID 5768) rss_mb | MB | 66 | 2128.409 | 240.051 | 2406.543 | 2193.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit2.py (PID 5768) main thread run-queue wait | percent | 65 | 57.408 | 0.007 | 71.620 | 29.460 | 37.784502 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capcrit2.py (PID 5768) vms_mb | MB | 66 | 2669.619 | 762.168 | 3092.465 | 2462.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5858) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5858) rss_mb | MB | 6 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5858) main thread run-queue wait | percent | 5 | 0.005 | 0.000 | 0.025 | 0.000 | 0.000255 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5858) vms_mb | MB | 6 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5859) CPU | percent | 2 | 2.434 | 1.937 | 2.931 | 2.931 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5859) rss_mb | MB | 3 | 12.176 | 12.176 | 12.176 | 12.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5859) main thread run-queue wait | percent | 2 | 0.098 | 0.013 | 0.184 | 0.184 | 0.002015 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5859) vms_mb | MB | 3 | 15.801 | 15.801 | 15.801 | 15.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5860) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5860) rss_mb | MB | 3 | 1.055 | 1.055 | 1.055 | 1.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5860) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5860) vms_mb | MB | 3 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpofv4vzbv.py (PID 5873) rss_mb | MB | 1 | 8.691 | 8.691 | 8.691 | 8.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpofv4vzbv.py (PID 5873) vms_mb | MB | 1 | 13.250 | 13.250 | 13.250 | 13.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp8pypwj9f.py (PID 5940) rss_mb | MB | 1 | 8.188 | 8.188 | 8.188 | 8.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp8pypwj9f.py (PID 5940) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5957) CPU | percent | 2 | 2.886 | 2.841 | 2.931 | 2.841 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5957) rss_mb | MB | 3 | 12.068 | 11.984 | 12.109 | 12.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5957) main thread run-queue wait | percent | 2 | 0.043 | 0.019 | 0.068 | 0.019 | 0.000890 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — analyze.py (PID 5957) vms_mb | MB | 3 | 15.793 | 15.793 | 15.793 | 15.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5958) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5958) rss_mb | MB | 3 | 1.086 | 1.086 | 1.086 | 1.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5958) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5958) vms_mb | MB | 3 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp62e_dvvm.py (PID 5977) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp62e_dvvm.py (PID 5977) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp7rmjpeio.py (PID 6012) rss_mb | MB | 1 | 8.242 | 8.242 | 8.242 | 8.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp7rmjpeio.py (PID 6012) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmptal1pyqe.py (PID 6047) rss_mb | MB | 1 | 6.973 | 6.973 | 6.973 | 6.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmptal1pyqe.py (PID 6047) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6174) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6174) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6175) rss_mb | MB | 1 | 20.246 | 20.246 | 20.246 | 20.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6175) vms_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6203) CPU | percent | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6203) rss_mb | MB | 30 | 2.926 | 2.926 | 2.926 | 2.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6203) main thread run-queue wait | percent | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6203) vms_mb | MB | 30 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6206) CPU | percent | 29 | 169.703 | 107.131 | 174.900 | 171.036 | 49.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6206) rss_mb | MB | 30 | 2462.601 | 25.340 | 2727.031 | 2726.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6206) main thread run-queue wait | percent | 29 | 51.758 | 1.816 | 73.130 | 50.505 | 15.117066 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6206) vms_mb | MB | 30 | 2684.229 | 217.543 | 2948.551 | 2948.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6223) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6223) rss_mb | MB | 17 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6223) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6223) vms_mb | MB | 17 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc.py (PID 6225) CPU | percent | 16 | 166.116 | 159.112 | 177.968 | 162.095 | 26.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc.py (PID 6225) rss_mb | MB | 17 | 370.458 | 324.965 | 464.223 | 372.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc.py (PID 6225) main thread run-queue wait | percent | 16 | 47.017 | 42.243 | 53.246 | 47.162 | 7.579148 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc.py (PID 6225) vms_mb | MB | 17 | 1022.911 | 1015.867 | 1115.246 | 1017.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6229) rss_mb | MB | 1 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6229) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6230) rss_mb | MB | 1 | 6.629 | 6.629 | 6.629 | 6.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6230) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6343) CPU | percent | 144 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6343) rss_mb | MB | 145 | 2.945 | 2.945 | 2.945 | 2.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6343) main thread run-queue wait | percent | 144 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6343) vms_mb | MB | 145 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6346) CPU | percent | 144 | 171.253 | 85.464 | 177.038 | 172.735 | 248.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6346) rss_mb | MB | 145 | 2150.261 | 13.359 | 2315.984 | 2182.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6346) main thread run-queue wait | percent | 144 | 54.890 | 4.834 | 78.250 | 74.713 | 79.630134 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6346) vms_mb | MB | 145 | 2373.361 | 207.250 | 2703.555 | 2404.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6418) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6418) rss_mb | MB | 3 | 1.469 | 1.469 | 1.469 | 1.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6418) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6418) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6419) CPU | percent | 2 | 4.474 | 3.978 | 4.971 | 3.978 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6419) rss_mb | MB | 3 | 13.646 | 7.660 | 18.488 | 18.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6419) main thread run-queue wait | percent | 2 | 42.885 | 38.042 | 47.729 | 38.042 | 0.862605 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6419) vms_mb | MB | 3 | 18.849 | 11.926 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6447) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6447) rss_mb | MB | 8 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6447) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6447) vms_mb | MB | 8 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc2.py (PID 6449) CPU | percent | 7 | 162.409 | 131.777 | 175.377 | 175.377 | 11.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc2.py (PID 6449) rss_mb | MB | 8 | 642.875 | 13.617 | 868.488 | 672.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc2.py (PID 6449) main thread run-queue wait | percent | 7 | 49.654 | 34.456 | 72.290 | 52.442 | 3.502949 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc2.py (PID 6449) vms_mb | MB | 8 | 1400.998 | 207.520 | 1630.281 | 1434.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6470) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6470) rss_mb | MB | 2 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6470) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6470) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr2.py (PID 6472) CPU | percent | 1 | 171.869 | 171.869 | 171.869 | 171.869 | 1.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr2.py (PID 6472) rss_mb | MB | 2 | 478.010 | 230.117 | 725.902 | 725.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr2.py (PID 6472) main thread run-queue wait | percent | 1 | 39.655 | 39.655 | 39.655 | 39.655 | 0.399157 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr2.py (PID 6472) vms_mb | MB | 2 | 1479.059 | 1473.590 | 1484.527 | 1484.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6473) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6473) rss_mb | MB | 2 | 1.758 | 1.758 | 1.758 | 1.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6473) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6473) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6474) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6474) rss_mb | MB | 2 | 6.473 | 6.473 | 6.473 | 6.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6474) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6474) vms_mb | MB | 2 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6487) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6487) rss_mb | MB | 3 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6487) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6487) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr2.py (PID 6488) CPU | percent | 2 | 160.316 | 146.300 | 174.333 | 174.333 | 3.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr2.py (PID 6488) rss_mb | MB | 3 | 273.225 | 13.168 | 718.738 | 87.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr2.py (PID 6488) main thread run-queue wait | percent | 2 | 44.128 | 33.427 | 54.830 | 54.830 | 0.891696 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — thr2.py (PID 6488) vms_mb | MB | 3 | 665.073 | 207.215 | 1477.395 | 310.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6489) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6489) rss_mb | MB | 3 | 1.691 | 1.691 | 1.691 | 1.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6489) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6489) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6490) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6490) rss_mb | MB | 3 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6490) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6490) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 6491) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 6491) rss_mb | MB | 3 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 6491) main thread run-queue wait | percent | 2 | 0.095 | 0.000 | 0.189 | 0.189 | 0.001910 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 6491) vms_mb | MB | 3 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6492) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6492) rss_mb | MB | 3 | 6.855 | 6.855 | 6.855 | 6.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6492) main thread run-queue wait | percent | 2 | 4.887 | 0.000 | 9.774 | 9.774 | 0.098678 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6492) vms_mb | MB | 3 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6493) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6493) rss_mb | MB | 3 | 6.410 | 6.410 | 6.410 | 6.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6493) main thread run-queue wait | percent | 2 | 4.986 | 0.000 | 9.972 | 9.972 | 0.100670 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6493) vms_mb | MB | 3 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6605) rss_mb | MB | 1 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6605) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6606) rss_mb | MB | 1 | 5.227 | 5.227 | 5.227 | 5.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6606) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6618) CPU | percent | 79 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6618) rss_mb | MB | 80 | 2.777 | 2.777 | 2.777 | 2.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6618) main thread run-queue wait | percent | 79 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6618) vms_mb | MB | 80 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 6620) CPU | percent | 79 | 169.303 | 115.297 | 177.445 | 146.137 | 134.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 6620) rss_mb | MB | 80 | 2212.757 | 127.410 | 2245.410 | 2237.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 6620) main thread run-queue wait | percent | 79 | 52.773 | 9.519 | 76.324 | 74.691 | 42.002433 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 6620) vms_mb | MB | 80 | 2435.321 | 400.918 | 2467.309 | 2459.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6631) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6631) rss_mb | MB | 4 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6631) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6631) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6632) CPU | percent | 3 | 3.313 | 2.980 | 3.977 | 3.977 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6632) rss_mb | MB | 4 | 12.797 | 7.551 | 18.512 | 18.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6632) main thread run-queue wait | percent | 3 | 52.006 | 39.645 | 60.726 | 55.648 | 1.569677 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6632) vms_mb | MB | 4 | 17.655 | 11.926 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6635) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6635) rss_mb | MB | 4 | 1.414 | 1.414 | 1.414 | 1.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6635) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6635) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6637) CPU | percent | 3 | 3.965 | 2.972 | 4.967 | 4.967 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6637) rss_mb | MB | 4 | 13.688 | 8.102 | 20.398 | 20.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6637) main thread run-queue wait | percent | 3 | 60.772 | 60.278 | 61.384 | 60.278 | 1.839566 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6637) vms_mb | MB | 4 | 18.507 | 13.023 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6641) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6641) rss_mb | MB | 4 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6641) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6641) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6642) CPU | percent | 3 | 2.651 | 1.987 | 2.983 | 2.983 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6642) rss_mb | MB | 4 | 12.271 | 6.805 | 18.102 | 18.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6642) main thread run-queue wait | percent | 3 | 51.492 | 45.066 | 59.377 | 59.377 | 1.554121 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6642) vms_mb | MB | 4 | 17.348 | 11.660 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6644) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6644) rss_mb | MB | 21 | 2.715 | 0.555 | 2.930 | 0.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6644) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6644) vms_mb | MB | 21 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — vfence.py (PID 6646) CPU | percent | 20 | 64.489 | 0.994 | 173.056 | 4.025 | 13.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — vfence.py (PID 6646) rss_mb | MB | 21 | 2155.489 | 4.785 | 7654.312 | 1335.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — vfence.py (PID 6646) main thread run-queue wait | percent | 20 | 46.024 | 0.001 | 74.535 | 0.291 | 9.276005 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — vfence.py (PID 6646) vms_mb | MB | 21 | 2788.913 | 10.000 | 8088.027 | 8088.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6775) rss_mb | MB | 1 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6775) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6776) rss_mb | MB | 1 | 21.078 | 21.078 | 21.078 | 21.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6776) vms_mb | MB | 1 | 26.906 | 26.906 | 26.906 | 26.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6786) rss_mb | MB | 1 | 1.285 | 1.285 | 1.285 | 1.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6786) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6787) rss_mb | MB | 1 | 20.402 | 20.402 | 20.402 | 20.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6787) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6788) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6788) rss_mb | MB | 17 | 2.766 | 2.766 | 2.766 | 2.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6788) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6788) vms_mb | MB | 17 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — vfence.py (PID 6790) CPU | percent | 9 | 118.743 | 10.937 | 173.054 | 147.611 | 10.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — vfence.py (PID 6790) rss_mb | MB | 10 | 1436.384 | 173.453 | 2056.152 | 2056.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — vfence.py (PID 6790) main thread run-queue wait | percent | 9 | 41.349 | 0.002 | 74.072 | 70.802 | 3.747469 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — vfence.py (PID 6790) vms_mb | MB | 10 | 1802.512 | 762.008 | 2277.027 | 2277.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc3.py (PID 6794) CPU | percent | 5 | 138.253 | 90.168 | 172.500 | 159.916 | 6.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc3.py (PID 6794) rss_mb | MB | 6 | 393.378 | 236.344 | 507.094 | 446.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc3.py (PID 6794) main thread run-queue wait | percent | 5 | 30.635 | 12.839 | 44.549 | 37.799 | 1.548681 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc3.py (PID 6794) vms_mb | MB | 6 | 1758.624 | 1698.410 | 1855.434 | 1757.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6807) rss_mb | MB | 1 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6807) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6808) rss_mb | MB | 1 | 20.457 | 20.457 | 20.457 | 20.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6808) vms_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6811) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6811) rss_mb | MB | 8 | 2.938 | 2.938 | 2.938 | 2.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6811) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6811) vms_mb | MB | 8 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc4.py (PID 6813) CPU | percent | 7 | 154.087 | 148.924 | 163.027 | 151.760 | 10.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc4.py (PID 6813) rss_mb | MB | 8 | 495.959 | 312.098 | 738.414 | 738.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc4.py (PID 6813) main thread run-queue wait | percent | 7 | 54.413 | 39.844 | 62.511 | 57.069 | 3.835317 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — disc4.py (PID 6813) vms_mb | MB | 8 | 1600.976 | 1553.562 | 1745.391 | 1553.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 6814) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 6814) rss_mb | MB | 8 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 6814) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 6814) vms_mb | MB | 8 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6829) rss_mb | MB | 1 | 2.684 | 2.684 | 2.684 | 2.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6829) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6830) rss_mb | MB | 1 | 23.453 | 23.453 | 23.453 | 23.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6830) vms_mb | MB | 1 | 215.684 | 215.684 | 215.684 | 215.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6941) rss_mb | MB | 1 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6941) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6945) rss_mb | MB | 1 | 1.172 | 1.172 | 1.172 | 1.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6945) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 6946) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 6946) vms_mb | MB | 1 | 0.418 | 0.418 | 0.418 | 0.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6954) CPU | percent | 62 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6954) rss_mb | MB | 63 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6954) main thread run-queue wait | percent | 62 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6954) vms_mb | MB | 63 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capheld.py (PID 6956) CPU | percent | 62 | 154.830 | 74.532 | 174.975 | 172.053 | 96.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capheld.py (PID 6956) rss_mb | MB | 63 | 2156.270 | 20.637 | 2292.105 | 2159.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capheld.py (PID 6956) main thread run-queue wait | percent | 62 | 63.317 | 1.048 | 79.397 | 56.321 | 39.550061 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capheld.py (PID 6956) vms_mb | MB | 63 | 2478.546 | 212.352 | 3187.066 | 2439.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6957) rss_mb | MB | 1 | 1.469 | 1.469 | 1.469 | 1.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6957) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6958) rss_mb | MB | 1 | 20.406 | 20.406 | 20.406 | 20.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6958) vms_mb | MB | 1 | 25.504 | 25.504 | 25.504 | 25.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6966) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6966) rss_mb | MB | 2 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6966) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6966) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6967) CPU | percent | 1 | 7.920 | 7.920 | 7.920 | 7.920 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6967) rss_mb | MB | 2 | 11.736 | 5.457 | 18.016 | 18.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6967) main thread run-queue wait | percent | 1 | 68.886 | 68.886 | 68.886 | 68.886 | 0.695805 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6967) vms_mb | MB | 2 | 17.805 | 11.512 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6968) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6968) rss_mb | MB | 9 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6968) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6968) vms_mb | MB | 9 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6969) CPU | percent | 8 | 43.365 | 3.959 | 97.389 | 97.389 | 3.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6969) rss_mb | MB | 9 | 68.227 | 7.953 | 163.562 | 47.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6969) main thread run-queue wait | percent | 8 | 66.627 | 40.567 | 81.223 | 73.083 | 5.365829 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6969) vms_mb | MB | 9 | 468.750 | 13.020 | 1238.043 | 420.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6974) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6974) rss_mb | MB | 3 | 1.398 | 1.398 | 1.398 | 1.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6974) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6974) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6975) CPU | percent | 2 | 6.448 | 3.975 | 8.921 | 8.921 | 0.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6975) rss_mb | MB | 3 | 15.480 | 9.297 | 21.441 | 21.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6975) main thread run-queue wait | percent | 2 | 49.102 | 44.677 | 53.527 | 44.677 | 0.989337 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6975) vms_mb | MB | 3 | 20.310 | 13.492 | 26.910 | 26.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6981) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6981) rss_mb | MB | 3 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6981) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6981) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6982) CPU | percent | 2 | 6.888 | 2.975 | 10.802 | 10.802 | 0.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6982) rss_mb | MB | 3 | 14.361 | 7.523 | 21.293 | 21.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6982) main thread run-queue wait | percent | 2 | 64.647 | 61.183 | 68.112 | 68.112 | 1.310625 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6982) vms_mb | MB | 3 | 19.573 | 11.926 | 26.906 | 26.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6983) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6983) rss_mb | MB | 7 | 2.766 | 2.766 | 2.766 | 2.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6983) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6983) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6984) CPU | percent | 6 | 42.593 | 1.988 | 87.518 | 69.614 | 2.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6984) rss_mb | MB | 7 | 56.076 | 19.074 | 116.016 | 69.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6984) main thread run-queue wait | percent | 6 | 68.850 | 54.430 | 81.750 | 76.392 | 4.155994 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6984) vms_mb | MB | 7 | 415.005 | 211.621 | 837.422 | 419.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6988) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6988) rss_mb | MB | 2 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6988) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6988) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6989) CPU | percent | 1 | 5.842 | 5.842 | 5.842 | 5.842 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6989) rss_mb | MB | 2 | 13.713 | 9.418 | 18.008 | 18.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6989) main thread run-queue wait | percent | 1 | 81.528 | 81.528 | 81.528 | 81.528 | 0.837400 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6989) vms_mb | MB | 2 | 18.820 | 13.492 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7001) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7001) rss_mb | MB | 3 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7001) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7001) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 7003) CPU | percent | 2 | 165.164 | 156.627 | 173.700 | 156.627 | 3.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 7003) rss_mb | MB | 3 | 130.577 | 83.641 | 159.754 | 83.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 7003) main thread run-queue wait | percent | 2 | 52.272 | 50.797 | 53.747 | 53.747 | 1.053949 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 7003) vms_mb | MB | 3 | 353.193 | 301.422 | 379.078 | 301.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7045) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7045) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7046) rss_mb | MB | 1 | 21.508 | 21.508 | 21.508 | 21.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7046) vms_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7132) CPU | percent | 79 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7132) rss_mb | MB | 80 | 2.969 | 2.969 | 2.969 | 2.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7132) main thread run-queue wait | percent | 79 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7132) vms_mb | MB | 80 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir4.py (PID 7134) CPU | percent | 79 | 168.026 | 98.286 | 182.765 | 142.186 | 134.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir4.py (PID 7134) rss_mb | MB | 80 | 2230.076 | 23.957 | 2628.148 | 2334.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir4.py (PID 7134) main thread run-queue wait | percent | 79 | 52.686 | 0.013 | 75.160 | 35.962 | 42.210923 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — capdir4.py (PID 7134) vms_mb | MB | 80 | 2534.276 | 216.082 | 2905.105 | 2612.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7144) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7144) rss_mb | MB | 2 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7144) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7144) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7145) CPU | percent | 1 | 2.969 | 2.969 | 2.969 | 2.969 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7145) rss_mb | MB | 2 | 14.840 | 14.082 | 15.598 | 15.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7145) main thread run-queue wait | percent | 1 | 61.255 | 61.255 | 61.255 | 61.255 | 0.619022 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7145) vms_mb | MB | 2 | 20.303 | 19.836 | 20.770 | 20.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7146) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7146) rss_mb | MB | 2 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7146) main thread run-queue wait | percent | 1 | 0.246 | 0.246 | 0.246 | 0.246 | 0.002483 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7146) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 7149) rss_mb | MB | 1 | 5.488 | 5.488 | 5.488 | 5.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 7149) vms_mb | MB | 1 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 7150) rss_mb | MB | 1 | 8.754 | 8.754 | 8.754 | 8.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 7150) vms_mb | MB | 1 | 13.176 | 13.176 | 13.176 | 13.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7151) rss_mb | MB | 1 | 1.105 | 1.105 | 1.105 | 1.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7151) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7152) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7152) rss_mb | MB | 2 | 1.555 | 1.555 | 1.555 | 1.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7152) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7152) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7153) CPU | percent | 1 | 3.977 | 3.977 | 3.977 | 3.977 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7153) rss_mb | MB | 2 | 12.250 | 8.918 | 15.582 | 15.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7153) main thread run-queue wait | percent | 1 | 54.249 | 54.249 | 54.249 | 54.249 | 0.545685 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7153) vms_mb | MB | 2 | 16.936 | 13.410 | 20.461 | 20.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7180) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7180) rss_mb | MB | 3 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7180) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7180) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7181) CPU | percent | 2 | 3.480 | 2.984 | 3.976 | 2.984 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7181) rss_mb | MB | 3 | 13.493 | 8.016 | 17.941 | 17.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7181) main thread run-queue wait | percent | 2 | 51.103 | 46.780 | 55.426 | 46.780 | 1.028008 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7181) vms_mb | MB | 3 | 19.013 | 12.926 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7201) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7201) rss_mb | MB | 4 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7201) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7201) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7202) CPU | percent | 3 | 3.646 | 1.987 | 5.967 | 5.967 | 0.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7202) rss_mb | MB | 4 | 13.758 | 7.914 | 20.855 | 20.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7202) main thread run-queue wait | percent | 3 | 61.601 | 59.776 | 64.864 | 59.776 | 1.858914 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7202) vms_mb | MB | 4 | 18.640 | 12.926 | 25.633 | 25.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7219) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7219) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7220) rss_mb | MB | 1 | 5.379 | 5.379 | 5.379 | 5.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7220) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7227) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7227) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7228) rss_mb | MB | 1 | 8.934 | 8.934 | 8.934 | 8.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7228) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7246) rss_mb | MB | 1 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7246) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7247) rss_mb | MB | 1 | 1.664 | 1.664 | 1.664 | 1.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7247) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sort (PID 7248) rss_mb | MB | 1 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sort (PID 7248) vms_mb | MB | 1 | 14.641 | 14.641 | 14.641 | 14.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — uniq (PID 7249) rss_mb | MB | 1 | 1.117 | 1.117 | 1.117 | 1.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — uniq (PID 7249) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sort (PID 7250) rss_mb | MB | 1 | 1.211 | 1.211 | 1.211 | 1.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sort (PID 7250) vms_mb | MB | 1 | 14.641 | 14.641 | 14.641 | 14.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 7251) rss_mb | MB | 1 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 7251) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 7252) rss_mb | MB | 1 | 7.227 | 7.227 | 7.227 | 7.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 7252) vms_mb | MB | 1 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7280) CPU | percent | 109 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7280) rss_mb | MB | 110 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7280) main thread run-queue wait | percent | 109 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7280) vms_mb | MB | 110 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7282) CPU | percent | 109 | 27.147 | 0.000 | 175.523 | 172.085 | 29.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7282) rss_mb | MB | 110 | 363.634 | 1.348 | 2419.633 | 2278.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7282) main thread run-queue wait | percent | 109 | 8.133 | 0.000 | 62.097 | 50.687 | 8.934752 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7282) vms_mb | MB | 110 | 411.304 | 3.980 | 2672.020 | 2515.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 7283) CPU | percent | 91 | 169.660 | 90.263 | 176.179 | 168.507 | 155.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 7283) rss_mb | MB | 92 | 2196.294 | 23.266 | 2322.145 | 2077.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 7283) main thread run-queue wait | percent | 91 | 53.339 | 0.207 | 74.054 | 55.158 | 48.936518 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 7283) vms_mb | MB | 92 | 2420.328 | 215.562 | 2740.930 | 2299.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7293) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7293) rss_mb | MB | 3 | 1.305 | 1.305 | 1.305 | 1.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7293) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7293) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7294) CPU | percent | 2 | 2.485 | 1.987 | 2.983 | 2.983 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7294) rss_mb | MB | 3 | 11.197 | 7.859 | 15.172 | 15.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7294) main thread run-queue wait | percent | 2 | 58.580 | 46.159 | 71.000 | 71.000 | 1.178769 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7294) vms_mb | MB | 3 | 16.185 | 12.926 | 20.426 | 20.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7297) CPU | percent | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7297) rss_mb | MB | 29 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7297) main thread run-queue wait | percent | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7297) vms_mb | MB | 29 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — base7.py (PID 7299) CPU | percent | 28 | 0.319 | 0.000 | 2.982 | 0.000 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — base7.py (PID 7299) rss_mb | MB | 29 | 11.581 | 7.211 | 11.848 | 11.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — base7.py (PID 7299) main thread run-queue wait | percent | 28 | 9.091 | 0.026 | 60.841 | 0.026 | 2.564122 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — base7.py (PID 7299) vms_mb | MB | 29 | 15.513 | 11.918 | 15.727 | 15.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpt58wi3ap.py (PID 7303) rss_mb | MB | 1 | 6.230 | 6.230 | 6.230 | 6.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpt58wi3ap.py (PID 7303) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpdbqdwyue.py (PID 7304) rss_mb | MB | 1 | 6.676 | 6.676 | 6.676 | 6.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpdbqdwyue.py (PID 7304) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpt497olx8.py (PID 7305) rss_mb | MB | 1 | 7.074 | 7.074 | 7.074 | 7.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpt497olx8.py (PID 7305) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp7c807pa9.py (PID 7306) rss_mb | MB | 1 | 7.254 | 7.254 | 7.254 | 7.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp7c807pa9.py (PID 7306) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpx9_oiiwu.py (PID 7307) rss_mb | MB | 1 | 7.176 | 7.176 | 7.176 | 7.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpx9_oiiwu.py (PID 7307) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpp6a6o0si.py (PID 7308) rss_mb | MB | 1 | 7.637 | 7.637 | 7.637 | 7.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpp6a6o0si.py (PID 7308) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvtobxotp.py (PID 7309) rss_mb | MB | 1 | 7.891 | 7.891 | 7.891 | 7.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvtobxotp.py (PID 7309) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp3isfttzi.py (PID 7310) rss_mb | MB | 1 | 7.852 | 7.852 | 7.852 | 7.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp3isfttzi.py (PID 7310) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp5cxwduro.py (PID 7311) rss_mb | MB | 1 | 7.875 | 7.875 | 7.875 | 7.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp5cxwduro.py (PID 7311) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp9mqaltye.py (PID 7312) rss_mb | MB | 1 | 7.590 | 7.590 | 7.590 | 7.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp9mqaltye.py (PID 7312) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpugoemm9q.py (PID 7313) rss_mb | MB | 1 | 7.941 | 7.941 | 7.941 | 7.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpugoemm9q.py (PID 7313) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp9yjkpo1t.py (PID 7314) rss_mb | MB | 1 | 8.109 | 8.109 | 8.109 | 8.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp9yjkpo1t.py (PID 7314) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpywvulpbn.py (PID 7315) rss_mb | MB | 1 | 8.105 | 8.105 | 8.105 | 8.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpywvulpbn.py (PID 7315) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpt51rm3pc.py (PID 7316) rss_mb | MB | 1 | 8.395 | 8.395 | 8.395 | 8.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpt51rm3pc.py (PID 7316) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp307izvle.py (PID 7317) rss_mb | MB | 1 | 8.484 | 8.484 | 8.484 | 8.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp307izvle.py (PID 7317) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpjsjnr5g8.py (PID 7318) rss_mb | MB | 1 | 8.547 | 8.547 | 8.547 | 8.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpjsjnr5g8.py (PID 7318) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppesf4kvq.py (PID 7320) rss_mb | MB | 1 | 6.711 | 6.711 | 6.711 | 6.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppesf4kvq.py (PID 7320) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpxq9fpszl.py (PID 7321) rss_mb | MB | 1 | 7.051 | 7.051 | 7.051 | 7.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpxq9fpszl.py (PID 7321) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0i301n6e.py (PID 7322) rss_mb | MB | 1 | 7.086 | 7.086 | 7.086 | 7.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp0i301n6e.py (PID 7322) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvyac2v8z.py (PID 7324) rss_mb | MB | 1 | 7.340 | 7.340 | 7.340 | 7.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpvyac2v8z.py (PID 7324) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpyj90kjsl.py (PID 7325) rss_mb | MB | 1 | 7.445 | 7.445 | 7.445 | 7.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpyj90kjsl.py (PID 7325) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmps04kxun5.py (PID 7326) rss_mb | MB | 1 | 7.582 | 7.582 | 7.582 | 7.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmps04kxun5.py (PID 7326) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpu01miul2.py (PID 7327) rss_mb | MB | 1 | 7.336 | 7.336 | 7.336 | 7.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpu01miul2.py (PID 7327) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp9m_czrx1.py (PID 7328) rss_mb | MB | 1 | 7.582 | 7.582 | 7.582 | 7.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp9m_czrx1.py (PID 7328) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmps8m1nus_.py (PID 7329) rss_mb | MB | 1 | 7.984 | 7.984 | 7.984 | 7.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmps8m1nus_.py (PID 7329) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7330) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7330) rss_mb | MB | 4 | 1.391 | 1.391 | 1.391 | 1.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7330) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7330) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7331) CPU | percent | 3 | 2.650 | 0.990 | 3.977 | 3.977 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7331) rss_mb | MB | 4 | 12.548 | 7.590 | 18.145 | 18.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7331) main thread run-queue wait | percent | 3 | 44.914 | 33.488 | 56.092 | 45.162 | 1.356587 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7331) vms_mb | MB | 4 | 17.414 | 11.926 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7337) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7337) rss_mb | MB | 4 | 1.391 | 1.391 | 1.391 | 1.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7337) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7337) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7338) CPU | percent | 3 | 3.286 | 1.927 | 3.977 | 3.977 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7338) rss_mb | MB | 4 | 12.863 | 7.438 | 18.453 | 18.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7338) main thread run-queue wait | percent | 3 | 55.309 | 50.487 | 59.859 | 50.487 | 1.690074 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7338) vms_mb | MB | 4 | 17.987 | 11.926 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7343) rss_mb | MB | 1 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7343) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7344) rss_mb | MB | 1 | 7.109 | 7.109 | 7.109 | 7.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7344) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7374) rss_mb | MB | 1 | 1.469 | 1.469 | 1.469 | 1.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7374) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7375) rss_mb | MB | 1 | 7.562 | 7.562 | 7.562 | 7.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7375) vms_mb | MB | 1 | 11.926 | 11.926 | 11.926 | 11.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7421) CPU | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7421) rss_mb | MB | 99 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7421) main thread run-queue wait | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7421) vms_mb | MB | 99 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7422) CPU | percent | 98 | 34.401 | 0.000 | 175.363 | 168.073 | 33.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7422) rss_mb | MB | 99 | 455.347 | 1.516 | 2324.973 | 2302.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7422) main thread run-queue wait | percent | 98 | 10.236 | 0.000 | 67.760 | 50.736 | 10.104241 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7422) vms_mb | MB | 99 | 509.643 | 3.977 | 2624.879 | 2532.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 7423) CPU | percent | 77 | 166.884 | 79.412 | 176.905 | 167.893 | 129.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 7423) rss_mb | MB | 78 | 2191.889 | 20.406 | 2242.934 | 2216.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 7423) main thread run-queue wait | percent | 77 | 56.115 | 7.593 | 77.564 | 56.437 | 43.547923 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps2.py (PID 7423) vms_mb | MB | 78 | 2419.925 | 212.160 | 2735.930 | 2438.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7424) rss_mb | MB | 1 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7424) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7425) rss_mb | MB | 1 | 20.113 | 20.113 | 20.113 | 20.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7425) vms_mb | MB | 1 | 25.117 | 25.117 | 25.117 | 25.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7432) rss_mb | MB | 1 | 1.398 | 1.398 | 1.398 | 1.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7432) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7433) rss_mb | MB | 1 | 9.910 | 9.910 | 9.910 | 9.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7433) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7434) rss_mb | MB | 1 | 1.391 | 1.391 | 1.391 | 1.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7434) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7435) rss_mb | MB | 1 | 20.250 | 20.250 | 20.250 | 20.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7435) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7438) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7438) rss_mb | MB | 4 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7438) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7438) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7439) CPU | percent | 3 | 4.308 | 2.981 | 6.960 | 6.960 | 0.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7439) rss_mb | MB | 4 | 13.719 | 7.984 | 20.363 | 20.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7439) main thread run-queue wait | percent | 3 | 52.092 | 40.170 | 65.248 | 50.859 | 1.572051 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7439) vms_mb | MB | 4 | 18.914 | 13.023 | 25.633 | 25.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7440) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7440) rss_mb | MB | 4 | 1.422 | 1.422 | 1.422 | 1.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7440) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7440) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7441) CPU | percent | 3 | 2.982 | 1.989 | 3.977 | 3.977 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7441) rss_mb | MB | 4 | 12.494 | 7.520 | 18.309 | 18.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7441) main thread run-queue wait | percent | 3 | 51.998 | 45.824 | 60.739 | 49.432 | 1.569356 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7441) vms_mb | MB | 4 | 17.419 | 11.789 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7443) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7443) rss_mb | MB | 4 | 1.305 | 1.305 | 1.305 | 1.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7443) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7443) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7444) CPU | percent | 3 | 3.311 | 1.979 | 4.970 | 4.970 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7444) rss_mb | MB | 4 | 13.522 | 7.758 | 20.297 | 20.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7444) main thread run-queue wait | percent | 3 | 58.942 | 49.853 | 66.204 | 49.853 | 1.781412 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7444) vms_mb | MB | 4 | 18.333 | 12.926 | 24.988 | 24.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7449) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7449) rss_mb | MB | 4 | 1.391 | 1.391 | 1.391 | 1.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7449) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7449) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7450) CPU | percent | 3 | 2.982 | 1.987 | 3.977 | 2.982 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7450) rss_mb | MB | 4 | 12.352 | 7.426 | 18.137 | 18.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7450) main thread run-queue wait | percent | 3 | 55.554 | 54.022 | 56.649 | 54.022 | 1.676624 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7450) vms_mb | MB | 4 | 17.393 | 11.789 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7452) rss_mb | MB | 1 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7452) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7453) rss_mb | MB | 1 | 7.992 | 7.992 | 7.992 | 7.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7453) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7454) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7454) rss_mb | MB | 4 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7454) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7454) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7455) CPU | percent | 3 | 2.969 | 1.977 | 3.962 | 3.962 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7455) rss_mb | MB | 4 | 12.321 | 7.031 | 18.102 | 18.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7455) main thread run-queue wait | percent | 3 | 60.448 | 59.445 | 61.254 | 59.445 | 1.832535 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7455) vms_mb | MB | 4 | 17.360 | 11.660 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7460) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7460) rss_mb | MB | 4 | 1.387 | 1.387 | 1.387 | 1.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7460) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7460) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7461) CPU | percent | 3 | 2.972 | 1.980 | 3.966 | 3.966 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7461) rss_mb | MB | 4 | 12.321 | 7.219 | 18.062 | 18.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7461) main thread run-queue wait | percent | 3 | 53.197 | 46.341 | 58.922 | 58.922 | 1.611198 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7461) vms_mb | MB | 4 | 17.419 | 11.789 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7465) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7465) rss_mb | MB | 4 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7465) main thread run-queue wait | percent | 3 | 0.033 | 0.000 | 0.100 | 0.000 | 0.001006 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7465) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7466) CPU | percent | 3 | 4.308 | 1.987 | 6.959 | 6.959 | 0.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7466) rss_mb | MB | 4 | 11.474 | 1.484 | 20.309 | 20.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7466) main thread run-queue wait | percent | 3 | 62.790 | 45.132 | 76.305 | 66.934 | 1.894986 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7466) vms_mb | MB | 4 | 15.514 | 2.531 | 25.504 | 25.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7467) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7467) rss_mb | MB | 4 | 1.488 | 1.488 | 1.488 | 1.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7467) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7467) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7468) CPU | percent | 3 | 2.968 | 1.972 | 3.961 | 3.961 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7468) rss_mb | MB | 4 | 12.352 | 7.148 | 18.137 | 18.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7468) main thread run-queue wait | percent | 3 | 54.279 | 50.098 | 57.015 | 55.723 | 1.646971 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7468) vms_mb | MB | 4 | 17.380 | 11.789 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7470) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7470) rss_mb | MB | 5 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7470) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7470) vms_mb | MB | 5 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7471) CPU | percent | 4 | 3.479 | 0.993 | 6.960 | 6.960 | 0.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7471) rss_mb | MB | 5 | 13.157 | 4.555 | 21.281 | 21.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7471) main thread run-queue wait | percent | 4 | 59.762 | 50.894 | 66.104 | 65.948 | 2.405013 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7471) vms_mb | MB | 5 | 18.513 | 10.000 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7472) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7472) rss_mb | MB | 2 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7472) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7472) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7473) CPU | percent | 1 | 2.980 | 2.980 | 2.980 | 2.980 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7473) rss_mb | MB | 2 | 8.631 | 7.465 | 9.797 | 9.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7473) main thread run-queue wait | percent | 1 | 61.324 | 61.324 | 61.324 | 61.324 | 0.617286 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7473) vms_mb | MB | 2 | 12.795 | 11.926 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7492) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7492) rss_mb | MB | 8 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7492) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7492) vms_mb | MB | 8 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — flips89.py (PID 7494) CPU | percent | 7 | 161.104 | 91.472 | 174.970 | 172.094 | 11.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — flips89.py (PID 7494) rss_mb | MB | 8 | 1661.688 | 17.266 | 2028.031 | 1110.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — flips89.py (PID 7494) main thread run-queue wait | percent | 7 | 60.862 | 0.016 | 74.182 | 71.761 | 4.283878 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — flips89.py (PID 7494) vms_mb | MB | 8 | 1898.941 | 209.711 | 2249.074 | 1519.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7548) rss_mb | MB | 1 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7548) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7549) rss_mb | MB | 1 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7549) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7550) rss_mb | MB | 1 | 1.305 | 1.305 | 1.305 | 1.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7550) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7551) rss_mb | MB | 1 | 1.305 | 1.305 | 1.305 | 1.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7551) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7567) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7567) rss_mb | MB | 10 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7567) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7567) vms_mb | MB | 10 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endkeys.py (PID 7569) CPU | percent | 9 | 161.227 | 112.263 | 174.616 | 171.000 | 14.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endkeys.py (PID 7569) rss_mb | MB | 10 | 2000.257 | 300.297 | 2215.109 | 2162.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endkeys.py (PID 7569) main thread run-queue wait | percent | 9 | 48.229 | 5.117 | 67.795 | 63.754 | 4.379741 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endkeys.py (PID 7569) vms_mb | MB | 10 | 2247.065 | 762.031 | 2438.215 | 2385.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7570) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7570) rss_mb | MB | 10 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7570) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7570) vms_mb | MB | 10 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7588) rss_mb | MB | 1 | 1.387 | 1.387 | 1.387 | 1.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7588) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7589) rss_mb | MB | 1 | 10.004 | 10.004 | 10.004 | 10.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7589) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7614) CPU | percent | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7614) rss_mb | MB | 31 | 2.953 | 2.953 | 2.953 | 2.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7614) main thread run-queue wait | percent | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7614) vms_mb | MB | 31 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfit.py (PID 7616) CPU | percent | 30 | 168.460 | 134.947 | 175.206 | 173.823 | 50.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfit.py (PID 7616) rss_mb | MB | 31 | 2024.319 | 424.293 | 2175.625 | 2142.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfit.py (PID 7616) main thread run-queue wait | percent | 30 | 65.681 | 23.614 | 77.738 | 49.277 | 19.852909 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfit.py (PID 7616) vms_mb | MB | 31 | 2474.849 | 762.117 | 2854.180 | 2426.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7617) CPU | percent | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7617) rss_mb | MB | 31 | 1.086 | 1.086 | 1.086 | 1.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7617) main thread run-queue wait | percent | 30 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7617) vms_mb | MB | 31 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7623) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7623) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7624) rss_mb | MB | 1 | 19.379 | 19.379 | 19.379 | 19.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7624) vms_mb | MB | 1 | 24.859 | 24.859 | 24.859 | 24.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7632) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7632) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7633) rss_mb | MB | 1 | 18.660 | 18.660 | 18.660 | 18.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7633) vms_mb | MB | 1 | 24.609 | 24.609 | 24.609 | 24.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7635) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7635) rss_mb | MB | 7 | 2.953 | 2.953 | 2.953 | 2.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7635) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7635) vms_mb | MB | 7 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfit2.py (PID 7637) CPU | percent | 6 | 162.183 | 150.875 | 170.051 | 160.570 | 9.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfit2.py (PID 7637) rss_mb | MB | 7 | 1439.223 | 1380.270 | 1733.480 | 1381.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfit2.py (PID 7637) main thread run-queue wait | percent | 6 | 40.748 | 22.350 | 55.026 | 39.154 | 2.461996 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfit2.py (PID 7637) vms_mb | MB | 7 | 1765.714 | 1593.254 | 2702.250 | 1593.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7638) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7638) rss_mb | MB | 7 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7638) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7638) vms_mb | MB | 7 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7642) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7642) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7643) rss_mb | MB | 1 | 21.781 | 21.781 | 21.781 | 21.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7643) vms_mb | MB | 1 | 26.926 | 26.926 | 26.926 | 26.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7653) CPU | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7653) rss_mb | MB | 24 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7653) main thread run-queue wait | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7653) vms_mb | MB | 24 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfinal.py (PID 7655) CPU | percent | 23 | 168.213 | 123.771 | 176.238 | 171.022 | 39.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfinal.py (PID 7655) rss_mb | MB | 24 | 2045.736 | 0.000 | 2361.797 | 2360.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfinal.py (PID 7655) main thread run-queue wait | percent | 23 | 62.402 | 11.947 | 77.183 | 51.419 | 14.467769 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — endfinal.py (PID 7655) vms_mb | MB | 24 | 2400.109 | 0.387 | 3038.191 | 2610.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7656) CPU | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7656) rss_mb | MB | 24 | 1.125 | 1.125 | 1.125 | 1.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7656) main thread run-queue wait | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7656) vms_mb | MB | 24 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7687) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7687) rss_mb | MB | 8 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7687) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7687) vms_mb | MB | 8 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7688) CPU | percent | 7 | 159.299 | 87.474 | 171.990 | 171.970 | 11.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7688) rss_mb | MB | 8 | 1718.779 | 13.613 | 2027.309 | 2027.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7688) main thread run-queue wait | percent | 7 | 49.609 | 5.116 | 69.874 | 69.874 | 3.494199 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7688) vms_mb | MB | 8 | 1990.870 | 207.211 | 2250.453 | 2250.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7689) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7689) rss_mb | MB | 8 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7689) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7689) vms_mb | MB | 8 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7705) CPU | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7705) rss_mb | MB | 20 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7705) main thread run-queue wait | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7705) vms_mb | MB | 20 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7707) CPU | percent | 19 | 167.417 | 100.294 | 179.200 | 166.022 | 32.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7707) rss_mb | MB | 20 | 1899.454 | 12.484 | 2026.016 | 2026.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7707) main thread run-queue wait | percent | 19 | 58.154 | 9.495 | 73.320 | 49.617 | 11.145391 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7707) vms_mb | MB | 20 | 2144.912 | 199.090 | 2249.008 | 2249.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7708) CPU | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7708) rss_mb | MB | 20 | 1.086 | 1.086 | 1.086 | 1.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7708) main thread run-queue wait | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cut (PID 7708) vms_mb | MB | 20 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7712) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7712) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7713) rss_mb | MB | 1 | 13.215 | 13.215 | 13.215 | 13.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7713) vms_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7722) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7722) rss_mb | MB | 7 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7722) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7722) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_final.py (PID 7724) CPU | percent | 6 | 165.199 | 145.829 | 172.077 | 166.103 | 9.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_final.py (PID 7724) rss_mb | MB | 7 | 131.935 | 6.723 | 189.098 | 85.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_final.py (PID 7724) main thread run-queue wait | percent | 6 | 52.166 | 32.206 | 68.529 | 52.403 | 3.147879 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_final.py (PID 7724) vms_mb | MB | 7 | 319.650 | 11.656 | 407.102 | 302.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7775) rss_mb | MB | 1 | 1.422 | 1.422 | 1.422 | 1.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7775) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7776) rss_mb | MB | 1 | 20.852 | 20.852 | 20.852 | 20.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7776) vms_mb | MB | 1 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| docker inspect (PID 7794) rss_mb | MB | 1 | 2.637 | 2.637 | 2.637 | 2.637 | n/a | n/a |
| docker inspect (PID 7794) vms_mb | MB | 1 | 69.043 | 69.043 | 69.043 | 69.043 | n/a | n/a |
| docker commit (PID 7811) CPU | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 7811) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 7811) io write MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 7811) rss_mb | MB | 25 | 29.090 | 29.090 | 29.090 | 29.090 | n/a | n/a |
| docker commit (PID 7811) main thread run-queue wait | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 7811) vms_mb | MB | 25 | 1699.199 | 1699.199 | 1699.199 | 1699.199 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 CPU | percent | 4161 | 92.443 | 0.000 | 218.809 | 0.000 | 3878.819120 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 4161 | 14.282 | 0.000 | 50.882 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 4161 | 19.952 | 0.000 | 96.415 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_full_pct | percent of wall time stalled | 4161 | 0.161 | 0.000 | 96.523 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_some_pct | percent of wall time stalled | 4161 | 0.201 | 0.000 | 96.570 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io read MB/s | MB/s | 4161 | 0.842 | 0.000 | 185.789 | 0.000 | 3730.761719 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io write MB/s | MB/s | 4161 | 0.475 | 0.000 | 238.222 | 0.000 | 1990.699219 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory | MB | 4162 | 2076.036 | 17.352 | 8271.016 | 1907.281 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_full_pct | percent of wall time stalled | 4161 | 0.065 | 0.000 | 60.579 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_some_pct | percent of wall time stalled | 4161 | 0.065 | 0.000 | 60.685 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net rx MB/s | MB/s | 4161 | 0.002 | 0.000 | 8.395 | 0.000 | 8.505226 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net tx MB/s | MB/s | 4161 | 0.000 | 0.000 | 0.016 | 0.000 | 0.056931 MB | n/a |
| workload total CPU | percent | 4167 | 6.652 | 1.532 | 176.738 | 2.046 | 286.013303 CPU seconds | n/a |
| workload total memory | MB | 4168 | 7826.278 | 5943.355 | 11164.066 | 7425.598 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
