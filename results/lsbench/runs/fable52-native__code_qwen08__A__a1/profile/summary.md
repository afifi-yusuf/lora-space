# agprof summary

- Duration: **2820.378 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **94 calls**, 94 succeeded, 0 failed, 0 interrupted, n/a reported retries, 2286.044 s total wait
- Tools: **119/119 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **262181** at 1.976 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2795971.068 / 2795971.068 ms |
| LLM latency p50 / p95 | 21015.525 / 55801.447 ms |
| LLM TTFT p50 / p95 | 10420.686 / 47566.183 ms |
| LLM input / output tokens | 190 / 239787 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 94 total, 94 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 442.220 / 15909.307 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 2/2 | 2 | 0 | 0 | 327.366 ms | 353.696 ms |
| attribution | 2/2 | 2 | 0 | 0 | 331.682 ms | 337.970 ms |
| bash | 61/61 | 61 | 0 | 0 | 1139.700 ms | 19307.759 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 354.036 ms | 354.036 ms |
| generate | 8/8 | 8 | 0 | 0 | 8007.663 ms | 12900.981 ms |
| get_current_resources | 1/1 | 1 | 0 | 0 | 241.659 ms | 241.659 ms |
| inspect | 8/8 | 8 | 0 | 0 | 2036.138 ms | 2156.216 ms |
| patch | 23/23 | 23 | 0 | 0 | 419.964 ms | 439.582 ms |
| submit_output | 2/2 | 2 | 0 | 0 | 236.849 ms | 240.178 ms |
| token_stats | 2/2 | 2 | 0 | 0 | 6794.347 ms | 10905.930 ms |
| trace | 9/9 | 9 | 0 | 0 | 5872.522 ms | 10877.141 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 6.253% | 167.592% | 176.764 s | 6759.627 MB | 9439.930 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 5817 |  | 2803 | 0.182% | 5.963% | 5.150 s | 1791.253 MB | 1803.961 MB | 11044.736 MB | 11046.586 MB | 0.007812 MB | 0.046875 MB |
| python | 5851 |  | 2803 | 0.000% | 0.000% | 0.000 s | 12.080 MB | 12.176 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python | 5812 |  | 2803 | 3.772% | 167.121% | 106.730 s | 3262.818 MB | 5512.055 MB | 16423.455 MB | 19367.773 MB | 75.917969 MB | 7283.367188 MB |
| docker-init | 6070 | sandbox_agent_lsb-native_0000_0000 | 2779 | 0.002% | 0.995% | 0.060 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 6199 | sandbox_agent_lsb-native_0000_0000 | 2 | 100.900% | 100.900% | 1.020 s | 53.820 MB | 81.352 MB | 65.947 MB | 96.676 MB | n/a MB | n/a MB |
| lsb_grid_worker | 4980 |  | 2803 | 0.000% | 0.000% | 0.000 s | 3.344 MB | 3.344 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 6193 | sandbox_agent_lsb-native_0000_0000 | 2779 | 4.297% | 100.469% | 120.190 s | 102.503 MB | 107.500 MB | 970.866 MB | 973.961 MB | n/a MB | n/a MB |
| tail | 6102 | sandbox_agent_lsb-native_0000_0000 | 2779 | 0.002% | 0.995% | 0.060 s | 1.477 MB | 1.477 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 5852 |  | 2803 | 2.293% | 57.334% | 64.710 s | 2311.270 MB | 2324.484 MB | 21267.672 MB | 21268.094 MB | 0.003906 MB | 0.015625 MB |
| python3 | 6211 | sandbox_agent_lsb-native_0000_0000 | 2752 | 0.169% | 61.601% | 4.670 s | 73.404 MB | 76.691 MB | 88.290 MB | 92.867 MB | n/a MB | n/a MB |
| python | 6229 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.000 MB | 13.000 MB | 207.148 MB | 207.148 MB | n/a MB | n/a MB |
| bash | 6224 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.973 MB | 2.973 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6303 | sandbox_agent_lsb-native_0000_0000 | 3 | 3.474% | 3.970% | 0.070 s | 12.469 MB | 12.469 MB | 15.883 MB | 15.883 MB | n/a MB | n/a MB |
| python | 6320 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.129 MB | 0.129 MB | 6.734 MB | 6.734 MB | n/a MB | n/a MB |
| python | 6361 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.406 MB | 7.406 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python | 6403 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.469 MB | 12.469 MB | 15.883 MB | 15.883 MB | n/a MB | n/a MB |
| python | 6526 | sandbox_agent_lsb-native_0000_0000 | 3 | 3.974% | 3.978% | 0.080 s | 12.919 MB | 13.086 MB | 17.029 MB | 17.062 MB | n/a MB | n/a MB |
| python | 6539 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.898 MB | 7.898 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python | 6581 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.672 MB | 7.672 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 6621 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python | 6675 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.730 MB | 12.730 MB | 17.047 MB | 17.047 MB | n/a MB | n/a MB |
| bash | 6673 | sandbox_agent_lsb-native_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 2.871 MB | 2.871 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6674 | sandbox_agent_lsb-native_0000_0000 | 13 | 0.741% | 4.911% | 0.090 s | 13.077 MB | 13.105 MB | 17.058 MB | 17.059 MB | n/a MB | n/a MB |
| python | 6715 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.535 MB | 7.535 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python | 6717 | sandbox_agent_lsb-native_0000_0000 | 9 | 99.994% | 100.515% | 8.040 s | 682.532 MB | 1227.602 MB | 728.115 MB | 1288.855 MB | n/a MB | n/a MB |
| python | 6754 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.648 MB | 7.648 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python | 6794 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.117 MB | 7.117 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python | 6771 | sandbox_agent_lsb-native_0000_0000 | 2 | 2.977% | 2.977% | 0.030 s | 12.941 MB | 12.941 MB | 16.918 MB | 16.918 MB | n/a MB | n/a MB |
| tail | 6772 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 2.840 MB | 2.840 MB | n/a MB | n/a MB |
| python | 7150 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 237.500 MB | 237.500 MB | 700.961 MB | 700.961 MB | n/a MB | n/a MB |
| bash | 7147 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.809 MB | 2.809 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 7164 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.879 MB | 2.879 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7165 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.133 MB | 13.133 MB | 207.180 MB | 207.180 MB | n/a MB | n/a MB |
| bash | 7174 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.867 MB | 2.867 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7176 | sandbox_agent_lsb-native_0000_0000 | 2 | 197.881% | 197.881% | 1.990 s | 1373.988 MB | 1572.988 MB | 1794.281 MB | 1794.281 MB | n/a MB | n/a MB |
| bash | 7183 | sandbox_agent_lsb-native_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 2.707 MB | 2.707 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7184 | sandbox_agent_lsb-native_0000_0000 | 15 | 199.337% | 201.838% | 28.110 s | 1201.837 MB | 1535.398 MB | 1474.369 MB | 1757.352 MB | n/a MB | n/a MB |
| python | 7204 | sandbox_agent_lsb-native_0000_0000 | 2 | 77.552% | 77.552% | 0.780 s | 363.723 MB | 691.191 MB | 1598.256 MB | 1998.234 MB | n/a MB | n/a MB |
| bash | 7201 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.773 MB | 2.773 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 7214 | sandbox_agent_lsb-native_0000_0000 | 30 | 0.000% | 0.000% | 0.000 s | 2.965 MB | 2.965 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7216 | sandbox_agent_lsb-native_0000_0000 | 30 | 198.787% | 202.959% | 58.250 s | 1266.763 MB | 1385.543 MB | 1480.976 MB | 1599.023 MB | n/a MB | n/a MB |
| bash | 7322 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.020 MB | 3.020 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7323 | sandbox_agent_lsb-native_0000_0000 | 5 | 198.736% | 202.382% | 8.050 s | 1044.573 MB | 1293.465 MB | 1289.851 MB | 1596.039 MB | n/a MB | n/a MB |
| python | 7335 | sandbox_agent_lsb-native_0000_0000 | 3 | 175.592% | 189.953% | 3.540 s | 948.977 MB | 1492.152 MB | 1807.658 MB | 2683.469 MB | n/a MB | n/a MB |
| bash | 7333 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.656 MB | 2.656 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 7346 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.055 MB | 3.055 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7347 | sandbox_agent_lsb-native_0000_0000 | 2 | 193.916% | 193.916% | 1.950 s | 1311.383 MB | 1375.414 MB | 2503.102 MB | 2566.848 MB | n/a MB | n/a MB |
| bash | 7356 | sandbox_agent_lsb-native_0000_0000 | 16 | 0.000% | 0.000% | 0.000 s | 2.840 MB | 2.840 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7357 | sandbox_agent_lsb-native_0000_0000 | 15 | 197.895% | 202.892% | 27.930 s | 1160.175 MB | 1327.625 MB | 2350.072 MB | 2519.332 MB | n/a MB | n/a MB |
| python | 7370 | sandbox_agent_lsb-native_0000_0000 | 10 | 198.955% | 204.660% | 18.030 s | 1013.369 MB | 1085.379 MB | 1253.845 MB | 1381.094 MB | n/a MB | n/a MB |
| bash | 7368 | sandbox_agent_lsb-native_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.957 MB | 2.957 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 7382 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.035 MB | 3.035 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7383 | sandbox_agent_lsb-native_0000_0000 | 4 | 155.009% | 165.884% | 4.680 s | 1005.580 MB | 1355.008 MB | 2188.963 MB | 2545.215 MB | n/a MB | n/a MB |
| python | 7397 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 26.320 MB | 26.320 MB | 217.570 MB | 217.570 MB | n/a MB | n/a MB |
| bash | 7396 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.867 MB | 2.867 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7406 | sandbox_agent_lsb-native_0000_0000 | 16 | 197.811% | 201.283% | 29.870 s | 1475.800 MB | 2001.934 MB | 3570.823 MB | 3735.188 MB | n/a MB | n/a MB |
| python | 7503 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.363 MB | 7.363 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python | 7484 | sandbox_agent_lsb-native_0000_0000 | 2 | 4.964% | 4.964% | 0.050 s | 13.172 MB | 13.297 MB | 17.047 MB | 17.105 MB | n/a MB | n/a MB |
| python | 7543 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.539 MB | 8.539 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| python | 7791 | sandbox_agent_lsb-native_0000_0000 | 7 | 4.135% | 4.963% | 0.250 s | 13.255 MB | 13.309 MB | 17.107 MB | 17.117 MB | n/a MB | n/a MB |
| python | 7819 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.000 MB | 5.000 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| bash | 7790 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 7860 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python | 7900 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.641 MB | 7.641 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 7941 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.301 MB | 7.301 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python | 7981 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.930 MB | 6.930 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python | 8020 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.605 MB | 7.605 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 8061 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.609 MB | 7.609 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| bash | 8215 | sandbox_agent_lsb-native_0000_0000 | 19 | 0.000% | 0.000% | 0.000 s | 2.957 MB | 2.957 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8217 | sandbox_agent_lsb-native_0000_0000 | 19 | 174.105% | 200.944% | 31.600 s | 1199.422 MB | 1518.805 MB | 2406.747 MB | 2703.508 MB | n/a MB | n/a MB |
| bash | 8259 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.840 MB | 2.965 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8260 | sandbox_agent_lsb-native_0000_0000 | 2 | 196.860% | 196.860% | 1.980 s | 1439.742 MB | 1534.551 MB | 2630.682 MB | 2725.410 MB | n/a MB | n/a MB |
| python | 8501 | sandbox_agent_lsb-native_0000_0000 | 12 | 78.647% | 152.158% | 8.710 s | 352.365 MB | 1588.277 MB | 1510.302 MB | 2779.488 MB | n/a MB | n/a MB |
| bash | 8500 | sandbox_agent_lsb-native_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 3.039 MB | 3.039 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8515 | sandbox_agent_lsb-native_0000_0000 | 9 | 200.572% | 210.081% | 16.170 s | 1621.829 MB | 1764.922 MB | 1837.927 MB | 1980.312 MB | n/a MB | n/a MB |
| bash | 8514 | sandbox_agent_lsb-native_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.996 MB | 2.996 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8525 | sandbox_agent_lsb-native_0000_0000 | 26 | 197.761% | 204.042% | 49.950 s | 2221.520 MB | 3042.168 MB | 3436.805 MB | 4227.008 MB | n/a MB | n/a MB |
| python | 8623 | sandbox_agent_lsb-native_0000_0000 | 17 | 192.019% | 202.178% | 31.000 s | 2700.406 MB | 3187.926 MB | 4364.066 MB | 5238.305 MB | n/a MB | n/a MB |
| python | 8642 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2587.707 MB | 2587.707 MB | 3779.914 MB | 3779.914 MB | n/a MB | n/a MB |
| bash | 8639 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.738 MB | 2.738 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8653 | sandbox_agent_lsb-native_0000_0000 | 6 | 192.862% | 201.561% | 9.780 s | 919.547 MB | 1100.809 MB | 1946.109 MB | 2293.863 MB | n/a MB | n/a MB |
| bash | 8652 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 3.023 MB | 3.023 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 8762 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.789 MB | 2.789 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8763 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.137 MB | 13.137 MB | 207.281 MB | 207.281 MB | n/a MB | n/a MB |
| bash | 8785 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.945 MB | 2.945 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8786 | sandbox_agent_lsb-native_0000_0000 | 6 | 199.522% | 201.856% | 10.070 s | 1274.981 MB | 1359.594 MB | 2469.771 MB | 2592.320 MB | n/a MB | n/a MB |
| python | 8880 | sandbox_agent_lsb-native_0000_0000 | 16 | 194.641% | 201.278% | 29.410 s | 2867.348 MB | 3362.344 MB | 4767.327 MB | 5374.145 MB | n/a MB | n/a MB |
| bash | 8890 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.980 MB | 2.980 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8891 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 85.508 MB | 85.508 MB | 1247.387 MB | 1247.387 MB | n/a MB | n/a MB |
| python | 8903 | sandbox_agent_lsb-native_0000_0000 | 4 | 174.848% | 199.297% | 5.290 s | 2125.213 MB | 3007.227 MB | 3200.784 MB | 4198.648 MB | n/a MB | n/a MB |
| bash | 8902 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.824 MB | 2.824 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 8914 | sandbox_agent_lsb-native_0000_0000 | 25 | 0.000% | 0.000% | 0.000 s | 2.941 MB | 2.941 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8915 | sandbox_agent_lsb-native_0000_0000 | 25 | 198.878% | 201.919% | 48.100 s | 2817.103 MB | 3017.973 MB | 4889.165 MB | 5153.609 MB | n/a MB | n/a MB |
| bash | 8994 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8995 | sandbox_agent_lsb-native_0000_0000 | 7 | 194.809% | 201.202% | 11.800 s | 105.824 MB | 137.535 MB | 462.387 MB | 1312.797 MB | n/a MB | n/a MB |
| python3 | 9010 | sandbox_agent_lsb-native_0000_0000 | 13 | 0.000% | 0.000% | 0.000 s | 8.377 MB | 72.945 MB | 10.928 MB | 91.488 MB | n/a MB | n/a MB |
| python | 9011 | sandbox_agent_lsb-native_0000_0000 | 12 | 199.531% | 201.498% | 22.120 s | 1181.435 MB | 1371.016 MB | 2292.389 MB | 2562.656 MB | n/a MB | n/a MB |
| docker | 9143 |  | 1 | n/a% | n/a% | n/a s | 30.207 MB | 30.207 MB | 1843.770 MB | 1843.770 MB | n/a MB | n/a MB |
| docker | 9160 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.141 MB | 30.141 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |
| docker | 9210 |  | 1 | n/a% | n/a% | n/a s | 30.152 MB | 30.152 MB | 1907.590 MB | 1907.590 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 3.293% | 100.000% | 11948.866 MB | 13020.000 MB | 29.941 W | 73.779 W | 84418.842 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 23.282% | 209.925% | 652.041 s | 1863.953 MB | 6019.781 MB | 337.847656 MB | 2307.839844 MB | 0.001112 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 5960 | 2820.313 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2795.971 | n/a | n/a | 337.848 | 2795971.068 | 2795971.068 | 2795971.068 |
| engine:execute | 1/1 | 0 | 0 | 2795.969 | 2.864 | 2793.087 | 337.848 | 2795969.459 | 2795969.459 | 2795969.459 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2768.661 | 0.004 | 2768.657 | 337.676 | 2768661.118 | 2768661.118 | 2768661.118 |
| turn | 94/94 | 0 | 0 | 2766.111 | n/a | n/a | 337.426 | 29426.714 | 23979.593 | 60160.201 |
| llm:attempt | 94/94 | 0 | 0 | 2286.044 | 4.396 | 2281.645 | 8.728 | 24319.618 | 21015.525 | 55801.447 |
| tool:bash | 61/61 | 0 | 0 | 307.912 | n/a | n/a | 326.919 | 5047.745 | 1139.700 | 19307.759 |
| process:bash | 61/61 | 1 | 0 | 307.293 | n/a | n/a | 326.774 | 5037.594 | 1130.821 | 19292.261 |
| tool:generate | 8/8 | 0 | 0 | 66.582 | n/a | n/a | 0.003 | 8322.778 | 8007.663 | 12900.981 |
| tool:trace | 9/9 | 0 | 0 | 52.940 | n/a | n/a | 0.005 | 5882.239 | 5872.522 | 10877.141 |
| run:container_call | 13/13 | 0 | 0 | 23.913 | 0.003 | 23.910 | 0.077 | 1839.435 | 53.675 | 9361.708 |
| teardown:commit | 1/1 | 0 | 0 | 23.495 | 0.005 | 23.490 | 0.077 | 23494.673 | 23494.673 | 23494.673 |
| sandbox:commit | 1/1 | 0 | 0 | 23.286 | 0.003 | 23.283 | 0.077 | 23285.884 | 23285.884 | 23285.884 |
| checkpoint.total | 1/1 | 0 | 0 | 23.286 | 0.003 | 23.283 | 0.077 | 23285.723 | 23285.723 | 23285.723 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 23.286 | 0.002 | 23.283 | 0.077 | 23285.548 | 23285.548 | 23285.548 |
| tool:inspect | 8/8 | 0 | 0 | 16.275 | n/a | n/a | 0.038 | 2034.345 | 2036.138 | 2156.216 |
| tool:token_stats | 2/2 | 0 | 0 | 13.589 | n/a | n/a | 0.000 | 6794.347 | 6794.347 | 10905.930 |
| tool:patch | 23/23 | 0 | 0 | 9.692 | n/a | n/a | 0.000 | 421.397 | 419.964 | 439.582 |
| syscall:sendto | 2579/2579 | 0 | 0 | 6.000 | n/a | n/a | 0.529 | 2.326 | 2.001 | 4.515 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.098 | 0.714 | 2.384 | 0.000 | 3098.141 | 3098.141 | 3098.141 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.098 | 0.714 | 2.384 | 0.000 | 3097.844 | 3097.844 | 3097.844 |
| syscall:connect | 697/697 | 0 | 0 | 1.655 | n/a | n/a | 0.145 | 2.375 | 2.011 | 4.577 |
| syscall:execve | 1025/1025 | 0 | 0 | 1.238 | n/a | n/a | 0.069 | 1.208 | 1.139 | 1.610 |
| tool:attribution | 2/2 | 0 | 0 | 0.663 | n/a | n/a | 0.000 | 331.682 | 331.682 | 337.970 |
| tool:attention | 2/2 | 0 | 0 | 0.655 | n/a | n/a | 0.000 | 327.366 | 327.366 | 353.696 |
| tool:submit_output | 2/2 | 0 | 0 | 0.474 | n/a | n/a | 0.000 | 236.849 | 236.849 | 240.178 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.354 | n/a | n/a | 0.000 | 354.036 | 354.036 | 354.036 |
| sandbox:start | 1/1 | 0 | 0 | 0.352 | 0.002 | 0.350 | 0.000 | 352.217 | 352.217 | 352.217 |
| runtime.container_create | 1/1 | 0 | 0 | 0.352 | 0.002 | 0.350 | 0.000 | 352.086 | 352.086 | 352.086 |
| sandbox:create | 1/1 | 0 | 0 | 0.340 | 0.247 | 0.093 | 0.000 | 340.358 | 340.358 | 340.358 |
| tool:get_current_resources | 1/1 | 0 | 0 | 0.242 | n/a | n/a | 0.000 | 241.659 | 241.659 | 241.659 |
| sandbox:stop | 1/1 | 0 | 0 | 0.209 | 0.002 | 0.207 | 0.000 | 208.516 | 208.516 | 208.516 |
| agency:services_close | 1/1 | 0 | 0 | 0.170 | 0.001 | 0.169 | 0.084 | 169.571 | 169.571 | 169.571 |
| agency:services_start | 1/1 | 0 | 0 | 0.070 | 0.040 | 0.030 | 0.000 | 70.432 | 70.432 | 70.432 |
| run:detect | 1/1 | 0 | 0 | 0.055 | 0.001 | 0.055 | 0.000 | 55.417 | 55.417 | 55.417 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.008 | 0.041 | 0.000 | 49.488 | 49.488 | 49.488 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.002 | 4.299 | 4.299 | 4.299 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.198 | 1.198 | 1.198 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.074 | 0.070 | 0.106 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.167 | 0.167 | 0.167 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.097 | 0.097 | 0.097 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2802 | 0.334 | 0.035 | 43.284 | 0.045 | 9.399445 CPU seconds | n/a |
| GPU 0 memory | MB | 2803 | 11948.866 | 11670.000 | 13020.000 | 11898.000 | n/a | n/a |
| GPU 0 power | W | 2803 | 29.941 | 28.132 | 73.779 | 28.171 | n/a | 84418.842 J |
| GPU 0 proc / 5812-835947 / sandbox / ~ / device / GPU-180de555-2877-179b-374e-80424af6fcc8 memory | MB | 2803 | 3270.796 | 3118.000 | 4336.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 5812-835947 / sandbox / ~ / device / GPU-180de555-2877-179b-374e-80424af6fcc8 estimated power | W | 2271 | 1.546 | 0.000 | 73.779 | 0.000 | n/a | n/a |
| GPU 0 proc / 5812-835947 / sandbox / ~ / device / GPU-180de555-2877-179b-374e-80424af6fcc8 utilization | percent | 2271 | 1.261 | 0.000 | 92.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 5852-837785 / sandbox / ~ / device / GPU-180de555-2877-179b-374e-80424af6fcc8 memory | MB | 2803 | 8196.070 | 8070.000 | 8202.000 | 8202.000 | n/a | n/a |
| GPU 0 proc / 5852-837785 / sandbox / ~ / device / GPU-180de555-2877-179b-374e-80424af6fcc8 estimated power | W | 497 | 8.712 | 0.000 | 73.329 | 0.000 | n/a | n/a |
| GPU 0 proc / 5852-837785 / sandbox / ~ / device / GPU-180de555-2877-179b-374e-80424af6fcc8 utilization | percent | 497 | 12.026 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2803 | 11466.866 | 11188.000 | 12538.000 | 11416.000 | n/a | n/a |
| GPU 0 utilization | percent | 2803 | 3.293 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2803 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2802 | 4.638 | 0.009 | 54.816 | 0.240 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2802 | 7.330 | 0.000 | 60.794 | 0.500 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2802 | 0.776 | 0.000 | 222.324 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2802 | 3.422 | 0.000 | 230.609 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2802 | 1.273 | 0.000 | 94.002 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2802 | 1.340 | 0.000 | 94.729 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 2803 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 2803 | 7479.250 | 6449.133 | 11120.746 | 7925.316 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2802 | 0.027 | 0.000 | 15.049 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2802 | 0.027 | 0.000 | 15.088 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2802 | 0.001 | 0.000 | 0.578 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2802 | 0.023 | 0.000 | 1.258 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4980) CPU | percent | 2802 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4980) io read MB/s | MB/s | 2802 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4980) io write MB/s | MB/s | 2802 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4980) rss_mb | MB | 2803 | 3.344 | 3.344 | 3.344 | 3.344 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4980) main thread run-queue wait | percent | 2802 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4980) vms_mb | MB | 2803 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 5812) CPU | percent | 2802 | 3.772 | 0.000 | 167.121 | 0.996 | 106.730000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 5812) io read MB/s | MB/s | 2802 | 0.027 | 0.000 | 41.671 | 0.000 | 75.917969 MB | n/a |
| Agency harness — python -m lsbench (PID 5812) io write MB/s | MB/s | 2802 | 2.581 | 0.012 | 861.537 | 0.027 | 7283.367188 MB | n/a |
| Agency harness — python -m lsbench (PID 5812) rss_mb | MB | 2803 | 3262.818 | 2319.688 | 5512.055 | 3941.371 | n/a | n/a |
| Agency harness — python -m lsbench (PID 5812) main thread run-queue wait | percent | 2802 | 0.001 | 0.000 | 1.696 | 0.000 | 0.022231 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 5812) vms_mb | MB | 2803 | 16423.455 | 13795.871 | 19367.773 | 16962.621 | n/a | n/a |
| Python — vllm (PID 5817) CPU | percent | 2802 | 0.182 | 0.000 | 5.963 | 0.000 | 5.150000 CPU seconds | n/a |
| Python — vllm (PID 5817) io read MB/s | MB/s | 2802 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 5817) io write MB/s | MB/s | 2802 | 0.000 | 0.000 | 0.008 | 0.000 | 0.046875 MB | n/a |
| Python — vllm (PID 5817) rss_mb | MB | 2803 | 1791.253 | 1753.305 | 1803.961 | 1753.305 | n/a | n/a |
| Python — vllm (PID 5817) main thread run-queue wait | percent | 2802 | 0.003 | 0.000 | 0.580 | 0.000 | 0.097489 run-queue seconds | n/a |
| Python — vllm (PID 5817) vms_mb | MB | 2803 | 11044.736 | 10974.566 | 11046.586 | 11046.586 | n/a | n/a |
| Python — python -c (PID 5851) CPU | percent | 2802 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 5851) io read MB/s | MB/s | 2802 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 5851) io write MB/s | MB/s | 2802 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 5851) rss_mb | MB | 2803 | 12.080 | 12.051 | 12.176 | 12.051 | n/a | n/a |
| Python — python -c (PID 5851) main thread run-queue wait | percent | 2802 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 5851) vms_mb | MB | 2803 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 5852) CPU | percent | 2802 | 2.293 | 0.000 | 57.334 | 0.996 | 64.710000 CPU seconds | n/a |
| VLLM::EngineCore (PID 5852) io read MB/s | MB/s | 2802 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 5852) io write MB/s | MB/s | 2802 | 0.000 | 0.000 | 0.004 | 0.000 | 0.015625 MB | n/a |
| VLLM::EngineCore (PID 5852) rss_mb | MB | 2803 | 2311.270 | 2271.746 | 2324.484 | 2271.746 | n/a | n/a |
| VLLM::EngineCore (PID 5852) main thread run-queue wait | percent | 2802 | 0.000 | 0.000 | 0.055 | 0.000 | 0.006573 run-queue seconds | n/a |
| VLLM::EngineCore (PID 5852) vms_mb | MB | 2803 | 21267.672 | 21267.078 | 21268.094 | 21268.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 6070) CPU | percent | 2778 | 0.002 | 0.000 | 0.995 | 0.000 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 6070) rss_mb | MB | 2779 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 6070) main thread run-queue wait | percent | 2778 | 0.006 | 0.000 | 5.295 | 0.002 | 0.180893 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 6070) vms_mb | MB | 2779 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 6102) CPU | percent | 2778 | 0.002 | 0.000 | 0.995 | 0.000 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 6102) rss_mb | MB | 2779 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 6102) main thread run-queue wait | percent | 2778 | 0.006 | 0.000 | 5.257 | 0.030 | 0.157889 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 6102) vms_mb | MB | 2779 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6193) CPU | percent | 2778 | 4.297 | 0.000 | 100.469 | 0.000 | 120.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6193) rss_mb | MB | 2779 | 102.503 | 3.055 | 107.500 | 104.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6193) main thread run-queue wait | percent | 2778 | 0.000 | 0.000 | 0.008 | 0.007 | 0.000218 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6193) vms_mb | MB | 2779 | 970.866 | 4.258 | 973.961 | 973.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6199) CPU | percent | 1 | 100.900 | 100.900 | 100.900 | 100.900 | 1.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6199) rss_mb | MB | 2 | 53.820 | 26.289 | 81.352 | 81.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6199) main thread run-queue wait | percent | 1 | 0.012 | 0.012 | 0.012 | 0.012 | 0.000123 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6199) vms_mb | MB | 2 | 65.947 | 35.219 | 96.676 | 96.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 6211) CPU | percent | 2751 | 0.169 | 0.000 | 61.601 | 0.000 | 4.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 6211) rss_mb | MB | 2752 | 73.404 | 30.703 | 76.691 | 73.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 6211) main thread run-queue wait | percent | 2751 | 0.010 | 0.000 | 1.190 | 0.000 | 0.265566 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 6211) vms_mb | MB | 2752 | 88.290 | 36.234 | 92.867 | 91.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6224) rss_mb | MB | 1 | 2.973 | 2.973 | 2.973 | 2.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6224) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6229) rss_mb | MB | 1 | 13.000 | 13.000 | 13.000 | 13.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 6229) vms_mb | MB | 1 | 207.148 | 207.148 | 207.148 | 207.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ev.py (PID 6303) CPU | percent | 2 | 3.474 | 2.979 | 3.970 | 2.979 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ev.py (PID 6303) rss_mb | MB | 3 | 12.469 | 12.469 | 12.469 | 12.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ev.py (PID 6303) main thread run-queue wait | percent | 2 | 0.020 | 0.018 | 0.023 | 0.023 | 0.000409 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ev.py (PID 6303) vms_mb | MB | 3 | 15.883 | 15.883 | 15.883 | 15.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpmi4dbmtv.py (PID 6320) rss_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpmi4dbmtv.py (PID 6320) vms_mb | MB | 1 | 6.734 | 6.734 | 6.734 | 6.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp92dr98d7.py (PID 6361) rss_mb | MB | 1 | 7.406 | 7.406 | 7.406 | 7.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp92dr98d7.py (PID 6361) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ev.py (PID 6403) rss_mb | MB | 1 | 12.469 | 12.469 | 12.469 | 12.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ev.py (PID 6403) vms_mb | MB | 1 | 15.883 | 15.883 | 15.883 | 15.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6526) CPU | percent | 2 | 3.974 | 3.971 | 3.978 | 3.971 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6526) rss_mb | MB | 3 | 12.919 | 12.836 | 13.086 | 13.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6526) main thread run-queue wait | percent | 2 | 0.015 | 0.014 | 0.015 | 0.015 | 0.000294 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6526) vms_mb | MB | 3 | 17.029 | 17.012 | 17.062 | 17.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpv5tzt6v6.py (PID 6539) rss_mb | MB | 1 | 7.898 | 7.898 | 7.898 | 7.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpv5tzt6v6.py (PID 6539) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp9q7odgfm.py (PID 6581) rss_mb | MB | 1 | 7.672 | 7.672 | 7.672 | 7.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp9q7odgfm.py (PID 6581) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpttgrhcip.py (PID 6621) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpttgrhcip.py (PID 6621) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6673) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6673) rss_mb | MB | 15 | 2.871 | 2.871 | 2.871 | 2.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6673) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6673) vms_mb | MB | 15 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6674) CPU | percent | 12 | 0.741 | 0.000 | 4.911 | 3.981 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6674) rss_mb | MB | 13 | 13.077 | 12.730 | 13.105 | 13.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6674) main thread run-queue wait | percent | 12 | 0.002 | 0.000 | 0.014 | 0.010 | 0.000272 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6674) vms_mb | MB | 13 | 17.058 | 17.047 | 17.059 | 17.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6675) rss_mb | MB | 1 | 12.730 | 12.730 | 12.730 | 12.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6675) vms_mb | MB | 1 | 17.047 | 17.047 | 17.047 | 17.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmppc3d9hue.py (PID 6715) rss_mb | MB | 1 | 7.535 | 7.535 | 7.535 | 7.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmppc3d9hue.py (PID 6715) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp_ypewy7r.py (PID 6717) CPU | percent | 8 | 99.994 | 98.486 | 100.515 | 100.515 | 8.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp_ypewy7r.py (PID 6717) rss_mb | MB | 9 | 682.532 | 136.727 | 1227.602 | 1227.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp_ypewy7r.py (PID 6717) main thread run-queue wait | percent | 8 | 0.002 | 0.001 | 0.003 | 0.003 | 0.000187 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp_ypewy7r.py (PID 6717) vms_mb | MB | 9 | 728.115 | 149.215 | 1288.855 | 1288.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpjzpwn7um.py (PID 6754) rss_mb | MB | 1 | 7.648 | 7.648 | 7.648 | 7.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpjzpwn7um.py (PID 6754) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6771) CPU | percent | 1 | 2.977 | 2.977 | 2.977 | 2.977 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6771) rss_mb | MB | 2 | 12.941 | 12.941 | 12.941 | 12.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6771) main thread run-queue wait | percent | 1 | 0.019 | 0.019 | 0.019 | 0.019 | 0.000194 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip.py (PID 6771) vms_mb | MB | 2 | 16.918 | 16.918 | 16.918 | 16.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 6772) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 6772) rss_mb | MB | 2 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 6772) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 6772) vms_mb | MB | 2 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpdm7_bifq.py (PID 6794) rss_mb | MB | 1 | 7.117 | 7.117 | 7.117 | 7.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpdm7_bifq.py (PID 6794) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7147) rss_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7147) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7150) rss_mb | MB | 1 | 237.500 | 237.500 | 237.500 | 237.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7150) vms_mb | MB | 1 | 700.961 | 700.961 | 700.961 | 700.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7164) rss_mb | MB | 1 | 2.879 | 2.879 | 2.879 | 2.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7164) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7165) rss_mb | MB | 1 | 13.133 | 13.133 | 13.133 | 13.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7165) vms_mb | MB | 1 | 207.180 | 207.180 | 207.180 | 207.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7174) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7174) rss_mb | MB | 2 | 2.867 | 2.867 | 2.867 | 2.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7174) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7174) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7176) CPU | percent | 1 | 197.881 | 197.881 | 197.881 | 197.881 | 1.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7176) rss_mb | MB | 2 | 1373.988 | 1174.988 | 1572.988 | 1572.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7176) main thread run-queue wait | percent | 1 | 49.890 | 49.890 | 49.890 | 49.890 | 0.501727 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7176) vms_mb | MB | 2 | 1794.281 | 1794.281 | 1794.281 | 1794.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7183) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7183) rss_mb | MB | 15 | 2.707 | 2.707 | 2.707 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7183) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7183) vms_mb | MB | 15 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7184) CPU | percent | 14 | 199.337 | 197.830 | 201.838 | 200.816 | 28.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7184) rss_mb | MB | 15 | 1201.837 | 765.398 | 1535.398 | 1157.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7184) main thread run-queue wait | percent | 14 | 50.398 | 48.429 | 55.687 | 50.778 | 7.106782 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7184) vms_mb | MB | 15 | 1474.369 | 1378.441 | 1757.352 | 1378.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7201) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7201) rss_mb | MB | 2 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7201) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7201) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7204) CPU | percent | 1 | 77.552 | 77.552 | 77.552 | 77.552 | 0.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7204) rss_mb | MB | 2 | 363.723 | 36.254 | 691.191 | 691.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7204) main thread run-queue wait | percent | 1 | 0.056 | 0.056 | 0.056 | 0.056 | 0.000568 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7204) vms_mb | MB | 2 | 1598.256 | 1198.277 | 1998.234 | 1998.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7214) CPU | percent | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7214) rss_mb | MB | 30 | 2.965 | 2.965 | 2.965 | 2.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7214) main thread run-queue wait | percent | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7214) vms_mb | MB | 30 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7216) CPU | percent | 29 | 198.787 | 190.521 | 202.959 | 195.481 | 58.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7216) rss_mb | MB | 30 | 1266.763 | 1230.770 | 1385.543 | 1385.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7216) main thread run-queue wait | percent | 29 | 48.940 | 43.005 | 55.332 | 43.677 | 14.340835 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7216) vms_mb | MB | 30 | 1480.976 | 1448.961 | 1599.023 | 1599.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7322) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7322) rss_mb | MB | 5 | 3.020 | 3.020 | 3.020 | 3.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7322) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7322) vms_mb | MB | 5 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7323) CPU | percent | 4 | 198.736 | 189.085 | 202.382 | 201.777 | 8.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7323) rss_mb | MB | 5 | 1044.573 | 236.203 | 1293.465 | 1293.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7323) main thread run-queue wait | percent | 4 | 47.105 | 39.378 | 50.036 | 49.819 | 1.908174 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7323) vms_mb | MB | 5 | 1289.851 | 506.273 | 1596.039 | 1596.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7333) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7333) rss_mb | MB | 3 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7333) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7333) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7335) CPU | percent | 2 | 175.592 | 161.231 | 189.953 | 189.953 | 3.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7335) rss_mb | MB | 3 | 948.977 | 13.223 | 1492.152 | 1492.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7335) main thread run-queue wait | percent | 2 | 41.589 | 35.320 | 47.859 | 47.859 | 0.838301 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7335) vms_mb | MB | 3 | 1807.658 | 207.160 | 2683.469 | 2683.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7346) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7346) rss_mb | MB | 2 | 3.055 | 3.055 | 3.055 | 3.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7346) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7346) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7347) CPU | percent | 1 | 193.916 | 193.916 | 193.916 | 193.916 | 1.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7347) rss_mb | MB | 2 | 1311.383 | 1247.352 | 1375.414 | 1375.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7347) main thread run-queue wait | percent | 1 | 43.708 | 43.708 | 43.708 | 43.708 | 0.439524 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7347) vms_mb | MB | 2 | 2503.102 | 2439.355 | 2566.848 | 2566.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7356) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7356) rss_mb | MB | 16 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7356) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7356) vms_mb | MB | 16 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7357) CPU | percent | 14 | 197.895 | 182.952 | 202.892 | 200.106 | 27.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7357) rss_mb | MB | 15 | 1160.175 | 58.910 | 1327.625 | 1212.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7357) main thread run-queue wait | percent | 14 | 49.748 | 41.441 | 53.816 | 50.556 | 7.021243 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7357) vms_mb | MB | 15 | 2350.072 | 1221.172 | 2519.332 | 2404.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7368) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7368) rss_mb | MB | 10 | 2.957 | 2.957 | 2.957 | 2.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7368) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7368) vms_mb | MB | 10 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7370) CPU | percent | 9 | 198.955 | 189.959 | 204.660 | 198.849 | 18.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7370) rss_mb | MB | 10 | 1013.369 | 842.188 | 1085.379 | 1082.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7370) main thread run-queue wait | percent | 9 | 48.548 | 40.575 | 51.022 | 50.032 | 4.399619 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7370) vms_mb | MB | 10 | 1253.845 | 1150.027 | 1381.094 | 1381.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7382) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7382) rss_mb | MB | 4 | 3.035 | 3.035 | 3.035 | 3.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7382) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7382) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7383) CPU | percent | 3 | 155.009 | 141.071 | 165.884 | 141.071 | 4.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7383) rss_mb | MB | 4 | 1005.580 | 56.336 | 1355.008 | 1355.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7383) main thread run-queue wait | percent | 3 | 23.870 | 14.972 | 29.825 | 14.972 | 0.720676 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7383) vms_mb | MB | 4 | 2188.963 | 1217.438 | 2545.215 | 2545.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7396) rss_mb | MB | 1 | 2.867 | 2.867 | 2.867 | 2.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7396) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7397) rss_mb | MB | 1 | 26.320 | 26.320 | 26.320 | 26.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7397) vms_mb | MB | 1 | 217.570 | 217.570 | 217.570 | 217.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 7406) CPU | percent | 15 | 197.811 | 182.426 | 201.283 | 182.426 | 29.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 7406) rss_mb | MB | 16 | 1475.800 | 1427.633 | 2001.934 | 2001.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 7406) main thread run-queue wait | percent | 15 | 48.440 | 40.324 | 50.670 | 40.324 | 7.314538 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 7406) vms_mb | MB | 16 | 3570.823 | 3185.172 | 3735.188 | 3185.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip2.py (PID 7484) CPU | percent | 1 | 4.964 | 4.964 | 4.964 | 4.964 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip2.py (PID 7484) rss_mb | MB | 2 | 13.172 | 13.047 | 13.297 | 13.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip2.py (PID 7484) main thread run-queue wait | percent | 1 | 0.021 | 0.021 | 0.021 | 0.021 | 0.000210 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — strip2.py (PID 7484) vms_mb | MB | 2 | 17.047 | 16.988 | 17.105 | 17.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp24axf62f.py (PID 7503) rss_mb | MB | 1 | 7.363 | 7.363 | 7.363 | 7.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp24axf62f.py (PID 7503) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp381xlusi.py (PID 7543) rss_mb | MB | 1 | 8.539 | 8.539 | 8.539 | 8.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp381xlusi.py (PID 7543) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7790) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7790) rss_mb | MB | 7 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7790) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7790) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7791) CPU | percent | 6 | 4.135 | 2.980 | 4.963 | 4.961 | 0.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7791) rss_mb | MB | 7 | 13.255 | 13.059 | 13.309 | 13.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7791) main thread run-queue wait | percent | 6 | 0.019 | 0.011 | 0.027 | 0.027 | 0.001122 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 7791) vms_mb | MB | 7 | 17.107 | 17.043 | 17.117 | 17.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpar0c8523.py (PID 7819) rss_mb | MB | 1 | 5.000 | 5.000 | 5.000 | 5.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpar0c8523.py (PID 7819) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmph29jphv9.py (PID 7860) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmph29jphv9.py (PID 7860) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp7zifvzoh.py (PID 7900) rss_mb | MB | 1 | 7.641 | 7.641 | 7.641 | 7.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp7zifvzoh.py (PID 7900) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpvv7r591e.py (PID 7941) rss_mb | MB | 1 | 7.301 | 7.301 | 7.301 | 7.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpvv7r591e.py (PID 7941) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpukrawfld.py (PID 7981) rss_mb | MB | 1 | 6.930 | 6.930 | 6.930 | 6.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpukrawfld.py (PID 7981) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp66ojypv5.py (PID 8020) rss_mb | MB | 1 | 7.605 | 7.605 | 7.605 | 7.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp66ojypv5.py (PID 8020) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpi3orn1u4.py (PID 8061) rss_mb | MB | 1 | 7.609 | 7.609 | 7.609 | 7.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpi3orn1u4.py (PID 8061) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8215) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8215) rss_mb | MB | 19 | 2.957 | 2.957 | 2.957 | 2.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8215) main thread run-queue wait | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8215) vms_mb | MB | 19 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8217) CPU | percent | 18 | 174.105 | 19.895 | 200.944 | 194.882 | 31.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8217) rss_mb | MB | 19 | 1199.422 | 478.156 | 1518.805 | 1095.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8217) main thread run-queue wait | percent | 18 | 39.636 | 0.041 | 53.901 | 44.283 | 7.195746 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8217) vms_mb | MB | 19 | 2406.747 | 1884.281 | 2703.508 | 2279.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8259) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8259) rss_mb | MB | 3 | 2.840 | 2.590 | 2.965 | 2.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8259) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8259) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8260) CPU | percent | 1 | 196.860 | 196.860 | 196.860 | 196.860 | 1.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8260) rss_mb | MB | 2 | 1439.742 | 1344.934 | 1534.551 | 1534.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8260) main thread run-queue wait | percent | 1 | 52.635 | 52.635 | 52.635 | 52.635 | 0.529394 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8260) vms_mb | MB | 2 | 2630.682 | 2535.953 | 2725.410 | 2725.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8500) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8500) rss_mb | MB | 12 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8500) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8500) vms_mb | MB | 12 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8501) CPU | percent | 11 | 78.647 | 70.432 | 152.158 | 152.158 | 8.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8501) rss_mb | MB | 12 | 352.365 | 19.676 | 1588.277 | 1588.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8501) main thread run-queue wait | percent | 11 | 2.340 | 0.082 | 24.783 | 24.783 | 0.258784 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8501) vms_mb | MB | 12 | 1510.302 | 211.848 | 2779.488 | 2779.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8514) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8514) rss_mb | MB | 9 | 2.996 | 2.996 | 2.996 | 2.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8514) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8514) vms_mb | MB | 9 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8515) CPU | percent | 8 | 200.572 | 197.813 | 210.081 | 199.140 | 16.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8515) rss_mb | MB | 9 | 1621.829 | 1548.109 | 1764.922 | 1764.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8515) main thread run-queue wait | percent | 8 | 49.093 | 42.818 | 54.827 | 44.413 | 3.957637 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8515) vms_mb | MB | 9 | 1837.927 | 1749.250 | 1980.312 | 1980.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_fit.py (PID 8525) CPU | percent | 25 | 197.761 | 171.675 | 204.042 | 198.805 | 49.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_fit.py (PID 8525) rss_mb | MB | 26 | 2221.520 | 586.742 | 3042.168 | 586.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_fit.py (PID 8525) main thread run-queue wait | percent | 25 | 48.034 | 30.560 | 55.023 | 50.376 | 12.134117 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_fit.py (PID 8525) vms_mb | MB | 26 | 3436.805 | 1771.434 | 4227.008 | 1771.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble.py (PID 8623) CPU | percent | 16 | 192.019 | 108.917 | 202.178 | 200.842 | 31.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble.py (PID 8623) rss_mb | MB | 17 | 2700.406 | 13.719 | 3187.926 | 3187.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble.py (PID 8623) main thread run-queue wait | percent | 16 | 46.032 | 13.344 | 55.179 | 53.011 | 7.431442 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble.py (PID 8623) vms_mb | MB | 17 | 4364.066 | 207.523 | 5238.305 | 4371.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8639) rss_mb | MB | 1 | 2.738 | 2.738 | 2.738 | 2.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8639) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8642) rss_mb | MB | 1 | 2587.707 | 2587.707 | 2587.707 | 2587.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8642) vms_mb | MB | 1 | 3779.914 | 3779.914 | 3779.914 | 3779.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8652) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8652) rss_mb | MB | 6 | 3.023 | 3.023 | 3.023 | 3.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8652) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8652) vms_mb | MB | 6 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8653) CPU | percent | 5 | 192.862 | 169.797 | 201.561 | 197.895 | 9.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8653) rss_mb | MB | 6 | 919.547 | 13.238 | 1100.809 | 1100.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8653) main thread run-queue wait | percent | 5 | 46.175 | 33.952 | 49.626 | 49.198 | 2.339661 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8653) vms_mb | MB | 6 | 1946.109 | 207.336 | 2293.863 | 2293.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8762) rss_mb | MB | 1 | 2.789 | 2.789 | 2.789 | 2.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8762) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8763) rss_mb | MB | 1 | 13.137 | 13.137 | 13.137 | 13.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8763) vms_mb | MB | 1 | 207.281 | 207.281 | 207.281 | 207.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8785) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8785) rss_mb | MB | 6 | 2.945 | 2.945 | 2.945 | 2.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8785) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8785) vms_mb | MB | 6 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8786) CPU | percent | 5 | 199.522 | 192.584 | 201.856 | 192.584 | 10.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8786) rss_mb | MB | 6 | 1274.981 | 1258.059 | 1359.594 | 1359.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8786) main thread run-queue wait | percent | 5 | 48.619 | 45.237 | 49.950 | 45.237 | 2.453879 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8786) vms_mb | MB | 6 | 2469.771 | 2445.262 | 2592.320 | 2592.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble2.py (PID 8880) CPU | percent | 15 | 194.641 | 135.979 | 201.278 | 197.880 | 29.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble2.py (PID 8880) rss_mb | MB | 16 | 2867.348 | 24.223 | 3362.344 | 2808.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble2.py (PID 8880) main thread run-queue wait | percent | 15 | 46.464 | 9.551 | 53.614 | 49.130 | 7.020286 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble2.py (PID 8880) vms_mb | MB | 16 | 4767.327 | 216.012 | 5374.145 | 4819.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8890) rss_mb | MB | 1 | 2.980 | 2.980 | 2.980 | 2.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8890) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8891) rss_mb | MB | 1 | 85.508 | 85.508 | 85.508 | 85.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8891) vms_mb | MB | 1 | 1247.387 | 1247.387 | 1247.387 | 1247.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8902) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8902) rss_mb | MB | 4 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8902) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8902) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8903) CPU | percent | 3 | 174.848 | 137.501 | 199.297 | 187.747 | 5.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8903) rss_mb | MB | 4 | 2125.213 | 13.172 | 3007.227 | 3007.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8903) main thread run-queue wait | percent | 3 | 38.929 | 16.876 | 50.065 | 49.847 | 1.177329 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8903) vms_mb | MB | 4 | 3200.784 | 207.191 | 4198.648 | 4198.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8914) CPU | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8914) rss_mb | MB | 25 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8914) main thread run-queue wait | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8914) vms_mb | MB | 25 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8915) CPU | percent | 24 | 198.878 | 191.857 | 201.919 | 191.857 | 48.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8915) rss_mb | MB | 25 | 2817.103 | 2390.219 | 3017.973 | 3017.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8915) main thread run-queue wait | percent | 24 | 49.102 | 42.058 | 54.129 | 49.396 | 11.875583 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8915) vms_mb | MB | 25 | 4889.165 | 4202.711 | 5153.609 | 4202.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8994) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8994) rss_mb | MB | 7 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8994) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8994) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8995) CPU | percent | 6 | 194.809 | 180.075 | 201.202 | 191.869 | 11.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8995) rss_mb | MB | 7 | 105.824 | 13.234 | 137.535 | 124.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8995) main thread run-queue wait | percent | 6 | 47.115 | 40.532 | 52.685 | 46.927 | 2.853736 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8995) vms_mb | MB | 7 | 462.387 | 207.227 | 1312.797 | 1312.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9010) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9010) rss_mb | MB | 13 | 8.377 | 2.996 | 72.945 | 2.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9010) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000047 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9010) vms_mb | MB | 13 | 10.928 | 4.215 | 91.488 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 9011) CPU | percent | 11 | 199.531 | 196.972 | 201.498 | 196.972 | 22.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 9011) rss_mb | MB | 12 | 1181.435 | 93.500 | 1371.016 | 93.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 9011) main thread run-queue wait | percent | 11 | 49.867 | 48.432 | 55.162 | 51.082 | 5.528195 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 9011) vms_mb | MB | 12 | 2292.389 | 315.020 | 2562.656 | 315.020 | n/a | n/a |
| docker inspect (PID 9143) rss_mb | MB | 1 | 30.207 | 30.207 | 30.207 | 30.207 | n/a | n/a |
| docker inspect (PID 9143) vms_mb | MB | 1 | 1843.770 | 1843.770 | 1843.770 | 1843.770 | n/a | n/a |
| docker commit (PID 9160) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 9160) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 9160) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 9160) rss_mb | MB | 22 | 30.141 | 30.141 | 30.141 | 30.141 | n/a | n/a |
| docker commit (PID 9160) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 9160) vms_mb | MB | 22 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker inspect (PID 9210) rss_mb | MB | 1 | 30.152 | 30.152 | 30.152 | 30.152 | n/a | n/a |
| docker inspect (PID 9210) vms_mb | MB | 1 | 1907.590 | 1907.590 | 1907.590 | 1907.590 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 2778 | 23.282 | 0.000 | 209.925 | 0.040 | 652.040506 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2778 | 4.403 | 0.000 | 50.584 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2778 | 4.473 | 0.000 | 51.281 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 2778 | 0.012 | 0.000 | 12.855 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 2778 | 0.012 | 0.000 | 12.857 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 2778 | 0.121 | 0.000 | 222.324 | 0.000 | 337.847656 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 2778 | 0.822 | 0.000 | 210.059 | 0.000 | 2307.839844 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 2779 | 1863.953 | 17.328 | 6019.781 | 2764.887 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2778 | 0.019 | 0.000 | 10.486 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2778 | 0.019 | 0.000 | 10.486 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 2778 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001112 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 2778 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 2802 | 6.253 | 1.399 | 167.592 | 2.071 | 176.764180 CPU seconds | n/a |
| workload total memory | MB | 2803 | 6759.627 | 5017.500 | 9439.930 | 7358.344 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
