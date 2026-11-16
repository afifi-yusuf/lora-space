# agprof summary

- Duration: **11190.874 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **78 calls**, 78 succeeded, 0 failed, 0 interrupted, n/a reported retries, 10566.332 s total wait
- Tools: **120/120 completed**, 1 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **1102949** at 1.974 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 11165492.419 / 11165492.419 ms |
| LLM latency p50 / p95 | 94960.447 / 335487.085 ms |
| LLM TTFT p50 / p95 | 75739.086 / 327215.465 ms |
| LLM input / output tokens | 13702812 / 90982 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 78 total, 78 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1024.254 / 18441.747 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 1/1 | 1 | 0 | 0 | 324.114 ms | 324.114 ms |
| attribution | 4/4 | 4 | 0 | 0 | 314.219 ms | 321.040 ms |
| bash | 47/47 | 46 | 1 | 0 | 1781.545 ms | 62774.930 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 363.153 ms | 363.153 ms |
| generate | 7/7 | 7 | 0 | 0 | 1290.228 ms | 1790.249 ms |
| get_current_resources | 1/1 | 1 | 0 | 0 | 237.630 ms | 237.630 ms |
| inspect | 8/8 | 8 | 0 | 0 | 1779.699 ms | 1851.311 ms |
| inspect_module_inputs | 8/8 | 8 | 0 | 0 | 1843.427 ms | 1885.945 ms |
| patch | 19/19 | 19 | 0 | 0 | 413.300 ms | 419.515 ms |
| read | 6/6 | 6 | 0 | 0 | 0.529 ms | 1.082 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 241.316 ms | 241.316 ms |
| submitted_output | 1/1 | 1 | 0 | 0 | 240.963 ms | 240.963 ms |
| todowrite | 4/4 | 4 | 0 | 0 | 0.145 ms | 0.230 ms |
| token_stats | 2/2 | 2 | 0 | 0 | 2469.283 ms | 2754.126 ms |
| top_activations | 6/6 | 6 | 0 | 0 | 3538.083 ms | 3771.164 ms |
| trace | 2/2 | 2 | 0 | 0 | 1186.518 ms | 1444.253 ms |
| write | 2/2 | 2 | 0 | 0 | 0.405 ms | 0.434 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 2.941% | 116.453% | 329.339 s | 9223.150 MB | 9854.238 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 1759 |  | 11132 | 0.088% | 7.962% | 9.840 s | 1766.957 MB | 1767.137 MB | 11021.272 MB | 11036.051 MB | 0.007812 MB | 0.042969 MB |
| python | 1793 |  | 11132 | 0.000% | 0.000% | 0.000 s | 12.195 MB | 12.195 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python | 1897 |  | 11132 | 0.024% | 4.973% | 2.730 s | 46.208 MB | 47.121 MB | 203.537 MB | 204.273 MB | 0.113281 MB | 0.281250 MB |
| python | 1730 |  | 11132 | 1.324% | 114.758% | 148.370 s | 3174.060 MB | 3561.848 MB | 16135.768 MB | 16924.559 MB | 78.382812 MB | 987.000000 MB |
| lsb_grid_worker | 1721 |  | 11132 | 0.000% | 0.000% | 0.000 s | 3.363 MB | 3.363 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 1794 |  | 11132 | 1.502% | 51.370% | 168.070 s | 2313.909 MB | 2314.000 MB | 21203.184 MB | 21203.184 MB | 0.000000 MB | 0.074219 MB |
| python3 | 2144 | sandbox_agent_lsb-native_0000_0000 | 3 | 57.156% | 61.692% | 1.150 s | 49.835 MB | 77.848 MB | 61.204 MB | 93.281 MB | n/a MB | n/a MB |
| tail | 2046 | sandbox_agent_lsb-native_0000_0000 | 11106 | 0.003% | 0.996% | 0.310 s | 1.309 MB | 1.309 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| docker-init | 2012 | sandbox_agent_lsb-native_0000_0000 | 11106 | 0.002% | 0.995% | 0.250 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 2138 | sandbox_agent_lsb-native_0000_0000 | 11106 | 2.526% | 82.192% | 282.060 s | 103.904 MB | 111.301 MB | 961.047 MB | 972.781 MB | n/a MB | n/a MB |
| python3 | 2156 | sandbox_agent_lsb-native_0000_0000 | 11080 | 0.043% | 63.561% | 4.780 s | 72.441 MB | 75.227 MB | 86.489 MB | 89.773 MB | n/a MB | n/a MB |
| bash | 2526 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.816 MB | 2.816 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 2528 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.988 MB | 22.988 MB | 215.582 MB | 215.582 MB | n/a MB | n/a MB |
| python3 | 2730 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.863 MB | 8.863 MB | 13.188 MB | 13.188 MB | n/a MB | n/a MB |
| python3 | 2891 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1527.586 MB | 1527.586 MB | 1757.777 MB | 1757.777 MB | n/a MB | n/a MB |
| python3 | 2908 | sandbox_agent_lsb-native_0000_0000 | 3 | 120.218% | 161.940% | 2.420 s | 441.089 MB | 1119.270 MB | 923.376 MB | 1537.406 MB | n/a MB | n/a MB |
| python3 | 2979 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.422 MB | 6.422 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 2997 | sandbox_agent_lsb-native_0000_0000 | 3 | 142.073% | 187.787% | 2.860 s | 814.587 MB | 1266.535 MB | 1330.846 MB | 2015.395 MB | n/a MB | n/a MB |
| bash | 3034 | sandbox_agent_lsb-native_0000_0000 | 4 | 150.133% | 200.119% | 4.540 s | 616.518 MB | 1153.277 MB | 922.607 MB | 1570.664 MB | n/a MB | n/a MB |
| python3 | 3131 | sandbox_agent_lsb-native_0000_0000 | 2 | 95.342% | 95.342% | 0.960 s | 229.947 MB | 444.238 MB | 626.973 MB | 1045.543 MB | n/a MB | n/a MB |
| python3 | 3276 | sandbox_agent_lsb-native_0000_0000 | 3 | 123.150% | 145.025% | 2.480 s | 764.346 MB | 2113.973 MB | 1033.918 MB | 2531.484 MB | n/a MB | n/a MB |
| python3 | 3348 | sandbox_agent_lsb-native_0000_0000 | 2 | 94.287% | 94.287% | 0.950 s | 241.562 MB | 464.926 MB | 627.805 MB | 1045.590 MB | n/a MB | n/a MB |
| python3 | 3364 | sandbox_agent_lsb-native_0000_0000 | 2 | 105.236% | 105.236% | 1.060 s | 620.275 MB | 1196.809 MB | 1021.322 MB | 1614.234 MB | n/a MB | n/a MB |
| python3 | 3406 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 74.906 MB | 74.906 MB | 473.078 MB | 473.078 MB | n/a MB | n/a MB |
| python3 | 3460 | sandbox_agent_lsb-native_0000_0000 | 3 | 165.079% | 193.110% | 3.330 s | 865.353 MB | 1262.133 MB | 1272.267 MB | 1679.234 MB | n/a MB | n/a MB |
| python3 | 3475 | sandbox_agent_lsb-native_0000_0000 | 4 | 151.819% | 172.094% | 4.580 s | 926.708 MB | 1217.660 MB | 1335.753 MB | 1634.305 MB | n/a MB | n/a MB |
| python3 | 3491 | sandbox_agent_lsb-native_0000_0000 | 2 | 93.466% | 93.466% | 0.940 s | 644.000 MB | 1250.441 MB | 1217.342 MB | 2014.621 MB | n/a MB | n/a MB |
| python3 | 3505 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 91.738 MB | 91.738 MB | 493.598 MB | 493.598 MB | n/a MB | n/a MB |
| python3 | 3607 | sandbox_agent_lsb-native_0000_0000 | 119 | 190.189% | 205.321% | 226.070 s | 437.014 MB | 529.219 MB | 853.759 MB | 937.359 MB | n/a MB | n/a MB |
| python3 | 3626 | sandbox_agent_lsb-native_0000_0000 | 8 | 151.617% | 164.877% | 10.680 s | 150.236 MB | 174.316 MB | 512.854 MB | 592.574 MB | n/a MB | n/a MB |
| python3 | 3641 | sandbox_agent_lsb-native_0000_0000 | 2 | 113.148% | 113.148% | 1.140 s | 58.141 MB | 93.230 MB | 361.346 MB | 508.133 MB | n/a MB | n/a MB |
| python3 | 3657 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 28.230 MB | 28.230 MB | 250.883 MB | 250.883 MB | n/a MB | n/a MB |
| python3 | 3712 | sandbox_agent_lsb-native_0000_0000 | 2 | 147.972% | 147.972% | 1.490 s | 131.844 MB | 187.906 MB | 534.389 MB | 606.555 MB | n/a MB | n/a MB |
| python3 | 3775 | sandbox_agent_lsb-native_0000_0000 | 3 | 163.540% | 197.848% | 3.290 s | 788.003 MB | 1143.703 MB | 1200.608 MB | 1562.469 MB | n/a MB | n/a MB |
| python3 | 3791 | sandbox_agent_lsb-native_0000_0000 | 62 | 193.127% | 198.451% | 118.610 s | 92.766 MB | 123.004 MB | 312.368 MB | 341.629 MB | n/a MB | n/a MB |
| python3 | 3830 | sandbox_agent_lsb-native_0000_0000 | 68 | 189.353% | 195.504% | 127.750 s | 93.652 MB | 118.797 MB | 313.329 MB | 337.602 MB | n/a MB | n/a MB |
| python3 | 3895 | sandbox_agent_lsb-native_0000_0000 | 62 | 190.244% | 195.412% | 116.930 s | 98.017 MB | 118.910 MB | 318.369 MB | 340.309 MB | n/a MB | n/a MB |
| python3 | 3919 | sandbox_agent_lsb-native_0000_0000 | 2 | 149.999% | 149.999% | 1.510 s | 164.273 MB | 226.484 MB | 568.369 MB | 643.121 MB | n/a MB | n/a MB |
| python3 | 3957 | sandbox_agent_lsb-native_0000_0000 | 3 | 124.721% | 149.144% | 2.510 s | 450.762 MB | 1163.484 MB | 719.005 MB | 1576.363 MB | n/a MB | n/a MB |
| python3 | 4000 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.934 MB | 12.934 MB | 207.066 MB | 207.066 MB | n/a MB | n/a MB |
| python3 | 4093 | sandbox_agent_lsb-native_0000_0000 | 34 | 185.957% | 194.446% | 61.780 s | 1157.622 MB | 1241.008 MB | 1569.042 MB | 1655.387 MB | n/a MB | n/a MB |
| python3 | 4129 | sandbox_agent_lsb-native_0000_0000 | 18 | 190.919% | 195.048% | 32.680 s | 111.706 MB | 133.715 MB | 331.519 MB | 353.578 MB | n/a MB | n/a MB |
| python3 | 4149 | sandbox_agent_lsb-native_0000_0000 | 2 | 193.310% | 193.310% | 1.950 s | 119.680 MB | 138.328 MB | 338.393 MB | 356.707 MB | n/a MB | n/a MB |
| python3 | 4193 | sandbox_agent_lsb-native_0000_0000 | 19 | 192.821% | 201.880% | 34.950 s | 1075.721 MB | 1592.645 MB | 1491.114 MB | 2089.051 MB | n/a MB | n/a MB |
| python3 | 4216 | sandbox_agent_lsb-native_0000_0000 | 12 | 189.948% | 193.196% | 21.030 s | 105.314 MB | 139.164 MB | 324.235 MB | 357.320 MB | n/a MB | n/a MB |
| python3 | 4285 | sandbox_agent_lsb-native_0000_0000 | 16 | 190.628% | 201.140% | 28.790 s | 988.329 MB | 1297.320 MB | 1387.925 MB | 1709.602 MB | n/a MB | n/a MB |
| python3 | 4307 | sandbox_agent_lsb-native_0000_0000 | 13 | 191.987% | 201.399% | 23.200 s | 275.418 MB | 569.613 MB | 684.525 MB | 1160.324 MB | n/a MB | n/a MB |
| docker | 4428 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.086 MB | 30.086 MB | 1843.262 MB | 1843.262 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.286% | 100.000% | 11856.703 MB | 12152.000 MB | 28.439 W | 70.746 W | 318206.449 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 10.500% | 217.236% | 1173.774 s | 244.730 MB | 2330.195 MB | 64.515625 MB | 2.390625 MB | 0.001369 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 1903 | 11190.809 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 11165.492 | n/a | n/a | 64.516 | 11165492.419 | 11165492.419 | 11165492.419 |
| engine:execute | 1/1 | 0 | 0 | 11165.491 | 8.192 | 11157.203 | 64.516 | 11165490.594 | 11165490.594 | 11165490.594 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 11136.875 | 0.002 | 11136.873 | 36.654 | 11136874.766 | 11136874.766 | 11136874.766 |
| turn | 78/78 | 0 | 0 | 11134.532 | n/a | n/a | 35.551 | 142750.411 | 102166.710 | 335839.094 |
| llm:attempt | 78/78 | 0 | 0 | 10566.332 | 3.707 | 10562.625 | 6.632 | 135465.794 | 94960.447 | 335487.085 |
| tool:bash | 47/47 | 1 | 0 | 484.208 | n/a | n/a | 25.720 | 10302.300 | 1781.545 | 62774.930 |
| process:bash | 47/47 | 4 | 0 | 483.731 | n/a | n/a | 25.677 | 10292.152 | 1772.333 | 62763.366 |
| run:container_call | 13/13 | 0 | 0 | 23.177 | 0.002 | 23.174 | 0.053 | 1782.842 | 36.827 | 9154.311 |
| teardown:commit | 1/1 | 0 | 0 | 22.566 | 0.004 | 22.562 | 0.053 | 22565.815 | 22565.815 | 22565.815 |
| sandbox:commit | 1/1 | 0 | 0 | 22.379 | 0.002 | 22.376 | 0.053 | 22378.509 | 22378.509 | 22378.509 |
| checkpoint.total | 1/1 | 0 | 0 | 22.378 | 0.002 | 22.376 | 0.053 | 22378.350 | 22378.350 | 22378.350 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.378 | 0.002 | 22.376 | 0.053 | 22378.166 | 22378.166 | 22378.166 |
| tool:top_activations | 6/6 | 0 | 0 | 21.549 | n/a | n/a | 0.000 | 3591.526 | 3538.083 | 3771.164 |
| tool:inspect_module_inputs | 8/8 | 0 | 0 | 14.195 | n/a | n/a | 0.000 | 1774.351 | 1843.427 | 1885.945 |
| tool:inspect | 8/8 | 0 | 0 | 13.709 | n/a | n/a | 0.000 | 1713.620 | 1779.699 | 1851.311 |
| tool:generate | 7/7 | 0 | 0 | 8.592 | n/a | n/a | 0.000 | 1227.446 | 1290.228 | 1790.249 |
| tool:patch | 19/19 | 0 | 0 | 7.854 | n/a | n/a | 0.000 | 413.361 | 413.300 | 419.515 |
| syscall:sendto | 2497/2497 | 0 | 0 | 5.744 | n/a | n/a | 0.866 | 2.300 | 2.031 | 4.313 |
| tool:token_stats | 2/2 | 0 | 0 | 4.939 | n/a | n/a | 0.000 | 2469.283 | 2469.283 | 2754.126 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.762 | 1.105 | 3.658 | 27.704 | 4762.454 | 4762.454 | 4762.454 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.762 | 1.104 | 3.658 | 27.704 | 4762.195 | 4762.195 | 4762.195 |
| tool:trace | 2/2 | 0 | 0 | 2.373 | n/a | n/a | 0.000 | 1186.518 | 1186.518 | 1444.253 |
| syscall:connect | 637/637 | 0 | 0 | 1.437 | n/a | n/a | 0.237 | 2.255 | 1.869 | 4.617 |
| tool:attribution | 4/4 | 0 | 0 | 1.260 | n/a | n/a | 0.000 | 315.029 | 314.219 | 321.040 |
| sandbox:create | 1/1 | 0 | 0 | 0.925 | 0.248 | 0.677 | 0.000 | 925.299 | 925.299 | 925.299 |
| run:detect | 1/1 | 0 | 0 | 0.622 | 0.001 | 0.622 | 0.000 | 622.331 | 622.331 | 622.331 |
| sandbox:start | 1/1 | 0 | 0 | 0.545 | 0.002 | 0.543 | 0.000 | 545.286 | 545.286 | 545.286 |
| runtime.container_create | 1/1 | 0 | 0 | 0.545 | 0.002 | 0.543 | 0.000 | 545.126 | 545.126 | 545.126 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.363 | n/a | n/a | 0.000 | 363.153 | 363.153 | 363.153 |
| tool:attention | 1/1 | 0 | 0 | 0.324 | n/a | n/a | 0.000 | 324.114 | 324.114 | 324.114 |
| tool:submit_output | 1/1 | 0 | 0 | 0.241 | n/a | n/a | 0.000 | 241.316 | 241.316 | 241.316 |
| tool:submitted_output | 1/1 | 0 | 0 | 0.241 | n/a | n/a | 0.000 | 240.963 | 240.963 | 240.963 |
| tool:get_current_resources | 1/1 | 0 | 0 | 0.238 | n/a | n/a | 2.463 | 237.630 | 237.630 | 237.630 |
| syscall:execve | 144/144 | 0 | 0 | 0.216 | n/a | n/a | 0.057 | 1.499 | 1.150 | 3.019 |
| sandbox:stop | 1/1 | 0 | 0 | 0.187 | 0.002 | 0.185 | 0.000 | 187.032 | 187.032 | 187.032 |
| agency:services_close | 1/1 | 0 | 0 | 0.184 | 0.001 | 0.183 | 0.014 | 184.005 | 184.005 | 184.005 |
| agency:services_start | 1/1 | 0 | 0 | 0.089 | 0.043 | 0.047 | 0.000 | 89.454 | 89.454 | 89.454 |
| agent:create | 1/1 | 0 | 0 | 0.050 | 0.009 | 0.041 | 0.000 | 49.520 | 49.520 | 49.520 |
| tool:read | 6/6 | 0 | 0 | 0.003 | n/a | n/a | 0.000 | 0.557 | 0.529 | 1.082 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 2.277 | 2.277 | 2.277 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.202 | 1.202 | 1.202 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.071 | 0.076 | 0.099 |
| tool:write | 2/2 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.405 | 0.405 | 0.434 |
| tool:todowrite | 4/4 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.167 | 0.145 | 0.230 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.169 | 0.169 | 0.169 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.073 | 0.073 | 0.073 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 11130 | 0.159 | 0.036 | 48.535 | 0.063 | 17.778618 CPU seconds | n/a |
| GPU 0 memory | MB | 11132 | 11856.703 | 11670.000 | 12152.000 | 11852.000 | n/a | n/a |
| GPU 0 power | W | 11132 | 28.439 | 27.564 | 70.746 | 28.337 | n/a | 318206.449 J |
| GPU 0 proc / 1730-2961 / sandbox / ~ / device / GPU-f2e826ff-b268-64fc-6d09-5378802f055a memory | MB | 11132 | 3245.070 | 3118.000 | 3522.000 | 3222.000 | n/a | n/a |
| GPU 0 proc / 1730-2961 / sandbox / ~ / device / GPU-f2e826ff-b268-64fc-6d09-5378802f055a estimated power | W | 10198 | 0.295 | 0.000 | 60.490 | 0.000 | n/a | n/a |
| GPU 0 proc / 1730-2961 / sandbox / ~ / device / GPU-f2e826ff-b268-64fc-6d09-5378802f055a utilization | percent | 10198 | 0.230 | 0.000 | 50.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 1794-6837 / sandbox / ~ / device / GPU-f2e826ff-b268-64fc-6d09-5378802f055a memory | MB | 11132 | 8129.633 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 1794-6837 / sandbox / ~ / device / GPU-f2e826ff-b268-64fc-6d09-5378802f055a estimated power | W | 763 | 0.641 | 0.000 | 64.348 | 0.000 | n/a | n/a |
| GPU 0 proc / 1794-6837 / sandbox / ~ / device / GPU-f2e826ff-b268-64fc-6d09-5378802f055a utilization | percent | 763 | 0.761 | 0.000 | 88.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 11132 | 11374.703 | 11188.000 | 11670.000 | 11370.000 | n/a | n/a |
| GPU 0 utilization | percent | 11132 | 0.286 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 11132 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 11131 | 2.399 | 0.031 | 61.949 | 0.255 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 11131 | 3.194 | 0.000 | 52.983 | 0.251 | n/a | n/a |
| host disk_read_mb_s | MB/s | 11131 | 0.163 | 0.000 | 230.619 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 11131 | 0.100 | 0.000 | 87.461 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 11131 | 0.088 | 0.000 | 57.594 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 11131 | 0.089 | 0.000 | 57.875 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 11132 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 11132 | 7256.873 | 6664.535 | 9386.348 | 7513.246 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 11131 | 0.000 | 0.000 | 0.028 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 11131 | 0.000 | 0.000 | 0.032 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 11131 | 0.000 | 0.000 | 0.035 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 11131 | 0.004 | 0.000 | 1.128 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1721) CPU | percent | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1721) io read MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1721) io write MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1721) rss_mb | MB | 11132 | 3.363 | 3.363 | 3.363 | 3.363 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1721) main thread run-queue wait | percent | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1721) vms_mb | MB | 11132 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1730) CPU | percent | 11131 | 1.324 | 0.000 | 114.758 | 0.000 | 148.370000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 1730) io read MB/s | MB/s | 11131 | 0.007 | 0.000 | 39.402 | 0.000 | 78.382812 MB | n/a |
| Agency harness — python -m lsbench (PID 1730) io write MB/s | MB/s | 11131 | 0.088 | 0.015 | 167.841 | 0.023 | 987.000000 MB | n/a |
| Agency harness — python -m lsbench (PID 1730) rss_mb | MB | 11132 | 3174.060 | 2535.336 | 3561.848 | 3561.848 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1730) main thread run-queue wait | percent | 11131 | 0.000 | 0.000 | 4.186 | 0.000 | 0.048238 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 1730) vms_mb | MB | 11132 | 16135.768 | 14031.812 | 16924.559 | 16659.520 | n/a | n/a |
| Python — vllm (PID 1759) CPU | percent | 11131 | 0.088 | 0.000 | 7.962 | 0.000 | 9.840000 CPU seconds | n/a |
| Python — vllm (PID 1759) io read MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 1759) io write MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.008 | 0.000 | 0.042969 MB | n/a |
| Python — vllm (PID 1759) rss_mb | MB | 11132 | 1766.957 | 1766.262 | 1767.137 | 1767.137 | n/a | n/a |
| Python — vllm (PID 1759) main thread run-queue wait | percent | 11131 | 0.002 | 0.000 | 2.618 | 0.000 | 0.210092 run-queue seconds | n/a |
| Python — vllm (PID 1759) vms_mb | MB | 11132 | 11021.272 | 10963.031 | 11036.051 | 11036.051 | n/a | n/a |
| Python — python -c (PID 1793) CPU | percent | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 1793) io read MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1793) io write MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1793) rss_mb | MB | 11132 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| Python — python -c (PID 1793) main thread run-queue wait | percent | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 1793) vms_mb | MB | 11132 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 1794) CPU | percent | 11131 | 1.502 | 0.000 | 51.370 | 0.996 | 168.070000 CPU seconds | n/a |
| VLLM::EngineCore (PID 1794) io read MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 1794) io write MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.008 | 0.000 | 0.074219 MB | n/a |
| VLLM::EngineCore (PID 1794) rss_mb | MB | 11132 | 2313.909 | 2313.500 | 2314.000 | 2314.000 | n/a | n/a |
| VLLM::EngineCore (PID 1794) main thread run-queue wait | percent | 11131 | 0.000 | 0.000 | 0.087 | 0.000 | 0.002356 run-queue seconds | n/a |
| VLLM::EngineCore (PID 1794) vms_mb | MB | 11132 | 21203.184 | 21203.184 | 21203.184 | 21203.184 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1897) CPU | percent | 11131 | 0.024 | 0.000 | 4.973 | 0.000 | 2.730000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1897) io read MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.113 | 0.000 | 0.113281 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1897) io write MB/s | MB/s | 11131 | 0.000 | 0.000 | 0.008 | 0.000 | 0.281250 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1897) rss_mb | MB | 11132 | 46.208 | 43.590 | 47.121 | 45.973 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1897) main thread run-queue wait | percent | 11131 | 0.001 | 0.000 | 0.643 | 0.000 | 0.076273 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1897) vms_mb | MB | 11132 | 203.537 | 131.172 | 204.273 | 203.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2012) CPU | percent | 11105 | 0.002 | 0.000 | 0.995 | 0.000 | 0.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2012) rss_mb | MB | 11106 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2012) main thread run-queue wait | percent | 11105 | 0.004 | 0.000 | 5.215 | 0.000 | 0.439068 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2012) vms_mb | MB | 11106 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2046) CPU | percent | 11105 | 0.003 | 0.000 | 0.996 | 0.000 | 0.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2046) rss_mb | MB | 11106 | 1.309 | 1.309 | 1.309 | 1.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2046) main thread run-queue wait | percent | 11105 | 0.004 | 0.000 | 5.035 | 0.000 | 0.428840 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2046) vms_mb | MB | 11106 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2138) CPU | percent | 11105 | 2.526 | 0.000 | 82.192 | 0.000 | 282.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2138) rss_mb | MB | 11106 | 103.904 | 2.969 | 111.301 | 111.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2138) main thread run-queue wait | percent | 11105 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000066 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2138) vms_mb | MB | 11106 | 961.047 | 4.258 | 972.781 | 972.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2144) CPU | percent | 2 | 57.156 | 52.620 | 61.692 | 61.692 | 1.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2144) rss_mb | MB | 3 | 49.835 | 22.785 | 77.848 | 77.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2144) main thread run-queue wait | percent | 2 | 0.018 | 0.015 | 0.020 | 0.020 | 0.000352 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2144) vms_mb | MB | 3 | 61.204 | 32.141 | 93.281 | 93.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2156) CPU | percent | 11079 | 0.043 | 0.000 | 63.561 | 6.964 | 4.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2156) rss_mb | MB | 11080 | 72.441 | 21.312 | 75.227 | 71.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2156) main thread run-queue wait | percent | 11079 | 0.005 | 0.000 | 5.708 | 0.004 | 0.504122 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2156) vms_mb | MB | 11080 | 86.489 | 26.242 | 89.773 | 85.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2526) rss_mb | MB | 1 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2526) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2528) rss_mb | MB | 1 | 22.988 | 22.988 | 22.988 | 22.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2528) vms_mb | MB | 1 | 215.582 | 215.582 | 215.582 | 215.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2730) rss_mb | MB | 1 | 8.863 | 8.863 | 8.863 | 8.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2730) vms_mb | MB | 1 | 13.188 | 13.188 | 13.188 | 13.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2891) rss_mb | MB | 1 | 1527.586 | 1527.586 | 1527.586 | 1527.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2891) vms_mb | MB | 1 | 1757.777 | 1757.777 | 1757.777 | 1757.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2908) CPU | percent | 2 | 120.218 | 78.496 | 161.940 | 161.940 | 2.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2908) rss_mb | MB | 3 | 441.089 | 20.488 | 1119.270 | 1119.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2908) main thread run-queue wait | percent | 2 | 14.836 | 4.956 | 24.715 | 24.715 | 0.298653 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2908) vms_mb | MB | 3 | 923.376 | 212.316 | 1537.406 | 1537.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2979) rss_mb | MB | 1 | 6.422 | 6.422 | 6.422 | 6.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2979) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2997) CPU | percent | 2 | 142.073 | 96.359 | 187.787 | 187.787 | 2.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2997) rss_mb | MB | 3 | 814.587 | 31.496 | 1266.535 | 1145.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2997) main thread run-queue wait | percent | 2 | 24.412 | 9.309 | 39.515 | 39.515 | 0.491411 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2997) vms_mb | MB | 3 | 1330.846 | 414.754 | 2015.395 | 1562.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3034) CPU | percent | 3 | 150.133 | 99.236 | 200.119 | 200.119 | 4.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3034) rss_mb | MB | 4 | 616.518 | 0.000 | 1153.277 | 1153.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3034) main thread run-queue wait | percent | 3 | 33.630 | 22.967 | 51.687 | 51.687 | 1.017236 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3034) vms_mb | MB | 4 | 922.607 | 1.617 | 1570.664 | 1570.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3131) CPU | percent | 1 | 95.342 | 95.342 | 95.342 | 95.342 | 0.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3131) rss_mb | MB | 2 | 229.947 | 15.656 | 444.238 | 444.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3131) main thread run-queue wait | percent | 1 | 6.334 | 6.334 | 6.334 | 6.334 | 0.063781 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3131) vms_mb | MB | 2 | 626.973 | 208.402 | 1045.543 | 1045.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3276) CPU | percent | 2 | 123.150 | 101.274 | 145.025 | 145.025 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3276) rss_mb | MB | 3 | 764.346 | 7.129 | 2113.973 | 2113.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3276) main thread run-queue wait | percent | 2 | 17.144 | 16.022 | 18.266 | 16.022 | 0.345267 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3276) vms_mb | MB | 3 | 1033.918 | 11.793 | 2531.484 | 2531.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3348) CPU | percent | 1 | 94.287 | 94.287 | 94.287 | 94.287 | 0.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3348) rss_mb | MB | 2 | 241.562 | 18.199 | 464.926 | 464.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3348) main thread run-queue wait | percent | 1 | 6.049 | 6.049 | 6.049 | 6.049 | 0.060952 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3348) vms_mb | MB | 2 | 627.805 | 210.020 | 1045.590 | 1045.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3364) CPU | percent | 1 | 105.236 | 105.236 | 105.236 | 105.236 | 1.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3364) rss_mb | MB | 2 | 620.275 | 43.742 | 1196.809 | 1196.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3364) main thread run-queue wait | percent | 1 | 1.860 | 1.860 | 1.860 | 1.860 | 0.018732 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3364) vms_mb | MB | 2 | 1021.322 | 428.410 | 1614.234 | 1614.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3406) rss_mb | MB | 1 | 74.906 | 74.906 | 74.906 | 74.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3406) vms_mb | MB | 1 | 473.078 | 473.078 | 473.078 | 473.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3460) CPU | percent | 2 | 165.079 | 137.048 | 193.110 | 193.110 | 3.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3460) rss_mb | MB | 3 | 865.353 | 116.262 | 1262.133 | 1262.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3460) main thread run-queue wait | percent | 2 | 36.378 | 15.968 | 56.789 | 56.789 | 0.734233 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3460) vms_mb | MB | 3 | 1272.267 | 502.746 | 1679.234 | 1679.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3475) CPU | percent | 3 | 151.819 | 113.344 | 172.094 | 170.020 | 4.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3475) rss_mb | MB | 4 | 926.708 | 53.852 | 1217.660 | 1217.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3475) main thread run-queue wait | percent | 3 | 47.975 | 7.036 | 68.843 | 68.843 | 1.447212 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3475) vms_mb | MB | 4 | 1335.753 | 440.098 | 1634.305 | 1634.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3491) CPU | percent | 1 | 93.466 | 93.466 | 93.466 | 93.466 | 0.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3491) rss_mb | MB | 2 | 644.000 | 37.559 | 1250.441 | 1250.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3491) main thread run-queue wait | percent | 1 | 0.017 | 0.017 | 0.017 | 0.017 | 0.000172 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3491) vms_mb | MB | 2 | 1217.342 | 420.062 | 2014.621 | 2014.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3505) rss_mb | MB | 1 | 91.738 | 91.738 | 91.738 | 91.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3505) vms_mb | MB | 1 | 493.598 | 493.598 | 493.598 | 493.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3607) CPU | percent | 118 | 190.189 | 117.334 | 205.321 | 193.967 | 226.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3607) rss_mb | MB | 119 | 437.014 | 25.527 | 529.219 | 281.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3607) main thread run-queue wait | percent | 118 | 41.523 | 15.134 | 55.469 | 44.113 | 49.357807 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3607) vms_mb | MB | 119 | 853.759 | 217.684 | 937.359 | 690.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3626) CPU | percent | 7 | 151.617 | 101.308 | 164.877 | 156.216 | 10.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3626) rss_mb | MB | 8 | 150.236 | 7.410 | 174.316 | 174.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3626) main thread run-queue wait | percent | 7 | 58.146 | 18.942 | 75.833 | 63.806 | 4.095743 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3626) vms_mb | MB | 8 | 512.854 | 11.812 | 592.574 | 592.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3641) CPU | percent | 1 | 113.148 | 113.148 | 113.148 | 113.148 | 1.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3641) rss_mb | MB | 2 | 58.141 | 23.051 | 93.230 | 93.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3641) main thread run-queue wait | percent | 1 | 16.846 | 16.846 | 16.846 | 16.846 | 0.169730 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3641) vms_mb | MB | 2 | 361.346 | 214.559 | 508.133 | 508.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3657) rss_mb | MB | 1 | 28.230 | 28.230 | 28.230 | 28.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3657) vms_mb | MB | 1 | 250.883 | 250.883 | 250.883 | 250.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3712) CPU | percent | 1 | 147.972 | 147.972 | 147.972 | 147.972 | 1.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3712) rss_mb | MB | 2 | 131.844 | 75.781 | 187.906 | 187.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3712) main thread run-queue wait | percent | 1 | 53.436 | 53.436 | 53.436 | 53.436 | 0.538071 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3712) vms_mb | MB | 2 | 534.389 | 462.223 | 606.555 | 606.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3775) CPU | percent | 2 | 163.540 | 129.232 | 197.848 | 197.848 | 3.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3775) rss_mb | MB | 3 | 788.003 | 76.602 | 1143.703 | 1143.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3775) main thread run-queue wait | percent | 2 | 27.900 | 5.880 | 49.920 | 49.920 | 0.561258 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3775) vms_mb | MB | 3 | 1200.608 | 476.887 | 1562.469 | 1562.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3791) CPU | percent | 61 | 193.127 | 184.944 | 198.451 | 195.858 | 118.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3791) rss_mb | MB | 62 | 92.766 | 72.215 | 123.004 | 72.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3791) main thread run-queue wait | percent | 61 | 52.995 | 45.269 | 63.945 | 53.462 | 32.547203 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3791) vms_mb | MB | 62 | 312.368 | 290.613 | 341.629 | 290.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3830) CPU | percent | 67 | 189.353 | 184.018 | 195.504 | 190.427 | 127.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3830) rss_mb | MB | 68 | 93.652 | 65.145 | 118.797 | 116.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3830) main thread run-queue wait | percent | 67 | 53.173 | 43.911 | 61.767 | 55.475 | 35.872881 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3830) vms_mb | MB | 68 | 313.329 | 284.070 | 337.602 | 334.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3895) CPU | percent | 61 | 190.244 | 181.976 | 195.412 | 192.871 | 116.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3895) rss_mb | MB | 62 | 98.017 | 66.812 | 118.910 | 114.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3895) main thread run-queue wait | percent | 61 | 52.237 | 43.367 | 59.807 | 55.442 | 32.107738 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3895) vms_mb | MB | 62 | 318.369 | 290.504 | 340.309 | 334.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3919) CPU | percent | 1 | 149.999 | 149.999 | 149.999 | 149.999 | 1.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3919) rss_mb | MB | 2 | 164.273 | 102.062 | 226.484 | 226.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3919) main thread run-queue wait | percent | 1 | 45.357 | 45.357 | 45.357 | 45.357 | 0.456602 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3919) vms_mb | MB | 2 | 568.369 | 493.617 | 643.121 | 643.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3957) CPU | percent | 2 | 124.721 | 100.298 | 149.144 | 149.144 | 2.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3957) rss_mb | MB | 3 | 450.762 | 7.363 | 1163.484 | 1163.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3957) main thread run-queue wait | percent | 2 | 24.205 | 21.312 | 27.097 | 27.097 | 0.487140 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3957) vms_mb | MB | 3 | 719.005 | 11.941 | 1576.363 | 1576.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4000) rss_mb | MB | 1 | 12.934 | 12.934 | 12.934 | 12.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4000) vms_mb | MB | 1 | 207.066 | 207.066 | 207.066 | 207.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4093) CPU | percent | 33 | 185.957 | 94.479 | 194.446 | 190.930 | 61.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4093) rss_mb | MB | 34 | 1157.622 | 20.590 | 1241.008 | 1232.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4093) main thread run-queue wait | percent | 33 | 49.807 | 9.670 | 59.094 | 52.373 | 16.547269 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4093) vms_mb | MB | 34 | 1569.042 | 212.363 | 1655.387 | 1647.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4129) CPU | percent | 17 | 190.919 | 184.975 | 195.048 | 192.224 | 32.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4129) rss_mb | MB | 18 | 111.706 | 82.059 | 133.715 | 122.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4129) main thread run-queue wait | percent | 17 | 52.835 | 44.472 | 57.521 | 54.581 | 9.044144 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4129) vms_mb | MB | 18 | 331.519 | 300.391 | 353.578 | 340.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4149) CPU | percent | 1 | 193.310 | 193.310 | 193.310 | 193.310 | 1.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4149) rss_mb | MB | 2 | 119.680 | 101.031 | 138.328 | 138.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4149) main thread run-queue wait | percent | 1 | 55.315 | 55.315 | 55.315 | 55.315 | 0.557985 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4149) vms_mb | MB | 2 | 338.393 | 320.078 | 356.707 | 356.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4193) CPU | percent | 18 | 192.821 | 132.221 | 201.880 | 201.880 | 34.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4193) rss_mb | MB | 19 | 1075.721 | 35.648 | 1592.645 | 1266.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4193) main thread run-queue wait | percent | 18 | 46.537 | 17.595 | 55.598 | 49.361 | 8.435148 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4193) vms_mb | MB | 19 | 1491.114 | 417.473 | 2089.051 | 1678.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4216) CPU | percent | 11 | 189.948 | 184.974 | 193.196 | 189.934 | 21.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4216) rss_mb | MB | 12 | 105.314 | 67.703 | 139.164 | 133.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4216) main thread run-queue wait | percent | 11 | 49.700 | 44.435 | 54.945 | 48.063 | 5.502519 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4216) vms_mb | MB | 12 | 324.235 | 287.871 | 357.320 | 352.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_and_verify_adapter.py (PID 4285) CPU | percent | 15 | 190.628 | 124.099 | 201.140 | 192.550 | 28.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_and_verify_adapter.py (PID 4285) rss_mb | MB | 16 | 988.329 | 24.855 | 1297.320 | 1241.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_and_verify_adapter.py (PID 4285) main thread run-queue wait | percent | 15 | 46.525 | 20.956 | 55.599 | 50.685 | 7.026695 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_and_verify_adapter.py (PID 4285) vms_mb | MB | 16 | 1387.925 | 216.508 | 1709.602 | 1653.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4307) CPU | percent | 12 | 191.987 | 115.119 | 201.399 | 191.970 | 23.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4307) rss_mb | MB | 13 | 275.418 | 22.449 | 569.613 | 569.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4307) main thread run-queue wait | percent | 12 | 46.249 | 6.839 | 55.187 | 46.290 | 5.588787 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4307) vms_mb | MB | 13 | 684.525 | 213.949 | 1160.324 | 1160.324 | n/a | n/a |
| docker commit (PID 4428) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4428) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4428) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4428) rss_mb | MB | 22 | 30.086 | 30.086 | 30.086 | 30.086 | n/a | n/a |
| docker commit (PID 4428) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4428) vms_mb | MB | 22 | 1843.262 | 1843.262 | 1843.262 | 1843.262 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 11105 | 10.500 | 0.000 | 217.236 | 0.000 | 1173.774183 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 11105 | 2.140 | 0.000 | 50.301 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 11105 | 2.242 | 0.000 | 61.456 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 11105 | 0.007 | 0.000 | 31.075 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 11105 | 0.007 | 0.000 | 31.077 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 11105 | 0.006 | 0.000 | 18.448 | 0.000 | 64.515625 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 11105 | 0.000 | 0.000 | 0.754 | 0.000 | 2.390625 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 11106 | 244.730 | 38.652 | 2330.195 | 192.871 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 11105 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 11105 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 11105 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001369 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 11105 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 11131 | 2.941 | 1.419 | 116.453 | 2.131 | 329.338587 CPU seconds | n/a |
| workload total memory | MB | 11132 | 9223.150 | 8439.223 | 9854.238 | 9849.379 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
