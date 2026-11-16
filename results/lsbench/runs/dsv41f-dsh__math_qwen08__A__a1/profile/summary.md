# agprof summary

- Duration: **1110.111 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **107 calls**, 97 succeeded, 10 failed, 0 interrupted, n/a reported retries, 691.088 s total wait
- Tools: **95/95 completed**, 3 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **115392** at 1.967 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1086756.703 / 1086756.703 ms |
| LLM latency p50 / p95 | 5074.656 / 14656.769 ms |
| LLM TTFT p50 / p95 | 2322.800 / 9662.382 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 107 total, 97 succeeded, 10 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- dsh: {"automatic_functions": "host_only", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "unavailable", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 72/72 | 71 | 1 | 0 | n/a | n/a |
| mcp__agency__attention | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 5/5 | 3 | 2 | 0 | n/a | n/a |
| mcp__agency__inspect | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 4/4 | 4 | 0 | 0 | n/a | n/a |
| todo_write | 1/1 | 1 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 16.682% | 267.509% | 185.310 s | 5272.241 MB | 6606.293 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker-init | 4013 | sandbox_agent_lsb-dsh_0000_0000 | 1079 | 0.001% | 0.995% | 0.010 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 3732 |  | 1102 | 9.233% | 43.752% | 102.540 s | 2339.535 MB | 2339.984 MB | 21861.807 MB | 21862.250 MB | 0.000000 MB | 0.003906 MB |
| python | 3731 |  | 1102 | 0.000% | 0.000% | 0.000 s | 12.191 MB | 12.191 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 3673 |  | 1102 | 0.782% | 4.972% | 8.690 s | 1784.047 MB | 1784.473 MB | 11991.051 MB | 11993.230 MB | 0.000000 MB | 0.046875 MB |
| python | 3664 |  | 1102 | 6.626% | 267.344% | 73.630 s | 2561.840 MB | 3959.781 MB | 15505.056 MB | 19499.031 MB | 3.433594 MB | 370.054688 MB |
| python3 | 4160 | sandbox_agent_lsb-dsh_0000_0000 | 2 | 98.832% | 98.832% | 1.000 s | 56.613 MB | 82.227 MB | 68.469 MB | 98.148 MB | n/a MB | n/a MB |
| bash | 4154 | sandbox_agent_lsb-dsh_0000_0000 | 1079 | 8.803% | 91.514% | 95.630 s | 106.494 MB | 113.223 MB | 965.452 MB | 974.570 MB | n/a MB | n/a MB |
| lsb_guard.sh | 3683 |  | 1102 | 0.001% | 0.992% | 0.010 s | 3.367 MB | 3.367 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| lsb_grid_worker | 3655 |  | 1102 | 0.000% | 0.000% | 0.000 s | 3.410 MB | 3.410 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3686 |  | 16 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| tail | 4052 | sandbox_agent_lsb-dsh_0000_0000 | 1079 | 0.002% | 0.994% | 0.020 s | 1.426 MB | 1.426 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| MainThread | 4184 | sandbox_agent_lsb-dsh_0000_0000 | 1051 | 1.134% | 116.243% | 11.990 s | 397.084 MB | 473.328 MB | 10217.338 MB | 10349.527 MB | n/a MB | n/a MB |
| sleep | 4217 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4244 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4338 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4377 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4391 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4423 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4486 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4516 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 973.738 MB | 973.738 MB | 2527.984 MB | 2527.984 MB | n/a MB | n/a MB |
| python3 | 4539 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 1427.781 MB | 1427.781 MB | 2315.926 MB | 2315.926 MB | n/a MB | n/a MB |
| python3 | 4551 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 1082.656 MB | 1082.656 MB | 1465.633 MB | 1465.633 MB | n/a MB | n/a MB |
| python3 | 4562 | sandbox_agent_lsb-dsh_0000_0000 | 9 | 189.278% | 194.795% | 15.250 s | 93.533 MB | 121.160 MB | 471.670 MB | 499.074 MB | n/a MB | n/a MB |
| sleep | 4578 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4640 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.754 MB | 8.754 MB | 13.152 MB | 13.152 MB | n/a MB | n/a MB |
| sleep | 4679 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4680 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 1080.172 MB | 1080.172 MB | 1431.660 MB | 1431.660 MB | n/a MB | n/a MB |
| python3 | 4705 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.930 MB | 19.930 MB | 371.891 MB | 371.891 MB | n/a MB | n/a MB |
| sleep | 4717 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4722 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.207 MB | 13.207 MB | 367.125 MB | 367.125 MB | n/a MB | n/a MB |
| bash | 4721 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.773 MB | 2.773 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 4723 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.238 MB | 1.238 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 4789 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.945 MB | 16.945 MB | 369.590 MB | 369.590 MB | n/a MB | n/a MB |
| python3 | 4815 | sandbox_agent_lsb-dsh_0000_0000 | 5 | 188.398% | 188.958% | 7.580 s | 224.654 MB | 296.801 MB | 595.295 MB | 665.004 MB | n/a MB | n/a MB |
| sleep | 4824 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4836 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.340 MB | 13.340 MB | 367.238 MB | 367.238 MB | n/a MB | n/a MB |
| python3 | 4860 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.223 MB | 13.223 MB | 367.078 MB | 367.078 MB | n/a MB | n/a MB |
| python3 | 4871 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.227 MB | 17.227 MB | 369.789 MB | 369.789 MB | n/a MB | n/a MB |
| sleep | 4883 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4888 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 621.016 MB | 621.016 MB | 1004.293 MB | 1004.293 MB | n/a MB | n/a MB |
| python3 | 4911 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 1022.910 MB | 1022.910 MB | 1382.625 MB | 1382.625 MB | n/a MB | n/a MB |
| python3 | 4922 | sandbox_agent_lsb-dsh_0000_0000 | 2 | 118.321% | 118.321% | 1.190 s | 1529.004 MB | 3036.207 MB | 1895.365 MB | 3416.773 MB | n/a MB | n/a MB |
| sleep | 4959 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4972 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 644.707 MB | 644.707 MB | 1027.707 MB | 1027.707 MB | n/a MB | n/a MB |
| sleep | 5010 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5024 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.301 MB | 20.301 MB | 372.215 MB | 372.215 MB | n/a MB | n/a MB |
| python3 | 5042 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.852 MB | 20.852 MB | 372.246 MB | 372.246 MB | n/a MB | n/a MB |
| python3 | 5058 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 3444.660 MB | 3444.660 MB | 4343.816 MB | 4343.816 MB | n/a MB | n/a MB |
| sleep | 5072 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5112 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.590 MB | 8.590 MB | 13.250 MB | 13.250 MB | n/a MB | n/a MB |
| python3 | 5138 | sandbox_agent_lsb-dsh_0000_0000 | 11 | 189.855% | 195.135% | 19.120 s | 82.290 MB | 88.945 MB | 458.614 MB | 467.105 MB | n/a MB | n/a MB |
| bash | 5137 | sandbox_agent_lsb-dsh_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 5147 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5152 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 202.676 MB | 202.676 MB | 560.523 MB | 560.523 MB | n/a MB | n/a MB |
| bash | 5151 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.656 MB | 2.656 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5163 | sandbox_agent_lsb-dsh_0000_0000 | 2 | 119.302% | 119.302% | 1.200 s | 834.605 MB | 1648.215 MB | 1201.363 MB | 2030.410 MB | n/a MB | n/a MB |
| sleep | 5207 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5222 | sandbox_agent_lsb-dsh_0000_0000 | 11 | 186.584% | 194.308% | 18.780 s | 131.438 MB | 291.273 MB | 510.891 MB | 669.465 MB | n/a MB | n/a MB |
| bash | 5221 | sandbox_agent_lsb-dsh_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.957 MB | 2.957 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 5233 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.781 MB | 2.781 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5234 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 747.004 MB | 747.004 MB | 1345.895 MB | 1345.895 MB | n/a MB | n/a MB |
| bash | 5250 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.891 MB | 2.891 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5252 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.762 MB | 22.762 MB | 375.340 MB | 375.340 MB | n/a MB | n/a MB |
| sleep | 5267 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| docker | 5312 |  | 22 | 0.000% | 0.000% | 0.000 s | 29.047 MB | 29.047 MB | 1843.191 MB | 1843.191 MB | 0.000000 MB | 0.000000 MB |
| docker | 5358 |  | 1 | n/a% | n/a% | n/a s | 21.656 MB | 21.656 MB | 1625.848 MB | 1625.848 MB | n/a MB | n/a MB |
| sleep | 5448 |  | 13 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 25.836% | 100.000% | 11855.060 MB | 15598.000 MB | 41.732 W | 74.097 W | 46305.359 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-dsh_0000_0000 | 19.662% | 207.768% | 213.662 s | 1177.564 MB | 5106.648 MB | 4.484375 MB | 1158.386719 MB | 0.000940 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 3879 | 1110.054 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1086.757 | n/a | n/a | 4.484 | 1086756.703 | 1086756.703 | 1086756.703 |
| engine:execute | 1/1 | 0 | 0 | 1086.755 | 1.673 | 1085.080 | 4.484 | 1086755.232 | 1086755.232 | 1086755.232 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1060.378 | 0.002 | 1060.375 | 4.484 | 1060377.591 | 1060377.591 | 1060377.591 |
| llm:attempt | 107/107 | 10 | 0 | 691.088 | 11.005 | 680.081 | 1.110 | 6458.763 | 5074.656 | 14656.769 |
| tool:mcp__agency__generate | 5/5 | 2 | 0 | 232.895 | n/a | n/a | 0.000 | 46579.098 | 51871.134 | 60020.846 |
| tool:bash | 72/72 | 1 | 0 | 69.978 | n/a | n/a | 3.199 | 971.922 | 439.679 | 3440.496 |
| run:container_call | 13/13 | 0 | 0 | 23.096 | 0.002 | 23.094 | 0.000 | 1776.647 | 33.820 | 9097.466 |
| teardown:commit | 1/1 | 0 | 0 | 22.702 | 0.004 | 22.698 | 0.000 | 22702.041 | 22702.041 | 22702.041 |
| sandbox:commit | 1/1 | 0 | 0 | 22.527 | 0.002 | 22.525 | 0.000 | 22526.751 | 22526.751 | 22526.751 |
| checkpoint.total | 1/1 | 0 | 0 | 22.527 | 0.002 | 22.525 | 0.000 | 22526.604 | 22526.604 | 22526.604 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.526 | 0.002 | 22.525 | 0.000 | 22526.462 | 22526.462 | 22526.462 |
| tool:mcp__agency__token_stats | 2/2 | 0 | 0 | 20.377 | n/a | n/a | 0.000 | 10188.493 | 10188.493 | 19018.634 |
| tool:mcp__agency__trace | 4/4 | 0 | 0 | 16.749 | n/a | n/a | 0.000 | 4187.227 | 2702.901 | 9911.954 |
| tool:mcp__agency__logit_lens | 3/3 | 0 | 0 | 5.311 | n/a | n/a | 0.000 | 1770.269 | 2005.534 | 2101.932 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.046 | 0.686 | 2.359 | 0.000 | 3045.789 | 3045.789 | 3045.789 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.046 | 0.686 | 2.359 | 0.000 | 3045.569 | 3045.569 | 3045.569 |
| tool:mcp__agency__attention | 2/2 | 0 | 0 | 2.085 | n/a | n/a | 0.000 | 1042.348 | 1042.348 | 1692.385 |
| syscall:execve | 239/239 | 0 | 0 | 0.822 | n/a | n/a | 0.029 | 3.438 | 1.245 | 9.326 |
| syscall:connect | 364/364 | 0 | 0 | 0.646 | n/a | n/a | 0.016 | 1.773 | 1.634 | 3.024 |
| tool:mcp__agency__inspect | 3/3 | 0 | 0 | 0.364 | n/a | n/a | 0.000 | 121.366 | 116.050 | 139.881 |
| sandbox:create | 1/1 | 0 | 0 | 0.331 | 0.245 | 0.087 | 0.000 | 331.388 | 331.388 | 331.388 |
| sandbox:start | 1/1 | 0 | 0 | 0.329 | 0.002 | 0.327 | 0.000 | 328.900 | 328.900 | 328.900 |
| runtime.container_create | 1/1 | 0 | 0 | 0.329 | 0.002 | 0.327 | 0.000 | 328.716 | 328.716 | 328.716 |
| sandbox:stop | 1/1 | 0 | 0 | 0.175 | 0.002 | 0.173 | 0.000 | 175.015 | 175.015 | 175.015 |
| agency:services_close | 1/1 | 0 | 0 | 0.158 | 0.001 | 0.157 | 0.000 | 157.691 | 157.691 | 157.691 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 0.123 | n/a | n/a | 0.000 | 123.322 | 123.322 | 123.322 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.099 | n/a | n/a | 0.000 | 98.873 | 98.873 | 98.873 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.032 | 0.000 | 72.926 | 72.926 | 72.926 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.058 | n/a | n/a | 0.000 | 57.711 | 57.711 | 57.711 |
| run:detect | 1/1 | 0 | 0 | 0.050 | 0.001 | 0.049 | 0.000 | 49.583 | 49.583 | 49.583 |
| agent:create | 1/1 | 0 | 0 | 0.042 | 0.007 | 0.035 | 0.000 | 41.965 | 41.965 | 41.965 |
| tool:todo_write | 1/1 | 0 | 0 | 0.009 | n/a | n/a | 0.000 | 9.286 | 9.286 | 9.286 |
| syscall:sendto | 2/2 | 0 | 0 | 0.002 | n/a | n/a | 0.000 | 1.014 | 1.014 | 1.020 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.976 | 1.976 | 1.976 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.263 | 1.263 | 1.263 |
| syscall:bind | 1/1 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 1.120 | 1.120 | 1.120 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.070 | 0.067 | 0.100 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.172 | 0.172 | 0.172 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.078 | 0.078 | 0.078 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1101 | 0.779 | 0.035 | 53.006 | 0.073 | 8.634819 CPU seconds | n/a |
| GPU 0 memory | MB | 1102 | 11855.060 | 11670.000 | 15598.000 | 11858.000 | n/a | n/a |
| GPU 0 power | W | 1102 | 41.732 | 29.198 | 74.097 | 29.765 | n/a | 46305.359 J |
| GPU 0 proc / 3664-113022 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 memory | MB | 1102 | 3221.644 | 3118.000 | 6944.000 | 3204.000 | n/a | n/a |
| GPU 0 proc / 3664-113022 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 estimated power | W | 769 | 2.937 | 0.000 | 74.097 | 0.000 | n/a | n/a |
| GPU 0 proc / 3664-113022 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 utilization | percent | 769 | 2.852 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 3732-114784 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 memory | MB | 1102 | 8151.416 | 8070.000 | 8172.000 | 8172.000 | n/a | n/a |
| GPU 0 proc / 3732-114784 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 estimated power | W | 311 | 58.261 | 0.000 | 72.306 | 72.077 | n/a | n/a |
| GPU 0 proc / 3732-114784 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 utilization | percent | 311 | 80.778 | 0.000 | 100.000 | 100.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1102 | 11373.060 | 11188.000 | 15116.000 | 11376.000 | n/a | n/a |
| GPU 0 utilization | percent | 1102 | 25.836 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1102 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1101 | 3.438 | 0.023 | 79.630 | 0.115 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1101 | 4.467 | 0.000 | 34.289 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1101 | 1.508 | 0.000 | 211.542 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1101 | 1.436 | 0.000 | 247.623 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1101 | 0.968 | 0.000 | 92.374 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1101 | 0.971 | 0.000 | 92.501 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1102 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1102 | 7104.544 | 6625.066 | 10743.051 | 6904.422 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1101 | 0.000 | 0.000 | 0.022 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1101 | 0.000 | 0.000 | 0.022 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1101 | 0.013 | 0.000 | 0.249 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1101 | 0.018 | 0.000 | 0.330 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3655) CPU | percent | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 3655) io read MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3655) io write MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3655) rss_mb | MB | 1102 | 3.410 | 3.410 | 3.410 | 3.410 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3655) main thread run-queue wait | percent | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 3655) vms_mb | MB | 1102 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3664) CPU | percent | 1101 | 6.626 | 0.000 | 267.344 | 0.000 | 73.630000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 3664) io read MB/s | MB/s | 1101 | 0.003 | 0.000 | 1.726 | 0.000 | 3.433594 MB | n/a |
| Agency harness — python -m lsbench (PID 3664) io write MB/s | MB/s | 1101 | 0.333 | 0.015 | 100.872 | 0.023 | 370.054688 MB | n/a |
| Agency harness — python -m lsbench (PID 3664) rss_mb | MB | 1102 | 2561.840 | 2096.266 | 3959.781 | 2803.199 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3664) main thread run-queue wait | percent | 1101 | 0.000 | 0.000 | 0.097 | 0.000 | 0.001853 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 3664) vms_mb | MB | 1102 | 15505.056 | 14211.883 | 19499.031 | 15957.617 | n/a | n/a |
| Python — vllm (PID 3673) CPU | percent | 1101 | 0.782 | 0.000 | 4.972 | 0.000 | 8.690000 CPU seconds | n/a |
| Python — vllm (PID 3673) io read MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 3673) io write MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.008 | 0.000 | 0.046875 MB | n/a |
| Python — vllm (PID 3673) rss_mb | MB | 1102 | 1784.047 | 1782.348 | 1784.473 | 1784.473 | n/a | n/a |
| Python — vllm (PID 3673) main thread run-queue wait | percent | 1101 | 0.003 | 0.000 | 0.468 | 0.000 | 0.028583 run-queue seconds | n/a |
| Python — vllm (PID 3673) vms_mb | MB | 1102 | 11991.051 | 11919.211 | 11993.230 | 11993.230 | n/a | n/a |
| bash lsb_guard.sh (PID 3683) CPU | percent | 1101 | 0.001 | 0.000 | 0.992 | 0.000 | 0.010000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 3683) io read MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3683) io write MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3683) rss_mb | MB | 1102 | 3.367 | 3.367 | 3.367 | 3.367 | n/a | n/a |
| bash lsb_guard.sh (PID 3683) main thread run-queue wait | percent | 1101 | 0.000 | 0.000 | 0.099 | 0.000 | 0.000992 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 3683) vms_mb | MB | 1102 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sleep (PID 3686) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3686) io read MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3686) io write MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3686) rss_mb | MB | 16 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3686) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3686) vms_mb | MB | 16 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — python -c (PID 3731) CPU | percent | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 3731) io read MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3731) io write MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3731) rss_mb | MB | 1102 | 12.191 | 12.191 | 12.191 | 12.191 | n/a | n/a |
| Python — python -c (PID 3731) main thread run-queue wait | percent | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 3731) vms_mb | MB | 1102 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 3732) CPU | percent | 1101 | 9.233 | 0.000 | 43.752 | 1.991 | 102.540000 CPU seconds | n/a |
| VLLM::EngineCore (PID 3732) io read MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 3732) io write MB/s | MB/s | 1101 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 3732) rss_mb | MB | 1102 | 2339.535 | 2338.359 | 2339.984 | 2339.984 | n/a | n/a |
| VLLM::EngineCore (PID 3732) main thread run-queue wait | percent | 1101 | 0.001 | 0.000 | 0.128 | 0.000 | 0.014593 run-queue seconds | n/a |
| VLLM::EngineCore (PID 3732) vms_mb | MB | 1102 | 21861.807 | 21860.652 | 21862.250 | 21862.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 4013) CPU | percent | 1078 | 0.001 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 4013) rss_mb | MB | 1079 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 4013) main thread run-queue wait | percent | 1078 | 0.020 | 0.000 | 7.916 | 0.000 | 0.222205 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 4013) vms_mb | MB | 1079 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 4052) CPU | percent | 1078 | 0.002 | 0.000 | 0.994 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 4052) rss_mb | MB | 1079 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 4052) main thread run-queue wait | percent | 1078 | 0.020 | 0.000 | 7.569 | 0.001 | 0.219097 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 4052) vms_mb | MB | 1079 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4154) CPU | percent | 1078 | 8.803 | 0.000 | 91.514 | 0.000 | 95.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4154) rss_mb | MB | 1079 | 106.494 | 3.012 | 113.223 | 111.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4154) main thread run-queue wait | percent | 1078 | 0.000 | 0.000 | 0.013 | 0.000 | 0.000195 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4154) vms_mb | MB | 1079 | 965.452 | 4.262 | 974.570 | 973.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4160) CPU | percent | 1 | 98.832 | 98.832 | 98.832 | 98.832 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4160) rss_mb | MB | 2 | 56.613 | 31.000 | 82.227 | 82.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4160) main thread run-queue wait | percent | 1 | 0.006 | 0.006 | 0.006 | 0.006 | 0.000065 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4160) vms_mb | MB | 2 | 68.469 | 38.789 | 98.148 | 98.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 4184) CPU | percent | 1050 | 1.134 | 0.000 | 116.243 | 0.000 | 11.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 4184) rss_mb | MB | 1051 | 397.084 | 32.750 | 473.328 | 401.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 4184) main thread run-queue wait | percent | 1050 | 1.745 | 0.000 | 60.441 | 0.004 | 18.449106 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 4184) vms_mb | MB | 1051 | 10217.338 | 1171.449 | 10349.527 | 10232.629 | n/a | n/a |
| sleep (PID 4217) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4217) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4217) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4217) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4217) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4217) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4244) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4244) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4244) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4244) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4244) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4244) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4338) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4338) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4338) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4338) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4338) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4338) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4377) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4377) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4377) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4377) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4377) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4377) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4391) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4391) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4391) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4391) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 4391) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4391) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4423) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4423) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4423) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4423) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4423) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4423) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4486) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4486) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4486) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4486) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4486) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4486) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4516) rss_mb | MB | 1 | 973.738 | 973.738 | 973.738 | 973.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4516) vms_mb | MB | 1 | 2527.984 | 2527.984 | 2527.984 | 2527.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — st.py (PID 4539) rss_mb | MB | 1 | 1427.781 | 1427.781 | 1427.781 | 1427.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — st.py (PID 4539) vms_mb | MB | 1 | 2315.926 | 2315.926 | 2315.926 | 2315.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4551) rss_mb | MB | 1 | 1082.656 | 1082.656 | 1082.656 | 1082.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4551) vms_mb | MB | 1 | 1465.633 | 1465.633 | 1465.633 | 1465.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4562) CPU | percent | 8 | 189.278 | 186.892 | 194.795 | 194.795 | 15.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4562) rss_mb | MB | 9 | 93.533 | 20.418 | 121.160 | 121.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4562) main thread run-queue wait | percent | 8 | 73.395 | 59.072 | 82.620 | 75.096 | 5.913575 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4562) vms_mb | MB | 9 | 471.670 | 372.410 | 499.074 | 499.074 | n/a | n/a |
| sleep (PID 4578) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4578) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4578) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4578) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4578) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4578) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4640) rss_mb | MB | 1 | 8.754 | 8.754 | 8.754 | 8.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4640) vms_mb | MB | 1 | 13.152 | 13.152 | 13.152 | 13.152 | n/a | n/a |
| sleep (PID 4679) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4679) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4679) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4679) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4679) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4679) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4680) rss_mb | MB | 1 | 1080.172 | 1080.172 | 1080.172 | 1080.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4680) vms_mb | MB | 1 | 1431.660 | 1431.660 | 1431.660 | 1431.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4705) rss_mb | MB | 1 | 19.930 | 19.930 | 19.930 | 19.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4705) vms_mb | MB | 1 | 371.891 | 371.891 | 371.891 | 371.891 | n/a | n/a |
| sleep (PID 4717) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4717) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4717) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4717) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4717) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4717) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4721) rss_mb | MB | 1 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4721) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4722) rss_mb | MB | 1 | 13.207 | 13.207 | 13.207 | 13.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4722) vms_mb | MB | 1 | 367.125 | 367.125 | 367.125 | 367.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — head (PID 4723) rss_mb | MB | 1 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — head (PID 4723) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4789) rss_mb | MB | 1 | 16.945 | 16.945 | 16.945 | 16.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4789) vms_mb | MB | 1 | 369.590 | 369.590 | 369.590 | 369.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4815) CPU | percent | 4 | 188.398 | 186.837 | 188.958 | 188.877 | 7.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4815) rss_mb | MB | 5 | 224.654 | 68.219 | 296.801 | 296.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4815) main thread run-queue wait | percent | 4 | 68.710 | 65.617 | 72.149 | 68.406 | 2.764475 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4815) vms_mb | MB | 5 | 595.295 | 448.020 | 665.004 | 665.004 | n/a | n/a |
| sleep (PID 4824) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4824) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4824) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4824) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4824) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4824) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4836) rss_mb | MB | 1 | 13.340 | 13.340 | 13.340 | 13.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4836) vms_mb | MB | 1 | 367.238 | 367.238 | 367.238 | 367.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4860) rss_mb | MB | 1 | 13.223 | 13.223 | 13.223 | 13.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4860) vms_mb | MB | 1 | 367.078 | 367.078 | 367.078 | 367.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4871) rss_mb | MB | 1 | 17.227 | 17.227 | 17.227 | 17.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4871) vms_mb | MB | 1 | 369.789 | 369.789 | 369.789 | 369.789 | n/a | n/a |
| sleep (PID 4883) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4883) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4883) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4883) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4883) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4883) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4888) rss_mb | MB | 1 | 621.016 | 621.016 | 621.016 | 621.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4888) vms_mb | MB | 1 | 1004.293 | 1004.293 | 1004.293 | 1004.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4911) rss_mb | MB | 1 | 1022.910 | 1022.910 | 1022.910 | 1022.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4911) vms_mb | MB | 1 | 1382.625 | 1382.625 | 1382.625 | 1382.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4922) CPU | percent | 1 | 118.321 | 118.321 | 118.321 | 118.321 | 1.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4922) rss_mb | MB | 2 | 1529.004 | 21.801 | 3036.207 | 3036.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4922) main thread run-queue wait | percent | 1 | 7.206 | 7.206 | 7.206 | 7.206 | 0.072474 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4922) vms_mb | MB | 2 | 1895.365 | 373.957 | 3416.773 | 3416.773 | n/a | n/a |
| sleep (PID 4959) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4959) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4959) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4959) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4959) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4959) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — build.py (PID 4972) rss_mb | MB | 1 | 644.707 | 644.707 | 644.707 | 644.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — build.py (PID 4972) vms_mb | MB | 1 | 1027.707 | 1027.707 | 1027.707 | 1027.707 | n/a | n/a |
| sleep (PID 5010) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5010) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5010) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5010) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5010) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5010) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 5024) rss_mb | MB | 1 | 20.301 | 20.301 | 20.301 | 20.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 5024) vms_mb | MB | 1 | 372.215 | 372.215 | 372.215 | 372.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — make_adapter.py (PID 5042) rss_mb | MB | 1 | 20.852 | 20.852 | 20.852 | 20.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — make_adapter.py (PID 5042) vms_mb | MB | 1 | 372.246 | 372.246 | 372.246 | 372.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — dirs.py (PID 5058) rss_mb | MB | 1 | 3444.660 | 3444.660 | 3444.660 | 3444.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — dirs.py (PID 5058) vms_mb | MB | 1 | 4343.816 | 4343.816 | 4343.816 | 4343.816 | n/a | n/a |
| sleep (PID 5072) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5072) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5072) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5072) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 5072) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5072) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — make_adapter.py (PID 5112) rss_mb | MB | 1 | 8.590 | 8.590 | 8.590 | 8.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — make_adapter.py (PID 5112) vms_mb | MB | 1 | 13.250 | 13.250 | 13.250 | 13.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5137) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5137) rss_mb | MB | 11 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5137) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5137) vms_mb | MB | 11 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5138) CPU | percent | 10 | 189.855 | 186.909 | 195.135 | 187.956 | 19.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5138) rss_mb | MB | 11 | 82.290 | 21.910 | 88.945 | 88.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5138) main thread run-queue wait | percent | 10 | 75.540 | 64.441 | 81.656 | 75.332 | 7.607728 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5138) vms_mb | MB | 11 | 458.614 | 373.836 | 467.105 | 467.105 | n/a | n/a |
| sleep (PID 5147) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5147) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5147) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5147) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 5147) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5147) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5151) rss_mb | MB | 1 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5151) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5152) rss_mb | MB | 1 | 202.676 | 202.676 | 202.676 | 202.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5152) vms_mb | MB | 1 | 560.523 | 560.523 | 560.523 | 560.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — make_adapter2.py (PID 5163) CPU | percent | 1 | 119.302 | 119.302 | 119.302 | 119.302 | 1.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — make_adapter2.py (PID 5163) rss_mb | MB | 2 | 834.605 | 20.996 | 1648.215 | 1648.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — make_adapter2.py (PID 5163) main thread run-queue wait | percent | 1 | 17.359 | 17.359 | 17.359 | 17.359 | 0.174604 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — make_adapter2.py (PID 5163) vms_mb | MB | 2 | 1201.363 | 372.316 | 2030.410 | 2030.410 | n/a | n/a |
| sleep (PID 5207) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5207) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5207) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5207) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5207) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5207) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5221) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5221) rss_mb | MB | 11 | 2.957 | 2.957 | 2.957 | 2.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5221) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5221) vms_mb | MB | 11 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5222) CPU | percent | 10 | 186.584 | 159.031 | 194.308 | 159.031 | 18.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5222) rss_mb | MB | 11 | 131.438 | 85.898 | 291.273 | 291.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5222) main thread run-queue wait | percent | 10 | 74.667 | 67.187 | 82.729 | 67.187 | 7.515088 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5222) vms_mb | MB | 11 | 510.891 | 480.551 | 669.465 | 669.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5233) rss_mb | MB | 1 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5233) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5234) rss_mb | MB | 1 | 747.004 | 747.004 | 747.004 | 747.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5234) vms_mb | MB | 1 | 1345.895 | 1345.895 | 1345.895 | 1345.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5250) rss_mb | MB | 1 | 2.891 | 2.891 | 2.891 | 2.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5250) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 5252) rss_mb | MB | 1 | 22.762 | 22.762 | 22.762 | 22.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 5252) vms_mb | MB | 1 | 375.340 | 375.340 | 375.340 | 375.340 | n/a | n/a |
| sleep (PID 5267) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5267) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5267) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5267) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5267) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5267) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| docker commit (PID 5312) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 5312) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5312) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5312) rss_mb | MB | 22 | 29.047 | 29.047 | 29.047 | 29.047 | n/a | n/a |
| docker commit (PID 5312) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 5312) vms_mb | MB | 22 | 1843.191 | 1843.191 | 1843.191 | 1843.191 | n/a | n/a |
| docker inspect (PID 5358) rss_mb | MB | 1 | 21.656 | 21.656 | 21.656 | 21.656 | n/a | n/a |
| docker inspect (PID 5358) vms_mb | MB | 1 | 1625.848 | 1625.848 | 1625.848 | 1625.848 | n/a | n/a |
| sleep (PID 5448) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5448) io read MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5448) io write MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5448) rss_mb | MB | 13 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5448) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5448) vms_mb | MB | 13 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 CPU | percent | 1078 | 19.662 | 0.000 | 207.768 | 0.043 | 213.661976 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1078 | 3.365 | 0.000 | 75.216 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1078 | 3.525 | 0.000 | 79.092 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io_psi_full_pct | percent of wall time stalled | 1078 | 0.003 | 0.000 | 0.403 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io_psi_some_pct | percent of wall time stalled | 1078 | 0.003 | 0.000 | 0.411 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io read MB/s | MB/s | 1078 | 0.004 | 0.000 | 1.247 | 0.000 | 4.484375 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io write MB/s | MB/s | 1078 | 1.068 | 0.000 | 250.606 | 0.000 | 1158.386719 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory | MB | 1079 | 1177.564 | 23.719 | 5106.648 | 1194.273 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1078 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1078 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 net rx MB/s | MB/s | 1078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000940 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 net tx MB/s | MB/s | 1078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 1101 | 16.682 | 1.299 | 267.509 | 2.165 | 185.310049 CPU seconds | n/a |
| workload total memory | MB | 1102 | 5272.241 | 4753.145 | 6606.293 | 5605.367 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
