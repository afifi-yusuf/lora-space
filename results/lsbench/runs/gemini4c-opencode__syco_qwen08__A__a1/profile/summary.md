# agprof summary

- Duration: **11581.099 s**
- Runs: **0/1 completed**, 0 succeeded, 0 failed, 1 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **101 calls**, 101 succeeded, 0 failed, 0 interrupted, n/a reported retries, 10908.670 s total wait
- Tools: **110/110 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **1141987** at 1.975 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | n/a / n/a ms |
| LLM latency p50 / p95 | 73210.897 / 261676.590 ms |
| LLM TTFT p50 / p95 | 50289.039 / 257239.536 ms |
| LLM input / output tokens | 10059758 / 99376 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 101 total, 101 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- opencode: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 85/85 | 85 | 0 | 0 | n/a | n/a |
| edit | 2/2 | 2 | 0 | 0 | n/a | n/a |
| read | 18/18 | 18 | 0 | 0 | n/a | n/a |
| todowrite | 3/3 | 3 | 0 | 0 | n/a | n/a |
| write | 2/2 | 2 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 2.834% | 119.298% | 328.544 s | 7824.808 MB | 8415.414 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker | 2209 |  | 1 | n/a% | n/a% | n/a s | 30.113 MB | 30.113 MB | 1771.508 MB | 1771.508 MB | n/a MB | n/a MB |
| vllm | 1994 |  | 11518 | 0.085% | 7.958% | 9.870 s | 1751.984 MB | 1786.023 MB | 11015.485 MB | 11036.254 MB | 0.007812 MB | 0.042969 MB |
| python | 2153 |  | 11518 | 0.030% | 5.942% | 3.530 s | 43.958 MB | 44.996 MB | 131.224 MB | 131.680 MB | 0.265625 MB | 0.347656 MB |
| python | 1989 |  | 11518 | 1.337% | 118.052% | 155.170 s | 2904.700 MB | 3333.184 MB | 15721.612 MB | 16608.996 MB | 113.597656 MB | 1112.027344 MB |
| VLLM::EngineCor | 2029 |  | 11518 | 1.380% | 58.653% | 159.840 s | 2276.060 MB | 2311.258 MB | 21204.019 MB | 21204.387 MB | 1.234375 MB | 0.078125 MB |
| lsb_grid_worker | 1980 |  | 11518 | 0.000% | 0.000% | 0.000 s | 3.253 MB | 3.328 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 2028 |  | 11518 | 0.000% | 0.000% | 0.000 s | 12.010 MB | 12.336 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 2267 | sandbox_agent_lsb-opencode_0000_0000 | 11517 | 0.002% | 1.990% | 0.250 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 2394 | sandbox_agent_lsb-opencode_0000_0000 | 11517 | 31.171% | 108.337% | 3609.320 s | 112.510 MB | 117.852 MB | 901.957 MB | 903.641 MB | n/a MB | n/a MB |
| python3 | 2400 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 57.655% | 61.687% | 1.160 s | 49.980 MB | 77.773 MB | 61.194 MB | 93.023 MB | n/a MB | n/a MB |
| tail | 2302 | sandbox_agent_lsb-opencode_0000_0000 | 11517 | 0.003% | 0.996% | 0.300 s | 1.312 MB | 1.312 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| opencode | 2408 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.758 MB | 12.758 MB | 6358.133 MB | 6358.133 MB | n/a MB | n/a MB |
| opencode | 2422 | sandbox_agent_lsb-opencode_0000_0000 | 11512 | 2.911% | 124.210% | 336.970 s | 703.066 MB | 930.883 MB | 16731.499 MB | 16847.746 MB | n/a MB | n/a MB |
| bash | 2727 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.863 MB | 2.863 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 2728 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.137 MB | 0.137 MB | 6.734 MB | 6.734 MB | n/a MB | n/a MB |
| python3 | 3637 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 56.406 MB | 56.406 MB | 69.930 MB | 69.930 MB | n/a MB | n/a MB |
| python3 | 3650 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 59.426 MB | 59.426 MB | 74.250 MB | 74.250 MB | n/a MB | n/a MB |
| python3 | 3705 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 63.215 MB | 63.215 MB | 78.500 MB | 78.500 MB | n/a MB | n/a MB |
| python3 | 3832 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.734 MB | 7.734 MB | 12.938 MB | 12.938 MB | n/a MB | n/a MB |
| python3 | 3846 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 68.941 MB | 68.941 MB | 289.164 MB | 289.164 MB | n/a MB | n/a MB |
| python3 | 3908 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 18.563% | 55.690% | 0.560 s | 69.081 MB | 77.195 MB | 270.548 MB | 280.125 MB | n/a MB | n/a MB |
| python3 | 3954 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 67.551% | 67.551% | 0.680 s | 55.805 MB | 77.102 MB | 254.799 MB | 279.875 MB | n/a MB | n/a MB |
| python3 | 4016 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 31.328 MB | 31.328 MB | 49.965 MB | 49.965 MB | n/a MB | n/a MB |
| python3 | 4029 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 61.199 MB | 61.199 MB | 257.246 MB | 257.246 MB | n/a MB | n/a MB |
| python3 | 4068 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 9.098% | 36.390% | 0.370 s | 71.902 MB | 76.809 MB | 272.790 MB | 278.852 MB | n/a MB | n/a MB |
| python3 | 4089 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 31.111% | 86.381% | 0.940 s | 61.587 MB | 77.051 MB | 215.249 MB | 279.906 MB | n/a MB | n/a MB |
| python3 | 4155 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.086 MB | 7.086 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 4169 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 20.883% | 41.767% | 0.420 s | 69.238 MB | 77.168 MB | 269.979 MB | 279.953 MB | n/a MB | n/a MB |
| python3 | 4224 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 14.886% | 22.837% | 0.300 s | 71.444 MB | 77.398 MB | 272.242 MB | 280.094 MB | n/a MB | n/a MB |
| python3 | 4255 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 37.788% | 37.788% | 0.380 s | 65.557 MB | 76.918 MB | 265.209 MB | 279.965 MB | n/a MB | n/a MB |
| python3 | 4286 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 32.772% | 85.406% | 0.990 s | 58.312 MB | 76.895 MB | 211.621 MB | 279.953 MB | n/a MB | n/a MB |
| python3 | 4301 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 55.632% | 55.632% | 0.560 s | 60.674 MB | 76.930 MB | 260.826 MB | 279.961 MB | n/a MB | n/a MB |
| python3 | 4333 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 26.353% | 52.706% | 0.530 s | 67.844 MB | 77.148 MB | 268.637 MB | 279.938 MB | n/a MB | n/a MB |
| python3 | 4376 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 40.035% | 84.437% | 1.210 s | 58.845 MB | 79.867 MB | 211.826 MB | 282.035 MB | n/a MB | n/a MB |
| python3 | 4480 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 11.934% | 23.868% | 0.240 s | 71.022 MB | 77.125 MB | 271.796 MB | 279.949 MB | n/a MB | n/a MB |
| python3 | 4532 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 85.371% | 85.371% | 0.860 s | 471.434 MB | 905.980 MB | 983.047 MB | 1734.207 MB | n/a MB | n/a MB |
| python3 | 4556 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 89.398% | 89.398% | 0.900 s | 569.725 MB | 1087.164 MB | 769.773 MB | 1290.918 MB | n/a MB | n/a MB |
| python3 | 4599 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 16.868% | 33.736% | 0.340 s | 69.638 MB | 77.469 MB | 270.014 MB | 279.938 MB | n/a MB | n/a MB |
| python3 | 4619 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 97.310% | 124.115% | 1.960 s | 418.350 MB | 1161.895 MB | 627.870 MB | 1395.133 MB | n/a MB | n/a MB |
| python3 | 4641 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 89.359% | 89.359% | 0.900 s | 1142.176 MB | 2238.410 MB | 1473.678 MB | 2704.375 MB | n/a MB | n/a MB |
| python3 | 4688 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 34.280% | 59.661% | 0.690 s | 65.743 MB | 78.082 MB | 266.177 MB | 280.648 MB | n/a MB | n/a MB |
| python3 | 4762 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 89.501% | 89.501% | 0.900 s | 639.301 MB | 1230.219 MB | 989.465 MB | 1734.355 MB | n/a MB | n/a MB |
| python3 | 4780 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 37.371 MB | 37.371 MB | 231.941 MB | 231.941 MB | n/a MB | n/a MB |
| python3 | 4890 | sandbox_agent_lsb-opencode_0000_0000 | 14 | 8.845% | 84.293% | 1.160 s | 75.345 MB | 80.797 MB | 277.470 MB | 283.203 MB | n/a MB | n/a MB |
| python3 | 4910 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 31.320 MB | 31.320 MB | 224.824 MB | 224.824 MB | n/a MB | n/a MB |
| python3 | 4923 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 109.820% | 138.270% | 2.210 s | 447.642 MB | 1154.555 MB | 657.977 MB | 1388.047 MB | n/a MB | n/a MB |
| python3 | 4948 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 146.567% | 170.465% | 4.430 s | 887.831 MB | 1172.336 MB | 1112.251 MB | 1406.070 MB | n/a MB | n/a MB |
| python3 | 4990 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 142.296% | 167.786% | 7.160 s | 786.471 MB | 1151.383 MB | 1008.864 MB | 1385.074 MB | n/a MB | n/a MB |
| python3 | 5050 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 53.184 MB | 53.184 MB | 249.836 MB | 249.836 MB | n/a MB | n/a MB |
| python3 | 5108 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 164.597% | 179.367% | 13.270 s | 1162.674 MB | 2384.848 MB | 1405.753 MB | 2768.062 MB | n/a MB | n/a MB |
| python3 | 5172 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 164.812% | 172.993% | 6.630 s | 122.173 MB | 157.387 MB | 344.595 MB | 386.168 MB | n/a MB | n/a MB |
| python3 | 5190 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 75.452% | 75.452% | 0.760 s | 70.469 MB | 116.727 MB | 282.938 MB | 349.961 MB | n/a MB | n/a MB |
| python3 | 5259 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 90.294% | 90.294% | 0.910 s | 571.592 MB | 1090.543 MB | 770.947 MB | 1293.367 MB | n/a MB | n/a MB |
| python3 | 5304 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 172.641% | 175.042% | 6.950 s | 48.234 MB | 50.246 MB | 271.412 MB | 273.484 MB | n/a MB | n/a MB |
| python3 | 5321 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.305 MB | 21.305 MB | 213.680 MB | 213.680 MB | n/a MB | n/a MB |
| python3 | 5341 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 172.087% | 174.484% | 8.670 s | 37.788 MB | 43.852 MB | 256.046 MB | 267.285 MB | n/a MB | n/a MB |
| bash | 5380 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 114.637% | 147.959% | 2.310 s | 87.056 MB | 201.266 MB | 230.165 MB | 432.121 MB | n/a MB | n/a MB |
| python3 | 5409 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 134.510% | 164.051% | 4.060 s | 1214.629 MB | 2463.582 MB | 1438.555 MB | 2701.301 MB | n/a MB | n/a MB |
| python3 | 5439 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 48.492 MB | 48.492 MB | 244.625 MB | 244.625 MB | n/a MB | n/a MB |
| python3 | 5457 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 14.284% | 85.511% | 1.160 s | 69.878 MB | 78.930 MB | 250.408 MB | 281.453 MB | n/a MB | n/a MB |
| python3 | 5480 | sandbox_agent_lsb-opencode_0000_0000 | 17 | 163.971% | 175.270% | 26.420 s | 1000.651 MB | 1119.160 MB | 1250.717 MB | 1353.602 MB | n/a MB | n/a MB |
| python3 | 5504 | sandbox_agent_lsb-opencode_0000_0000 | 12 | 161.508% | 174.799% | 17.890 s | 1094.352 MB | 1358.023 MB | 1339.257 MB | 1589.289 MB | n/a MB | n/a MB |
| python3 | 5557 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 160.129% | 177.274% | 19.360 s | 1104.272 MB | 1467.781 MB | 1478.203 MB | 3517.547 MB | n/a MB | n/a MB |
| python3 | 5577 | sandbox_agent_lsb-opencode_0000_0000 | 8 | 156.731% | 176.822% | 11.040 s | 1015.458 MB | 1402.887 MB | 1257.305 MB | 1732.434 MB | n/a MB | n/a MB |
| python3 | 5614 | sandbox_agent_lsb-opencode_0000_0000 | 10 | 157.115% | 174.547% | 14.230 s | 1001.660 MB | 1255.508 MB | 1224.665 MB | 1484.477 MB | n/a MB | n/a MB |
| python3 | 5633 | sandbox_agent_lsb-opencode_0000_0000 | 16 | 7.077% | 74.466% | 1.070 s | 77.065 MB | 83.016 MB | 279.060 MB | 285.160 MB | n/a MB | n/a MB |
| python3 | 5657 | sandbox_agent_lsb-opencode_0000_0000 | 36 | 173.185% | 176.968% | 61.030 s | 70.867 MB | 84.625 MB | 295.020 MB | 308.527 MB | n/a MB | n/a MB |
| python3 | 5712 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 170.656% | 176.436% | 20.620 s | 62.515 MB | 70.980 MB | 269.443 MB | 294.668 MB | n/a MB | n/a MB |
| python3 | 5729 | sandbox_agent_lsb-opencode_0000_0000 | 23 | 171.258% | 175.352% | 37.930 s | 64.694 MB | 72.203 MB | 288.721 MB | 296.297 MB | n/a MB | n/a MB |
| python3 | 5747 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 16.730% | 82.529% | 1.010 s | 69.796 MB | 78.355 MB | 244.477 MB | 280.848 MB | n/a MB | n/a MB |
| python3 | 5779 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 150.156% | 156.121% | 3.020 s | 42.327 MB | 62.090 MB | 193.539 MB | 286.461 MB | n/a MB | n/a MB |
| python3 | 5834 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 13.062% | 64.507% | 0.790 s | 71.433 MB | 78.156 MB | 273.354 MB | 281.137 MB | n/a MB | n/a MB |
| python3 | 5852 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 89.289% | 89.289% | 0.900 s | 580.207 MB | 1106.000 MB | 780.385 MB | 1309.180 MB | n/a MB | n/a MB |
| python3 | 5866 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 85.872% | 102.269% | 1.730 s | 402.727 MB | 1115.031 MB | 612.456 MB | 1349.102 MB | n/a MB | n/a MB |
| python3 | 5902 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 126.243% | 159.108% | 3.810 s | 729.688 MB | 1119.359 MB | 1164.034 MB | 1731.480 MB | n/a MB | n/a MB |
| python3 | 5944 | sandbox_agent_lsb-opencode_0000_0000 | 100 | 167.347% | 179.643% | 167.630 s | 3600.029 MB | 5172.617 MB | 3872.966 MB | 5400.184 MB | n/a MB | n/a MB |
| python3 | 6014 | sandbox_agent_lsb-opencode_0000_0000 | 95 | 169.058% | 178.618% | 160.060 s | 3609.112 MB | 5172.871 MB | 3871.721 MB | 5400.176 MB | n/a MB | n/a MB |
| python3 | 6057 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 58.545% | 58.545% | 0.590 s | 62.082 MB | 77.371 MB | 261.637 MB | 280.199 MB | n/a MB | n/a MB |
| python3 | 6067 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 54.023 MB | 54.023 MB | 249.980 MB | 249.980 MB | n/a MB | n/a MB |
| python3 | 6136 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.871 MB | 50.871 MB | 246.809 MB | 246.809 MB | n/a MB | n/a MB |
| python3 | 6162 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 82.436% | 82.436% | 0.830 s | 52.334 MB | 75.223 MB | 252.178 MB | 278.055 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.243% | 100.000% | 11920.576 MB | 12142.000 MB | 28.195 W | 72.486 W | 326495.855 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-opencode_0000_0000 | 40.011% | 212.205% | 4634.695 s | 1172.511 MB | 6203.613 MB | 277.027344 MB | 288.238281 MB | 26.250693 MB | 0.509892 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2159 | 11581.031 | interrupted |
| run0:write_lora_adapter:agent_lsb-opencode_0000 | -1 | 11581.030 | interrupted |
| engine:execute | 2160 | 11581.028 | interrupted |
| harness:attempt_rpc | 2407 | 11575.189 | interrupted |
| harness:await_cli | -1 | 11556.860 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| llm:attempt | 101/101 | 0 | 0 | 10908.670 | 4.123 | 10904.545 | 21.094 | 108006.639 | 73210.897 | 261676.590 |
| tool:bash | 85/85 | 0 | 0 | 529.084 | n/a | n/a | 109.879 | 6224.515 | 2251.087 | 16625.521 |
| harness:startup_ready | 1/1 | 0 | 0 | 16.257 | n/a | n/a | 60.446 | 16256.880 | 16256.880 | 16256.880 |
| syscall:sendto | 2336/2336 | 0 | 0 | 5.073 | n/a | n/a | 0.636 | 2.172 | 1.851 | 4.311 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.878 | 1.137 | 3.740 | 50.025 | 4877.520 | 4877.520 | 4877.520 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.877 | 1.137 | 3.740 | 50.021 | 4877.287 | 4877.287 | 4877.287 |
| tool:read | 18/18 | 0 | 0 | 1.801 | n/a | n/a | 1.906 | 100.053 | 68.793 | 231.575 |
| syscall:connect | 615/615 | 0 | 0 | 1.447 | n/a | n/a | 0.709 | 2.352 | 1.923 | 4.998 |
| harness:submit | 1/1 | 0 | 0 | 1.007 | n/a | n/a | 0.002 | 1007.220 | 1007.220 | 1007.220 |
| sandbox:create | 1/1 | 0 | 0 | 0.843 | 0.245 | 0.598 | 0.000 | 842.848 | 842.848 | 842.848 |
| run:container_call | 6/6 | 0 | 0 | 0.650 | 0.001 | 0.648 | 0.000 | 108.262 | 55.098 | 330.214 |
| sandbox:start | 1/1 | 0 | 0 | 0.576 | 0.002 | 0.573 | 0.000 | 575.680 | 575.680 | 575.680 |
| runtime.container_create | 1/1 | 0 | 0 | 0.576 | 0.002 | 0.573 | 0.000 | 575.540 | 575.540 | 575.540 |
| run:detect | 1/1 | 0 | 0 | 0.542 | 0.001 | 0.541 | 0.000 | 541.968 | 541.968 | 541.968 |
| syscall:execve | 177/177 | 0 | 0 | 0.278 | n/a | n/a | 0.080 | 1.573 | 1.334 | 2.429 |
| tool:todowrite | 3/3 | 0 | 0 | 0.171 | n/a | n/a | 0.002 | 56.843 | 49.821 | 81.601 |
| tool:write | 2/2 | 0 | 0 | 0.130 | n/a | n/a | 0.004 | 65.082 | 65.082 | 77.988 |
| tool:edit | 2/2 | 0 | 0 | 0.129 | n/a | n/a | 0.198 | 64.542 | 64.542 | 69.070 |
| agency:services_start | 1/1 | 0 | 0 | 0.077 | 0.043 | 0.034 | 0.000 | 76.770 | 76.770 | 76.770 |
| agent:create | 1/1 | 0 | 0 | 0.052 | 0.010 | 0.042 | 0.000 | 51.587 | 51.587 | 51.587 |
| harness:launch | 1/1 | 0 | 0 | 0.048 | n/a | n/a | 1.245 | 48.057 | 48.057 | 48.057 |
| syscall:bind | 10/10 | 0 | 0 | 0.022 | n/a | n/a | 0.076 | 2.224 | 1.862 | 3.856 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.300 | 1.300 | 1.300 |
| sync:container | 6/6 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.079 | 0.076 | 0.124 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.194 | 0.194 | 0.194 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.076 | 0.076 | 0.076 |
| harness:attempt_rpc | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| run:write_lora_adapter | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| engine:execute | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:await_cli | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 11516 | 0.092 | 0.036 | 1.010 | 0.135 | 10.615162 CPU seconds | n/a |
| GPU 0 memory | MB | 11518 | 11920.576 | 11670.000 | 12142.000 | 12142.000 | n/a | n/a |
| GPU 0 power | W | 11518 | 28.195 | 27.754 | 72.486 | 28.039 | n/a | 326495.855 J |
| GPU 0 proc / 1989-7337 / sandbox / ~ / device / GPU-6b78a9e2-4dd2-aea6-4b59-b27a7800516c memory | MB | 11518 | 3310.440 | 3118.000 | 3508.000 | 3508.000 | n/a | n/a |
| GPU 0 proc / 1989-7337 / sandbox / ~ / device / GPU-6b78a9e2-4dd2-aea6-4b59-b27a7800516c estimated power | W | 10862 | 0.250 | 0.000 | 53.706 | 0.000 | n/a | n/a |
| GPU 0 proc / 1989-7337 / sandbox / ~ / device / GPU-6b78a9e2-4dd2-aea6-4b59-b27a7800516c utilization | percent | 10862 | 0.202 | 0.000 | 47.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2029-9184 / sandbox / ~ / device / GPU-6b78a9e2-4dd2-aea6-4b59-b27a7800516c memory | MB | 11518 | 8128.136 | 8070.000 | 8152.000 | 8152.000 | n/a | n/a |
| GPU 0 proc / 2029-9184 / sandbox / ~ / device / GPU-6b78a9e2-4dd2-aea6-4b59-b27a7800516c estimated power | W | 494 | 0.956 | 0.000 | 68.761 | 0.000 | n/a | n/a |
| GPU 0 proc / 2029-9184 / sandbox / ~ / device / GPU-6b78a9e2-4dd2-aea6-4b59-b27a7800516c utilization | percent | 494 | 1.067 | 0.000 | 94.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 11518 | 11438.576 | 11188.000 | 11660.000 | 11660.000 | n/a | n/a |
| GPU 0 utilization | percent | 11518 | 0.243 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 11518 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 11517 | 2.615 | 0.112 | 75.845 | 0.538 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 11517 | 10.526 | 4.282 | 55.051 | 5.013 | n/a | n/a |
| host disk_read_mb_s | MB/s | 11517 | 0.063 | 0.000 | 63.779 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 11517 | 0.163 | 0.000 | 117.868 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 11517 | 0.138 | 0.000 | 73.065 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 11517 | 0.144 | 0.000 | 75.381 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 11518 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 11518 | 7638.502 | 6589.566 | 13156.141 | 8014.129 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 11517 | 0.007 | 0.000 | 28.774 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 11517 | 0.007 | 0.000 | 28.809 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 11517 | 0.005 | 0.000 | 12.380 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 11517 | 0.003 | 0.000 | 0.552 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1980) CPU | percent | 11517 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1980) io read MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1980) io write MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1980) rss_mb | MB | 11518 | 3.253 | 2.570 | 3.328 | 2.570 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1980) main thread run-queue wait | percent | 11517 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1980) vms_mb | MB | 11518 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1989) CPU | percent | 11517 | 1.337 | 0.000 | 118.052 | 1.990 | 155.170000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 1989) io read MB/s | MB/s | 11517 | 0.010 | 0.000 | 45.192 | 0.000 | 113.597656 MB | n/a |
| Agency harness — python -m lsbench (PID 1989) io write MB/s | MB/s | 11517 | 0.096 | 0.000 | 34.847 | 0.023 | 1112.027344 MB | n/a |
| Agency harness — python -m lsbench (PID 1989) rss_mb | MB | 11518 | 2904.700 | 2295.641 | 3333.184 | 3139.730 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1989) main thread run-queue wait | percent | 11517 | 0.000 | 0.000 | 2.462 | 0.000 | 0.045974 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 1989) vms_mb | MB | 11518 | 15721.612 | 13795.875 | 16608.996 | 16599.941 | n/a | n/a |
| Python — vllm (PID 1994) CPU | percent | 11517 | 0.085 | 0.000 | 7.958 | 0.000 | 9.870000 CPU seconds | n/a |
| Python — vllm (PID 1994) io read MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 1994) io write MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.008 | 0.000 | 0.042969 MB | n/a |
| Python — vllm (PID 1994) rss_mb | MB | 11518 | 1751.984 | 1447.184 | 1786.023 | 1447.184 | n/a | n/a |
| Python — vllm (PID 1994) main thread run-queue wait | percent | 11517 | 0.002 | 0.000 | 0.536 | 0.000 | 0.214117 run-queue seconds | n/a |
| Python — vllm (PID 1994) vms_mb | MB | 11518 | 11015.485 | 10963.234 | 11036.254 | 11036.254 | n/a | n/a |
| Python — python -c (PID 2028) CPU | percent | 11517 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2028) io read MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2028) io write MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2028) rss_mb | MB | 11518 | 12.010 | 9.062 | 12.336 | 9.062 | n/a | n/a |
| Python — python -c (PID 2028) main thread run-queue wait | percent | 11517 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2028) vms_mb | MB | 11518 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2029) CPU | percent | 11517 | 1.380 | 0.000 | 58.653 | 1.990 | 159.840000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2029) io read MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.922 | 0.000 | 1.234375 MB | n/a |
| VLLM::EngineCore (PID 2029) io write MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.008 | 0.000 | 0.078125 MB | n/a |
| VLLM::EngineCore (PID 2029) rss_mb | MB | 11518 | 2276.060 | 1957.652 | 2311.258 | 1959.383 | n/a | n/a |
| VLLM::EngineCore (PID 2029) main thread run-queue wait | percent | 11517 | 0.000 | 0.000 | 0.424 | 0.000 | 0.010375 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2029) vms_mb | MB | 11518 | 21204.019 | 21203.387 | 21204.387 | 21204.387 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2153) CPU | percent | 11517 | 0.030 | 0.000 | 5.942 | 0.000 | 3.530000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2153) io read MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.256 | 0.000 | 0.265625 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2153) io write MB/s | MB/s | 11517 | 0.000 | 0.000 | 0.008 | 0.000 | 0.347656 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2153) rss_mb | MB | 11518 | 43.958 | 34.340 | 44.996 | 36.520 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2153) main thread run-queue wait | percent | 11517 | 0.001 | 0.000 | 0.244 | 0.002 | 0.067816 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2153) vms_mb | MB | 11518 | 131.224 | 131.176 | 131.680 | 131.176 | n/a | n/a |
| docker inspect (PID 2209) rss_mb | MB | 1 | 30.113 | 30.113 | 30.113 | 30.113 | n/a | n/a |
| docker inspect (PID 2209) vms_mb | MB | 1 | 1771.508 | 1771.508 | 1771.508 | 1771.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2267) CPU | percent | 11516 | 0.002 | 0.000 | 1.990 | 0.000 | 0.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2267) rss_mb | MB | 11517 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2267) main thread run-queue wait | percent | 11516 | 0.004 | 0.000 | 5.385 | 0.000 | 0.468877 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2267) vms_mb | MB | 11517 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2302) CPU | percent | 11516 | 0.003 | 0.000 | 0.996 | 0.000 | 0.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2302) rss_mb | MB | 11517 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2302) main thread run-queue wait | percent | 11516 | 0.004 | 0.000 | 5.571 | 0.000 | 0.439335 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2302) vms_mb | MB | 11517 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2394) CPU | percent | 11516 | 31.171 | 0.000 | 108.337 | 17.910 | 3609.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2394) rss_mb | MB | 11517 | 112.510 | 2.914 | 117.852 | 115.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2394) main thread run-queue wait | percent | 11516 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000150 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2394) vms_mb | MB | 11517 | 901.957 | 4.262 | 903.641 | 902.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2400) CPU | percent | 2 | 57.655 | 53.623 | 61.687 | 61.687 | 1.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2400) rss_mb | MB | 3 | 49.980 | 23.105 | 77.773 | 77.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2400) main thread run-queue wait | percent | 2 | 0.029 | 0.026 | 0.032 | 0.026 | 0.000582 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2400) vms_mb | MB | 3 | 61.194 | 32.422 | 93.023 | 93.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2408) rss_mb | MB | 1 | 12.758 | 12.758 | 12.758 | 12.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2408) vms_mb | MB | 1 | 6358.133 | 6358.133 | 6358.133 | 6358.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2422) CPU | percent | 11511 | 2.911 | 0.000 | 124.210 | 0.000 | 336.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2422) rss_mb | MB | 11512 | 703.066 | 33.332 | 930.883 | 687.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2422) main thread run-queue wait | percent | 11511 | 1.584 | 0.000 | 85.562 | 0.000 | 183.835956 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2422) vms_mb | MB | 11512 | 16731.499 | 6358.195 | 16847.746 | 16847.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2727) rss_mb | MB | 1 | 2.863 | 2.863 | 2.863 | 2.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2727) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2728) rss_mb | MB | 1 | 0.137 | 0.137 | 0.137 | 0.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2728) vms_mb | MB | 1 | 6.734 | 6.734 | 6.734 | 6.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3637) rss_mb | MB | 1 | 56.406 | 56.406 | 56.406 | 56.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3637) vms_mb | MB | 1 | 69.930 | 69.930 | 69.930 | 69.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3650) rss_mb | MB | 1 | 59.426 | 59.426 | 59.426 | 59.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3650) vms_mb | MB | 1 | 74.250 | 74.250 | 74.250 | 74.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3705) rss_mb | MB | 1 | 63.215 | 63.215 | 63.215 | 63.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3705) vms_mb | MB | 1 | 78.500 | 78.500 | 78.500 | 78.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3832) rss_mb | MB | 1 | 7.734 | 7.734 | 7.734 | 7.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3832) vms_mb | MB | 1 | 12.938 | 12.938 | 12.938 | 12.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3846) rss_mb | MB | 1 | 68.941 | 68.941 | 68.941 | 68.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3846) vms_mb | MB | 1 | 289.164 | 289.164 | 289.164 | 289.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3908) CPU | percent | 3 | 18.563 | 0.000 | 55.690 | 0.000 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3908) rss_mb | MB | 4 | 69.081 | 44.738 | 77.195 | 77.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3908) main thread run-queue wait | percent | 3 | 0.084 | 0.000 | 0.251 | 0.000 | 0.002524 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3908) vms_mb | MB | 4 | 270.548 | 241.816 | 280.125 | 280.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3954) CPU | percent | 1 | 67.551 | 67.551 | 67.551 | 67.551 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3954) rss_mb | MB | 2 | 55.805 | 34.508 | 77.102 | 77.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3954) main thread run-queue wait | percent | 1 | 0.191 | 0.191 | 0.191 | 0.191 | 0.001926 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3954) vms_mb | MB | 2 | 254.799 | 229.723 | 279.875 | 279.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4016) rss_mb | MB | 1 | 31.328 | 31.328 | 31.328 | 31.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4016) vms_mb | MB | 1 | 49.965 | 49.965 | 49.965 | 49.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4029) rss_mb | MB | 1 | 61.199 | 61.199 | 61.199 | 61.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4029) vms_mb | MB | 1 | 257.246 | 257.246 | 257.246 | 257.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4068) CPU | percent | 4 | 9.098 | 0.000 | 36.390 | 0.000 | 0.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4068) rss_mb | MB | 5 | 71.902 | 52.277 | 76.809 | 76.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4068) main thread run-queue wait | percent | 4 | 0.038 | 0.000 | 0.152 | 0.000 | 0.001550 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4068) vms_mb | MB | 5 | 272.790 | 248.543 | 278.852 | 278.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4089) CPU | percent | 3 | 31.111 | 0.000 | 86.381 | 0.000 | 0.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4089) rss_mb | MB | 4 | 61.587 | 19.168 | 77.051 | 77.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4089) main thread run-queue wait | percent | 3 | 3.100 | 0.000 | 8.991 | 0.000 | 0.093665 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4089) vms_mb | MB | 4 | 215.249 | 25.273 | 279.906 | 279.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4155) rss_mb | MB | 1 | 7.086 | 7.086 | 7.086 | 7.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4155) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4169) CPU | percent | 2 | 20.883 | 0.000 | 41.767 | 0.000 | 0.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4169) rss_mb | MB | 3 | 69.238 | 53.379 | 77.168 | 77.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4169) main thread run-queue wait | percent | 2 | 0.217 | 0.000 | 0.433 | 0.000 | 0.004356 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4169) vms_mb | MB | 3 | 269.979 | 250.031 | 279.953 | 279.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4224) CPU | percent | 2 | 14.886 | 6.936 | 22.837 | 6.936 | 0.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4224) rss_mb | MB | 3 | 71.444 | 59.910 | 77.398 | 77.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4224) main thread run-queue wait | percent | 2 | 0.236 | 0.108 | 0.363 | 0.108 | 0.004751 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4224) vms_mb | MB | 3 | 272.242 | 256.699 | 280.094 | 280.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4255) CPU | percent | 1 | 37.788 | 37.788 | 37.788 | 37.788 | 0.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4255) rss_mb | MB | 2 | 65.557 | 54.195 | 76.918 | 76.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4255) main thread run-queue wait | percent | 1 | 0.342 | 0.342 | 0.342 | 0.342 | 0.003438 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4255) vms_mb | MB | 2 | 265.209 | 250.453 | 279.965 | 279.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4286) CPU | percent | 3 | 32.772 | 0.000 | 85.406 | 0.000 | 0.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4286) rss_mb | MB | 4 | 58.312 | 8.828 | 76.895 | 76.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4286) main thread run-queue wait | percent | 3 | 3.268 | 0.000 | 9.594 | 0.000 | 0.098723 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4286) vms_mb | MB | 4 | 211.621 | 13.301 | 279.953 | 279.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4301) CPU | percent | 1 | 55.632 | 55.632 | 55.632 | 55.632 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4301) rss_mb | MB | 2 | 60.674 | 44.418 | 76.930 | 76.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4301) main thread run-queue wait | percent | 1 | 0.298 | 0.298 | 0.298 | 0.298 | 0.002995 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4301) vms_mb | MB | 2 | 260.826 | 241.691 | 279.961 | 279.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4333) CPU | percent | 2 | 26.353 | 0.000 | 52.706 | 0.000 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4333) rss_mb | MB | 3 | 67.844 | 49.234 | 77.148 | 77.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4333) main thread run-queue wait | percent | 2 | 0.256 | 0.000 | 0.511 | 0.000 | 0.005140 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4333) vms_mb | MB | 3 | 268.637 | 246.035 | 279.938 | 279.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4376) CPU | percent | 3 | 40.035 | 9.849 | 84.437 | 9.849 | 1.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4376) rss_mb | MB | 4 | 58.845 | 7.887 | 79.867 | 79.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4376) main thread run-queue wait | percent | 3 | 4.727 | 1.283 | 11.427 | 1.472 | 0.142902 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4376) vms_mb | MB | 4 | 211.826 | 12.945 | 282.035 | 282.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4480) CPU | percent | 2 | 11.934 | 0.000 | 23.868 | 0.000 | 0.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4480) rss_mb | MB | 3 | 71.022 | 58.816 | 77.125 | 77.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4480) main thread run-queue wait | percent | 2 | 0.081 | 0.000 | 0.162 | 0.000 | 0.001626 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4480) vms_mb | MB | 3 | 271.796 | 255.488 | 279.949 | 279.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4532) CPU | percent | 1 | 85.371 | 85.371 | 85.371 | 85.371 | 0.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4532) rss_mb | MB | 2 | 471.434 | 36.887 | 905.980 | 905.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4532) main thread run-queue wait | percent | 1 | 0.079 | 0.079 | 0.079 | 0.079 | 0.000796 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4532) vms_mb | MB | 2 | 983.047 | 231.887 | 1734.207 | 1734.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4556) CPU | percent | 1 | 89.398 | 89.398 | 89.398 | 89.398 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4556) rss_mb | MB | 2 | 569.725 | 52.285 | 1087.164 | 1087.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4556) main thread run-queue wait | percent | 1 | 0.040 | 0.040 | 0.040 | 0.040 | 0.000407 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4556) vms_mb | MB | 2 | 769.773 | 248.629 | 1290.918 | 1290.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4599) CPU | percent | 2 | 16.868 | 0.000 | 33.736 | 0.000 | 0.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4599) rss_mb | MB | 3 | 69.638 | 53.977 | 77.469 | 77.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4599) main thread run-queue wait | percent | 2 | 0.171 | 0.000 | 0.341 | 0.000 | 0.003441 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4599) vms_mb | MB | 3 | 270.014 | 250.168 | 279.938 | 279.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4619) CPU | percent | 2 | 97.310 | 70.504 | 124.115 | 124.115 | 1.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4619) rss_mb | MB | 3 | 418.350 | 20.574 | 1161.895 | 1161.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4619) main thread run-queue wait | percent | 2 | 9.056 | 0.067 | 18.046 | 18.046 | 0.182413 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4619) vms_mb | MB | 3 | 627.870 | 212.527 | 1395.133 | 1395.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4641) CPU | percent | 1 | 89.359 | 89.359 | 89.359 | 89.359 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4641) rss_mb | MB | 2 | 1142.176 | 45.941 | 2238.410 | 2238.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4641) main thread run-queue wait | percent | 1 | 0.034 | 0.034 | 0.034 | 0.034 | 0.000341 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4641) vms_mb | MB | 2 | 1473.678 | 242.980 | 2704.375 | 2704.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4688) CPU | percent | 2 | 34.280 | 8.899 | 59.661 | 8.899 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4688) rss_mb | MB | 3 | 65.743 | 42.066 | 78.082 | 78.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4688) main thread run-queue wait | percent | 2 | 0.624 | 0.257 | 0.990 | 0.990 | 0.012598 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4688) vms_mb | MB | 3 | 266.177 | 238.930 | 280.648 | 280.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4762) CPU | percent | 1 | 89.501 | 89.501 | 89.501 | 89.501 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4762) rss_mb | MB | 2 | 639.301 | 48.383 | 1230.219 | 1230.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4762) main thread run-queue wait | percent | 1 | 0.037 | 0.037 | 0.037 | 0.037 | 0.000369 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4762) vms_mb | MB | 2 | 989.465 | 244.574 | 1734.355 | 1734.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4780) rss_mb | MB | 1 | 37.371 | 37.371 | 37.371 | 37.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4780) vms_mb | MB | 1 | 231.941 | 231.941 | 231.941 | 231.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4890) CPU | percent | 13 | 8.845 | 0.000 | 84.293 | 3.957 | 1.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4890) rss_mb | MB | 14 | 75.345 | 29.891 | 80.797 | 80.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4890) main thread run-queue wait | percent | 13 | 1.015 | 0.000 | 10.021 | 0.423 | 0.133079 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4890) vms_mb | MB | 14 | 277.470 | 226.594 | 283.203 | 283.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4910) rss_mb | MB | 1 | 31.320 | 31.320 | 31.320 | 31.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4910) vms_mb | MB | 1 | 224.824 | 224.824 | 224.824 | 224.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4923) CPU | percent | 2 | 109.820 | 81.369 | 138.270 | 138.270 | 2.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4923) rss_mb | MB | 3 | 447.642 | 30.930 | 1154.555 | 1154.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4923) main thread run-queue wait | percent | 2 | 16.010 | 0.041 | 31.978 | 31.978 | 0.321890 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4923) vms_mb | MB | 3 | 657.977 | 224.840 | 1388.047 | 1388.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4948) CPU | percent | 3 | 146.567 | 105.249 | 170.465 | 170.465 | 4.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4948) rss_mb | MB | 4 | 887.831 | 62.316 | 1172.336 | 1172.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4948) main thread run-queue wait | percent | 3 | 44.247 | 8.054 | 62.797 | 61.890 | 1.337440 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4948) vms_mb | MB | 4 | 1112.251 | 258.793 | 1406.070 | 1406.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4990) CPU | percent | 5 | 142.296 | 90.303 | 167.786 | 147.148 | 7.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4990) rss_mb | MB | 6 | 786.471 | 54.961 | 1151.383 | 99.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4990) main thread run-queue wait | percent | 5 | 51.271 | 0.031 | 69.849 | 57.773 | 2.579282 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4990) vms_mb | MB | 6 | 1008.864 | 251.836 | 1385.074 | 332.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5050) rss_mb | MB | 1 | 53.184 | 53.184 | 53.184 | 53.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5050) vms_mb | MB | 1 | 249.836 | 249.836 | 249.836 | 249.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5108) CPU | percent | 8 | 164.597 | 89.297 | 179.367 | 172.031 | 13.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5108) rss_mb | MB | 9 | 1162.674 | 52.277 | 2384.848 | 1151.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5108) main thread run-queue wait | percent | 8 | 55.151 | 0.027 | 74.175 | 52.053 | 4.446365 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5108) vms_mb | MB | 9 | 1405.753 | 248.691 | 2768.062 | 1381.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5172) CPU | percent | 4 | 164.812 | 143.210 | 172.993 | 172.993 | 6.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5172) rss_mb | MB | 5 | 122.173 | 57.465 | 157.387 | 157.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5172) main thread run-queue wait | percent | 4 | 51.966 | 30.429 | 74.202 | 74.202 | 2.090513 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5172) vms_mb | MB | 5 | 344.595 | 254.266 | 386.168 | 386.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5190) CPU | percent | 1 | 75.452 | 75.452 | 75.452 | 75.452 | 0.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5190) rss_mb | MB | 2 | 70.469 | 24.211 | 116.727 | 116.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5190) main thread run-queue wait | percent | 1 | 0.053 | 0.053 | 0.053 | 0.053 | 0.000531 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5190) vms_mb | MB | 2 | 282.938 | 215.914 | 349.961 | 349.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5259) CPU | percent | 1 | 90.294 | 90.294 | 90.294 | 90.294 | 0.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5259) rss_mb | MB | 2 | 571.592 | 52.641 | 1090.543 | 1090.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5259) main thread run-queue wait | percent | 1 | 0.030 | 0.030 | 0.030 | 0.030 | 0.000301 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5259) vms_mb | MB | 2 | 770.947 | 248.527 | 1293.367 | 1293.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5304) CPU | percent | 4 | 172.641 | 171.094 | 175.042 | 172.011 | 6.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5304) rss_mb | MB | 5 | 48.234 | 46.586 | 50.246 | 47.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5304) main thread run-queue wait | percent | 4 | 65.975 | 60.002 | 71.375 | 66.488 | 2.655970 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5304) vms_mb | MB | 5 | 271.412 | 269.785 | 273.484 | 270.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5321) rss_mb | MB | 1 | 21.305 | 21.305 | 21.305 | 21.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5321) vms_mb | MB | 1 | 213.680 | 213.680 | 213.680 | 213.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5341) CPU | percent | 5 | 172.087 | 168.005 | 174.484 | 173.002 | 8.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5341) rss_mb | MB | 6 | 37.788 | 21.633 | 43.852 | 38.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5341) main thread run-queue wait | percent | 5 | 68.151 | 64.257 | 71.959 | 71.959 | 3.433414 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5341) vms_mb | MB | 6 | 256.046 | 213.965 | 267.285 | 262.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5380) CPU | percent | 2 | 114.637 | 81.315 | 147.959 | 147.959 | 2.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5380) rss_mb | MB | 3 | 87.056 | 0.000 | 201.266 | 201.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5380) main thread run-queue wait | percent | 2 | 26.414 | 9.254 | 43.574 | 43.574 | 0.532130 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5380) vms_mb | MB | 3 | 230.165 | 1.617 | 432.121 | 432.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5409) CPU | percent | 3 | 134.510 | 89.502 | 164.051 | 164.051 | 4.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5409) rss_mb | MB | 4 | 1214.629 | 47.191 | 2463.582 | 1182.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5409) main thread run-queue wait | percent | 3 | 27.528 | 0.038 | 52.061 | 52.061 | 0.830933 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5409) vms_mb | MB | 4 | 1438.555 | 243.250 | 2701.301 | 1413.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5439) rss_mb | MB | 1 | 48.492 | 48.492 | 48.492 | 48.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5439) vms_mb | MB | 1 | 244.625 | 244.625 | 244.625 | 244.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5457) CPU | percent | 8 | 14.284 | 0.000 | 85.511 | 0.000 | 1.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5457) rss_mb | MB | 9 | 69.878 | 12.383 | 78.930 | 78.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5457) main thread run-queue wait | percent | 8 | 1.781 | 0.000 | 12.173 | 0.001 | 0.144793 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5457) vms_mb | MB | 9 | 250.408 | 16.758 | 281.453 | 281.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5480) CPU | percent | 16 | 163.971 | 75.451 | 175.270 | 175.270 | 26.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5480) rss_mb | MB | 17 | 1000.651 | 18.152 | 1119.160 | 1119.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5480) main thread run-queue wait | percent | 16 | 62.472 | 0.067 | 77.759 | 72.388 | 10.065993 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5480) vms_mb | MB | 17 | 1250.717 | 210.266 | 1353.602 | 1353.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5504) CPU | percent | 11 | 161.508 | 76.474 | 174.799 | 172.019 | 17.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5504) rss_mb | MB | 12 | 1094.352 | 21.711 | 1358.023 | 1358.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5504) main thread run-queue wait | percent | 11 | 56.616 | 0.055 | 73.910 | 51.430 | 6.272071 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5504) vms_mb | MB | 12 | 1339.257 | 213.977 | 1589.289 | 1589.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5557) CPU | percent | 12 | 160.129 | 69.586 | 177.274 | 160.041 | 19.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5557) rss_mb | MB | 13 | 1104.272 | 15.184 | 1467.781 | 1467.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5557) main thread run-queue wait | percent | 12 | 48.280 | 4.895 | 74.795 | 40.071 | 5.837337 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5557) vms_mb | MB | 13 | 1478.203 | 208.750 | 3517.547 | 1698.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5577) CPU | percent | 7 | 156.731 | 85.366 | 176.822 | 171.067 | 11.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5577) rss_mb | MB | 8 | 1015.458 | 41.820 | 1402.887 | 1113.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5577) main thread run-queue wait | percent | 7 | 53.194 | 0.035 | 73.999 | 66.972 | 3.746294 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5577) vms_mb | MB | 8 | 1257.305 | 239.086 | 1732.434 | 1347.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5614) CPU | percent | 9 | 157.115 | 69.628 | 174.547 | 174.547 | 14.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5614) rss_mb | MB | 10 | 1001.660 | 13.613 | 1255.508 | 1255.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5614) main thread run-queue wait | percent | 9 | 58.201 | 5.020 | 78.082 | 73.724 | 5.272070 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5614) vms_mb | MB | 10 | 1224.665 | 207.453 | 1484.477 | 1484.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5633) CPU | percent | 15 | 7.077 | 0.000 | 74.466 | 4.945 | 1.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5633) rss_mb | MB | 16 | 77.065 | 30.926 | 83.016 | 83.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5633) main thread run-queue wait | percent | 15 | 0.394 | 0.000 | 2.469 | 0.549 | 0.059563 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5633) vms_mb | MB | 16 | 279.060 | 226.902 | 285.160 | 285.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5657) CPU | percent | 35 | 173.185 | 165.042 | 176.968 | 172.028 | 61.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5657) rss_mb | MB | 36 | 70.867 | 42.836 | 84.625 | 84.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5657) main thread run-queue wait | percent | 35 | 64.228 | 46.069 | 78.930 | 54.881 | 22.630552 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5657) vms_mb | MB | 36 | 295.020 | 267.320 | 308.527 | 308.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5712) CPU | percent | 12 | 170.656 | 146.980 | 176.436 | 171.026 | 20.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5712) rss_mb | MB | 13 | 62.515 | 9.301 | 70.980 | 69.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5712) main thread run-queue wait | percent | 12 | 59.613 | 48.670 | 73.842 | 73.842 | 7.202854 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5712) vms_mb | MB | 13 | 269.443 | 13.523 | 294.668 | 293.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5729) CPU | percent | 22 | 171.258 | 164.799 | 175.352 | 172.433 | 37.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5729) rss_mb | MB | 23 | 64.694 | 50.223 | 72.203 | 66.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5729) main thread run-queue wait | percent | 22 | 62.743 | 47.752 | 73.912 | 57.817 | 13.894265 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5729) vms_mb | MB | 23 | 288.721 | 274.895 | 296.297 | 290.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5747) CPU | percent | 6 | 16.730 | 0.000 | 82.529 | 0.000 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5747) rss_mb | MB | 7 | 69.796 | 24.855 | 78.355 | 78.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5747) main thread run-queue wait | percent | 6 | 1.213 | 0.000 | 5.798 | 0.000 | 0.073225 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5747) vms_mb | MB | 7 | 244.477 | 31.676 | 280.848 | 280.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5779) CPU | percent | 2 | 150.156 | 144.190 | 156.121 | 156.121 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5779) rss_mb | MB | 3 | 42.327 | 7.973 | 62.090 | 56.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5779) main thread run-queue wait | percent | 2 | 59.861 | 49.523 | 70.200 | 70.200 | 1.203959 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5779) vms_mb | MB | 3 | 193.539 | 13.027 | 286.461 | 281.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5834) CPU | percent | 6 | 13.062 | 0.000 | 64.507 | 3.955 | 0.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5834) rss_mb | MB | 7 | 71.433 | 34.094 | 78.156 | 78.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5834) main thread run-queue wait | percent | 6 | 0.324 | 0.000 | 0.561 | 0.369 | 0.019624 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5834) vms_mb | MB | 7 | 273.354 | 229.559 | 281.137 | 281.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5852) CPU | percent | 1 | 89.289 | 89.289 | 89.289 | 89.289 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5852) rss_mb | MB | 2 | 580.207 | 54.414 | 1106.000 | 1106.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5852) main thread run-queue wait | percent | 1 | 0.033 | 0.033 | 0.033 | 0.033 | 0.000334 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5852) vms_mb | MB | 2 | 780.385 | 251.590 | 1309.180 | 1309.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5866) CPU | percent | 2 | 85.872 | 69.474 | 102.269 | 102.269 | 1.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5866) rss_mb | MB | 3 | 402.727 | 21.328 | 1115.031 | 1115.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5866) main thread run-queue wait | percent | 2 | 0.081 | 0.079 | 0.083 | 0.079 | 0.001635 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5866) vms_mb | MB | 3 | 612.456 | 213.723 | 1349.102 | 1349.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5902) CPU | percent | 3 | 126.243 | 84.440 | 159.108 | 159.108 | 3.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5902) rss_mb | MB | 4 | 729.688 | 34.094 | 1119.359 | 1119.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5902) main thread run-queue wait | percent | 3 | 36.446 | 0.042 | 69.640 | 69.640 | 1.099695 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5902) vms_mb | MB | 4 | 1164.034 | 227.852 | 1731.480 | 1348.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 5944) CPU | percent | 99 | 167.347 | 76.571 | 179.643 | 155.721 | 167.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 5944) rss_mb | MB | 100 | 3600.029 | 23.570 | 5172.617 | 1212.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 5944) main thread run-queue wait | percent | 99 | 54.242 | 0.034 | 77.869 | 49.677 | 54.330008 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 5944) vms_mb | MB | 100 | 3872.966 | 215.316 | 5400.184 | 1437.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 6014) CPU | percent | 94 | 169.058 | 68.535 | 178.618 | 173.973 | 160.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 6014) rss_mb | MB | 95 | 3609.112 | 22.297 | 5172.871 | 1181.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 6014) main thread run-queue wait | percent | 94 | 53.765 | 0.067 | 77.464 | 51.702 | 50.901645 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 6014) vms_mb | MB | 95 | 3871.721 | 214.625 | 5400.176 | 1406.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6057) CPU | percent | 1 | 58.545 | 58.545 | 58.545 | 58.545 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6057) rss_mb | MB | 2 | 62.082 | 46.793 | 77.371 | 77.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6057) main thread run-queue wait | percent | 1 | 0.179 | 0.179 | 0.179 | 0.179 | 0.001806 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6057) vms_mb | MB | 2 | 261.637 | 243.074 | 280.199 | 280.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6067) rss_mb | MB | 1 | 54.023 | 54.023 | 54.023 | 54.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6067) vms_mb | MB | 1 | 249.980 | 249.980 | 249.980 | 249.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6136) rss_mb | MB | 1 | 50.871 | 50.871 | 50.871 | 50.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6136) vms_mb | MB | 1 | 246.809 | 246.809 | 246.809 | 246.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6162) CPU | percent | 1 | 82.436 | 82.436 | 82.436 | 82.436 | 0.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6162) rss_mb | MB | 2 | 52.334 | 29.445 | 75.223 | 75.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6162) main thread run-queue wait | percent | 1 | 5.654 | 5.654 | 5.654 | 5.654 | 0.056925 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 6162) vms_mb | MB | 2 | 252.178 | 226.301 | 278.055 | 278.055 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 CPU | percent | 11516 | 40.011 | 16.530 | 212.205 | 18.302 | 4634.694784 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 11516 | 1.827 | 0.021 | 50.628 | 0.270 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 11516 | 2.381 | 0.021 | 75.509 | 0.270 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_full_pct | percent of wall time stalled | 11516 | 0.010 | 0.000 | 33.354 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_some_pct | percent of wall time stalled | 11516 | 0.011 | 0.000 | 33.354 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io read MB/s | MB/s | 11516 | 0.024 | 0.000 | 29.482 | 0.000 | 277.027344 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io write MB/s | MB/s | 11516 | 0.025 | 0.000 | 85.000 | 0.000 | 288.238281 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory | MB | 11517 | 1172.511 | 39.191 | 6203.613 | 975.031 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_full_pct | percent of wall time stalled | 11516 | 0.006 | 0.000 | 23.280 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_some_pct | percent of wall time stalled | 11516 | 0.006 | 0.000 | 23.280 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net rx MB/s | MB/s | 11516 | 0.002 | 0.000 | 11.691 | 0.000 | 26.250693 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net tx MB/s | MB/s | 11516 | 0.000 | 0.000 | 0.072 | 0.000 | 0.509892 MB | n/a |
| workload total CPU | percent | 11517 | 2.834 | 1.499 | 119.298 | 2.187 | 328.544480 CPU seconds | n/a |
| workload total memory | MB | 11518 | 7824.808 | 7176.176 | 8415.414 | 7723.820 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
