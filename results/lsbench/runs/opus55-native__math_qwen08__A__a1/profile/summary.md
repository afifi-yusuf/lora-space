# agprof summary

- Duration: **3924.843 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **94 calls**, 94 succeeded, 0 failed, 0 interrupted, n/a reported retries, 912.445 s total wait
- Tools: **96/96 completed**, 1 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **372687** at 1.955 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 3924517.184 / 3924517.184 ms |
| LLM latency p50 / p95 | 7807.196 / 24068.795 ms |
| LLM TTFT p50 / p95 | 4823.577 / 19491.612 ms |
| LLM input / output tokens | 190 / 92848 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 94 total, 94 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1053.584 / 136981.173 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 77/77 | 76 | 1 | 0 | 634.851 ms | 112223.514 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 829.611 ms | 829.611 ms |
| generate | 5/5 | 5 | 0 | 0 | 83603.970 ms | 470445.452 ms |
| inspect | 1/1 | 1 | 0 | 0 | 1067.824 ms | 1067.824 ms |
| inspect_module_inputs | 1/1 | 1 | 0 | 0 | 451.673 ms | 451.673 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 242.840 ms | 242.840 ms |
| token_stats | 2/2 | 2 | 0 | 0 | 68860.486 ms | 122480.192 ms |
| trace | 8/8 | 8 | 0 | 0 | 16780.327 ms | 28287.478 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 16.545% | 177.352% | 647.744 s | 7307.360 MB | 12493.141 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lsb_grid_worker | 1960 |  | 3873 | 0.000% | 0.000% | 0.000 s | 3.340 MB | 3.340 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 1969 |  | 3873 | 8.669% | 176.842% | 339.510 s | 3073.033 MB | 6484.219 MB | 16338.061 MB | 22589.762 MB | 361.281250 MB | 8692.003906 MB |
| python | 2012 |  | 3873 | 0.000% | 0.000% | 0.000 s | 10.088 MB | 12.371 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 1974 |  | 3873 | 0.642% | 7.915% | 25.120 s | 1422.700 MB | 1772.219 MB | 11037.243 MB | 11041.176 MB | 4.824219 MB | 0.140625 MB |
| docker | 2367 |  | 18 | 0.410% | 2.988% | 0.070 s | 23.941 MB | 31.914 MB | 1585.666 MB | 1843.270 MB | 51.710938 MB | 0.000000 MB |
| VLLM::EngineCor | 2013 |  | 3873 | 7.216% | 44.476% | 282.410 s | 1922.330 MB | 2329.863 MB | 21242.799 MB | 21243.297 MB | 21.523438 MB | 0.027344 MB |
| docker-compose | 2377 |  | 5 | 0.498% | 0.996% | 0.020 s | 6.930 MB | 13.422 MB | 1240.395 MB | 1260.309 MB | 15.777344 MB | 0.000000 MB |
| docker-buildx | 2378 |  | 11 | 0.896% | 2.987% | 0.090 s | 13.872 MB | 41.145 MB | 1187.760 MB | 1298.477 MB | 42.000000 MB | 0.000000 MB |
| docker | 2434 |  | 5 | 0.000% | 0.000% | 0.000 s | 30.271 MB | 30.379 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |
| docker | 2516 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.711 MB | 30.711 MB | 1843.762 MB | 1843.762 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 2480 | sandbox_agent_lsb-native_0000_0000 | 3840 | 0.002% | 0.995% | 0.070 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2514 | sandbox_agent_lsb-native_0000_0000 | 3840 | 0.002% | 0.995% | 0.080 s | 1.277 MB | 1.277 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 2607 | sandbox_agent_lsb-native_0000_0000 | 3840 | 3.477% | 101.080% | 135.620 s | 53.989 MB | 100.375 MB | 963.659 MB | 972.738 MB | n/a MB | n/a MB |
| python3 | 2613 | sandbox_agent_lsb-native_0000_0000 | 29 | 4.689% | 30.838% | 1.320 s | 35.754 MB | 81.277 MB | 44.409 MB | 97.996 MB | n/a MB | n/a MB |
| python3 | 2615 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 80.523 MB | 80.523 MB | 96.543 MB | 96.543 MB | n/a MB | n/a MB |
| python3 | 2625 | sandbox_agent_lsb-native_0000_0000 | 3496 | 0.077% | 40.599% | 2.740 s | 46.165 MB | 71.266 MB | 86.353 MB | 89.789 MB | n/a MB | n/a MB |
| bash | 2636 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| wc | 2641 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.184 MB | 0.184 MB | n/a MB | n/a MB |
| bash | 2648 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.871 MB | 0.871 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 2646 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.910 MB | 2.910 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 2661 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.855 MB | 2.855 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 2844 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2845 | sandbox_agent_lsb-native_0000_0000 | 4 | 11.935% | 28.845% | 0.360 s | 15.206 MB | 21.977 MB | 1791.929 MB | 1880.727 MB | n/a MB | n/a MB |
| bash | 2860 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2862 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 994.914 MB | 994.914 MB | 1185.953 MB | 1185.953 MB | n/a MB | n/a MB |
| python | 2870 | sandbox_agent_lsb-native_0000_0000 | 12 | 174.364% | 202.220% | 19.310 s | 2691.242 MB | 3102.410 MB | 2907.138 MB | 3322.652 MB | n/a MB | n/a MB |
| bash | 2869 | sandbox_agent_lsb-native_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 2.781 MB | 2.781 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2886 | sandbox_agent_lsb-native_0000_0000 | 5 | 188.536% | 198.467% | 7.610 s | 1628.509 MB | 2386.605 MB | 1845.009 MB | 2609.043 MB | n/a MB | n/a MB |
| bash | 2884 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.988 MB | 2.988 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2900 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.016 MB | 20.016 MB | 212.074 MB | 212.074 MB | n/a MB | n/a MB |
| bash | 2898 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2909 | sandbox_agent_lsb-native_0000_0000 | 7 | 195.003% | 201.865% | 11.800 s | 2207.713 MB | 2955.074 MB | 2442.059 MB | 3177.383 MB | n/a MB | n/a MB |
| bash | 2908 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.895 MB | 2.895 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 2917 | sandbox_agent_lsb-native_0000_0000 | 119 | 0.000% | 0.000% | 0.000 s | 2.805 MB | 2.805 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2918 | sandbox_agent_lsb-native_0000_0000 | 125 | 161.164% | 205.007% | 203.800 s | 4199.754 MB | 6821.715 MB | 4572.884 MB | 7155.902 MB | n/a MB | n/a MB |
| bash | 2931 | sandbox_agent_lsb-native_0000_0000 | 133 | 0.000% | 0.000% | 0.000 s | 1.487 MB | 1.516 MB | 3.248 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 2932 | sandbox_agent_lsb-native_0000_0000 | 41 | 0.000% | 0.000% | 0.000 s | 1.441 MB | 1.453 MB | 2.851 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2933 | sandbox_agent_lsb-native_0000_0000 | 40 | 93.812% | 201.809% | 36.860 s | 1522.967 MB | 2577.594 MB | 1849.743 MB | 2927.293 MB | n/a MB | n/a MB |
| bash | 2949 | sandbox_agent_lsb-native_0000_0000 | 60 | 0.000% | 0.000% | 0.000 s | 2.875 MB | 2.875 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 2950 | sandbox_agent_lsb-native_0000_0000 | 60 | 0.000% | 0.000% | 0.000 s | 1.457 MB | 1.457 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| python | 2951 | sandbox_agent_lsb-native_0000_0000 | 92 | 191.253% | 203.542% | 175.360 s | 2190.820 MB | 2679.812 MB | 2449.417 MB | 2927.293 MB | n/a MB | n/a MB |
| bash | 2979 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.035 MB | 3.035 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2980 | sandbox_agent_lsb-native_0000_0000 | 5 | 15.607% | 25.841% | 0.630 s | 52.370 MB | 134.207 MB | 172.691 MB | 327.453 MB | n/a MB | n/a MB |
| bash | 2987 | sandbox_agent_lsb-native_0000_0000 | 99 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 2988 | sandbox_agent_lsb-native_0000_0000 | 99 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| bash | 3053 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.727 MB | 2.727 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3054 | sandbox_agent_lsb-native_0000_0000 | 3 | 133.253% | 141.249% | 2.680 s | 324.387 MB | 547.332 MB | 547.611 MB | 770.375 MB | n/a MB | n/a MB |
| python | 3066 | sandbox_agent_lsb-native_0000_0000 | 61 | 193.412% | 211.780% | 116.870 s | 2068.358 MB | 2645.898 MB | 2312.611 MB | 2882.633 MB | n/a MB | n/a MB |
| bash | 3063 | sandbox_agent_lsb-native_0000_0000 | 61 | 0.000% | 0.000% | 0.000 s | 2.984 MB | 2.984 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3081 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.695 MB | 13.695 MB | 207.285 MB | 207.285 MB | n/a MB | n/a MB |
| bash | 3080 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3098 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.648 MB | 2.648 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3099 | sandbox_agent_lsb-native_0000_0000 | 5 | 182.260% | 198.438% | 7.340 s | 902.361 MB | 1124.484 MB | 1120.436 MB | 1348.688 MB | n/a MB | n/a MB |
| bash | 3128 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3129 | sandbox_agent_lsb-native_0000_0000 | 3 | 110.626% | 112.178% | 2.230 s | 263.102 MB | 422.613 MB | 527.349 MB | 787.750 MB | n/a MB | n/a MB |
| bash | 3235 | sandbox_agent_lsb-native_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 2.875 MB | 2.875 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3238 | sandbox_agent_lsb-native_0000_0000 | 14 | 184.441% | 201.373% | 24.190 s | 1053.717 MB | 1448.680 MB | 1298.526 MB | 1719.617 MB | n/a MB | n/a MB |
| bash | 3251 | sandbox_agent_lsb-native_0000_0000 | 107 | 0.000% | 0.000% | 0.000 s | 2.992 MB | 2.992 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3252 | sandbox_agent_lsb-native_0000_0000 | 107 | 193.348% | 212.776% | 206.590 s | 2022.372 MB | 2663.984 MB | 2270.360 MB | 2946.766 MB | n/a MB | n/a MB |
| bash | 3343 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.023 MB | 3.023 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3344 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.383 MB | 13.383 MB | 207.250 MB | 207.250 MB | n/a MB | n/a MB |
| python | 3354 | sandbox_agent_lsb-native_0000_0000 | 12 | 187.720% | 200.030% | 20.810 s | 971.998 MB | 1171.254 MB | 1220.328 MB | 1445.934 MB | n/a MB | n/a MB |
| bash | 3353 | sandbox_agent_lsb-native_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3367 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.871 MB | 2.871 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3368 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 210.980 MB | 210.980 MB | 531.090 MB | 531.090 MB | n/a MB | n/a MB |
| python | 3418 | sandbox_agent_lsb-native_0000_0000 | 19 | 139.278% | 202.013% | 25.310 s | 1718.174 MB | 3943.348 MB | 2015.480 MB | 4139.332 MB | n/a MB | n/a MB |
| bash | 3417 | sandbox_agent_lsb-native_0000_0000 | 19 | 0.000% | 0.000% | 0.000 s | 2.801 MB | 2.801 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3555 | sandbox_agent_lsb-native_0000_0000 | 37 | 143.067% | 207.194% | 52.370 s | 2597.212 MB | 5046.762 MB | 2844.769 MB | 5481.504 MB | n/a MB | n/a MB |
| bash | 3553 | sandbox_agent_lsb-native_0000_0000 | 37 | 0.000% | 0.000% | 0.000 s | 2.879 MB | 2.879 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3601 | sandbox_agent_lsb-native_0000_0000 | 13 | 160.541% | 202.412% | 19.490 s | 1658.288 MB | 4239.871 MB | 1919.987 MB | 4525.777 MB | n/a MB | n/a MB |
| bash | 3599 | sandbox_agent_lsb-native_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 2.793 MB | 2.793 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3605 | sandbox_agent_lsb-native_0000_0000 | 4 | 70.434% | 71.117% | 2.140 s | 2518.504 MB | 4464.211 MB | 2825.287 MB | 4693.281 MB | n/a MB | n/a MB |
| bash | 3634 | sandbox_agent_lsb-native_0000_0000 | 62 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3635 | sandbox_agent_lsb-native_0000_0000 | 62 | 192.119% | 212.825% | 118.570 s | 1956.943 MB | 2544.703 MB | 2192.874 MB | 2846.770 MB | n/a MB | n/a MB |
| bash | 3848 | sandbox_agent_lsb-native_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.836 MB | 2.836 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3849 | sandbox_agent_lsb-native_0000_0000 | 8 | 184.418% | 201.173% | 13.000 s | 1977.826 MB | 3146.148 MB | 2312.162 MB | 4299.863 MB | n/a MB | n/a MB |
| python | 3861 | sandbox_agent_lsb-native_0000_0000 | 8 | 179.345% | 197.881% | 12.650 s | 2939.669 MB | 4025.523 MB | 3879.917 MB | 4247.668 MB | n/a MB | n/a MB |
| bash | 3859 | sandbox_agent_lsb-native_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.754 MB | 2.754 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3873 | sandbox_agent_lsb-native_0000_0000 | 4 | 194.842% | 197.829% | 5.880 s | 2260.814 MB | 2465.348 MB | 2922.215 MB | 4392.836 MB | n/a MB | n/a MB |
| bash | 3871 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.875 MB | 2.875 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3883 | sandbox_agent_lsb-native_0000_0000 | 161 | 0.000% | 0.000% | 0.000 s | 2.805 MB | 2.805 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3885 | sandbox_agent_lsb-native_0000_0000 | 161 | 197.274% | 209.877% | 318.060 s | 1937.016 MB | 2177.961 MB | 2173.130 MB | 2400.238 MB | n/a MB | n/a MB |
| python | 4164 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 33.957 MB | 33.957 MB | 224.621 MB | 224.621 MB | n/a MB | n/a MB |
| bash | 4162 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.785 MB | 2.785 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4175 | sandbox_agent_lsb-native_0000_0000 | 3 | 98.886% | 99.523% | 1.990 s | 28.491 MB | 32.383 MB | 220.137 MB | 223.656 MB | n/a MB | n/a MB |
| bash | 4174 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.855 MB | 2.855 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 4185 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.785 MB | 2.785 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4186 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.547 MB | 13.547 MB | 207.176 MB | 207.176 MB | n/a MB | n/a MB |
| bash | 4193 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.711 MB | 2.711 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4194 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.199 MB | 13.199 MB | 207.121 MB | 207.121 MB | n/a MB | n/a MB |
| python | 4211 | sandbox_agent_lsb-native_0000_0000 | 24 | 87.180% | 199.939% | 20.200 s | 4874.043 MB | 7332.996 MB | 5263.233 MB | 7545.559 MB | n/a MB | n/a MB |
| bash | 4224 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.898 MB | 2.898 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4229 | sandbox_agent_lsb-native_0000_0000 | 12 | 147.632% | 202.929% | 16.370 s | 3483.080 MB | 6775.582 MB | 3937.668 MB | 6980.074 MB | n/a MB | n/a MB |
| python | 4239 | sandbox_agent_lsb-native_0000_0000 | 12 | 151.019% | 201.264% | 16.960 s | 2786.429 MB | 5848.977 MB | 3070.929 MB | 6205.359 MB | n/a MB | n/a MB |
| python | 4256 | sandbox_agent_lsb-native_0000_0000 | 157 | 197.505% | 204.921% | 310.510 s | 2491.873 MB | 2668.180 MB | 2721.577 MB | 2889.562 MB | n/a MB | n/a MB |
| grep | 4290 | sandbox_agent_lsb-native_0000_0000 | 158 | 0.000% | 0.000% | 0.000 s | 1.668 MB | 1.668 MB | 3.629 MB | 3.629 MB | n/a MB | n/a MB |
| python | 4289 | sandbox_agent_lsb-native_0000_0000 | 158 | 197.057% | 211.561% | 311.750 s | 2479.379 MB | 2667.898 MB | 2716.536 MB | 2889.562 MB | n/a MB | n/a MB |
| bash | 4288 | sandbox_agent_lsb-native_0000_0000 | 314 | 0.000% | 0.000% | 0.000 s | 3.043 MB | 3.043 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4551 | sandbox_agent_lsb-native_0000_0000 | 156 | 197.720% | 211.212% | 308.890 s | 2484.110 MB | 2667.719 MB | 2723.757 MB | 2889.562 MB | n/a MB | n/a MB |
| grep | 4552 | sandbox_agent_lsb-native_0000_0000 | 156 | 0.000% | 0.000% | 0.000 s | 1.676 MB | 1.676 MB | 3.629 MB | 3.629 MB | n/a MB | n/a MB |
| python | 4620 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.797 MB | 23.797 MB | 215.645 MB | 215.645 MB | n/a MB | n/a MB |
| bash | 4619 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.934 MB | 2.934 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 4648 | sandbox_agent_lsb-native_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 2.762 MB | 2.762 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4649 | sandbox_agent_lsb-native_0000_0000 | 12 | 149.245% | 198.532% | 16.560 s | 3434.249 MB | 6913.777 MB | 3829.352 MB | 7140.383 MB | n/a MB | n/a MB |
| bash | 4664 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4665 | sandbox_agent_lsb-native_0000_0000 | 3 | 158.873% | 197.215% | 3.230 s | 1483.840 MB | 2228.930 MB | 1696.173 MB | 2448.906 MB | n/a MB | n/a MB |
| docker | 4685 |  | 1 | n/a% | n/a% | n/a s | 12.207 MB | 12.207 MB | 1625.598 MB | 1625.598 MB | n/a MB | n/a MB |
| docker | 4710 |  | 120 | 0.000% | 0.000% | 0.000 s | 29.891 MB | 29.891 MB | 1771.758 MB | 1771.758 MB | 0.042969 MB | 0.000000 MB |
| docker | 4731 |  | 119 | 0.000% | 0.000% | 0.000 s | 30.082 MB | 30.082 MB | 1907.590 MB | 1907.590 MB | 0.000000 MB | 0.000000 MB |
| docker | 4771 |  | 69 | 0.000% | 0.000% | 0.000 s | 28.441 MB | 28.441 MB | 1771.195 MB | 1771.195 MB | 0.000000 MB | 0.000000 MB |
| docker | 4820 |  | 7 | 0.000% | 0.000% | 0.000 s | 30.043 MB | 30.043 MB | 1843.512 MB | 1843.512 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 24.284% | 100.000% | 12147.904 MB | 15266.000 MB | 39.049 W | 73.255 W | 153087.474 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 67.055% | 214.968% | 2599.520 s | 2151.161 MB | 9406.348 MB | 2185.714844 MB | 1200.636719 MB | 0.000668 MB | 0.000000 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2365 | 3924.523 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 1/1 | 0 | 0 | 3924.517 | 0.000 | 3924.517 | 2185.715 | 3924517.499 | 3924517.499 | 3924517.499 |
| run:write_lora_adapter | 1/1 | 0 | 0 | 3924.517 | n/a | n/a | 2185.715 | 3924517.184 | 3924517.184 | 3924517.184 |
| engine:execute | 1/1 | 0 | 0 | 3924.516 | 10.907 | 3913.405 | 2185.715 | 3924515.556 | 3924515.556 | 3924515.556 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 3546.866 | 0.002 | 3546.864 | 2139.134 | 3546866.137 | 3546866.137 | 3546866.137 |
| turn | 94/94 | 0 | 0 | 3540.221 | n/a | n/a | 2111.966 | 37661.921 | 12864.240 | 146512.491 |
| tool:bash | 77/77 | 1 | 0 | 1405.924 | n/a | n/a | 1058.666 | 18258.751 | 634.851 | 112223.514 |
| process:bash | 77/77 | 3 | 0 | 1401.984 | n/a | n/a | 1048.764 | 18207.580 | 626.195 | 111643.043 |
| tool:generate | 5/5 | 0 | 0 | 914.033 | n/a | n/a | 0.075 | 182806.642 | 83603.970 | 470445.452 |
| llm:attempt | 94/94 | 0 | 0 | 912.445 | 3.527 | 908.898 | 1028.711 | 9706.857 | 7807.196 | 24068.795 |
| run:container_call | 15/15 | 2 | 0 | 324.603 | 0.003 | 324.600 | 0.232 | 21640.179 | 305.830 | 120058.755 |
| teardown:commit | 1/1 | 0 | 0 | 319.402 | 0.011 | 319.391 | 0.243 | 319402.108 | 319402.108 | 319402.108 |
| sandbox:commit | 1/1 | 0 | 0 | 312.423 | 0.009 | 312.414 | 0.243 | 312423.290 | 312423.290 | 312423.290 |
| checkpoint.total | 1/1 | 0 | 0 | 312.423 | 0.009 | 312.414 | 0.243 | 312423.154 | 312423.154 | 312423.154 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 312.423 | 0.009 | 312.414 | 0.242 | 312422.985 | 312422.985 | 312422.985 |
| tool:token_stats | 2/2 | 0 | 0 | 137.721 | n/a | n/a | 9.396 | 68860.486 | 68860.486 | 122480.192 |
| tool:trace | 8/8 | 0 | 0 | 136.599 | n/a | n/a | 0.480 | 17074.825 | 16780.327 | 28287.478 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 39.134 | 7.916 | 31.217 | 45.840 | 39133.909 | 39133.909 | 39133.909 |
| runtime.harness_start | 1/1 | 0 | 0 | 39.134 | 7.916 | 31.217 | 45.840 | 39133.691 | 39133.691 | 39133.691 |
| sandbox:create | 1/1 | 0 | 0 | 18.311 | 0.242 | 18.069 | 0.000 | 18311.006 | 18311.006 | 18311.006 |
| run:detect | 1/1 | 0 | 0 | 17.645 | 0.001 | 17.644 | 0.000 | 17645.011 | 17645.011 | 17645.011 |
| sandbox:start | 1/1 | 0 | 0 | 7.255 | 0.002 | 7.253 | 0.000 | 7255.142 | 7255.142 | 7255.142 |
| runtime.container_create | 1/1 | 0 | 0 | 7.255 | 0.002 | 7.253 | 0.000 | 7255.001 | 7255.001 | 7255.001 |
| sandbox:stop | 1/1 | 0 | 0 | 6.979 | 0.002 | 6.977 | 0.000 | 6978.586 | 6978.586 | 6978.586 |
| syscall:sendto | 1693/1693 | 0 | 0 | 5.006 | n/a | n/a | 3.690 | 2.957 | 2.114 | 4.772 |
| syscall:execve | 286/286 | 0 | 0 | 1.859 | n/a | n/a | 1.983 | 6.500 | 1.216 | 5.925 |
| syscall:connect | 486/486 | 0 | 0 | 1.645 | n/a | n/a | 2.543 | 3.385 | 2.111 | 5.782 |
| tool:inspect | 1/1 | 0 | 0 | 1.068 | n/a | n/a | 0.007 | 1067.824 | 1067.824 | 1067.824 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.830 | n/a | n/a | 0.003 | 829.611 | 829.611 | 829.611 |
| agency:services_start | 1/1 | 0 | 0 | 0.553 | 0.044 | 0.508 | 0.000 | 552.628 | 552.628 | 552.628 |
| tool:inspect_module_inputs | 1/1 | 0 | 0 | 0.452 | n/a | n/a | 0.000 | 451.673 | 451.673 | 451.673 |
| tool:submit_output | 1/1 | 0 | 0 | 0.243 | n/a | n/a | 0.002 | 242.840 | 242.840 | 242.840 |
| agent:create | 1/1 | 0 | 0 | 0.222 | 0.010 | 0.212 | 0.000 | 221.592 | 221.592 | 221.592 |
| agency:services_close | 1/1 | 0 | 0 | 0.146 | 0.001 | 0.145 | 0.366 | 145.544 | 145.544 | 145.544 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.004 | 1.527 | 1.527 | 1.527 |
| sync:container | 15/15 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.085 | 0.070 | 0.162 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.218 | 1.218 | 1.218 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.171 | 0.171 | 0.171 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.077 | 0.077 | 0.077 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 3846 | 1.922 | 0.037 | 225.482 | 0.051 | 74.432603 CPU seconds | n/a |
| GPU 0 memory | MB | 3873 | 12147.904 | 11670.000 | 15266.000 | 12134.000 | n/a | n/a |
| GPU 0 power | W | 3873 | 39.049 | 27.670 | 73.255 | 27.966 | n/a | 153087.474 J |
| GPU 0 proc / 1969-23311 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c memory | MB | 3873 | 3389.707 | 3118.000 | 6508.000 | 3324.000 | n/a | n/a |
| GPU 0 proc / 1969-23311 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c estimated power | W | 2784 | 2.961 | 0.000 | 72.295 | 0.000 | n/a | n/a |
| GPU 0 proc / 1969-23311 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c utilization | percent | 2784 | 2.774 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2013-42192 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c memory | MB | 3873 | 8276.197 | 8070.000 | 8328.000 | 8328.000 | n/a | n/a |
| GPU 0 proc / 2013-42192 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c estimated power | W | 1012 | 59.156 | 0.000 | 72.763 | 0.000 | n/a | n/a |
| GPU 0 proc / 2013-42192 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c utilization | percent | 1012 | 81.944 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 3873 | 11665.904 | 11188.000 | 14784.000 | 11652.000 | n/a | n/a |
| GPU 0 utilization | percent | 3873 | 24.284 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 3873 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 3872 | 14.957 | 0.008 | 72.698 | 0.434 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 3872 | 21.378 | 0.251 | 70.781 | 1.508 | n/a | n/a |
| host disk_read_mb_s | MB/s | 3872 | 1.113 | 0.000 | 246.711 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 3872 | 3.999 | 0.000 | 249.019 | 124.922 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 3872 | 9.773 | 0.000 | 98.214 | 92.764 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 3872 | 10.060 | 0.000 | 98.961 | 93.589 | n/a | n/a |
| host mem_total_mb | MB | 3873 | 15363.539 | 15363.539 | 15363.539 | 15363.539 | n/a | n/a |
| host mem_used_mb | MB | 3873 | 7297.958 | 4889.422 | 13784.473 | 5062.273 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 3872 | 0.430 | 0.000 | 93.296 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 3872 | 0.437 | 0.000 | 93.738 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 3872 | 0.120 | 0.000 | 82.292 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 3872 | 0.007 | 0.000 | 0.559 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1960) CPU | percent | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1960) io read MB/s | MB/s | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1960) io write MB/s | MB/s | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1960) rss_mb | MB | 3873 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1960) main thread run-queue wait | percent | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1960) vms_mb | MB | 3873 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1969) CPU | percent | 3872 | 8.669 | 0.000 | 176.842 | 0.000 | 339.510000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 1969) io read MB/s | MB/s | 3872 | 0.063 | 0.000 | 100.447 | 0.000 | 361.281250 MB | n/a |
| Agency harness — python -m lsbench (PID 1969) io write MB/s | MB/s | 3872 | 2.217 | 0.000 | 994.683 | 0.023 | 8692.003906 MB | n/a |
| Agency harness — python -m lsbench (PID 1969) rss_mb | MB | 3873 | 3073.033 | 2504.887 | 6484.219 | 3187.379 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1969) main thread run-queue wait | percent | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 1969) vms_mb | MB | 3873 | 16338.061 | 13967.793 | 22589.762 | 16410.059 | n/a | n/a |
| Python — vllm (PID 1974) CPU | percent | 3872 | 0.642 | 0.000 | 7.915 | 0.000 | 25.120000 CPU seconds | n/a |
| Python — vllm (PID 1974) io read MB/s | MB/s | 3872 | 0.001 | 0.000 | 0.571 | 0.000 | 4.824219 MB | n/a |
| Python — vllm (PID 1974) io write MB/s | MB/s | 3872 | 0.000 | 0.000 | 0.008 | 0.000 | 0.140625 MB | n/a |
| Python — vllm (PID 1974) rss_mb | MB | 3873 | 1422.700 | 753.430 | 1772.219 | 757.238 | n/a | n/a |
| Python — vllm (PID 1974) main thread run-queue wait | percent | 3872 | 0.011 | 0.000 | 0.792 | 0.000 | 0.421758 run-queue seconds | n/a |
| Python — vllm (PID 1974) vms_mb | MB | 3873 | 11037.243 | 10964.156 | 11041.176 | 11039.176 | n/a | n/a |
| Python — python -c (PID 2012) CPU | percent | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2012) io read MB/s | MB/s | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2012) io write MB/s | MB/s | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2012) rss_mb | MB | 3873 | 10.088 | 5.742 | 12.371 | 5.742 | n/a | n/a |
| Python — python -c (PID 2012) main thread run-queue wait | percent | 3872 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2012) vms_mb | MB | 3873 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2013) CPU | percent | 3872 | 7.216 | 0.000 | 44.476 | 1.991 | 282.410000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2013) io read MB/s | MB/s | 3872 | 0.006 | 0.000 | 1.343 | 0.000 | 21.523438 MB | n/a |
| VLLM::EngineCore (PID 2013) io write MB/s | MB/s | 3872 | 0.000 | 0.000 | 0.004 | 0.000 | 0.027344 MB | n/a |
| VLLM::EngineCore (PID 2013) rss_mb | MB | 3873 | 1922.330 | 978.391 | 2329.863 | 992.641 | n/a | n/a |
| VLLM::EngineCore (PID 2013) main thread run-queue wait | percent | 3872 | 0.001 | 0.000 | 0.314 | 0.000 | 0.056004 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2013) vms_mb | MB | 3873 | 21242.799 | 21234.984 | 21243.297 | 21243.297 | n/a | n/a |
| docker info (PID 2367) CPU | percent | 17 | 0.410 | 0.000 | 2.988 | 0.000 | 0.070000 CPU seconds | n/a |
| docker info (PID 2367) io read MB/s | MB/s | 17 | 3.027 | 0.000 | 24.079 | 0.000 | 51.710938 MB | n/a |
| docker info (PID 2367) io write MB/s | MB/s | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker info (PID 2367) rss_mb | MB | 18 | 23.941 | 0.129 | 31.914 | 31.914 | n/a | n/a |
| docker info (PID 2367) main thread run-queue wait | percent | 17 | 0.002 | 0.000 | 0.016 | 0.000 | 0.000261 run-queue seconds | n/a |
| docker info (PID 2367) vms_mb | MB | 18 | 1585.666 | 66.910 | 1843.270 | 1843.270 | n/a | n/a |
| docker-compose (PID 2377) CPU | percent | 4 | 0.498 | 0.000 | 0.996 | 0.996 | 0.020000 CPU seconds | n/a |
| docker-compose (PID 2377) io read MB/s | MB/s | 4 | 3.926 | 2.392 | 6.673 | 6.673 | 15.777344 MB | n/a |
| docker-compose (PID 2377) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker-compose (PID 2377) rss_mb | MB | 5 | 6.930 | 1.223 | 13.422 | 13.422 | n/a | n/a |
| docker-compose (PID 2377) main thread run-queue wait | percent | 4 | 0.001 | 0.000 | 0.002 | 0.002 | 0.000032 run-queue seconds | n/a |
| docker-compose (PID 2377) vms_mb | MB | 5 | 1240.395 | 1160.988 | 1260.309 | 1260.309 | n/a | n/a |
| docker-buildx (PID 2378) CPU | percent | 10 | 0.896 | 0.000 | 2.987 | 2.987 | 0.090000 CPU seconds | n/a |
| docker-buildx (PID 2378) io read MB/s | MB/s | 10 | 4.181 | 1.249 | 10.786 | 10.786 | 42.000000 MB | n/a |
| docker-buildx (PID 2378) io write MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker-buildx (PID 2378) rss_mb | MB | 11 | 13.872 | 0.961 | 41.145 | 41.145 | n/a | n/a |
| docker-buildx (PID 2378) main thread run-queue wait | percent | 10 | 0.002 | 0.000 | 0.016 | 0.016 | 0.000239 run-queue seconds | n/a |
| docker-buildx (PID 2378) vms_mb | MB | 11 | 1187.760 | 99.875 | 1298.477 | 1298.477 | n/a | n/a |
| docker run (PID 2434) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker run (PID 2434) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker run (PID 2434) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker run (PID 2434) rss_mb | MB | 5 | 30.271 | 30.109 | 30.379 | 30.379 | n/a | n/a |
| docker run (PID 2434) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000013 run-queue seconds | n/a |
| docker run (PID 2434) vms_mb | MB | 5 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2480) CPU | percent | 3839 | 0.002 | 0.000 | 0.995 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2480) rss_mb | MB | 3840 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2480) main thread run-queue wait | percent | 3839 | 0.010 | 0.000 | 5.281 | 0.000 | 0.369433 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2480) vms_mb | MB | 3840 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2514) CPU | percent | 3839 | 0.002 | 0.000 | 0.995 | 0.000 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2514) rss_mb | MB | 3840 | 1.277 | 1.277 | 1.277 | 1.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2514) main thread run-queue wait | percent | 3839 | 0.012 | 0.000 | 5.210 | 0.000 | 0.470101 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2514) vms_mb | MB | 3840 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| docker exec (PID 2516) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker exec (PID 2516) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker exec (PID 2516) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker exec (PID 2516) rss_mb | MB | 2 | 30.711 | 30.711 | 30.711 | 30.711 | n/a | n/a |
| docker exec (PID 2516) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker exec (PID 2516) vms_mb | MB | 2 | 1843.762 | 1843.762 | 1843.762 | 1843.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2607) CPU | percent | 3839 | 3.477 | 0.000 | 101.080 | 0.000 | 135.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2607) rss_mb | MB | 3840 | 53.989 | 2.875 | 100.375 | 47.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2607) main thread run-queue wait | percent | 3839 | 0.000 | 0.000 | 0.010 | 0.000 | 0.000124 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2607) vms_mb | MB | 3840 | 963.659 | 4.258 | 972.738 | 972.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2613) CPU | percent | 28 | 4.689 | 0.000 | 30.838 | 0.995 | 1.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2613) rss_mb | MB | 29 | 35.754 | 0.129 | 81.277 | 81.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2613) main thread run-queue wait | percent | 28 | 0.004 | 0.000 | 0.051 | 0.005 | 0.001081 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2613) vms_mb | MB | 29 | 44.409 | 0.395 | 97.996 | 97.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2615) rss_mb | MB | 1 | 80.523 | 80.523 | 80.523 | 80.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2615) vms_mb | MB | 1 | 96.543 | 96.543 | 96.543 | 96.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2625) CPU | percent | 3495 | 0.077 | 0.000 | 40.599 | 6.913 | 2.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2625) rss_mb | MB | 3496 | 46.165 | 19.320 | 71.266 | 63.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2625) main thread run-queue wait | percent | 3495 | 0.021 | 0.000 | 16.976 | 0.108 | 0.744028 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2625) vms_mb | MB | 3496 | 86.353 | 52.504 | 89.789 | 87.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2636) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2636) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wc (PID 2641) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wc (PID 2641) vms_mb | MB | 1 | 0.184 | 0.184 | 0.184 | 0.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2646) rss_mb | MB | 1 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2646) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2648) rss_mb | MB | 1 | 0.871 | 0.871 | 0.871 | 0.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2648) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash p0s.json (PID 2661) rss_mb | MB | 1 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash p0s.json (PID 2661) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2844) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2844) rss_mb | MB | 4 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2844) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2844) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2845) CPU | percent | 3 | 11.935 | 0.994 | 28.845 | 5.968 | 0.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2845) rss_mb | MB | 4 | 15.206 | 11.305 | 21.977 | 21.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2845) main thread run-queue wait | percent | 3 | 0.819 | 0.002 | 2.449 | 0.007 | 0.024713 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2845) vms_mb | MB | 4 | 1791.929 | 1690.594 | 1880.727 | 1880.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2860) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2860) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2862) rss_mb | MB | 1 | 994.914 | 994.914 | 994.914 | 994.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2862) vms_mb | MB | 1 | 1185.953 | 1185.953 | 1185.953 | 1185.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2869) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2869) rss_mb | MB | 12 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2869) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2869) vms_mb | MB | 12 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2870) CPU | percent | 11 | 174.364 | 0.994 | 202.220 | 178.884 | 19.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2870) rss_mb | MB | 12 | 2691.242 | 1125.238 | 3102.410 | 2118.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2870) main thread run-queue wait | percent | 11 | 42.567 | 0.000 | 51.069 | 40.728 | 4.714223 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2870) vms_mb | MB | 12 | 2907.138 | 1321.570 | 3322.652 | 2338.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2884) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2884) rss_mb | MB | 5 | 2.988 | 2.988 | 2.988 | 2.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2884) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2884) vms_mb | MB | 5 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2886) CPU | percent | 4 | 188.536 | 173.971 | 198.467 | 197.889 | 7.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2886) rss_mb | MB | 5 | 1628.509 | 112.512 | 2386.605 | 2386.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2886) main thread run-queue wait | percent | 4 | 41.834 | 30.816 | 50.401 | 50.401 | 1.689180 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2886) vms_mb | MB | 5 | 1845.009 | 304.516 | 2609.043 | 2609.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2898) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2898) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2900) rss_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2900) vms_mb | MB | 1 | 212.074 | 212.074 | 212.074 | 212.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2908) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2908) rss_mb | MB | 7 | 2.895 | 2.895 | 2.895 | 2.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2908) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2908) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2909) CPU | percent | 6 | 195.003 | 178.814 | 201.865 | 197.960 | 11.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2909) rss_mb | MB | 7 | 2207.713 | 1133.969 | 2955.074 | 2955.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2909) main thread run-queue wait | percent | 6 | 45.768 | 30.251 | 50.656 | 50.384 | 2.769762 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2909) vms_mb | MB | 7 | 2442.059 | 1440.293 | 3177.383 | 3177.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2917) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2917) rss_mb | MB | 119 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2917) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2917) vms_mb | MB | 119 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2918) CPU | percent | 124 | 161.164 | 0.000 | 205.007 | 4.963 | 203.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2918) rss_mb | MB | 125 | 4199.754 | 67.281 | 6821.715 | 67.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2918) main thread run-queue wait | percent | 124 | 37.490 | 0.000 | 55.809 | 0.011 | 47.375292 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2918) vms_mb | MB | 125 | 4572.884 | 148.707 | 7155.902 | 148.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2931) CPU | percent | 132 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2931) rss_mb | MB | 133 | 1.487 | 1.422 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2931) main thread run-queue wait | percent | 132 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000006 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2931) vms_mb | MB | 133 | 3.248 | 2.816 | 4.215 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2932) CPU | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2932) rss_mb | MB | 41 | 1.441 | 0.965 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2932) main thread run-queue wait | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2932) vms_mb | MB | 41 | 2.851 | 2.816 | 4.215 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — thinkprob.py (PID 2933) CPU | percent | 39 | 93.812 | 0.000 | 201.809 | 198.805 | 36.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — thinkprob.py (PID 2933) rss_mb | MB | 40 | 1522.967 | 148.180 | 2577.594 | 2067.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — thinkprob.py (PID 2933) main thread run-queue wait | percent | 39 | 21.216 | 0.000 | 54.771 | 48.115 | 8.336288 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — thinkprob.py (PID 2933) vms_mb | MB | 40 | 1849.743 | 341.484 | 2927.293 | 2290.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2949) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2949) rss_mb | MB | 60 | 2.875 | 2.875 | 2.875 | 2.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2949) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2949) vms_mb | MB | 60 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2950) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2950) rss_mb | MB | 60 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2950) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2950) vms_mb | MB | 60 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — thinkprob.py (PID 2951) CPU | percent | 91 | 191.253 | 145.106 | 203.542 | 197.848 | 175.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — thinkprob.py (PID 2951) rss_mb | MB | 92 | 2190.820 | 500.402 | 2679.812 | 2143.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — thinkprob.py (PID 2951) main thread run-queue wait | percent | 91 | 45.130 | 33.597 | 55.373 | 48.705 | 41.378660 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — thinkprob.py (PID 2951) vms_mb | MB | 92 | 2449.417 | 1311.488 | 2927.293 | 2365.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2979) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2979) rss_mb | MB | 5 | 3.035 | 3.035 | 3.035 | 3.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2979) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2979) vms_mb | MB | 5 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2980) CPU | percent | 4 | 15.607 | 1.987 | 25.841 | 24.662 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2980) rss_mb | MB | 5 | 52.370 | 7.133 | 134.207 | 134.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2980) main thread run-queue wait | percent | 4 | 58.004 | 37.017 | 78.995 | 78.995 | 2.340621 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2980) vms_mb | MB | 5 | 172.691 | 11.785 | 327.453 | 327.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2987) CPU | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2987) rss_mb | MB | 99 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2987) main thread run-queue wait | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2987) vms_mb | MB | 99 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2988) CPU | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2988) rss_mb | MB | 99 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2988) main thread run-queue wait | percent | 98 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2988) vms_mb | MB | 99 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3053) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3053) rss_mb | MB | 3 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3053) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3053) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3054) CPU | percent | 2 | 133.253 | 125.256 | 141.249 | 141.249 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3054) rss_mb | MB | 3 | 324.387 | 28.527 | 547.332 | 28.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3054) main thread run-queue wait | percent | 2 | 17.992 | 11.602 | 24.383 | 24.383 | 0.361831 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3054) vms_mb | MB | 3 | 547.611 | 251.453 | 770.375 | 251.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3063) CPU | percent | 60 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3063) rss_mb | MB | 61 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3063) main thread run-queue wait | percent | 60 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3063) vms_mb | MB | 61 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3066) CPU | percent | 60 | 193.412 | 170.094 | 211.780 | 197.885 | 116.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3066) rss_mb | MB | 61 | 2068.358 | 1059.586 | 2645.898 | 2019.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3066) main thread run-queue wait | percent | 60 | 44.994 | 34.041 | 54.988 | 50.400 | 27.188549 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3066) vms_mb | MB | 61 | 2312.611 | 1251.633 | 2882.633 | 2240.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3080) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3080) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3081) rss_mb | MB | 1 | 13.695 | 13.695 | 13.695 | 13.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3081) vms_mb | MB | 1 | 207.285 | 207.285 | 207.285 | 207.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3098) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3098) rss_mb | MB | 5 | 2.648 | 2.648 | 2.648 | 2.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3098) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3098) vms_mb | MB | 5 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3099) CPU | percent | 4 | 182.260 | 134.814 | 198.438 | 197.871 | 7.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3099) rss_mb | MB | 5 | 902.361 | 14.117 | 1124.484 | 1124.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3099) main thread run-queue wait | percent | 4 | 42.179 | 20.824 | 49.670 | 48.960 | 1.698399 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3099) vms_mb | MB | 5 | 1120.436 | 207.430 | 1348.688 | 1348.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3128) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3128) rss_mb | MB | 3 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3128) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3128) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3129) CPU | percent | 2 | 110.626 | 109.074 | 112.178 | 112.178 | 2.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3129) rss_mb | MB | 3 | 263.102 | 13.441 | 422.613 | 353.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3129) main thread run-queue wait | percent | 2 | 23.794 | 23.178 | 24.410 | 24.410 | 0.479633 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3129) vms_mb | MB | 3 | 527.349 | 207.223 | 787.750 | 587.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3235) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3235) rss_mb | MB | 14 | 2.875 | 2.875 | 2.875 | 2.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3235) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3235) vms_mb | MB | 14 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3238) CPU | percent | 13 | 184.441 | 144.540 | 201.373 | 200.349 | 24.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3238) rss_mb | MB | 14 | 1053.717 | 95.867 | 1448.680 | 680.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3238) main thread run-queue wait | percent | 13 | 39.896 | 24.306 | 52.691 | 45.839 | 5.231862 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3238) vms_mb | MB | 14 | 1298.526 | 517.828 | 1719.617 | 892.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3251) CPU | percent | 106 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3251) rss_mb | MB | 107 | 2.992 | 2.992 | 2.992 | 2.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3251) main thread run-queue wait | percent | 106 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3251) vms_mb | MB | 107 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3252) CPU | percent | 106 | 193.348 | 123.336 | 212.776 | 197.979 | 206.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3252) rss_mb | MB | 107 | 2022.372 | 13.824 | 2663.984 | 2194.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3252) main thread run-queue wait | percent | 106 | 44.805 | 13.207 | 54.999 | 49.611 | 47.871976 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3252) vms_mb | MB | 107 | 2270.360 | 207.277 | 2946.766 | 2416.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3343) rss_mb | MB | 1 | 3.023 | 3.023 | 3.023 | 3.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3343) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3344) rss_mb | MB | 1 | 13.383 | 13.383 | 13.383 | 13.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3344) vms_mb | MB | 1 | 207.250 | 207.250 | 207.250 | 207.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3353) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3353) rss_mb | MB | 12 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3353) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3353) vms_mb | MB | 12 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3354) CPU | percent | 11 | 187.720 | 145.819 | 200.030 | 188.932 | 20.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3354) rss_mb | MB | 12 | 971.998 | 588.520 | 1171.254 | 1171.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3354) main thread run-queue wait | percent | 11 | 42.671 | 26.173 | 50.278 | 44.670 | 4.730118 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3354) vms_mb | MB | 12 | 1220.328 | 802.723 | 1445.934 | 1385.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3367) rss_mb | MB | 1 | 2.871 | 2.871 | 2.871 | 2.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3367) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3368) rss_mb | MB | 1 | 210.980 | 210.980 | 210.980 | 210.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3368) vms_mb | MB | 1 | 531.090 | 531.090 | 531.090 | 531.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3417) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3417) rss_mb | MB | 19 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3417) main thread run-queue wait | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3417) vms_mb | MB | 19 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3418) CPU | percent | 18 | 139.278 | 39.639 | 202.013 | 200.048 | 25.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3418) rss_mb | MB | 19 | 1718.174 | 340.102 | 3943.348 | 913.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3418) main thread run-queue wait | percent | 18 | 27.410 | 0.037 | 52.889 | 50.780 | 4.982595 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3418) vms_mb | MB | 19 | 2015.480 | 815.602 | 4139.332 | 1127.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3553) CPU | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3553) rss_mb | MB | 37 | 2.879 | 2.879 | 2.879 | 2.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3553) main thread run-queue wait | percent | 36 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3553) vms_mb | MB | 37 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3555) CPU | percent | 36 | 143.067 | 4.638 | 207.194 | 196.808 | 52.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3555) rss_mb | MB | 37 | 2597.212 | 427.398 | 5046.762 | 1459.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3555) main thread run-queue wait | percent | 36 | 32.776 | 0.006 | 53.772 | 44.530 | 11.978424 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3555) vms_mb | MB | 37 | 2844.769 | 815.551 | 5481.504 | 1673.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3599) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3599) rss_mb | MB | 17 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3599) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3599) vms_mb | MB | 17 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sched.py (PID 3601) CPU | percent | 12 | 160.541 | 70.238 | 202.412 | 200.719 | 19.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sched.py (PID 3601) rss_mb | MB | 13 | 1658.288 | 340.668 | 4239.871 | 1558.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sched.py (PID 3601) main thread run-queue wait | percent | 12 | 33.955 | 0.082 | 55.358 | 41.692 | 4.120783 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sched.py (PID 3601) vms_mb | MB | 13 | 1919.987 | 815.582 | 4525.777 | 1770.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3605) CPU | percent | 3 | 70.434 | 69.116 | 71.117 | 71.117 | 2.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3605) rss_mb | MB | 4 | 2518.504 | 549.902 | 4464.211 | 4464.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3605) main thread run-queue wait | percent | 3 | 0.083 | 0.067 | 0.091 | 0.091 | 0.002507 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3605) vms_mb | MB | 4 | 2825.287 | 815.578 | 4693.281 | 4693.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3634) CPU | percent | 61 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3634) rss_mb | MB | 62 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3634) main thread run-queue wait | percent | 61 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3634) vms_mb | MB | 62 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3635) CPU | percent | 61 | 192.119 | 112.371 | 212.825 | 171.985 | 118.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3635) rss_mb | MB | 62 | 1956.943 | 90.328 | 2544.703 | 90.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3635) main thread run-queue wait | percent | 61 | 44.456 | 18.218 | 55.099 | 40.245 | 27.427912 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3635) vms_mb | MB | 62 | 2192.874 | 311.891 | 2846.770 | 311.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3848) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3848) rss_mb | MB | 8 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3848) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3848) vms_mb | MB | 8 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3849) CPU | percent | 7 | 184.418 | 123.897 | 201.173 | 197.558 | 13.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3849) rss_mb | MB | 8 | 1977.826 | 13.445 | 3146.148 | 2140.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3849) main thread run-queue wait | percent | 7 | 36.187 | 16.572 | 49.751 | 25.577 | 2.550969 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3849) vms_mb | MB | 8 | 2312.162 | 207.246 | 4299.863 | 2359.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3859) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3859) rss_mb | MB | 8 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3859) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3859) vms_mb | MB | 8 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3861) CPU | percent | 7 | 179.345 | 117.242 | 197.881 | 185.928 | 12.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3861) rss_mb | MB | 8 | 2939.669 | 959.547 | 4025.523 | 3931.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3861) main thread run-queue wait | percent | 7 | 20.530 | 6.029 | 24.210 | 23.439 | 1.447766 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3861) vms_mb | MB | 8 | 3879.917 | 1305.660 | 4247.668 | 4247.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3871) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3871) rss_mb | MB | 4 | 2.875 | 2.875 | 2.875 | 2.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3871) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3871) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3873) CPU | percent | 3 | 194.842 | 189.801 | 197.829 | 196.895 | 5.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3873) rss_mb | MB | 4 | 2260.814 | 2117.117 | 2465.348 | 2465.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3873) main thread run-queue wait | percent | 3 | 42.752 | 40.638 | 46.596 | 46.596 | 1.290183 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3873) vms_mb | MB | 4 | 2922.215 | 2396.043 | 4392.836 | 4392.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3883) CPU | percent | 160 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3883) rss_mb | MB | 161 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3883) main thread run-queue wait | percent | 160 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3883) vms_mb | MB | 161 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3885) CPU | percent | 160 | 197.274 | 81.520 | 209.877 | 201.851 | 318.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3885) rss_mb | MB | 161 | 1937.016 | 7.566 | 2177.961 | 2052.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3885) main thread run-queue wait | percent | 160 | 46.741 | 11.696 | 55.386 | 50.512 | 75.358008 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3885) vms_mb | MB | 161 | 2173.130 | 11.918 | 2400.238 | 2275.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4162) rss_mb | MB | 1 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4162) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4164) rss_mb | MB | 1 | 33.957 | 33.957 | 33.957 | 33.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4164) vms_mb | MB | 1 | 224.621 | 224.621 | 224.621 | 224.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4174) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4174) rss_mb | MB | 3 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4174) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4174) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4175) CPU | percent | 2 | 98.886 | 98.248 | 99.523 | 99.523 | 1.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4175) rss_mb | MB | 3 | 28.491 | 21.176 | 32.383 | 32.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4175) main thread run-queue wait | percent | 2 | 0.006 | 0.003 | 0.010 | 0.003 | 0.000130 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4175) vms_mb | MB | 3 | 220.137 | 213.625 | 223.656 | 223.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4185) rss_mb | MB | 1 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4185) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4186) rss_mb | MB | 1 | 13.547 | 13.547 | 13.547 | 13.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4186) vms_mb | MB | 1 | 207.176 | 207.176 | 207.176 | 207.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4193) rss_mb | MB | 1 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4193) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4194) rss_mb | MB | 1 | 13.199 | 13.199 | 13.199 | 13.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4194) vms_mb | MB | 1 | 207.121 | 207.121 | 207.121 | 207.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4211) CPU | percent | 23 | 87.180 | 22.825 | 199.939 | 184.146 | 20.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4211) rss_mb | MB | 24 | 4874.043 | 96.148 | 7332.996 | 4234.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4211) main thread run-queue wait | percent | 23 | 13.263 | 0.004 | 50.298 | 39.991 | 3.073153 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4211) vms_mb | MB | 24 | 5263.233 | 288.500 | 7545.559 | 4855.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4224) rss_mb | MB | 1 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4224) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4229) CPU | percent | 11 | 147.632 | 70.497 | 202.929 | 178.052 | 16.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4229) rss_mb | MB | 12 | 3483.080 | 823.367 | 6775.582 | 4267.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4229) main thread run-queue wait | percent | 11 | 27.620 | 0.075 | 50.114 | 41.730 | 3.063606 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4229) vms_mb | MB | 12 | 3937.668 | 1313.414 | 6980.074 | 4851.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4239) CPU | percent | 11 | 151.019 | 54.653 | 201.264 | 193.482 | 16.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4239) rss_mb | MB | 12 | 2786.429 | 184.926 | 5848.977 | 184.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4239) main thread run-queue wait | percent | 11 | 29.069 | 0.053 | 53.600 | 42.275 | 3.225360 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4239) vms_mb | MB | 12 | 3070.929 | 398.777 | 6205.359 | 398.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4256) CPU | percent | 156 | 197.505 | 102.460 | 204.921 | 201.632 | 310.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4256) rss_mb | MB | 157 | 2491.873 | 122.496 | 2668.180 | 1658.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4256) main thread run-queue wait | percent | 156 | 46.588 | 12.831 | 56.207 | 50.635 | 73.222057 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4256) vms_mb | MB | 157 | 2721.577 | 314.527 | 2889.562 | 1880.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4288) CPU | percent | 313 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4288) rss_mb | MB | 314 | 3.043 | 3.043 | 3.043 | 3.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4288) main thread run-queue wait | percent | 313 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4288) vms_mb | MB | 314 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4289) CPU | percent | 157 | 197.057 | 80.068 | 211.561 | 198.937 | 311.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4289) rss_mb | MB | 158 | 2479.379 | 13.449 | 2667.898 | 1658.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4289) main thread run-queue wait | percent | 157 | 46.752 | 5.212 | 55.403 | 50.893 | 73.961216 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4289) vms_mb | MB | 158 | 2716.536 | 207.277 | 2889.562 | 1880.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 4290) CPU | percent | 157 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 4290) rss_mb | MB | 158 | 1.668 | 1.668 | 1.668 | 1.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 4290) main thread run-queue wait | percent | 157 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 4290) vms_mb | MB | 158 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4551) CPU | percent | 155 | 197.720 | 140.895 | 211.212 | 198.856 | 308.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4551) rss_mb | MB | 156 | 2484.110 | 1118.238 | 2667.719 | 1657.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4551) main thread run-queue wait | percent | 155 | 46.708 | 21.910 | 55.532 | 41.633 | 72.959429 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — val.py (PID 4551) vms_mb | MB | 156 | 2723.757 | 1311.531 | 2889.562 | 1880.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 4552) CPU | percent | 155 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 4552) rss_mb | MB | 156 | 1.676 | 1.676 | 1.676 | 1.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 4552) main thread run-queue wait | percent | 155 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 4552) vms_mb | MB | 156 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4619) rss_mb | MB | 1 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4619) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4620) rss_mb | MB | 1 | 23.797 | 23.797 | 23.797 | 23.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4620) vms_mb | MB | 1 | 215.645 | 215.645 | 215.645 | 215.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4648) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4648) rss_mb | MB | 12 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4648) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4648) vms_mb | MB | 12 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4649) CPU | percent | 11 | 149.245 | 69.501 | 198.532 | 198.532 | 16.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4649) rss_mb | MB | 12 | 3434.249 | 876.801 | 6913.777 | 2604.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4649) main thread run-queue wait | percent | 11 | 27.744 | 0.070 | 54.971 | 39.254 | 3.079367 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 4649) vms_mb | MB | 12 | 3829.352 | 1313.422 | 7140.383 | 3610.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4664) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4664) rss_mb | MB | 3 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4664) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4664) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4665) CPU | percent | 2 | 158.873 | 120.532 | 197.215 | 197.215 | 3.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4665) rss_mb | MB | 3 | 1483.840 | 12.941 | 2228.930 | 2228.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4665) main thread run-queue wait | percent | 2 | 26.675 | 12.718 | 40.632 | 40.632 | 0.541842 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4665) vms_mb | MB | 3 | 1696.173 | 206.945 | 2448.906 | 2448.906 | n/a | n/a |
| docker inspect (PID 4685) rss_mb | MB | 1 | 12.207 | 12.207 | 12.207 | 12.207 | n/a | n/a |
| docker inspect (PID 4685) vms_mb | MB | 1 | 1625.598 | 1625.598 | 1625.598 | 1625.598 | n/a | n/a |
| docker commit (PID 4710) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4710) io read MB/s | MB/s | 119 | 0.000 | 0.000 | 0.043 | 0.000 | 0.042969 MB | n/a |
| docker commit (PID 4710) io write MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4710) rss_mb | MB | 120 | 29.891 | 29.891 | 29.891 | 29.891 | n/a | n/a |
| docker commit (PID 4710) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4710) vms_mb | MB | 120 | 1771.758 | 1771.758 | 1771.758 | 1771.758 | n/a | n/a |
| docker commit (PID 4731) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4731) io read MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4731) io write MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4731) rss_mb | MB | 119 | 30.082 | 30.082 | 30.082 | 30.082 | n/a | n/a |
| docker commit (PID 4731) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4731) vms_mb | MB | 119 | 1907.590 | 1907.590 | 1907.590 | 1907.590 | n/a | n/a |
| docker commit (PID 4771) CPU | percent | 68 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4771) io read MB/s | MB/s | 68 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4771) io write MB/s | MB/s | 68 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4771) rss_mb | MB | 69 | 28.441 | 28.441 | 28.441 | 28.441 | n/a | n/a |
| docker commit (PID 4771) main thread run-queue wait | percent | 68 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4771) vms_mb | MB | 69 | 1771.195 | 1771.195 | 1771.195 | 1771.195 | n/a | n/a |
| docker stop (PID 4820) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker stop (PID 4820) io read MB/s | MB/s | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker stop (PID 4820) io write MB/s | MB/s | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker stop (PID 4820) rss_mb | MB | 7 | 30.043 | 30.043 | 30.043 | 30.043 | n/a | n/a |
| docker stop (PID 4820) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker stop (PID 4820) vms_mb | MB | 7 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 3839 | 67.055 | 0.000 | 214.968 | 0.000 | 2599.519819 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 3839 | 14.572 | 0.000 | 50.704 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 3839 | 14.734 | 0.000 | 72.329 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 3839 | 1.882 | 0.000 | 99.726 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 3839 | 1.921 | 0.000 | 99.732 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 3839 | 0.561 | 0.000 | 246.895 | 0.000 | 2185.714844 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 3839 | 0.303 | 0.000 | 206.767 | 0.000 | 1200.636719 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 3840 | 2151.161 | 7.879 | 9406.348 | 2050.074 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 3839 | 0.347 | 0.000 | 95.270 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 3839 | 0.347 | 0.000 | 95.482 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 3839 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000668 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 3839 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| workload total CPU | percent | 3872 | 16.545 | 1.277 | 177.352 | 2.142 | 647.744291 CPU seconds | n/a |
| workload total memory | MB | 3873 | 7307.360 | 4510.996 | 12493.141 | 4702.742 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
