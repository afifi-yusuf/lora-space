# agprof summary

- Duration: **13923.791 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **138 calls**, 138 succeeded, 0 failed, 0 interrupted, n/a reported retries, 12462.100 s total wait
- Tools: **152/152 completed**, 2 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **1373867** at 1.971 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 13902242.855 / 13902242.855 ms |
| LLM latency p50 / p95 | 52436.019 / 293773.024 ms |
| LLM TTFT p50 / p95 | 34500.425 / 287868.205 ms |
| LLM input / output tokens | 20956027 / 198535 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 138 total, 138 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 692.764 / 52838.392 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 2/2 | 2 | 0 | 0 | 344.737 ms | 354.478 ms |
| attribution | 4/4 | 4 | 0 | 0 | 332.337 ms | 374.912 ms |
| bash | 92/92 | 90 | 2 | 0 | 585.952 ms | 80187.231 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 478.193 ms | 478.193 ms |
| generate | 10/10 | 10 | 0 | 0 | 17066.120 ms | 34166.651 ms |
| get_current_resources | 2/2 | 2 | 0 | 0 | 240.808 ms | 242.346 ms |
| inspect | 5/5 | 5 | 0 | 0 | 1138.603 ms | 2309.286 ms |
| inspect_module_inputs | 5/5 | 5 | 0 | 0 | 1594.707 ms | 2066.016 ms |
| logit_lens | 3/3 | 3 | 0 | 0 | 982.550 ms | 3090.385 ms |
| patch | 2/2 | 2 | 0 | 0 | 439.283 ms | 442.074 ms |
| read | 3/3 | 3 | 0 | 0 | 0.621 ms | 0.735 ms |
| release_resource | 1/1 | 1 | 0 | 0 | 814.585 ms | 814.585 ms |
| reserve_resource | 1/1 | 1 | 0 | 0 | 315.036 ms | 315.036 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 244.648 ms | 244.648 ms |
| todowrite | 2/2 | 2 | 0 | 0 | 0.187 ms | 0.223 ms |
| trace | 15/15 | 15 | 0 | 0 | 956.386 ms | 16030.341 ms |
| write | 3/3 | 3 | 0 | 0 | 0.418 ms | 0.572 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 3.141% | 101.868% | 437.855 s | 8480.463 MB | 13410.586 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lsb_grid_worker | 30393 |  | 13839 | 0.000% | 0.000% | 0.000 s | 3.059 MB | 3.359 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 30556 |  | 13839 | 0.033% | 5.968% | 4.660 s | 44.275 MB | 47.598 MB | 203.266 MB | 204.273 MB | 4.453125 MB | 0.468750 MB |
| docker | 30564 |  | 1 | n/a% | n/a% | n/a s | 30.137 MB | 30.137 MB | 1843.520 MB | 1843.520 MB | n/a MB | n/a MB |
| python | 30408 |  | 13839 | 1.198% | 102.108% | 166.990 s | 3272.827 MB | 7184.652 MB | 16435.254 MB | 20475.047 MB | 1145.988281 MB | 7419.359375 MB |
| python | 30452 |  | 13839 | 0.000% | 0.000% | 0.000 s | 11.359 MB | 12.184 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 30453 |  | 13839 | 1.766% | 58.614% | 246.100 s | 2236.220 MB | 2312.453 MB | 21204.972 MB | 21205.281 MB | 3.054688 MB | 0.093750 MB |
| vllm | 30418 |  | 13839 | 0.140% | 7.948% | 19.510 s | 1724.776 MB | 1786.418 MB | 11031.800 MB | 11036.375 MB | 1.011719 MB | 0.078125 MB |
| docker | 30694 |  | 1 | n/a% | n/a% | n/a s | 31.023 MB | 31.023 MB | 1843.262 MB | 1843.262 MB | n/a MB | n/a MB |
| tail | 30763 | sandbox_agent_lsb-native_0000_0000 | 13816 | 0.003% | 1.989% | 0.440 s | 1.146 MB | 1.414 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 30861 | sandbox_agent_lsb-native_0000_0000 | 2 | 58.216% | 58.216% | 0.590 s | 51.168 MB | 63.719 MB | 59.465 MB | 72.801 MB | n/a MB | n/a MB |
| docker-init | 30734 | sandbox_agent_lsb-native_0000_0000 | 13816 | 0.003% | 0.995% | 0.360 s | 0.494 MB | 0.539 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 30855 | sandbox_agent_lsb-native_0000_0000 | 13816 | 3.519% | 101.439% | 489.690 s | 101.450 MB | 107.145 MB | 971.035 MB | 972.191 MB | n/a MB | n/a MB |
| python3 | 30873 | sandbox_agent_lsb-native_0000_0000 | 13787 | 0.036% | 52.463% | 5.010 s | 71.191 MB | 75.434 MB | 87.413 MB | 90.816 MB | n/a MB | n/a MB |
| python3 | 31053 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.379 MB | 22.379 MB | 215.445 MB | 215.445 MB | n/a MB | n/a MB |
| python3 | 31152 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.449 MB | 9.449 MB | 13.535 MB | 13.535 MB | n/a MB | n/a MB |
| bash | 31543 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| python3 | 31702 | sandbox_agent_lsb-native_0000_0000 | 4 | 100.045% | 100.396% | 3.020 s | 11.184 MB | 11.246 MB | 15.074 MB | 15.074 MB | n/a MB | n/a MB |
| python3 | 31848 | sandbox_agent_lsb-native_0000_0000 | 3 | 99.710% | 100.365% | 2.020 s | 10.493 MB | 10.535 MB | 14.762 MB | 14.762 MB | n/a MB | n/a MB |
| python3 | 32092 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1997.766 MB | 1997.766 MB | 2702.051 MB | 2702.051 MB | n/a MB | n/a MB |
| python3 | 32111 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.953 MB | 13.953 MB | 207.488 MB | 207.488 MB | n/a MB | n/a MB |
| python3 | 32179 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1088.246 MB | 1088.246 MB | 1310.691 MB | 1310.691 MB | n/a MB | n/a MB |
| python3 | 32191 | sandbox_agent_lsb-native_0000_0000 | 3 | 193.717% | 196.569% | 3.920 s | 1087.111 MB | 1097.445 MB | 1309.371 MB | 1319.547 MB | n/a MB | n/a MB |
| python3 | 32206 | sandbox_agent_lsb-native_0000_0000 | 28 | 198.979% | 207.489% | 54.160 s | 1117.175 MB | 2491.930 MB | 1338.614 MB | 2702.121 MB | n/a MB | n/a MB |
| python3 | 32222 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 56.867 MB | 56.867 MB | 249.363 MB | 249.363 MB | n/a MB | n/a MB |
| python3 | 32268 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 681.945 MB | 681.945 MB | 1671.078 MB | 1671.078 MB | n/a MB | n/a MB |
| python3 | 32280 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 56.023 MB | 56.023 MB | 248.422 MB | 248.422 MB | n/a MB | n/a MB |
| python3 | 32325 | sandbox_agent_lsb-native_0000_0000 | 4 | 100.032% | 100.376% | 3.020 s | 12.828 MB | 12.828 MB | 16.996 MB | 16.996 MB | n/a MB | n/a MB |
| python3 | 32378 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.035 MB | 14.035 MB | 207.512 MB | 207.512 MB | n/a MB | n/a MB |
| python3 | 32414 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 25.332 MB | 25.332 MB | 217.605 MB | 217.605 MB | n/a MB | n/a MB |
| python3 | 32504 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.996 MB | 19.996 MB | 212.117 MB | 212.117 MB | n/a MB | n/a MB |
| python3 | 32704 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.910 MB | 18.910 MB | 211.270 MB | 211.270 MB | n/a MB | n/a MB |
| python3 | 32731 | sandbox_agent_lsb-native_0000_0000 | 3 | 58.029% | 94.195% | 1.170 s | 844.228 MB | 1341.090 MB | 997.870 MB | 1564.551 MB | n/a MB | n/a MB |
| python3 | 32782 | sandbox_agent_lsb-native_0000_0000 | 119 | 180.369% | 211.821% | 214.460 s | 3293.698 MB | 3719.430 MB | 3562.815 MB | 3935.574 MB | n/a MB | n/a MB |
| python3 | 32831 | sandbox_agent_lsb-native_0000_0000 | 53 | 145.358% | 212.414% | 76.140 s | 376.705 MB | 538.039 MB | 624.241 MB | 753.195 MB | n/a MB | n/a MB |
| python3 | 32873 | sandbox_agent_lsb-native_0000_0000 | 13 | 164.810% | 349.982% | 19.950 s | 258.884 MB | 530.531 MB | 524.335 MB | 745.727 MB | n/a MB | n/a MB |
| python3 | 32891 | sandbox_agent_lsb-native_0000_0000 | 25 | 153.459% | 364.908% | 37.090 s | 462.574 MB | 663.965 MB | 718.036 MB | 908.695 MB | n/a MB | n/a MB |
| python3 | 33027 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 507.980 MB | 507.980 MB | 757.379 MB | 757.379 MB | n/a MB | n/a MB |
| python3 | 33064 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.156 MB | 14.156 MB | 208.652 MB | 208.652 MB | n/a MB | n/a MB |
| python3 | 33075 | sandbox_agent_lsb-native_0000_0000 | 2 | 203.350% | 203.350% | 2.050 s | 1046.586 MB | 1181.691 MB | 1566.789 MB | 1727.363 MB | n/a MB | n/a MB |
| python3 | 33088 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 524.316 MB | 524.316 MB | 757.246 MB | 757.246 MB | n/a MB | n/a MB |
| python3 | 33112 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 346.164 MB | 346.164 MB | 757.184 MB | 757.184 MB | n/a MB | n/a MB |
| python3 | 33132 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 332.434 MB | 332.434 MB | 758.699 MB | 758.699 MB | n/a MB | n/a MB |
| python3 | 33148 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.055 MB | 14.055 MB | 207.504 MB | 207.504 MB | n/a MB | n/a MB |
| python3 | 33169 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.746 MB | 20.746 MB | 212.414 MB | 212.414 MB | n/a MB | n/a MB |
| python3 | 33187 | sandbox_agent_lsb-native_0000_0000 | 3 | 385.316% | 385.364% | 7.780 s | 178.055 MB | 212.082 MB | 398.628 MB | 431.652 MB | n/a MB | n/a MB |
| python3 | 33219 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 460.438 MB | 460.438 MB | 764.129 MB | 764.129 MB | n/a MB | n/a MB |
| python3 | 33231 | sandbox_agent_lsb-native_0000_0000 | 3 | 275.786% | 337.875% | 5.560 s | 941.203 MB | 1173.594 MB | 1180.786 MB | 1394.098 MB | n/a MB | n/a MB |
| python3 | 33245 | sandbox_agent_lsb-native_0000_0000 | 6 | 259.355% | 346.884% | 13.130 s | 2648.469 MB | 3750.574 MB | 3179.108 MB | 4332.281 MB | n/a MB | n/a MB |
| python3 | 33262 | sandbox_agent_lsb-native_0000_0000 | 41 | 151.628% | 384.383% | 61.130 s | 3045.710 MB | 4093.348 MB | 3908.853 MB | 4313.922 MB | n/a MB | n/a MB |
| python3 | 33298 | sandbox_agent_lsb-native_0000_0000 | 26 | 189.804% | 397.532% | 47.790 s | 2930.190 MB | 4073.074 MB | 3693.274 MB | 4294.059 MB | n/a MB | n/a MB |
| python3 | 33319 | sandbox_agent_lsb-native_0000_0000 | 44 | 165.539% | 367.764% | 71.650 s | 2821.456 MB | 3986.723 MB | 3767.139 MB | 4353.965 MB | n/a MB | n/a MB |
| python3 | 33337 | sandbox_agent_lsb-native_0000_0000 | 44 | 167.048% | 385.643% | 72.330 s | 2766.427 MB | 4073.809 MB | 3776.135 MB | 4294.133 MB | n/a MB | n/a MB |
| python3 | 33373 | sandbox_agent_lsb-native_0000_0000 | 40 | 332.330% | 385.625% | 130.760 s | 2348.061 MB | 4118.098 MB | 2700.881 MB | 4340.094 MB | n/a MB | n/a MB |
| python3 | 33391 | sandbox_agent_lsb-native_0000_0000 | 120 | 127.143% | 397.348% | 152.310 s | 2122.917 MB | 3263.246 MB | 3186.361 MB | 3476.754 MB | n/a MB | n/a MB |
| python3 | 33429 | sandbox_agent_lsb-native_0000_0000 | 20 | 144.978% | 364.654% | 27.720 s | 2885.447 MB | 4194.277 MB | 3660.801 MB | 4493.559 MB | n/a MB | n/a MB |
| bash | 33452 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 33454 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1359.516 MB | 1359.516 MB | 1734.117 MB | 1734.117 MB | n/a MB | n/a MB |
| python3 | 33458 | sandbox_agent_lsb-native_0000_0000 | 3 | 248.828% | 284.224% | 5.010 s | 1562.734 MB | 2098.234 MB | 1831.017 MB | 2364.453 MB | n/a MB | n/a MB |
| python3 | 33498 | sandbox_agent_lsb-native_0000_0000 | 14 | 153.812% | 370.254% | 20.150 s | 472.078 MB | 789.906 MB | 723.113 MB | 1030.770 MB | n/a MB | n/a MB |
| python3 | 33518 | sandbox_agent_lsb-native_0000_0000 | 52 | 211.651% | 397.620% | 108.770 s | 2494.507 MB | 2776.715 MB | 2767.145 MB | 2990.102 MB | n/a MB | n/a MB |
| python3 | 33611 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.809 MB | 7.809 MB | 12.930 MB | 12.930 MB | n/a MB | n/a MB |
| python3 | 33626 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.129 MB | 7.129 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| python3 | 33649 | sandbox_agent_lsb-native_0000_0000 | 79 | 196.293% | 398.133% | 154.920 s | 5206.447 MB | 6997.578 MB | 5903.817 MB | 7262.871 MB | n/a MB | n/a MB |
| python3 | 33712 | sandbox_agent_lsb-native_0000_0000 | 100 | 116.731% | 181.816% | 116.270 s | 2984.234 MB | 3965.133 MB | 4180.387 MB | 4311.234 MB | n/a MB | n/a MB |
| python3 | 33738 | sandbox_agent_lsb-native_0000_0000 | 80 | 117.670% | 319.646% | 93.570 s | 3091.101 MB | 4858.449 MB | 4039.366 MB | 5259.000 MB | n/a MB | n/a MB |
| python3 | 33810 | sandbox_agent_lsb-native_0000_0000 | 21 | 119.990% | 205.678% | 24.140 s | 2830.412 MB | 3687.312 MB | 4149.237 MB | 4269.969 MB | n/a MB | n/a MB |
| python3 | 33827 | sandbox_agent_lsb-native_0000_0000 | 57 | 206.587% | 397.614% | 116.550 s | 2460.094 MB | 2881.062 MB | 2725.831 MB | 3127.070 MB | n/a MB | n/a MB |
| python3 | 33859 | sandbox_agent_lsb-native_0000_0000 | 90 | 169.387% | 397.626% | 152.440 s | 5237.074 MB | 7032.719 MB | 5822.145 MB | 7264.512 MB | n/a MB | n/a MB |
| bash | 33858 | sandbox_agent_lsb-native_0000_0000 | 91 | 0.000% | 0.000% | 0.000 s | 2.359 MB | 2.727 MB | 4.205 MB | 4.215 MB | n/a MB | n/a MB |
| docker | 33886 |  | 1 | n/a% | n/a% | n/a s | 27.719 MB | 27.719 MB | 1770.754 MB | 1770.754 MB | n/a MB | n/a MB |
| docker | 34019 |  | 1 | n/a% | n/a% | n/a s | 30.305 MB | 30.305 MB | 1843.512 MB | 1843.512 MB | n/a MB | n/a MB |
| docker | 34036 |  | 23 | 0.000% | 0.000% | 0.000 s | 30.336 MB | 30.336 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.307% | 100.000% | 12070.561 MB | 12674.000 MB | 30.363 W | 74.043 W | 422737.451 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 17.005% | 398.541% | 2367.820 s | 749.961 MB | 7297.508 MB | 10764.203125 MB | 2.429688 MB | 0.001040 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 30562 | 13923.724 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 13902.243 | n/a | n/a | 10764.203 | 13902242.855 | 13902242.855 | 13902242.855 |
| engine:execute | 1/1 | 0 | 0 | 13902.241 | 10.217 | 13891.982 | 10764.203 | 13902241.104 | 13902241.104 | 13902241.104 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 13872.074 | 0.005 | 13872.069 | 10745.280 | 13872073.779 | 13872073.779 | 13872073.779 |
| turn | 137/137 | 0 | 0 | 13868.191 | n/a | n/a | 10742.544 | 101227.673 | 62222.941 | 294935.901 |
| llm:attempt | 138/138 | 0 | 0 | 12462.100 | 6.231 | 12455.869 | 31.463 | 90305.075 | 52436.019 | 293773.024 |
| tool:bash | 92/92 | 2 | 0 | 1134.045 | n/a | n/a | 10694.114 | 12326.581 | 585.952 | 80187.231 |
| process:bash | 92/92 | 18 | 0 | 1132.793 | n/a | n/a | 10693.343 | 12312.971 | 556.491 | 80154.401 |
| tool:generate | 10/10 | 0 | 0 | 173.295 | n/a | n/a | 0.000 | 17329.467 | 17066.120 | 34166.651 |
| llm:compact | 1/1 | 0 | 0 | 119.257 | n/a | n/a | 0.000 | 119257.429 | 119257.429 | 119257.429 |
| tool:trace | 15/15 | 0 | 0 | 59.348 | n/a | n/a | 0.354 | 3956.521 | 956.386 | 16030.341 |
| run:container_call | 17/17 | 0 | 0 | 24.771 | 0.003 | 24.768 | 2.717 | 1457.127 | 56.047 | 4910.614 |
| teardown:commit | 1/1 | 0 | 0 | 23.669 | 0.005 | 23.664 | 0.016 | 23669.139 | 23669.139 | 23669.139 |
| sandbox:commit | 1/1 | 0 | 0 | 23.417 | 0.003 | 23.414 | 0.016 | 23416.571 | 23416.571 | 23416.571 |
| checkpoint.total | 1/1 | 0 | 0 | 23.416 | 0.003 | 23.414 | 0.016 | 23416.426 | 23416.426 | 23416.426 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 23.416 | 0.002 | 23.414 | 0.016 | 23416.278 | 23416.278 | 23416.278 |
| tool:inspect_module_inputs | 5/5 | 0 | 0 | 7.995 | n/a | n/a | 0.000 | 1599.084 | 1594.707 | 2066.016 |
| syscall:sendto | 2967/2967 | 0 | 0 | 7.047 | n/a | n/a | 3.548 | 2.375 | 2.064 | 4.476 |
| tool:inspect | 5/5 | 0 | 0 | 6.573 | n/a | n/a | 0.643 | 1314.528 | 1138.603 | 2309.286 |
| tool:logit_lens | 3/3 | 0 | 0 | 5.048 | n/a | n/a | 0.498 | 1682.677 | 982.550 | 3090.385 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.481 | 1.040 | 3.441 | 18.829 | 4481.123 | 4481.123 | 4481.123 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.481 | 1.039 | 3.441 | 18.829 | 4480.840 | 4480.840 | 4480.840 |
| syscall:connect | 817/817 | 0 | 0 | 2.055 | n/a | n/a | 1.624 | 2.515 | 2.109 | 4.631 |
| sandbox:create | 1/1 | 0 | 0 | 1.633 | 0.258 | 1.375 | 0.000 | 1633.263 | 1633.263 | 1633.263 |
| tool:attribution | 4/4 | 0 | 0 | 1.367 | n/a | n/a | 0.000 | 341.799 | 332.337 | 374.912 |
| tool:patch | 2/2 | 0 | 0 | 0.879 | n/a | n/a | 0.000 | 439.283 | 439.283 | 442.074 |
| run:detect | 1/1 | 0 | 0 | 0.855 | 0.001 | 0.854 | 0.000 | 854.889 | 854.889 | 854.889 |
| tool:release_resource | 1/1 | 0 | 0 | 0.815 | n/a | n/a | 3.743 | 814.585 | 814.585 | 814.585 |
| tool:attention | 2/2 | 0 | 0 | 0.689 | n/a | n/a | 0.000 | 344.737 | 344.737 | 354.478 |
| sandbox:update_limits | 2/2 | 0 | 0 | 0.608 | 0.003 | 0.605 | 2.706 | 304.054 | 304.054 | 514.215 |
| syscall:execve | 308/308 | 0 | 0 | 0.525 | n/a | n/a | 3.741 | 1.705 | 1.215 | 3.468 |
| tool:get_current_resources | 2/2 | 0 | 0 | 0.482 | n/a | n/a | 0.001 | 240.808 | 240.808 | 242.346 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.478 | n/a | n/a | 0.000 | 478.193 | 478.193 | 478.193 |
| sandbox:start | 1/1 | 0 | 0 | 0.425 | 0.002 | 0.423 | 0.000 | 425.439 | 425.439 | 425.439 |
| runtime.container_create | 1/1 | 0 | 0 | 0.425 | 0.002 | 0.423 | 0.000 | 425.292 | 425.292 | 425.292 |
| tool:reserve_resource | 1/1 | 0 | 0 | 0.315 | n/a | n/a | 0.000 | 315.036 | 315.036 | 315.036 |
| sandbox:stop | 1/1 | 0 | 0 | 0.252 | 0.002 | 0.251 | 0.000 | 252.273 | 252.273 | 252.273 |
| tool:submit_output | 1/1 | 0 | 0 | 0.245 | n/a | n/a | 0.000 | 244.648 | 244.648 | 244.648 |
| agency:services_close | 1/1 | 0 | 0 | 0.172 | 0.001 | 0.171 | 0.025 | 171.543 | 171.543 | 171.543 |
| agency:services_start | 1/1 | 0 | 0 | 0.087 | 0.044 | 0.043 | 0.000 | 87.189 | 87.189 | 87.189 |
| agent:create | 1/1 | 0 | 0 | 0.051 | 0.009 | 0.042 | 0.000 | 50.790 | 50.790 | 50.790 |
| tool:read | 3/3 | 0 | 0 | 0.002 | n/a | n/a | 0.000 | 0.575 | 0.621 | 0.735 |
| tool:write | 3/3 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.472 | 0.418 | 0.572 |
| sync:container | 17/17 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.001 | 0.074 | 0.074 | 0.104 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.214 | 1.214 | 1.214 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.635 | 0.635 | 0.635 |
| tool:todowrite | 2/2 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.187 | 0.187 | 0.223 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.165 | 0.165 | 0.165 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.083 | 0.083 | 0.083 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 13836 | 0.115 | 0.012 | 46.855 | 0.031 | 16.015027 CPU seconds | n/a |
| GPU 0 memory | MB | 13839 | 12070.561 | 11670.000 | 12674.000 | 12062.000 | n/a | n/a |
| GPU 0 power | W | 13839 | 30.363 | 29.591 | 74.043 | 29.682 | n/a | 422737.451 J |
| GPU 0 proc / 30408-5019853 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc memory | MB | 13839 | 3275.412 | 3118.000 | 3826.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 30408-5019853 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc estimated power | W | 9909 | 0.203 | 0.000 | 63.306 | 0.000 | n/a | n/a |
| GPU 0 proc / 30408-5019853 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc utilization | percent | 9909 | 0.123 | 0.000 | 76.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 30453-5023704 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc memory | MB | 13839 | 8313.149 | 8070.000 | 8366.000 | 8366.000 | n/a | n/a |
| GPU 0 proc / 30453-5023704 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc estimated power | W | 3699 | 3.192 | 0.000 | 73.217 | 0.000 | n/a | n/a |
| GPU 0 proc / 30453-5023704 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc utilization | percent | 3699 | 4.355 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 13839 | 11588.561 | 11188.000 | 12192.000 | 11580.000 | n/a | n/a |
| GPU 0 utilization | percent | 13839 | 1.307 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 13839 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 13838 | 1.061 | 0.008 | 52.240 | 0.215 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 13838 | 4.873 | 0.250 | 100.000 | 0.500 | n/a | n/a |
| host disk_read_mb_s | MB/s | 13838 | 0.981 | 0.000 | 234.039 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 13838 | 0.536 | 0.000 | 235.120 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 13838 | 0.407 | 0.000 | 96.517 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 13838 | 0.424 | 0.000 | 97.514 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 13839 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 13839 | 7643.304 | 6703.164 | 15203.129 | 8102.383 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 13838 | 0.036 | 0.000 | 24.469 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 13838 | 0.036 | 0.000 | 24.585 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 13838 | 0.000 | 0.000 | 0.070 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 13838 | 0.005 | 0.000 | 1.122 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 30393) CPU | percent | 13838 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 30393) io read MB/s | MB/s | 13838 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 30393) io write MB/s | MB/s | 13838 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 30393) rss_mb | MB | 13839 | 3.059 | 2.105 | 3.359 | 2.105 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 30393) main thread run-queue wait | percent | 13838 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 30393) vms_mb | MB | 13839 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 30408) CPU | percent | 13838 | 1.198 | 0.000 | 102.108 | 0.000 | 166.990000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 30408) io read MB/s | MB/s | 13838 | 0.082 | 0.000 | 125.262 | 0.000 | 1145.988281 MB | n/a |
| Agency harness — python -m lsbench (PID 30408) io write MB/s | MB/s | 13838 | 0.532 | 0.000 | 778.980 | 0.000 | 7419.359375 MB | n/a |
| Agency harness — python -m lsbench (PID 30408) rss_mb | MB | 13839 | 3272.827 | 2553.418 | 7184.652 | 3798.586 | n/a | n/a |
| Agency harness — python -m lsbench (PID 30408) main thread run-queue wait | percent | 13838 | 0.000 | 0.000 | 3.646 | 0.000 | 0.060709 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 30408) vms_mb | MB | 13839 | 16435.254 | 14094.812 | 20475.047 | 17305.469 | n/a | n/a |
| Python — vllm (PID 30418) CPU | percent | 13838 | 0.140 | 0.000 | 7.948 | 0.000 | 19.510000 CPU seconds | n/a |
| Python — vllm (PID 30418) io read MB/s | MB/s | 13838 | 0.000 | 0.000 | 0.849 | 0.000 | 1.011719 MB | n/a |
| Python — vllm (PID 30418) io write MB/s | MB/s | 13838 | 0.000 | 0.000 | 0.004 | 0.000 | 0.078125 MB | n/a |
| Python — vllm (PID 30418) rss_mb | MB | 13839 | 1724.776 | 1404.105 | 1786.418 | 1404.105 | n/a | n/a |
| Python — vllm (PID 30418) main thread run-queue wait | percent | 13838 | 0.002 | 0.000 | 10.062 | 0.000 | 0.265810 run-queue seconds | n/a |
| Python — vllm (PID 30418) vms_mb | MB | 13839 | 11031.800 | 10963.355 | 11036.375 | 11036.375 | n/a | n/a |
| Python — python -c (PID 30452) CPU | percent | 13838 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 30452) io read MB/s | MB/s | 13838 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 30452) io write MB/s | MB/s | 13838 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 30452) rss_mb | MB | 13839 | 11.359 | 8.680 | 12.184 | 8.680 | n/a | n/a |
| Python — python -c (PID 30452) main thread run-queue wait | percent | 13838 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 30452) vms_mb | MB | 13839 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 30453) CPU | percent | 13838 | 1.766 | 0.000 | 58.614 | 0.995 | 246.100000 CPU seconds | n/a |
| VLLM::EngineCore (PID 30453) io read MB/s | MB/s | 13838 | 0.000 | 0.000 | 1.509 | 0.000 | 3.054688 MB | n/a |
| VLLM::EngineCore (PID 30453) io write MB/s | MB/s | 13838 | 0.000 | 0.000 | 0.008 | 0.000 | 0.093750 MB | n/a |
| VLLM::EngineCore (PID 30453) rss_mb | MB | 13839 | 2236.220 | 1830.328 | 2312.453 | 1830.328 | n/a | n/a |
| VLLM::EngineCore (PID 30453) main thread run-queue wait | percent | 13838 | 0.000 | 0.000 | 0.208 | 0.000 | 0.023642 run-queue seconds | n/a |
| VLLM::EngineCore (PID 30453) vms_mb | MB | 13839 | 21204.972 | 21204.133 | 21205.281 | 21205.266 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 30556) CPU | percent | 13838 | 0.033 | 0.000 | 5.968 | 0.000 | 4.660000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 30556) io read MB/s | MB/s | 13838 | 0.000 | 0.000 | 3.611 | 0.000 | 4.453125 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 30556) io write MB/s | MB/s | 13838 | 0.000 | 0.000 | 0.008 | 0.000 | 0.468750 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 30556) rss_mb | MB | 13839 | 44.275 | 34.211 | 47.598 | 36.828 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 30556) main thread run-queue wait | percent | 13838 | 0.000 | 0.000 | 0.343 | 0.000 | 0.056052 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 30556) vms_mb | MB | 13839 | 203.266 | 131.172 | 204.273 | 203.176 | n/a | n/a |
| docker info (PID 30564) rss_mb | MB | 1 | 30.137 | 30.137 | 30.137 | 30.137 | n/a | n/a |
| docker info (PID 30564) vms_mb | MB | 1 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker run (PID 30694) rss_mb | MB | 1 | 31.023 | 31.023 | 31.023 | 31.023 | n/a | n/a |
| docker run (PID 30694) vms_mb | MB | 1 | 1843.262 | 1843.262 | 1843.262 | 1843.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 30734) CPU | percent | 13815 | 0.003 | 0.000 | 0.995 | 0.000 | 0.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 30734) rss_mb | MB | 13816 | 0.494 | 0.289 | 0.539 | 0.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 30734) main thread run-queue wait | percent | 13815 | 0.002 | 0.000 | 4.910 | 0.000 | 0.209157 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 30734) vms_mb | MB | 13816 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 30763) CPU | percent | 13815 | 0.003 | 0.000 | 1.989 | 0.000 | 0.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 30763) rss_mb | MB | 13816 | 1.146 | 0.164 | 1.414 | 0.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 30763) main thread run-queue wait | percent | 13815 | 0.001 | 0.000 | 3.765 | 0.000 | 0.133987 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 30763) vms_mb | MB | 13816 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 30855) CPU | percent | 13815 | 3.519 | 0.000 | 101.439 | 0.000 | 489.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 30855) rss_mb | MB | 13816 | 101.450 | 2.930 | 107.145 | 97.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 30855) main thread run-queue wait | percent | 13815 | 0.000 | 0.000 | 0.016 | 0.000 | 0.000187 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 30855) vms_mb | MB | 13816 | 971.035 | 4.258 | 972.191 | 972.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 30861) CPU | percent | 1 | 58.216 | 58.216 | 58.216 | 58.216 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 30861) rss_mb | MB | 2 | 51.168 | 38.617 | 63.719 | 63.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 30861) main thread run-queue wait | percent | 1 | 0.019 | 0.019 | 0.019 | 0.019 | 0.000197 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 30861) vms_mb | MB | 2 | 59.465 | 46.129 | 72.801 | 72.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 30873) CPU | percent | 13786 | 0.036 | 0.000 | 52.463 | 0.000 | 5.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 30873) rss_mb | MB | 13787 | 71.191 | 40.293 | 75.434 | 62.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 30873) main thread run-queue wait | percent | 13786 | 0.003 | 0.000 | 5.789 | 0.000 | 0.411876 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 30873) vms_mb | MB | 13787 | 87.413 | 48.512 | 90.816 | 88.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31053) rss_mb | MB | 1 | 22.379 | 22.379 | 22.379 | 22.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31053) vms_mb | MB | 1 | 215.445 | 215.445 | 215.445 | 215.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31152) rss_mb | MB | 1 | 9.449 | 9.449 | 9.449 | 9.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31152) vms_mb | MB | 1 | 13.535 | 13.535 | 13.535 | 13.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 31543) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 31543) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31702) CPU | percent | 3 | 100.045 | 99.386 | 100.396 | 100.396 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31702) rss_mb | MB | 4 | 11.184 | 11.121 | 11.246 | 11.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31702) main thread run-queue wait | percent | 3 | 0.006 | 0.005 | 0.006 | 0.006 | 0.000177 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31702) vms_mb | MB | 4 | 15.074 | 15.074 | 15.074 | 15.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31848) CPU | percent | 2 | 99.710 | 99.055 | 100.365 | 100.365 | 2.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31848) rss_mb | MB | 3 | 10.493 | 10.410 | 10.535 | 10.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31848) main thread run-queue wait | percent | 2 | 0.003 | 0.002 | 0.004 | 0.002 | 0.000061 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 31848) vms_mb | MB | 3 | 14.762 | 14.762 | 14.762 | 14.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32092) rss_mb | MB | 1 | 1997.766 | 1997.766 | 1997.766 | 1997.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32092) vms_mb | MB | 1 | 2702.051 | 2702.051 | 2702.051 | 2702.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32111) rss_mb | MB | 1 | 13.953 | 13.953 | 13.953 | 13.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32111) vms_mb | MB | 1 | 207.488 | 207.488 | 207.488 | 207.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32179) rss_mb | MB | 1 | 1088.246 | 1088.246 | 1088.246 | 1088.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32179) vms_mb | MB | 1 | 1310.691 | 1310.691 | 1310.691 | 1310.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32191) CPU | percent | 2 | 193.717 | 190.865 | 196.569 | 196.569 | 3.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32191) rss_mb | MB | 3 | 1087.111 | 1072.934 | 1097.445 | 1090.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32191) main thread run-queue wait | percent | 2 | 39.689 | 39.488 | 39.891 | 39.891 | 0.803142 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32191) vms_mb | MB | 3 | 1309.371 | 1295.547 | 1319.547 | 1313.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32206) CPU | percent | 27 | 198.979 | 195.889 | 207.489 | 198.192 | 54.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32206) rss_mb | MB | 28 | 1117.175 | 1066.188 | 2491.930 | 1066.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32206) main thread run-queue wait | percent | 27 | 50.328 | 45.422 | 55.695 | 48.885 | 13.698293 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32206) vms_mb | MB | 28 | 1338.614 | 1288.113 | 2702.121 | 1288.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32222) rss_mb | MB | 1 | 56.867 | 56.867 | 56.867 | 56.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32222) vms_mb | MB | 1 | 249.363 | 249.363 | 249.363 | 249.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32268) rss_mb | MB | 1 | 681.945 | 681.945 | 681.945 | 681.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32268) vms_mb | MB | 1 | 1671.078 | 1671.078 | 1671.078 | 1671.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32280) rss_mb | MB | 1 | 56.023 | 56.023 | 56.023 | 56.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32280) vms_mb | MB | 1 | 248.422 | 248.422 | 248.422 | 248.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32325) CPU | percent | 3 | 100.032 | 99.387 | 100.376 | 100.376 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32325) rss_mb | MB | 4 | 12.828 | 12.828 | 12.828 | 12.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32325) main thread run-queue wait | percent | 3 | 0.002 | 0.002 | 0.002 | 0.002 | 0.000062 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32325) vms_mb | MB | 4 | 16.996 | 16.996 | 16.996 | 16.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32378) rss_mb | MB | 1 | 14.035 | 14.035 | 14.035 | 14.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32378) vms_mb | MB | 1 | 207.512 | 207.512 | 207.512 | 207.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32414) rss_mb | MB | 1 | 25.332 | 25.332 | 25.332 | 25.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32414) vms_mb | MB | 1 | 217.605 | 217.605 | 217.605 | 217.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32504) rss_mb | MB | 1 | 19.996 | 19.996 | 19.996 | 19.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32504) vms_mb | MB | 1 | 212.117 | 212.117 | 212.117 | 212.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32704) rss_mb | MB | 1 | 18.910 | 18.910 | 18.910 | 18.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 32704) vms_mb | MB | 1 | 211.270 | 211.270 | 211.270 | 211.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 32731) CPU | percent | 2 | 58.029 | 21.863 | 94.195 | 21.863 | 1.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 32731) rss_mb | MB | 3 | 844.228 | 74.684 | 1341.090 | 1341.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 32731) main thread run-queue wait | percent | 2 | 6.914 | 4.271 | 9.557 | 4.271 | 0.139365 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 32731) vms_mb | MB | 3 | 997.870 | 88.969 | 1564.551 | 1564.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_detectors.py (PID 32782) CPU | percent | 118 | 180.369 | 30.751 | 211.821 | 185.018 | 214.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_detectors.py (PID 32782) rss_mb | MB | 119 | 3293.698 | 46.480 | 3719.430 | 3623.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_detectors.py (PID 32782) main thread run-queue wait | percent | 118 | 41.330 | 0.040 | 55.027 | 38.650 | 49.142941 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_detectors.py (PID 32782) vms_mb | MB | 119 | 3562.815 | 295.230 | 3935.574 | 3934.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_detectors.py (PID 32831) CPU | percent | 52 | 145.358 | 23.871 | 212.414 | 201.140 | 76.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_detectors.py (PID 32831) rss_mb | MB | 53 | 376.705 | 22.078 | 538.039 | 537.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_detectors.py (PID 32831) main thread run-queue wait | percent | 52 | 25.732 | 0.040 | 44.673 | 39.023 | 13.476229 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_detectors.py (PID 32831) vms_mb | MB | 53 | 624.241 | 214.156 | 753.195 | 751.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_outliers.py (PID 32873) CPU | percent | 12 | 164.810 | 71.400 | 349.982 | 349.982 | 19.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_outliers.py (PID 32873) rss_mb | MB | 13 | 258.884 | 112.508 | 530.531 | 135.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_outliers.py (PID 32873) main thread run-queue wait | percent | 12 | 0.715 | 0.008 | 3.923 | 0.008 | 0.086557 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_outliers.py (PID 32873) vms_mb | MB | 13 | 524.335 | 348.785 | 745.727 | 348.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_midfunc_and_innerdef.py (PID 32891) CPU | percent | 24 | 153.459 | 70.469 | 364.908 | 137.038 | 37.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_midfunc_and_innerdef.py (PID 32891) rss_mb | MB | 25 | 462.574 | 141.066 | 663.965 | 444.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_midfunc_and_innerdef.py (PID 32891) main thread run-queue wait | percent | 24 | 1.058 | 0.069 | 5.130 | 0.110 | 0.255763 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_midfunc_and_innerdef.py (PID 32891) vms_mb | MB | 25 | 718.036 | 455.312 | 908.695 | 657.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_ov_and_nonrotary_qk.py (PID 33027) rss_mb | MB | 1 | 507.980 | 507.980 | 507.980 | 507.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_ov_and_nonrotary_qk.py (PID 33027) vms_mb | MB | 1 | 757.379 | 757.379 | 757.379 | 757.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33064) rss_mb | MB | 1 | 14.156 | 14.156 | 14.156 | 14.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33064) vms_mb | MB | 1 | 208.652 | 208.652 | 208.652 | 208.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_copy_circuit.py (PID 33075) CPU | percent | 1 | 203.350 | 203.350 | 203.350 | 203.350 | 2.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_copy_circuit.py (PID 33075) rss_mb | MB | 2 | 1046.586 | 911.480 | 1181.691 | 1181.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_copy_circuit.py (PID 33075) main thread run-queue wait | percent | 1 | 2.923 | 2.923 | 2.923 | 2.923 | 0.029463 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_copy_circuit.py (PID 33075) vms_mb | MB | 2 | 1566.789 | 1406.215 | 1727.363 | 1406.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_true_ov_and_v.py (PID 33088) rss_mb | MB | 1 | 524.316 | 524.316 | 524.316 | 524.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_true_ov_and_v.py (PID 33088) vms_mb | MB | 1 | 757.246 | 757.246 | 757.246 | 757.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — find_value_pos.py (PID 33112) rss_mb | MB | 1 | 346.164 | 346.164 | 346.164 | 346.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — find_value_pos.py (PID 33112) vms_mb | MB | 1 | 757.184 | 757.184 | 757.184 | 757.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_linattn_heads_at_def.py (PID 33132) rss_mb | MB | 1 | 332.434 | 332.434 | 332.434 | 332.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_linattn_heads_at_def.py (PID 33132) vms_mb | MB | 1 | 758.699 | 758.699 | 758.699 | 758.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_concise_def_shift.py (PID 33148) rss_mb | MB | 1 | 14.055 | 14.055 | 14.055 | 14.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_concise_def_shift.py (PID 33148) vms_mb | MB | 1 | 207.504 | 207.504 | 207.504 | 207.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_qk_on_non_assert.py (PID 33169) rss_mb | MB | 1 | 20.746 | 20.746 | 20.746 | 20.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_qk_on_non_assert.py (PID 33169) vms_mb | MB | 1 | 212.414 | 212.414 | 212.414 | 212.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_qnorm_and_attn_shift.py (PID 33187) CPU | percent | 2 | 385.316 | 385.268 | 385.364 | 385.364 | 7.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_qnorm_and_attn_shift.py (PID 33187) rss_mb | MB | 3 | 178.055 | 148.043 | 212.082 | 148.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_qnorm_and_attn_shift.py (PID 33187) main thread run-queue wait | percent | 2 | 3.123 | 2.159 | 4.087 | 2.159 | 0.063062 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_qnorm_and_attn_shift.py (PID 33187) vms_mb | MB | 3 | 398.628 | 367.613 | 431.652 | 367.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_sig_continuations.py (PID 33219) rss_mb | MB | 1 | 460.438 | 460.438 | 460.438 | 460.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_sig_continuations.py (PID 33219) vms_mb | MB | 1 | 764.129 | 764.129 | 764.129 | 764.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_gentle_qk_steering.py (PID 33231) CPU | percent | 2 | 275.786 | 213.697 | 337.875 | 337.875 | 5.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_gentle_qk_steering.py (PID 33231) rss_mb | MB | 3 | 941.203 | 479.672 | 1173.594 | 1173.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_gentle_qk_steering.py (PID 33231) main thread run-queue wait | percent | 2 | 1.721 | 1.026 | 2.416 | 1.026 | 0.034668 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_gentle_qk_steering.py (PID 33231) vms_mb | MB | 3 | 1180.786 | 757.445 | 1394.098 | 1394.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_dr_vocab_safety.py (PID 33245) CPU | percent | 5 | 259.355 | 143.967 | 346.884 | 250.736 | 13.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_dr_vocab_safety.py (PID 33245) rss_mb | MB | 6 | 2648.469 | 1163.184 | 3750.574 | 2172.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_dr_vocab_safety.py (PID 33245) main thread run-queue wait | percent | 5 | 1.046 | 0.010 | 2.186 | 2.186 | 0.052993 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_dr_vocab_safety.py (PID 33245) vms_mb | MB | 6 | 3179.108 | 1355.699 | 4332.281 | 2395.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_assert_vs_pure_prose.py (PID 33262) CPU | percent | 40 | 151.628 | 99.296 | 384.383 | 100.458 | 61.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_assert_vs_pure_prose.py (PID 33262) rss_mb | MB | 41 | 3045.710 | 1.828 | 4093.348 | 4020.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_assert_vs_pure_prose.py (PID 33262) main thread run-queue wait | percent | 40 | 1.994 | 0.002 | 11.143 | 0.003 | 0.805155 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_assert_vs_pure_prose.py (PID 33262) vms_mb | MB | 41 | 3908.853 | 9.512 | 4313.922 | 4313.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_gate_plus_query.py (PID 33298) CPU | percent | 25 | 189.804 | 99.333 | 397.532 | 99.339 | 47.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_gate_plus_query.py (PID 33298) rss_mb | MB | 26 | 2930.190 | 85.281 | 4073.074 | 4027.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_gate_plus_query.py (PID 33298) main thread run-queue wait | percent | 25 | 2.146 | 0.005 | 8.337 | 0.005 | 0.540320 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_gate_plus_query.py (PID 33298) vms_mb | MB | 26 | 3693.274 | 277.672 | 4294.059 | 4294.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — calibrate_r2_conservative.py (PID 33319) CPU | percent | 43 | 165.539 | 99.345 | 367.764 | 100.443 | 71.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — calibrate_r2_conservative.py (PID 33319) rss_mb | MB | 44 | 2821.456 | 5.758 | 3986.723 | 3800.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — calibrate_r2_conservative.py (PID 33319) main thread run-queue wait | percent | 43 | 2.325 | 0.002 | 11.421 | 0.003 | 1.007153 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — calibrate_r2_conservative.py (PID 33319) vms_mb | MB | 44 | 3767.139 | 11.656 | 4353.965 | 4353.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33337) CPU | percent | 43 | 167.048 | 99.414 | 385.643 | 114.360 | 72.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33337) rss_mb | MB | 44 | 2766.427 | 1940.086 | 4073.809 | 4073.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33337) main thread run-queue wait | percent | 43 | 2.016 | 0.002 | 10.803 | 0.006 | 0.873008 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33337) vms_mb | MB | 44 | 3776.135 | 2350.129 | 4294.133 | 4294.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33373) CPU | percent | 39 | 332.330 | 258.888 | 385.625 | 338.683 | 130.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33373) rss_mb | MB | 40 | 2348.061 | 1268.266 | 4118.098 | 2917.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33373) main thread run-queue wait | percent | 39 | 7.681 | 0.019 | 12.300 | 8.516 | 3.022206 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33373) vms_mb | MB | 40 | 2700.881 | 1734.711 | 4340.094 | 4340.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_r1_r3_r4_logits.py (PID 33391) CPU | percent | 119 | 127.143 | 60.660 | 397.348 | 146.057 | 152.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_r1_r3_r4_logits.py (PID 33391) rss_mb | MB | 120 | 2122.917 | 4.848 | 3263.246 | 1367.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_r1_r3_r4_logits.py (PID 33391) main thread run-queue wait | percent | 119 | 0.230 | 0.001 | 9.365 | 0.089 | 0.275540 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_r1_r3_r4_logits.py (PID 33391) vms_mb | MB | 120 | 3186.361 | 11.512 | 3476.754 | 3476.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_r1_r3_r4_logits.py (PID 33429) CPU | percent | 19 | 144.978 | 70.464 | 364.654 | 99.350 | 27.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_r1_r3_r4_logits.py (PID 33429) rss_mb | MB | 20 | 2885.447 | 1100.379 | 4194.277 | 4105.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_r1_r3_r4_logits.py (PID 33429) main thread run-queue wait | percent | 19 | 0.540 | 0.004 | 4.565 | 0.006 | 0.103269 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_r1_r3_r4_logits.py (PID 33429) vms_mb | MB | 20 | 3660.801 | 2219.551 | 4493.559 | 4493.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 33452) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 33452) rss_mb | MB | 4 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 33452) main thread run-queue wait | percent | 3 | 0.001 | 0.000 | 0.002 | 0.000 | 0.000018 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 33452) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33454) rss_mb | MB | 1 | 1359.516 | 1359.516 | 1359.516 | 1359.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33454) vms_mb | MB | 1 | 1734.117 | 1734.117 | 1734.117 | 1734.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 33458) CPU | percent | 2 | 248.828 | 213.431 | 284.224 | 284.224 | 5.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 33458) rss_mb | MB | 3 | 1562.734 | 500.363 | 2098.234 | 2089.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 33458) main thread run-queue wait | percent | 2 | 30.403 | 22.456 | 38.349 | 38.349 | 0.612097 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 33458) vms_mb | MB | 3 | 1831.017 | 764.145 | 2364.453 | 2364.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_edge_cases_25.py (PID 33498) CPU | percent | 13 | 153.812 | 41.746 | 370.254 | 365.194 | 20.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_edge_cases_25.py (PID 33498) rss_mb | MB | 14 | 472.078 | 119.465 | 789.906 | 641.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_edge_cases_25.py (PID 33498) main thread run-queue wait | percent | 13 | 0.817 | 0.062 | 4.410 | 0.715 | 0.107077 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_edge_cases_25.py (PID 33498) vms_mb | MB | 14 | 723.113 | 442.895 | 1030.770 | 855.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 33518) CPU | percent | 51 | 211.651 | 25.803 | 397.620 | 397.380 | 108.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 33518) rss_mb | MB | 52 | 2494.507 | 1761.676 | 2776.715 | 2364.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 33518) main thread run-queue wait | percent | 51 | 0.719 | 0.007 | 8.265 | 0.099 | 0.369073 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 33518) vms_mb | MB | 52 | 2767.145 | 2502.012 | 2990.102 | 2577.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33611) rss_mb | MB | 1 | 7.809 | 7.809 | 7.809 | 7.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33611) vms_mb | MB | 1 | 12.930 | 12.930 | 12.930 | 12.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33626) rss_mb | MB | 1 | 7.129 | 7.129 | 7.129 | 7.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33626) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_heldout.py (PID 33649) CPU | percent | 78 | 196.293 | 42.132 | 398.133 | 99.804 | 154.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_heldout.py (PID 33649) rss_mb | MB | 79 | 5206.447 | 24.660 | 6997.578 | 6857.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_heldout.py (PID 33649) main thread run-queue wait | percent | 78 | 8.511 | 0.002 | 50.957 | 0.008 | 6.715158 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_heldout.py (PID 33649) vms_mb | MB | 79 | 5903.817 | 216.406 | 7262.871 | 7262.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_sig_cont_19.py (PID 33712) CPU | percent | 99 | 116.731 | 13.925 | 181.816 | 100.321 | 116.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_sig_cont_19.py (PID 33712) rss_mb | MB | 100 | 2984.234 | 223.262 | 3965.133 | 3682.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_sig_cont_19.py (PID 33712) main thread run-queue wait | percent | 99 | 0.214 | 0.000 | 1.790 | 0.004 | 0.212876 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_sig_cont_19.py (PID 33712) vms_mb | MB | 100 | 4180.387 | 764.508 | 4311.234 | 4307.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_r2_cont_full.py (PID 33738) CPU | percent | 79 | 117.670 | 30.776 | 319.646 | 70.497 | 93.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_r2_cont_full.py (PID 33738) rss_mb | MB | 80 | 3091.101 | 14.496 | 4858.449 | 4678.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_r2_cont_full.py (PID 33738) main thread run-queue wait | percent | 79 | 0.370 | 0.001 | 3.690 | 0.115 | 0.294246 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_r2_cont_full.py (PID 33738) vms_mb | MB | 80 | 4039.366 | 208.859 | 5259.000 | 5065.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_cont_prose_and_heldout.py (PID 33810) CPU | percent | 20 | 119.990 | 99.322 | 205.678 | 100.308 | 24.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_cont_prose_and_heldout.py (PID 33810) rss_mb | MB | 21 | 2830.412 | 798.051 | 3687.312 | 3673.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_cont_prose_and_heldout.py (PID 33810) main thread run-queue wait | percent | 20 | 0.614 | 0.001 | 3.136 | 0.004 | 0.123436 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_cont_prose_and_heldout.py (PID 33810) vms_mb | MB | 21 | 4149.237 | 1734.594 | 4269.969 | 4269.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_final_adapter.py (PID 33827) CPU | percent | 56 | 206.587 | 18.858 | 397.614 | 397.608 | 116.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_final_adapter.py (PID 33827) rss_mb | MB | 57 | 2460.094 | 358.152 | 2881.062 | 2353.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_final_adapter.py (PID 33827) main thread run-queue wait | percent | 56 | 0.645 | 0.008 | 14.315 | 0.178 | 0.363515 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_final_adapter.py (PID 33827) vms_mb | MB | 57 | 2725.831 | 758.137 | 3127.070 | 2567.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 33858) CPU | percent | 90 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 33858) rss_mb | MB | 91 | 2.359 | 1.324 | 2.727 | 1.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 33858) main thread run-queue wait | percent | 90 | 0.000 | 0.000 | 0.003 | 0.003 | 0.000027 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 33858) vms_mb | MB | 91 | 4.205 | 3.328 | 4.215 | 3.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33859) CPU | percent | 89 | 169.387 | 41.151 | 397.626 | 99.952 | 152.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33859) rss_mb | MB | 90 | 5237.074 | 1134.242 | 7032.719 | 6768.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33859) main thread run-queue wait | percent | 89 | 6.995 | 0.002 | 50.810 | 0.007 | 6.291174 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 33859) vms_mb | MB | 90 | 5822.145 | 1334.660 | 7264.512 | 7264.512 | n/a | n/a |
| docker inspect (PID 33886) rss_mb | MB | 1 | 27.719 | 27.719 | 27.719 | 27.719 | n/a | n/a |
| docker inspect (PID 33886) vms_mb | MB | 1 | 1770.754 | 1770.754 | 1770.754 | 1770.754 | n/a | n/a |
| docker inspect (PID 34019) rss_mb | MB | 1 | 30.305 | 30.305 | 30.305 | 30.305 | n/a | n/a |
| docker inspect (PID 34019) vms_mb | MB | 1 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| docker commit (PID 34036) CPU | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 34036) io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 34036) io write MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 34036) rss_mb | MB | 23 | 30.336 | 30.336 | 30.336 | 30.336 | n/a | n/a |
| docker commit (PID 34036) main thread run-queue wait | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 34036) vms_mb | MB | 23 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 13815 | 17.005 | 0.000 | 398.541 | 0.000 | 2367.820403 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 13815 | 0.834 | 0.000 | 50.381 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 13815 | 0.934 | 0.000 | 51.181 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 13815 | 0.102 | 0.000 | 70.610 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 13815 | 0.111 | 0.000 | 70.666 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 13815 | 0.771 | 0.000 | 216.641 | 0.000 | 10764.203125 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 13815 | 0.000 | 0.000 | 0.586 | 0.000 | 2.429688 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 13816 | 749.961 | 46.430 | 7297.508 | 175.215 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 13815 | 0.033 | 0.000 | 23.428 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 13815 | 0.033 | 0.000 | 23.428 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 13815 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001040 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 13815 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 13838 | 3.141 | 1.274 | 101.868 | 1.981 | 437.854899 CPU seconds | n/a |
| workload total memory | MB | 13839 | 8480.463 | 6766.750 | 13410.586 | 6895.992 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
