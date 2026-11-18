# agprof summary

- Duration: **930.121 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **31 calls**, 31 succeeded, 0 failed, 0 interrupted, n/a reported retries, 822.388 s total wait
- Tools: **85/85 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **86060** at 1.999 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 927259.092 / 927259.092 ms |
| LLM latency p50 / p95 | 27032.849 / 50557.069 ms |
| LLM TTFT p50 / p95 | 8121.118 / 10271.380 ms |
| LLM input / output tokens | 2422232 / 78979 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 31 total, 31 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 515.986 / 2324.413 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 4/4 | 4 | 0 | 0 | 287.006 ms | 579.126 ms |
| attribution | 1/1 | 1 | 0 | 0 | 322.172 ms | 322.172 ms |
| bash | 23/23 | 23 | 0 | 0 | 416.763 ms | 6305.889 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 350.175 ms | 350.175 ms |
| generate | 19/19 | 19 | 0 | 0 | 501.229 ms | 593.101 ms |
| inspect | 1/1 | 1 | 0 | 0 | 581.916 ms | 581.916 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 1110.706 ms | 1110.706 ms |
| patch | 11/11 | 11 | 0 | 0 | 406.478 ms | 414.601 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 227.178 ms | 227.178 ms |
| trace | 23/23 | 23 | 0 | 0 | 2125.329 ms | 2330.864 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 8.048% | 103.185% | 74.827 s | 6509.955 MB | 7276.820 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lsb_grid_worker | 12572 |  | 924 | 0.000% | 0.000% | 0.000 s | 3.387 MB | 3.387 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| tail | 12942 | sandbox_agent_lsb-native_0000_0000 | 922 | 0.001% | 0.995% | 0.010 s | 1.562 MB | 1.562 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 13048 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.845% | 99.845% | 1.010 s | 57.707 MB | 82.664 MB | 67.531 MB | 95.531 MB | n/a MB | n/a MB |
| python | 12581 |  | 924 | 6.053% | 102.136% | 56.310 s | 3048.665 MB | 3385.605 MB | 16628.111 MB | 16972.926 MB | 0.000000 MB | 2820.964844 MB |
| python | 12640 |  | 924 | 0.000% | 0.000% | 0.000 s | 12.188 MB | 12.188 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 12901 | sandbox_agent_lsb-native_0000_0000 | 922 | 0.002% | 0.994% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| vllm | 12590 |  | 924 | 0.187% | 10.940% | 1.740 s | 1783.779 MB | 1783.934 MB | 11990.974 MB | 11992.238 MB | 0.000000 MB | 0.089844 MB |
| VLLM::EngineCor | 12641 |  | 924 | 1.789% | 36.728% | 16.610 s | 2326.961 MB | 2327.117 MB | 21828.812 MB | 21828.812 MB | 0.000000 MB | 0.003906 MB |
| bash | 13042 | sandbox_agent_lsb-native_0000_0000 | 922 | 5.108% | 91.520% | 47.340 s | 109.289 MB | 117.160 MB | 966.941 MB | 975.133 MB | n/a MB | n/a MB |
| python3 | 13060 | sandbox_agent_lsb-native_0000_0000 | 916 | 0.438% | 45.667% | 4.030 s | 74.152 MB | 78.578 MB | 87.392 MB | 93.016 MB | n/a MB | n/a MB |
| bash | 13194 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.984 MB | 2.984 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 13195 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 32.086 MB | 32.086 MB | 51.191 MB | 51.191 MB | n/a MB | n/a MB |
| python | 13410 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.250 MB | 14.250 MB | 368.457 MB | 368.457 MB | n/a MB | n/a MB |
| python | 13531 | sandbox_agent_lsb-native_0000_0000 | 2 | 116.325% | 116.325% | 1.170 s | 210.047 MB | 375.098 MB | 447.715 MB | 629.668 MB | n/a MB | n/a MB |
| python | 13560 | sandbox_agent_lsb-native_0000_0000 | 7 | 182.330% | 197.930% | 11.010 s | 234.266 MB | 369.453 MB | 515.833 MB | 640.656 MB | n/a MB | n/a MB |
| python | 13568 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.762 MB | 23.762 MB | 375.578 MB | 375.578 MB | n/a MB | n/a MB |
| bash | 13565 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.754 MB | 2.754 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 13637 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.449 MB | 23.449 MB | 135.551 MB | 135.551 MB | n/a MB | n/a MB |
| python | 13652 | sandbox_agent_lsb-native_0000_0000 | 6 | 95.198% | 98.448% | 4.790 s | 137.402 MB | 177.773 MB | 303.390 MB | 348.531 MB | n/a MB | n/a MB |
| python | 13651 | sandbox_agent_lsb-native_0000_0000 | 2 | 85.291% | 85.291% | 0.860 s | 98.518 MB | 149.484 MB | 269.881 MB | 351.180 MB | n/a MB | n/a MB |
| bash | 13649 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 3.322 MB | 3.488 MB | 4.551 MB | 4.719 MB | n/a MB | n/a MB |
| python | 13708 | sandbox_agent_lsb-native_0000_0000 | 2 | 139.211% | 139.211% | 1.400 s | 164.115 MB | 318.656 MB | 303.928 MB | 594.383 MB | n/a MB | n/a MB |
| python | 13717 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 34.562 MB | 34.562 MB | 137.395 MB | 137.395 MB | n/a MB | n/a MB |
| bash | 13716 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.992 MB | 2.992 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 13719 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.008 MB | 3.008 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 13720 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 128.027 MB | 128.027 MB | 300.215 MB | 300.215 MB | n/a MB | n/a MB |
| python | 13838 | sandbox_agent_lsb-native_0000_0000 | 6 | 181.705% | 196.543% | 9.140 s | 357.335 MB | 445.781 MB | 632.906 MB | 720.848 MB | n/a MB | n/a MB |
| bash | 13843 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.801 MB | 2.801 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 13844 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 84.305 MB | 84.305 MB | 364.609 MB | 364.609 MB | n/a MB | n/a MB |
| bash | 13853 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.844 MB | 2.844 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 13856 | sandbox_agent_lsb-native_0000_0000 | 2 | 178.577% | 178.577% | 1.800 s | 115.607 MB | 183.406 MB | 365.154 MB | 461.867 MB | n/a MB | n/a MB |
| docker | 13915 |  | 1 | n/a% | n/a% | n/a s | 30.309 MB | 30.309 MB | 2059.789 MB | 2059.789 MB | n/a MB | n/a MB |
| docker | 13960 |  | 1 | n/a% | n/a% | n/a s | 20.969 MB | 20.969 MB | 1689.918 MB | 1689.918 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.960% | 84.000% | 11834.509 MB | 11876.000 MB | 29.339 W | 54.360 W | 27234.128 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 10.605% | 203.611% | 98.293 s | 156.161 MB | 578.074 MB | 0.000000 MB | 2.539062 MB | 0.000978 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 12772 | 930.066 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 927.259 | n/a | n/a | 0.000 | 927259.092 | 927259.092 | 927259.092 |
| engine:execute | 1/1 | 0 | 0 | 927.257 | 1.705 | 925.552 | 0.000 | 927257.339 | 927257.339 | 927257.339 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 921.241 | 0.004 | 921.237 | 0.000 | 921240.804 | 921240.804 | 921240.804 |
| turn | 31/31 | 0 | 0 | 917.787 | n/a | n/a | 0.000 | 29606.024 | 31401.023 | 54195.289 |
| llm:attempt | 31/31 | 0 | 0 | 822.388 | 4.138 | 818.249 | 0.000 | 26528.633 | 27032.849 | 50557.069 |
| tool:trace | 23/23 | 0 | 0 | 41.262 | n/a | n/a | 0.000 | 1794.021 | 2125.329 | 2330.864 |
| tool:bash | 23/23 | 0 | 0 | 32.079 | n/a | n/a | 0.000 | 1394.733 | 416.763 | 6305.889 |
| process:bash | 23/23 | 3 | 0 | 31.888 | n/a | n/a | 0.000 | 1386.455 | 408.267 | 6295.533 |
| tool:generate | 19/19 | 0 | 0 | 9.607 | n/a | n/a | 0.000 | 505.633 | 501.229 | 593.101 |
| tool:patch | 11/11 | 0 | 0 | 4.477 | n/a | n/a | 0.000 | 407.036 | 406.478 | 414.601 |
| syscall:sendto | 2001/2001 | 0 | 0 | 3.929 | n/a | n/a | 0.000 | 1.964 | 1.737 | 3.647 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.278 | 0.788 | 2.490 | 0.000 | 3278.413 | 3278.413 | 3278.413 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.278 | 0.788 | 2.490 | 0.000 | 3278.097 | 3278.097 | 3278.097 |
| run:container_call | 13/13 | 0 | 0 | 2.424 | 0.003 | 2.421 | 0.000 | 186.452 | 32.864 | 826.203 |
| teardown:commit | 1/1 | 0 | 0 | 2.051 | 0.004 | 2.047 | 0.000 | 2051.475 | 2051.475 | 2051.475 |
| sandbox:commit | 1/1 | 0 | 0 | 1.885 | 0.002 | 1.883 | 0.000 | 1885.403 | 1885.403 | 1885.403 |
| checkpoint.total | 1/1 | 0 | 0 | 1.885 | 0.002 | 1.883 | 0.000 | 1885.260 | 1885.260 | 1885.260 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.885 | 0.002 | 1.883 | 0.000 | 1885.109 | 1885.109 | 1885.109 |
| tool:attention | 4/4 | 0 | 0 | 1.489 | n/a | n/a | 0.000 | 372.167 | 287.006 | 579.126 |
| tool:logit_lens | 1/1 | 0 | 0 | 1.111 | n/a | n/a | 0.000 | 1110.706 | 1110.706 | 1110.706 |
| syscall:connect | 517/517 | 0 | 0 | 1.078 | n/a | n/a | 0.000 | 2.085 | 1.770 | 4.221 |
| tool:inspect | 1/1 | 0 | 0 | 0.582 | n/a | n/a | 0.000 | 581.916 | 581.916 | 581.916 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.350 | n/a | n/a | 0.000 | 350.175 | 350.175 | 350.175 |
| sandbox:create | 1/1 | 0 | 0 | 0.339 | 0.253 | 0.086 | 0.000 | 339.267 | 339.267 | 339.267 |
| tool:attribution | 1/1 | 0 | 0 | 0.322 | n/a | n/a | 0.000 | 322.172 | 322.172 | 322.172 |
| sandbox:start | 1/1 | 0 | 0 | 0.305 | 0.003 | 0.302 | 0.000 | 305.104 | 305.104 | 305.104 |
| runtime.container_create | 1/1 | 0 | 0 | 0.305 | 0.002 | 0.302 | 0.000 | 304.928 | 304.928 | 304.928 |
| tool:submit_output | 1/1 | 0 | 0 | 0.227 | n/a | n/a | 0.000 | 227.178 | 227.178 | 227.178 |
| agency:services_close | 1/1 | 0 | 0 | 0.184 | 0.000 | 0.184 | 0.000 | 184.345 | 184.345 | 184.345 |
| syscall:execve | 107/107 | 0 | 0 | 0.170 | n/a | n/a | 0.000 | 1.589 | 1.201 | 2.597 |
| sandbox:stop | 1/1 | 0 | 0 | 0.166 | 0.002 | 0.164 | 0.000 | 165.796 | 165.796 | 165.796 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.042 | 0.031 | 0.000 | 73.021 | 73.021 | 73.021 |
| run:detect | 1/1 | 0 | 0 | 0.049 | 0.001 | 0.048 | 0.000 | 48.515 | 48.515 | 48.515 |
| agent:create | 1/1 | 0 | 0 | 0.039 | 0.009 | 0.030 | 0.000 | 38.966 | 38.966 | 38.966 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 2.310 | 2.310 | 2.310 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.255 | 1.255 | 1.255 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.077 | 0.077 | 0.098 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.179 | 0.179 | 0.179 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.063 | 0.063 | 0.063 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 923 | 0.419 | 0.034 | 166.640 | 0.083 | 3.889993 CPU seconds | n/a |
| GPU 0 memory | MB | 924 | 11834.509 | 11670.000 | 11876.000 | 11844.000 | n/a | n/a |
| GPU 0 power | W | 924 | 29.339 | 28.121 | 54.360 | 28.196 | n/a | 27234.128 J |
| GPU 0 proc / 12581-851035 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb memory | MB | 924 | 3206.102 | 3118.000 | 3246.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 12581-851035 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb estimated power | W | 557 | 3.581 | 0.000 | 53.881 | 0.000 | n/a | n/a |
| GPU 0 proc / 12581-851035 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb utilization | percent | 557 | 2.594 | 0.000 | 46.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 12641-852794 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb memory | MB | 924 | 8146.407 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 12641-852794 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb estimated power | W | 375 | 1.612 | 0.000 | 45.664 | 0.000 | n/a | n/a |
| GPU 0 proc / 12641-852794 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb utilization | percent | 375 | 0.797 | 0.000 | 31.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 924 | 11352.509 | 11188.000 | 11394.000 | 11362.000 | n/a | n/a |
| GPU 0 utilization | percent | 924 | 1.960 | 0.000 | 84.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 924 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 923 | 0.476 | 0.030 | 15.929 | 0.139 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 923 | 2.277 | 0.125 | 26.027 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 923 | 0.000 | 0.000 | 0.124 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 923 | 3.075 | 0.000 | 158.210 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 923 | 0.310 | 0.000 | 27.496 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 923 | 0.312 | 0.000 | 27.610 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 924 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 924 | 7324.698 | 6540.246 | 8020.199 | 7422.395 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 923 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 923 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 923 | 0.006 | 0.000 | 0.253 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 923 | 0.020 | 0.000 | 1.197 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 12572) CPU | percent | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 12572) io read MB/s | MB/s | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 12572) io write MB/s | MB/s | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 12572) rss_mb | MB | 924 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 12572) main thread run-queue wait | percent | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 12572) vms_mb | MB | 924 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 12581) CPU | percent | 923 | 6.053 | 0.000 | 102.136 | 0.995 | 56.310000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 12581) io read MB/s | MB/s | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Agency harness — python -m lsbench (PID 12581) io write MB/s | MB/s | 923 | 3.032 | 0.016 | 214.241 | 0.093 | 2820.964844 MB | n/a |
| Agency harness — python -m lsbench (PID 12581) rss_mb | MB | 924 | 3048.665 | 2195.523 | 3385.605 | 3279.117 | n/a | n/a |
| Agency harness — python -m lsbench (PID 12581) main thread run-queue wait | percent | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 12581) vms_mb | MB | 924 | 16628.111 | 14276.027 | 16972.926 | 16753.805 | n/a | n/a |
| Python — vllm (PID 12590) CPU | percent | 923 | 0.187 | 0.000 | 10.940 | 0.000 | 1.740000 CPU seconds | n/a |
| Python — vllm (PID 12590) io read MB/s | MB/s | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 12590) io write MB/s | MB/s | 923 | 0.000 | 0.000 | 0.008 | 0.000 | 0.089844 MB | n/a |
| Python — vllm (PID 12590) rss_mb | MB | 924 | 1783.779 | 1782.809 | 1783.934 | 1783.934 | n/a | n/a |
| Python — vllm (PID 12590) main thread run-queue wait | percent | 923 | 0.000 | 0.000 | 0.005 | 0.000 | 0.001401 run-queue seconds | n/a |
| Python — vllm (PID 12590) vms_mb | MB | 924 | 11990.974 | 11919.219 | 11992.238 | 11992.238 | n/a | n/a |
| Python — python -c (PID 12640) CPU | percent | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 12640) io read MB/s | MB/s | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 12640) io write MB/s | MB/s | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 12640) rss_mb | MB | 924 | 12.188 | 12.188 | 12.188 | 12.188 | n/a | n/a |
| Python — python -c (PID 12640) main thread run-queue wait | percent | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 12640) vms_mb | MB | 924 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 12641) CPU | percent | 923 | 1.789 | 0.000 | 36.728 | 1.990 | 16.610000 CPU seconds | n/a |
| VLLM::EngineCore (PID 12641) io read MB/s | MB/s | 923 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 12641) io write MB/s | MB/s | 923 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 12641) rss_mb | MB | 924 | 2326.961 | 2326.742 | 2327.117 | 2327.117 | n/a | n/a |
| VLLM::EngineCore (PID 12641) main thread run-queue wait | percent | 923 | 0.000 | 0.000 | 0.006 | 0.000 | 0.000460 run-queue seconds | n/a |
| VLLM::EngineCore (PID 12641) vms_mb | MB | 924 | 21828.812 | 21828.812 | 21828.812 | 21828.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 12901) CPU | percent | 921 | 0.002 | 0.000 | 0.994 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 12901) rss_mb | MB | 922 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 12901) main thread run-queue wait | percent | 921 | 0.002 | 0.000 | 1.721 | 0.000 | 0.017489 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 12901) vms_mb | MB | 922 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 12942) CPU | percent | 921 | 0.001 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 12942) rss_mb | MB | 922 | 1.562 | 1.562 | 1.562 | 1.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 12942) main thread run-queue wait | percent | 921 | 0.002 | 0.000 | 1.484 | 0.001 | 0.015074 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 12942) vms_mb | MB | 922 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13042) CPU | percent | 921 | 5.108 | 0.000 | 91.520 | 0.000 | 47.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13042) rss_mb | MB | 922 | 109.289 | 2.922 | 117.160 | 116.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13042) main thread run-queue wait | percent | 921 | 0.000 | 0.000 | 0.009 | 0.001 | 0.000163 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13042) vms_mb | MB | 922 | 966.941 | 4.258 | 975.133 | 975.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 13048) CPU | percent | 1 | 99.845 | 99.845 | 99.845 | 99.845 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 13048) rss_mb | MB | 2 | 57.707 | 32.750 | 82.664 | 82.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 13048) main thread run-queue wait | percent | 1 | 0.009 | 0.009 | 0.009 | 0.009 | 0.000095 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 13048) vms_mb | MB | 2 | 67.531 | 39.531 | 95.531 | 95.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 13060) CPU | percent | 915 | 0.438 | 0.000 | 45.667 | 0.000 | 4.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 13060) rss_mb | MB | 916 | 74.152 | 26.000 | 78.578 | 77.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 13060) main thread run-queue wait | percent | 915 | 0.002 | 0.000 | 1.245 | 0.000 | 0.016484 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 13060) vms_mb | MB | 916 | 87.392 | 32.043 | 93.016 | 91.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13194) rss_mb | MB | 1 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13194) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13195) rss_mb | MB | 1 | 32.086 | 32.086 | 32.086 | 32.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13195) vms_mb | MB | 1 | 51.191 | 51.191 | 51.191 | 51.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — weights.py (PID 13410) rss_mb | MB | 1 | 14.250 | 14.250 | 14.250 | 14.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — weights.py (PID 13410) vms_mb | MB | 1 | 368.457 | 368.457 | 368.457 | 368.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 13531) CPU | percent | 1 | 116.325 | 116.325 | 116.325 | 116.325 | 1.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 13531) rss_mb | MB | 2 | 210.047 | 44.996 | 375.098 | 375.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 13531) main thread run-queue wait | percent | 1 | 6.379 | 6.379 | 6.379 | 6.379 | 0.064159 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 13531) vms_mb | MB | 2 | 447.715 | 265.762 | 629.668 | 629.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — roles.py (PID 13560) CPU | percent | 6 | 182.330 | 174.709 | 197.930 | 197.930 | 11.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — roles.py (PID 13560) rss_mb | MB | 7 | 234.266 | 47.648 | 369.453 | 200.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — roles.py (PID 13560) main thread run-queue wait | percent | 6 | 2.915 | 0.272 | 5.017 | 1.701 | 0.176038 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — roles.py (PID 13560) vms_mb | MB | 7 | 515.833 | 268.469 | 640.656 | 520.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13565) rss_mb | MB | 1 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13565) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13568) rss_mb | MB | 1 | 23.762 | 23.762 | 23.762 | 23.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13568) vms_mb | MB | 1 | 375.578 | 375.578 | 375.578 | 375.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reference.py (PID 13637) rss_mb | MB | 1 | 23.449 | 23.449 | 23.449 | 23.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reference.py (PID 13637) vms_mb | MB | 1 | 135.551 | 135.551 | 135.551 | 135.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13649) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13649) rss_mb | MB | 6 | 3.322 | 2.988 | 3.488 | 3.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13649) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13649) vms_mb | MB | 6 | 4.551 | 4.215 | 4.719 | 4.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reference.py (PID 13651) CPU | percent | 1 | 85.291 | 85.291 | 85.291 | 85.291 | 0.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reference.py (PID 13651) rss_mb | MB | 2 | 98.518 | 47.551 | 149.484 | 149.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reference.py (PID 13651) main thread run-queue wait | percent | 1 | 6.728 | 6.728 | 6.728 | 6.728 | 0.067840 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reference.py (PID 13651) vms_mb | MB | 2 | 269.881 | 188.582 | 351.180 | 351.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — keyread.py (PID 13652) CPU | percent | 5 | 95.198 | 87.274 | 98.448 | 97.482 | 4.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — keyread.py (PID 13652) rss_mb | MB | 6 | 137.402 | 47.551 | 177.773 | 176.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — keyread.py (PID 13652) main thread run-queue wait | percent | 5 | 1.901 | 0.002 | 6.821 | 0.004 | 0.095788 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — keyread.py (PID 13652) vms_mb | MB | 6 | 303.390 | 188.586 | 348.531 | 347.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — components.py (PID 13708) CPU | percent | 1 | 139.211 | 139.211 | 139.211 | 139.211 | 1.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — components.py (PID 13708) rss_mb | MB | 2 | 164.115 | 9.574 | 318.656 | 318.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — components.py (PID 13708) main thread run-queue wait | percent | 1 | 6.852 | 6.852 | 6.852 | 6.852 | 0.068907 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — components.py (PID 13708) vms_mb | MB | 2 | 303.928 | 13.473 | 594.383 | 594.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13716) rss_mb | MB | 1 | 2.992 | 2.992 | 2.992 | 2.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13716) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13717) rss_mb | MB | 1 | 34.562 | 34.562 | 34.562 | 34.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13717) vms_mb | MB | 1 | 137.395 | 137.395 | 137.395 | 137.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13719) rss_mb | MB | 1 | 3.008 | 3.008 | 3.008 | 3.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13719) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13720) rss_mb | MB | 1 | 128.027 | 128.027 | 128.027 | 128.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13720) vms_mb | MB | 1 | 300.215 | 300.215 | 300.215 | 300.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — source_factors.py (PID 13838) CPU | percent | 5 | 181.705 | 168.004 | 196.543 | 179.903 | 9.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — source_factors.py (PID 13838) rss_mb | MB | 6 | 357.335 | 265.480 | 445.781 | 322.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — source_factors.py (PID 13838) main thread run-queue wait | percent | 5 | 5.802 | 0.626 | 11.725 | 5.557 | 0.291848 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — source_factors.py (PID 13838) vms_mb | MB | 6 | 632.906 | 535.961 | 720.848 | 593.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13843) rss_mb | MB | 1 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13843) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13844) rss_mb | MB | 1 | 84.305 | 84.305 | 84.305 | 84.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 13844) vms_mb | MB | 1 | 364.609 | 364.609 | 364.609 | 364.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13853) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13853) rss_mb | MB | 2 | 2.844 | 2.844 | 2.844 | 2.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13853) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 13853) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 13856) CPU | percent | 1 | 178.577 | 178.577 | 178.577 | 178.577 | 1.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 13856) rss_mb | MB | 2 | 115.607 | 47.809 | 183.406 | 183.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 13856) main thread run-queue wait | percent | 1 | 16.604 | 16.604 | 16.604 | 16.604 | 0.167364 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 13856) vms_mb | MB | 2 | 365.154 | 268.441 | 461.867 | 461.867 | n/a | n/a |
| docker commit (PID 13915) rss_mb | MB | 1 | 30.309 | 30.309 | 30.309 | 30.309 | n/a | n/a |
| docker commit (PID 13915) vms_mb | MB | 1 | 2059.789 | 2059.789 | 2059.789 | 2059.789 | n/a | n/a |
| docker inspect (PID 13960) rss_mb | MB | 1 | 20.969 | 20.969 | 20.969 | 20.969 | n/a | n/a |
| docker inspect (PID 13960) vms_mb | MB | 1 | 1689.918 | 1689.918 | 1689.918 | 1689.918 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 921 | 10.605 | 0.038 | 203.611 | 0.038 | 98.293352 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 921 | 0.616 | 0.000 | 16.225 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 921 | 0.619 | 0.000 | 16.225 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 921 | 0.000 | 0.000 | 0.002 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 921 | 0.000 | 0.000 | 0.002 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 921 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 921 | 0.003 | 0.000 | 0.708 | 0.000 | 2.539062 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 922 | 156.161 | 25.426 | 578.074 | 104.168 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 921 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 921 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 921 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000978 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 921 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 923 | 8.048 | 1.355 | 103.185 | 2.200 | 74.827439 CPU seconds | n/a |
| workload total memory | MB | 924 | 6509.955 | 4838.879 | 7276.820 | 7240.895 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
