# agprof summary

- Duration: **2460.224 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **67 calls**, 67 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1662.625 s total wait
- Tools: **83/83 completed**, 1 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **242140** at 1.97 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2446956.511 / 2446956.511 ms |
| LLM latency p50 / p95 | 15663.973 / 68594.327 ms |
| LLM TTFT p50 / p95 | 8040.414 / 55979.918 ms |
| LLM input / output tokens | 136 / 179044 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 67 total, 67 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1128.059 / 85846.631 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 44/44 | 43 | 1 | 0 | 1432.258 ms | 108550.055 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 433.338 ms | 433.338 ms |
| generate | 2/2 | 2 | 0 | 0 | 820.236 ms | 937.283 ms |
| inspect | 1/1 | 1 | 0 | 0 | 4566.344 ms | 4566.344 ms |
| inspect_module_inputs | 10/10 | 10 | 0 | 0 | 3969.759 ms | 4000.988 ms |
| patch | 15/15 | 15 | 0 | 0 | 422.733 ms | 438.299 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 241.003 ms | 241.003 ms |
| top_activations | 3/3 | 3 | 0 | 0 | 3450.938 ms | 3456.507 ms |
| trace | 6/6 | 6 | 0 | 0 | 1769.558 ms | 2818.629 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.094% | 104.522% | 125.493 s | 6242.688 MB | 7193.125 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| tail | 5891 | sandbox_agent_lsb-native_0000_0000 | 2431 | 0.003% | 0.995% | 0.070 s | 1.555 MB | 1.555 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| docker-init | 5860 | sandbox_agent_lsb-native_0000_0000 | 2431 | 0.002% | 0.995% | 0.060 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python | 5584 |  | 2444 | 3.703% | 102.527% | 91.300 s | 3107.619 MB | 3794.098 MB | 16051.943 MB | 16769.809 MB | 74.796875 MB | 1687.972656 MB |
| bash | 5987 | sandbox_agent_lsb-native_0000_0000 | 2431 | 13.387% | 101.220% | 327.620 s | 102.843 MB | 109.812 MB | 970.190 MB | 973.637 MB | n/a MB | n/a MB |
| python3 | 5993 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.490% | 99.490% | 1.010 s | 51.426 MB | 77.852 MB | 63.391 MB | 92.895 MB | n/a MB | n/a MB |
| lsb_grid_worker | 4281 |  | 2444 | 0.000% | 0.000% | 0.000 s | 3.324 MB | 3.324 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| vllm | 5589 |  | 2444 | 0.097% | 8.926% | 2.380 s | 1784.515 MB | 1784.523 MB | 11043.753 MB | 11044.590 MB | 0.003906 MB | 0.015625 MB |
| python | 5620 |  | 2444 | 0.000% | 0.000% | 0.000 s | 12.371 MB | 12.371 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 5621 |  | 2444 | 1.286% | 37.687% | 31.620 s | 2319.574 MB | 2319.574 MB | 21203.031 MB | 21203.031 MB | 0.000000 MB | 0.015625 MB |
| python3 | 6116 | sandbox_agent_lsb-native_0000_0000 | 2404 | 0.144% | 66.508% | 3.480 s | 73.108 MB | 75.289 MB | 87.356 MB | 89.355 MB | n/a MB | n/a MB |
| python | 6134 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.629 MB | 12.629 MB | 207.078 MB | 207.078 MB | n/a MB | n/a MB |
| bash | 6130 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.020 MB | 3.020 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| pip | 6247 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.527 MB | 17.527 MB | 21.598 MB | 21.598 MB | n/a MB | n/a MB |
| bash | 6243 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.984 MB | 2.984 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| head | 6248 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.469 MB | 1.469 MB | 2.816 MB | 2.816 MB | n/a MB | n/a MB |
| python | 6254 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.848 MB | 13.848 MB | 208.559 MB | 208.559 MB | n/a MB | n/a MB |
| bash | 6299 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.820 MB | 2.820 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6303 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 365.660 MB | 365.660 MB | 2174.645 MB | 2174.645 MB | n/a MB | n/a MB |
| python | 6312 | sandbox_agent_lsb-native_0000_0000 | 2 | 172.594% | 172.594% | 1.740 s | 311.781 MB | 604.926 MB | 1108.328 MB | 2006.816 MB | n/a MB | n/a MB |
| bash | 6310 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.773 MB | 2.773 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 6433 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.074 MB | 3.074 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6434 | sandbox_agent_lsb-native_0000_0000 | 2 | 181.933% | 181.933% | 1.830 s | 313.330 MB | 603.055 MB | 1135.170 MB | 2054.672 MB | n/a MB | n/a MB |
| bash | 6441 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.805 MB | 2.805 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6442 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python | 6451 | sandbox_agent_lsb-native_0000_0000 | 3 | 175.176% | 184.859% | 3.530 s | 780.436 MB | 1477.828 MB | 2234.642 MB | 2636.605 MB | n/a MB | n/a MB |
| bash | 6449 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.637 MB | 2.637 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6521 | sandbox_agent_lsb-native_0000_0000 | 2 | 197.517% | 197.517% | 1.990 s | 737.377 MB | 1175.586 MB | 2477.496 MB | 2791.621 MB | n/a MB | n/a MB |
| bash | 6519 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.887 MB | 2.887 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 6679 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6680 | sandbox_agent_lsb-native_0000_0000 | 4 | 191.560% | 198.879% | 5.780 s | 1209.871 MB | 1778.613 MB | 2676.051 MB | 2965.160 MB | n/a MB | n/a MB |
| python | 6694 | sandbox_agent_lsb-native_0000_0000 | 2 | 143.155% | 143.155% | 1.440 s | 471.445 MB | 935.750 MB | 1316.945 MB | 2622.105 MB | n/a MB | n/a MB |
| bash | 6693 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.867 MB | 2.867 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 6703 | sandbox_agent_lsb-native_0000_0000 | 26 | 0.000% | 0.000% | 0.000 s | 2.922 MB | 2.922 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6704 | sandbox_agent_lsb-native_0000_0000 | 26 | 196.848% | 203.247% | 49.580 s | 283.982 MB | 337.066 MB | 2169.490 MB | 2274.840 MB | n/a MB | n/a MB |
| bash | 6890 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.012 MB | 3.012 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6892 | sandbox_agent_lsb-native_0000_0000 | 2 | 191.755% | 191.755% | 1.930 s | 1224.115 MB | 1522.039 MB | 2743.875 MB | 2904.449 MB | n/a MB | n/a MB |
| bash | 6900 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.051 MB | 3.051 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6901 | sandbox_agent_lsb-native_0000_0000 | 3 | 177.913% | 183.823% | 3.580 s | 939.005 MB | 1164.230 MB | 2605.393 MB | 2783.211 MB | n/a MB | n/a MB |
| python | 7014 | sandbox_agent_lsb-native_0000_0000 | 111 | 90.707% | 181.894% | 100.470 s | 1909.172 MB | 2201.098 MB | 3544.443 MB | 3816.750 MB | n/a MB | n/a MB |
| bash | 7012 | sandbox_agent_lsb-native_0000_0000 | 111 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7094 | sandbox_agent_lsb-native_0000_0000 | 47 | 104.604% | 186.036% | 48.510 s | 1881.995 MB | 2202.184 MB | 3515.087 MB | 3818.742 MB | n/a MB | n/a MB |
| bash | 7092 | sandbox_agent_lsb-native_0000_0000 | 47 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7121 | sandbox_agent_lsb-native_0000_0000 | 14 | 116.089% | 199.714% | 15.220 s | 2214.447 MB | 2803.672 MB | 3400.790 MB | 3934.352 MB | n/a MB | n/a MB |
| bash | 7118 | sandbox_agent_lsb-native_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 2.859 MB | 2.859 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7221 | sandbox_agent_lsb-native_0000_0000 | 124 | 96.877% | 188.198% | 120.030 s | 1590.830 MB | 2225.699 MB | 3210.662 MB | 3840.738 MB | n/a MB | n/a MB |
| bash | 7219 | sandbox_agent_lsb-native_0000_0000 | 119 | 0.000% | 0.000% | 0.000 s | 2.773 MB | 2.773 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7303 | sandbox_agent_lsb-native_0000_0000 | 21 | 129.028% | 200.955% | 26.020 s | 2020.584 MB | 2378.676 MB | 3646.034 MB | 3988.234 MB | n/a MB | n/a MB |
| sleep | 7311 | sandbox_agent_lsb-native_0000_0000 | 90 | 0.000% | 0.000% | 0.000 s | 1.465 MB | 1.465 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| bash | 7310 | sandbox_agent_lsb-native_0000_0000 | 90 | 0.000% | 0.000% | 0.000 s | 2.887 MB | 2.887 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7387 | sandbox_agent_lsb-native_0000_0000 | 9 | 192.699% | 201.210% | 15.540 s | 974.313 MB | 1241.355 MB | 2456.142 MB | 2850.234 MB | n/a MB | n/a MB |
| python | 7417 | sandbox_agent_lsb-native_0000_0000 | 2 | 185.496% | 185.496% | 1.870 s | 987.467 MB | 1207.684 MB | 2665.848 MB | 2822.848 MB | n/a MB | n/a MB |
| bash | 7416 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.898 MB | 2.898 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7505 | sandbox_agent_lsb-native_0000_0000 | 4 | 184.440% | 197.694% | 5.570 s | 185.432 MB | 243.562 MB | 1648.156 MB | 2129.801 MB | n/a MB | n/a MB |
| bash | 7503 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.855 MB | 2.855 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7516 | sandbox_agent_lsb-native_0000_0000 | 4 | 183.807% | 196.825% | 5.550 s | 1049.373 MB | 1718.953 MB | 2220.482 MB | 2982.559 MB | n/a MB | n/a MB |
| bash | 7515 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.832 MB | 2.832 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 7527 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.703 MB | 2.703 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7529 | sandbox_agent_lsb-native_0000_0000 | 3 | 184.773% | 188.913% | 3.720 s | 339.116 MB | 525.336 MB | 2177.682 MB | 2331.590 MB | n/a MB | n/a MB |
| python | 7657 | sandbox_agent_lsb-native_0000_0000 | 9 | 184.067% | 192.812% | 14.840 s | 338.838 MB | 417.277 MB | 2224.130 MB | 2299.121 MB | n/a MB | n/a MB |
| sleep | 7658 | sandbox_agent_lsb-native_0000_0000 | 99 | 0.000% | 0.000% | 0.000 s | 1.461 MB | 1.461 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| bash | 7654 | sandbox_agent_lsb-native_0000_0000 | 99 | 0.000% | 0.000% | 0.000 s | 3.000 MB | 3.000 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 7670 | sandbox_agent_lsb-native_0000_0000 | 109 | 0.000% | 0.000% | 0.000 s | 3.043 MB | 3.043 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 7673 | sandbox_agent_lsb-native_0000_0000 | 109 | 0.000% | 0.000% | 0.000 s | 1.555 MB | 1.555 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| python | 7672 | sandbox_agent_lsb-native_0000_0000 | 17 | 194.305% | 202.382% | 31.320 s | 605.958 MB | 851.660 MB | 2461.049 MB | 2658.078 MB | n/a MB | n/a MB |
| bash | 7714 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.836 MB | 2.836 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7715 | sandbox_agent_lsb-native_0000_0000 | 4 | 190.498% | 196.738% | 5.770 s | 1137.473 MB | 1831.535 MB | 2640.852 MB | 3006.250 MB | n/a MB | n/a MB |
| docker | 7769 |  | 23 | 0.000% | 0.000% | 0.000 s | 30.418 MB | 30.418 MB | 1907.340 MB | 1907.340 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.032% | 51.000% | 19951.007 MB | 20219.188 MB | 30.354 W | 59.640 W | 74631.219 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 34.018% | 212.018% | 832.683 s | 462.315 MB | 2444.344 MB | 31.023438 MB | 170.476562 MB | 0.001007 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 5747 | 2460.160 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2446.957 | n/a | n/a | 31.023 | 2446956.511 | 2446956.511 | 2446956.511 |
| engine:execute | 1/1 | 0 | 0 | 2446.955 | 2.766 | 2444.174 | 31.023 | 2446954.850 | 2446954.850 | 2446954.850 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2419.713 | 0.002 | 2419.711 | 31.023 | 2419713.111 | 2419713.111 | 2419713.111 |
| turn | 67/67 | 0 | 0 | 2416.702 | n/a | n/a | 30.807 | 36070.173 | 19746.197 | 114816.678 |
| llm:attempt | 67/67 | 0 | 0 | 1662.625 | 3.047 | 1659.576 | 15.623 | 24815.304 | 15663.973 | 68594.327 |
| tool:bash | 44/44 | 1 | 0 | 674.763 | n/a | n/a | 13.877 | 15335.519 | 1432.258 | 108550.055 |
| process:bash | 44/44 | 1 | 0 | 674.325 | n/a | n/a | 13.726 | 15325.577 | 1422.988 | 108539.705 |
| tool:inspect_module_inputs | 10/10 | 0 | 0 | 38.493 | n/a | n/a | 0.134 | 3849.270 | 3969.759 | 4000.988 |
| run:container_call | 13/13 | 0 | 0 | 23.853 | 0.002 | 23.851 | 0.000 | 1834.863 | 41.613 | 9371.108 |
| teardown:commit | 1/1 | 0 | 0 | 23.430 | 0.004 | 23.426 | 0.000 | 23430.292 | 23430.292 | 23430.292 |
| sandbox:commit | 1/1 | 0 | 0 | 23.129 | 0.002 | 23.127 | 0.000 | 23129.205 | 23129.205 | 23129.205 |
| checkpoint.total | 1/1 | 0 | 0 | 23.129 | 0.002 | 23.127 | 0.000 | 23129.074 | 23129.074 | 23129.074 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 23.129 | 0.002 | 23.127 | 0.000 | 23128.939 | 23128.939 | 23128.939 |
| tool:top_activations | 3/3 | 0 | 0 | 10.356 | n/a | n/a | 0.000 | 3452.084 | 3450.938 | 3456.507 |
| tool:trace | 6/6 | 0 | 0 | 10.353 | n/a | n/a | 0.000 | 1725.463 | 1769.558 | 2818.629 |
| tool:patch | 15/15 | 0 | 0 | 6.372 | n/a | n/a | 0.000 | 424.780 | 422.733 | 438.299 |
| tool:inspect | 1/1 | 0 | 0 | 4.566 | n/a | n/a | 0.000 | 4566.344 | 4566.344 | 4566.344 |
| syscall:sendto | 1787/1787 | 0 | 0 | 4.245 | n/a | n/a | 0.564 | 2.376 | 2.061 | 4.526 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.178 | 0.786 | 2.391 | 0.000 | 3177.932 | 3177.932 | 3177.932 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.178 | 0.786 | 2.391 | 0.000 | 3177.645 | 3177.645 | 3177.645 |
| tool:generate | 2/2 | 0 | 0 | 1.640 | n/a | n/a | 0.000 | 820.236 | 820.236 | 937.283 |
| syscall:connect | 483/483 | 0 | 0 | 1.157 | n/a | n/a | 0.228 | 2.396 | 2.014 | 4.653 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.433 | n/a | n/a | 0.000 | 433.338 | 433.338 | 433.338 |
| sandbox:start | 1/1 | 0 | 0 | 0.355 | 0.002 | 0.352 | 0.000 | 354.535 | 354.535 | 354.535 |
| runtime.container_create | 1/1 | 0 | 0 | 0.354 | 0.002 | 0.352 | 0.000 | 354.399 | 354.399 | 354.399 |
| syscall:execve | 179/179 | 0 | 0 | 0.343 | n/a | n/a | 0.136 | 1.918 | 1.206 | 2.883 |
| sandbox:create | 1/1 | 0 | 0 | 0.340 | 0.248 | 0.092 | 0.000 | 340.009 | 340.009 | 340.009 |
| sandbox:stop | 1/1 | 0 | 0 | 0.301 | 0.002 | 0.299 | 0.000 | 300.841 | 300.841 | 300.841 |
| tool:submit_output | 1/1 | 0 | 0 | 0.241 | n/a | n/a | 0.000 | 241.003 | 241.003 | 241.003 |
| agency:services_close | 1/1 | 0 | 0 | 0.134 | 0.001 | 0.133 | 0.000 | 133.670 | 133.670 | 133.670 |
| agency:services_start | 1/1 | 0 | 0 | 0.071 | 0.040 | 0.031 | 0.000 | 71.256 | 71.256 | 71.256 |
| run:detect | 1/1 | 0 | 0 | 0.052 | 0.001 | 0.051 | 0.000 | 52.055 | 52.055 | 52.055 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.009 | 0.040 | 0.000 | 48.286 | 48.286 | 48.286 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 2.246 | 2.246 | 2.246 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.265 | 1.265 | 1.265 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.076 | 0.083 | 0.108 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.191 | 0.191 | 0.191 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.084 | 0.084 | 0.084 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2443 | 0.415 | 0.039 | 50.533 | 0.053 | 10.209928 CPU seconds | n/a |
| GPU 0 memory | MB | 2444 | 19951.007 | 19745.188 | 20219.188 | 19917.188 | n/a | n/a |
| GPU 0 power | W | 2444 | 30.354 | 29.573 | 59.640 | 29.736 | n/a | 74631.219 J |
| GPU 0 proc / 3282-652224 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc memory | MB | 2444 | 8070.000 | 8070.000 | 8070.000 | 8070.000 | n/a | n/a |
| GPU 0 proc / 5584-967832 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc memory | MB | 2444 | 3256.599 | 3118.000 | 3524.000 | 3222.000 | n/a | n/a |
| GPU 0 proc / 5584-967832 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc estimated power | W | 2251 | 1.572 | 0.000 | 58.476 | 0.000 | n/a | n/a |
| GPU 0 proc / 5584-967832 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc utilization | percent | 2251 | 1.106 | 0.000 | 47.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 5621-969630 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc memory | MB | 2444 | 8137.221 | 8070.000 | 8138.000 | 8138.000 | n/a | n/a |
| GPU 0 proc / 5621-969630 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc estimated power | W | 150 | 0.522 | 0.000 | 56.325 | 0.000 | n/a | n/a |
| GPU 0 proc / 5621-969630 / sandbox / ~ / device / GPU-f02dbcf7-082b-2b06-d4b4-1f1c82e3c9fc utilization | percent | 150 | 0.560 | 0.000 | 59.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2444 | 19463.820 | 19258.000 | 19732.000 | 19430.000 | n/a | n/a |
| GPU 0 utilization | percent | 2444 | 1.032 | 0.000 | 51.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2444 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2443 | 3.727 | 0.034 | 54.774 | 0.419 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2443 | 9.987 | 0.253 | 53.846 | 0.503 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2443 | 0.745 | 0.000 | 224.758 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2443 | 0.777 | 0.000 | 187.750 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2443 | 0.342 | 0.000 | 38.184 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2443 | 0.362 | 0.000 | 38.489 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 2444 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 2444 | 9184.451 | 8209.957 | 11230.758 | 9186.895 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2443 | 0.002 | 0.000 | 0.967 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2443 | 0.002 | 0.000 | 0.968 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2443 | 0.001 | 0.000 | 0.032 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2443 | 0.013 | 0.000 | 0.890 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4281) CPU | percent | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4281) io read MB/s | MB/s | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4281) io write MB/s | MB/s | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4281) rss_mb | MB | 2444 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4281) main thread run-queue wait | percent | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4281) vms_mb | MB | 2444 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 5584) CPU | percent | 2443 | 3.703 | 0.000 | 102.527 | 0.000 | 91.300000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 5584) io read MB/s | MB/s | 2443 | 0.030 | 0.000 | 67.621 | 0.000 | 74.796875 MB | n/a |
| Agency harness — python -m lsbench (PID 5584) io write MB/s | MB/s | 2443 | 0.685 | 0.015 | 193.077 | 0.023 | 1687.972656 MB | n/a |
| Agency harness — python -m lsbench (PID 5584) rss_mb | MB | 2444 | 3107.619 | 2319.484 | 3794.098 | 3438.941 | n/a | n/a |
| Agency harness — python -m lsbench (PID 5584) main thread run-queue wait | percent | 2443 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000066 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 5584) vms_mb | MB | 2444 | 16051.943 | 13795.883 | 16769.809 | 16281.035 | n/a | n/a |
| Python — vllm (PID 5589) CPU | percent | 2443 | 0.097 | 0.000 | 8.926 | 0.000 | 2.380000 CPU seconds | n/a |
| Python — vllm (PID 5589) io read MB/s | MB/s | 2443 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 5589) io write MB/s | MB/s | 2443 | 0.000 | 0.000 | 0.008 | 0.000 | 0.015625 MB | n/a |
| Python — vllm (PID 5589) rss_mb | MB | 2444 | 1784.515 | 1783.773 | 1784.523 | 1784.523 | n/a | n/a |
| Python — vllm (PID 5589) main thread run-queue wait | percent | 2443 | 0.003 | 0.000 | 0.444 | 0.001 | 0.063659 run-queue seconds | n/a |
| Python — vllm (PID 5589) vms_mb | MB | 2444 | 11043.753 | 10971.570 | 11044.590 | 11044.590 | n/a | n/a |
| Python — python -c (PID 5620) CPU | percent | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 5620) io read MB/s | MB/s | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 5620) io write MB/s | MB/s | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 5620) rss_mb | MB | 2444 | 12.371 | 12.371 | 12.371 | 12.371 | n/a | n/a |
| Python — python -c (PID 5620) main thread run-queue wait | percent | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 5620) vms_mb | MB | 2444 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 5621) CPU | percent | 2443 | 1.286 | 0.000 | 37.687 | 1.990 | 31.620000 CPU seconds | n/a |
| VLLM::EngineCore (PID 5621) io read MB/s | MB/s | 2443 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 5621) io write MB/s | MB/s | 2443 | 0.000 | 0.000 | 0.004 | 0.000 | 0.015625 MB | n/a |
| VLLM::EngineCore (PID 5621) rss_mb | MB | 2444 | 2319.574 | 2319.574 | 2319.574 | 2319.574 | n/a | n/a |
| VLLM::EngineCore (PID 5621) main thread run-queue wait | percent | 2443 | 0.000 | 0.000 | 0.019 | 0.000 | 0.000253 run-queue seconds | n/a |
| VLLM::EngineCore (PID 5621) vms_mb | MB | 2444 | 21203.031 | 21203.031 | 21203.031 | 21203.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 5860) CPU | percent | 2430 | 0.002 | 0.000 | 0.995 | 0.000 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 5860) rss_mb | MB | 2431 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 5860) main thread run-queue wait | percent | 2430 | 0.008 | 0.000 | 5.135 | 0.000 | 0.187368 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 5860) vms_mb | MB | 2431 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 5891) CPU | percent | 2430 | 0.003 | 0.000 | 0.995 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 5891) rss_mb | MB | 2431 | 1.555 | 1.555 | 1.555 | 1.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 5891) main thread run-queue wait | percent | 2430 | 0.010 | 0.000 | 5.229 | 0.000 | 0.240602 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 5891) vms_mb | MB | 2431 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5987) CPU | percent | 2430 | 13.387 | 0.000 | 101.220 | 0.000 | 327.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5987) rss_mb | MB | 2431 | 102.843 | 3.109 | 109.812 | 109.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5987) main thread run-queue wait | percent | 2430 | 0.000 | 0.000 | 0.007 | 0.000 | 0.000134 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5987) vms_mb | MB | 2431 | 970.190 | 4.258 | 973.637 | 973.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5993) CPU | percent | 1 | 99.490 | 99.490 | 99.490 | 99.490 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5993) rss_mb | MB | 2 | 51.426 | 25.000 | 77.852 | 77.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5993) main thread run-queue wait | percent | 1 | 0.002 | 0.002 | 0.002 | 0.002 | 0.000016 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5993) vms_mb | MB | 2 | 63.391 | 33.887 | 92.895 | 92.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 6116) CPU | percent | 2403 | 0.144 | 0.000 | 66.508 | 0.000 | 3.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 6116) rss_mb | MB | 2404 | 73.108 | 29.164 | 75.289 | 74.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 6116) main thread run-queue wait | percent | 2403 | 0.014 | 0.000 | 8.783 | 0.000 | 0.342536 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 6116) vms_mb | MB | 2404 | 87.356 | 35.758 | 89.355 | 88.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6130) rss_mb | MB | 1 | 3.020 | 3.020 | 3.020 | 3.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6130) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6134) rss_mb | MB | 1 | 12.629 | 12.629 | 12.629 | 12.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6134) vms_mb | MB | 1 | 207.078 | 207.078 | 207.078 | 207.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6243) rss_mb | MB | 1 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6243) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — pip (PID 6247) rss_mb | MB | 1 | 17.527 | 17.527 | 17.527 | 17.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — pip (PID 6247) vms_mb | MB | 1 | 21.598 | 21.598 | 21.598 | 21.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — head (PID 6248) rss_mb | MB | 1 | 1.469 | 1.469 | 1.469 | 1.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — head (PID 6248) vms_mb | MB | 1 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6254) rss_mb | MB | 1 | 13.848 | 13.848 | 13.848 | 13.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6254) vms_mb | MB | 1 | 208.559 | 208.559 | 208.559 | 208.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6299) rss_mb | MB | 1 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6299) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6303) rss_mb | MB | 1 | 365.660 | 365.660 | 365.660 | 365.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6303) vms_mb | MB | 1 | 2174.645 | 2174.645 | 2174.645 | 2174.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6310) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6310) rss_mb | MB | 2 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6310) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6310) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6312) CPU | percent | 1 | 172.594 | 172.594 | 172.594 | 172.594 | 1.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6312) rss_mb | MB | 2 | 311.781 | 18.637 | 604.926 | 604.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6312) main thread run-queue wait | percent | 1 | 32.330 | 32.330 | 32.330 | 32.330 | 0.325929 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6312) vms_mb | MB | 2 | 1108.328 | 209.840 | 2006.816 | 2006.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6433) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6433) rss_mb | MB | 2 | 3.074 | 3.074 | 3.074 | 3.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6433) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6433) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6434) CPU | percent | 1 | 181.933 | 181.933 | 181.933 | 181.933 | 1.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6434) rss_mb | MB | 2 | 313.330 | 23.605 | 603.055 | 603.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6434) main thread run-queue wait | percent | 1 | 41.404 | 41.404 | 41.404 | 41.404 | 0.416464 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6434) vms_mb | MB | 2 | 1135.170 | 215.668 | 2054.672 | 2054.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6441) rss_mb | MB | 1 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6441) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6442) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6442) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6449) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6449) rss_mb | MB | 3 | 2.637 | 2.637 | 2.637 | 2.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6449) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6449) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6451) CPU | percent | 2 | 175.176 | 165.493 | 184.859 | 165.493 | 3.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6451) rss_mb | MB | 3 | 780.436 | 60.426 | 1477.828 | 1477.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6451) main thread run-queue wait | percent | 2 | 55.838 | 48.453 | 63.222 | 63.222 | 1.125501 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6451) vms_mb | MB | 3 | 2234.642 | 1918.398 | 2636.605 | 2636.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6519) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6519) rss_mb | MB | 2 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6519) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6519) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6521) CPU | percent | 1 | 197.517 | 197.517 | 197.517 | 197.517 | 1.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6521) rss_mb | MB | 2 | 737.377 | 299.168 | 1175.586 | 1175.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6521) main thread run-queue wait | percent | 1 | 47.667 | 47.667 | 47.667 | 47.667 | 0.480244 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6521) vms_mb | MB | 2 | 2477.496 | 2163.371 | 2791.621 | 2791.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6679) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6679) rss_mb | MB | 4 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6679) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6679) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6680) CPU | percent | 3 | 191.560 | 178.912 | 198.879 | 196.890 | 5.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6680) rss_mb | MB | 4 | 1209.871 | 47.727 | 1778.613 | 1778.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6680) main thread run-queue wait | percent | 3 | 45.551 | 36.991 | 50.104 | 50.104 | 1.374387 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6680) vms_mb | MB | 4 | 2676.051 | 1905.797 | 2965.160 | 2909.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6693) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6693) rss_mb | MB | 2 | 2.867 | 2.867 | 2.867 | 2.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6693) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6693) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6694) CPU | percent | 1 | 143.155 | 143.155 | 143.155 | 143.155 | 1.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6694) rss_mb | MB | 2 | 471.445 | 7.141 | 935.750 | 935.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6694) main thread run-queue wait | percent | 1 | 21.956 | 21.956 | 21.956 | 21.956 | 0.220852 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6694) vms_mb | MB | 2 | 1316.945 | 11.785 | 2622.105 | 2622.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6703) CPU | percent | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6703) rss_mb | MB | 26 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6703) main thread run-queue wait | percent | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6703) vms_mb | MB | 26 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6704) CPU | percent | 25 | 196.848 | 131.110 | 203.247 | 197.885 | 49.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6704) rss_mb | MB | 26 | 283.982 | 13.473 | 337.066 | 323.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6704) main thread run-queue wait | percent | 25 | 48.961 | 21.310 | 54.486 | 50.243 | 12.331727 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6704) vms_mb | MB | 26 | 2169.490 | 207.336 | 2274.840 | 2206.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6890) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6890) rss_mb | MB | 2 | 3.012 | 3.012 | 3.012 | 3.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6890) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6890) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6892) CPU | percent | 1 | 191.755 | 191.755 | 191.755 | 191.755 | 1.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6892) rss_mb | MB | 2 | 1224.115 | 926.191 | 1522.039 | 1522.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6892) main thread run-queue wait | percent | 1 | 51.305 | 51.305 | 51.305 | 51.305 | 0.516384 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6892) vms_mb | MB | 2 | 2743.875 | 2583.301 | 2904.449 | 2904.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6900) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6900) rss_mb | MB | 3 | 3.051 | 3.051 | 3.051 | 3.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6900) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6900) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6901) CPU | percent | 2 | 177.913 | 172.003 | 183.823 | 172.003 | 3.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6901) rss_mb | MB | 3 | 939.005 | 566.719 | 1164.230 | 1164.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6901) main thread run-queue wait | percent | 2 | 51.991 | 51.643 | 52.339 | 51.643 | 1.046172 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6901) vms_mb | MB | 3 | 2605.393 | 2331.484 | 2783.211 | 2783.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7012) CPU | percent | 110 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7012) rss_mb | MB | 111 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7012) main thread run-queue wait | percent | 110 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7012) vms_mb | MB | 111 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7014) CPU | percent | 110 | 90.707 | 67.631 | 181.894 | 87.351 | 100.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7014) rss_mb | MB | 111 | 1909.172 | 40.637 | 2201.098 | 1418.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7014) main thread run-queue wait | percent | 110 | 8.474 | 0.084 | 47.143 | 13.393 | 9.386537 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7014) vms_mb | MB | 111 | 3544.443 | 1901.234 | 3816.750 | 3813.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7092) CPU | percent | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7092) rss_mb | MB | 47 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7092) main thread run-queue wait | percent | 46 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7092) vms_mb | MB | 47 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7094) CPU | percent | 46 | 104.604 | 69.625 | 186.036 | 111.117 | 48.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7094) rss_mb | MB | 47 | 1881.995 | 94.965 | 2202.184 | 1764.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7094) main thread run-queue wait | percent | 46 | 13.247 | 0.554 | 46.425 | 8.194 | 6.146575 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7094) vms_mb | MB | 47 | 3515.087 | 1952.711 | 3818.742 | 3818.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7118) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7118) rss_mb | MB | 14 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7118) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7118) vms_mb | MB | 14 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7121) CPU | percent | 13 | 116.089 | 82.433 | 199.714 | 88.319 | 15.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7121) rss_mb | MB | 14 | 2214.447 | 526.672 | 2803.672 | 2563.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7121) main thread run-queue wait | percent | 13 | 21.787 | 4.481 | 56.388 | 11.347 | 2.856168 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7121) vms_mb | MB | 14 | 3400.790 | 2303.547 | 3934.352 | 3696.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7219) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7219) rss_mb | MB | 119 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7219) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7219) vms_mb | MB | 119 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7221) CPU | percent | 123 | 96.877 | 74.497 | 188.198 | 76.463 | 120.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7221) rss_mb | MB | 124 | 1590.830 | 86.328 | 2225.699 | 2163.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7221) main thread run-queue wait | percent | 123 | 8.190 | 0.046 | 48.752 | 0.084 | 10.147804 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7221) vms_mb | MB | 124 | 3210.662 | 1943.223 | 3840.738 | 3777.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loco.py (PID 7303) CPU | percent | 20 | 129.028 | 63.480 | 200.955 | 197.847 | 26.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loco.py (PID 7303) rss_mb | MB | 21 | 2020.584 | 86.625 | 2378.676 | 2378.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loco.py (PID 7303) main thread run-queue wait | percent | 20 | 24.868 | 0.089 | 51.993 | 51.504 | 5.016319 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loco.py (PID 7303) vms_mb | MB | 21 | 3646.034 | 1943.195 | 3988.234 | 3988.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7310) CPU | percent | 89 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7310) rss_mb | MB | 90 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7310) main thread run-queue wait | percent | 89 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7310) vms_mb | MB | 90 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7311) CPU | percent | 89 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7311) rss_mb | MB | 90 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7311) main thread run-queue wait | percent | 89 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7311) vms_mb | MB | 90 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — est.py (PID 7387) CPU | percent | 8 | 192.699 | 168.646 | 201.210 | 198.812 | 15.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — est.py (PID 7387) rss_mb | MB | 9 | 974.313 | 21.789 | 1241.355 | 1225.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — est.py (PID 7387) main thread run-queue wait | percent | 8 | 47.876 | 30.009 | 57.681 | 49.813 | 3.860822 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — est.py (PID 7387) vms_mb | MB | 9 | 2456.142 | 213.922 | 2850.234 | 2834.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7416) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7416) rss_mb | MB | 2 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7416) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7416) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7417) CPU | percent | 1 | 185.496 | 185.496 | 185.496 | 185.496 | 1.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7417) rss_mb | MB | 2 | 987.467 | 767.250 | 1207.684 | 1207.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7417) main thread run-queue wait | percent | 1 | 51.021 | 51.021 | 51.021 | 51.021 | 0.514346 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7417) vms_mb | MB | 2 | 2665.848 | 2508.848 | 2822.848 | 2822.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7503) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7503) rss_mb | MB | 4 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7503) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7503) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7505) CPU | percent | 3 | 184.440 | 160.704 | 197.694 | 194.922 | 5.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7505) rss_mb | MB | 4 | 185.432 | 18.375 | 243.562 | 243.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7505) main thread run-queue wait | percent | 3 | 47.058 | 34.512 | 53.689 | 53.689 | 1.420983 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7505) vms_mb | MB | 4 | 1648.156 | 211.070 | 2129.801 | 2129.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7515) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7515) rss_mb | MB | 4 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7515) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7515) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7516) CPU | percent | 3 | 183.807 | 163.637 | 196.825 | 196.825 | 5.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7516) rss_mb | MB | 4 | 1049.373 | 19.785 | 1718.953 | 1718.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7516) main thread run-queue wait | percent | 3 | 46.606 | 30.876 | 56.063 | 52.878 | 1.406956 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7516) vms_mb | MB | 4 | 2220.482 | 211.766 | 2982.559 | 2982.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7527) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7527) rss_mb | MB | 3 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7527) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7527) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make.py (PID 7529) CPU | percent | 2 | 184.773 | 180.633 | 188.913 | 188.913 | 3.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make.py (PID 7529) rss_mb | MB | 3 | 339.116 | 79.262 | 525.336 | 525.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make.py (PID 7529) main thread run-queue wait | percent | 2 | 51.816 | 45.485 | 58.148 | 58.148 | 1.043117 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make.py (PID 7529) vms_mb | MB | 3 | 2177.682 | 1937.160 | 2331.590 | 2331.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7654) CPU | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7654) rss_mb | MB | 99 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7654) main thread run-queue wait | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7654) vms_mb | MB | 99 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val2.py (PID 7657) CPU | percent | 8 | 184.067 | 177.203 | 192.812 | 177.203 | 14.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val2.py (PID 7657) rss_mb | MB | 9 | 338.838 | 269.188 | 417.277 | 360.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val2.py (PID 7657) main thread run-queue wait | percent | 8 | 53.349 | 49.535 | 57.556 | 56.553 | 4.301537 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val2.py (PID 7657) vms_mb | MB | 9 | 2224.130 | 2150.973 | 2299.121 | 2243.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7658) CPU | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7658) rss_mb | MB | 99 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7658) main thread run-queue wait | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7658) vms_mb | MB | 99 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7670) CPU | percent | 108 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7670) rss_mb | MB | 109 | 3.043 | 3.043 | 3.043 | 3.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7670) main thread run-queue wait | percent | 108 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7670) vms_mb | MB | 109 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make2.py (PID 7672) CPU | percent | 16 | 194.305 | 186.720 | 202.382 | 202.382 | 31.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make2.py (PID 7672) rss_mb | MB | 17 | 605.958 | 339.617 | 851.660 | 851.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make2.py (PID 7672) main thread run-queue wait | percent | 16 | 46.587 | 38.447 | 51.742 | 44.638 | 7.509286 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make2.py (PID 7672) vms_mb | MB | 17 | 2461.049 | 2202.520 | 2658.078 | 2658.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7673) CPU | percent | 108 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7673) rss_mb | MB | 109 | 1.555 | 1.555 | 1.555 | 1.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7673) main thread run-queue wait | percent | 108 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 7673) vms_mb | MB | 109 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7714) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7714) rss_mb | MB | 4 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7714) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7714) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7715) CPU | percent | 3 | 190.498 | 181.468 | 196.738 | 193.288 | 5.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7715) rss_mb | MB | 4 | 1137.473 | 78.062 | 1831.535 | 1831.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7715) main thread run-queue wait | percent | 3 | 46.621 | 43.189 | 50.623 | 50.623 | 1.412044 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7715) vms_mb | MB | 4 | 2640.852 | 1936.035 | 3006.250 | 3006.250 | n/a | n/a |
| docker commit (PID 7769) CPU | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 7769) io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 7769) io write MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 7769) rss_mb | MB | 23 | 30.418 | 30.418 | 30.418 | 30.418 | n/a | n/a |
| docker commit (PID 7769) main thread run-queue wait | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 7769) vms_mb | MB | 23 | 1907.340 | 1907.340 | 1907.340 | 1907.340 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 2430 | 34.018 | 0.000 | 212.018 | 0.000 | 832.683219 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2430 | 3.135 | 0.000 | 50.315 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2430 | 3.380 | 0.000 | 54.120 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 2430 | 0.005 | 0.000 | 2.462 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 2430 | 0.005 | 0.000 | 2.715 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 2430 | 0.013 | 0.000 | 6.373 | 0.000 | 31.023438 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 2430 | 0.070 | 0.000 | 107.278 | 0.000 | 170.476562 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 2431 | 462.315 | 15.668 | 2444.344 | 297.746 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2430 | 0.000 | 0.000 | 0.008 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2430 | 0.000 | 0.000 | 0.008 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 2430 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001007 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 2430 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 2443 | 5.094 | 1.532 | 104.522 | 2.039 | 125.493113 CPU seconds | n/a |
| workload total memory | MB | 2444 | 6242.688 | 5073.398 | 7193.125 | 7106.027 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
