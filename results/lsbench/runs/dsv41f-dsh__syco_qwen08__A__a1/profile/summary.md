# agprof summary

- Duration: **720.143 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **83 calls**, 71 succeeded, 12 failed, 0 interrupted, n/a reported retries, 552.847 s total wait
- Tools: **69/69 completed**, 2 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **75026** at 1.973 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 705504.893 / 705504.893 ms |
| LLM latency p50 / p95 | 5591.119 / 15257.857 ms |
| LLM TTFT p50 / p95 | 2572.599 / 8147.569 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 83 total, 71 succeeded, 12 failed, 0 interrupted |
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
| bash | 44/44 | 42 | 2 | 0 | n/a | n/a |
| mcp__agency__attention | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 8/8 | 8 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 6/6 | 6 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 4/4 | 4 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.901% | 103.111% | 42.411 s | 8817.854 MB | 9025.641 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 2051 |  | 715 | 0.155% | 5.969% | 1.110 s | 1779.433 MB | 1779.461 MB | 11048.999 MB | 11051.348 MB | 0.007812 MB | 0.027344 MB |
| VLLM::EngineCor | 2086 |  | 715 | 1.698% | 40.517% | 12.200 s | 2309.895 MB | 2309.895 MB | 21204.074 MB | 21204.074 MB | 0.000000 MB | 0.003906 MB |
| sleep | 2153 |  | 36 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| lsb_guard.sh | 2045 |  | 715 | 0.000% | 0.000% | 0.000 s | 3.324 MB | 3.324 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 2085 |  | 715 | 0.000% | 0.000% | 0.000 s | 12.195 MB | 12.195 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python | 2040 |  | 715 | 3.969% | 102.137% | 28.530 s | 2905.608 MB | 3091.449 MB | 15982.803 MB | 16243.035 MB | 169.914062 MB | 119.429688 MB |
| docker | 2214 |  | 1 | n/a% | n/a% | n/a s | 30.043 MB | 30.043 MB | 1843.512 MB | 1843.512 MB | n/a MB | n/a MB |
| docker-buildx | 2224 |  | 1 | n/a% | n/a% | n/a s | 41.805 MB | 41.805 MB | 1298.727 MB | 1298.727 MB | n/a MB | n/a MB |
| lsb_grid_worker | 2031 |  | 715 | 0.000% | 0.000% | 0.000 s | 3.391 MB | 3.391 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 2448 | sandbox_agent_lsb-dsh_0000_0000 | 700 | 10.208% | 86.539% | 71.800 s | 105.001 MB | 108.402 MB | 960.555 MB | 973.391 MB | n/a MB | n/a MB |
| python3 | 2454 | sandbox_agent_lsb-dsh_0000_0000 | 3 | 55.054% | 64.389% | 1.110 s | 41.590 MB | 69.383 MB | 49.022 MB | 78.461 MB | n/a MB | n/a MB |
| docker-init | 2319 | sandbox_agent_lsb-dsh_0000_0000 | 700 | 0.001% | 0.995% | 0.010 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2354 | sandbox_agent_lsb-dsh_0000_0000 | 700 | 0.001% | 0.994% | 0.010 s | 1.312 MB | 1.312 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| MainThread | 2480 | sandbox_agent_lsb-dsh_0000_0000 | 670 | 1.450% | 90.353% | 9.760 s | 398.426 MB | 480.055 MB | 10196.928 MB | 10350.309 MB | n/a MB | n/a MB |
| sleep | 2592 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 2705 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.855 MB | 16.855 MB | 209.523 MB | 209.523 MB | n/a MB | n/a MB |
| sleep | 2714 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| head | 2717 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.301 MB | 1.301 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 2715 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.887 MB | 2.887 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 2716 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 102.926 MB | 102.926 MB | 2368.051 MB | 2368.051 MB | n/a MB | n/a MB |
| bash | 2731 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.688 MB | 2.688 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| grep | 2738 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| pip | 2737 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.934 MB | 14.934 MB | 18.590 MB | 18.590 MB | n/a MB | n/a MB |
| python3 | 2760 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2033.070 MB | 2033.070 MB | 2640.781 MB | 2640.781 MB | n/a MB | n/a MB |
| python3 | 2768 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 995.977 MB | 995.977 MB | 1230.512 MB | 1230.512 MB | n/a MB | n/a MB |
| sleep | 2783 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| head | 2819 | sandbox_agent_lsb-dsh_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.238 MB | 1.238 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 2818 | sandbox_agent_lsb-dsh_0000_0000 | 5 | 172.608% | 185.496% | 6.970 s | 885.910 MB | 1081.453 MB | 1102.016 MB | 1303.617 MB | n/a MB | n/a MB |
| bash | 2816 | sandbox_agent_lsb-dsh_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.699 MB | 2.699 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 2837 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 2851 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2054.680 MB | 2054.680 MB | 2640.906 MB | 2640.906 MB | n/a MB | n/a MB |
| sleep | 2872 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 2923 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 2924 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.699 MB | 19.699 MB | 211.848 MB | 211.848 MB | n/a MB | n/a MB |
| sleep | 2955 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 2982 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.086 MB | 9.086 MB | 13.500 MB | 13.500 MB | n/a MB | n/a MB |
| sleep | 2993 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 2994 | sandbox_agent_lsb-dsh_0000_0000 | 2 | 180.893% | 180.893% | 1.820 s | 36.926 MB | 36.996 MB | 258.676 MB | 258.676 MB | n/a MB | n/a MB |
| python3 | 3012 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 36.773 MB | 36.773 MB | 258.617 MB | 258.617 MB | n/a MB | n/a MB |
| sleep | 3020 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 3021 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.160 MB | 17.160 MB | 209.586 MB | 209.586 MB | n/a MB | n/a MB |
| python3 | 3036 | sandbox_agent_lsb-dsh_0000_0000 | 15 | 185.514% | 189.069% | 26.180 s | 88.580 MB | 138.199 MB | 306.291 MB | 355.055 MB | n/a MB | n/a MB |
| python3 | 3043 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 37.324 MB | 37.324 MB | 258.941 MB | 258.941 MB | n/a MB | n/a MB |
| sleep | 3052 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 3053 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.969 MB | 13.969 MB | 207.359 MB | 207.359 MB | n/a MB | n/a MB |
| MainThread | 3107 | sandbox_agent_lsb-dsh_0000_0000 | 15 | 183.772% | 189.938% | 25.930 s | 124.355 MB | 225.020 MB | 383.605 MB | 1066.969 MB | n/a MB | n/a MB |
| python3 | 3120 | sandbox_agent_lsb-dsh_0000_0000 | 15 | 185.749% | 188.992% | 26.190 s | 103.850 MB | 142.344 MB | 325.326 MB | 359.422 MB | n/a MB | n/a MB |
| sleep | 3126 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 3131 | sandbox_agent_lsb-dsh_0000_0000 | 16 | 185.789% | 188.465% | 28.060 s | 133.777 MB | 204.547 MB | 411.768 MB | 468.461 MB | n/a MB | n/a MB |
| docker | 3173 |  | 22 | 0.000% | 0.000% | 0.000 s | 31.027 MB | 31.027 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3190 |  | 22 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.136% | 100.000% | 11818.943 MB | 11934.000 MB | 28.898 W | 72.827 W | 20758.809 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-dsh_0000_0000 | 31.843% | 205.468% | 224.144 s | 691.761 MB | 2765.242 MB | 156.414062 MB | 94.582031 MB | 0.001083 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2212 | 720.078 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 705.505 | n/a | n/a | 156.414 | 705504.893 | 705504.893 | 705504.893 |
| engine:execute | 1/1 | 0 | 0 | 705.503 | 1.863 | 703.622 | 156.414 | 705503.043 | 705503.043 | 705503.043 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 676.876 | 0.002 | 676.875 | 114.535 | 676876.124 | 676876.124 | 676876.124 |
| llm:attempt | 83/83 | 12 | 0 | 552.847 | 8.109 | 544.733 | 9.060 | 6660.809 | 5591.119 | 15257.857 |
| tool:bash | 44/44 | 2 | 0 | 84.441 | n/a | n/a | 9.106 | 1919.103 | 396.264 | 14701.868 |
| run:container_call | 13/13 | 0 | 0 | 22.984 | 0.002 | 22.981 | 0.000 | 1767.969 | 37.747 | 9076.442 |
| teardown:commit | 1/1 | 0 | 0 | 22.338 | 0.005 | 22.333 | 0.000 | 22337.697 | 22337.697 | 22337.697 |
| sandbox:commit | 1/1 | 0 | 0 | 22.146 | 0.003 | 22.143 | 0.000 | 22145.614 | 22145.614 | 22145.614 |
| checkpoint.total | 1/1 | 0 | 0 | 22.145 | 0.003 | 22.143 | 0.000 | 22145.469 | 22145.469 | 22145.469 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.145 | 0.002 | 22.143 | 0.000 | 22145.312 | 22145.312 | 22145.312 |
| tool:mcp__agency__trace | 4/4 | 0 | 0 | 5.542 | n/a | n/a | 0.000 | 1385.541 | 1680.768 | 1714.533 |
| tool:mcp__agency__generate | 8/8 | 0 | 0 | 5.093 | n/a | n/a | 0.000 | 636.609 | 377.966 | 1631.979 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.825 | 1.078 | 3.746 | 40.023 | 4824.641 | 4824.641 | 4824.641 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.824 | 1.078 | 3.746 | 40.017 | 4824.455 | 4824.455 | 4824.455 |
| tool:mcp__agency__logit_lens | 1/1 | 0 | 0 | 2.691 | n/a | n/a | 0.000 | 2691.310 | 2691.310 | 2691.310 |
| tool:mcp__agency__patch | 6/6 | 0 | 0 | 1.318 | n/a | n/a | 0.000 | 219.745 | 218.459 | 229.084 |
| sandbox:create | 1/1 | 0 | 0 | 1.087 | 0.247 | 0.840 | 0.000 | 1086.586 | 1086.586 | 1086.586 |
| tool:mcp__agency__inspect | 1/1 | 0 | 0 | 0.758 | n/a | n/a | 0.000 | 757.662 | 757.662 | 757.662 |
| run:detect | 1/1 | 0 | 0 | 0.736 | 0.001 | 0.736 | 0.000 | 736.324 | 736.324 | 736.324 |
| sandbox:start | 1/1 | 0 | 0 | 0.578 | 0.002 | 0.576 | 0.000 | 578.211 | 578.211 | 578.211 |
| runtime.container_create | 1/1 | 0 | 0 | 0.578 | 0.002 | 0.576 | 0.000 | 578.079 | 578.079 | 578.079 |
| syscall:execve | 151/151 | 0 | 0 | 0.508 | n/a | n/a | 0.320 | 3.366 | 1.320 | 8.785 |
| syscall:connect | 245/245 | 0 | 0 | 0.438 | n/a | n/a | 0.310 | 1.787 | 1.547 | 3.110 |
| tool:mcp__agency__attribution | 2/2 | 0 | 0 | 0.235 | n/a | n/a | 0.000 | 117.516 | 117.516 | 122.634 |
| agency:services_close | 1/1 | 0 | 0 | 0.201 | 0.001 | 0.201 | 0.000 | 201.189 | 201.189 | 201.189 |
| sandbox:stop | 1/1 | 0 | 0 | 0.192 | 0.002 | 0.190 | 0.000 | 191.829 | 191.829 | 191.829 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.160 | n/a | n/a | 0.000 | 160.468 | 160.468 | 160.468 |
| tool:mcp__agency__attention | 1/1 | 0 | 0 | 0.125 | n/a | n/a | 0.000 | 125.342 | 125.342 | 125.342 |
| agency:services_start | 1/1 | 0 | 0 | 0.091 | 0.043 | 0.047 | 0.000 | 90.696 | 90.696 | 90.696 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.008 | 0.041 | 0.000 | 49.299 | 49.299 | 49.299 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.045 | n/a | n/a | 0.000 | 44.805 | 44.805 | 44.805 |
| syscall:sendto | 2/2 | 0 | 0 | 0.004 | n/a | n/a | 0.046 | 1.996 | 1.996 | 2.810 |
| syscall:bind | 1/1 | 0 | 0 | 0.003 | n/a | n/a | 0.029 | 2.575 | 2.575 | 2.575 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.201 | 1.201 | 1.201 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.072 | 0.068 | 0.116 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.856 | 0.856 | 0.856 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.175 | 0.175 | 0.175 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.079 | 0.079 | 0.079 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 713 | 1.152 | 0.042 | 51.691 | 0.075 | 8.261434 CPU seconds | n/a |
| GPU 0 memory | MB | 715 | 11818.943 | 11670.000 | 11934.000 | 11816.000 | n/a | n/a |
| GPU 0 power | W | 715 | 28.898 | 28.093 | 72.827 | 28.206 | n/a | 20758.809 J |
| GPU 0 proc / 2040-20687 / sandbox / ~ / device / GPU-93de64d8-162d-ad61-aaeb-0568a9136930 memory | MB | 715 | 3192.316 | 3118.000 | 3304.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 2040-20687 / sandbox / ~ / device / GPU-93de64d8-162d-ad61-aaeb-0568a9136930 estimated power | W | 653 | 1.137 | 0.000 | 54.210 | 0.000 | n/a | n/a |
| GPU 0 proc / 2040-20687 / sandbox / ~ / device / GPU-93de64d8-162d-ad61-aaeb-0568a9136930 utilization | percent | 653 | 0.502 | 0.000 | 45.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2086-24572 / sandbox / ~ / device / GPU-93de64d8-162d-ad61-aaeb-0568a9136930 memory | MB | 715 | 8144.624 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 2086-24572 / sandbox / ~ / device / GPU-93de64d8-162d-ad61-aaeb-0568a9136930 estimated power | W | 50 | 9.054 | 0.000 | 69.914 | 0.000 | n/a | n/a |
| GPU 0 proc / 2086-24572 / sandbox / ~ / device / GPU-93de64d8-162d-ad61-aaeb-0568a9136930 utilization | percent | 50 | 7.500 | 0.000 | 96.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 715 | 11336.940 | 11188.000 | 11452.000 | 11334.000 | n/a | n/a |
| GPU 0 utilization | percent | 715 | 1.136 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 715 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 714 | 6.255 | 0.058 | 62.351 | 0.280 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 714 | 9.375 | 0.251 | 51.716 | 0.251 | n/a | n/a |
| host disk_read_mb_s | MB/s | 714 | 2.637 | 0.000 | 204.560 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 714 | 0.380 | 0.000 | 88.607 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 714 | 1.226 | 0.000 | 82.291 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 714 | 1.238 | 0.000 | 82.558 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 715 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 715 | 7228.600 | 6562.539 | 9352.676 | 7029.883 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 714 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 714 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 714 | 0.016 | 0.000 | 0.249 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 714 | 0.021 | 0.000 | 0.316 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2031) CPU | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2031) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2031) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2031) rss_mb | MB | 715 | 3.391 | 3.391 | 3.391 | 3.391 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2031) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2031) vms_mb | MB | 715 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2040) CPU | percent | 714 | 3.969 | 0.000 | 102.137 | 0.000 | 28.530000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2040) io read MB/s | MB/s | 714 | 0.236 | 0.000 | 92.063 | 0.000 | 169.914062 MB | n/a |
| Agency harness — python -m lsbench (PID 2040) io write MB/s | MB/s | 714 | 0.166 | 0.015 | 4.241 | 0.023 | 119.429688 MB | n/a |
| Agency harness — python -m lsbench (PID 2040) rss_mb | MB | 715 | 2905.608 | 2312.164 | 3091.449 | 3091.449 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2040) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2040) vms_mb | MB | 715 | 15982.803 | 13774.809 | 16243.035 | 16218.902 | n/a | n/a |
| bash lsb_guard.sh (PID 2045) CPU | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 2045) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 2045) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 2045) rss_mb | MB | 715 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| bash lsb_guard.sh (PID 2045) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 2045) vms_mb | MB | 715 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Python — vllm (PID 2051) CPU | percent | 714 | 0.155 | 0.000 | 5.969 | 0.000 | 1.110000 CPU seconds | n/a |
| Python — vllm (PID 2051) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 2051) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.008 | 0.000 | 0.027344 MB | n/a |
| Python — vllm (PID 2051) rss_mb | MB | 715 | 1779.433 | 1778.586 | 1779.461 | 1779.461 | n/a | n/a |
| Python — vllm (PID 2051) main thread run-queue wait | percent | 714 | 0.006 | 0.000 | 0.547 | 0.000 | 0.043131 run-queue seconds | n/a |
| Python — vllm (PID 2051) vms_mb | MB | 715 | 11048.999 | 10978.328 | 11051.348 | 11051.348 | n/a | n/a |
| Python — python -c (PID 2085) CPU | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2085) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2085) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2085) rss_mb | MB | 715 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| Python — python -c (PID 2085) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2085) vms_mb | MB | 715 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2086) CPU | percent | 714 | 1.698 | 0.000 | 40.517 | 1.992 | 12.200000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2086) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 2086) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 2086) rss_mb | MB | 715 | 2309.895 | 2309.895 | 2309.895 | 2309.895 | n/a | n/a |
| VLLM::EngineCore (PID 2086) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.069 | 0.000 | 0.001904 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2086) vms_mb | MB | 715 | 21204.074 | 21204.074 | 21204.074 | 21204.074 | n/a | n/a |
| sleep (PID 2153) CPU | percent | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2153) io read MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2153) io write MB/s | MB/s | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2153) rss_mb | MB | 36 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2153) main thread run-queue wait | percent | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2153) vms_mb | MB | 36 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| docker info (PID 2214) rss_mb | MB | 1 | 30.043 | 30.043 | 30.043 | 30.043 | n/a | n/a |
| docker info (PID 2214) vms_mb | MB | 1 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| docker-buildx (PID 2224) rss_mb | MB | 1 | 41.805 | 41.805 | 41.805 | 41.805 | n/a | n/a |
| docker-buildx (PID 2224) vms_mb | MB | 1 | 1298.727 | 1298.727 | 1298.727 | 1298.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 2319) CPU | percent | 699 | 0.001 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 2319) rss_mb | MB | 700 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 2319) main thread run-queue wait | percent | 699 | 0.014 | 0.000 | 5.124 | 0.000 | 0.100988 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 2319) vms_mb | MB | 700 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 2354) CPU | percent | 699 | 0.001 | 0.000 | 0.994 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 2354) rss_mb | MB | 700 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 2354) main thread run-queue wait | percent | 699 | 0.010 | 0.000 | 4.105 | 0.000 | 0.067822 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 2354) vms_mb | MB | 700 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2448) CPU | percent | 699 | 10.208 | 0.000 | 86.539 | 0.000 | 71.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2448) rss_mb | MB | 700 | 105.001 | 2.980 | 108.402 | 107.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2448) main thread run-queue wait | percent | 699 | 0.000 | 0.000 | 0.016 | 0.000 | 0.000194 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2448) vms_mb | MB | 700 | 960.555 | 4.262 | 973.391 | 973.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2454) CPU | percent | 2 | 55.054 | 45.719 | 64.389 | 64.389 | 1.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2454) rss_mb | MB | 3 | 41.590 | 9.379 | 69.383 | 69.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2454) main thread run-queue wait | percent | 2 | 0.018 | 0.014 | 0.022 | 0.014 | 0.000363 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2454) vms_mb | MB | 3 | 49.022 | 13.523 | 78.461 | 78.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 2480) CPU | percent | 669 | 1.450 | 0.000 | 90.353 | 19.888 | 9.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 2480) rss_mb | MB | 670 | 398.426 | 157.324 | 480.055 | 295.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 2480) main thread run-queue wait | percent | 669 | 3.292 | 0.000 | 46.721 | 4.158 | 22.192791 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 2480) vms_mb | MB | 670 | 10196.928 | 1618.352 | 10350.309 | 1937.938 | n/a | n/a |
| sleep (PID 2592) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2592) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2592) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2592) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2592) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2592) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2705) rss_mb | MB | 1 | 16.855 | 16.855 | 16.855 | 16.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2705) vms_mb | MB | 1 | 209.523 | 209.523 | 209.523 | 209.523 | n/a | n/a |
| sleep (PID 2714) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2714) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2714) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2714) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2714) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2714) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2715) rss_mb | MB | 1 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2715) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2716) rss_mb | MB | 1 | 102.926 | 102.926 | 102.926 | 102.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2716) vms_mb | MB | 1 | 2368.051 | 2368.051 | 2368.051 | 2368.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — head (PID 2717) rss_mb | MB | 1 | 1.301 | 1.301 | 1.301 | 1.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — head (PID 2717) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2731) rss_mb | MB | 1 | 2.688 | 2.688 | 2.688 | 2.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2731) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — pip (PID 2737) rss_mb | MB | 1 | 14.934 | 14.934 | 14.934 | 14.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — pip (PID 2737) vms_mb | MB | 1 | 18.590 | 18.590 | 18.590 | 18.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — grep (PID 2738) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — grep (PID 2738) vms_mb | MB | 1 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2760) rss_mb | MB | 1 | 2033.070 | 2033.070 | 2033.070 | 2033.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2760) vms_mb | MB | 1 | 2640.781 | 2640.781 | 2640.781 | 2640.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2768) rss_mb | MB | 1 | 995.977 | 995.977 | 995.977 | 995.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2768) vms_mb | MB | 1 | 1230.512 | 1230.512 | 1230.512 | 1230.512 | n/a | n/a |
| sleep (PID 2783) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2783) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2783) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2783) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2783) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2783) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2816) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2816) rss_mb | MB | 5 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2816) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 2816) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2818) CPU | percent | 4 | 172.608 | 139.934 | 185.496 | 182.108 | 6.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2818) rss_mb | MB | 5 | 885.910 | 103.738 | 1081.453 | 1081.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2818) main thread run-queue wait | percent | 4 | 52.460 | 17.692 | 68.164 | 66.018 | 2.118556 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2818) vms_mb | MB | 5 | 1102.016 | 295.613 | 1303.617 | 1303.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — head (PID 2819) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — head (PID 2819) rss_mb | MB | 5 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — head (PID 2819) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — head (PID 2819) vms_mb | MB | 5 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sleep (PID 2837) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2837) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2837) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2837) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2837) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2837) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2851) rss_mb | MB | 1 | 2054.680 | 2054.680 | 2054.680 | 2054.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2851) vms_mb | MB | 1 | 2640.906 | 2640.906 | 2640.906 | 2640.906 | n/a | n/a |
| sleep (PID 2872) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2872) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2872) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2872) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2872) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2872) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 2923) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2923) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2923) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2923) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2923) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2923) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2924) rss_mb | MB | 1 | 19.699 | 19.699 | 19.699 | 19.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2924) vms_mb | MB | 1 | 211.848 | 211.848 | 211.848 | 211.848 | n/a | n/a |
| sleep (PID 2955) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2955) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2955) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2955) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2955) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2955) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2982) rss_mb | MB | 1 | 9.086 | 9.086 | 9.086 | 9.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2982) vms_mb | MB | 1 | 13.500 | 13.500 | 13.500 | 13.500 | n/a | n/a |
| sleep (PID 2993) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2993) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2993) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2993) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2993) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2993) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2994) CPU | percent | 1 | 180.893 | 180.893 | 180.893 | 180.893 | 1.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2994) rss_mb | MB | 2 | 36.926 | 36.855 | 36.996 | 36.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2994) main thread run-queue wait | percent | 1 | 73.230 | 73.230 | 73.230 | 73.230 | 0.736783 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 2994) vms_mb | MB | 2 | 258.676 | 258.676 | 258.676 | 258.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3012) rss_mb | MB | 1 | 36.773 | 36.773 | 36.773 | 36.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3012) vms_mb | MB | 1 | 258.617 | 258.617 | 258.617 | 258.617 | n/a | n/a |
| sleep (PID 3020) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3020) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3020) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3020) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3020) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3020) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3021) rss_mb | MB | 1 | 17.160 | 17.160 | 17.160 | 17.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3021) vms_mb | MB | 1 | 209.586 | 209.586 | 209.586 | 209.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3036) CPU | percent | 14 | 185.514 | 182.189 | 189.069 | 182.189 | 26.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3036) rss_mb | MB | 15 | 88.580 | 53.062 | 138.199 | 64.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3036) main thread run-queue wait | percent | 14 | 53.882 | 48.454 | 60.700 | 54.460 | 7.603291 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3036) vms_mb | MB | 15 | 306.291 | 270.977 | 355.055 | 280.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3043) rss_mb | MB | 1 | 37.324 | 37.324 | 37.324 | 37.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3043) vms_mb | MB | 1 | 258.941 | 258.941 | 258.941 | 258.941 | n/a | n/a |
| sleep (PID 3052) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3052) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3052) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3052) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3052) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3052) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — build_adapter.py (PID 3053) rss_mb | MB | 1 | 13.969 | 13.969 | 13.969 | 13.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — build_adapter.py (PID 3053) vms_mb | MB | 1 | 207.359 | 207.359 | 207.359 | 207.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 3107) CPU | percent | 14 | 183.772 | 160.926 | 189.938 | 186.863 | 25.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 3107) rss_mb | MB | 15 | 124.355 | 80.684 | 225.020 | 152.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 3107) main thread run-queue wait | percent | 14 | 52.588 | 39.870 | 58.748 | 49.007 | 7.420432 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 3107) vms_mb | MB | 15 | 383.605 | 299.188 | 1066.969 | 370.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3120) CPU | percent | 14 | 185.749 | 182.214 | 188.992 | 186.472 | 26.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3120) rss_mb | MB | 15 | 103.850 | 75.492 | 142.344 | 86.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3120) main thread run-queue wait | percent | 14 | 52.095 | 48.542 | 59.017 | 50.037 | 7.345131 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3120) vms_mb | MB | 15 | 325.326 | 298.953 | 359.422 | 359.422 | n/a | n/a |
| sleep (PID 3126) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3126) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3126) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3126) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3126) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3126) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3131) CPU | percent | 15 | 185.789 | 182.869 | 188.465 | 184.962 | 28.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3131) rss_mb | MB | 16 | 133.777 | 87.320 | 204.547 | 193.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3131) main thread run-queue wait | percent | 15 | 53.636 | 48.990 | 62.991 | 49.093 | 8.100990 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 3131) vms_mb | MB | 16 | 411.768 | 378.953 | 468.461 | 454.453 | n/a | n/a |
| docker commit (PID 3173) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 3173) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3173) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3173) rss_mb | MB | 22 | 31.027 | 31.027 | 31.027 | 31.027 | n/a | n/a |
| docker commit (PID 3173) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 3173) vms_mb | MB | 22 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| sleep (PID 3190) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3190) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3190) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3190) rss_mb | MB | 22 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3190) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3190) vms_mb | MB | 22 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 CPU | percent | 699 | 31.843 | 0.000 | 205.468 | 0.000 | 224.143639 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 699 | 5.146 | 0.000 | 50.356 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 699 | 6.132 | 0.000 | 61.680 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io_psi_full_pct | percent of wall time stalled | 699 | 0.183 | 0.000 | 32.875 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io_psi_some_pct | percent of wall time stalled | 699 | 0.185 | 0.000 | 32.875 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io read MB/s | MB/s | 699 | 0.222 | 0.000 | 54.488 | 0.000 | 156.414062 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io write MB/s | MB/s | 699 | 0.135 | 0.000 | 88.607 | 0.000 | 94.582031 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory | MB | 700 | 691.761 | 19.188 | 2765.242 | 274.590 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory_psi_full_pct | percent of wall time stalled | 699 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory_psi_some_pct | percent of wall time stalled | 699 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 net rx MB/s | MB/s | 699 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001083 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 net tx MB/s | MB/s | 699 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 714 | 5.901 | 1.593 | 103.111 | 2.236 | 42.411424 CPU seconds | n/a |
| workload total memory | MB | 715 | 8817.854 | 8205.832 | 9025.641 | 9017.277 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
