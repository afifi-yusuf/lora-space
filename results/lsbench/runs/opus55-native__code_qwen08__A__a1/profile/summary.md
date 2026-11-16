# agprof summary

- Duration: **1662.392 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **64 calls**, 64 succeeded, 0 failed, 0 interrupted, n/a reported retries, 845.419 s total wait
- Tools: **67/67 completed**, 1 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **155745** at 1.977 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1662209.183 / 1662209.183 ms |
| LLM latency p50 / p95 | 9792.263 / 31562.605 ms |
| LLM TTFT p50 / p95 | 4125.717 / 23688.271 ms |
| LLM input / output tokens | 130 / 94515 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 64 total, 64 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 472.461 / 22414.647 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 50/50 | 49 | 1 | 0 | 378.572 ms | 37648.340 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 822.831 ms | 822.831 ms |
| generate | 5/5 | 5 | 0 | 0 | 9320.258 ms | 11800.711 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 511.715 ms | 511.715 ms |
| patch | 2/2 | 2 | 0 | 0 | 425.915 ms | 438.381 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 234.707 ms | 234.707 ms |
| token_stats | 1/1 | 1 | 0 | 0 | 1589.321 ms | 1589.321 ms |
| trace | 6/6 | 6 | 0 | 0 | 3197.787 ms | 19539.469 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.001% | 110.098% | 83.151 s | 9679.776 MB | 11204.664 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker | 2609 |  | 16 | 0.398% | 1.992% | 0.060 s | 24.014 MB | 31.691 MB | 1589.638 MB | 1915.266 MB | 50.222656 MB | 0.000000 MB |
| lsb_grid_worker | 1955 |  | 1652 | 0.000% | 0.000% | 0.000 s | 3.320 MB | 3.320 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 2261 |  | 1652 | 2.402% | 57.732% | 39.940 s | 2553.926 MB | 2554.027 MB | 20940.238 MB | 20940.238 MB | 0.000000 MB | 0.011719 MB |
| python | 2260 |  | 1652 | 0.000% | 0.000% | 0.000 s | 12.207 MB | 12.207 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python | 2218 |  | 1652 | 2.369% | 108.346% | 39.390 s | 2834.726 MB | 4028.992 MB | 15748.804 MB | 17227.977 MB | 175.792969 MB | 2087.253906 MB |
| vllm | 2223 |  | 1652 | 0.197% | 6.968% | 3.270 s | 1779.680 MB | 1779.828 MB | 11042.192 MB | 11048.336 MB | 0.003906 MB | 0.031250 MB |
| docker-buildx | 2619 |  | 10 | 0.553% | 0.996% | 0.050 s | 12.259 MB | 28.312 MB | 1176.688 MB | 1296.570 MB | 34.460938 MB | 0.000000 MB |
| docker-compose | 2618 |  | 5 | 0.498% | 0.996% | 0.020 s | 6.837 MB | 13.004 MB | 1020.920 MB | 1260.309 MB | 15.890625 MB | 0.000000 MB |
| docker | 2676 |  | 4 | 0.332% | 0.995% | 0.010 s | 30.488 MB | 30.586 MB | 1907.832 MB | 1907.832 MB | 0.070312 MB | 0.000000 MB |
| docker | 2756 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.730 MB | 30.730 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 2719 | sandbox_agent_lsb-native_0000_0000 | 1629 | 0.002% | 0.995% | 0.030 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2754 | sandbox_agent_lsb-native_0000_0000 | 1629 | 0.002% | 0.995% | 0.030 s | 1.332 MB | 1.332 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 2846 | sandbox_agent_lsb-native_0000_0000 | 1629 | 3.328% | 96.288% | 54.500 s | 99.857 MB | 103.617 MB | 953.745 MB | 973.230 MB | n/a MB | n/a MB |
| python3 | 2852 | sandbox_agent_lsb-native_0000_0000 | 25 | 5.220% | 28.862% | 1.260 s | 36.896 MB | 81.020 MB | 45.482 MB | 96.543 MB | n/a MB | n/a MB |
| ldconfig | 2854 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.125 MB | 1.125 MB | n/a MB | n/a MB |
| python3 | 2864 | sandbox_agent_lsb-native_0000_0000 | 1240 | 0.182% | 63.663% | 2.270 s | 72.903 MB | 75.043 MB | 86.818 MB | 88.812 MB | n/a MB | n/a MB |
| python | 2881 | sandbox_agent_lsb-native_0000_0000 | 7 | 6.966% | 28.863% | 0.420 s | 16.294 MB | 26.195 MB | 138.456 MB | 219.168 MB | n/a MB | n/a MB |
| bash | 2877 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 3.039 MB | 3.039 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2964 | sandbox_agent_lsb-native_0000_0000 | 3 | 2.482% | 2.978% | 0.050 s | 12.982 MB | 13.023 MB | 17.085 MB | 17.090 MB | n/a MB | n/a MB |
| python | 2993 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.074 MB | 8.074 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| python | 3034 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.258 MB | 8.258 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| python | 3057 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.215 MB | 16.215 MB | 20.652 MB | 20.652 MB | n/a MB | n/a MB |
| python | 3102 | sandbox_agent_lsb-native_0000_0000 | 2 | 2.981% | 2.981% | 0.030 s | 13.223 MB | 13.223 MB | 17.125 MB | 17.125 MB | n/a MB | n/a MB |
| python | 3118 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.398 MB | 8.398 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| python | 3160 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| bash | 3221 | sandbox_agent_lsb-native_0000_0000 | 3 | 13.403% | 26.806% | 0.270 s | 8.711 MB | 20.758 MB | 73.542 MB | 212.195 MB | n/a MB | n/a MB |
| python | 3222 | sandbox_agent_lsb-native_0000_0000 | 2 | 2.976% | 2.976% | 0.030 s | 12.812 MB | 12.812 MB | 17.020 MB | 17.020 MB | n/a MB | n/a MB |
| python | 3255 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.555 MB | 7.555 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 3297 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.059 MB | 8.059 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| bash | 3330 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.094 MB | 3.094 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3359 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.035 MB | 3.035 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3366 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.469 MB | 8.469 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| python | 3360 | sandbox_agent_lsb-native_0000_0000 | 3 | 13.423% | 23.867% | 0.270 s | 16.022 MB | 22.434 MB | 82.757 MB | 214.254 MB | n/a MB | n/a MB |
| python | 3408 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.004 MB | 8.004 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python | 3570 | sandbox_agent_lsb-native_0000_0000 | 2 | 132.298% | 132.298% | 1.330 s | 66.342 MB | 119.398 MB | 275.188 MB | 343.074 MB | n/a MB | n/a MB |
| python | 3648 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.723 MB | 12.723 MB | 16.910 MB | 16.910 MB | n/a MB | n/a MB |
| python | 3654 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.176 MB | 7.176 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python | 3722 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 181.023 MB | 181.023 MB | 372.820 MB | 372.820 MB | n/a MB | n/a MB |
| python | 3730 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.117 MB | 13.117 MB | 207.215 MB | 207.215 MB | n/a MB | n/a MB |
| python | 3740 | sandbox_agent_lsb-native_0000_0000 | 8 | 188.002% | 198.889% | 13.240 s | 166.958 MB | 206.656 MB | 396.396 MB | 429.027 MB | n/a MB | n/a MB |
| bash | 3749 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| tail | 3752 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 2.840 MB | 2.840 MB | n/a MB | n/a MB |
| python | 3751 | sandbox_agent_lsb-native_0000_0000 | 7 | 200.021% | 201.340% | 12.100 s | 185.406 MB | 206.750 MB | 423.389 MB | 428.805 MB | n/a MB | n/a MB |
| python | 3771 | sandbox_agent_lsb-native_0000_0000 | 119 | 193.804% | 212.776% | 230.360 s | 463.261 MB | 542.809 MB | 682.824 MB | 754.223 MB | n/a MB | n/a MB |
| python | 3782 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.777 MB | 0.777 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| bash | 3781 | sandbox_agent_lsb-native_0000_0000 | 19 | 0.000% | 0.000% | 0.000 s | 1.501 MB | 2.863 MB | 2.890 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3783 | sandbox_agent_lsb-native_0000_0000 | 18 | 193.623% | 202.001% | 33.150 s | 491.913 MB | 608.887 MB | 779.099 MB | 918.520 MB | n/a MB | n/a MB |
| timeout | 3793 | sandbox_agent_lsb-native_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.434 MB | 1.434 MB | 2.816 MB | 2.816 MB | n/a MB | n/a MB |
| python | 3795 | sandbox_agent_lsb-native_0000_0000 | 15 | 197.592% | 206.403% | 27.860 s | 556.018 MB | 705.066 MB | 931.699 MB | 1013.637 MB | n/a MB | n/a MB |
| python | 3837 | sandbox_agent_lsb-native_0000_0000 | 53 | 197.717% | 203.749% | 103.540 s | 495.697 MB | 681.656 MB | 870.997 MB | 957.762 MB | n/a MB | n/a MB |
| timeout | 3835 | sandbox_agent_lsb-native_0000_0000 | 53 | 0.000% | 0.000% | 0.000 s | 1.461 MB | 1.461 MB | 2.816 MB | 2.816 MB | n/a MB | n/a MB |
| timeout | 3864 | sandbox_agent_lsb-native_0000_0000 | 53 | 0.000% | 0.000% | 0.000 s | 1.441 MB | 1.441 MB | 2.816 MB | 2.816 MB | n/a MB | n/a MB |
| python | 3866 | sandbox_agent_lsb-native_0000_0000 | 53 | 197.944% | 203.836% | 103.650 s | 501.152 MB | 646.914 MB | 878.004 MB | 956.355 MB | n/a MB | n/a MB |
| python | 3891 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 274.934 MB | 274.934 MB | 668.215 MB | 668.215 MB | n/a MB | n/a MB |
| python | 3901 | sandbox_agent_lsb-native_0000_0000 | 2 | 197.775% | 197.775% | 1.990 s | 160.818 MB | 161.422 MB | 380.164 MB | 380.168 MB | n/a MB | n/a MB |
| python | 3913 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 267.840 MB | 267.840 MB | 668.309 MB | 668.309 MB | n/a MB | n/a MB |
| bash | 3912 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.895 MB | 2.895 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3927 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.090 MB | 3.090 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| docker | 3956 |  | 119 | 0.008% | 0.995% | 0.010 s | 30.419 MB | 30.516 MB | 1771.516 MB | 1771.516 MB | 0.000000 MB | 0.000000 MB |
| docker | 4059 |  | 120 | 0.000% | 0.000% | 0.000 s | 30.418 MB | 30.418 MB | 1907.590 MB | 1907.590 MB | 0.000000 MB | 0.000000 MB |
| docker | 4082 |  | 118 | 0.000% | 0.000% | 0.000 s | 29.797 MB | 29.797 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.722% | 100.000% | 11541.772 MB | 11794.000 MB | 29.924 W | 73.531 W | 49695.823 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 37.613% | 212.542% | 616.602 s | 279.429 MB | 911.781 MB | 67.859375 MB | 1.539062 MB | 0.000534 MB | 0.000000 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2607 | 1662.215 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 1/1 | 0 | 0 | 1662.209 | 0.000 | 1662.209 | 67.859 | 1662209.268 | 1662209.268 | 1662209.268 |
| run:write_lora_adapter | 1/1 | 0 | 0 | 1662.209 | n/a | n/a | 67.859 | 1662209.183 | 1662209.183 | 1662209.183 |
| engine:execute | 1/1 | 0 | 0 | 1662.207 | 8.369 | 1653.799 | 67.859 | 1662207.491 | 1662207.491 | 1662207.491 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1247.609 | 0.003 | 1247.606 | 21.181 | 1247608.986 | 1247608.986 | 1247608.986 |
| turn | 64/64 | 0 | 0 | 1244.709 | n/a | n/a | 19.546 | 19448.571 | 12848.861 | 64048.518 |
| llm:attempt | 64/64 | 0 | 0 | 845.419 | 2.580 | 842.837 | 1.727 | 13209.665 | 9792.263 | 31562.605 |
| run:container_call | 15/15 | 2 | 0 | 365.827 | 0.003 | 365.824 | 0.042 | 24388.458 | 52.973 | 120089.513 |
| teardown:commit | 1/1 | 0 | 0 | 361.445 | 0.009 | 361.436 | 0.042 | 361445.193 | 361445.193 | 361445.193 |
| sandbox:commit | 1/1 | 0 | 0 | 361.127 | 0.007 | 361.120 | 0.042 | 361127.492 | 361127.492 | 361127.492 |
| checkpoint.total | 1/1 | 0 | 0 | 361.127 | 0.007 | 361.120 | 0.042 | 361127.360 | 361127.360 | 361127.360 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 361.127 | 0.007 | 361.120 | 0.042 | 361127.225 | 361127.225 | 361127.225 |
| tool:bash | 50/50 | 1 | 0 | 308.694 | n/a | n/a | 17.415 | 6173.877 | 378.572 | 37648.340 |
| process:bash | 50/50 | 3 | 0 | 308.242 | n/a | n/a | 17.379 | 6164.842 | 369.070 | 37636.921 |
| tool:generate | 5/5 | 0 | 0 | 42.236 | n/a | n/a | 0.000 | 8447.192 | 9320.258 | 11800.711 |
| tool:trace | 6/6 | 0 | 0 | 38.443 | n/a | n/a | 0.000 | 6407.150 | 3197.787 | 19539.469 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 35.437 | 7.179 | 28.257 | 46.530 | 35436.966 | 35436.966 | 35436.966 |
| runtime.harness_start | 1/1 | 0 | 0 | 35.437 | 7.179 | 28.257 | 46.530 | 35436.649 | 35436.649 | 35436.649 |
| sandbox:create | 1/1 | 0 | 0 | 16.949 | 0.248 | 16.701 | 0.000 | 16948.536 | 16948.536 | 16948.536 |
| run:detect | 1/1 | 0 | 0 | 16.474 | 0.001 | 16.473 | 0.000 | 16474.242 | 16474.242 | 16474.242 |
| sandbox:start | 1/1 | 0 | 0 | 6.354 | 0.002 | 6.352 | 0.000 | 6353.822 | 6353.822 | 6353.822 |
| runtime.container_create | 1/1 | 0 | 0 | 6.354 | 0.002 | 6.352 | 0.000 | 6353.658 | 6353.658 | 6353.658 |
| syscall:sendto | 1245/1245 | 0 | 0 | 3.109 | n/a | n/a | 0.134 | 2.497 | 2.181 | 4.884 |
| syscall:execve | 592/592 | 0 | 0 | 1.638 | n/a | n/a | 0.330 | 2.767 | 1.157 | 2.380 |
| tool:token_stats | 1/1 | 0 | 0 | 1.589 | n/a | n/a | 0.000 | 1589.321 | 1589.321 | 1589.321 |
| syscall:connect | 329/329 | 0 | 0 | 0.876 | n/a | n/a | 0.043 | 2.663 | 2.162 | 5.291 |
| tool:patch | 2/2 | 0 | 0 | 0.852 | n/a | n/a | 0.000 | 425.915 | 425.915 | 438.381 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.823 | n/a | n/a | 0.000 | 822.831 | 822.831 | 822.831 |
| tool:logit_lens | 1/1 | 0 | 0 | 0.512 | n/a | n/a | 0.000 | 511.715 | 511.715 | 511.715 |
| agency:services_start | 1/1 | 0 | 0 | 0.509 | 0.045 | 0.463 | 0.000 | 508.604 | 508.604 | 508.604 |
| sandbox:stop | 1/1 | 0 | 0 | 0.317 | 0.002 | 0.316 | 0.000 | 317.457 | 317.457 | 317.457 |
| tool:submit_output | 1/1 | 0 | 0 | 0.235 | n/a | n/a | 0.000 | 234.707 | 234.707 | 234.707 |
| agency:services_close | 1/1 | 0 | 0 | 0.174 | 0.000 | 0.173 | 0.009 | 173.667 | 173.667 | 173.667 |
| agent:create | 1/1 | 0 | 0 | 0.117 | 0.009 | 0.108 | 0.000 | 117.158 | 117.158 | 117.158 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 2.298 | 2.298 | 2.298 |
| sync:container | 15/15 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.098 | 0.071 | 0.253 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.251 | 1.251 | 1.251 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.219 | 0.219 | 0.219 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.053 | 0.053 | 0.053 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1628 | 0.627 | 0.039 | 85.830 | 14.948 | 10.259691 CPU seconds | n/a |
| GPU 0 memory | MB | 1652 | 11541.772 | 11326.000 | 11794.000 | 11580.000 | n/a | n/a |
| GPU 0 power | W | 1652 | 29.924 | 28.188 | 73.531 | 28.286 | n/a | 49695.823 J |
| GPU 0 proc / 2218-38248 / sandbox / ~ / device / GPU-271f4cab-2c99-4361-a9d7-17429dccf49d memory | MB | 1652 | 3185.845 | 3118.000 | 3420.000 | 3206.000 | n/a | n/a |
| GPU 0 proc / 2218-38248 / sandbox / ~ / device / GPU-271f4cab-2c99-4361-a9d7-17429dccf49d estimated power | W | 1374 | 0.566 | 0.000 | 73.531 | 0.000 | n/a | n/a |
| GPU 0 proc / 2218-38248 / sandbox / ~ / device / GPU-271f4cab-2c99-4361-a9d7-17429dccf49d utilization | percent | 1374 | 0.335 | 0.000 | 83.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2261-62584 / sandbox / ~ / device / GPU-271f4cab-2c99-4361-a9d7-17429dccf49d memory | MB | 1652 | 7873.926 | 7726.000 | 7892.000 | 7892.000 | n/a | n/a |
| GPU 0 proc / 2261-62584 / sandbox / ~ / device / GPU-271f4cab-2c99-4361-a9d7-17429dccf49d estimated power | W | 258 | 11.065 | 0.000 | 72.994 | 0.000 | n/a | n/a |
| GPU 0 proc / 2261-62584 / sandbox / ~ / device / GPU-271f4cab-2c99-4361-a9d7-17429dccf49d utilization | percent | 258 | 14.833 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1652 | 11059.771 | 10844.000 | 11312.000 | 11098.000 | n/a | n/a |
| GPU 0 utilization | percent | 1652 | 2.722 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1652 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1651 | 8.169 | 0.026 | 52.556 | 0.687 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1651 | 10.728 | 0.000 | 54.094 | 3.807 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1651 | 1.147 | 0.000 | 14.578 | 5.578 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1651 | 2.023 | 0.000 | 242.094 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1651 | 20.741 | 0.000 | 98.210 | 41.296 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1651 | 20.920 | 0.000 | 98.714 | 42.036 | n/a | n/a |
| host mem_total_mb | MB | 1652 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1652 | 7189.761 | 6406.988 | 8301.277 | 7341.465 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1651 | 0.002 | 0.000 | 1.420 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1651 | 0.002 | 0.000 | 1.429 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1651 | 0.283 | 0.000 | 130.736 | 0.001 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1651 | 0.014 | 0.000 | 0.617 | 0.001 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1955) CPU | percent | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1955) io read MB/s | MB/s | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1955) io write MB/s | MB/s | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1955) rss_mb | MB | 1652 | 3.320 | 3.320 | 3.320 | 3.320 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1955) main thread run-queue wait | percent | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1955) vms_mb | MB | 1652 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2218) CPU | percent | 1651 | 2.369 | 0.000 | 108.346 | 1.989 | 39.390000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2218) io read MB/s | MB/s | 1651 | 0.106 | 0.000 | 100.216 | 0.000 | 175.792969 MB | n/a |
| Agency harness — python -m lsbench (PID 2218) io write MB/s | MB/s | 1651 | 1.256 | 0.016 | 447.478 | 0.023 | 2087.253906 MB | n/a |
| Agency harness — python -m lsbench (PID 2218) rss_mb | MB | 1652 | 2834.726 | 2214.293 | 4028.992 | 3099.375 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2218) main thread run-queue wait | percent | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2218) vms_mb | MB | 1652 | 15748.804 | 13646.801 | 17227.977 | 16154.852 | n/a | n/a |
| Python — vllm (PID 2223) CPU | percent | 1651 | 0.197 | 0.000 | 6.968 | 0.000 | 3.270000 CPU seconds | n/a |
| Python — vllm (PID 2223) io read MB/s | MB/s | 1651 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 2223) io write MB/s | MB/s | 1651 | 0.000 | 0.000 | 0.008 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 2223) rss_mb | MB | 1652 | 1779.680 | 1778.305 | 1779.828 | 1779.828 | n/a | n/a |
| Python — vllm (PID 2223) main thread run-queue wait | percent | 1651 | 0.007 | 0.000 | 0.751 | 0.001 | 0.109513 run-queue seconds | n/a |
| Python — vllm (PID 2223) vms_mb | MB | 1652 | 11042.192 | 10975.316 | 11048.336 | 11048.336 | n/a | n/a |
| Python — python -c (PID 2260) CPU | percent | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2260) io read MB/s | MB/s | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2260) io write MB/s | MB/s | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2260) rss_mb | MB | 1652 | 12.207 | 12.207 | 12.207 | 12.207 | n/a | n/a |
| Python — python -c (PID 2260) main thread run-queue wait | percent | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2260) vms_mb | MB | 1652 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2261) CPU | percent | 1651 | 2.402 | 0.000 | 57.732 | 0.994 | 39.940000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2261) io read MB/s | MB/s | 1651 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 2261) io write MB/s | MB/s | 1651 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 2261) rss_mb | MB | 1652 | 2553.926 | 2553.402 | 2554.027 | 2554.027 | n/a | n/a |
| VLLM::EngineCore (PID 2261) main thread run-queue wait | percent | 1651 | 0.000 | 0.000 | 0.127 | 0.000 | 0.005644 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2261) vms_mb | MB | 1652 | 20940.238 | 20940.238 | 20940.238 | 20940.238 | n/a | n/a |
| docker info (PID 2609) CPU | percent | 15 | 0.398 | 0.000 | 1.992 | 0.000 | 0.060000 CPU seconds | n/a |
| docker info (PID 2609) io read MB/s | MB/s | 15 | 3.332 | 0.000 | 24.147 | 0.000 | 50.222656 MB | n/a |
| docker info (PID 2609) io write MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker info (PID 2609) rss_mb | MB | 16 | 24.014 | 1.582 | 31.691 | 31.691 | n/a | n/a |
| docker info (PID 2609) main thread run-queue wait | percent | 15 | 0.002 | 0.000 | 0.009 | 0.000 | 0.000249 run-queue seconds | n/a |
| docker info (PID 2609) vms_mb | MB | 16 | 1589.638 | 69.043 | 1915.266 | 1915.266 | n/a | n/a |
| docker-compose (PID 2618) CPU | percent | 4 | 0.498 | 0.000 | 0.996 | 0.996 | 0.020000 CPU seconds | n/a |
| docker-compose (PID 2618) io read MB/s | MB/s | 4 | 3.955 | 2.633 | 5.921 | 5.921 | 15.890625 MB | n/a |
| docker-compose (PID 2618) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker-compose (PID 2618) rss_mb | MB | 5 | 6.837 | 0.695 | 13.004 | 13.004 | n/a | n/a |
| docker-compose (PID 2618) main thread run-queue wait | percent | 4 | 0.002 | 0.000 | 0.007 | 0.000 | 0.000086 run-queue seconds | n/a |
| docker-compose (PID 2618) vms_mb | MB | 5 | 1020.920 | 63.613 | 1260.309 | 1260.309 | n/a | n/a |
| docker-buildx (PID 2619) CPU | percent | 9 | 0.553 | 0.000 | 0.996 | 0.996 | 0.050000 CPU seconds | n/a |
| docker-buildx (PID 2619) io read MB/s | MB/s | 9 | 3.813 | 1.342 | 7.527 | 5.290 | 34.460938 MB | n/a |
| docker-buildx (PID 2619) io write MB/s | MB/s | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker-buildx (PID 2619) rss_mb | MB | 10 | 12.259 | 0.961 | 28.312 | 28.312 | n/a | n/a |
| docker-buildx (PID 2619) main thread run-queue wait | percent | 9 | 0.002 | 0.000 | 0.007 | 0.007 | 0.000167 run-queue seconds | n/a |
| docker-buildx (PID 2619) vms_mb | MB | 10 | 1176.688 | 99.875 | 1296.570 | 1296.570 | n/a | n/a |
| docker run (PID 2676) CPU | percent | 3 | 0.332 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| docker run (PID 2676) io read MB/s | MB/s | 3 | 0.023 | 0.000 | 0.070 | 0.000 | 0.070312 MB | n/a |
| docker run (PID 2676) io write MB/s | MB/s | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker run (PID 2676) rss_mb | MB | 4 | 30.488 | 30.195 | 30.586 | 30.586 | n/a | n/a |
| docker run (PID 2676) main thread run-queue wait | percent | 3 | 0.001 | 0.000 | 0.004 | 0.000 | 0.000042 run-queue seconds | n/a |
| docker run (PID 2676) vms_mb | MB | 4 | 1907.832 | 1907.832 | 1907.832 | 1907.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2719) CPU | percent | 1628 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2719) rss_mb | MB | 1629 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2719) main thread run-queue wait | percent | 1628 | 0.007 | 0.000 | 5.133 | 0.000 | 0.117012 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2719) vms_mb | MB | 1629 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2754) CPU | percent | 1628 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2754) rss_mb | MB | 1629 | 1.332 | 1.332 | 1.332 | 1.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2754) main thread run-queue wait | percent | 1628 | 0.008 | 0.000 | 5.230 | 0.000 | 0.137406 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2754) vms_mb | MB | 1629 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| docker exec (PID 2756) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker exec (PID 2756) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker exec (PID 2756) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker exec (PID 2756) rss_mb | MB | 2 | 30.730 | 30.730 | 30.730 | 30.730 | n/a | n/a |
| docker exec (PID 2756) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker exec (PID 2756) vms_mb | MB | 2 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2846) CPU | percent | 1628 | 3.328 | 0.000 | 96.288 | 0.000 | 54.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2846) rss_mb | MB | 1629 | 99.857 | 0.309 | 103.617 | 103.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2846) main thread run-queue wait | percent | 1628 | 0.000 | 0.000 | 0.010 | 0.000 | 0.000168 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2846) vms_mb | MB | 1629 | 953.745 | 1.832 | 973.230 | 972.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2852) CPU | percent | 24 | 5.220 | 0.000 | 28.862 | 5.970 | 1.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2852) rss_mb | MB | 25 | 36.896 | 1.723 | 81.020 | 81.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2852) main thread run-queue wait | percent | 24 | 0.002 | 0.000 | 0.011 | 0.001 | 0.000525 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2852) vms_mb | MB | 25 | 45.482 | 9.508 | 96.543 | 96.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ldconfig (PID 2854) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ldconfig (PID 2854) vms_mb | MB | 1 | 1.125 | 1.125 | 1.125 | 1.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2864) CPU | percent | 1239 | 0.182 | 0.000 | 63.663 | 0.000 | 2.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2864) rss_mb | MB | 1240 | 72.903 | 26.230 | 75.043 | 73.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2864) main thread run-queue wait | percent | 1239 | 0.017 | 0.000 | 5.046 | 0.000 | 0.206756 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2864) vms_mb | MB | 1240 | 86.818 | 32.168 | 88.812 | 88.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2877) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2877) rss_mb | MB | 7 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2877) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2877) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2881) CPU | percent | 6 | 6.966 | 0.000 | 28.863 | 2.984 | 0.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2881) rss_mb | MB | 7 | 16.294 | 9.160 | 26.195 | 26.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2881) main thread run-queue wait | percent | 6 | 0.029 | 0.000 | 0.141 | 0.005 | 0.001735 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2881) vms_mb | MB | 7 | 138.456 | 13.352 | 219.168 | 219.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 2964) CPU | percent | 2 | 2.482 | 1.985 | 2.978 | 1.985 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 2964) rss_mb | MB | 3 | 12.982 | 12.898 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 2964) main thread run-queue wait | percent | 2 | 0.005 | 0.003 | 0.008 | 0.003 | 0.000109 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 2964) vms_mb | MB | 3 | 17.085 | 17.074 | 17.090 | 17.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpxxpd8ado.py (PID 2993) rss_mb | MB | 1 | 8.074 | 8.074 | 8.074 | 8.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpxxpd8ado.py (PID 2993) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpit78m71n.py (PID 3034) rss_mb | MB | 1 | 8.258 | 8.258 | 8.258 | 8.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpit78m71n.py (PID 3034) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmplumqx1ew.py (PID 3057) rss_mb | MB | 1 | 16.215 | 16.215 | 16.215 | 16.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmplumqx1ew.py (PID 3057) vms_mb | MB | 1 | 20.652 | 20.652 | 20.652 | 20.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3102) CPU | percent | 1 | 2.981 | 2.981 | 2.981 | 2.981 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3102) rss_mb | MB | 2 | 13.223 | 13.223 | 13.223 | 13.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3102) main thread run-queue wait | percent | 1 | 0.014 | 0.014 | 0.014 | 0.014 | 0.000142 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3102) vms_mb | MB | 2 | 17.125 | 17.125 | 17.125 | 17.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpkmapxb0_.py (PID 3118) rss_mb | MB | 1 | 8.398 | 8.398 | 8.398 | 8.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpkmapxb0_.py (PID 3118) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpmk42u076.py (PID 3160) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpmk42u076.py (PID 3160) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3221) CPU | percent | 2 | 13.403 | 0.000 | 26.806 | 26.806 | 0.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3221) rss_mb | MB | 3 | 8.711 | 2.688 | 20.758 | 20.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3221) main thread run-queue wait | percent | 2 | 5.466 | 0.000 | 10.932 | 10.932 | 0.110115 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3221) vms_mb | MB | 3 | 73.542 | 4.215 | 212.195 | 212.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3222) CPU | percent | 1 | 2.976 | 2.976 | 2.976 | 2.976 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3222) rss_mb | MB | 2 | 12.812 | 12.812 | 12.812 | 12.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3222) main thread run-queue wait | percent | 1 | 0.015 | 0.015 | 0.015 | 0.015 | 0.000150 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3222) vms_mb | MB | 2 | 17.020 | 17.020 | 17.020 | 17.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp_4234k5l.py (PID 3255) rss_mb | MB | 1 | 7.555 | 7.555 | 7.555 | 7.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp_4234k5l.py (PID 3255) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpwrt2akph.py (PID 3297) rss_mb | MB | 1 | 8.059 | 8.059 | 8.059 | 8.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpwrt2akph.py (PID 3297) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3330) rss_mb | MB | 1 | 3.094 | 3.094 | 3.094 | 3.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3330) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3359) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3359) rss_mb | MB | 3 | 3.035 | 3.035 | 3.035 | 3.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3359) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3359) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3360) CPU | percent | 2 | 13.423 | 2.978 | 23.867 | 23.867 | 0.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3360) rss_mb | MB | 3 | 16.022 | 12.754 | 22.434 | 22.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3360) main thread run-queue wait | percent | 2 | 4.784 | 0.011 | 9.558 | 9.558 | 0.096219 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_eval.py (PID 3360) vms_mb | MB | 3 | 82.757 | 17.008 | 214.254 | 214.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpfze1ge3e.py (PID 3366) rss_mb | MB | 1 | 8.469 | 8.469 | 8.469 | 8.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpfze1ge3e.py (PID 3366) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp_tqoc6n8.py (PID 3408) rss_mb | MB | 1 | 8.004 | 8.004 | 8.004 | 8.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp_tqoc6n8.py (PID 3408) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an1.py (PID 3570) CPU | percent | 1 | 132.298 | 132.298 | 132.298 | 132.298 | 1.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an1.py (PID 3570) rss_mb | MB | 2 | 66.342 | 13.285 | 119.398 | 119.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an1.py (PID 3570) main thread run-queue wait | percent | 1 | 39.123 | 39.123 | 39.123 | 39.123 | 0.393308 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an1.py (PID 3570) vms_mb | MB | 2 | 275.188 | 207.301 | 343.074 | 343.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_ho.py (PID 3648) rss_mb | MB | 1 | 12.723 | 12.723 | 12.723 | 12.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — run_ho.py (PID 3648) vms_mb | MB | 1 | 16.910 | 16.910 | 16.910 | 16.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpuh0et6y3.py (PID 3654) rss_mb | MB | 1 | 7.176 | 7.176 | 7.176 | 7.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpuh0et6y3.py (PID 3654) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an3.py (PID 3722) rss_mb | MB | 1 | 181.023 | 181.023 | 181.023 | 181.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an3.py (PID 3722) vms_mb | MB | 1 | 372.820 | 372.820 | 372.820 | 372.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an4.py (PID 3730) rss_mb | MB | 1 | 13.117 | 13.117 | 13.117 | 13.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an4.py (PID 3730) vms_mb | MB | 1 | 207.215 | 207.215 | 207.215 | 207.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an5.py (PID 3740) CPU | percent | 7 | 188.002 | 157.715 | 198.889 | 198.889 | 13.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an5.py (PID 3740) rss_mb | MB | 8 | 166.958 | 13.434 | 206.656 | 206.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an5.py (PID 3740) main thread run-queue wait | percent | 7 | 44.865 | 30.382 | 50.739 | 48.913 | 3.159512 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an5.py (PID 3740) vms_mb | MB | 8 | 396.396 | 207.227 | 429.027 | 428.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3749) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3749) rss_mb | MB | 7 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3749) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3749) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an5.py (PID 3751) CPU | percent | 6 | 200.021 | 198.585 | 201.340 | 198.857 | 12.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an5.py (PID 3751) rss_mb | MB | 7 | 185.406 | 168.652 | 206.750 | 206.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an5.py (PID 3751) main thread run-queue wait | percent | 6 | 50.518 | 49.457 | 51.925 | 49.457 | 3.056090 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an5.py (PID 3751) vms_mb | MB | 7 | 423.389 | 391.547 | 428.805 | 428.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3752) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3752) rss_mb | MB | 7 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3752) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3752) vms_mb | MB | 7 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an7.py (PID 3771) CPU | percent | 118 | 193.804 | 168.988 | 212.776 | 194.334 | 230.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an7.py (PID 3771) rss_mb | MB | 119 | 463.261 | 248.727 | 542.809 | 542.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an7.py (PID 3771) main thread run-queue wait | percent | 118 | 43.078 | 34.104 | 54.884 | 39.813 | 51.202511 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an7.py (PID 3771) vms_mb | MB | 119 | 682.824 | 460.156 | 754.223 | 754.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3781) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3781) rss_mb | MB | 19 | 1.501 | 1.426 | 2.863 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3781) main thread run-queue wait | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3781) vms_mb | MB | 19 | 2.890 | 2.816 | 4.215 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3782) rss_mb | MB | 1 | 0.777 | 0.777 | 0.777 | 0.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3782) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an7.py (PID 3783) CPU | percent | 17 | 193.623 | 134.194 | 202.001 | 200.337 | 33.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an7.py (PID 3783) rss_mb | MB | 18 | 491.913 | 381.598 | 608.887 | 507.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an7.py (PID 3783) main thread run-queue wait | percent | 17 | 47.803 | 25.677 | 54.413 | 54.041 | 8.184135 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an7.py (PID 3783) vms_mb | MB | 18 | 779.099 | 594.152 | 918.520 | 727.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3793) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3793) rss_mb | MB | 15 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3793) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3793) vms_mb | MB | 15 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an8.py (PID 3795) CPU | percent | 14 | 197.592 | 180.445 | 206.403 | 198.867 | 27.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an8.py (PID 3795) rss_mb | MB | 15 | 556.018 | 357.738 | 705.066 | 705.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an8.py (PID 3795) main thread run-queue wait | percent | 14 | 48.085 | 39.748 | 55.598 | 49.507 | 6.779726 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an8.py (PID 3795) vms_mb | MB | 15 | 931.699 | 570.367 | 1013.637 | 1013.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3835) CPU | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3835) rss_mb | MB | 53 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3835) main thread run-queue wait | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3835) vms_mb | MB | 53 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an9.py (PID 3837) CPU | percent | 52 | 197.717 | 156.734 | 203.749 | 197.790 | 103.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an9.py (PID 3837) rss_mb | MB | 53 | 495.697 | 13.441 | 681.656 | 648.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an9.py (PID 3837) main thread run-queue wait | percent | 52 | 47.321 | 24.383 | 55.411 | 49.284 | 24.780385 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an9.py (PID 3837) vms_mb | MB | 53 | 870.997 | 207.191 | 957.762 | 957.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3864) CPU | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3864) rss_mb | MB | 53 | 1.441 | 1.441 | 1.441 | 1.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3864) main thread run-queue wait | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3864) vms_mb | MB | 53 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an11.py (PID 3866) CPU | percent | 52 | 197.944 | 187.954 | 203.836 | 203.220 | 103.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an11.py (PID 3866) rss_mb | MB | 53 | 501.152 | 335.781 | 646.914 | 646.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an11.py (PID 3866) main thread run-queue wait | percent | 52 | 47.837 | 35.176 | 55.464 | 48.988 | 25.048306 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an11.py (PID 3866) vms_mb | MB | 53 | 878.004 | 547.043 | 956.355 | 956.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an13.py (PID 3891) rss_mb | MB | 1 | 274.934 | 274.934 | 274.934 | 274.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — an13.py (PID 3891) vms_mb | MB | 1 | 668.215 | 668.215 | 668.215 | 668.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 3901) CPU | percent | 1 | 197.775 | 197.775 | 197.775 | 197.775 | 1.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 3901) rss_mb | MB | 2 | 160.818 | 160.215 | 161.422 | 161.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 3901) main thread run-queue wait | percent | 1 | 48.980 | 48.980 | 48.980 | 48.980 | 0.492832 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 3901) vms_mb | MB | 2 | 380.164 | 380.160 | 380.168 | 380.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3912) rss_mb | MB | 1 | 2.895 | 2.895 | 2.895 | 2.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3912) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3913) rss_mb | MB | 1 | 267.840 | 267.840 | 267.840 | 267.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3913) vms_mb | MB | 1 | 668.309 | 668.309 | 668.309 | 668.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3927) rss_mb | MB | 1 | 3.090 | 3.090 | 3.090 | 3.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3927) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| docker commit (PID 3956) CPU | percent | 118 | 0.008 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| docker commit (PID 3956) io read MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3956) io write MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3956) rss_mb | MB | 119 | 30.419 | 30.387 | 30.516 | 30.387 | n/a | n/a |
| docker commit (PID 3956) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 3956) vms_mb | MB | 119 | 1771.516 | 1771.516 | 1771.516 | 1771.516 | n/a | n/a |
| docker commit (PID 4059) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4059) io read MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4059) io write MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4059) rss_mb | MB | 120 | 30.418 | 30.418 | 30.418 | 30.418 | n/a | n/a |
| docker commit (PID 4059) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4059) vms_mb | MB | 120 | 1907.590 | 1907.590 | 1907.590 | 1907.590 | n/a | n/a |
| docker commit (PID 4082) CPU | percent | 117 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4082) io read MB/s | MB/s | 117 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4082) io write MB/s | MB/s | 117 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4082) rss_mb | MB | 118 | 29.797 | 29.797 | 29.797 | 29.797 | n/a | n/a |
| docker commit (PID 4082) main thread run-queue wait | percent | 117 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4082) vms_mb | MB | 118 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 1628 | 37.613 | 0.000 | 212.542 | 0.000 | 616.601521 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1628 | 7.867 | 0.000 | 50.339 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1628 | 7.974 | 0.000 | 50.922 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 1628 | 1.816 | 0.000 | 99.573 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 1628 | 1.818 | 0.000 | 99.573 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 1628 | 0.041 | 0.000 | 3.623 | 0.000 | 67.859375 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 1628 | 0.001 | 0.000 | 0.688 | 0.000 | 1.539062 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 1629 | 279.429 | 6.195 | 911.781 | 160.898 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1628 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1628 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 1628 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000534 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 1628 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 1651 | 5.001 | 1.412 | 110.098 | 2.178 | 83.151275 CPU seconds | n/a |
| workload total memory | MB | 1652 | 9679.776 | 8292.148 | 11204.664 | 10419.473 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
