# agprof summary

- Duration: **1991.331 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **98 calls**, 98 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1696.428 s total wait
- Tools: **105/105 completed**, 2 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **185429** at 1.975 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1991258.986 / 1991258.986 ms |
| LLM latency p50 / p95 | 15110.294 / 44622.043 ms |
| LLM TTFT p50 / p95 | 7676.433 / 33384.356 ms |
| LLM input / output tokens | 392 / 187059 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 98 total, 98 succeeded, 0 failed, 0 interrupted |
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
| Bash | 59/59 | 57 | 2 | 0 | n/a | n/a |
| ToolSearch | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 11/11 | 11 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 7/7 | 7 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 8/8 | 8 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 12/12 | 12 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 6.517% | 104.919% | 129.908 s | 9381.770 MB | 9730.188 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bash | 5210 | sandbox_agent_lsb-claude_code_0000_0000 | 1979 | 32.468% | 107.321% | 646.220 s | 108.397 MB | 118.586 MB | 971.230 MB | 976.449 MB | n/a MB | n/a MB |
| lsb_grid_worker | 1958 |  | 1979 | 0.000% | 0.000% | 0.000 s | 3.164 MB | 3.164 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| tail | 5115 | sandbox_agent_lsb-claude_code_0000_0000 | 1979 | 0.003% | 0.995% | 0.050 s | 1.266 MB | 1.266 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| docker-init | 5086 | sandbox_agent_lsb-claude_code_0000_0000 | 1979 | 0.003% | 0.995% | 0.050 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 5216 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 62.973% | 69.644% | 1.270 s | 43.909 MB | 77.855 MB | 53.828 MB | 93.281 MB | n/a MB | n/a MB |
| python | 4866 |  | 1979 | 0.000% | 0.000% | 0.000 s | 12.176 MB | 12.176 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 4832 |  | 1979 | 0.095% | 7.939% | 1.900 s | 1803.021 MB | 1803.691 MB | 11045.574 MB | 11046.629 MB | 0.007812 MB | 0.015625 MB |
| VLLM::EngineCor | 4867 |  | 1979 | 1.272% | 22.825% | 25.320 s | 2321.896 MB | 2322.555 MB | 21204.309 MB | 21204.309 MB | 0.003906 MB | 0.011719 MB |
| python | 4827 |  | 1979 | 5.143% | 102.970% | 102.570 s | 2772.134 MB | 3008.578 MB | 15718.807 MB | 15988.961 MB | 6.191406 MB | 712.699219 MB |
| claude | 5224 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.203 MB | 13.203 MB | 5473.734 MB | 5473.734 MB | n/a MB | n/a MB |
| claude | 5229 | sandbox_agent_lsb-claude_code_0000_0000 | 1951 | 3.531% | 68.563% | 69.290 s | 307.414 MB | 342.973 MB | 5499.815 MB | 5499.879 MB | n/a MB | n/a MB |
| python3 | 5368 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.391 MB | 21.391 MB | 26.910 MB | 26.910 MB | n/a MB | n/a MB |
| sh | 5367 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5399 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.664 MB | 7.664 MB | 11.926 MB | 11.926 MB | n/a MB | n/a MB |
| sh | 5398 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5404 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.215 MB | 9.215 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| sh | 5403 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 5451 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.488 MB | 1.488 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5452 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.133 MB | 15.133 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| claude | 5465 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 305.457 MB | 305.457 MB | 5499.816 MB | 5499.816 MB | n/a MB | n/a MB |
| python3 | 5497 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.812 MB | 18.812 MB | 24.605 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 5496 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5506 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.410 MB | 6.410 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 5505 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 5648 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 55.652 MB | 55.652 MB | 66.602 MB | 66.602 MB | n/a MB | n/a MB |
| bash | 5644 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.754 MB | 2.754 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 5660 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5661 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.652 MB | 17.652 MB | 23.098 MB | 23.098 MB | n/a MB | n/a MB |
| python3 | 5676 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.453 MB | 20.453 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| sh | 5675 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5819 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.387 MB | 20.387 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| sh | 5818 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 5877 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5878 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.918 MB | 6.918 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 5883 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5884 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.488 MB | 18.488 MB | 24.254 MB | 24.254 MB | n/a MB | n/a MB |
| sh | 5886 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.488 MB | 1.488 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5887 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.145 MB | 18.145 MB | 24.098 MB | 24.098 MB | n/a MB | n/a MB |
| bash | 5893 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.727 MB | 2.727 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 5895 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.578 MB | 13.578 MB | 208.480 MB | 208.480 MB | n/a MB | n/a MB |
| bash | 5907 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.320 MB | 1.320 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 5906 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.668 MB | 2.668 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 5918 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5919 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.301 MB | 21.301 MB | 26.902 MB | 26.902 MB | n/a MB | n/a MB |
| python | 5924 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 857.258 MB | 857.258 MB | 1806.082 MB | 1806.082 MB | n/a MB | n/a MB |
| bash | 5922 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.691 MB | 2.691 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 5935 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 5937 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 161.911% | 161.911% | 1.630 s | 1534.869 MB | 2006.066 MB | 1955.707 MB | 2240.516 MB | n/a MB | n/a MB |
| python | 5954 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 168.273% | 175.695% | 23.730 s | 1874.456 MB | 2016.699 MB | 2093.942 MB | 2237.844 MB | n/a MB | n/a MB |
| bash | 5952 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 3.016 MB | 3.016 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 5978 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.793 MB | 13.793 MB | 207.262 MB | 207.262 MB | n/a MB | n/a MB |
| bash | 5977 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.836 MB | 2.836 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 6032 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 6033 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 6062 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 162.985% | 172.001% | 3.280 s | 1103.363 MB | 2023.664 MB | 1417.315 MB | 2244.527 MB | n/a MB | n/a MB |
| bash | 6060 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.887 MB | 2.887 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6079 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.859 MB | 23.859 MB | 215.684 MB | 215.684 MB | n/a MB | n/a MB |
| bash | 6077 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.809 MB | 2.809 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 6094 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.652 MB | 2.652 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6096 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 263.719 MB | 263.719 MB | 840.582 MB | 840.582 MB | n/a MB | n/a MB |
| sh | 6108 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6109 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.867 MB | 15.867 MB | 20.527 MB | 20.527 MB | n/a MB | n/a MB |
| python | 6114 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 99.206% | 100.338% | 6.990 s | 2032.082 MB | 2062.449 MB | 2244.009 MB | 2253.918 MB | n/a MB | n/a MB |
| bash | 6112 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.984 MB | 2.984 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6137 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.840 MB | 23.840 MB | 215.656 MB | 215.656 MB | n/a MB | n/a MB |
| bash | 6135 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.746 MB | 2.746 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| head | 6165 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.141 MB | 1.141 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 6161 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.789 MB | 2.789 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6164 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 130.445 MB | 130.445 MB | 135.340 MB | 135.340 MB | n/a MB | n/a MB |
| python | 6182 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.371 MB | 13.371 MB | 207.219 MB | 207.219 MB | n/a MB | n/a MB |
| bash | 6180 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.918 MB | 2.918 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6218 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.391 MB | 20.391 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| sh | 6217 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6228 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.859 MB | 2.859 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6229 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.145 MB | 9.145 MB | 13.254 MB | 13.254 MB | n/a MB | n/a MB |
| python3 | 6276 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.609 MB | 20.609 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| sh | 6275 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.605 MB | 1.605 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 6297 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.992 MB | 12.992 MB | 207.055 MB | 207.055 MB | n/a MB | n/a MB |
| bash | 6295 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.762 MB | 2.762 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 6313 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.773 MB | 2.773 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6316 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.648 MB | 17.648 MB | 209.781 MB | 209.781 MB | n/a MB | n/a MB |
| bash | 6329 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.934 MB | 2.934 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6331 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 156.099% | 171.975% | 6.290 s | 1061.796 MB | 1438.234 MB | 1282.205 MB | 1660.859 MB | n/a MB | n/a MB |
| sh | 6335 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.488 MB | 1.488 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6336 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.086 MB | 18.086 MB | 24.098 MB | 24.098 MB | n/a MB | n/a MB |
| python | 6348 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 151.667% | 162.552% | 6.120 s | 1601.947 MB | 1998.586 MB | 1818.495 MB | 2221.180 MB | n/a MB | n/a MB |
| bash | 6346 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.867 MB | 2.867 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6378 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.402 MB | 21.402 MB | 26.680 MB | 26.680 MB | n/a MB | n/a MB |
| sh | 6377 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.387 MB | 1.387 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6395 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.816 MB | 2.816 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6397 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.812 MB | 23.812 MB | 215.816 MB | 215.816 MB | n/a MB | n/a MB |
| python3 | 6402 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.809 MB | 15.809 MB | 20.461 MB | 20.461 MB | n/a MB | n/a MB |
| sh | 6401 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6411 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.035 MB | 3.035 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6413 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 81.445% | 81.445% | 0.820 s | 104.752 MB | 190.414 MB | 297.398 MB | 383.363 MB | n/a MB | n/a MB |
| python3 | 6425 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.281 MB | 20.281 MB | 25.246 MB | 25.246 MB | n/a MB | n/a MB |
| sh | 6424 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.426 MB | 1.426 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6429 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.930 MB | 2.930 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| tail | 6432 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.195 MB | 1.195 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python | 6431 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 197.113 MB | 197.113 MB | 390.133 MB | 390.133 MB | n/a MB | n/a MB |
| bash | 6446 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.875 MB | 2.875 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6447 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 135.340 MB | 135.340 MB | 139.254 MB | 139.254 MB | n/a MB | n/a MB |
| python3 | 6472 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.789 MB | 9.789 MB | 13.617 MB | 13.617 MB | n/a MB | n/a MB |
| sh | 6471 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6489 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.922 MB | 2.922 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python | 6491 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.836 MB | 21.836 MB | 213.934 MB | 213.934 MB | n/a MB | n/a MB |
| python3 | 6501 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.348 MB | 5.348 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| sh | 6500 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6502 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.656 MB | 2.656 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6505 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 76.182% | 77.499% | 4.600 s | 196.565 MB | 214.902 MB | 389.289 MB | 407.574 MB | n/a MB | n/a MB |
| python3 | 6518 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.609 MB | 21.609 MB | 26.906 MB | 26.906 MB | n/a MB | n/a MB |
| sh | 6517 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6520 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6522 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 77.135% | 78.546% | 4.660 s | 258.530 MB | 336.121 MB | 464.467 MB | 559.582 MB | n/a MB | n/a MB |
| python | 6541 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 158.027% | 175.265% | 7.980 s | 1070.506 MB | 1317.945 MB | 1283.199 MB | 1540.531 MB | n/a MB | n/a MB |
| bash | 6539 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6567 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 82.066% | 86.397% | 2.480 s | 221.002 MB | 294.727 MB | 587.485 MB | 1058.801 MB | n/a MB | n/a MB |
| bash | 6565 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.871 MB | 2.871 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 6581 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.605 MB | 1.605 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6582 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.250 MB | 9.250 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| python | 6586 | sandbox_agent_lsb-claude_code_0000_0000 | 12 | 78.926% | 86.485% | 8.740 s | 212.306 MB | 220.445 MB | 432.280 MB | 445.613 MB | n/a MB | n/a MB |
| bash | 6584 | sandbox_agent_lsb-claude_code_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 2.820 MB | 2.820 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 6604 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.320 MB | 20.320 MB | 25.117 MB | 25.117 MB | n/a MB | n/a MB |
| sh | 6603 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 6634 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 91.215 MB | 91.215 MB | 96.215 MB | 96.215 MB | n/a MB | n/a MB |
| bash | 6632 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.734 MB | 2.734 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 6649 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6650 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.641 MB | 14.641 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| sh | 6659 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6660 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.863 MB | 7.863 MB | 12.926 MB | 12.926 MB | n/a MB | n/a MB |
| bash | 6662 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.000 MB | 3.000 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python | 6664 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 196.680 MB | 196.680 MB | 390.211 MB | 390.211 MB | n/a MB | n/a MB |
| python | 6681 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 79.542% | 91.345% | 10.410 s | 205.740 MB | 221.422 MB | 413.534 MB | 446.664 MB | n/a MB | n/a MB |
| bash | 6679 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 2.961 MB | 2.961 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python | 6698 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 103.713% | 118.342% | 3.130 s | 2243.391 MB | 3379.625 MB | 2890.770 MB | 4303.621 MB | n/a MB | n/a MB |
| bash | 6696 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.746 MB | 2.746 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 6702 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6703 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.207 MB | 19.207 MB | 24.734 MB | 24.734 MB | n/a MB | n/a MB |
| python | 6714 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 120.302% | 120.302% | 1.210 s | 30.920 MB | 52.172 MB | 144.336 MB | 275.066 MB | n/a MB | n/a MB |
| bash | 6712 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.883 MB | 2.883 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 6726 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.578 MB | 20.578 MB | 25.504 MB | 25.504 MB | n/a MB | n/a MB |
| sh | 6724 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6731 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6730 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 73.808% | 74.453% | 2.230 s | 211.564 MB | 221.359 MB | 405.655 MB | 415.742 MB | n/a MB | n/a MB |
| bash | 6728 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| claude | 6732 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 6.680 MB | 6.680 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| sh | 6736 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6737 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.816 MB | 14.816 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| python3 | 6760 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.605 MB | 15.605 MB | 20.527 MB | 20.527 MB | n/a MB | n/a MB |
| sh | 6759 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6774 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.547 MB | 20.547 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| sh | 6773 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6789 | sandbox_agent_lsb-claude_code_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.965 MB | 2.965 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6791 | sandbox_agent_lsb-claude_code_0000_0000 | 11 | 78.510% | 85.380% | 7.910 s | 202.654 MB | 221.699 MB | 414.229 MB | 446.469 MB | n/a MB | n/a MB |
| bash | 6808 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.926 MB | 2.926 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 6810 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 165.479% | 171.674% | 6.660 s | 76.959 MB | 123.227 MB | 289.374 MB | 340.180 MB | n/a MB | n/a MB |
| python3 | 6815 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.777 MB | 2.777 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| sh | 6814 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 6823 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.246 MB | 13.246 MB | 207.137 MB | 207.137 MB | n/a MB | n/a MB |
| bash | 6821 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.832 MB | 2.832 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6842 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.516 MB | 18.516 MB | 24.148 MB | 24.148 MB | n/a MB | n/a MB |
| sh | 6841 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| claude | 6888 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 318.930 MB | 318.930 MB | 5499.879 MB | 5499.879 MB | n/a MB | n/a MB |
| docker | 6926 |  | 21 | 0.000% | 0.000% | 0.000 s | 30.445 MB | 30.445 MB | 1771.516 MB | 1771.516 MB | 0.000000 MB | 0.000000 MB |
| docker | 6975 |  | 1 | n/a% | n/a% | n/a s | 17.090 MB | 17.090 MB | 1625.598 MB | 1625.598 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.554% | 48.000% | 11936.799 MB | 12192.000 MB | 29.803 W | 57.744 W | 59316.528 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-claude_code_0000_0000 | 44.382% | 203.265% | 883.520 s | 563.423 MB | 3859.105 MB | 239.617188 MB | 20.781250 MB | 8.501284 MB | 0.049273 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4975 | 1991.266 | interrupted |
| harness:retire | -1 | 0.132 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 1/1 | 0 | 0 | 1991.260 | 0.000 | 1991.260 | 239.617 | 1991260.195 | 1991260.195 | 1991260.195 |
| run:write_lora_adapter | 1/1 | 0 | 0 | 1991.259 | n/a | n/a | 239.617 | 1991258.986 | 1991258.986 | 1991258.986 |
| engine:execute | 1/1 | 0 | 0 | 1991.257 | 2.833 | 1988.423 | 239.617 | 1991257.275 | 1991257.275 | 1991257.275 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1964.044 | 0.006 | 1964.038 | 153.229 | 1964043.935 | 1964043.935 | 1964043.935 |
| harness:await_cli | 1/1 | 0 | 0 | 1960.670 | n/a | n/a | 76.568 | 1960670.314 | 1960670.314 | 1960670.314 |
| llm:attempt | 98/98 | 0 | 0 | 1696.428 | 4.806 | 1691.620 | 22.606 | 17310.494 | 15110.294 | 44622.043 |
| tool:Bash | 59/59 | 2 | 0 | 146.354 | n/a | n/a | 43.324 | 2480.568 | 688.822 | 11152.705 |
| tool:mcp__agency__inspect | 11/11 | 0 | 0 | 41.858 | n/a | n/a | 0.386 | 3805.232 | 3791.158 | 3886.892 |
| tool:mcp__agency__inspect_module_inputs | 7/7 | 0 | 0 | 26.332 | n/a | n/a | 0.372 | 3761.685 | 3760.191 | 3985.623 |
| run:container_call | 13/13 | 0 | 0 | 22.607 | 0.003 | 22.604 | 0.000 | 1738.987 | 45.019 | 8880.348 |
| teardown:commit | 1/1 | 0 | 0 | 22.156 | 0.005 | 22.152 | 0.000 | 22156.300 | 22156.300 | 22156.300 |
| sandbox:commit | 1/1 | 0 | 0 | 21.966 | 0.003 | 21.963 | 0.000 | 21965.877 | 21965.877 | 21965.877 |
| checkpoint.total | 1/1 | 0 | 0 | 21.966 | 0.002 | 21.963 | 0.000 | 21965.726 | 21965.726 | 21965.726 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 21.966 | 0.002 | 21.963 | 0.000 | 21965.580 | 21965.580 | 21965.580 |
| tool:mcp__agency__trace | 12/12 | 0 | 0 | 9.421 | n/a | n/a | 0.544 | 785.060 | 633.128 | 1386.784 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.298 | 1.058 | 3.240 | 83.802 | 4297.754 | 4297.754 | 4297.754 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.298 | 1.058 | 3.240 | 83.792 | 4297.520 | 4297.520 | 4297.520 |
| tool:mcp__agency__patch | 8/8 | 0 | 0 | 3.254 | n/a | n/a | 0.132 | 406.765 | 400.572 | 425.180 |
| syscall:sendto | 837/837 | 0 | 0 | 2.216 | n/a | n/a | 0.865 | 2.648 | 2.215 | 6.329 |
| harness:startup_ready | 1/1 | 0 | 0 | 2.018 | n/a | n/a | 40.077 | 2018.084 | 2018.084 | 2018.084 |
| tool:mcp__agency__generate | 2/2 | 0 | 0 | 1.313 | n/a | n/a | 0.965 | 656.456 | 656.456 | 732.030 |
| syscall:execve | 634/634 | 0 | 0 | 0.943 | n/a | n/a | 0.837 | 1.487 | 1.336 | 2.567 |
| syscall:connect | 276/276 | 0 | 0 | 0.701 | n/a | n/a | 0.669 | 2.541 | 2.293 | 4.417 |
| harness:submit | 1/1 | 0 | 0 | 0.607 | n/a | n/a | 10.324 | 607.339 | 607.339 | 607.339 |
| tool:mcp__agency__attention | 2/2 | 0 | 0 | 0.581 | n/a | n/a | 0.018 | 290.702 | 290.702 | 292.496 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 0.560 | n/a | n/a | 0.001 | 559.998 | 559.998 | 559.998 |
| tool:ToolSearch | 1/1 | 0 | 0 | 0.459 | n/a | n/a | 0.806 | 458.990 | 458.990 | 458.990 |
| sandbox:start | 1/1 | 0 | 0 | 0.381 | 0.002 | 0.379 | 0.000 | 381.001 | 381.001 | 381.001 |
| runtime.container_create | 1/1 | 0 | 0 | 0.381 | 0.002 | 0.379 | 0.000 | 380.865 | 380.865 | 380.865 |
| sandbox:create | 1/1 | 0 | 0 | 0.369 | 0.262 | 0.107 | 0.000 | 369.142 | 369.142 | 369.142 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.355 | n/a | n/a | 0.041 | 354.856 | 354.856 | 354.856 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.244 | n/a | n/a | 0.001 | 243.611 | 243.611 | 243.611 |
| agency:services_close | 1/1 | 0 | 0 | 0.198 | 0.001 | 0.197 | 0.265 | 197.543 | 197.543 | 197.543 |
| sandbox:stop | 1/1 | 0 | 0 | 0.190 | 0.002 | 0.188 | 0.000 | 190.122 | 190.122 | 190.122 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.031 | 0.000 | 72.713 | 72.713 | 72.713 |
| run:detect | 1/1 | 0 | 0 | 0.059 | 0.001 | 0.058 | 0.000 | 58.506 | 58.506 | 58.506 |
| harness:launch | 1/1 | 0 | 0 | 0.052 | n/a | n/a | 1.640 | 52.104 | 52.104 | 52.104 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.008 | 0.041 | 0.000 | 49.126 | 49.126 | 49.126 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.009 | 0.009 | 0.000 | 0.037 | 8.607 | 8.607 | 8.607 |
| harness:snapshot | 1/1 | 0 | 0 | 0.005 | n/a | n/a | 0.024 | 5.479 | 5.479 | 5.479 |
| syscall:bind | 2/2 | 0 | 0 | 0.003 | n/a | n/a | 0.051 | 1.575 | 1.575 | 2.008 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.244 | 1.244 | 1.244 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.079 | 0.084 | 0.098 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.189 | 0.189 | 0.189 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.055 | 0.055 | 0.055 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1978 | 0.422 | 0.021 | 51.059 | 51.059 | 8.401374 CPU seconds | n/a |
| GPU 0 memory | MB | 1979 | 11936.799 | 11670.000 | 12192.000 | 11820.000 | n/a | n/a |
| GPU 0 power | W | 1979 | 29.803 | 28.239 | 57.744 | 28.587 | n/a | 59316.528 J |
| GPU 0 proc / 4827-318711 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 memory | MB | 1979 | 3304.053 | 3118.000 | 3558.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 4827-318711 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 estimated power | W | 1916 | 2.285 | 0.000 | 57.223 | 0.000 | n/a | n/a |
| GPU 0 proc / 4827-318711 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 utilization | percent | 1916 | 1.603 | 0.000 | 46.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 4867-321119 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 memory | MB | 1979 | 8150.747 | 8070.000 | 8152.000 | 8152.000 | n/a | n/a |
| GPU 0 proc / 4867-321119 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 estimated power | W | 36 | 3.007 | 0.000 | 39.690 | 0.000 | n/a | n/a |
| GPU 0 proc / 4867-321119 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 utilization | percent | 36 | 1.139 | 0.000 | 21.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1979 | 11454.799 | 11188.000 | 11710.000 | 11338.000 | n/a | n/a |
| GPU 0 utilization | percent | 1979 | 1.554 | 0.000 | 48.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1979 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1978 | 1.923 | 0.088 | 70.814 | 2.911 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1978 | 12.622 | 1.026 | 51.852 | 13.990 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1978 | 0.894 | 0.000 | 187.756 | 9.064 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1978 | 0.389 | 0.000 | 29.563 | 1.974 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1978 | 0.397 | 0.000 | 52.567 | 17.471 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1978 | 0.402 | 0.000 | 52.773 | 17.634 | n/a | n/a |
| host mem_total_mb | MB | 1979 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1979 | 7067.452 | 6535.258 | 10498.375 | 7109.340 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1978 | 0.084 | 0.000 | 51.926 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1978 | 0.084 | 0.000 | 52.123 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1978 | 0.007 | 0.000 | 8.689 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1978 | 0.026 | 0.000 | 0.970 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1958) CPU | percent | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1958) io read MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1958) io write MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1958) rss_mb | MB | 1979 | 3.164 | 3.164 | 3.164 | 3.164 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1958) main thread run-queue wait | percent | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1958) vms_mb | MB | 1979 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4827) CPU | percent | 1978 | 5.143 | 0.000 | 102.970 | 1.989 | 102.570000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 4827) io read MB/s | MB/s | 1978 | 0.003 | 0.000 | 3.108 | 0.124 | 6.191406 MB | n/a |
| Agency harness — python -m lsbench (PID 4827) io write MB/s | MB/s | 1978 | 0.357 | 0.016 | 57.870 | 0.035 | 712.699219 MB | n/a |
| Agency harness — python -m lsbench (PID 4827) rss_mb | MB | 1979 | 2772.134 | 2261.574 | 3008.578 | 3008.578 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4827) main thread run-queue wait | percent | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 4827) vms_mb | MB | 1979 | 15718.807 | 13731.855 | 15988.961 | 15743.406 | n/a | n/a |
| Python — vllm (PID 4832) CPU | percent | 1978 | 0.095 | 0.000 | 7.939 | 0.000 | 1.900000 CPU seconds | n/a |
| Python — vllm (PID 4832) io read MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 4832) io write MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.008 | 0.000 | 0.015625 MB | n/a |
| Python — vllm (PID 4832) rss_mb | MB | 1979 | 1803.021 | 1799.051 | 1803.691 | 1799.051 | n/a | n/a |
| Python — vllm (PID 4832) main thread run-queue wait | percent | 1978 | 0.002 | 0.000 | 0.690 | 0.002 | 0.037554 run-queue seconds | n/a |
| Python — vllm (PID 4832) vms_mb | MB | 1979 | 11045.574 | 10974.609 | 11046.629 | 11046.629 | n/a | n/a |
| Python — python -c (PID 4866) CPU | percent | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 4866) io read MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4866) io write MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4866) rss_mb | MB | 1979 | 12.176 | 12.176 | 12.176 | 12.176 | n/a | n/a |
| Python — python -c (PID 4866) main thread run-queue wait | percent | 1978 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 4866) vms_mb | MB | 1979 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 4867) CPU | percent | 1978 | 1.272 | 0.000 | 22.825 | 1.989 | 25.320000 CPU seconds | n/a |
| VLLM::EngineCore (PID 4867) io read MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 4867) io write MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 4867) rss_mb | MB | 1979 | 2321.896 | 2317.930 | 2322.555 | 2317.930 | n/a | n/a |
| VLLM::EngineCore (PID 4867) main thread run-queue wait | percent | 1978 | 0.000 | 0.000 | 0.326 | 0.000 | 0.003617 run-queue seconds | n/a |
| VLLM::EngineCore (PID 4867) vms_mb | MB | 1979 | 21204.309 | 21204.309 | 21204.309 | 21204.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 5086) CPU | percent | 1978 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 5086) rss_mb | MB | 1979 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 5086) main thread run-queue wait | percent | 1978 | 0.007 | 0.000 | 4.174 | 0.004 | 0.141878 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 5086) vms_mb | MB | 1979 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5115) CPU | percent | 1978 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5115) rss_mb | MB | 1979 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5115) main thread run-queue wait | percent | 1978 | 0.005 | 0.000 | 3.908 | 0.008 | 0.104433 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 5115) vms_mb | MB | 1979 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5210) CPU | percent | 1978 | 32.468 | 0.000 | 107.321 | 0.995 | 646.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5210) rss_mb | MB | 1979 | 108.397 | 2.941 | 118.586 | 118.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5210) main thread run-queue wait | percent | 1978 | 0.000 | 0.000 | 0.042 | 0.042 | 0.000580 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5210) vms_mb | MB | 1979 | 971.230 | 4.262 | 976.449 | 975.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5216) CPU | percent | 2 | 62.973 | 56.303 | 69.644 | 69.644 | 1.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5216) rss_mb | MB | 3 | 43.909 | 6.680 | 77.855 | 77.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5216) main thread run-queue wait | percent | 2 | 0.019 | 0.018 | 0.020 | 0.020 | 0.000390 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5216) vms_mb | MB | 3 | 53.828 | 11.680 | 93.281 | 93.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5224) rss_mb | MB | 1 | 13.203 | 13.203 | 13.203 | 13.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5224) vms_mb | MB | 1 | 5473.734 | 5473.734 | 5473.734 | 5473.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5229) CPU | percent | 1950 | 3.531 | 0.000 | 68.563 | 4.968 | 69.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5229) rss_mb | MB | 1951 | 307.414 | 111.734 | 342.973 | 323.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5229) main thread run-queue wait | percent | 1950 | 1.161 | 0.002 | 72.725 | 0.018 | 22.810431 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5229) vms_mb | MB | 1951 | 5499.815 | 5492.801 | 5499.879 | 5499.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5367) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5367) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5368) rss_mb | MB | 1 | 21.391 | 21.391 | 21.391 | 21.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5368) vms_mb | MB | 1 | 26.910 | 26.910 | 26.910 | 26.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5398) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5398) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5399) rss_mb | MB | 1 | 7.664 | 7.664 | 7.664 | 7.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5399) vms_mb | MB | 1 | 11.926 | 11.926 | 11.926 | 11.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5403) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5403) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5404) rss_mb | MB | 1 | 9.215 | 9.215 | 9.215 | 9.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5404) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5451) rss_mb | MB | 1 | 1.488 | 1.488 | 1.488 | 1.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5451) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5452) rss_mb | MB | 1 | 15.133 | 15.133 | 15.133 | 15.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5452) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5465) rss_mb | MB | 1 | 305.457 | 305.457 | 305.457 | 305.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 5465) vms_mb | MB | 1 | 5499.816 | 5499.816 | 5499.816 | 5499.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5496) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5496) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5497) rss_mb | MB | 1 | 18.812 | 18.812 | 18.812 | 18.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5497) vms_mb | MB | 1 | 24.605 | 24.605 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5505) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5505) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5506) rss_mb | MB | 1 | 6.410 | 6.410 | 6.410 | 6.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5506) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5644) rss_mb | MB | 1 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5644) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5648) rss_mb | MB | 1 | 55.652 | 55.652 | 55.652 | 55.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5648) vms_mb | MB | 1 | 66.602 | 66.602 | 66.602 | 66.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5660) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5660) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5661) rss_mb | MB | 1 | 17.652 | 17.652 | 17.652 | 17.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5661) vms_mb | MB | 1 | 23.098 | 23.098 | 23.098 | 23.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5675) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5675) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5676) rss_mb | MB | 1 | 20.453 | 20.453 | 20.453 | 20.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5676) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5818) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5818) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5819) rss_mb | MB | 1 | 20.387 | 20.387 | 20.387 | 20.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5819) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5877) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5877) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5878) rss_mb | MB | 1 | 6.918 | 6.918 | 6.918 | 6.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5878) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5883) rss_mb | MB | 1 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5883) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5884) rss_mb | MB | 1 | 18.488 | 18.488 | 18.488 | 18.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5884) vms_mb | MB | 1 | 24.254 | 24.254 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5886) rss_mb | MB | 1 | 1.488 | 1.488 | 1.488 | 1.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5886) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5887) rss_mb | MB | 1 | 18.145 | 18.145 | 18.145 | 18.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5887) vms_mb | MB | 1 | 24.098 | 24.098 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5893) rss_mb | MB | 1 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5893) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5895) rss_mb | MB | 1 | 13.578 | 13.578 | 13.578 | 13.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5895) vms_mb | MB | 1 | 208.480 | 208.480 | 208.480 | 208.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5906) rss_mb | MB | 1 | 2.668 | 2.668 | 2.668 | 2.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5906) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5907) rss_mb | MB | 1 | 1.320 | 1.320 | 1.320 | 1.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5907) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5918) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5918) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5919) rss_mb | MB | 1 | 21.301 | 21.301 | 21.301 | 21.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5919) vms_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5922) rss_mb | MB | 1 | 2.691 | 2.691 | 2.691 | 2.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5922) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dla.py (PID 5924) rss_mb | MB | 1 | 857.258 | 857.258 | 857.258 | 857.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dla.py (PID 5924) vms_mb | MB | 1 | 1806.082 | 1806.082 | 1806.082 | 1806.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5935) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5935) rss_mb | MB | 2 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5935) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5935) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an1.py (PID 5937) CPU | percent | 1 | 161.911 | 161.911 | 161.911 | 161.911 | 1.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an1.py (PID 5937) rss_mb | MB | 2 | 1534.869 | 1063.672 | 2006.066 | 2006.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an1.py (PID 5937) main thread run-queue wait | percent | 1 | 51.562 | 51.562 | 51.562 | 51.562 | 0.519090 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an1.py (PID 5937) vms_mb | MB | 2 | 1955.707 | 1670.898 | 2240.516 | 2240.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5952) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5952) rss_mb | MB | 15 | 3.016 | 3.016 | 3.016 | 3.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5952) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5952) vms_mb | MB | 15 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an2.py (PID 5954) CPU | percent | 14 | 168.273 | 103.387 | 175.695 | 171.979 | 23.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an2.py (PID 5954) rss_mb | MB | 15 | 1874.456 | 13.973 | 2016.699 | 2016.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an2.py (PID 5954) main thread run-queue wait | percent | 14 | 69.363 | 16.729 | 79.873 | 74.525 | 9.782249 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an2.py (PID 5954) vms_mb | MB | 15 | 2093.942 | 207.520 | 2237.844 | 2237.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5977) rss_mb | MB | 1 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 5977) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5978) rss_mb | MB | 1 | 13.793 | 13.793 | 13.793 | 13.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 5978) vms_mb | MB | 1 | 207.262 | 207.262 | 207.262 | 207.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6032) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6032) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6033) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6033) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6060) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6060) rss_mb | MB | 3 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6060) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6060) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gate2.py (PID 6062) CPU | percent | 2 | 162.985 | 153.970 | 172.001 | 172.001 | 3.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gate2.py (PID 6062) rss_mb | MB | 3 | 1103.363 | 95.316 | 2023.664 | 95.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gate2.py (PID 6062) main thread run-queue wait | percent | 2 | 54.800 | 36.494 | 73.106 | 73.106 | 1.102684 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gate2.py (PID 6062) vms_mb | MB | 3 | 1417.315 | 316.012 | 2244.527 | 316.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6077) rss_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6077) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — read.py (PID 6079) rss_mb | MB | 1 | 23.859 | 23.859 | 23.859 | 23.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — read.py (PID 6079) vms_mb | MB | 1 | 215.684 | 215.684 | 215.684 | 215.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6094) rss_mb | MB | 1 | 2.652 | 2.652 | 2.652 | 2.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6094) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cal.py (PID 6096) rss_mb | MB | 1 | 263.719 | 263.719 | 263.719 | 263.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cal.py (PID 6096) vms_mb | MB | 1 | 840.582 | 840.582 | 840.582 | 840.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6108) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6108) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6109) rss_mb | MB | 1 | 15.867 | 15.867 | 15.867 | 15.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6109) vms_mb | MB | 1 | 20.527 | 20.527 | 20.527 | 20.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6112) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6112) rss_mb | MB | 8 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6112) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6112) vms_mb | MB | 8 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cand.py (PID 6114) CPU | percent | 7 | 99.206 | 98.205 | 100.338 | 99.374 | 6.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cand.py (PID 6114) rss_mb | MB | 8 | 2032.082 | 1819.508 | 2062.449 | 2062.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cand.py (PID 6114) main thread run-queue wait | percent | 7 | 0.013 | 0.005 | 0.046 | 0.006 | 0.000935 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — cand.py (PID 6114) vms_mb | MB | 8 | 2244.009 | 2176.645 | 2253.918 | 2253.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6135) rss_mb | MB | 1 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6135) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — md.py (PID 6137) rss_mb | MB | 1 | 23.840 | 23.840 | 23.840 | 23.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — md.py (PID 6137) vms_mb | MB | 1 | 215.656 | 215.656 | 215.656 | 215.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6161) rss_mb | MB | 1 | 2.789 | 2.789 | 2.789 | 2.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6161) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tok.py (PID 6164) rss_mb | MB | 1 | 130.445 | 130.445 | 130.445 | 130.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tok.py (PID 6164) vms_mb | MB | 1 | 135.340 | 135.340 | 135.340 | 135.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 6165) rss_mb | MB | 1 | 1.141 | 1.141 | 1.141 | 1.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — head (PID 6165) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6180) rss_mb | MB | 1 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6180) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pos.py (PID 6182) rss_mb | MB | 1 | 13.371 | 13.371 | 13.371 | 13.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pos.py (PID 6182) vms_mb | MB | 1 | 207.219 | 207.219 | 207.219 | 207.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6217) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6217) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6218) rss_mb | MB | 1 | 20.391 | 20.391 | 20.391 | 20.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6218) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6228) rss_mb | MB | 1 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6228) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6229) rss_mb | MB | 1 | 9.145 | 9.145 | 9.145 | 9.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6229) vms_mb | MB | 1 | 13.254 | 13.254 | 13.254 | 13.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6275) rss_mb | MB | 1 | 1.605 | 1.605 | 1.605 | 1.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6275) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6276) rss_mb | MB | 1 | 20.609 | 20.609 | 20.609 | 20.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6276) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6295) rss_mb | MB | 1 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6295) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — xfer.py (PID 6297) rss_mb | MB | 1 | 12.992 | 12.992 | 12.992 | 12.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — xfer.py (PID 6297) vms_mb | MB | 1 | 207.055 | 207.055 | 207.055 | 207.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6313) rss_mb | MB | 1 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6313) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — wr.py (PID 6316) rss_mb | MB | 1 | 17.648 | 17.648 | 17.648 | 17.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — wr.py (PID 6316) vms_mb | MB | 1 | 209.781 | 209.781 | 209.781 | 209.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6329) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6329) rss_mb | MB | 5 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6329) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6329) vms_mb | MB | 5 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — lg.py (PID 6331) CPU | percent | 4 | 156.099 | 116.240 | 171.975 | 171.117 | 6.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — lg.py (PID 6331) rss_mb | MB | 5 | 1061.796 | 42.363 | 1438.234 | 1438.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — lg.py (PID 6331) main thread run-queue wait | percent | 4 | 42.864 | 3.377 | 61.131 | 56.127 | 1.727436 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — lg.py (PID 6331) vms_mb | MB | 5 | 1282.205 | 252.621 | 1660.859 | 1660.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6335) rss_mb | MB | 1 | 1.488 | 1.488 | 1.488 | 1.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6335) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6336) rss_mb | MB | 1 | 18.086 | 18.086 | 18.086 | 18.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6336) vms_mb | MB | 1 | 24.098 | 24.098 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6346) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6346) rss_mb | MB | 5 | 2.867 | 2.867 | 2.867 | 2.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6346) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6346) vms_mb | MB | 5 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — heads.py (PID 6348) CPU | percent | 4 | 151.667 | 124.980 | 162.552 | 159.141 | 6.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — heads.py (PID 6348) rss_mb | MB | 5 | 1601.947 | 23.926 | 1998.586 | 1998.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — heads.py (PID 6348) main thread run-queue wait | percent | 4 | 51.629 | 20.572 | 63.596 | 63.596 | 2.083405 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — heads.py (PID 6348) vms_mb | MB | 5 | 1818.495 | 215.754 | 2221.180 | 2221.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6377) rss_mb | MB | 1 | 1.387 | 1.387 | 1.387 | 1.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6377) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6378) rss_mb | MB | 1 | 21.402 | 21.402 | 21.402 | 21.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6378) vms_mb | MB | 1 | 26.680 | 26.680 | 26.680 | 26.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6395) rss_mb | MB | 1 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6395) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — att.py (PID 6397) rss_mb | MB | 1 | 23.812 | 23.812 | 23.812 | 23.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — att.py (PID 6397) vms_mb | MB | 1 | 215.816 | 215.816 | 215.816 | 215.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6401) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6401) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6402) rss_mb | MB | 1 | 15.809 | 15.809 | 15.809 | 15.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6402) vms_mb | MB | 1 | 20.461 | 20.461 | 20.461 | 20.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6411) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6411) rss_mb | MB | 2 | 3.035 | 3.035 | 3.035 | 3.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6411) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6411) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 6413) CPU | percent | 1 | 81.445 | 81.445 | 81.445 | 81.445 | 0.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 6413) rss_mb | MB | 2 | 104.752 | 19.090 | 190.414 | 190.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 6413) main thread run-queue wait | percent | 1 | 1.978 | 1.978 | 1.978 | 1.978 | 0.019914 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 6413) vms_mb | MB | 2 | 297.398 | 211.434 | 383.363 | 383.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6424) rss_mb | MB | 1 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6424) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6425) rss_mb | MB | 1 | 20.281 | 20.281 | 20.281 | 20.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6425) vms_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6429) rss_mb | MB | 1 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6429) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 6431) rss_mb | MB | 1 | 197.113 | 197.113 | 197.113 | 197.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 6431) vms_mb | MB | 1 | 390.133 | 390.133 | 390.133 | 390.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 6432) rss_mb | MB | 1 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 6432) vms_mb | MB | 1 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6446) rss_mb | MB | 1 | 2.875 | 2.875 | 2.875 | 2.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6446) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6447) rss_mb | MB | 1 | 135.340 | 135.340 | 135.340 | 135.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6447) vms_mb | MB | 1 | 139.254 | 139.254 | 139.254 | 139.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6471) rss_mb | MB | 1 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6471) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6472) rss_mb | MB | 1 | 9.789 | 9.789 | 9.789 | 9.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6472) vms_mb | MB | 1 | 13.617 | 13.617 | 13.617 | 13.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6489) rss_mb | MB | 1 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6489) vms_mb | MB | 1 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — att2.py (PID 6491) rss_mb | MB | 1 | 21.836 | 21.836 | 21.836 | 21.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — att2.py (PID 6491) vms_mb | MB | 1 | 213.934 | 213.934 | 213.934 | 213.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6500) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6500) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6501) rss_mb | MB | 1 | 5.348 | 5.348 | 5.348 | 5.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6501) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6502) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6502) rss_mb | MB | 7 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6502) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6502) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — att2.py (PID 6505) CPU | percent | 6 | 76.182 | 72.487 | 77.499 | 76.502 | 4.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — att2.py (PID 6505) rss_mb | MB | 7 | 196.565 | 182.844 | 214.902 | 214.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — att2.py (PID 6505) main thread run-queue wait | percent | 6 | 0.135 | 0.030 | 0.587 | 0.039 | 0.008168 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — att2.py (PID 6505) vms_mb | MB | 7 | 389.289 | 375.574 | 407.574 | 407.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6517) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6517) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6518) rss_mb | MB | 1 | 21.609 | 21.609 | 21.609 | 21.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6518) vms_mb | MB | 1 | 26.906 | 26.906 | 26.906 | 26.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6520) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6520) rss_mb | MB | 7 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6520) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6520) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — design.py (PID 6522) CPU | percent | 6 | 77.135 | 75.417 | 78.546 | 78.546 | 4.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — design.py (PID 6522) rss_mb | MB | 7 | 258.530 | 182.867 | 336.121 | 336.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — design.py (PID 6522) main thread run-queue wait | percent | 6 | 0.038 | 0.031 | 0.054 | 0.041 | 0.002306 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — design.py (PID 6522) vms_mb | MB | 7 | 464.467 | 375.590 | 559.582 | 559.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6539) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6539) rss_mb | MB | 6 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6539) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6539) vms_mb | MB | 6 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — margin.py (PID 6541) CPU | percent | 5 | 158.027 | 94.381 | 175.265 | 175.265 | 7.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — margin.py (PID 6541) rss_mb | MB | 6 | 1070.506 | 18.879 | 1317.945 | 1317.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — margin.py (PID 6541) main thread run-queue wait | percent | 5 | 49.360 | 2.079 | 73.884 | 73.884 | 2.493580 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — margin.py (PID 6541) vms_mb | MB | 6 | 1283.199 | 211.426 | 1540.531 | 1540.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6565) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6565) rss_mb | MB | 4 | 2.871 | 2.871 | 2.871 | 2.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6565) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6565) vms_mb | MB | 4 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — readans.py (PID 6567) CPU | percent | 3 | 82.066 | 74.491 | 86.397 | 74.491 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — readans.py (PID 6567) rss_mb | MB | 4 | 221.002 | 127.051 | 294.727 | 231.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — readans.py (PID 6567) main thread run-queue wait | percent | 3 | 6.476 | 0.068 | 9.929 | 0.068 | 0.195745 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — readans.py (PID 6567) vms_mb | MB | 4 | 587.485 | 350.047 | 1058.801 | 1058.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6581) rss_mb | MB | 1 | 1.605 | 1.605 | 1.605 | 1.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6581) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6582) rss_mb | MB | 1 | 9.250 | 9.250 | 9.250 | 9.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6582) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6584) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6584) rss_mb | MB | 12 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6584) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6584) vms_mb | MB | 12 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve.py (PID 6586) CPU | percent | 11 | 78.926 | 73.471 | 86.485 | 78.445 | 8.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve.py (PID 6586) rss_mb | MB | 12 | 212.306 | 203.609 | 220.445 | 220.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve.py (PID 6586) main thread run-queue wait | percent | 11 | 0.824 | 0.025 | 3.414 | 0.036 | 0.091252 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve.py (PID 6586) vms_mb | MB | 12 | 432.280 | 397.613 | 445.613 | 445.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6603) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6603) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6604) rss_mb | MB | 1 | 20.320 | 20.320 | 20.320 | 20.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6604) vms_mb | MB | 1 | 25.117 | 25.117 | 25.117 | 25.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6632) rss_mb | MB | 1 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6632) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6634) rss_mb | MB | 1 | 91.215 | 91.215 | 91.215 | 91.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6634) vms_mb | MB | 1 | 96.215 | 96.215 | 96.215 | 96.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6649) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6649) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6650) rss_mb | MB | 1 | 14.641 | 14.641 | 14.641 | 14.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6650) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6659) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6659) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6660) rss_mb | MB | 1 | 7.863 | 7.863 | 7.863 | 7.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6660) vms_mb | MB | 1 | 12.926 | 12.926 | 12.926 | 12.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6662) rss_mb | MB | 1 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6662) vms_mb | MB | 1 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — checkPR.py (PID 6664) rss_mb | MB | 1 | 196.680 | 196.680 | 196.680 | 196.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — checkPR.py (PID 6664) vms_mb | MB | 1 | 390.211 | 390.211 | 390.211 | 390.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6679) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6679) rss_mb | MB | 14 | 2.961 | 2.961 | 2.961 | 2.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6679) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6679) vms_mb | MB | 14 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve2.py (PID 6681) CPU | percent | 13 | 79.542 | 73.469 | 91.345 | 76.510 | 10.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve2.py (PID 6681) rss_mb | MB | 14 | 205.740 | 10.938 | 221.422 | 221.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve2.py (PID 6681) main thread run-queue wait | percent | 13 | 1.953 | 0.030 | 11.821 | 0.030 | 0.255622 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve2.py (PID 6681) vms_mb | MB | 14 | 413.534 | 55.191 | 446.664 | 446.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6696) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6696) rss_mb | MB | 4 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6696) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6696) vms_mb | MB | 4 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dlog.py (PID 6698) CPU | percent | 3 | 103.713 | 92.400 | 118.342 | 118.342 | 3.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dlog.py (PID 6698) rss_mb | MB | 4 | 2243.391 | 13.496 | 3379.625 | 3379.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dlog.py (PID 6698) main thread run-queue wait | percent | 3 | 2.809 | 0.021 | 7.733 | 7.733 | 0.084746 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dlog.py (PID 6698) vms_mb | MB | 4 | 2890.770 | 207.215 | 4303.621 | 4303.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6702) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6702) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6703) rss_mb | MB | 1 | 19.207 | 19.207 | 19.207 | 19.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6703) vms_mb | MB | 1 | 24.734 | 24.734 | 24.734 | 24.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6712) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6712) rss_mb | MB | 2 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6712) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6712) vms_mb | MB | 2 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — reads2.py (PID 6714) CPU | percent | 1 | 120.302 | 120.302 | 120.302 | 120.302 | 1.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — reads2.py (PID 6714) rss_mb | MB | 2 | 30.920 | 9.668 | 52.172 | 52.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — reads2.py (PID 6714) main thread run-queue wait | percent | 1 | 41.246 | 41.246 | 41.246 | 41.246 | 0.414852 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — reads2.py (PID 6714) vms_mb | MB | 2 | 144.336 | 13.605 | 275.066 | 275.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6724) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6724) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6726) rss_mb | MB | 1 | 20.578 | 20.578 | 20.578 | 20.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6726) vms_mb | MB | 1 | 25.504 | 25.504 | 25.504 | 25.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6728) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6728) rss_mb | MB | 4 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6728) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6728) vms_mb | MB | 4 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — scalechk.py (PID 6730) CPU | percent | 3 | 73.808 | 73.473 | 74.453 | 73.499 | 2.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — scalechk.py (PID 6730) rss_mb | MB | 4 | 211.564 | 182.305 | 221.359 | 221.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — scalechk.py (PID 6730) main thread run-queue wait | percent | 3 | 0.043 | 0.035 | 0.050 | 0.035 | 0.001312 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — scalechk.py (PID 6730) vms_mb | MB | 4 | 405.655 | 375.395 | 415.742 | 415.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6731) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6731) rss_mb | MB | 4 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6731) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6731) vms_mb | MB | 4 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6732) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6732) rss_mb | MB | 4 | 6.680 | 6.680 | 6.680 | 6.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6732) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 6732) vms_mb | MB | 4 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6736) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6736) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6737) rss_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6737) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6759) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6759) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6760) rss_mb | MB | 1 | 15.605 | 15.605 | 15.605 | 15.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6760) vms_mb | MB | 1 | 20.527 | 20.527 | 20.527 | 20.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6773) rss_mb | MB | 1 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6773) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6774) rss_mb | MB | 1 | 20.547 | 20.547 | 20.547 | 20.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6774) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6789) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6789) rss_mb | MB | 11 | 2.965 | 2.965 | 2.965 | 2.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6789) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6789) vms_mb | MB | 11 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — final_solve.py (PID 6791) CPU | percent | 10 | 78.510 | 74.753 | 85.380 | 74.753 | 7.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — final_solve.py (PID 6791) rss_mb | MB | 11 | 202.654 | 26.906 | 221.699 | 221.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — final_solve.py (PID 6791) main thread run-queue wait | percent | 10 | 1.089 | 0.030 | 5.632 | 0.044 | 0.109696 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — final_solve.py (PID 6791) vms_mb | MB | 11 | 414.229 | 228.184 | 446.469 | 446.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6808) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6808) rss_mb | MB | 5 | 2.926 | 2.926 | 2.926 | 2.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6808) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6808) vms_mb | MB | 5 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 6810) CPU | percent | 4 | 165.479 | 151.101 | 171.674 | 168.079 | 6.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 6810) rss_mb | MB | 5 | 76.959 | 13.668 | 123.227 | 109.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 6810) main thread run-queue wait | percent | 4 | 52.512 | 40.403 | 69.774 | 69.774 | 2.113374 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 6810) vms_mb | MB | 5 | 289.374 | 207.234 | 340.180 | 326.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6814) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6814) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6815) rss_mb | MB | 1 | 2.777 | 2.777 | 2.777 | 2.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6815) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6821) rss_mb | MB | 1 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6821) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6823) rss_mb | MB | 1 | 13.246 | 13.246 | 13.246 | 13.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6823) vms_mb | MB | 1 | 207.137 | 207.137 | 207.137 | 207.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6841) rss_mb | MB | 1 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6841) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6842) rss_mb | MB | 1 | 18.516 | 18.516 | 18.516 | 18.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6842) vms_mb | MB | 1 | 24.148 | 24.148 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6888) rss_mb | MB | 1 | 318.930 | 318.930 | 318.930 | 318.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6888) vms_mb | MB | 1 | 5499.879 | 5499.879 | 5499.879 | 5499.879 | n/a | n/a |
| docker commit (PID 6926) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6926) io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6926) io write MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6926) rss_mb | MB | 21 | 30.445 | 30.445 | 30.445 | 30.445 | n/a | n/a |
| docker commit (PID 6926) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6926) vms_mb | MB | 21 | 1771.516 | 1771.516 | 1771.516 | 1771.516 | n/a | n/a |
| docker stop (PID 6975) rss_mb | MB | 1 | 17.090 | 17.090 | 17.090 | 17.090 | n/a | n/a |
| docker stop (PID 6975) vms_mb | MB | 1 | 1625.598 | 1625.598 | 1625.598 | 1625.598 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 CPU | percent | 1978 | 44.382 | 0.000 | 203.265 | 0.042 | 883.519617 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1978 | 1.310 | 0.000 | 50.354 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1978 | 1.698 | 0.000 | 70.421 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_full_pct | percent of wall time stalled | 1978 | 0.058 | 0.000 | 38.952 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_some_pct | percent of wall time stalled | 1978 | 0.059 | 0.000 | 38.952 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io read MB/s | MB/s | 1978 | 0.120 | 0.000 | 63.030 | 0.000 | 239.617188 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io write MB/s | MB/s | 1978 | 0.010 | 0.000 | 17.136 | 0.000 | 20.781250 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory | MB | 1979 | 563.423 | 14.348 | 3859.105 | 308.305 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1978 | 0.024 | 0.000 | 13.954 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1978 | 0.024 | 0.000 | 13.956 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net rx MB/s | MB/s | 1978 | 0.004 | 0.000 | 8.401 | 0.000 | 8.501284 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net tx MB/s | MB/s | 1978 | 0.000 | 0.000 | 0.008 | 0.000 | 0.049273 MB | n/a |
| workload total CPU | percent | 1978 | 6.517 | 1.663 | 104.919 | 7.338 | 129.908109 CPU seconds | n/a |
| workload total memory | MB | 1979 | 9381.770 | 8884.555 | 9730.188 | 9187.945 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
