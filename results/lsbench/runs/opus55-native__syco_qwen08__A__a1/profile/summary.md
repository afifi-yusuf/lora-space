# agprof summary

- Duration: **1596.916 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **82 calls**, 82 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1075.793 s total wait
- Tools: **88/88 completed**, 1 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **148329** at 1.972 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1596543.242 / 1596543.242 ms |
| LLM latency p50 / p95 | 9661.623 / 33353.311 ms |
| LLM TTFT p50 / p95 | 5323.907 / 25615.211 ms |
| LLM input / output tokens | 166 / 119377 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 82 total, 82 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 517.407 / 11844.891 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 2/2 | 2 | 0 | 0 | 488.167 ms | 657.825 ms |
| attribution | 1/1 | 1 | 0 | 0 | 19700.089 ms | 19700.089 ms |
| bash | 52/52 | 51 | 1 | 0 | 293.892 ms | 14416.018 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 683.552 ms | 683.552 ms |
| generate | 8/8 | 8 | 0 | 0 | 569.433 ms | 748.451 ms |
| inspect | 3/3 | 3 | 0 | 0 | 3673.980 ms | 4181.333 ms |
| inspect_module_inputs | 2/2 | 2 | 0 | 0 | 3730.847 ms | 3750.986 ms |
| patch | 8/8 | 8 | 0 | 0 | 425.473 ms | 431.521 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 238.276 ms | 238.276 ms |
| trace | 10/10 | 10 | 0 | 0 | 2142.956 ms | 2238.150 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.737% | 101.967% | 91.622 s | 9406.887 MB | 9833.473 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VLLM::EngineCor | 2238 |  | 1587 | 1.477% | 28.845% | 23.570 s | 2554.209 MB | 2554.293 MB | 20940.461 MB | 20940.461 MB | 0.000000 MB | 0.011719 MB |
| vllm | 2200 |  | 1587 | 0.125% | 8.947% | 2.000 s | 1787.803 MB | 1787.863 MB | 11053.084 MB | 11056.719 MB | 0.007812 MB | 0.031250 MB |
| docker | 2561 |  | 18 | 0.937% | 12.939% | 0.160 s | 23.405 MB | 31.871 MB | 1667.717 MB | 1987.527 MB | 51.554688 MB | 0.000000 MB |
| lsb_grid_worker | 1958 |  | 1587 | 0.000% | 0.000% | 0.000 s | 3.414 MB | 3.414 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 2237 |  | 1587 | 0.000% | 0.000% | 0.000 s | 12.195 MB | 12.195 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python | 2142 |  | 1587 | 4.093% | 101.797% | 65.400 s | 2986.334 MB | 3300.707 MB | 15920.866 MB | 16250.980 MB | 178.347656 MB | 955.867188 MB |
| docker-buildx | 2570 |  | 11 | 0.995% | 3.981% | 0.100 s | 13.934 MB | 41.035 MB | 1187.783 MB | 1298.727 MB | 42.089844 MB | 0.000000 MB |
| docker-compose | 2571 |  | 5 | 0.498% | 0.996% | 0.020 s | 6.234 MB | 11.445 MB | 1020.495 MB | 1260.309 MB | 14.054688 MB | 0.000000 MB |
| docker | 2629 |  | 6 | 0.000% | 0.000% | 0.000 s | 30.525 MB | 30.680 MB | 1843.762 MB | 1843.762 MB | 0.070312 MB | 0.000000 MB |
| docker | 2709 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.957 MB | 30.957 MB | 1771.516 MB | 1771.516 MB | 0.000000 MB | 0.000000 MB |
| bash | 2798 | sandbox_agent_lsb-native_0000_0000 | 1561 | 3.508% | 66.651% | 55.090 s | 104.128 MB | 109.977 MB | 951.337 MB | 972.820 MB | n/a MB | n/a MB |
| docker-init | 2673 | sandbox_agent_lsb-native_0000_0000 | 1561 | 0.002% | 0.995% | 0.030 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 2805 | sandbox_agent_lsb-native_0000_0000 | 28 | 4.861% | 30.834% | 1.320 s | 33.801 MB | 80.332 MB | 42.342 MB | 95.531 MB | n/a MB | n/a MB |
| tail | 2707 | sandbox_agent_lsb-native_0000_0000 | 1561 | 0.003% | 0.995% | 0.050 s | 1.273 MB | 1.273 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| ldconfig | 2807 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.070 MB | 1.070 MB | n/a MB | n/a MB |
| python3 | 2817 | sandbox_agent_lsb-native_0000_0000 | 1364 | 0.214% | 23.830% | 2.930 s | 72.564 MB | 74.340 MB | 86.925 MB | 88.555 MB | n/a MB | n/a MB |
| python | 3088 | sandbox_agent_lsb-native_0000_0000 | 4 | 9.943% | 23.862% | 0.300 s | 14.740 MB | 21.598 MB | 1791.740 MB | 1880.641 MB | n/a MB | n/a MB |
| tail | 3104 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.840 MB | 2.840 MB | n/a MB | n/a MB |
| bash | 3101 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.695 MB | 2.695 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3103 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.824 MB | 4.824 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| python | 3128 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.125 MB | 12.125 MB | 19.848 MB | 19.848 MB | n/a MB | n/a MB |
| python | 3133 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 60.203 MB | 60.203 MB | 253.125 MB | 253.125 MB | n/a MB | n/a MB |
| python | 3151 | sandbox_agent_lsb-native_0000_0000 | 2 | 128.255% | 128.255% | 1.290 s | 1116.553 MB | 1643.930 MB | 2701.191 MB | 2974.402 MB | n/a MB | n/a MB |
| python | 3161 | sandbox_agent_lsb-native_0000_0000 | 2 | 134.235% | 134.235% | 1.350 s | 805.705 MB | 1564.645 MB | 2429.564 MB | 2954.445 MB | n/a MB | n/a MB |
| python | 3228 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.566 MB | 19.566 MB | 211.707 MB | 211.707 MB | n/a MB | n/a MB |
| python | 3236 | sandbox_agent_lsb-native_0000_0000 | 2 | 154.643% | 154.643% | 1.560 s | 1302.785 MB | 1703.441 MB | 2713.195 MB | 2998.406 MB | n/a MB | n/a MB |
| python | 3246 | sandbox_agent_lsb-native_0000_0000 | 4 | 100.110% | 180.990% | 3.020 s | 1187.244 MB | 1596.582 MB | 2275.159 MB | 2977.770 MB | n/a MB | n/a MB |
| python | 3308 | sandbox_agent_lsb-native_0000_0000 | 4 | 196.191% | 197.545% | 5.940 s | 53.521 MB | 66.996 MB | 282.392 MB | 300.008 MB | n/a MB | n/a MB |
| python | 3318 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.895 MB | 18.895 MB | 211.398 MB | 211.398 MB | n/a MB | n/a MB |
| python | 3341 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.336 MB | 20.336 MB | 212.203 MB | 212.203 MB | n/a MB | n/a MB |
| python | 3378 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.875 MB | 12.875 MB | 206.961 MB | 206.961 MB | n/a MB | n/a MB |
| python | 3416 | sandbox_agent_lsb-native_0000_0000 | 19 | 189.971% | 203.621% | 34.440 s | 159.946 MB | 269.797 MB | 456.055 MB | 524.277 MB | n/a MB | n/a MB |
| python3 | 3430 | sandbox_agent_lsb-native_0000_0000 | 14 | 190.485% | 206.912% | 24.920 s | 171.372 MB | 275.809 MB | 453.002 MB | 530.191 MB | n/a MB | n/a MB |
| python | 3444 | sandbox_agent_lsb-native_0000_0000 | 3 | 183.440% | 194.878% | 3.690 s | 1354.112 MB | 1604.203 MB | 2814.033 MB | 3007.051 MB | n/a MB | n/a MB |
| python | 3470 | sandbox_agent_lsb-native_0000_0000 | 119 | 198.158% | 204.015% | 235.510 s | 279.217 MB | 458.449 MB | 649.254 MB | 745.316 MB | n/a MB | n/a MB |
| bash | 3482 | sandbox_agent_lsb-native_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.602 MB | 2.605 MB | 2.972 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3485 | sandbox_agent_lsb-native_0000_0000 | 8 | 199.657% | 201.480% | 14.090 s | 242.607 MB | 299.281 MB | 522.340 MB | 546.902 MB | n/a MB | n/a MB |
| timeout | 3505 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 2.816 MB | 2.816 MB | n/a MB | n/a MB |
| python | 3506 | sandbox_agent_lsb-native_0000_0000 | 4 | 197.102% | 198.539% | 5.950 s | 206.625 MB | 269.879 MB | 438.283 MB | 518.488 MB | n/a MB | n/a MB |
| python | 3526 | sandbox_agent_lsb-native_0000_0000 | 15 | 199.270% | 211.669% | 28.090 s | 190.782 MB | 263.359 MB | 462.233 MB | 479.152 MB | n/a MB | n/a MB |
| timeout | 3525 | sandbox_agent_lsb-native_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.516 MB | 1.516 MB | 2.816 MB | 2.816 MB | n/a MB | n/a MB |
| python | 3541 | sandbox_agent_lsb-native_0000_0000 | 5 | 187.382% | 201.260% | 7.550 s | 168.386 MB | 367.164 MB | 1752.359 MB | 2325.281 MB | n/a MB | n/a MB |
| timeout | 3539 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.477 MB | 1.477 MB | 2.816 MB | 2.816 MB | n/a MB | n/a MB |
| python | 3565 | sandbox_agent_lsb-native_0000_0000 | 4 | 188.625% | 198.816% | 5.700 s | 68.356 MB | 99.195 MB | 1478.468 MB | 1975.160 MB | n/a MB | n/a MB |
| docker | 3612 |  | 119 | 0.000% | 0.000% | 0.000 s | 30.560 MB | 30.605 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |
| docker | 3699 |  | 44 | 0.046% | 1.989% | 0.020 s | 28.633 MB | 28.863 MB | 1767.642 MB | 1770.945 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.926% | 50.000% | 11484.663 MB | 11668.000 MB | 29.351 W | 58.045 W | 46830.608 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 29.225% | 212.411% | 459.129 s | 248.971 MB | 1341.344 MB | 72.781250 MB | 1.464844 MB | 0.000534 MB | 0.000000 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2559 | 1596.548 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1596.543 | n/a | n/a | 72.781 | 1596543.242 | 1596543.242 | 1596543.242 |
| sync:result_wait | 1/1 | 0 | 0 | 1596.542 | 0.000 | 1596.542 | 72.781 | 1596542.429 | 1596542.429 | 1596542.429 |
| engine:execute | 1/1 | 0 | 0 | 1596.542 | 9.179 | 1587.333 | 72.781 | 1596541.631 | 1596541.631 | 1596541.631 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1373.735 | 0.002 | 1373.732 | 27.030 | 1373734.655 | 1373734.655 | 1373734.655 |
| turn | 82/82 | 0 | 0 | 1369.831 | n/a | n/a | 25.283 | 16705.259 | 12710.549 | 36739.191 |
| llm:attempt | 82/82 | 0 | 0 | 1075.793 | 3.337 | 1072.454 | 1.924 | 13119.425 | 9661.623 | 33353.311 |
| tool:bash | 52/52 | 1 | 0 | 219.489 | n/a | n/a | 22.891 | 4220.943 | 293.892 | 14416.018 |
| process:bash | 52/52 | 2 | 0 | 219.015 | n/a | n/a | 22.822 | 4211.827 | 285.712 | 14403.182 |
| run:container_call | 14/14 | 1 | 0 | 171.092 | 0.003 | 171.089 | 0.042 | 12220.854 | 45.175 | 70216.110 |
| teardown:commit | 1/1 | 0 | 0 | 164.849 | 0.008 | 164.841 | 0.042 | 164848.926 | 164848.926 | 164848.926 |
| sandbox:commit | 1/1 | 0 | 0 | 164.665 | 0.007 | 164.659 | 0.042 | 164665.372 | 164665.372 | 164665.372 |
| checkpoint.total | 1/1 | 0 | 0 | 164.665 | 0.006 | 164.659 | 0.042 | 164665.237 | 164665.237 | 164665.237 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 164.665 | 0.006 | 164.659 | 0.042 | 164665.098 | 164665.098 | 164665.098 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 39.035 | 7.910 | 31.124 | 45.613 | 39034.736 | 39034.736 | 39034.736 |
| runtime.harness_start | 1/1 | 0 | 0 | 39.034 | 7.910 | 31.124 | 45.612 | 39034.446 | 39034.446 | 39034.446 |
| tool:attribution | 1/1 | 0 | 0 | 19.700 | n/a | n/a | 0.000 | 19700.089 | 19700.089 | 19700.089 |
| sandbox:create | 1/1 | 0 | 0 | 18.274 | 0.257 | 18.017 | 0.000 | 18274.196 | 18274.196 | 18274.196 |
| tool:trace | 10/10 | 0 | 0 | 17.762 | n/a | n/a | 0.000 | 1776.193 | 2142.956 | 2238.150 |
| run:detect | 1/1 | 0 | 0 | 17.546 | 0.001 | 17.545 | 0.000 | 17546.333 | 17546.333 | 17546.333 |
| tool:inspect | 3/3 | 0 | 0 | 11.554 | n/a | n/a | 0.000 | 3851.386 | 3673.980 | 4181.333 |
| tool:inspect_module_inputs | 2/2 | 0 | 0 | 7.462 | n/a | n/a | 0.000 | 3730.847 | 3730.847 | 3750.986 |
| sandbox:start | 1/1 | 0 | 0 | 7.303 | 0.002 | 7.301 | 0.000 | 7303.089 | 7303.089 | 7303.089 |
| runtime.container_create | 1/1 | 0 | 0 | 7.303 | 0.002 | 7.301 | 0.000 | 7302.946 | 7302.946 | 7302.946 |
| tool:generate | 8/8 | 0 | 0 | 4.738 | n/a | n/a | 0.000 | 592.251 | 569.433 | 748.451 |
| syscall:sendto | 1863/1863 | 0 | 0 | 4.559 | n/a | n/a | 0.260 | 2.447 | 2.119 | 4.544 |
| tool:patch | 8/8 | 0 | 0 | 3.397 | n/a | n/a | 0.000 | 424.630 | 425.473 | 431.521 |
| syscall:execve | 183/183 | 0 | 0 | 1.266 | n/a | n/a | 0.281 | 6.917 | 1.191 | 4.282 |
| syscall:connect | 479/479 | 0 | 0 | 1.183 | n/a | n/a | 0.066 | 2.469 | 2.129 | 5.218 |
| tool:attention | 2/2 | 0 | 0 | 0.976 | n/a | n/a | 0.000 | 488.167 | 488.167 | 657.825 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.684 | n/a | n/a | 0.000 | 683.552 | 683.552 | 683.552 |
| agency:services_start | 1/1 | 0 | 0 | 0.455 | 0.044 | 0.410 | 0.000 | 454.715 | 454.715 | 454.715 |
| agent:create | 1/1 | 0 | 0 | 0.262 | 0.009 | 0.253 | 0.000 | 262.498 | 262.498 | 262.498 |
| tool:submit_output | 1/1 | 0 | 0 | 0.238 | n/a | n/a | 0.000 | 238.276 | 238.276 | 238.276 |
| sandbox:stop | 1/1 | 0 | 0 | 0.183 | 0.002 | 0.182 | 0.000 | 183.325 | 183.325 | 183.325 |
| agency:services_close | 1/1 | 0 | 0 | 0.128 | 0.001 | 0.128 | 0.009 | 128.158 | 128.158 | 128.158 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 2.446 | 2.446 | 2.446 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.298 | 1.298 | 1.298 |
| sync:container | 14/14 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.081 | 0.074 | 0.146 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.175 | 0.175 | 0.175 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.055 | 0.055 | 0.055 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1560 | 0.659 | 0.042 | 150.207 | 24.310 | 10.339988 CPU seconds | n/a |
| GPU 0 memory | MB | 1587 | 11484.663 | 11326.000 | 11668.000 | 11476.000 | n/a | n/a |
| GPU 0 power | W | 1587 | 29.351 | 28.101 | 58.045 | 28.625 | n/a | 46830.608 J |
| GPU 0 proc / 2142-37100 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 memory | MB | 1587 | 3198.851 | 3118.000 | 3378.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 2142-37100 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 estimated power | W | 1457 | 1.483 | 0.000 | 57.358 | 0.000 | n/a | n/a |
| GPU 0 proc / 2142-37100 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 utilization | percent | 1457 | 0.942 | 0.000 | 47.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2238-62967 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 memory | MB | 1587 | 7803.812 | 7726.000 | 7808.000 | 7808.000 | n/a | n/a |
| GPU 0 proc / 2238-62967 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 estimated power | W | 103 | 2.895 | 0.000 | 41.616 | 0.000 | n/a | n/a |
| GPU 0 proc / 2238-62967 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 utilization | percent | 103 | 1.553 | 0.000 | 27.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1587 | 11002.663 | 10844.000 | 11186.000 | 10994.000 | n/a | n/a |
| GPU 0 utilization | percent | 1587 | 0.926 | 0.000 | 50.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1587 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1586 | 6.349 | 0.025 | 58.742 | 0.990 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1586 | 8.585 | 0.000 | 53.731 | 6.345 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1586 | 1.191 | 0.000 | 212.978 | 4.846 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1586 | 0.615 | 0.000 | 63.431 | 0.241 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1586 | 10.169 | 0.000 | 97.832 | 66.395 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1586 | 10.263 | 0.000 | 98.730 | 66.799 | n/a | n/a |
| host mem_total_mb | MB | 1587 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1587 | 7278.092 | 6514.414 | 8540.949 | 7436.734 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1586 | 0.000 | 0.000 | 0.002 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1586 | 0.000 | 0.000 | 0.002 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1586 | 0.003 | 0.000 | 0.316 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1586 | 0.018 | 0.000 | 0.652 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1958) CPU | percent | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1958) io read MB/s | MB/s | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1958) io write MB/s | MB/s | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1958) rss_mb | MB | 1587 | 3.414 | 3.414 | 3.414 | 3.414 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1958) main thread run-queue wait | percent | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1958) vms_mb | MB | 1587 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2142) CPU | percent | 1586 | 4.093 | 0.000 | 101.797 | 1.990 | 65.400000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2142) io read MB/s | MB/s | 1586 | 0.112 | 0.000 | 100.981 | 0.000 | 178.347656 MB | n/a |
| Agency harness — python -m lsbench (PID 2142) io write MB/s | MB/s | 1586 | 0.597 | 0.000 | 121.480 | 0.023 | 955.867188 MB | n/a |
| Agency harness — python -m lsbench (PID 2142) rss_mb | MB | 1587 | 2986.334 | 2326.930 | 3300.707 | 3204.328 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2142) main thread run-queue wait | percent | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2142) vms_mb | MB | 1587 | 15920.866 | 13774.793 | 16250.980 | 16175.336 | n/a | n/a |
| Python — vllm (PID 2200) CPU | percent | 1586 | 0.125 | 0.000 | 8.947 | 0.000 | 2.000000 CPU seconds | n/a |
| Python — vllm (PID 2200) io read MB/s | MB/s | 1586 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 2200) io write MB/s | MB/s | 1586 | 0.000 | 0.000 | 0.008 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 2200) rss_mb | MB | 1587 | 1787.803 | 1786.863 | 1787.863 | 1787.863 | n/a | n/a |
| Python — vllm (PID 2200) main thread run-queue wait | percent | 1586 | 0.005 | 0.000 | 0.501 | 0.000 | 0.078303 run-queue seconds | n/a |
| Python — vllm (PID 2200) vms_mb | MB | 1587 | 11053.084 | 10983.699 | 11056.719 | 11056.719 | n/a | n/a |
| Python — python -c (PID 2237) CPU | percent | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2237) io read MB/s | MB/s | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2237) io write MB/s | MB/s | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2237) rss_mb | MB | 1587 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| Python — python -c (PID 2237) main thread run-queue wait | percent | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2237) vms_mb | MB | 1587 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2238) CPU | percent | 1586 | 1.477 | 0.000 | 28.845 | 1.990 | 23.570000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2238) io read MB/s | MB/s | 1586 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 2238) io write MB/s | MB/s | 1586 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 2238) rss_mb | MB | 1587 | 2554.209 | 2553.758 | 2554.293 | 2554.293 | n/a | n/a |
| VLLM::EngineCore (PID 2238) main thread run-queue wait | percent | 1586 | 0.000 | 0.000 | 0.104 | 0.000 | 0.002614 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2238) vms_mb | MB | 1587 | 20940.461 | 20940.461 | 20940.461 | 20940.461 | n/a | n/a |
| docker (PID 2561) CPU | percent | 17 | 0.937 | 0.000 | 12.939 | 0.000 | 0.160000 CPU seconds | n/a |
| docker (PID 2561) io read MB/s | MB/s | 17 | 3.017 | 0.000 | 23.986 | 0.000 | 51.554688 MB | n/a |
| docker (PID 2561) io write MB/s | MB/s | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker (PID 2561) rss_mb | MB | 18 | 23.405 | 0.000 | 31.871 | 31.871 | n/a | n/a |
| docker (PID 2561) main thread run-queue wait | percent | 17 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000066 run-queue seconds | n/a |
| docker (PID 2561) vms_mb | MB | 18 | 1667.717 | 32.195 | 1987.527 | 1987.527 | n/a | n/a |
| docker-buildx (PID 2570) CPU | percent | 10 | 0.995 | 0.000 | 3.981 | 3.981 | 0.100000 CPU seconds | n/a |
| docker-buildx (PID 2570) io read MB/s | MB/s | 10 | 4.189 | 1.555 | 10.100 | 10.100 | 42.089844 MB | n/a |
| docker-buildx (PID 2570) io write MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker-buildx (PID 2570) rss_mb | MB | 11 | 13.934 | 0.836 | 41.035 | 41.035 | n/a | n/a |
| docker-buildx (PID 2570) main thread run-queue wait | percent | 10 | 0.004 | 0.000 | 0.020 | 0.020 | 0.000404 run-queue seconds | n/a |
| docker-buildx (PID 2570) vms_mb | MB | 11 | 1187.783 | 99.875 | 1298.727 | 1298.727 | n/a | n/a |
| docker-compose (PID 2571) CPU | percent | 4 | 0.498 | 0.000 | 0.996 | 0.995 | 0.020000 CPU seconds | n/a |
| docker-compose (PID 2571) io read MB/s | MB/s | 4 | 3.497 | 2.388 | 4.802 | 4.802 | 14.054688 MB | n/a |
| docker-compose (PID 2571) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker-compose (PID 2571) rss_mb | MB | 5 | 6.234 | 0.555 | 11.445 | 11.445 | n/a | n/a |
| docker-compose (PID 2571) main thread run-queue wait | percent | 4 | 0.001 | 0.000 | 0.001 | 0.000 | 0.000021 run-queue seconds | n/a |
| docker-compose (PID 2571) vms_mb | MB | 5 | 1020.495 | 63.613 | 1260.309 | 1260.309 | n/a | n/a |
| docker run (PID 2629) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker run (PID 2629) io read MB/s | MB/s | 5 | 0.014 | 0.000 | 0.070 | 0.000 | 0.070312 MB | n/a |
| docker run (PID 2629) io write MB/s | MB/s | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker run (PID 2629) rss_mb | MB | 6 | 30.525 | 30.371 | 30.680 | 30.680 | n/a | n/a |
| docker run (PID 2629) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000025 run-queue seconds | n/a |
| docker run (PID 2629) vms_mb | MB | 6 | 1843.762 | 1843.762 | 1843.762 | 1843.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2673) CPU | percent | 1560 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2673) rss_mb | MB | 1561 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2673) main thread run-queue wait | percent | 1560 | 0.009 | 0.000 | 5.100 | 0.000 | 0.134638 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2673) vms_mb | MB | 1561 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2707) CPU | percent | 1560 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2707) rss_mb | MB | 1561 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2707) main thread run-queue wait | percent | 1560 | 0.007 | 0.000 | 5.063 | 0.000 | 0.117623 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2707) vms_mb | MB | 1561 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| docker exec (PID 2709) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker exec (PID 2709) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker exec (PID 2709) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker exec (PID 2709) rss_mb | MB | 2 | 30.957 | 30.957 | 30.957 | 30.957 | n/a | n/a |
| docker exec (PID 2709) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker exec (PID 2709) vms_mb | MB | 2 | 1771.516 | 1771.516 | 1771.516 | 1771.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2798) CPU | percent | 1560 | 3.508 | 0.000 | 66.651 | 0.000 | 55.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2798) rss_mb | MB | 1561 | 104.128 | 2.883 | 109.977 | 109.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2798) main thread run-queue wait | percent | 1560 | 0.000 | 0.000 | 0.004 | 0.000 | 0.000119 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2798) vms_mb | MB | 1561 | 951.337 | 4.258 | 972.820 | 972.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2805) CPU | percent | 27 | 4.861 | 0.000 | 30.834 | 5.966 | 1.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2805) rss_mb | MB | 28 | 33.801 | 0.129 | 80.332 | 80.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2805) main thread run-queue wait | percent | 27 | 0.003 | 0.000 | 0.009 | 0.008 | 0.000729 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2805) vms_mb | MB | 28 | 42.342 | 0.395 | 95.531 | 95.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ldconfig (PID 2807) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ldconfig (PID 2807) vms_mb | MB | 1 | 1.070 | 1.070 | 1.070 | 1.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2817) CPU | percent | 1363 | 0.214 | 0.000 | 23.830 | 0.000 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2817) rss_mb | MB | 1364 | 72.564 | 51.879 | 74.340 | 73.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2817) main thread run-queue wait | percent | 1363 | 0.020 | 0.000 | 4.996 | 0.000 | 0.278588 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2817) vms_mb | MB | 1364 | 86.925 | 59.477 | 88.555 | 88.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3088) CPU | percent | 3 | 9.943 | 0.000 | 23.862 | 5.966 | 0.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3088) rss_mb | MB | 4 | 14.740 | 10.652 | 21.598 | 21.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3088) main thread run-queue wait | percent | 3 | 0.103 | 0.004 | 0.282 | 0.023 | 0.003115 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3088) vms_mb | MB | 4 | 1791.740 | 1690.371 | 1880.641 | 1880.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3101) rss_mb | MB | 1 | 2.695 | 2.695 | 2.695 | 2.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3101) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3103) rss_mb | MB | 1 | 4.824 | 4.824 | 4.824 | 4.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3103) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3104) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3104) vms_mb | MB | 1 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3128) rss_mb | MB | 1 | 12.125 | 12.125 | 12.125 | 12.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3128) vms_mb | MB | 1 | 19.848 | 19.848 | 19.848 | 19.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3133) rss_mb | MB | 1 | 60.203 | 60.203 | 60.203 | 60.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3133) vms_mb | MB | 1 | 253.125 | 253.125 | 253.125 | 253.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3151) CPU | percent | 1 | 128.255 | 128.255 | 128.255 | 128.255 | 1.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3151) rss_mb | MB | 2 | 1116.553 | 589.176 | 1643.930 | 1643.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3151) main thread run-queue wait | percent | 1 | 36.655 | 36.655 | 36.655 | 36.655 | 0.368681 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3151) vms_mb | MB | 2 | 2701.191 | 2427.980 | 2974.402 | 2974.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3161) CPU | percent | 1 | 134.235 | 134.235 | 134.235 | 134.235 | 1.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3161) rss_mb | MB | 2 | 805.705 | 46.766 | 1564.645 | 1564.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3161) main thread run-queue wait | percent | 1 | 23.114 | 23.114 | 23.114 | 23.114 | 0.232461 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3161) vms_mb | MB | 2 | 2429.564 | 1904.684 | 2954.445 | 2954.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3228) rss_mb | MB | 1 | 19.566 | 19.566 | 19.566 | 19.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3228) vms_mb | MB | 1 | 211.707 | 211.707 | 211.707 | 211.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3236) CPU | percent | 1 | 154.643 | 154.643 | 154.643 | 154.643 | 1.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3236) rss_mb | MB | 2 | 1302.785 | 902.129 | 1703.441 | 1703.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3236) main thread run-queue wait | percent | 1 | 44.459 | 44.459 | 44.459 | 44.459 | 0.448494 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3236) vms_mb | MB | 2 | 2713.195 | 2427.984 | 2998.406 | 2998.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3246) CPU | percent | 3 | 100.110 | 22.879 | 180.990 | 180.990 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3246) rss_mb | MB | 4 | 1187.244 | 22.781 | 1596.582 | 1596.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3246) main thread run-queue wait | percent | 3 | 22.906 | 0.009 | 66.941 | 66.941 | 0.691006 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3246) vms_mb | MB | 4 | 2275.159 | 214.387 | 2977.770 | 2977.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3308) CPU | percent | 3 | 196.191 | 194.263 | 197.545 | 197.545 | 5.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3308) rss_mb | MB | 4 | 53.521 | 45.230 | 66.996 | 53.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3308) main thread run-queue wait | percent | 3 | 53.925 | 53.097 | 55.531 | 53.097 | 1.632674 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3308) vms_mb | MB | 4 | 282.392 | 264.516 | 300.008 | 300.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3318) rss_mb | MB | 1 | 18.895 | 18.895 | 18.895 | 18.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3318) vms_mb | MB | 1 | 211.398 | 211.398 | 211.398 | 211.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3341) rss_mb | MB | 1 | 20.336 | 20.336 | 20.336 | 20.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3341) vms_mb | MB | 1 | 212.203 | 212.203 | 212.203 | 212.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3378) rss_mb | MB | 1 | 12.875 | 12.875 | 12.875 | 12.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3378) vms_mb | MB | 1 | 206.961 | 206.961 | 206.961 | 206.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3416) CPU | percent | 18 | 189.971 | 171.991 | 203.621 | 191.544 | 34.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3416) rss_mb | MB | 19 | 159.946 | 13.242 | 269.797 | 53.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3416) main thread run-queue wait | percent | 18 | 45.150 | 35.613 | 51.652 | 51.652 | 8.185236 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3416) vms_mb | MB | 19 | 456.055 | 207.215 | 524.277 | 264.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3430) CPU | percent | 13 | 190.485 | 162.748 | 206.912 | 201.383 | 24.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3430) rss_mb | MB | 14 | 171.372 | 73.598 | 275.809 | 253.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3430) main thread run-queue wait | percent | 13 | 44.598 | 30.434 | 50.617 | 49.087 | 5.834365 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3430) vms_mb | MB | 14 | 453.002 | 87.879 | 530.191 | 530.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3444) CPU | percent | 2 | 183.440 | 172.001 | 194.878 | 194.878 | 3.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3444) rss_mb | MB | 3 | 1354.112 | 853.992 | 1604.203 | 1604.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3444) main thread run-queue wait | percent | 2 | 41.521 | 31.135 | 51.908 | 51.908 | 0.835225 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3444) vms_mb | MB | 3 | 2814.033 | 2428.000 | 3007.051 | 3007.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3470) CPU | percent | 118 | 198.158 | 183.915 | 204.015 | 199.320 | 235.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3470) rss_mb | MB | 119 | 279.217 | 48.121 | 458.449 | 304.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3470) main thread run-queue wait | percent | 118 | 47.364 | 39.943 | 54.628 | 51.217 | 56.291446 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3470) vms_mb | MB | 119 | 649.254 | 242.801 | 745.316 | 745.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3482) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3482) rss_mb | MB | 9 | 1.602 | 1.477 | 2.605 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3482) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000014 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3482) vms_mb | MB | 9 | 2.972 | 2.816 | 4.215 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3485) CPU | percent | 7 | 199.657 | 197.802 | 201.480 | 200.406 | 14.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3485) rss_mb | MB | 8 | 242.607 | 172.934 | 299.281 | 299.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3485) main thread run-queue wait | percent | 7 | 47.768 | 41.825 | 55.328 | 49.488 | 3.371263 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3485) vms_mb | MB | 8 | 522.340 | 485.898 | 546.902 | 546.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3505) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3505) rss_mb | MB | 4 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3505) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3505) vms_mb | MB | 4 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3506) CPU | percent | 3 | 197.102 | 194.957 | 198.539 | 197.810 | 5.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3506) rss_mb | MB | 4 | 206.625 | 141.270 | 269.879 | 269.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3506) main thread run-queue wait | percent | 3 | 44.939 | 41.405 | 46.978 | 46.978 | 1.356630 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3506) vms_mb | MB | 4 | 438.283 | 358.078 | 518.488 | 518.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3525) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3525) rss_mb | MB | 15 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3525) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3525) vms_mb | MB | 15 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3526) CPU | percent | 14 | 199.270 | 190.353 | 211.669 | 197.801 | 28.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3526) rss_mb | MB | 15 | 190.782 | 87.191 | 263.359 | 231.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3526) main thread run-queue wait | percent | 14 | 48.070 | 45.551 | 51.087 | 45.551 | 6.776250 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3526) vms_mb | MB | 15 | 462.233 | 350.953 | 479.152 | 479.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3539) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3539) rss_mb | MB | 5 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3539) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — timeout (PID 3539) vms_mb | MB | 5 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3541) CPU | percent | 4 | 187.382 | 178.743 | 201.260 | 186.894 | 7.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3541) rss_mb | MB | 5 | 168.386 | 17.250 | 367.164 | 36.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3541) main thread run-queue wait | percent | 4 | 43.248 | 35.389 | 51.242 | 50.313 | 1.742506 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3541) vms_mb | MB | 5 | 1752.359 | 209.730 | 2325.281 | 1917.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3565) CPU | percent | 3 | 188.625 | 169.237 | 198.816 | 198.816 | 5.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3565) rss_mb | MB | 4 | 68.356 | 0.000 | 99.195 | 99.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3565) main thread run-queue wait | percent | 3 | 43.436 | 33.105 | 49.497 | 49.497 | 1.312317 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3565) vms_mb | MB | 4 | 1478.468 | 0.387 | 1975.160 | 1975.160 | n/a | n/a |
| docker commit (PID 3612) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 3612) io read MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3612) io write MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3612) rss_mb | MB | 119 | 30.560 | 30.426 | 30.605 | 30.605 | n/a | n/a |
| docker commit (PID 3612) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 3612) vms_mb | MB | 119 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| docker commit (PID 3699) CPU | percent | 43 | 0.046 | 0.000 | 1.989 | 0.000 | 0.020000 CPU seconds | n/a |
| docker commit (PID 3699) io read MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3699) io write MB/s | MB/s | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3699) rss_mb | MB | 44 | 28.633 | 18.719 | 28.863 | 28.863 | n/a | n/a |
| docker commit (PID 3699) main thread run-queue wait | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 3699) vms_mb | MB | 44 | 1767.642 | 1625.598 | 1770.945 | 1770.945 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 1560 | 29.225 | 0.000 | 212.411 | 0.000 | 459.128541 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1560 | 6.091 | 0.000 | 50.332 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1560 | 6.218 | 0.000 | 58.143 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 1560 | 1.836 | 0.000 | 99.637 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 1560 | 1.845 | 0.000 | 99.640 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 1560 | 0.046 | 0.000 | 3.829 | 0.000 | 72.781250 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 1560 | 0.001 | 0.000 | 0.563 | 0.000 | 1.464844 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 1561 | 248.971 | 7.805 | 1341.344 | 179.121 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1560 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1560 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 1560 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000534 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 1560 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 1586 | 5.737 | 1.658 | 101.967 | 2.022 | 91.622097 CPU seconds | n/a |
| workload total memory | MB | 1587 | 9406.887 | 8411.281 | 9833.473 | 9833.473 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
