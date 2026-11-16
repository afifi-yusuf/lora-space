# agprof summary

- Duration: **4980.446 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **93 calls**, 93 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1394.586 s total wait
- Tools: **103/103 completed**, 2 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **472851** at 1.963 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 4952957.511 / 4952957.511 ms |
| LLM latency p50 / p95 | 10460.150 / 48032.678 ms |
| LLM TTFT p50 / p95 | 4845.138 / 43319.895 ms |
| LLM input / output tokens | 188 / 138357 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 93 total, 93 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 2078.952 / 135913.060 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 74/74 | 72 | 2 | 0 | 1421.945 ms | 65437.648 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 325.067 ms | 325.067 ms |
| generate | 6/6 | 6 | 0 | 0 | 40603.100 ms | 538520.471 ms |
| get_current_resources | 1/1 | 1 | 0 | 0 | 225.445 ms | 225.445 ms |
| inspect | 2/2 | 2 | 0 | 0 | 903.293 ms | 942.989 ms |
| inspect_module_inputs | 2/2 | 2 | 0 | 0 | 848.916 ms | 862.152 ms |
| release_resource | 1/1 | 1 | 0 | 0 | 313.317 ms | 313.317 ms |
| reserve_resource | 1/1 | 1 | 0 | 0 | 280.576 ms | 280.576 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 227.902 ms | 227.902 ms |
| token_stats | 4/4 | 4 | 0 | 0 | 210578.962 ms | 503590.063 ms |
| trace | 10/10 | 10 | 0 | 0 | 20617.235 ms | 45517.831 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 55.721% | 279.296% | 2774.876 s | 13170.686 MB | 18882.016 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker | 1998 |  | 1 | n/a% | n/a% | n/a s | 29.367 MB | 29.367 MB | 2060.273 MB | 2060.273 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 1865 |  | 4942 | 6.747% | 61.427% | 336.580 s | 2334.416 MB | 2335.758 MB | 21868.615 MB | 21869.031 MB | 0.003906 MB | 0.031250 MB |
| lsb_grid_worker | 1692 |  | 4942 | 0.000% | 0.000% | 0.000 s | 3.414 MB | 3.414 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| docker-buildx | 2011 |  | 1 | n/a% | n/a% | n/a s | 39.109 MB | 39.109 MB | 1298.969 MB | 1298.969 MB | n/a MB | n/a MB |
| python | 1864 |  | 4942 | 0.000% | 0.000% | 0.000 s | 12.184 MB | 12.184 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 1763 |  | 4942 | 0.590% | 7.938% | 29.460 s | 1791.696 MB | 1792.660 MB | 12027.722 MB | 12029.773 MB | 0.007812 MB | 0.175781 MB |
| python | 1701 |  | 4942 | 48.374% | 277.062% | 2408.300 s | 2855.612 MB | 6372.719 MB | 17081.092 MB | 22538.590 MB | 170.476562 MB | 16419.984375 MB |
| tail | 2190 | sandbox_agent_lsb-native_0000_0000 | 4914 | 0.029% | 67.615% | 1.430 s | 0.932 MB | 1.312 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 2300 | sandbox_agent_lsb-native_0000_0000 | 3 | 57.157% | 65.624% | 1.150 s | 41.145 MB | 70.156 MB | 48.174 MB | 78.578 MB | n/a MB | n/a MB |
| bash | 2294 | sandbox_agent_lsb-native_0000_0000 | 4914 | 4.896% | 392.476% | 242.200 s | 95.689 MB | 102.746 MB | 970.094 MB | 972.973 MB | n/a MB | n/a MB |
| docker-init | 2148 | sandbox_agent_lsb-native_0000_0000 | 4914 | 0.002% | 0.995% | 0.090 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 2308 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.672 MB | 1.672 MB | 3.719 MB | 3.719 MB | n/a MB | n/a MB |
| python3 | 2312 | sandbox_agent_lsb-native_0000_0000 | 4885 | 0.061% | 20.883% | 2.990 s | 66.172 MB | 72.078 MB | 86.239 MB | 89.637 MB | n/a MB | n/a MB |
| bash | 2810 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.723 MB | 2.723 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2811 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| python | 2815 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 24.543 MB | 24.543 MB | 2049.355 MB | 2049.355 MB | n/a MB | n/a MB |
| python | 2866 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.242 MB | 20.242 MB | 372.207 MB | 372.207 MB | n/a MB | n/a MB |
| python | 2882 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1269.238 MB | 1269.238 MB | 1891.992 MB | 1891.992 MB | n/a MB | n/a MB |
| bash | 2901 | sandbox_agent_lsb-native_0000_0000 | 426 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 2902 | sandbox_agent_lsb-native_0000_0000 | 45 | 0.000% | 0.000% | 0.000 s | 1.473 MB | 1.473 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| python | 2903 | sandbox_agent_lsb-native_0000_0000 | 304 | 277.983% | 430.602% | 848.530 s | 3783.082 MB | 4697.812 MB | 4320.252 MB | 5090.980 MB | n/a MB | n/a MB |
| bash | 2897 | sandbox_agent_lsb-native_0000_0000 | 45 | 0.000% | 0.000% | 0.000 s | 3.000 MB | 3.000 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3045 | sandbox_agent_lsb-native_0000_0000 | 122 | 281.341% | 424.593% | 342.810 s | 3598.549 MB | 4563.785 MB | 4122.153 MB | 5068.707 MB | n/a MB | n/a MB |
| python | 3263 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.688 MB | 11.688 MB | 15.973 MB | 15.973 MB | n/a MB | n/a MB |
| bash | 3262 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.852 MB | 2.852 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 3352 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| bash | 3347 | sandbox_agent_lsb-native_0000_0000 | 2 | 1.968% | 1.968% | 0.020 s | 5.670 MB | 8.367 MB | 8.682 MB | 13.148 MB | n/a MB | n/a MB |
| python | 3349 | sandbox_agent_lsb-native_0000_0000 | 98 | 178.105% | 354.462% | 174.070 s | 3712.750 MB | 4660.035 MB | 4214.539 MB | 5090.512 MB | n/a MB | n/a MB |
| python | 3351 | sandbox_agent_lsb-native_0000_0000 | 240 | 188.027% | 425.746% | 453.050 s | 3767.310 MB | 4704.793 MB | 4309.603 MB | 5091.902 MB | n/a MB | n/a MB |
| python | 3372 | sandbox_agent_lsb-native_0000_0000 | 2 | 2.982% | 2.982% | 0.030 s | 8.223 MB | 9.062 MB | 12.525 MB | 13.262 MB | n/a MB | n/a MB |
| sh | 3409 | sandbox_agent_lsb-native_0000_0000 | 137 | 0.000% | 0.000% | 0.000 s | 0.572 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 3410 | sandbox_agent_lsb-native_0000_0000 | 50 | 0.000% | 0.000% | 0.000 s | 0.428 MB | 1.453 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| bash | 3405 | sandbox_agent_lsb-native_0000_0000 | 50 | 0.000% | 0.000% | 0.000 s | 0.825 MB | 3.000 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3411 | sandbox_agent_lsb-native_0000_0000 | 52 | 160.631% | 361.736% | 82.580 s | 2406.929 MB | 3516.656 MB | 2904.635 MB | 4237.070 MB | n/a MB | n/a MB |
| python | 3423 | sandbox_agent_lsb-native_0000_0000 | 85 | 175.155% | 377.463% | 148.180 s | 2870.223 MB | 4344.113 MB | 3403.031 MB | 4933.996 MB | n/a MB | n/a MB |
| wc | 3505 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.820 MB | 2.820 MB | n/a MB | n/a MB |
| grep | 3504 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.836 MB | 1.836 MB | 3.629 MB | 3.629 MB | n/a MB | n/a MB |
| grep | 3503 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.773 MB | 1.773 MB | 3.629 MB | 3.629 MB | n/a MB | n/a MB |
| ps | 3502 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.137 MB | 4.137 MB | 8.281 MB | 8.281 MB | n/a MB | n/a MB |
| bash | 3500 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.891 MB | 2.891 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 3508 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.441 MB | 1.441 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| python | 3507 | sandbox_agent_lsb-native_0000_0000 | 19 | 138.944% | 249.629% | 25.220 s | 3032.896 MB | 4022.707 MB | 3481.060 MB | 5090.910 MB | n/a MB | n/a MB |
| python | 3506 | sandbox_agent_lsb-native_0000_0000 | 437 | 215.371% | 426.623% | 945.590 s | 3748.041 MB | 4700.852 MB | 4276.681 MB | 5090.520 MB | n/a MB | n/a MB |
| python | 3545 | sandbox_agent_lsb-native_0000_0000 | 8 | 28.408% | 49.733% | 2.000 s | 766.910 MB | 2279.906 MB | 1239.767 MB | 2663.047 MB | n/a MB | n/a MB |
| bash | 3543 | sandbox_agent_lsb-native_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.785 MB | 2.785 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3558 | sandbox_agent_lsb-native_0000_0000 | 38 | 194.608% | 353.396% | 72.520 s | 3447.240 MB | 4918.098 MB | 3872.410 MB | 5387.734 MB | n/a MB | n/a MB |
| python | 3577 | sandbox_agent_lsb-native_0000_0000 | 11 | 104.646% | 351.572% | 10.550 s | 819.285 MB | 2430.277 MB | 1491.499 MB | 2793.023 MB | n/a MB | n/a MB |
| python | 3600 | sandbox_agent_lsb-native_0000_0000 | 9 | 12.542% | 48.702% | 1.010 s | 531.980 MB | 1068.906 MB | 1244.681 MB | 2376.969 MB | n/a MB | n/a MB |
| bash | 3597 | sandbox_agent_lsb-native_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 3.023 MB | 3.023 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3615 | sandbox_agent_lsb-native_0000_0000 | 12 | 159.998% | 324.156% | 17.710 s | 435.233 MB | 790.398 MB | 760.063 MB | 1161.789 MB | n/a MB | n/a MB |
| bash | 3614 | sandbox_agent_lsb-native_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 3.047 MB | 3.047 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3628 | sandbox_agent_lsb-native_0000_0000 | 59 | 0.000% | 0.000% | 0.000 s | 2.926 MB | 2.926 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 3629 | sandbox_agent_lsb-native_0000_0000 | 59 | 0.000% | 0.000% | 0.000 s | 1.328 MB | 1.328 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| grep | 3681 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.793 MB | 1.793 MB | 3.629 MB | 3.629 MB | n/a MB | n/a MB |
| grep | 3682 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.797 MB | 1.797 MB | 3.629 MB | 3.629 MB | n/a MB | n/a MB |
| ps | 3680 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.090 MB | 4.090 MB | 8.281 MB | 8.281 MB | n/a MB | n/a MB |
| bash | 3676 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.758 MB | 2.758 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| awk | 3683 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.016 MB | 2.016 MB | 3.871 MB | 3.871 MB | n/a MB | n/a MB |
| bash | 3701 | sandbox_agent_lsb-native_0000_0000 | 20 | 0.000% | 0.000% | 0.000 s | 2.941 MB | 2.941 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 3703 | sandbox_agent_lsb-native_0000_0000 | 20 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| python | 3702 | sandbox_agent_lsb-native_0000_0000 | 423 | 234.546% | 414.854% | 999.040 s | 3745.529 MB | 4711.387 MB | 4248.852 MB | 5091.910 MB | n/a MB | n/a MB |
| bash | 3725 | sandbox_agent_lsb-native_0000_0000 | 33 | 0.000% | 0.000% | 0.000 s | 2.871 MB | 2.871 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3726 | sandbox_agent_lsb-native_0000_0000 | 33 | 130.743% | 301.187% | 42.150 s | 499.558 MB | 2243.176 MB | 949.940 MB | 2706.039 MB | n/a MB | n/a MB |
| python3 | 3739 | sandbox_agent_lsb-native_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 6.635 MB | 57.145 MB | 9.689 MB | 86.320 MB | n/a MB | n/a MB |
| python | 3740 | sandbox_agent_lsb-native_0000_0000 | 14 | 79.407% | 233.616% | 10.390 s | 1061.946 MB | 2398.734 MB | 1633.380 MB | 2792.902 MB | n/a MB | n/a MB |
| sleep | 3756 | sandbox_agent_lsb-native_0000_0000 | 74 | 0.000% | 0.000% | 0.000 s | 1.453 MB | 1.453 MB | 2.809 MB | 2.809 MB | n/a MB | n/a MB |
| bash | 3755 | sandbox_agent_lsb-native_0000_0000 | 74 | 0.000% | 0.000% | 0.000 s | 3.020 MB | 3.020 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3764 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.859 MB | 2.859 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| cut | 3766 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.422 MB | 1.422 MB | 2.816 MB | 2.816 MB | n/a MB | n/a MB |
| python | 3765 | sandbox_agent_lsb-native_0000_0000 | 7 | 145.640% | 219.418% | 8.810 s | 374.801 MB | 931.508 MB | 719.877 MB | 1491.027 MB | n/a MB | n/a MB |
| python | 3881 | sandbox_agent_lsb-native_0000_0000 | 78 | 175.669% | 405.303% | 136.200 s | 6469.120 MB | 11576.645 MB | 8998.175 MB | 15297.934 MB | n/a MB | n/a MB |
| bash | 3876 | sandbox_agent_lsb-native_0000_0000 | 79 | 0.000% | 0.000% | 0.000 s | 2.357 MB | 2.957 MB | 4.219 MB | 4.219 MB | n/a MB | n/a MB |
| python | 3901 | sandbox_agent_lsb-native_0000_0000 | 48 | 153.425% | 252.369% | 72.550 s | 2084.982 MB | 3095.152 MB | 2751.659 MB | 3553.926 MB | n/a MB | n/a MB |
| bash | 3900 | sandbox_agent_lsb-native_0000_0000 | 48 | 0.000% | 0.000% | 0.000 s | 2.762 MB | 2.762 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3918 | sandbox_agent_lsb-native_0000_0000 | 4 | 284.119% | 339.257% | 8.570 s | 1546.707 MB | 2131.246 MB | 1935.091 MB | 2557.887 MB | n/a MB | n/a MB |
| python | 3933 | sandbox_agent_lsb-native_0000_0000 | 8 | 347.251% | 413.566% | 24.480 s | 1186.432 MB | 1444.910 MB | 1939.721 MB | 2194.445 MB | n/a MB | n/a MB |
| bash | 3957 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.832 MB | 2.832 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3958 | sandbox_agent_lsb-native_0000_0000 | 2 | 138.243% | 138.243% | 1.390 s | 450.607 MB | 887.777 MB | 978.566 MB | 1589.879 MB | n/a MB | n/a MB |
| python | 3978 | sandbox_agent_lsb-native_0000_0000 | 6 | 365.946% | 414.648% | 18.450 s | 1203.598 MB | 1401.887 MB | 1969.496 MB | 2194.090 MB | n/a MB | n/a MB |
| bash | 3977 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 3.094 MB | 3.094 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 4002 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.930 MB | 2.930 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4003 | sandbox_agent_lsb-native_0000_0000 | 4 | 71.500% | 72.455% | 2.160 s | 451.505 MB | 891.293 MB | 1122.769 MB | 1347.879 MB | n/a MB | n/a MB |
| bash | 4023 | sandbox_agent_lsb-native_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 2.871 MB | 2.871 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4025 | sandbox_agent_lsb-native_0000_0000 | 12 | 20.069% | 76.579% | 2.220 s | 2497.892 MB | 2754.270 MB | 2872.214 MB | 3108.453 MB | n/a MB | n/a MB |
| python | 4061 | sandbox_agent_lsb-native_0000_0000 | 8 | 360.114% | 406.809% | 25.380 s | 1233.709 MB | 1435.215 MB | 2026.982 MB | 2215.586 MB | n/a MB | n/a MB |
| python | 4087 | sandbox_agent_lsb-native_0000_0000 | 2 | 129.223% | 129.223% | 1.300 s | 458.729 MB | 896.527 MB | 992.721 MB | 1611.848 MB | n/a MB | n/a MB |
| bash | 4085 | sandbox_agent_lsb-native_0000_0000 | 21 | 0.000% | 0.000% | 0.000 s | 2.738 MB | 2.738 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| tail | 4088 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.445 MB | 1.445 MB | 2.840 MB | 2.840 MB | n/a MB | n/a MB |
| python | 4103 | sandbox_agent_lsb-native_0000_0000 | 19 | 123.604% | 185.989% | 22.390 s | 1264.355 MB | 1917.766 MB | 2060.763 MB | 2296.676 MB | n/a MB | n/a MB |
| python | 4120 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 45.148 MB | 45.148 MB | 397.316 MB | 397.316 MB | n/a MB | n/a MB |
| bash | 4119 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.938 MB | 2.938 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 4149 | sandbox_agent_lsb-native_0000_0000 | 3 | 204.524% | 207.765% | 4.120 s | 152.574 MB | 383.262 MB | 673.658 MB | 1572.961 MB | n/a MB | n/a MB |
| bash | 4147 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4174 | sandbox_agent_lsb-native_0000_0000 | 2 | 188.277% | 188.277% | 1.900 s | 290.900 MB | 568.668 MB | 967.570 MB | 1567.887 MB | n/a MB | n/a MB |
| bash | 4173 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.000 MB | 3.000 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 4190 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.012 MB | 3.012 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4191 | sandbox_agent_lsb-native_0000_0000 | 3 | 217.284% | 261.605% | 4.370 s | 760.051 MB | 1379.969 MB | 1578.471 MB | 2359.336 MB | n/a MB | n/a MB |
| python | 4281 | sandbox_agent_lsb-native_0000_0000 | 9 | 10.816% | 52.722% | 0.870 s | 755.718 MB | 1911.699 MB | 1413.714 MB | 2437.090 MB | n/a MB | n/a MB |
| python | 4295 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 44.871 MB | 44.871 MB | 404.160 MB | 404.160 MB | n/a MB | n/a MB |
| python | 4309 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2055.938 MB | 2055.938 MB | 2438.145 MB | 2438.145 MB | n/a MB | n/a MB |
| sed | 4325 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.891 MB | 1.891 MB | 3.707 MB | 3.707 MB | n/a MB | n/a MB |
| bash | 4322 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.008 MB | 3.008 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4324 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2054.324 MB | 2054.324 MB | 2437.137 MB | 2437.137 MB | n/a MB | n/a MB |
| bash | 4340 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.836 MB | 2.836 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sed | 4343 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.801 MB | 1.801 MB | 3.707 MB | 3.707 MB | n/a MB | n/a MB |
| python | 4342 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1645.887 MB | 1645.887 MB | 2437.137 MB | 2437.137 MB | n/a MB | n/a MB |
| python | 4351 | sandbox_agent_lsb-native_0000_0000 | 2 | 317.006% | 317.006% | 3.190 s | 313.197 MB | 452.324 MB | 774.107 MB | 993.664 MB | n/a MB | n/a MB |
| python | 4364 | sandbox_agent_lsb-native_0000_0000 | 17 | 128.405% | 189.922% | 20.680 s | 1271.067 MB | 1837.566 MB | 2020.605 MB | 2292.227 MB | n/a MB | n/a MB |
| bash | 4363 | sandbox_agent_lsb-native_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 2.938 MB | 2.938 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4383 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.164 MB | 8.164 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| bash | 4424 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.848 MB | 2.848 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4425 | sandbox_agent_lsb-native_0000_0000 | 3 | 286.711% | 391.822% | 5.770 s | 1240.146 MB | 1979.762 MB | 2099.272 MB | 3104.188 MB | n/a MB | n/a MB |
| bash | 4464 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.781 MB | 2.781 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4465 | sandbox_agent_lsb-native_0000_0000 | 3 | 244.350% | 296.846% | 4.920 s | 819.130 MB | 1539.688 MB | 1547.906 MB | 2258.488 MB | n/a MB | n/a MB |
| python | 4480 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 68.148 MB | 68.148 MB | 450.543 MB | 450.543 MB | n/a MB | n/a MB |
| sed | 4481 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.891 MB | 1.891 MB | 3.707 MB | 3.707 MB | n/a MB | n/a MB |
| bash | 4493 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4495 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 171.352 MB | 171.352 MB | 554.484 MB | 554.484 MB | n/a MB | n/a MB |
| bash | 4510 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.754 MB | 2.754 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4511 | sandbox_agent_lsb-native_0000_0000 | 2 | 210.719% | 210.719% | 2.120 s | 400.703 MB | 552.520 MB | 1144.236 MB | 1323.504 MB | n/a MB | n/a MB |
| bash | 4534 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4535 | sandbox_agent_lsb-native_0000_0000 | 3 | 212.641% | 300.345% | 4.290 s | 950.645 MB | 1450.676 MB | 1837.188 MB | 2612.285 MB | n/a MB | n/a MB |
| docker | 4630 |  | 23 | 0.000% | 0.000% | 0.000 s | 30.207 MB | 30.207 MB | 2059.844 MB | 2059.844 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 29.914% | 100.000% | 12686.706 MB | 15118.000 MB | 44.073 W | 77.145 W | 219595.538 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 98.688% | 647.864% | 4885.743 s | 2631.247 MB | 12000.000 MB | 3823.781250 MB | 6538.695312 MB | 0.001389 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 1996 | 4980.378 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 4952.958 | n/a | n/a | 3823.781 | 4952957.511 | 4952957.511 | 4952957.511 |
| engine:execute | 1/1 | 0 | 0 | 4952.956 | 4.828 | 4948.013 | 3823.781 | 4952955.793 | 4952955.793 | 4952955.793 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 4923.616 | 0.003 | 4923.613 | 3783.513 | 4923616.222 | 4923616.222 | 4923616.222 |
| turn | 93/93 | 0 | 0 | 4919.644 | n/a | n/a | 3781.501 | 52899.397 | 18951.641 | 269017.189 |
| llm:attempt | 93/93 | 0 | 0 | 1394.586 | 3.639 | 1390.935 | 65.817 | 14995.553 | 10460.150 | 48032.678 |
| tool:generate | 6/6 | 0 | 0 | 1153.940 | n/a | n/a | 0.086 | 192323.321 | 40603.100 | 538520.471 |
| tool:bash | 74/74 | 2 | 0 | 1117.813 | n/a | n/a | 3705.295 | 15105.585 | 1421.945 | 65437.648 |
| process:bash | 74/74 | 5 | 0 | 1115.842 | n/a | n/a | 3703.729 | 15078.952 | 1414.435 | 65389.287 |
| tool:token_stats | 4/4 | 0 | 0 | 1001.418 | n/a | n/a | 1.198 | 250354.425 | 210578.962 | 503590.063 |
| tool:trace | 10/10 | 0 | 0 | 230.157 | n/a | n/a | 1.030 | 23015.684 | 20617.235 | 45517.831 |
| run:container_call | 17/17 | 0 | 0 | 23.931 | 0.003 | 23.928 | 0.082 | 1407.735 | 32.035 | 4894.139 |
| teardown:commit | 1/1 | 0 | 0 | 23.242 | 0.004 | 23.238 | 0.000 | 23241.957 | 23241.957 | 23241.957 |
| sandbox:commit | 1/1 | 0 | 0 | 23.066 | 0.002 | 23.064 | 0.000 | 23066.251 | 23066.251 | 23066.251 |
| checkpoint.total | 1/1 | 0 | 0 | 23.066 | 0.002 | 23.064 | 0.000 | 23066.106 | 23066.106 | 23066.106 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 23.066 | 0.002 | 23.064 | 0.000 | 23065.951 | 23065.951 | 23065.951 |
| syscall:sendto | 1925/1925 | 0 | 0 | 6.976 | n/a | n/a | 1.949 | 3.624 | 2.038 | 6.626 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.604 | 1.020 | 3.584 | 40.141 | 4604.042 | 4604.042 | 4604.042 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.604 | 1.020 | 3.584 | 40.141 | 4603.771 | 4603.771 | 4603.771 |
| syscall:connect | 566/566 | 0 | 0 | 1.994 | n/a | n/a | 0.734 | 3.522 | 2.179 | 6.831 |
| tool:inspect | 2/2 | 0 | 0 | 1.807 | n/a | n/a | 0.000 | 903.293 | 903.293 | 942.989 |
| syscall:execve | 349/349 | 0 | 0 | 1.752 | n/a | n/a | 1.076 | 5.019 | 1.626 | 12.851 |
| tool:inspect_module_inputs | 2/2 | 0 | 0 | 1.698 | n/a | n/a | 0.000 | 848.916 | 848.916 | 862.152 |
| sandbox:create | 1/1 | 0 | 0 | 1.183 | 0.247 | 0.937 | 0.000 | 1183.405 | 1183.405 | 1183.405 |
| run:detect | 1/1 | 0 | 0 | 0.773 | 0.001 | 0.772 | 0.000 | 772.950 | 772.950 | 772.950 |
| sandbox:start | 1/1 | 0 | 0 | 0.520 | 0.002 | 0.517 | 0.000 | 519.683 | 519.683 | 519.683 |
| runtime.container_create | 1/1 | 0 | 0 | 0.520 | 0.002 | 0.517 | 0.000 | 519.528 | 519.528 | 519.528 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.325 | n/a | n/a | 0.000 | 325.067 | 325.067 | 325.067 |
| tool:release_resource | 1/1 | 0 | 0 | 0.313 | n/a | n/a | 0.000 | 313.317 | 313.317 | 313.317 |
| tool:reserve_resource | 1/1 | 0 | 0 | 0.281 | n/a | n/a | 0.461 | 280.576 | 280.576 | 280.576 |
| tool:submit_output | 1/1 | 0 | 0 | 0.228 | n/a | n/a | 0.000 | 227.902 | 227.902 | 227.902 |
| tool:get_current_resources | 1/1 | 0 | 0 | 0.225 | n/a | n/a | 0.055 | 225.445 | 225.445 | 225.445 |
| sandbox:stop | 1/1 | 0 | 0 | 0.175 | 0.002 | 0.174 | 0.000 | 175.441 | 175.441 | 175.441 |
| agency:services_close | 1/1 | 0 | 0 | 0.107 | 0.001 | 0.106 | 0.000 | 106.538 | 106.538 | 106.538 |
| agency:services_start | 1/1 | 0 | 0 | 0.104 | 0.044 | 0.060 | 0.000 | 104.151 | 104.151 | 104.151 |
| sandbox:update_limits | 2/2 | 0 | 0 | 0.104 | 0.002 | 0.101 | 0.084 | 51.765 | 51.765 | 52.571 |
| agent:create | 1/1 | 0 | 0 | 0.052 | 0.010 | 0.041 | 0.000 | 51.765 | 51.765 | 51.765 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.943 | 1.943 | 1.943 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.240 | 1.240 | 1.240 |
| sync:container | 17/17 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.068 | 0.064 | 0.096 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.185 | 0.185 | 0.185 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.063 | 0.063 | 0.063 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 4940 | 0.254 | 0.025 | 51.692 | 0.067 | 12.645144 CPU seconds | n/a |
| GPU 0 memory | MB | 4942 | 12686.706 | 11670.000 | 15118.000 | 12328.000 | n/a | n/a |
| GPU 0 power | W | 4942 | 44.073 | 30.111 | 77.145 | 30.557 | n/a | 219595.538 J |
| GPU 0 proc / 1701-6565 / sandbox / ~ / device / GPU-427db96d-b9a4-8a05-0b4c-d2ac1b0ebf41 memory | MB | 4942 | 3912.382 | 3118.000 | 6314.000 | 3524.000 | n/a | n/a |
| GPU 0 proc / 1701-6565 / sandbox / ~ / device / GPU-427db96d-b9a4-8a05-0b4c-d2ac1b0ebf41 estimated power | W | 3390 | 12.776 | 0.000 | 76.690 | 0.000 | n/a | n/a |
| GPU 0 proc / 1701-6565 / sandbox / ~ / device / GPU-427db96d-b9a4-8a05-0b4c-d2ac1b0ebf41 utilization | percent | 3390 | 9.647 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 1865-10413 / sandbox / ~ / device / GPU-427db96d-b9a4-8a05-0b4c-d2ac1b0ebf41 memory | MB | 4942 | 8292.324 | 8070.000 | 8322.000 | 8322.000 | n/a | n/a |
| GPU 0 proc / 1865-10413 / sandbox / ~ / device / GPU-427db96d-b9a4-8a05-0b4c-d2ac1b0ebf41 estimated power | W | 1442 | 54.544 | 0.000 | 74.056 | 0.000 | n/a | n/a |
| GPU 0 proc / 1865-10413 / sandbox / ~ / device / GPU-427db96d-b9a4-8a05-0b4c-d2ac1b0ebf41 utilization | percent | 1442 | 75.620 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 4942 | 12204.706 | 11188.000 | 14636.000 | 11846.000 | n/a | n/a |
| GPU 0 utilization | percent | 4942 | 29.914 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 4942 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 4941 | 11.953 | 0.007 | 100.000 | 0.182 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 4941 | 19.255 | 0.000 | 81.445 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 4941 | 1.129 | 0.000 | 247.567 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 4941 | 4.408 | 0.000 | 244.686 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 4941 | 2.131 | 0.000 | 97.386 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 4941 | 2.215 | 0.000 | 97.896 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 4942 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 4942 | 8858.149 | 6282.176 | 19019.566 | 7170.996 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 4941 | 0.045 | 0.000 | 87.619 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 4941 | 0.045 | 0.000 | 87.763 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 4941 | 0.000 | 0.000 | 0.021 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 4941 | 0.008 | 0.000 | 0.805 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1692) CPU | percent | 4941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1692) io read MB/s | MB/s | 4941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1692) io write MB/s | MB/s | 4941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1692) rss_mb | MB | 4942 | 3.414 | 3.414 | 3.414 | 3.414 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1692) main thread run-queue wait | percent | 4941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1692) vms_mb | MB | 4942 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1701) CPU | percent | 4941 | 48.374 | 0.000 | 277.062 | 0.995 | 2408.300000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 1701) io read MB/s | MB/s | 4941 | 0.034 | 0.000 | 93.126 | 0.000 | 170.476562 MB | n/a |
| Agency harness — python -m lsbench (PID 1701) io write MB/s | MB/s | 4941 | 3.297 | 0.000 | 1145.147 | 0.035 | 16419.984375 MB | n/a |
| Agency harness — python -m lsbench (PID 1701) rss_mb | MB | 4942 | 2855.612 | 1968.121 | 6372.719 | 2989.902 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1701) main thread run-queue wait | percent | 4941 | 0.000 | 0.000 | 0.299 | 0.000 | 0.012348 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 1701) vms_mb | MB | 4942 | 17081.092 | 14062.965 | 22538.590 | 16603.582 | n/a | n/a |
| Python — vllm (PID 1763) CPU | percent | 4941 | 0.590 | 0.000 | 7.938 | 0.000 | 29.460000 CPU seconds | n/a |
| Python — vllm (PID 1763) io read MB/s | MB/s | 4941 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 1763) io write MB/s | MB/s | 4941 | 0.000 | 0.000 | 0.008 | 0.000 | 0.175781 MB | n/a |
| Python — vllm (PID 1763) rss_mb | MB | 4942 | 1791.696 | 1786.359 | 1792.660 | 1792.109 | n/a | n/a |
| Python — vllm (PID 1763) main thread run-queue wait | percent | 4941 | 0.019 | 0.000 | 5.952 | 0.000 | 0.942183 run-queue seconds | n/a |
| Python — vllm (PID 1763) vms_mb | MB | 4942 | 12027.722 | 11951.754 | 12029.773 | 12028.773 | n/a | n/a |
| Python — python -c (PID 1864) CPU | percent | 4941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 1864) io read MB/s | MB/s | 4941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1864) io write MB/s | MB/s | 4941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1864) rss_mb | MB | 4942 | 12.184 | 12.184 | 12.184 | 12.184 | n/a | n/a |
| Python — python -c (PID 1864) main thread run-queue wait | percent | 4941 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 1864) vms_mb | MB | 4942 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 1865) CPU | percent | 4941 | 6.747 | 0.000 | 61.427 | 0.995 | 336.580000 CPU seconds | n/a |
| VLLM::EngineCore (PID 1865) io read MB/s | MB/s | 4941 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 1865) io write MB/s | MB/s | 4941 | 0.000 | 0.000 | 0.004 | 0.000 | 0.031250 MB | n/a |
| VLLM::EngineCore (PID 1865) rss_mb | MB | 4942 | 2334.416 | 2326.633 | 2335.758 | 2333.277 | n/a | n/a |
| VLLM::EngineCore (PID 1865) main thread run-queue wait | percent | 4941 | 0.007 | 0.000 | 8.984 | 0.000 | 0.365986 run-queue seconds | n/a |
| VLLM::EngineCore (PID 1865) vms_mb | MB | 4942 | 21868.615 | 21860.680 | 21869.031 | 21869.031 | n/a | n/a |
| docker info (PID 1998) rss_mb | MB | 1 | 29.367 | 29.367 | 29.367 | 29.367 | n/a | n/a |
| docker info (PID 1998) vms_mb | MB | 1 | 2060.273 | 2060.273 | 2060.273 | 2060.273 | n/a | n/a |
| docker-buildx (PID 2011) rss_mb | MB | 1 | 39.109 | 39.109 | 39.109 | 39.109 | n/a | n/a |
| docker-buildx (PID 2011) vms_mb | MB | 1 | 1298.969 | 1298.969 | 1298.969 | 1298.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2148) CPU | percent | 4913 | 0.002 | 0.000 | 0.995 | 0.000 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2148) rss_mb | MB | 4914 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2148) main thread run-queue wait | percent | 4913 | 0.059 | 0.000 | 59.542 | 0.000 | 2.921152 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2148) vms_mb | MB | 4914 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2190) CPU | percent | 4913 | 0.029 | 0.000 | 67.615 | 0.000 | 1.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2190) rss_mb | MB | 4914 | 0.932 | 0.090 | 1.312 | 0.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2190) main thread run-queue wait | percent | 4913 | 0.066 | 0.000 | 114.724 | 0.000 | 3.273745 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2190) vms_mb | MB | 4914 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2294) CPU | percent | 4913 | 4.896 | 0.000 | 392.476 | 0.000 | 242.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2294) rss_mb | MB | 4914 | 95.689 | 3.008 | 102.746 | 93.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2294) main thread run-queue wait | percent | 4913 | 0.000 | 0.000 | 0.007 | 0.000 | 0.000087 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2294) vms_mb | MB | 4914 | 970.094 | 4.258 | 972.973 | 972.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2300) CPU | percent | 2 | 57.157 | 48.690 | 65.624 | 65.624 | 1.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2300) rss_mb | MB | 3 | 41.145 | 7.125 | 70.156 | 70.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2300) main thread run-queue wait | percent | 2 | 0.027 | 0.020 | 0.033 | 0.033 | 0.000539 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2300) vms_mb | MB | 3 | 48.174 | 11.809 | 78.578 | 78.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2308) rss_mb | MB | 1 | 1.672 | 1.672 | 1.672 | 1.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2308) vms_mb | MB | 1 | 3.719 | 3.719 | 3.719 | 3.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2312) CPU | percent | 4884 | 0.061 | 0.000 | 20.883 | 0.000 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2312) rss_mb | MB | 4885 | 66.172 | 52.996 | 72.078 | 63.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2312) main thread run-queue wait | percent | 4884 | 0.115 | 0.000 | 40.965 | 0.000 | 5.638515 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2312) vms_mb | MB | 4885 | 86.239 | 60.637 | 89.637 | 88.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2810) rss_mb | MB | 1 | 2.723 | 2.723 | 2.723 | 2.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2810) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python (PID 2811) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python (PID 2811) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2815) rss_mb | MB | 1 | 24.543 | 24.543 | 24.543 | 24.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2815) vms_mb | MB | 1 | 2049.355 | 2049.355 | 2049.355 | 2049.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2866) rss_mb | MB | 1 | 20.242 | 20.242 | 20.242 | 20.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2866) vms_mb | MB | 1 | 372.207 | 372.207 | 372.207 | 372.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2882) rss_mb | MB | 1 | 1269.238 | 1269.238 | 1269.238 | 1269.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2882) vms_mb | MB | 1 | 1891.992 | 1891.992 | 1891.992 | 1891.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2897) CPU | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2897) rss_mb | MB | 45 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2897) main thread run-queue wait | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2897) vms_mb | MB | 45 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2901) CPU | percent | 425 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2901) rss_mb | MB | 426 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2901) main thread run-queue wait | percent | 425 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2901) vms_mb | MB | 426 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2902) CPU | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2902) rss_mb | MB | 45 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2902) main thread run-queue wait | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 2902) vms_mb | MB | 45 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 2903) CPU | percent | 303 | 277.983 | 99.401 | 430.602 | 314.386 | 848.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 2903) rss_mb | MB | 304 | 3783.082 | 969.070 | 4697.812 | 3194.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 2903) main thread run-queue wait | percent | 303 | 28.345 | 0.002 | 55.141 | 40.278 | 86.536351 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 2903) vms_mb | MB | 304 | 4320.252 | 1407.066 | 5090.980 | 3893.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3045) CPU | percent | 121 | 281.341 | 97.470 | 424.593 | 329.033 | 342.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3045) rss_mb | MB | 122 | 3598.549 | 41.551 | 4563.785 | 3286.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3045) main thread run-queue wait | percent | 121 | 28.472 | 0.002 | 50.492 | 39.173 | 34.697621 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3045) vms_mb | MB | 122 | 4122.153 | 393.062 | 5068.707 | 3942.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3262) rss_mb | MB | 1 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3262) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grade.py (PID 3263) rss_mb | MB | 1 | 11.688 | 11.688 | 11.688 | 11.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grade.py (PID 3263) vms_mb | MB | 1 | 15.973 | 15.973 | 15.973 | 15.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3347) CPU | percent | 1 | 1.968 | 1.968 | 1.968 | 1.968 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3347) rss_mb | MB | 2 | 5.670 | 2.973 | 8.367 | 8.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3347) main thread run-queue wait | percent | 1 | 44.995 | 44.995 | 44.995 | 44.995 | 0.457156 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3347) vms_mb | MB | 2 | 8.682 | 4.215 | 13.148 | 13.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3349) CPU | percent | 97 | 178.105 | 0.000 | 354.462 | 0.000 | 174.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3349) rss_mb | MB | 98 | 3712.750 | 1800.633 | 4660.035 | 4596.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3349) main thread run-queue wait | percent | 97 | 51.681 | 0.000 | 89.040 | 0.000 | 50.551719 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3349) vms_mb | MB | 98 | 4214.539 | 2180.496 | 5090.512 | 5090.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3351) CPU | percent | 239 | 188.027 | 0.000 | 425.746 | 0.000 | 453.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3351) rss_mb | MB | 240 | 3767.310 | 0.203 | 4704.793 | 0.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3351) main thread run-queue wait | percent | 239 | 46.672 | 0.000 | 92.533 | 0.000 | 112.428900 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3351) vms_mb | MB | 240 | 4309.603 | 2180.887 | 5091.902 | 5091.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3352) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3352) vms_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3372) CPU | percent | 1 | 2.982 | 2.982 | 2.982 | 2.982 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3372) rss_mb | MB | 2 | 8.223 | 7.383 | 9.062 | 9.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3372) main thread run-queue wait | percent | 1 | 49.563 | 49.563 | 49.563 | 49.563 | 0.498626 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3372) vms_mb | MB | 2 | 12.525 | 11.789 | 13.262 | 13.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3405) CPU | percent | 49 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3405) rss_mb | MB | 50 | 0.825 | 0.348 | 3.000 | 0.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3405) main thread run-queue wait | percent | 49 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3405) vms_mb | MB | 50 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sh (PID 3409) CPU | percent | 136 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sh (PID 3409) rss_mb | MB | 137 | 0.572 | 0.121 | 1.520 | 0.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sh (PID 3409) main thread run-queue wait | percent | 136 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sh (PID 3409) vms_mb | MB | 137 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3410) CPU | percent | 49 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3410) rss_mb | MB | 50 | 0.428 | 0.203 | 1.453 | 0.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3410) main thread run-queue wait | percent | 49 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3410) vms_mb | MB | 50 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3411) CPU | percent | 51 | 160.631 | 3.966 | 361.736 | 137.123 | 82.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3411) rss_mb | MB | 52 | 2406.929 | 16.691 | 3516.656 | 1613.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3411) main thread run-queue wait | percent | 51 | 49.807 | 0.001 | 78.926 | 44.908 | 25.601386 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3411) vms_mb | MB | 52 | 2904.635 | 368.539 | 4237.070 | 2000.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3423) CPU | percent | 84 | 175.155 | 2.982 | 377.463 | 260.461 | 148.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3423) rss_mb | MB | 85 | 2870.223 | 20.684 | 4344.113 | 3270.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3423) main thread run-queue wait | percent | 84 | 44.431 | 0.000 | 75.498 | 32.530 | 37.587511 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3423) vms_mb | MB | 85 | 3403.031 | 372.578 | 4933.996 | 3649.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3500) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3500) rss_mb | MB | 3 | 2.891 | 2.891 | 2.891 | 2.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3500) main thread run-queue wait | percent | 2 | 0.124 | 0.000 | 0.248 | 0.000 | 0.002500 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3500) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ps (PID 3502) rss_mb | MB | 1 | 4.137 | 4.137 | 4.137 | 4.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ps (PID 3502) vms_mb | MB | 1 | 8.281 | 8.281 | 8.281 | 8.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 3503) rss_mb | MB | 1 | 1.773 | 1.773 | 1.773 | 1.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 3503) vms_mb | MB | 1 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 3504) rss_mb | MB | 1 | 1.836 | 1.836 | 1.836 | 1.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 3504) vms_mb | MB | 1 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wc (PID 3505) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wc (PID 3505) vms_mb | MB | 1 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3506) CPU | percent | 436 | 215.371 | 15.902 | 426.623 | 167.076 | 945.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3506) rss_mb | MB | 437 | 3748.041 | 1177.020 | 4700.852 | 3867.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3506) main thread run-queue wait | percent | 436 | 42.504 | 0.004 | 114.665 | 48.622 | 186.653973 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3506) vms_mb | MB | 437 | 4276.681 | 1663.500 | 5090.520 | 4361.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3507) CPU | percent | 18 | 138.944 | 14.902 | 249.629 | 167.466 | 25.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3507) rss_mb | MB | 19 | 3032.896 | 1175.504 | 4022.707 | 3735.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3507) main thread run-queue wait | percent | 18 | 53.167 | 0.091 | 114.721 | 82.823 | 9.651964 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3507) vms_mb | MB | 19 | 3481.060 | 1663.891 | 5090.910 | 4120.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3508) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3508) rss_mb | MB | 2 | 1.441 | 1.441 | 1.441 | 1.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3508) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3508) vms_mb | MB | 2 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3543) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3543) rss_mb | MB | 8 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3543) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3543) vms_mb | MB | 8 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3545) CPU | percent | 7 | 28.408 | 1.985 | 49.733 | 37.786 | 2.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3545) rss_mb | MB | 8 | 766.910 | 8.766 | 2279.906 | 2279.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3545) main thread run-queue wait | percent | 7 | 39.679 | 18.871 | 62.050 | 38.385 | 2.794601 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3545) vms_mb | MB | 8 | 1239.767 | 13.129 | 2663.047 | 2663.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 3558) CPU | percent | 37 | 194.608 | 1.978 | 353.396 | 226.734 | 72.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 3558) rss_mb | MB | 38 | 3447.240 | 7.211 | 4918.098 | 1935.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 3558) main thread run-queue wait | percent | 37 | 55.496 | 5.091 | 75.524 | 50.979 | 20.676096 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build.py (PID 3558) vms_mb | MB | 38 | 3872.410 | 11.785 | 5387.734 | 2306.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — det.py (PID 3577) CPU | percent | 10 | 104.646 | 3.964 | 351.572 | 97.375 | 10.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — det.py (PID 3577) rss_mb | MB | 11 | 819.285 | 23.203 | 2430.277 | 2430.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — det.py (PID 3577) main thread run-queue wait | percent | 10 | 55.091 | 8.203 | 88.348 | 26.100 | 5.557978 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — det.py (PID 3577) vms_mb | MB | 11 | 1491.499 | 375.543 | 2793.023 | 2793.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3597) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3597) rss_mb | MB | 9 | 3.023 | 3.023 | 3.023 | 3.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3597) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3597) vms_mb | MB | 9 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3600) CPU | percent | 8 | 12.542 | 2.971 | 48.702 | 3.960 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3600) rss_mb | MB | 9 | 531.980 | 6.762 | 1068.906 | 1068.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3600) main thread run-queue wait | percent | 8 | 10.364 | 1.371 | 52.625 | 5.410 | 0.834552 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3600) vms_mb | MB | 9 | 1244.681 | 11.656 | 2376.969 | 2376.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3614) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3614) rss_mb | MB | 12 | 3.047 | 3.047 | 3.047 | 3.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3614) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3614) vms_mb | MB | 12 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3615) CPU | percent | 11 | 159.998 | 0.989 | 324.156 | 134.753 | 17.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3615) rss_mb | MB | 12 | 435.233 | 6.266 | 790.398 | 595.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3615) main thread run-queue wait | percent | 11 | 54.712 | 25.186 | 74.444 | 27.271 | 6.059975 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3615) vms_mb | MB | 12 | 760.063 | 11.656 | 1161.789 | 965.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3628) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3628) rss_mb | MB | 59 | 2.926 | 2.926 | 2.926 | 2.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3628) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3628) vms_mb | MB | 59 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3629) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3629) rss_mb | MB | 59 | 1.328 | 1.328 | 1.328 | 1.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3629) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3629) vms_mb | MB | 59 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3676) rss_mb | MB | 1 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3676) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ps (PID 3680) rss_mb | MB | 1 | 4.090 | 4.090 | 4.090 | 4.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ps (PID 3680) vms_mb | MB | 1 | 8.281 | 8.281 | 8.281 | 8.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 3681) rss_mb | MB | 1 | 1.793 | 1.793 | 1.793 | 1.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 3681) vms_mb | MB | 1 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 3682) rss_mb | MB | 1 | 1.797 | 1.797 | 1.797 | 1.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 3682) vms_mb | MB | 1 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — awk (PID 3683) rss_mb | MB | 1 | 2.016 | 2.016 | 2.016 | 2.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — awk (PID 3683) vms_mb | MB | 1 | 3.871 | 3.871 | 3.871 | 3.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3701) CPU | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3701) rss_mb | MB | 20 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3701) main thread run-queue wait | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3701) vms_mb | MB | 20 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3702) CPU | percent | 422 | 234.546 | 1.987 | 414.854 | 246.680 | 999.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3702) rss_mb | MB | 423 | 3745.529 | 13.551 | 4711.387 | 3680.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3702) main thread run-queue wait | percent | 422 | 37.741 | 0.001 | 87.049 | 29.783 | 160.670570 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — logits.py (PID 3702) vms_mb | MB | 423 | 4248.852 | 367.262 | 5091.910 | 4192.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3703) CPU | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3703) rss_mb | MB | 20 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3703) main thread run-queue wait | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3703) vms_mb | MB | 20 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3725) CPU | percent | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3725) rss_mb | MB | 33 | 2.871 | 2.871 | 2.871 | 2.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3725) main thread run-queue wait | percent | 32 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3725) vms_mb | MB | 33 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3726) CPU | percent | 32 | 130.743 | 1.982 | 301.187 | 9.938 | 42.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3726) rss_mb | MB | 33 | 499.558 | 20.871 | 2243.176 | 2243.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3726) main thread run-queue wait | percent | 32 | 58.615 | 23.501 | 82.715 | 49.943 | 18.898663 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3726) vms_mb | MB | 33 | 949.940 | 372.410 | 2706.039 | 2706.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3739) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3739) rss_mb | MB | 15 | 6.635 | 3.027 | 57.145 | 3.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3739) main thread run-queue wait | percent | 14 | 0.037 | 0.000 | 0.515 | 0.000 | 0.005182 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3739) vms_mb | MB | 15 | 9.689 | 4.215 | 86.320 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3740) CPU | percent | 13 | 79.407 | 2.969 | 233.616 | 31.693 | 10.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3740) rss_mb | MB | 14 | 1061.946 | 387.750 | 2398.734 | 1280.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3740) main thread run-queue wait | percent | 13 | 58.331 | 15.240 | 87.164 | 60.982 | 7.637018 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3740) vms_mb | MB | 14 | 1633.380 | 757.090 | 2792.902 | 1643.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3755) CPU | percent | 73 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3755) rss_mb | MB | 74 | 3.020 | 3.020 | 3.020 | 3.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3755) main thread run-queue wait | percent | 73 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3755) vms_mb | MB | 74 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3756) CPU | percent | 73 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3756) rss_mb | MB | 74 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3756) main thread run-queue wait | percent | 73 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sleep (PID 3756) vms_mb | MB | 74 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3764) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3764) rss_mb | MB | 7 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3764) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3764) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — det.py (PID 3765) CPU | percent | 6 | 145.640 | 28.714 | 219.418 | 129.853 | 8.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — det.py (PID 3765) rss_mb | MB | 7 | 374.801 | 7.602 | 931.508 | 931.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — det.py (PID 3765) main thread run-queue wait | percent | 6 | 58.355 | 13.477 | 83.143 | 32.687 | 3.528866 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — det.py (PID 3765) vms_mb | MB | 7 | 719.877 | 11.918 | 1491.027 | 1491.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — cut (PID 3766) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — cut (PID 3766) rss_mb | MB | 7 | 1.422 | 1.422 | 1.422 | 1.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — cut (PID 3766) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — cut (PID 3766) vms_mb | MB | 7 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3876) CPU | percent | 78 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3876) rss_mb | MB | 79 | 2.357 | 0.324 | 2.957 | 0.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3876) main thread run-queue wait | percent | 78 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3876) vms_mb | MB | 79 | 4.219 | 4.219 | 4.219 | 4.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3881) CPU | percent | 77 | 175.669 | 0.000 | 405.303 | 11.932 | 136.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3881) rss_mb | MB | 78 | 6469.120 | 13.293 | 11576.645 | 11576.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3881) main thread run-queue wait | percent | 77 | 16.705 | 0.000 | 49.284 | 0.092 | 12.953170 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3881) vms_mb | MB | 78 | 8998.175 | 367.195 | 15297.934 | 15297.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3900) CPU | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3900) rss_mb | MB | 48 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3900) main thread run-queue wait | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3900) vms_mb | MB | 48 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3901) CPU | percent | 47 | 153.425 | 0.994 | 252.369 | 1.990 | 72.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3901) rss_mb | MB | 48 | 2084.982 | 15.496 | 3095.152 | 2394.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3901) main thread run-queue wait | percent | 47 | 10.662 | 0.000 | 21.587 | 0.000 | 5.041784 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3901) vms_mb | MB | 48 | 2751.659 | 368.414 | 3553.926 | 2772.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo.py (PID 3918) CPU | percent | 3 | 284.119 | 221.710 | 339.257 | 291.391 | 8.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo.py (PID 3918) rss_mb | MB | 4 | 1546.707 | 487.902 | 2131.246 | 1869.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo.py (PID 3918) main thread run-queue wait | percent | 3 | 29.243 | 15.370 | 36.583 | 35.775 | 0.882041 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo.py (PID 3918) vms_mb | MB | 4 | 1935.091 | 841.496 | 2557.887 | 2265.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo2.py (PID 3933) CPU | percent | 7 | 347.251 | 105.275 | 413.566 | 387.659 | 24.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo2.py (PID 3933) rss_mb | MB | 8 | 1186.432 | 29.668 | 1444.910 | 1440.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo2.py (PID 3933) main thread run-queue wait | percent | 7 | 27.988 | 4.816 | 35.264 | 35.264 | 1.973046 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo2.py (PID 3933) vms_mb | MB | 8 | 1939.721 | 728.273 | 2194.445 | 2194.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3957) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3957) rss_mb | MB | 2 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3957) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3957) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3958) CPU | percent | 1 | 138.243 | 138.243 | 138.243 | 138.243 | 1.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3958) rss_mb | MB | 2 | 450.607 | 13.438 | 887.777 | 887.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3958) main thread run-queue wait | percent | 1 | 9.180 | 9.180 | 9.180 | 9.180 | 0.092307 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3958) vms_mb | MB | 2 | 978.566 | 367.254 | 1589.879 | 1589.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3977) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3977) rss_mb | MB | 6 | 3.094 | 3.094 | 3.094 | 3.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3977) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3977) vms_mb | MB | 6 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3978) CPU | percent | 5 | 365.946 | 242.541 | 414.648 | 414.648 | 18.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3978) rss_mb | MB | 6 | 1203.598 | 363.031 | 1401.887 | 1373.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3978) main thread run-queue wait | percent | 5 | 27.733 | 17.678 | 32.800 | 31.147 | 1.398285 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3978) vms_mb | MB | 6 | 1969.496 | 1065.691 | 2194.090 | 2171.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4002) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4002) rss_mb | MB | 4 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4002) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4002) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4003) CPU | percent | 3 | 71.500 | 70.575 | 72.455 | 72.455 | 2.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4003) rss_mb | MB | 4 | 451.505 | 96.012 | 891.293 | 360.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4003) main thread run-queue wait | percent | 3 | 0.054 | 0.051 | 0.056 | 0.051 | 0.001639 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4003) vms_mb | MB | 4 | 1122.769 | 449.188 | 1347.879 | 1347.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4023) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4023) rss_mb | MB | 12 | 2.871 | 2.871 | 2.871 | 2.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4023) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4023) vms_mb | MB | 12 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4025) CPU | percent | 11 | 20.069 | 0.000 | 76.579 | 1.990 | 2.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4025) rss_mb | MB | 12 | 2497.892 | 906.145 | 2754.270 | 2754.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4025) main thread run-queue wait | percent | 11 | 0.012 | 0.000 | 0.058 | 0.000 | 0.001283 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4025) vms_mb | MB | 12 | 2872.214 | 1259.883 | 3108.453 | 3108.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo3.py (PID 4061) CPU | percent | 7 | 360.114 | 155.147 | 406.809 | 367.863 | 25.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo3.py (PID 4061) rss_mb | MB | 8 | 1233.709 | 38.789 | 1435.215 | 1389.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo3.py (PID 4061) main thread run-queue wait | percent | 7 | 30.332 | 9.154 | 39.658 | 39.658 | 2.137808 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — loo3.py (PID 4061) vms_mb | MB | 8 | 2026.982 | 739.219 | 2215.586 | 2215.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4085) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4085) rss_mb | MB | 21 | 2.738 | 2.738 | 2.738 | 2.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4085) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4085) vms_mb | MB | 21 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final.py (PID 4087) CPU | percent | 1 | 129.223 | 129.223 | 129.223 | 129.223 | 1.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final.py (PID 4087) rss_mb | MB | 2 | 458.729 | 20.930 | 896.527 | 896.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final.py (PID 4087) main thread run-queue wait | percent | 1 | 12.120 | 12.120 | 12.120 | 12.120 | 0.121933 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final.py (PID 4087) vms_mb | MB | 2 | 992.721 | 373.594 | 1611.848 | 1611.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4088) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4088) rss_mb | MB | 2 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4088) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4088) vms_mb | MB | 2 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4103) CPU | percent | 18 | 123.604 | 68.627 | 185.989 | 113.228 | 22.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4103) rss_mb | MB | 19 | 1264.355 | 22.043 | 1917.766 | 1189.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4103) main thread run-queue wait | percent | 18 | 8.990 | 0.040 | 18.211 | 7.066 | 1.628614 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4103) vms_mb | MB | 19 | 2060.763 | 373.879 | 2296.676 | 1849.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4119) rss_mb | MB | 1 | 2.938 | 2.938 | 2.938 | 2.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4119) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4120) rss_mb | MB | 1 | 45.148 | 45.148 | 45.148 | 45.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4120) vms_mb | MB | 1 | 397.316 | 397.316 | 397.316 | 397.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4147) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4147) rss_mb | MB | 3 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4147) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4147) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4149) CPU | percent | 2 | 204.524 | 201.282 | 207.765 | 207.765 | 4.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4149) rss_mb | MB | 3 | 152.574 | 0.953 | 383.262 | 73.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4149) main thread run-queue wait | percent | 2 | 10.037 | 4.392 | 15.682 | 4.392 | 0.202340 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4149) vms_mb | MB | 3 | 673.658 | 4.215 | 1572.961 | 443.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4173) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4173) rss_mb | MB | 2 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4173) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4173) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4174) CPU | percent | 1 | 188.277 | 188.277 | 188.277 | 188.277 | 1.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4174) rss_mb | MB | 2 | 290.900 | 13.133 | 568.668 | 568.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4174) main thread run-queue wait | percent | 1 | 20.527 | 20.527 | 20.527 | 20.527 | 0.207153 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4174) vms_mb | MB | 2 | 967.570 | 367.254 | 1567.887 | 1567.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4190) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4190) rss_mb | MB | 3 | 3.012 | 3.012 | 3.012 | 3.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4190) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4190) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4191) CPU | percent | 2 | 217.284 | 172.964 | 261.605 | 261.605 | 4.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4191) rss_mb | MB | 3 | 760.051 | 217.875 | 1379.969 | 217.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4191) main thread run-queue wait | percent | 2 | 20.146 | 18.493 | 21.798 | 21.798 | 0.405185 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4191) vms_mb | MB | 3 | 1578.471 | 987.016 | 2359.336 | 987.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4281) CPU | percent | 8 | 10.816 | 2.982 | 52.722 | 52.722 | 0.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4281) rss_mb | MB | 9 | 755.718 | 84.695 | 1911.699 | 1911.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4281) main thread run-queue wait | percent | 8 | 0.838 | 0.000 | 6.692 | 6.692 | 0.067353 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4281) vms_mb | MB | 9 | 1413.714 | 437.039 | 2437.090 | 2437.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4295) rss_mb | MB | 1 | 44.871 | 44.871 | 44.871 | 44.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4295) vms_mb | MB | 1 | 404.160 | 404.160 | 404.160 | 404.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4309) rss_mb | MB | 1 | 2055.938 | 2055.938 | 2055.938 | 2055.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4309) vms_mb | MB | 1 | 2438.145 | 2438.145 | 2438.145 | 2438.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4322) rss_mb | MB | 1 | 3.008 | 3.008 | 3.008 | 3.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4322) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4324) rss_mb | MB | 1 | 2054.324 | 2054.324 | 2054.324 | 2054.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4324) vms_mb | MB | 1 | 2437.137 | 2437.137 | 2437.137 | 2437.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sed (PID 4325) rss_mb | MB | 1 | 1.891 | 1.891 | 1.891 | 1.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sed (PID 4325) vms_mb | MB | 1 | 3.707 | 3.707 | 3.707 | 3.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4340) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4340) rss_mb | MB | 3 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4340) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4340) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4342) rss_mb | MB | 1 | 1645.887 | 1645.887 | 1645.887 | 1645.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4342) vms_mb | MB | 1 | 2437.137 | 2437.137 | 2437.137 | 2437.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sed (PID 4343) rss_mb | MB | 1 | 1.801 | 1.801 | 1.801 | 1.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sed (PID 4343) vms_mb | MB | 1 | 3.707 | 3.707 | 3.707 | 3.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4351) CPU | percent | 1 | 317.006 | 317.006 | 317.006 | 317.006 | 3.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4351) rss_mb | MB | 2 | 313.197 | 174.070 | 452.324 | 452.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4351) main thread run-queue wait | percent | 1 | 38.635 | 38.635 | 38.635 | 38.635 | 0.388778 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4351) vms_mb | MB | 2 | 774.107 | 554.551 | 993.664 | 993.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4363) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4363) rss_mb | MB | 17 | 2.938 | 2.938 | 2.938 | 2.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4363) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4363) vms_mb | MB | 17 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4364) CPU | percent | 16 | 128.405 | 81.494 | 189.922 | 189.922 | 20.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4364) rss_mb | MB | 17 | 1271.067 | 88.246 | 1837.566 | 88.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4364) main thread run-queue wait | percent | 16 | 9.016 | 0.066 | 17.241 | 8.440 | 1.452237 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4364) vms_mb | MB | 17 | 2020.605 | 450.855 | 2292.227 | 450.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4383) rss_mb | MB | 1 | 8.164 | 8.164 | 8.164 | 8.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4383) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4424) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4424) rss_mb | MB | 3 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4424) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4424) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4425) CPU | percent | 2 | 286.711 | 181.600 | 391.822 | 391.822 | 5.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4425) rss_mb | MB | 3 | 1240.146 | 336.621 | 1979.762 | 1404.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4425) main thread run-queue wait | percent | 2 | 23.413 | 9.300 | 37.526 | 37.526 | 0.471061 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4425) vms_mb | MB | 3 | 2099.272 | 1038.883 | 3104.188 | 2154.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4464) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4464) rss_mb | MB | 4 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4464) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4464) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4465) CPU | percent | 2 | 244.350 | 191.853 | 296.846 | 296.846 | 4.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4465) rss_mb | MB | 3 | 819.130 | 409.152 | 1539.688 | 409.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4465) main thread run-queue wait | percent | 2 | 21.846 | 14.320 | 29.372 | 29.372 | 0.439915 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4465) vms_mb | MB | 3 | 1547.906 | 1174.832 | 2258.488 | 1174.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4480) rss_mb | MB | 1 | 68.148 | 68.148 | 68.148 | 68.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 4480) vms_mb | MB | 1 | 450.543 | 450.543 | 450.543 | 450.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sed (PID 4481) rss_mb | MB | 1 | 1.891 | 1.891 | 1.891 | 1.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sed (PID 4481) vms_mb | MB | 1 | 3.707 | 3.707 | 3.707 | 3.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4493) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4493) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4495) rss_mb | MB | 1 | 171.352 | 171.352 | 171.352 | 171.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4495) vms_mb | MB | 1 | 554.484 | 554.484 | 554.484 | 554.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4510) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4510) rss_mb | MB | 2 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4510) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4510) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4511) CPU | percent | 1 | 210.719 | 210.719 | 210.719 | 210.719 | 2.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4511) rss_mb | MB | 2 | 400.703 | 248.887 | 552.520 | 552.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4511) main thread run-queue wait | percent | 1 | 13.940 | 13.940 | 13.940 | 13.940 | 0.140252 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4511) vms_mb | MB | 2 | 1144.236 | 964.969 | 1323.504 | 1323.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4534) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4534) rss_mb | MB | 3 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4534) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4534) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4535) CPU | percent | 2 | 212.641 | 124.937 | 300.345 | 300.345 | 4.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4535) rss_mb | MB | 3 | 950.645 | 30.035 | 1450.676 | 1371.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4535) main thread run-queue wait | percent | 2 | 16.338 | 8.339 | 24.338 | 24.338 | 0.329630 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4535) vms_mb | MB | 3 | 1837.188 | 728.309 | 2612.285 | 2612.285 | n/a | n/a |
| docker commit (PID 4630) CPU | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4630) io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4630) io write MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4630) rss_mb | MB | 23 | 30.207 | 30.207 | 30.207 | 30.207 | n/a | n/a |
| docker commit (PID 4630) main thread run-queue wait | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4630) vms_mb | MB | 23 | 2059.844 | 2059.844 | 2059.844 | 2059.844 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 4913 | 98.688 | 0.000 | 647.864 | 0.000 | 4885.743422 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 4913 | 9.767 | 0.000 | 82.861 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 4913 | 11.992 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 4913 | 0.832 | 0.000 | 98.505 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 4913 | 0.858 | 0.000 | 98.505 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 4913 | 0.773 | 0.000 | 247.816 | 0.000 | 3823.781250 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 4913 | 1.320 | 0.000 | 246.712 | 0.000 | 6538.695312 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 4914 | 2631.247 | 17.047 | 12000.000 | 2668.543 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 4913 | 0.048 | 0.000 | 86.987 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 4913 | 0.048 | 0.000 | 86.994 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 4913 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001389 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 4913 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 4941 | 55.721 | 1.428 | 279.296 | 2.111 | 2774.875915 CPU seconds | n/a |
| workload total memory | MB | 4942 | 13170.686 | 7898.559 | 18882.016 | 17353.730 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
