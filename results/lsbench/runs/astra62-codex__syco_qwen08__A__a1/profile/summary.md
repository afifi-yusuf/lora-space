# agprof summary

- Duration: **990.124 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **28 calls**, 28 succeeded, 0 failed, 0 interrupted, n/a reported retries, 852.193 s total wait
- Tools: **79/79 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **91451** at 1.989 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 972007.375 / 972007.375 ms |
| LLM latency p50 / p95 | 29653.558 / 67866.570 ms |
| LLM TTFT p50 / p95 | 8674.414 / 10951.441 ms |
| LLM input / output tokens | 2281361 / 78283 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 28 total, 28 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- codex: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 18/18 | 18 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 14/14 | 14 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 13/13 | 13 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 22/22 | 22 | 0 | 0 | n/a | n/a |
| update_plan | 6/6 | 6 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 6.428% | 141.254% | 63.677 s | 9150.568 MB | 9823.336 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 2160 |  | 984 | 4.801% | 139.685% | 47.580 s | 2778.579 MB | 3099.320 MB | 16230.342 MB | 16665.461 MB | 171.402344 MB | 1733.894531 MB |
| docker-buildx | 2390 |  | 1 | n/a% | n/a% | n/a s | 41.727 MB | 41.727 MB | 1299.461 MB | 1299.461 MB | n/a MB | n/a MB |
| python | 2219 |  | 984 | 0.000% | 0.000% | 0.000 s | 12.195 MB | 12.195 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 2169 |  | 984 | 0.159% | 10.944% | 1.570 s | 1787.584 MB | 1787.879 MB | 12022.707 MB | 12024.562 MB | 0.003906 MB | 0.074219 MB |
| VLLM::EngineCor | 2220 |  | 984 | 1.432% | 35.792% | 14.160 s | 2312.582 MB | 2312.809 MB | 21828.738 MB | 21828.754 MB | 0.000000 MB | 0.003906 MB |
| docker | 2376 |  | 1 | n/a% | n/a% | n/a s | 30.250 MB | 30.250 MB | 2060.523 MB | 2060.523 MB | n/a MB | n/a MB |
| lsb_grid_worker | 2151 |  | 984 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 2647 | sandbox_agent_lsb-codex_0000_0000 | 965 | 25.248% | 92.574% | 244.850 s | 110.805 MB | 123.832 MB | 989.960 MB | 1049.008 MB | n/a MB | n/a MB |
| docker-init | 2501 | sandbox_agent_lsb-codex_0000_0000 | 965 | 0.003% | 0.995% | 0.030 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 2653 | sandbox_agent_lsb-codex_0000_0000 | 3 | 54.708% | 63.685% | 1.100 s | 44.665 MB | 75.754 MB | 54.423 MB | 91.488 MB | n/a MB | n/a MB |
| tail | 2543 | sandbox_agent_lsb-codex_0000_0000 | 965 | 0.003% | 0.995% | 0.030 s | 1.250 MB | 1.250 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| codex | 2661 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.898 MB | 12.898 MB | 246.531 MB | 246.531 MB | n/a MB | n/a MB |
| codex | 2670 | sandbox_agent_lsb-codex_0000_0000 | 938 | 2.002% | 21.834% | 18.880 s | 140.140 MB | 152.992 MB | 398.490 MB | 573.180 MB | n/a MB | n/a MB |
| git | 2701 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.312 MB | 3.312 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git-remote-http | 2710 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.871 MB | 17.871 MB | 99.594 MB | 99.594 MB | n/a MB | n/a MB |
| git | 2706 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.836 MB | 2.836 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 2745 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.828 MB | 3.828 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 2750 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.965 MB | 4.965 MB | 296.301 MB | 296.301 MB | n/a MB | n/a MB |
| python3 | 2836 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.477 MB | 10.477 MB | 15.195 MB | 15.195 MB | n/a MB | n/a MB |
| python3 | 2882 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.340 MB | 20.340 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| python3 | 2926 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.191 MB | 9.191 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| head | 2932 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.609 MB | 1.609 MB | 2.859 MB | 2.859 MB | n/a MB | n/a MB |
| find | 2931 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.656 MB | 2.656 MB | 4.930 MB | 4.930 MB | n/a MB | n/a MB |
| bash | 2928 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.973 MB | 2.973 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 2938 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.840 MB | 14.840 MB | 368.617 MB | 368.617 MB | n/a MB | n/a MB |
| python3 | 2970 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.441 MB | 8.441 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python3 | 2984 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.211 MB | 8.211 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python3 | 3001 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.438 MB | 21.438 MB | 26.945 MB | 26.945 MB | n/a MB | n/a MB |
| python3 | 3080 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.348 MB | 19.348 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python3 | 3086 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.777 MB | 21.777 MB | 27.059 MB | 27.059 MB | n/a MB | n/a MB |
| python3 | 3143 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.637 MB | 21.637 MB | 27.008 MB | 27.008 MB | n/a MB | n/a MB |
| bash | 3144 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.137 MB | 3.137 MB | 4.371 MB | 4.371 MB | n/a MB | n/a MB |
| bash | 3179 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.730 MB | 2.730 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 3182 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.039 MB | 3.039 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 3183 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 38.094 MB | 38.094 MB | 417.449 MB | 417.449 MB | n/a MB | n/a MB |
| python3 | 3199 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.207 MB | 20.207 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| bash | 3201 | sandbox_agent_lsb-codex_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.000 MB | 3.000 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 3202 | sandbox_agent_lsb-codex_0000_0000 | 5 | 164.258% | 173.402% | 6.620 s | 179.641 MB | 233.738 MB | 615.145 MB | 666.918 MB | n/a MB | n/a MB |
| python3 | 3209 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.266 MB | 21.266 MB | 26.746 MB | 26.746 MB | n/a MB | n/a MB |
| python3 | 3211 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.703 MB | 15.703 MB | 20.539 MB | 20.539 MB | n/a MB | n/a MB |
| python3 | 3237 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.004 MB | 18.004 MB | 24.176 MB | 24.176 MB | n/a MB | n/a MB |
| python3 | 3288 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.738 MB | 14.738 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python | 3312 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 56.598 MB | 56.598 MB | 437.762 MB | 437.762 MB | n/a MB | n/a MB |
| bash | 3370 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.652 MB | 2.652 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 3396 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.344 MB | 8.344 MB | 13.285 MB | 13.285 MB | n/a MB | n/a MB |
| bash | 3398 | sandbox_agent_lsb-codex_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.805 MB | 2.805 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 3399 | sandbox_agent_lsb-codex_0000_0000 | 8 | 170.486% | 179.754% | 12.060 s | 392.638 MB | 447.297 MB | 808.141 MB | 870.406 MB | n/a MB | n/a MB |
| python3 | 3438 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.477 MB | 20.477 MB | 25.324 MB | 25.324 MB | n/a MB | n/a MB |
| python3 | 3439 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.520 MB | 20.520 MB | 25.324 MB | 25.324 MB | n/a MB | n/a MB |
| python3 | 3467 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.824 MB | 15.824 MB | 20.539 MB | 20.539 MB | n/a MB | n/a MB |
| python3 | 3470 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.395 MB | 15.395 MB | 20.207 MB | 20.207 MB | n/a MB | n/a MB |
| python | 3481 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 73.527 MB | 73.527 MB | 486.234 MB | 486.234 MB | n/a MB | n/a MB |
| bash | 3480 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| bash | 3501 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.098 MB | 3.098 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 3502 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.195 MB | 22.195 MB | 213.895 MB | 213.895 MB | n/a MB | n/a MB |
| python3 | 3522 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.578 MB | 20.578 MB | 25.324 MB | 25.324 MB | n/a MB | n/a MB |
| python3 | 3528 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.996 MB | 6.996 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| bash | 3532 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.844 MB | 2.844 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 3533 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.891 MB | 21.891 MB | 213.688 MB | 213.688 MB | n/a MB | n/a MB |
| python3 | 3547 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.938 MB | 7.938 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python | 3552 | sandbox_agent_lsb-codex_0000_0000 | 11 | 164.364% | 175.094% | 16.530 s | 482.189 MB | 591.727 MB | 914.167 MB | 1092.480 MB | n/a MB | n/a MB |
| bash | 3604 | sandbox_agent_lsb-codex_0000_0000 | 13 | 0.000% | 0.000% | 0.000 s | 2.883 MB | 2.883 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 3605 | sandbox_agent_lsb-codex_0000_0000 | 11 | 166.145% | 177.701% | 16.730 s | 504.642 MB | 582.430 MB | 921.057 MB | 1004.191 MB | n/a MB | n/a MB |
| python | 3618 | sandbox_agent_lsb-codex_0000_0000 | 2 | 164.797% | 164.797% | 1.660 s | 115.801 MB | 191.461 MB | 526.072 MB | 631.102 MB | n/a MB | n/a MB |
| python3 | 3642 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.773 MB | 20.773 MB | 25.582 MB | 25.582 MB | n/a MB | n/a MB |
| python3 | 3655 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.539 MB | 20.539 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| docker | 3696 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.215 MB | 30.215 MB | 1987.770 MB | 1987.770 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.303% | 68.000% | 11827.179 MB | 11900.000 MB | 29.539 W | 55.326 W | 29207.753 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 36.341% | 208.143% | 352.558 s | 554.483 MB | 1153.547 MB | 252.804688 MB | 176.492188 MB | 24.938220 MB | 1.097149 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2374 | 990.056 | interrupted |
| harness:retire | -1 | 0.378 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 972.007 | n/a | n/a | 252.805 | 972007.375 | 972007.375 | 972007.375 |
| engine:execute | 1/1 | 0 | 0 | 972.006 | 2.008 | 969.997 | 252.805 | 972005.541 | 972005.541 | 972005.541 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 943.964 | 0.006 | 943.959 | 201.211 | 943964.497 | 943964.497 | 943964.497 |
| harness:await_cli | 1/1 | 0 | 0 | 940.140 | n/a | n/a | 75.683 | 940140.320 | 940140.320 | 940140.320 |
| llm:attempt | 28/28 | 0 | 0 | 852.193 | 3.982 | 848.207 | 23.154 | 30435.450 | 29653.558 | 67866.570 |
| tool:Bash | 18/18 | 0 | 0 | 181.799 | n/a | n/a | 50.015 | 10099.968 | 1021.772 | 38737.650 |
| tool:mcp__agency__trace | 22/22 | 0 | 0 | 29.840 | n/a | n/a | 0.005 | 1356.379 | 1227.317 | 2393.367 |
| run:container_call | 13/13 | 0 | 0 | 22.610 | 0.002 | 22.608 | 0.000 | 1739.267 | 34.302 | 8934.277 |
| teardown:commit | 1/1 | 0 | 0 | 21.970 | 0.004 | 21.966 | 0.000 | 21970.048 | 21970.048 | 21970.048 |
| sandbox:commit | 1/1 | 0 | 0 | 21.773 | 0.003 | 21.771 | 0.000 | 21773.454 | 21773.454 | 21773.454 |
| checkpoint.total | 1/1 | 0 | 0 | 21.773 | 0.003 | 21.771 | 0.000 | 21773.328 | 21773.328 | 21773.328 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 21.773 | 0.002 | 21.771 | 0.000 | 21773.195 | 21773.195 | 21773.195 |
| tool:mcp__agency__generate | 14/14 | 0 | 0 | 6.710 | n/a | n/a | 0.810 | 479.273 | 455.650 | 593.491 |
| tool:mcp__agency__patch | 13/13 | 0 | 0 | 4.905 | n/a | n/a | 0.000 | 377.294 | 373.724 | 397.210 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.677 | 1.038 | 3.638 | 50.934 | 4676.779 | 4676.779 | 4676.779 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.677 | 1.038 | 3.638 | 50.932 | 4676.510 | 4676.510 | 4676.510 |
| tool:mcp__agency__token_stats | 1/1 | 0 | 0 | 1.655 | n/a | n/a | 0.000 | 1655.430 | 1655.430 | 1655.430 |
| syscall:connect | 633/633 | 0 | 0 | 1.533 | n/a | n/a | 4.010 | 2.421 | 2.025 | 3.943 |
| tool:mcp__agency__attention | 2/2 | 0 | 0 | 1.502 | n/a | n/a | 0.002 | 751.139 | 751.139 | 1202.382 |
| harness:submit | 1/1 | 0 | 0 | 1.411 | n/a | n/a | 28.305 | 1410.537 | 1410.537 | 1410.537 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.225 | n/a | n/a | 69.803 | 1224.566 | 1224.566 | 1224.566 |
| tool:mcp__agency__logit_lens | 1/1 | 0 | 0 | 1.171 | n/a | n/a | 0.573 | 1170.921 | 1170.921 | 1170.921 |
| syscall:execve | 665/665 | 0 | 0 | 1.082 | n/a | n/a | 6.208 | 1.626 | 1.235 | 2.672 |
| sandbox:create | 1/1 | 0 | 0 | 1.043 | 0.255 | 0.788 | 0.000 | 1043.498 | 1043.498 | 1043.498 |
| syscall:sendto | 428/428 | 0 | 0 | 0.952 | n/a | n/a | 2.781 | 2.224 | 2.055 | 3.878 |
| tool:update_plan | 6/6 | 0 | 0 | 0.947 | n/a | n/a | 1.576 | 157.916 | 157.986 | 164.374 |
| harness:snapshot | 1/1 | 0 | 0 | 0.769 | n/a | n/a | 0.200 | 768.904 | 768.904 | 768.904 |
| run:detect | 1/1 | 0 | 0 | 0.728 | 0.001 | 0.727 | 0.000 | 728.123 | 728.123 | 728.123 |
| sandbox:start | 1/1 | 0 | 0 | 0.576 | 0.002 | 0.573 | 0.000 | 575.766 | 575.766 | 575.766 |
| runtime.container_create | 1/1 | 0 | 0 | 0.576 | 0.002 | 0.573 | 0.000 | 575.627 | 575.627 | 575.627 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.417 | n/a | n/a | 0.000 | 416.875 | 416.875 | 416.875 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.197 | n/a | n/a | 0.000 | 197.083 | 197.083 | 197.083 |
| sandbox:stop | 1/1 | 0 | 0 | 0.196 | 0.002 | 0.195 | 0.000 | 196.347 | 196.347 | 196.347 |
| agency:services_close | 1/1 | 0 | 0 | 0.144 | 0.000 | 0.143 | 0.000 | 143.510 | 143.510 | 143.510 |
| agency:services_start | 1/1 | 0 | 0 | 0.105 | 0.043 | 0.061 | 0.000 | 104.522 | 104.522 | 104.522 |
| harness:launch | 1/1 | 0 | 0 | 0.053 | n/a | n/a | 1.991 | 53.279 | 53.279 | 53.279 |
| agent:create | 1/1 | 0 | 0 | 0.052 | 0.009 | 0.043 | 0.000 | 51.525 | 51.525 | 51.525 |
| syscall:bind | 4/4 | 0 | 0 | 0.007 | n/a | n/a | 0.287 | 1.779 | 1.498 | 2.500 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.006 | 0.006 | 0.000 | 0.000 | 6.142 | 6.142 | 6.142 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.256 | 1.256 | 1.256 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.074 | 0.062 | 0.113 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.177 | 0.177 | 0.177 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.078 | 0.078 | 0.078 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 982 | 0.723 | 0.035 | 39.873 | 0.048 | 7.138833 CPU seconds | n/a |
| GPU 0 memory | MB | 984 | 11827.179 | 11670.000 | 11900.000 | 11848.000 | n/a | n/a |
| GPU 0 power | W | 984 | 29.539 | 28.157 | 55.326 | 28.592 | n/a | 29207.753 J |
| GPU 0 proc / 2160-22396 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 memory | MB | 984 | 3203.530 | 3118.000 | 3274.000 | 3222.000 | n/a | n/a |
| GPU 0 proc / 2160-22396 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 estimated power | W | 702 | 2.673 | 0.000 | 55.326 | 0.000 | n/a | n/a |
| GPU 0 proc / 2160-22396 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 utilization | percent | 702 | 1.581 | 0.000 | 47.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2220-26137 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 memory | MB | 984 | 8141.648 | 8070.000 | 8144.000 | 8144.000 | n/a | n/a |
| GPU 0 proc / 2220-26137 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 estimated power | W | 282 | 2.021 | 0.000 | 43.963 | 0.000 | n/a | n/a |
| GPU 0 proc / 2220-26137 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 utilization | percent | 282 | 0.791 | 0.000 | 26.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 984 | 11345.179 | 11188.000 | 11418.000 | 11366.000 | n/a | n/a |
| GPU 0 utilization | percent | 984 | 1.303 | 0.000 | 68.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 984 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 983 | 2.084 | 0.063 | 52.300 | 0.104 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 983 | 5.213 | 0.000 | 37.484 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 983 | 1.953 | 0.000 | 247.717 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 983 | 2.004 | 0.000 | 111.623 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 983 | 0.967 | 0.000 | 89.887 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 983 | 0.971 | 0.000 | 89.896 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 984 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 984 | 7031.612 | 6283.016 | 7955.770 | 7154.051 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 983 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 983 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 983 | 0.032 | 0.000 | 25.088 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 983 | 0.020 | 0.000 | 1.218 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2151) CPU | percent | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2151) io read MB/s | MB/s | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2151) io write MB/s | MB/s | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2151) rss_mb | MB | 984 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2151) main thread run-queue wait | percent | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2151) vms_mb | MB | 984 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2160) CPU | percent | 983 | 4.801 | 0.000 | 139.685 | 0.000 | 47.580000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2160) io read MB/s | MB/s | 983 | 0.173 | 0.000 | 93.213 | 0.000 | 171.402344 MB | n/a |
| Agency harness — python -m lsbench (PID 2160) io write MB/s | MB/s | 983 | 1.749 | 0.016 | 222.909 | 0.023 | 1733.894531 MB | n/a |
| Agency harness — python -m lsbench (PID 2160) rss_mb | MB | 984 | 2778.579 | 1982.066 | 3099.320 | 3041.719 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2160) main thread run-queue wait | percent | 983 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000006 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2160) vms_mb | MB | 984 | 16230.342 | 14062.980 | 16665.461 | 16430.852 | n/a | n/a |
| Python — vllm (PID 2169) CPU | percent | 983 | 0.159 | 0.000 | 10.944 | 0.000 | 1.570000 CPU seconds | n/a |
| Python — vllm (PID 2169) io read MB/s | MB/s | 983 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 2169) io write MB/s | MB/s | 983 | 0.000 | 0.000 | 0.008 | 0.000 | 0.074219 MB | n/a |
| Python — vllm (PID 2169) rss_mb | MB | 984 | 1787.584 | 1786.754 | 1787.879 | 1787.879 | n/a | n/a |
| Python — vllm (PID 2169) main thread run-queue wait | percent | 983 | 0.000 | 0.000 | 0.086 | 0.000 | 0.002470 run-queue seconds | n/a |
| Python — vllm (PID 2169) vms_mb | MB | 984 | 12022.707 | 11951.543 | 12024.562 | 12024.562 | n/a | n/a |
| Python — python -c (PID 2219) CPU | percent | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2219) io read MB/s | MB/s | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2219) io write MB/s | MB/s | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2219) rss_mb | MB | 984 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| Python — python -c (PID 2219) main thread run-queue wait | percent | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2219) vms_mb | MB | 984 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2220) CPU | percent | 983 | 1.432 | 0.000 | 35.792 | 1.992 | 14.160000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2220) io read MB/s | MB/s | 983 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 2220) io write MB/s | MB/s | 983 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 2220) rss_mb | MB | 984 | 2312.582 | 2312.309 | 2312.809 | 2312.809 | n/a | n/a |
| VLLM::EngineCore (PID 2220) main thread run-queue wait | percent | 983 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000243 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2220) vms_mb | MB | 984 | 21828.738 | 21828.738 | 21828.754 | 21828.738 | n/a | n/a |
| docker info (PID 2376) rss_mb | MB | 1 | 30.250 | 30.250 | 30.250 | 30.250 | n/a | n/a |
| docker info (PID 2376) vms_mb | MB | 1 | 2060.523 | 2060.523 | 2060.523 | 2060.523 | n/a | n/a |
| docker-buildx (PID 2390) rss_mb | MB | 1 | 41.727 | 41.727 | 41.727 | 41.727 | n/a | n/a |
| docker-buildx (PID 2390) vms_mb | MB | 1 | 1299.461 | 1299.461 | 1299.461 | 1299.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 2501) CPU | percent | 964 | 0.003 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 2501) rss_mb | MB | 965 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 2501) main thread run-queue wait | percent | 964 | 0.011 | 0.000 | 5.901 | 0.000 | 0.103385 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 2501) vms_mb | MB | 965 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 2543) CPU | percent | 964 | 0.003 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 2543) rss_mb | MB | 965 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 2543) main thread run-queue wait | percent | 964 | 0.004 | 0.000 | 4.030 | 0.000 | 0.043041 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 2543) vms_mb | MB | 965 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2647) CPU | percent | 964 | 25.248 | 0.000 | 92.574 | 0.000 | 244.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2647) rss_mb | MB | 965 | 110.805 | 2.992 | 123.832 | 123.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2647) main thread run-queue wait | percent | 964 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000100 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2647) vms_mb | MB | 965 | 989.960 | 4.262 | 1049.008 | 1046.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 2653) CPU | percent | 2 | 54.708 | 45.731 | 63.685 | 63.685 | 1.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 2653) rss_mb | MB | 3 | 44.665 | 10.922 | 75.754 | 75.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 2653) main thread run-queue wait | percent | 2 | 0.019 | 0.018 | 0.020 | 0.020 | 0.000386 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 2653) vms_mb | MB | 3 | 54.423 | 15.281 | 91.488 | 91.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2661) rss_mb | MB | 1 | 12.898 | 12.898 | 12.898 | 12.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2661) vms_mb | MB | 1 | 246.531 | 246.531 | 246.531 | 246.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2670) CPU | percent | 937 | 2.002 | 0.000 | 21.834 | 2.986 | 18.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2670) rss_mb | MB | 938 | 140.140 | 35.773 | 152.992 | 148.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2670) main thread run-queue wait | percent | 937 | 0.007 | 0.000 | 6.176 | 0.000 | 0.062913 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 2670) vms_mb | MB | 938 | 398.490 | 343.105 | 573.180 | 408.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 2701) rss_mb | MB | 1 | 3.312 | 3.312 | 3.312 | 3.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 2701) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 2706) rss_mb | MB | 1 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 2706) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 2710) rss_mb | MB | 1 | 17.871 | 17.871 | 17.871 | 17.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 2710) vms_mb | MB | 1 | 99.594 | 99.594 | 99.594 | 99.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 2745) rss_mb | MB | 1 | 3.828 | 3.828 | 3.828 | 3.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 2745) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 2750) rss_mb | MB | 1 | 4.965 | 4.965 | 4.965 | 4.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 2750) vms_mb | MB | 1 | 296.301 | 296.301 | 296.301 | 296.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2836) rss_mb | MB | 1 | 10.477 | 10.477 | 10.477 | 10.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2836) vms_mb | MB | 1 | 15.195 | 15.195 | 15.195 | 15.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2882) rss_mb | MB | 1 | 20.340 | 20.340 | 20.340 | 20.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2882) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2926) rss_mb | MB | 1 | 9.191 | 9.191 | 9.191 | 9.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2926) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2928) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2928) rss_mb | MB | 2 | 2.973 | 2.973 | 2.973 | 2.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2928) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 2928) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 2931) rss_mb | MB | 1 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 2931) vms_mb | MB | 1 | 4.930 | 4.930 | 4.930 | 4.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 2932) rss_mb | MB | 1 | 1.609 | 1.609 | 1.609 | 1.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 2932) vms_mb | MB | 1 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 2938) rss_mb | MB | 1 | 14.840 | 14.840 | 14.840 | 14.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 2938) vms_mb | MB | 1 | 368.617 | 368.617 | 368.617 | 368.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2970) rss_mb | MB | 1 | 8.441 | 8.441 | 8.441 | 8.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2970) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2984) rss_mb | MB | 1 | 8.211 | 8.211 | 8.211 | 8.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 2984) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3001) rss_mb | MB | 1 | 21.438 | 21.438 | 21.438 | 21.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3001) vms_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3080) rss_mb | MB | 1 | 19.348 | 19.348 | 19.348 | 19.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3080) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3086) rss_mb | MB | 1 | 21.777 | 21.777 | 21.777 | 21.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3086) vms_mb | MB | 1 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3143) rss_mb | MB | 1 | 21.637 | 21.637 | 21.637 | 21.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3143) vms_mb | MB | 1 | 27.008 | 27.008 | 27.008 | 27.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3144) rss_mb | MB | 1 | 3.137 | 3.137 | 3.137 | 3.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3144) vms_mb | MB | 1 | 4.371 | 4.371 | 4.371 | 4.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3179) rss_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3179) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3182) rss_mb | MB | 1 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3182) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3183) rss_mb | MB | 1 | 38.094 | 38.094 | 38.094 | 38.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3183) vms_mb | MB | 1 | 417.449 | 417.449 | 417.449 | 417.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3199) rss_mb | MB | 1 | 20.207 | 20.207 | 20.207 | 20.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3199) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3201) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3201) rss_mb | MB | 5 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3201) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3201) vms_mb | MB | 5 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3202) CPU | percent | 4 | 164.258 | 149.150 | 173.402 | 167.742 | 6.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3202) rss_mb | MB | 5 | 179.641 | 136.359 | 233.738 | 170.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3202) main thread run-queue wait | percent | 4 | 58.969 | 56.188 | 63.306 | 56.945 | 2.376406 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3202) vms_mb | MB | 5 | 615.145 | 581.172 | 666.918 | 603.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3209) rss_mb | MB | 1 | 21.266 | 21.266 | 21.266 | 21.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3209) vms_mb | MB | 1 | 26.746 | 26.746 | 26.746 | 26.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3211) rss_mb | MB | 1 | 15.703 | 15.703 | 15.703 | 15.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3211) vms_mb | MB | 1 | 20.539 | 20.539 | 20.539 | 20.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3237) rss_mb | MB | 1 | 18.004 | 18.004 | 18.004 | 18.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3237) vms_mb | MB | 1 | 24.176 | 24.176 | 24.176 | 24.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3288) rss_mb | MB | 1 | 14.738 | 14.738 | 14.738 | 14.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3288) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — geometry.py (PID 3312) rss_mb | MB | 1 | 56.598 | 56.598 | 56.598 | 56.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — geometry.py (PID 3312) vms_mb | MB | 1 | 437.762 | 437.762 | 437.762 | 437.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3370) rss_mb | MB | 1 | 2.652 | 2.652 | 2.652 | 2.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3370) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3396) rss_mb | MB | 1 | 8.344 | 8.344 | 8.344 | 8.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3396) vms_mb | MB | 1 | 13.285 | 13.285 | 13.285 | 13.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3398) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3398) rss_mb | MB | 8 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3398) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3398) vms_mb | MB | 8 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3399) CPU | percent | 7 | 170.486 | 161.573 | 179.754 | 171.822 | 12.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3399) rss_mb | MB | 8 | 392.638 | 64.230 | 447.297 | 440.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3399) main thread run-queue wait | percent | 7 | 49.463 | 44.170 | 55.016 | 44.170 | 3.498904 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3399) vms_mb | MB | 8 | 808.141 | 447.566 | 870.406 | 863.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3438) rss_mb | MB | 1 | 20.477 | 20.477 | 20.477 | 20.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3438) vms_mb | MB | 1 | 25.324 | 25.324 | 25.324 | 25.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3439) rss_mb | MB | 1 | 20.520 | 20.520 | 20.520 | 20.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3439) vms_mb | MB | 1 | 25.324 | 25.324 | 25.324 | 25.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3467) rss_mb | MB | 1 | 15.824 | 15.824 | 15.824 | 15.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3467) vms_mb | MB | 1 | 20.539 | 20.539 | 20.539 | 20.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3470) rss_mb | MB | 1 | 15.395 | 15.395 | 15.395 | 15.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3470) vms_mb | MB | 1 | 20.207 | 20.207 | 20.207 | 20.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3480) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3480) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3481) rss_mb | MB | 1 | 73.527 | 73.527 | 73.527 | 73.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3481) vms_mb | MB | 1 | 486.234 | 486.234 | 486.234 | 486.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3501) rss_mb | MB | 1 | 3.098 | 3.098 | 3.098 | 3.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3501) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3502) rss_mb | MB | 1 | 22.195 | 22.195 | 22.195 | 22.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3502) vms_mb | MB | 1 | 213.895 | 213.895 | 213.895 | 213.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3522) rss_mb | MB | 1 | 20.578 | 20.578 | 20.578 | 20.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3522) vms_mb | MB | 1 | 25.324 | 25.324 | 25.324 | 25.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3528) rss_mb | MB | 1 | 6.996 | 6.996 | 6.996 | 6.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3528) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3532) rss_mb | MB | 1 | 2.844 | 2.844 | 2.844 | 2.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3532) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3533) rss_mb | MB | 1 | 21.891 | 21.891 | 21.891 | 21.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 3533) vms_mb | MB | 1 | 213.688 | 213.688 | 213.688 | 213.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3547) rss_mb | MB | 1 | 7.938 | 7.938 | 7.938 | 7.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3547) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 3552) CPU | percent | 10 | 164.364 | 151.836 | 175.094 | 173.038 | 16.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 3552) rss_mb | MB | 11 | 482.189 | 48.324 | 591.727 | 591.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 3552) main thread run-queue wait | percent | 10 | 46.857 | 33.729 | 56.656 | 55.801 | 4.712152 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 3552) vms_mb | MB | 11 | 914.167 | 430.504 | 1092.480 | 1092.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3604) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3604) rss_mb | MB | 13 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3604) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 3604) vms_mb | MB | 13 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 3605) CPU | percent | 10 | 166.145 | 154.786 | 177.701 | 176.061 | 16.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 3605) rss_mb | MB | 11 | 504.642 | 127.016 | 582.430 | 581.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 3605) main thread run-queue wait | percent | 10 | 46.766 | 28.233 | 55.978 | 54.735 | 4.708749 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 3605) vms_mb | MB | 11 | 921.057 | 549.082 | 1004.191 | 1003.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — validate_adapter.py (PID 3618) CPU | percent | 1 | 164.797 | 164.797 | 164.797 | 164.797 | 1.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — validate_adapter.py (PID 3618) rss_mb | MB | 2 | 115.801 | 40.141 | 191.461 | 191.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — validate_adapter.py (PID 3618) main thread run-queue wait | percent | 1 | 52.765 | 52.765 | 52.765 | 52.765 | 0.531498 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — validate_adapter.py (PID 3618) vms_mb | MB | 2 | 526.072 | 421.043 | 631.102 | 631.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3642) rss_mb | MB | 1 | 20.773 | 20.773 | 20.773 | 20.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3642) vms_mb | MB | 1 | 25.582 | 25.582 | 25.582 | 25.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3655) rss_mb | MB | 1 | 20.539 | 20.539 | 20.539 | 20.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 3655) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| docker commit (PID 3696) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 3696) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3696) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3696) rss_mb | MB | 22 | 30.215 | 30.215 | 30.215 | 30.215 | n/a | n/a |
| docker commit (PID 3696) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 3696) vms_mb | MB | 22 | 1987.770 | 1987.770 | 1987.770 | 1987.770 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 964 | 36.341 | 0.000 | 208.143 | 0.000 | 352.557571 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 964 | 2.053 | 0.000 | 52.435 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 964 | 2.070 | 0.000 | 54.541 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 964 | 0.170 | 0.000 | 48.024 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 964 | 0.171 | 0.000 | 48.024 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 964 | 0.260 | 0.000 | 64.392 | 0.000 | 252.804688 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 964 | 0.182 | 0.000 | 69.039 | 0.000 | 176.492188 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 965 | 554.483 | 22.195 | 1153.547 | 402.098 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 964 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 964 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 964 | 0.026 | 0.000 | 24.282 | 0.000 | 24.938220 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 964 | 0.001 | 0.000 | 0.287 | 0.000 | 1.097149 MB | n/a |
| workload total CPU | percent | 983 | 6.428 | 1.466 | 141.254 | 1.726 | 63.677190 CPU seconds | n/a |
| workload total memory | MB | 984 | 9150.568 | 7890.004 | 9823.336 | 9810.594 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
