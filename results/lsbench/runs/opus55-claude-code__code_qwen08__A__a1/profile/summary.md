# agprof summary

- Duration: **1954.088 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **71 calls**, 71 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1104.609 s total wait
- Tools: **71/71 completed**, 1 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **184498** at 1.949 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1954009.609 / 1954009.609 ms |
| LLM latency p50 / p95 | 13081.824 / 45145.802 ms |
| LLM TTFT p50 / p95 | 5800.424 / 25797.758 ms |
| LLM input / output tokens | 284 / 124301 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 71 total, 71 succeeded, 0 failed, 0 interrupted |
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
| Bash | 46/46 | 45 | 1 | 0 | n/a | n/a |
| ToolSearch | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 5/5 | 5 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 6/6 | 6 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 6/6 | 6 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.013% | 164.585% | 98.918 s | 9010.863 MB | 11081.898 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 11215 |  | 1921 | 2.502% | 162.912% | 50.080 s | 3258.261 MB | 4867.016 MB | 16556.834 MB | 18112.773 MB | 163.796875 MB | 3203.285156 MB |
| vllm | 11220 |  | 1921 | 0.196% | 8.923% | 3.810 s | 1641.568 MB | 1804.000 MB | 11041.170 MB | 11044.629 MB | 0.031250 MB | 0.031250 MB |
| docker | 11510 |  | 1 | n/a% | n/a% | n/a s | 30.375 MB | 30.375 MB | 1843.512 MB | 1843.512 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 11255 |  | 1921 | 2.302% | 63.455% | 44.790 s | 2242.590 MB | 2324.828 MB | 21204.084 MB | 21204.148 MB | 0.152344 MB | 0.015625 MB |
| lsb_grid_worker | 4781 |  | 1921 | 0.000% | 0.000% | 0.000 s | 2.938 MB | 2.938 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 11254 |  | 1921 | 0.000% | 0.000% | 0.000 s | 12.199 MB | 12.199 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 11476 | sandbox_agent_lsb-claude_code_0000_0000 | 1919 | 0.002% | 0.995% | 0.030 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 11600 | sandbox_agent_lsb-claude_code_0000_0000 | 1919 | 32.643% | 104.323% | 636.560 s | 103.326 MB | 109.859 MB | 971.453 MB | 975.469 MB | n/a MB | n/a MB |
| tail | 11508 | sandbox_agent_lsb-claude_code_0000_0000 | 1919 | 0.003% | 0.995% | 0.050 s | 1.430 MB | 1.430 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 11606 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 71.133% | 71.133% | 0.720 s | 54.791 MB | 68.035 MB | 62.799 MB | 76.793 MB | n/a MB | n/a MB |
| claude | 11619 | sandbox_agent_lsb-claude_code_0000_0000 | 1882 | 3.466% | 70.542% | 66.170 s | 286.868 MB | 342.055 MB | 5499.800 MB | 5499.816 MB | n/a MB | n/a MB |
| python3 | 11718 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.566 MB | 7.566 MB | 11.926 MB | 11.926 MB | n/a MB | n/a MB |
| sh | 11717 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 11771 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 1.986% | 1.986% | 0.020 s | 12.352 MB | 12.477 MB | 15.812 MB | 15.848 MB | n/a MB | n/a MB |
| bash | 11770 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.672 MB | 2.672 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 11779 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.695 MB | 8.695 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python | 11817 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.570 MB | 7.570 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 11861 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.754 MB | 5.754 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| tail | 11862 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.211 MB | 1.211 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 11859 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.676 MB | 2.676 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 11896 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.664 MB | 10.664 MB | 15.203 MB | 15.203 MB | n/a MB | n/a MB |
| sh | 11895 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11928 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.934 MB | 21.934 MB | 26.918 MB | 26.918 MB | n/a MB | n/a MB |
| sh | 11927 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 11956 | sandbox_agent_lsb-claude_code_0000_0000 | 12 | 0.361% | 2.978% | 0.040 s | 12.434 MB | 12.434 MB | 15.777 MB | 15.777 MB | n/a MB | n/a MB |
| python | 11964 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 99.915% | 100.494% | 4.020 s | 8.250 MB | 8.250 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| bash | 11955 | sandbox_agent_lsb-claude_code_0000_0000 | 18 | 0.000% | 0.000% | 0.000 s | 2.855 MB | 2.855 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| tail | 11957 | sandbox_agent_lsb-claude_code_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python | 11965 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 99.966% | 100.487% | 4.020 s | 8.520 MB | 8.520 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python | 11975 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.488 MB | 7.488 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 12014 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.383 MB | 4.383 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python | 12023 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.398% | 1.988% | 0.020 s | 12.172 MB | 12.172 MB | 15.691 MB | 15.691 MB | n/a MB | n/a MB |
| tail | 12024 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python | 12028 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 99.888% | 100.479% | 4.020 s | 8.500 MB | 8.500 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python | 12053 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.441 MB | 0.441 MB | 9.500 MB | 9.500 MB | n/a MB | n/a MB |
| python3 | 12077 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.414 MB | 21.414 MB | 27.094 MB | 27.094 MB | n/a MB | n/a MB |
| sh | 12076 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.547 MB | 1.547 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 12122 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.730 MB | 8.730 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| bash | 12103 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.809 MB | 2.809 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 12104 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 3.967% | 3.967% | 0.040 s | 12.461 MB | 12.523 MB | 15.875 MB | 15.875 MB | n/a MB | n/a MB |
| python | 12161 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.566 MB | 7.566 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| tail | 12168 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.211 MB | 1.211 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python | 12167 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.320 MB | 12.320 MB | 15.723 MB | 15.723 MB | n/a MB | n/a MB |
| python | 12198 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.445 MB | 7.445 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| bash | 12257 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.734 MB | 2.734 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 12258 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 85.934 MB | 85.934 MB | 313.289 MB | 313.289 MB | n/a MB | n/a MB |
| python | 12270 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 82.460% | 84.414% | 2.490 s | 651.824 MB | 904.496 MB | 865.848 MB | 1192.438 MB | n/a MB | n/a MB |
| bash | 12269 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.879 MB | 2.879 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 12282 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.684 MB | 21.684 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 12281 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.555 MB | 1.555 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12342 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.078 MB | 19.078 MB | 24.605 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 12341 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 12394 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.730 MB | 2.730 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 12397 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.570 MB | 21.570 MB | 213.691 MB | 213.691 MB | n/a MB | n/a MB |
| python | 12412 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 459.391 MB | 459.391 MB | 786.219 MB | 786.219 MB | n/a MB | n/a MB |
| bash | 12410 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.930 MB | 2.930 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 12417 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.086 MB | 14.086 MB | 19.836 MB | 19.836 MB | n/a MB | n/a MB |
| sh | 12416 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12436 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.773 MB | 21.773 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 12435 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.555 MB | 1.555 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 12456 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12457 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.781 MB | 21.781 MB | 26.906 MB | 26.906 MB | n/a MB | n/a MB |
| bash | 12468 | sandbox_agent_lsb-claude_code_0000_0000 | 168 | 0.000% | 0.000% | 0.000 s | 3.031 MB | 3.031 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 12470 | sandbox_agent_lsb-claude_code_0000_0000 | 168 | 168.518% | 183.870% | 284.070 s | 1102.848 MB | 1109.273 MB | 1326.400 MB | 1333.105 MB | n/a MB | n/a MB |
| sh | 12502 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12503 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 5.463% | 5.963% | 0.110 s | 13.323 MB | 18.004 MB | 18.697 MB | 24.148 MB | n/a MB | n/a MB |
| sh | 12513 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.555 MB | 1.555 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12514 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.977% | 5.966% | 0.120 s | 13.714 MB | 19.391 MB | 18.443 MB | 24.605 MB | n/a MB | n/a MB |
| sleep | 12517 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 12516 | sandbox_agent_lsb-claude_code_0000_0000 | 401 | 0.007% | 0.995% | 0.030 s | 2.727 MB | 2.727 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 12518 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12519 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12520 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12522 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12523 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12524 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12525 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12526 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12527 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12529 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12530 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12532 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12533 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12534 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12535 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 12536 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.193 MB | 1.258 MB | 2.748 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 12537 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.273 MB | 1.273 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12538 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12539 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.273 MB | 1.273 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12540 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12541 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12543 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12544 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12546 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12547 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12548 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12549 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12550 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12551 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12552 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12553 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12554 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12556 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12557 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12558 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12559 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12560 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12561 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12562 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12564 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12583 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12585 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12586 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12587 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12588 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12589 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12590 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12591 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12592 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12593 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12594 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12596 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12597 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.281 MB | 1.281 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12599 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12600 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12601 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12602 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12603 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12604 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12605 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12606 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12608 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12609 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12610 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 12615 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.162 MB | 1.219 MB | 2.748 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 12617 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12618 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12619 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12620 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12621 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12622 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12624 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12625 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12626 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12627 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12629 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12630 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12631 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12632 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.273 MB | 1.273 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 12638 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| python | 12662 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 95.424% | 95.424% | 0.960 s | 1280.521 MB | 2505.254 MB | 1743.682 MB | 3240.066 MB | n/a MB | n/a MB |
| bash | 12660 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.992 MB | 2.992 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 12680 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12681 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.211 MB | 21.211 MB | 25.762 MB | 25.762 MB | n/a MB | n/a MB |
| python | 12717 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 2.973% | 2.973% | 0.030 s | 12.336 MB | 12.336 MB | 15.777 MB | 15.777 MB | n/a MB | n/a MB |
| tail | 12718 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 12716 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.758 MB | 2.758 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 12724 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.383 MB | 2.383 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| python | 12761 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.613 MB | 7.613 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 12783 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.395 MB | 12.395 MB | 15.699 MB | 15.699 MB | n/a MB | n/a MB |
| tail | 12784 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.180 MB | 1.180 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python | 12798 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.715 MB | 7.715 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 12823 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.887 MB | 18.887 MB | 24.605 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 12822 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.512 MB | 1.512 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12874 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.645 MB | 18.645 MB | 24.254 MB | 24.254 MB | n/a MB | n/a MB |
| sh | 12873 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 12885 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| bash | 12897 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 12899 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 78.910% | 102.229% | 3.970 s | 602.886 MB | 1926.055 MB | 909.305 MB | 2765.102 MB | n/a MB | n/a MB |
| sh | 12929 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12930 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.727 MB | 15.727 MB | 20.461 MB | 20.461 MB | n/a MB | n/a MB |
| sh | 12964 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12965 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.539 MB | 15.539 MB | 20.461 MB | 20.461 MB | n/a MB | n/a MB |
| python | 13011 | sandbox_agent_lsb-claude_code_0000_0000 | 21 | 68.450% | 105.699% | 13.960 s | 1889.724 MB | 3885.531 MB | 2170.851 MB | 4129.852 MB | n/a MB | n/a MB |
| bash | 13009 | sandbox_agent_lsb-claude_code_0000_0000 | 21 | 0.000% | 0.000% | 0.000 s | 2.848 MB | 2.848 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| claude | 13015 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.109 MB | 228.109 MB | 5499.816 MB | 5499.816 MB | n/a MB | n/a MB |
| bash | 13048 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.832 MB | 2.832 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 13049 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.098 MB | 22.098 MB | 214.012 MB | 214.012 MB | n/a MB | n/a MB |
| sh | 13065 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13066 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.918 MB | 17.918 MB | 23.098 MB | 23.098 MB | n/a MB | n/a MB |
| python3 | 13074 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.801 MB | 21.801 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| sh | 13073 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 13086 | sandbox_agent_lsb-claude_code_0000_0000 | 13 | 69.906% | 93.477% | 8.700 s | 3168.553 MB | 4931.395 MB | 3445.796 MB | 5124.789 MB | n/a MB | n/a MB |
| bash | 13084 | sandbox_agent_lsb-claude_code_0000_0000 | 13 | 0.000% | 0.000% | 0.000 s | 2.727 MB | 2.727 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 13091 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.137 MB | 7.137 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 13090 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.551 MB | 1.551 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 13101 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.848 MB | 2.848 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 13102 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1653.789 MB | 1653.789 MB | 2731.027 MB | 2731.027 MB | n/a MB | n/a MB |
| bash | 13132 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.848 MB | 2.848 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python | 13133 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 72.931% | 98.005% | 6.680 s | 2738.220 MB | 4965.152 MB | 3010.378 MB | 5333.852 MB | n/a MB | n/a MB |
| sh | 13173 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13174 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.316 MB | 19.316 MB | 24.730 MB | 24.730 MB | n/a MB | n/a MB |
| python | 13188 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 73.190% | 95.073% | 10.450 s | 2438.305 MB | 4891.656 MB | 2714.917 MB | 5160.594 MB | n/a MB | n/a MB |
| bash | 13186 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 2.895 MB | 2.895 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 13194 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.391 MB | 20.391 MB | 25.117 MB | 25.117 MB | n/a MB | n/a MB |
| sh | 13193 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 13206 | sandbox_agent_lsb-claude_code_0000_0000 | 16 | 72.693% | 92.218% | 11.040 s | 2058.321 MB | 4341.625 MB | 2345.203 MB | 4700.801 MB | n/a MB | n/a MB |
| bash | 13203 | sandbox_agent_lsb-claude_code_0000_0000 | 16 | 0.000% | 0.000% | 0.000 s | 2.695 MB | 2.695 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| docker | 13247 |  | 3 | 0.000% | 0.000% | 0.000 s | 29.217 MB | 29.301 MB | 1771.203 MB | 1771.203 MB | 0.000000 MB | 0.000000 MB |
| docker | 13257 |  | 4 | 0.000% | 0.000% | 0.000 s | 30.836 MB | 30.836 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |
| docker | 13274 |  | 25 | 0.000% | 0.000% | 0.000 s | 30.039 MB | 30.039 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |
| docker | 13344 |  | 1 | n/a% | n/a% | n/a s | 30.410 MB | 30.410 MB | 1843.020 MB | 1843.020 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.992% | 100.000% | 11888.407 MB | 12304.000 MB | 31.034 W | 74.592 W | 60575.478 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-claude_code_0000_0000 | 56.435% | 213.918% | 1098.106 s | 696.831 MB | 5557.449 MB | 617.296875 MB | 109.046875 MB | 8.499495 MB | 0.051053 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 11362 | 1954.023 | interrupted |
| harness:retire | -1 | 0.201 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 1/1 | 0 | 0 | 1954.014 | 0.000 | 1954.014 | 617.297 | 1954013.840 | 1954013.840 | 1954013.840 |
| run:write_lora_adapter | 1/1 | 0 | 0 | 1954.010 | n/a | n/a | 617.297 | 1954009.609 | 1954009.609 | 1954009.609 |
| engine:execute | 1/1 | 0 | 0 | 1954.008 | 2.948 | 1951.026 | 617.297 | 1954007.543 | 1954007.543 | 1954007.543 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1915.353 | 0.005 | 1915.348 | 591.399 | 1915353.292 | 1915353.292 | 1915353.292 |
| harness:await_cli | 1/1 | 0 | 0 | 1911.716 | n/a | n/a | 475.840 | 1911715.635 | 1911715.635 | 1911715.635 |
| llm:attempt | 71/71 | 0 | 0 | 1104.609 | 3.421 | 1101.175 | 89.209 | 15557.878 | 13081.824 | 45145.802 |
| tool:Bash | 46/46 | 1 | 0 | 661.429 | n/a | n/a | 353.157 | 14378.900 | 476.103 | 22236.736 |
| tool:mcp__agency__generate | 5/5 | 0 | 0 | 51.306 | n/a | n/a | 2.337 | 10261.252 | 10195.039 | 12614.093 |
| run:container_call | 13/13 | 0 | 0 | 33.973 | 0.002 | 33.971 | 0.530 | 2613.319 | 63.261 | 12378.799 |
| teardown:commit | 1/1 | 0 | 0 | 33.354 | 0.004 | 33.350 | 0.530 | 33354.271 | 33354.271 | 33354.271 |
| sandbox:commit | 1/1 | 0 | 0 | 32.412 | 0.002 | 32.410 | 0.530 | 32412.254 | 32412.254 | 32412.254 |
| checkpoint.total | 1/1 | 0 | 0 | 32.412 | 0.002 | 32.410 | 0.530 | 32412.093 | 32412.093 | 32412.093 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 32.412 | 0.002 | 32.410 | 0.530 | 32411.959 | 32411.959 | 32411.959 |
| tool:mcp__agency__trace | 6/6 | 0 | 0 | 24.758 | n/a | n/a | 0.128 | 4126.350 | 2998.912 | 7493.022 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 20.404 | n/a | n/a | 0.216 | 20403.583 | 20403.583 | 20403.583 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.556 | 1.148 | 3.407 | 22.483 | 4555.503 | 4555.503 | 4555.503 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.555 | 1.148 | 3.407 | 22.471 | 4555.215 | 4555.215 | 4555.215 |
| tool:mcp__agency__inspect_module_inputs | 2/2 | 0 | 0 | 3.407 | n/a | n/a | 0.265 | 1703.643 | 1703.643 | 2496.232 |
| tool:mcp__agency__patch | 6/6 | 0 | 0 | 2.887 | n/a | n/a | 0.202 | 481.240 | 446.735 | 621.690 |
| tool:mcp__agency__token_stats | 1/1 | 0 | 0 | 2.773 | n/a | n/a | 0.000 | 2773.065 | 2773.065 | 2773.065 |
| harness:startup_ready | 1/1 | 0 | 0 | 2.015 | n/a | n/a | 44.847 | 2015.387 | 2015.387 | 2015.387 |
| tool:mcp__agency__logit_lens | 1/1 | 0 | 0 | 1.859 | n/a | n/a | 0.307 | 1858.899 | 1858.899 | 1858.899 |
| syscall:sendto | 570/570 | 0 | 0 | 1.730 | n/a | n/a | 1.436 | 3.035 | 2.125 | 6.095 |
| syscall:execve | 914/914 | 0 | 0 | 1.370 | n/a | n/a | 1.027 | 1.499 | 1.257 | 2.385 |
| syscall:connect | 196/196 | 0 | 0 | 1.095 | n/a | n/a | 2.316 | 5.588 | 2.241 | 5.583 |
| sandbox:stop | 1/1 | 0 | 0 | 0.942 | 0.001 | 0.940 | 0.000 | 941.763 | 941.763 | 941.763 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.811 | n/a | n/a | 0.775 | 811.279 | 811.279 | 811.279 |
| harness:submit | 1/1 | 0 | 0 | 0.610 | n/a | n/a | 5.672 | 609.546 | 609.546 | 609.546 |
| sandbox:start | 1/1 | 0 | 0 | 0.548 | 0.002 | 0.546 | 0.000 | 548.172 | 548.172 | 548.172 |
| runtime.container_create | 1/1 | 0 | 0 | 0.548 | 0.002 | 0.546 | 0.000 | 548.044 | 548.044 | 548.044 |
| sandbox:create | 1/1 | 0 | 0 | 0.416 | 0.245 | 0.171 | 0.000 | 416.105 | 416.105 | 416.105 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 0.312 | n/a | n/a | 0.262 | 312.456 | 312.456 | 312.456 |
| tool:ToolSearch | 1/1 | 0 | 0 | 0.208 | n/a | n/a | 0.446 | 208.156 | 208.156 | 208.156 |
| agency:services_close | 1/1 | 0 | 0 | 0.181 | 0.001 | 0.180 | 0.146 | 180.736 | 180.736 | 180.736 |
| run:detect | 1/1 | 0 | 0 | 0.126 | 0.001 | 0.126 | 0.000 | 126.473 | 126.473 | 126.473 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.032 | 0.000 | 73.023 | 73.023 | 73.023 |
| harness:launch | 1/1 | 0 | 0 | 0.051 | n/a | n/a | 4.079 | 51.243 | 51.243 | 51.243 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.008 | 0.040 | 0.000 | 47.633 | 47.633 | 47.633 |
| harness:snapshot | 1/1 | 0 | 0 | 0.007 | n/a | n/a | 0.129 | 7.425 | 7.425 | 7.425 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.007 | 0.007 | 0.000 | 0.005 | 6.681 | 6.681 | 6.681 |
| syscall:bind | 2/2 | 0 | 0 | 0.002 | n/a | n/a | 0.042 | 1.112 | 1.112 | 1.126 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.241 | 1.241 | 1.241 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.077 | 0.080 | 0.106 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.195 | 0.195 | 0.195 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.051 | 0.051 | 0.051 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1919 | 0.463 | 0.014 | 46.115 | 14.068 | 8.983477 CPU seconds | n/a |
| GPU 0 memory | MB | 1921 | 11888.407 | 11670.000 | 12304.000 | 12138.000 | n/a | n/a |
| GPU 0 power | W | 1921 | 31.034 | 29.240 | 74.592 | 29.318 | n/a | 60575.478 J |
| GPU 0 proc / 11215-782458 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 memory | MB | 1921 | 3190.051 | 3118.000 | 3596.000 | 3430.000 | n/a | n/a |
| GPU 0 proc / 11215-782458 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 estimated power | W | 1428 | 0.993 | 0.000 | 70.989 | 0.000 | n/a | n/a |
| GPU 0 proc / 11215-782458 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 utilization | percent | 1428 | 0.662 | 0.000 | 84.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 11255-784483 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 memory | MB | 1921 | 8216.356 | 8070.000 | 8226.000 | 8226.000 | n/a | n/a |
| GPU 0 proc / 11255-784483 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 estimated power | W | 458 | 7.549 | 0.000 | 73.205 | 0.000 | n/a | n/a |
| GPU 0 proc / 11255-784483 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 utilization | percent | 458 | 10.251 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1921 | 11406.407 | 11188.000 | 11822.000 | 11656.000 | n/a | n/a |
| GPU 0 utilization | percent | 1921 | 2.992 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1921 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1920 | 6.757 | 0.081 | 75.612 | 1.515 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1920 | 15.312 | 0.251 | 53.465 | 6.061 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1920 | 1.151 | 0.000 | 209.865 | 3.344 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1920 | 2.318 | 0.000 | 234.539 | 0.453 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1920 | 1.733 | 0.000 | 88.713 | 48.345 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1920 | 1.790 | 0.000 | 89.199 | 50.571 | n/a | n/a |
| host mem_total_mb | MB | 1921 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1921 | 7636.567 | 6729.762 | 11970.188 | 6729.762 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1920 | 0.817 | 0.000 | 88.422 | 47.346 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1920 | 0.836 | 0.000 | 89.021 | 49.487 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1920 | 0.007 | 0.000 | 8.703 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1920 | 0.018 | 0.000 | 0.827 | 0.000 | n/a | n/a |
| Agency harness — python -m lsbench (PID 11215) CPU | percent | 1920 | 2.502 | 0.000 | 162.912 | 0.000 | 50.080000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 11215) io read MB/s | MB/s | 1920 | 0.025 | 0.000 | 6.687 | 0.240 | 163.796875 MB | n/a |
| Agency harness — python -m lsbench (PID 11215) io write MB/s | MB/s | 1920 | 1.654 | 0.015 | 542.122 | 0.058 | 3203.285156 MB | n/a |
| Agency harness — python -m lsbench (PID 11215) rss_mb | MB | 1921 | 3258.261 | 2588.230 | 4867.016 | 3356.617 | n/a | n/a |
| Agency harness — python -m lsbench (PID 11215) main thread run-queue wait | percent | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 11215) vms_mb | MB | 1921 | 16556.834 | 14243.996 | 18112.773 | 17134.641 | n/a | n/a |
| Python — vllm (PID 11220) CPU | percent | 1920 | 0.196 | 0.000 | 8.923 | 0.000 | 3.810000 CPU seconds | n/a |
| Python — vllm (PID 11220) io read MB/s | MB/s | 1920 | 0.000 | 0.000 | 0.023 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 11220) io write MB/s | MB/s | 1920 | 0.000 | 0.000 | 0.004 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 11220) rss_mb | MB | 1921 | 1641.568 | 510.781 | 1804.000 | 510.781 | n/a | n/a |
| Python — vllm (PID 11220) main thread run-queue wait | percent | 1920 | 0.007 | 0.000 | 0.607 | 0.000 | 0.127460 run-queue seconds | n/a |
| Python — vllm (PID 11220) vms_mb | MB | 1921 | 11041.170 | 10971.609 | 11044.629 | 11044.629 | n/a | n/a |
| Python — python -c (PID 11254) CPU | percent | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 11254) io read MB/s | MB/s | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 11254) io write MB/s | MB/s | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 11254) rss_mb | MB | 1921 | 12.199 | 12.199 | 12.199 | 12.199 | n/a | n/a |
| Python — python -c (PID 11254) main thread run-queue wait | percent | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 11254) vms_mb | MB | 1921 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 11255) CPU | percent | 1920 | 2.302 | 0.000 | 63.455 | 1.984 | 44.790000 CPU seconds | n/a |
| VLLM::EngineCore (PID 11255) io read MB/s | MB/s | 1920 | 0.000 | 0.000 | 0.151 | 0.000 | 0.152344 MB | n/a |
| VLLM::EngineCore (PID 11255) io write MB/s | MB/s | 1920 | 0.000 | 0.000 | 0.008 | 0.000 | 0.015625 MB | n/a |
| VLLM::EngineCore (PID 11255) rss_mb | MB | 1921 | 2242.590 | 1864.137 | 2324.828 | 1864.281 | n/a | n/a |
| VLLM::EngineCore (PID 11255) main thread run-queue wait | percent | 1920 | 0.001 | 0.000 | 0.261 | 0.000 | 0.016409 run-queue seconds | n/a |
| VLLM::EngineCore (PID 11255) vms_mb | MB | 1921 | 21204.084 | 21203.133 | 21204.148 | 21204.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 11476) CPU | percent | 1918 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 11476) rss_mb | MB | 1919 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 11476) main thread run-queue wait | percent | 1918 | 0.003 | 0.000 | 4.573 | 0.000 | 0.067815 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 11476) vms_mb | MB | 1919 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11508) CPU | percent | 1918 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11508) rss_mb | MB | 1919 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11508) main thread run-queue wait | percent | 1918 | 0.003 | 0.000 | 2.752 | 0.000 | 0.052979 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11508) vms_mb | MB | 1919 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| docker exec (PID 11510) rss_mb | MB | 1 | 30.375 | 30.375 | 30.375 | 30.375 | n/a | n/a |
| docker exec (PID 11510) vms_mb | MB | 1 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11600) CPU | percent | 1918 | 32.643 | 0.000 | 104.323 | 0.000 | 636.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11600) rss_mb | MB | 1919 | 103.326 | 2.859 | 109.859 | 103.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11600) main thread run-queue wait | percent | 1918 | 0.000 | 0.000 | 0.028 | 0.000 | 0.000424 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11600) vms_mb | MB | 1919 | 971.453 | 4.262 | 975.469 | 974.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 11606) CPU | percent | 1 | 71.133 | 71.133 | 71.133 | 71.133 | 0.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 11606) rss_mb | MB | 2 | 54.791 | 41.547 | 68.035 | 68.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 11606) main thread run-queue wait | percent | 1 | 0.043 | 0.043 | 0.043 | 0.043 | 0.000439 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 11606) vms_mb | MB | 2 | 62.799 | 48.805 | 76.793 | 76.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 11619) CPU | percent | 1881 | 3.466 | 0.000 | 70.542 | 1.988 | 66.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 11619) rss_mb | MB | 1882 | 286.868 | 41.305 | 342.055 | 230.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 11619) main thread run-queue wait | percent | 1881 | 4.829 | 0.000 | 86.922 | 0.012 | 91.756216 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 11619) vms_mb | MB | 1882 | 5499.800 | 5484.289 | 5499.816 | 5499.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11717) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11717) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11718) rss_mb | MB | 1 | 7.566 | 7.566 | 7.566 | 7.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11718) vms_mb | MB | 1 | 11.926 | 11.926 | 11.926 | 11.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11770) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11770) rss_mb | MB | 2 | 2.672 | 2.672 | 2.672 | 2.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11770) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11770) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 11771) CPU | percent | 1 | 1.986 | 1.986 | 1.986 | 1.986 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 11771) rss_mb | MB | 2 | 12.352 | 12.227 | 12.477 | 12.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 11771) main thread run-queue wait | percent | 1 | 0.017 | 0.017 | 0.017 | 0.017 | 0.000169 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 11771) vms_mb | MB | 2 | 15.812 | 15.777 | 15.848 | 15.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp8pa6oj01.py (PID 11779) rss_mb | MB | 1 | 8.695 | 8.695 | 8.695 | 8.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp8pa6oj01.py (PID 11779) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpgq7vyx37.py (PID 11817) rss_mb | MB | 1 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpgq7vyx37.py (PID 11817) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11859) rss_mb | MB | 1 | 2.676 | 2.676 | 2.676 | 2.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11859) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 11861) rss_mb | MB | 1 | 5.754 | 5.754 | 5.754 | 5.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 11861) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11862) rss_mb | MB | 1 | 1.211 | 1.211 | 1.211 | 1.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11862) vms_mb | MB | 1 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11895) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11895) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11896) rss_mb | MB | 1 | 10.664 | 10.664 | 10.664 | 10.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11896) vms_mb | MB | 1 | 15.203 | 15.203 | 15.203 | 15.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11927) rss_mb | MB | 1 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 11927) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11928) rss_mb | MB | 1 | 21.934 | 21.934 | 21.934 | 21.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 11928) vms_mb | MB | 1 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11955) CPU | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11955) rss_mb | MB | 18 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11955) main thread run-queue wait | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 11955) vms_mb | MB | 18 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 11956) CPU | percent | 11 | 0.361 | 0.000 | 2.978 | 2.978 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 11956) rss_mb | MB | 12 | 12.434 | 12.434 | 12.434 | 12.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 11956) main thread run-queue wait | percent | 11 | 0.002 | 0.000 | 0.023 | 0.023 | 0.000253 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 11956) vms_mb | MB | 12 | 15.777 | 15.777 | 15.777 | 15.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11957) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11957) rss_mb | MB | 12 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11957) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 11957) vms_mb | MB | 12 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpp9aptr47.py (PID 11964) CPU | percent | 4 | 99.915 | 99.227 | 100.494 | 100.478 | 4.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpp9aptr47.py (PID 11964) rss_mb | MB | 5 | 8.250 | 8.250 | 8.250 | 8.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpp9aptr47.py (PID 11964) main thread run-queue wait | percent | 4 | 0.004 | 0.003 | 0.006 | 0.003 | 0.000150 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpp9aptr47.py (PID 11964) vms_mb | MB | 5 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpioemm7ru.py (PID 11965) CPU | percent | 4 | 99.966 | 99.445 | 100.487 | 100.487 | 4.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpioemm7ru.py (PID 11965) rss_mb | MB | 5 | 8.520 | 8.520 | 8.520 | 8.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpioemm7ru.py (PID 11965) main thread run-queue wait | percent | 4 | 0.004 | 0.002 | 0.005 | 0.005 | 0.000149 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpioemm7ru.py (PID 11965) vms_mb | MB | 5 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpmrgl6vlb.py (PID 11975) rss_mb | MB | 1 | 7.488 | 7.488 | 7.488 | 7.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpmrgl6vlb.py (PID 11975) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpe31tdw95.py (PID 12014) rss_mb | MB | 1 | 4.383 | 4.383 | 4.383 | 4.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpe31tdw95.py (PID 12014) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 12023) CPU | percent | 5 | 0.398 | 0.000 | 1.988 | 1.988 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 12023) rss_mb | MB | 6 | 12.172 | 12.172 | 12.172 | 12.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 12023) main thread run-queue wait | percent | 5 | 0.001 | 0.000 | 0.005 | 0.005 | 0.000054 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 12023) vms_mb | MB | 6 | 15.691 | 15.691 | 15.691 | 15.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12024) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12024) rss_mb | MB | 6 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12024) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12024) vms_mb | MB | 6 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1kn41ym7.py (PID 12028) CPU | percent | 4 | 99.888 | 99.293 | 100.479 | 100.479 | 4.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1kn41ym7.py (PID 12028) rss_mb | MB | 5 | 8.500 | 8.500 | 8.500 | 8.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1kn41ym7.py (PID 12028) main thread run-queue wait | percent | 4 | 0.004 | 0.003 | 0.006 | 0.003 | 0.000167 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmp1kn41ym7.py (PID 12028) vms_mb | MB | 5 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpkyjz5cwa.py (PID 12053) rss_mb | MB | 1 | 0.441 | 0.441 | 0.441 | 0.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpkyjz5cwa.py (PID 12053) vms_mb | MB | 1 | 9.500 | 9.500 | 9.500 | 9.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12076) rss_mb | MB | 1 | 1.547 | 1.547 | 1.547 | 1.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12076) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12077) rss_mb | MB | 1 | 21.414 | 21.414 | 21.414 | 21.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12077) vms_mb | MB | 1 | 27.094 | 27.094 | 27.094 | 27.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12103) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12103) rss_mb | MB | 3 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12103) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12103) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 12104) CPU | percent | 1 | 3.967 | 3.967 | 3.967 | 3.967 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 12104) rss_mb | MB | 2 | 12.461 | 12.398 | 12.523 | 12.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 12104) main thread run-queue wait | percent | 1 | 0.011 | 0.011 | 0.011 | 0.011 | 0.000107 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 12104) vms_mb | MB | 2 | 15.875 | 15.875 | 15.875 | 15.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpbt5plyb7.py (PID 12122) rss_mb | MB | 1 | 8.730 | 8.730 | 8.730 | 8.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpbt5plyb7.py (PID 12122) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppien4yec.py (PID 12161) rss_mb | MB | 1 | 7.566 | 7.566 | 7.566 | 7.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmppien4yec.py (PID 12161) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 12167) rss_mb | MB | 1 | 12.320 | 12.320 | 12.320 | 12.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 12167) vms_mb | MB | 1 | 15.723 | 15.723 | 15.723 | 15.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12168) rss_mb | MB | 1 | 1.211 | 1.211 | 1.211 | 1.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12168) vms_mb | MB | 1 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpo27_mt1l.py (PID 12198) rss_mb | MB | 1 | 7.445 | 7.445 | 7.445 | 7.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpo27_mt1l.py (PID 12198) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12257) rss_mb | MB | 1 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12257) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 12258) rss_mb | MB | 1 | 85.934 | 85.934 | 85.934 | 85.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 12258) vms_mb | MB | 1 | 313.289 | 313.289 | 313.289 | 313.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12269) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12269) rss_mb | MB | 4 | 2.879 | 2.879 | 2.879 | 2.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12269) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12269) vms_mb | MB | 4 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 12270) CPU | percent | 3 | 82.460 | 79.422 | 84.414 | 84.414 | 2.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 12270) rss_mb | MB | 4 | 651.824 | 4.590 | 904.496 | 904.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 12270) main thread run-queue wait | percent | 3 | 8.553 | 7.428 | 9.420 | 8.812 | 0.258303 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 12270) vms_mb | MB | 4 | 865.848 | 10.000 | 1192.438 | 1192.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12281) rss_mb | MB | 1 | 1.555 | 1.555 | 1.555 | 1.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12281) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12282) rss_mb | MB | 1 | 21.684 | 21.684 | 21.684 | 21.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12282) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12341) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12341) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12342) rss_mb | MB | 1 | 19.078 | 19.078 | 19.078 | 19.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12342) vms_mb | MB | 1 | 24.605 | 24.605 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12394) rss_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12394) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 12397) rss_mb | MB | 1 | 21.570 | 21.570 | 21.570 | 21.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 12397) vms_mb | MB | 1 | 213.691 | 213.691 | 213.691 | 213.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12410) rss_mb | MB | 1 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12410) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 12412) rss_mb | MB | 1 | 459.391 | 459.391 | 459.391 | 459.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 12412) vms_mb | MB | 1 | 786.219 | 786.219 | 786.219 | 786.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12416) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12416) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12417) rss_mb | MB | 1 | 14.086 | 14.086 | 14.086 | 14.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12417) vms_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12435) rss_mb | MB | 1 | 1.555 | 1.555 | 1.555 | 1.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12435) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12436) rss_mb | MB | 1 | 21.773 | 21.773 | 21.773 | 21.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12436) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12456) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12456) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12457) rss_mb | MB | 1 | 21.781 | 21.781 | 21.781 | 21.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12457) vms_mb | MB | 1 | 26.906 | 26.906 | 26.906 | 26.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12468) CPU | percent | 167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12468) rss_mb | MB | 168 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12468) main thread run-queue wait | percent | 167 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12468) vms_mb | MB | 168 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — headdla.py (PID 12470) CPU | percent | 167 | 168.518 | 116.699 | 183.870 | 159.048 | 284.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — headdla.py (PID 12470) rss_mb | MB | 168 | 1102.848 | 50.793 | 1109.273 | 1109.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — headdla.py (PID 12470) main thread run-queue wait | percent | 167 | 68.599 | 5.138 | 79.626 | 74.922 | 115.635236 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — headdla.py (PID 12470) vms_mb | MB | 168 | 1326.400 | 252.578 | 1333.105 | 1333.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12502) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12502) rss_mb | MB | 3 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12502) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12502) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12503) CPU | percent | 2 | 5.463 | 4.963 | 5.963 | 5.963 | 0.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12503) rss_mb | MB | 3 | 13.323 | 7.488 | 18.004 | 18.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12503) main thread run-queue wait | percent | 2 | 55.283 | 51.811 | 58.755 | 58.755 | 1.113189 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12503) vms_mb | MB | 3 | 18.697 | 11.926 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12513) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12513) rss_mb | MB | 4 | 1.555 | 1.555 | 1.555 | 1.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12513) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12513) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12514) CPU | percent | 3 | 3.977 | 2.981 | 5.966 | 5.966 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12514) rss_mb | MB | 4 | 13.714 | 8.906 | 19.391 | 19.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12514) main thread run-queue wait | percent | 3 | 47.097 | 44.526 | 48.560 | 48.207 | 1.421216 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12514) vms_mb | MB | 4 | 18.443 | 13.410 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12516) CPU | percent | 400 | 0.007 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12516) rss_mb | MB | 401 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12516) main thread run-queue wait | percent | 400 | 0.013 | 0.000 | 5.348 | 0.000 | 0.053977 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12516) vms_mb | MB | 401 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12517) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12517) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12517) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12517) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12518) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12518) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12518) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12518) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12519) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12519) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12519) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12519) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12520) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12520) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12520) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12520) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12522) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12522) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12522) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12522) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12523) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12523) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12523) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12523) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12524) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12524) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12524) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12524) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12525) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12525) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12525) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12525) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12526) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12526) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12526) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12526) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12527) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12527) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12527) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12527) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12529) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12529) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12529) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12529) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12530) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12530) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12530) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12530) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12532) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12532) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12532) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12532) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12533) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12533) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12533) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12533) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12534) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12534) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12534) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12534) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12535) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12535) rss_mb | MB | 4 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12535) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12535) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12536) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12536) rss_mb | MB | 5 | 1.193 | 0.934 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12536) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12536) vms_mb | MB | 5 | 2.748 | 2.441 | 3.977 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12537) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12537) rss_mb | MB | 5 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12537) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12537) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12538) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12538) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12538) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12538) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12539) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12539) rss_mb | MB | 5 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12539) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12539) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12540) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12540) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12540) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12540) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12541) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12541) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12541) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12541) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12543) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12543) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12543) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12543) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12544) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12544) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12544) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12544) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12546) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12546) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12546) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12546) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12547) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12547) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12547) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12547) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12548) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12548) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12548) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12548) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12549) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12549) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12549) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12549) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12550) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12550) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12550) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12550) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12551) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12551) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12551) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12551) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12552) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12552) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12552) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12552) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12553) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12553) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12553) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12553) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12554) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12554) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12554) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12554) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12556) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12556) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12556) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12556) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12557) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12557) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12557) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12557) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12558) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12558) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12558) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12558) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12559) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12559) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12559) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12559) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12560) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12560) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12560) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12560) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12561) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12561) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12561) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12561) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12562) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12562) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12562) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12562) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12564) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12564) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12564) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12564) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12583) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12583) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12583) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12583) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12585) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12585) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12585) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12585) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12586) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12586) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12586) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12586) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12587) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12587) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12587) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12587) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12588) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12588) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12588) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12588) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12589) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12589) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12589) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12589) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12590) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12590) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12590) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12590) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12591) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12591) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12591) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12591) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12592) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12592) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12592) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12592) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12593) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12593) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12593) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12593) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12594) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12594) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12594) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12594) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12596) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12596) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12596) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12596) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12597) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12597) rss_mb | MB | 5 | 1.281 | 1.281 | 1.281 | 1.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12597) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12597) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12599) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12599) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12599) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12599) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12600) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12600) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12600) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12600) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12601) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12601) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12601) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12601) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12602) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12602) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12602) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12602) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12603) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12603) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12603) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12603) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12604) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12604) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12604) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12604) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12605) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12605) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12605) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12605) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12606) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12606) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12606) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12606) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12608) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12608) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12608) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12608) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12609) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12609) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12609) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12609) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12610) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12610) rss_mb | MB | 4 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12610) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12610) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12615) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12615) rss_mb | MB | 5 | 1.162 | 0.934 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12615) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12615) vms_mb | MB | 5 | 2.748 | 2.441 | 3.977 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12617) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12617) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12617) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12617) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12618) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12618) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12618) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12618) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12619) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12619) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12619) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12619) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12620) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12620) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12620) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12620) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12621) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12621) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12621) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12621) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12622) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12622) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12622) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12622) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12624) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12624) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12624) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12624) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12625) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12625) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12625) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12625) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12626) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12626) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12626) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12626) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12627) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12627) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12627) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12627) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12629) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12629) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12629) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12629) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12630) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12630) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12630) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12630) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12631) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12631) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12631) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12631) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12632) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12632) rss_mb | MB | 5 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12632) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12632) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12638) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12638) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12638) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 12638) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12660) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12660) rss_mb | MB | 2 | 2.992 | 2.992 | 2.992 | 2.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12660) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12660) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — hard.py (PID 12662) CPU | percent | 1 | 95.424 | 95.424 | 95.424 | 95.424 | 0.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — hard.py (PID 12662) rss_mb | MB | 2 | 1280.521 | 55.789 | 2505.254 | 2505.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — hard.py (PID 12662) main thread run-queue wait | percent | 1 | 2.389 | 2.389 | 2.389 | 2.389 | 0.024030 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — hard.py (PID 12662) vms_mb | MB | 2 | 1743.682 | 247.297 | 3240.066 | 3240.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12680) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12680) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12681) rss_mb | MB | 1 | 21.211 | 21.211 | 21.211 | 21.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12681) vms_mb | MB | 1 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12716) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12716) rss_mb | MB | 3 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12716) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12716) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 12717) CPU | percent | 1 | 2.973 | 2.973 | 2.973 | 2.973 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 12717) rss_mb | MB | 2 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 12717) main thread run-queue wait | percent | 1 | 0.012 | 0.012 | 0.012 | 0.012 | 0.000116 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — evalgen.py (PID 12717) vms_mb | MB | 2 | 15.777 | 15.777 | 15.777 | 15.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12718) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12718) rss_mb | MB | 2 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12718) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12718) vms_mb | MB | 2 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpbmj0pxmo.py (PID 12724) rss_mb | MB | 1 | 2.383 | 2.383 | 2.383 | 2.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpbmj0pxmo.py (PID 12724) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmplw4l1m7i.py (PID 12761) rss_mb | MB | 1 | 7.613 | 7.613 | 7.613 | 7.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmplw4l1m7i.py (PID 12761) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 12783) rss_mb | MB | 1 | 12.395 | 12.395 | 12.395 | 12.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — upper.py (PID 12783) vms_mb | MB | 1 | 15.699 | 15.699 | 15.699 | 15.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12784) rss_mb | MB | 1 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 12784) vms_mb | MB | 1 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpky7v6fol.py (PID 12798) rss_mb | MB | 1 | 7.715 | 7.715 | 7.715 | 7.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tmpky7v6fol.py (PID 12798) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12822) rss_mb | MB | 1 | 1.512 | 1.512 | 1.512 | 1.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12822) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12823) rss_mb | MB | 1 | 18.887 | 18.887 | 18.887 | 18.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12823) vms_mb | MB | 1 | 24.605 | 24.605 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12873) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12873) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12874) rss_mb | MB | 1 | 18.645 | 18.645 | 18.645 | 18.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12874) vms_mb | MB | 1 | 24.254 | 24.254 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12885) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12885) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12897) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12897) rss_mb | MB | 6 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12897) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 12897) vms_mb | MB | 6 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — onpol_an.py (PID 12899) CPU | percent | 5 | 78.910 | 69.570 | 102.229 | 102.229 | 3.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — onpol_an.py (PID 12899) rss_mb | MB | 6 | 602.886 | 14.445 | 1926.055 | 1118.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — onpol_an.py (PID 12899) main thread run-queue wait | percent | 5 | 0.889 | 0.048 | 4.124 | 0.048 | 0.044708 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — onpol_an.py (PID 12899) vms_mb | MB | 6 | 909.305 | 207.363 | 2765.102 | 1342.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12929) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12929) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12930) rss_mb | MB | 1 | 15.727 | 15.727 | 15.727 | 15.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12930) vms_mb | MB | 1 | 20.461 | 20.461 | 20.461 | 20.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12964) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 12964) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12965) rss_mb | MB | 1 | 15.539 | 15.539 | 15.539 | 15.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 12965) vms_mb | MB | 1 | 20.461 | 20.461 | 20.461 | 20.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13009) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13009) rss_mb | MB | 21 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13009) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13009) vms_mb | MB | 21 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gate.py (PID 13011) CPU | percent | 20 | 68.450 | 28.688 | 105.699 | 70.325 | 13.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gate.py (PID 13011) rss_mb | MB | 21 | 1889.724 | 20.609 | 3885.531 | 254.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gate.py (PID 13011) main thread run-queue wait | percent | 20 | 2.466 | 0.012 | 33.711 | 0.080 | 0.515064 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gate.py (PID 13011) vms_mb | MB | 21 | 2170.851 | 212.496 | 4129.852 | 476.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 13015) rss_mb | MB | 1 | 228.109 | 228.109 | 228.109 | 228.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 13015) vms_mb | MB | 1 | 5499.816 | 5499.816 | 5499.816 | 5499.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13048) rss_mb | MB | 1 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13048) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 13049) rss_mb | MB | 1 | 22.098 | 22.098 | 22.098 | 22.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 13049) vms_mb | MB | 1 | 214.012 | 214.012 | 214.012 | 214.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13065) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13065) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13066) rss_mb | MB | 1 | 17.918 | 17.918 | 17.918 | 17.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13066) vms_mb | MB | 1 | 23.098 | 23.098 | 23.098 | 23.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13073) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13073) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13074) rss_mb | MB | 1 | 21.801 | 21.801 | 21.801 | 21.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13074) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13084) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13084) rss_mb | MB | 13 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13084) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13084) vms_mb | MB | 13 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 13086) CPU | percent | 12 | 69.906 | 33.085 | 93.477 | 83.066 | 8.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 13086) rss_mb | MB | 13 | 3168.553 | 125.684 | 4931.395 | 4849.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 13086) main thread run-queue wait | percent | 12 | 1.393 | 0.007 | 15.650 | 0.040 | 0.176701 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 13086) vms_mb | MB | 13 | 3445.796 | 376.398 | 5124.789 | 5109.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13090) rss_mb | MB | 1 | 1.551 | 1.551 | 1.551 | 1.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13090) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13091) rss_mb | MB | 1 | 7.137 | 7.137 | 7.137 | 7.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13091) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13101) rss_mb | MB | 1 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13101) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 13102) rss_mb | MB | 1 | 1653.789 | 1653.789 | 1653.789 | 1653.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 13102) vms_mb | MB | 1 | 2731.027 | 2731.027 | 2731.027 | 2731.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13132) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13132) rss_mb | MB | 10 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13132) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13132) vms_mb | MB | 10 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 13133) CPU | percent | 9 | 72.931 | 64.175 | 98.005 | 76.276 | 6.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 13133) rss_mb | MB | 10 | 2738.220 | 146.055 | 4965.152 | 4965.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 13133) main thread run-queue wait | percent | 9 | 2.260 | 0.063 | 19.651 | 0.132 | 0.205549 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 13133) vms_mb | MB | 10 | 3010.378 | 376.398 | 5333.852 | 5333.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13173) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13173) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13174) rss_mb | MB | 1 | 19.316 | 19.316 | 19.316 | 19.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13174) vms_mb | MB | 1 | 24.730 | 24.730 | 24.730 | 24.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13186) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13186) rss_mb | MB | 15 | 2.895 | 2.895 | 2.895 | 2.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13186) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13186) vms_mb | MB | 15 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build2.py (PID 13188) CPU | percent | 14 | 73.190 | 63.557 | 95.073 | 69.356 | 10.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build2.py (PID 13188) rss_mb | MB | 15 | 2438.305 | 469.297 | 4891.656 | 3074.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build2.py (PID 13188) main thread run-queue wait | percent | 14 | 2.209 | 0.078 | 12.525 | 0.085 | 0.312102 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build2.py (PID 13188) vms_mb | MB | 15 | 2714.917 | 719.855 | 5160.594 | 3322.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13193) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 13193) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13194) rss_mb | MB | 1 | 20.391 | 20.391 | 20.391 | 20.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 13194) vms_mb | MB | 1 | 25.117 | 25.117 | 25.117 | 25.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13203) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13203) rss_mb | MB | 16 | 2.695 | 2.695 | 2.695 | 2.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13203) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 13203) vms_mb | MB | 16 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build2.py (PID 13206) CPU | percent | 15 | 72.693 | 66.571 | 92.218 | 70.324 | 11.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build2.py (PID 13206) rss_mb | MB | 16 | 2058.321 | 23.965 | 4341.625 | 3764.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build2.py (PID 13206) main thread run-queue wait | percent | 15 | 1.830 | 0.071 | 10.936 | 0.071 | 0.276924 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build2.py (PID 13206) vms_mb | MB | 16 | 2345.203 | 215.828 | 4700.801 | 4088.285 | n/a | n/a |
| docker inspect (PID 13247) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker inspect (PID 13247) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker inspect (PID 13247) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker inspect (PID 13247) rss_mb | MB | 3 | 29.217 | 29.176 | 29.301 | 29.301 | n/a | n/a |
| docker inspect (PID 13247) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker inspect (PID 13247) vms_mb | MB | 3 | 1771.203 | 1771.203 | 1771.203 | 1771.203 | n/a | n/a |
| docker inspect (PID 13257) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker inspect (PID 13257) io read MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker inspect (PID 13257) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker inspect (PID 13257) rss_mb | MB | 4 | 30.836 | 30.836 | 30.836 | 30.836 | n/a | n/a |
| docker inspect (PID 13257) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker inspect (PID 13257) vms_mb | MB | 4 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker commit (PID 13274) CPU | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 13274) io read MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 13274) io write MB/s | MB/s | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 13274) rss_mb | MB | 25 | 30.039 | 30.039 | 30.039 | 30.039 | n/a | n/a |
| docker commit (PID 13274) main thread run-queue wait | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 13274) vms_mb | MB | 25 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker stop (PID 13344) rss_mb | MB | 1 | 30.410 | 30.410 | 30.410 | 30.410 | n/a | n/a |
| docker stop (PID 13344) vms_mb | MB | 1 | 1843.020 | 1843.020 | 1843.020 | 1843.020 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4781) CPU | percent | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4781) io read MB/s | MB/s | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4781) io write MB/s | MB/s | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4781) rss_mb | MB | 1921 | 2.938 | 2.938 | 2.938 | 2.938 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4781) main thread run-queue wait | percent | 1920 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4781) vms_mb | MB | 1921 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 CPU | percent | 1918 | 56.435 | 0.000 | 213.918 | 0.000 | 1098.106361 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1918 | 4.782 | 0.000 | 51.049 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1918 | 6.512 | 0.000 | 75.335 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_full_pct | percent of wall time stalled | 1918 | 0.509 | 0.000 | 90.881 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_some_pct | percent of wall time stalled | 1918 | 0.524 | 0.000 | 90.881 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io read MB/s | MB/s | 1918 | 0.316 | 0.000 | 89.822 | 0.000 | 617.296875 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io write MB/s | MB/s | 1918 | 0.056 | 0.000 | 41.064 | 0.000 | 109.046875 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory | MB | 1919 | 696.831 | 60.746 | 5557.449 | 491.781 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1918 | 0.333 | 0.000 | 80.440 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1918 | 0.342 | 0.000 | 80.528 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net rx MB/s | MB/s | 1918 | 0.004 | 0.000 | 8.405 | 0.000 | 8.499495 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net tx MB/s | MB/s | 1918 | 0.000 | 0.000 | 0.012 | 0.000 | 0.051053 MB | n/a |
| workload total CPU | percent | 1920 | 5.013 | 1.341 | 164.585 | 9.628 | 98.917802 CPU seconds | n/a |
| workload total memory | MB | 1921 | 9010.863 | 7769.176 | 11081.898 | 7936.344 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
