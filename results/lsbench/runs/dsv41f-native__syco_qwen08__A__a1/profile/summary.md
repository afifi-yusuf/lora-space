# agprof summary

- Duration: **1674.342 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **115 calls**, 113 succeeded, 2 failed, 0 interrupted, n/a reported retries, 1417.729 s total wait
- Tools: **112/112 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **155318** at 1.972 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1674272.155 / 1674272.155 ms |
| LLM latency p50 / p95 | 5053.919 / 15970.612 ms |
| LLM TTFT p50 / p95 | 2435.338 / 7481.651 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 115 total, 113 succeeded, 2 failed, 0 interrupted |
| Tool latency p50 / p95 | 558.715 / 9732.925 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 2/2 | 2 | 0 | 0 | 317.235 ms | 323.425 ms |
| attribution | 1/1 | 1 | 0 | 0 | 343.122 ms | 343.122 ms |
| bash | 78/78 | 78 | 0 | 0 | 487.943 ms | 9986.912 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 404.305 ms | 404.305 ms |
| generate | 9/9 | 9 | 0 | 0 | 585.886 ms | 1387.910 ms |
| inspect | 8/8 | 8 | 0 | 0 | 1123.496 ms | 1797.635 ms |
| inspect_module_inputs | 1/1 | 1 | 0 | 0 | 558.872 ms | 558.872 ms |
| patch | 6/6 | 6 | 0 | 0 | 426.948 ms | 437.979 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 239.972 ms | 239.972 ms |
| trace | 5/5 | 5 | 0 | 0 | 1086.354 ms | 1100.577 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 4.741% | 101.629% | 79.423 s | 8794.067 MB | 9001.508 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 7457 |  | 1663 | 0.128% | 7.946% | 2.150 s | 1804.258 MB | 1804.273 MB | 11043.829 MB | 11044.707 MB | 0.003906 MB | 0.031250 MB |
| python | 7452 |  | 1663 | 3.061% | 100.909% | 51.330 s | 2795.325 MB | 2966.176 MB | 16050.551 MB | 16322.172 MB | 1.707031 MB | 332.203125 MB |
| lsb_grid_worker | 1958 |  | 1663 | 0.000% | 0.000% | 0.000 s | 2.902 MB | 2.902 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 7491 |  | 1663 | 0.000% | 0.000% | 0.000 s | 12.121 MB | 12.121 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 7492 |  | 1663 | 1.539% | 42.757% | 25.740 s | 2321.477 MB | 2321.520 MB | 21203.375 MB | 21203.375 MB | 0.000000 MB | 0.007812 MB |
| docker | 7669 |  | 1 | n/a% | n/a% | n/a s | 30.324 MB | 30.324 MB | 1907.340 MB | 1907.340 MB | n/a MB | n/a MB |
| python3 | 7838 | sandbox_agent_lsb-native_0000_0000 | 2 | 59.657% | 59.657% | 0.600 s | 40.869 MB | 55.445 MB | 49.676 MB | 63.832 MB | n/a MB | n/a MB |
| docker-init | 7710 | sandbox_agent_lsb-native_0000_0000 | 1662 | 0.003% | 0.995% | 0.050 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 7832 | sandbox_agent_lsb-native_0000_0000 | 1662 | 4.085% | 99.517% | 68.330 s | 104.679 MB | 108.930 MB | 968.072 MB | 973.047 MB | n/a MB | n/a MB |
| tail | 7740 | sandbox_agent_lsb-native_0000_0000 | 1662 | 0.003% | 0.995% | 0.050 s | 1.293 MB | 1.293 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 7850 | sandbox_agent_lsb-native_0000_0000 | 1639 | 0.218% | 61.524% | 3.600 s | 72.013 MB | 73.988 MB | 86.398 MB | 88.074 MB | n/a MB | n/a MB |
| grep | 8114 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.664 MB | 1.664 MB | 3.629 MB | 3.629 MB | n/a MB | n/a MB |
| pip | 8113 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.938 MB | 11.938 MB | 16.188 MB | 16.188 MB | n/a MB | n/a MB |
| bash | 8111 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.977 MB | 2.977 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 8132 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.000 MB | 23.000 MB | 215.613 MB | 215.613 MB | n/a MB | n/a MB |
| python3 | 8207 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1008.414 MB | 1008.414 MB | 1670.891 MB | 1670.891 MB | n/a MB | n/a MB |
| python3 | 8215 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.703 MB | 21.703 MB | 213.691 MB | 213.691 MB | n/a MB | n/a MB |
| python3 | 8222 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 32.348 MB | 32.348 MB | 36.203 MB | 36.203 MB | n/a MB | n/a MB |
| python3 | 8226 | sandbox_agent_lsb-native_0000_0000 | 2 | 138.178% | 138.178% | 1.390 s | 538.258 MB | 1055.141 MB | 746.322 MB | 1278.945 MB | n/a MB | n/a MB |
| python3 | 8273 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 90.027 MB | 90.027 MB | 700.867 MB | 700.867 MB | n/a MB | n/a MB |
| python3 | 8312 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 101.715 MB | 101.715 MB | 106.328 MB | 106.328 MB | n/a MB | n/a MB |
| python3 | 8318 | sandbox_agent_lsb-native_0000_0000 | 2 | 131.231% | 131.231% | 1.320 s | 589.195 MB | 1132.691 MB | 804.979 MB | 1357.598 MB | n/a MB | n/a MB |
| python3 | 8325 | sandbox_agent_lsb-native_0000_0000 | 21 | 197.528% | 201.923% | 39.780 s | 1104.391 MB | 1132.980 MB | 1333.029 MB | 1357.648 MB | n/a MB | n/a MB |
| python3 | 8335 | sandbox_agent_lsb-native_0000_0000 | 3 | 179.981% | 199.953% | 3.630 s | 808.797 MB | 1132.754 MB | 1023.290 MB | 1357.625 MB | n/a MB | n/a MB |
| python3 | 8357 | sandbox_agent_lsb-native_0000_0000 | 9 | 197.858% | 200.698% | 15.920 s | 1225.435 MB | 1956.602 MB | 1515.745 MB | 2780.641 MB | n/a MB | n/a MB |
| python3 | 8379 | sandbox_agent_lsb-native_0000_0000 | 7 | 181.765% | 198.886% | 10.980 s | 1162.421 MB | 2393.074 MB | 1379.289 MB | 2780.648 MB | n/a MB | n/a MB |
| python3 | 8452 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 248.328 MB | 248.328 MB | 700.863 MB | 700.863 MB | n/a MB | n/a MB |
| python3 | 8465 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 81.523 MB | 81.523 MB | 278.754 MB | 278.754 MB | n/a MB | n/a MB |
| python3 | 8472 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 146.641 MB | 146.641 MB | 339.617 MB | 339.617 MB | n/a MB | n/a MB |
| python3 | 8479 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 607.945 MB | 607.945 MB | 840.617 MB | 840.617 MB | n/a MB | n/a MB |
| python3 | 8489 | sandbox_agent_lsb-native_0000_0000 | 2 | 151.089% | 151.089% | 1.520 s | 1242.320 MB | 2170.465 MB | 1615.227 MB | 2389.754 MB | n/a MB | n/a MB |
| python3 | 8497 | sandbox_agent_lsb-native_0000_0000 | 4 | 179.278% | 198.847% | 5.410 s | 1663.675 MB | 2139.043 MB | 1979.715 MB | 2359.398 MB | n/a MB | n/a MB |
| python3 | 8505 | sandbox_agent_lsb-native_0000_0000 | 3 | 174.387% | 199.822% | 3.520 s | 1138.906 MB | 2169.477 MB | 1873.333 MB | 2389.688 MB | n/a MB | n/a MB |
| python3 | 8516 | sandbox_agent_lsb-native_0000_0000 | 4 | 158.391% | 199.795% | 4.790 s | 1492.587 MB | 2169.914 MB | 1941.837 MB | 2780.660 MB | n/a MB | n/a MB |
| python3 | 8529 | sandbox_agent_lsb-native_0000_0000 | 4 | 159.644% | 196.705% | 4.820 s | 989.496 MB | 2170.266 MB | 1562.199 MB | 3265.676 MB | n/a MB | n/a MB |
| python3 | 8540 | sandbox_agent_lsb-native_0000_0000 | 4 | 183.154% | 197.961% | 5.530 s | 1739.565 MB | 2201.164 MB | 2017.647 MB | 2420.066 MB | n/a MB | n/a MB |
| python3 | 8554 | sandbox_agent_lsb-native_0000_0000 | 3 | 155.985% | 201.617% | 3.150 s | 1468.358 MB | 2200.426 MB | 1678.810 MB | 2420.031 MB | n/a MB | n/a MB |
| python3 | 8562 | sandbox_agent_lsb-native_0000_0000 | 19 | 196.065% | 202.177% | 35.590 s | 2056.050 MB | 2170.270 MB | 2297.046 MB | 2389.750 MB | n/a MB | n/a MB |
| python3 | 8589 | sandbox_agent_lsb-native_0000_0000 | 6 | 184.210% | 201.194% | 9.290 s | 1838.873 MB | 2200.785 MB | 2053.698 MB | 2420.035 MB | n/a MB | n/a MB |
| python3 | 8598 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 237.293 MB | 237.293 MB | 840.613 MB | 840.613 MB | n/a MB | n/a MB |
| python3 | 8607 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 143.973 MB | 143.973 MB | 336.637 MB | 336.637 MB | n/a MB | n/a MB |
| python3 | 8618 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1383.875 MB | 1383.875 MB | 1810.594 MB | 1810.594 MB | n/a MB | n/a MB |
| python3 | 8625 | sandbox_agent_lsb-native_0000_0000 | 7 | 192.180% | 201.543% | 11.640 s | 1937.681 MB | 2169.504 MB | 2155.479 MB | 2389.770 MB | n/a MB | n/a MB |
| python3 | 8637 | sandbox_agent_lsb-native_0000_0000 | 9 | 194.733% | 201.699% | 15.700 s | 1985.984 MB | 2170.133 MB | 2207.589 MB | 2389.816 MB | n/a MB | n/a MB |
| python3 | 8645 | sandbox_agent_lsb-native_0000_0000 | 8 | 181.758% | 198.817% | 12.800 s | 1918.328 MB | 2420.047 MB | 2128.630 MB | 2780.766 MB | n/a MB | n/a MB |
| python3 | 8663 | sandbox_agent_lsb-native_0000_0000 | 10 | 191.001% | 202.816% | 17.330 s | 1934.821 MB | 2139.719 MB | 2151.817 MB | 2359.395 MB | n/a MB | n/a MB |
| python3 | 8672 | sandbox_agent_lsb-native_0000_0000 | 4 | 191.729% | 200.844% | 5.800 s | 2123.070 MB | 2138.633 MB | 2464.717 MB | 2780.672 MB | n/a MB | n/a MB |
| python3 | 8682 | sandbox_agent_lsb-native_0000_0000 | 4 | 183.035% | 199.397% | 5.560 s | 1678.456 MB | 2137.582 MB | 1978.641 MB | 2357.969 MB | n/a MB | n/a MB |
| python3 | 8720 | sandbox_agent_lsb-native_0000_0000 | 18 | 191.983% | 202.370% | 32.950 s | 1945.697 MB | 2103.504 MB | 2181.129 MB | 2327.652 MB | n/a MB | n/a MB |
| python3 | 8732 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.637 MB | 21.637 MB | 213.777 MB | 213.777 MB | n/a MB | n/a MB |
| python3 | 8746 | sandbox_agent_lsb-native_0000_0000 | 10 | 196.223% | 199.475% | 17.770 s | 2169.019 MB | 2438.027 MB | 2401.557 MB | 2780.703 MB | n/a MB | n/a MB |
| python3 | 8759 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.465 MB | 12.465 MB | 206.980 MB | 206.980 MB | n/a MB | n/a MB |
| bash | 8758 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.895 MB | 2.895 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| docker | 8835 |  | 18 | 0.000% | 0.000% | 0.000 s | 30.137 MB | 30.137 MB | 1843.262 MB | 1843.262 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.692% | 100.000% | 11950.502 MB | 12060.000 MB | 29.192 W | 63.969 W | 48823.377 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 23.812% | 204.813% | 398.739 s | 380.525 MB | 2689.578 MB | 51.996094 MB | 1.625000 MB | 0.000854 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 7599 | 1674.277 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1674.272 | n/a | n/a | 51.996 | 1674272.155 | 1674272.155 | 1674272.155 |
| sync:result_wait | 1/1 | 0 | 0 | 1674.271 | 0.000 | 1674.271 | 51.996 | 1674271.405 | 1674271.405 | 1674271.405 |
| engine:execute | 1/1 | 0 | 0 | 1674.271 | 2.408 | 1671.838 | 51.996 | 1674270.691 | 1674270.691 | 1674270.691 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1650.483 | 0.002 | 1650.480 | 28.386 | 1650482.666 | 1650482.666 | 1650482.666 |
| turn | 113/113 | 0 | 0 | 1645.889 | n/a | n/a | 25.604 | 14565.393 | 6256.218 | 22171.359 |
| llm:attempt | 115/115 | 2 | 0 | 1417.729 | 13.554 | 1404.171 | 12.678 | 12328.075 | 5053.919 | 15970.612 |
| tool:bash | 78/78 | 0 | 0 | 190.052 | n/a | n/a | 11.501 | 2436.561 | 487.943 | 9986.912 |
| process:bash | 78/78 | 4 | 0 | 189.254 | n/a | n/a | 11.355 | 2426.333 | 478.793 | 9975.011 |
| run:container_call | 13/13 | 0 | 0 | 18.981 | 0.003 | 18.978 | 0.020 | 1460.069 | 45.991 | 7489.972 |
| teardown:commit | 1/1 | 0 | 0 | 18.236 | 0.005 | 18.231 | 0.021 | 18235.522 | 18235.522 | 18235.522 |
| sandbox:commit | 1/1 | 0 | 0 | 18.039 | 0.003 | 18.036 | 0.021 | 18038.868 | 18038.868 | 18038.868 |
| checkpoint.total | 1/1 | 0 | 0 | 18.039 | 0.003 | 18.036 | 0.021 | 18038.691 | 18038.691 | 18038.691 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 18.039 | 0.003 | 18.036 | 0.021 | 18038.543 | 18038.543 | 18038.543 |
| tool:inspect | 8/8 | 0 | 0 | 9.179 | n/a | n/a | 0.000 | 1147.354 | 1123.496 | 1797.635 |
| tool:generate | 9/9 | 0 | 0 | 6.903 | n/a | n/a | 0.000 | 767.048 | 585.886 | 1387.910 |
| syscall:sendto | 2217/2217 | 0 | 0 | 5.591 | n/a | n/a | 0.665 | 2.522 | 2.183 | 4.702 |
| tool:trace | 5/5 | 0 | 0 | 5.431 | n/a | n/a | 0.000 | 1086.278 | 1086.354 | 1100.577 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.449 | 0.965 | 3.484 | 23.481 | 4448.969 | 4448.969 | 4448.969 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.449 | 0.965 | 3.484 | 23.481 | 4448.743 | 4448.743 | 4448.743 |
| tool:patch | 6/6 | 0 | 0 | 2.578 | n/a | n/a | 0.000 | 429.618 | 426.948 | 437.979 |
| syscall:connect | 561/561 | 0 | 0 | 1.542 | n/a | n/a | 0.209 | 2.749 | 2.209 | 5.644 |
| sandbox:create | 1/1 | 0 | 0 | 0.797 | 0.252 | 0.545 | 0.000 | 797.301 | 797.301 | 797.301 |
| sandbox:start | 1/1 | 0 | 0 | 0.676 | 0.003 | 0.673 | 0.000 | 675.586 | 675.586 | 675.586 |
| runtime.container_create | 1/1 | 0 | 0 | 0.675 | 0.002 | 0.673 | 0.000 | 675.421 | 675.421 | 675.421 |
| tool:attention | 2/2 | 0 | 0 | 0.634 | n/a | n/a | 0.000 | 317.235 | 317.235 | 323.425 |
| tool:inspect_module_inputs | 1/1 | 0 | 0 | 0.559 | n/a | n/a | 0.000 | 558.872 | 558.872 | 558.872 |
| run:detect | 1/1 | 0 | 0 | 0.485 | 0.001 | 0.484 | 0.000 | 485.072 | 485.072 | 485.072 |
| syscall:execve | 258/258 | 0 | 0 | 0.410 | n/a | n/a | 0.149 | 1.589 | 1.208 | 3.318 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.404 | n/a | n/a | 0.000 | 404.305 | 404.305 | 404.305 |
| tool:attribution | 1/1 | 0 | 0 | 0.343 | n/a | n/a | 0.000 | 343.122 | 343.122 | 343.122 |
| tool:submit_output | 1/1 | 0 | 0 | 0.240 | n/a | n/a | 0.000 | 239.972 | 239.972 | 239.972 |
| sandbox:stop | 1/1 | 0 | 0 | 0.196 | 0.002 | 0.195 | 0.000 | 196.377 | 196.377 | 196.377 |
| agency:services_close | 1/1 | 0 | 0 | 0.154 | 0.001 | 0.153 | 0.011 | 154.300 | 154.300 | 154.300 |
| llm:retry_backoff | 2/2 | 0 | 0 | 0.135 | n/a | n/a | 0.000 | 67.624 | 67.624 | 110.618 |
| agency:services_start | 1/1 | 0 | 0 | 0.074 | 0.042 | 0.032 | 0.000 | 74.254 | 74.254 | 74.254 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.009 | 0.040 | 0.000 | 48.614 | 48.614 | 48.614 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 1.279 | 1.279 | 1.279 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.248 | 1.248 | 1.248 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.075 | 0.077 | 0.106 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.173 | 0.173 | 0.173 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.058 | 0.058 | 0.058 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1661 | 0.415 | 0.012 | 41.258 | 40.107 | 6.934896 CPU seconds | n/a |
| GPU 0 memory | MB | 1663 | 11950.502 | 11670.000 | 12060.000 | 12060.000 | n/a | n/a |
| GPU 0 power | W | 1663 | 29.192 | 28.236 | 63.969 | 28.472 | n/a | 48823.377 J |
| GPU 0 proc / 7452-555976 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 memory | MB | 1663 | 3321.817 | 3118.000 | 3430.000 | 3430.000 | n/a | n/a |
| GPU 0 proc / 7452-555976 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 estimated power | W | 1547 | 0.663 | 0.000 | 54.129 | 0.000 | n/a | n/a |
| GPU 0 proc / 7452-555976 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 utilization | percent | 1547 | 0.363 | 0.000 | 45.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 7492-558441 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 memory | MB | 1663 | 8146.684 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 7492-558441 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 estimated power | W | 89 | 4.869 | 0.000 | 63.969 | 0.000 | n/a | n/a |
| GPU 0 proc / 7492-558441 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 utilization | percent | 89 | 4.124 | 0.000 | 78.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1663 | 11468.502 | 11188.000 | 11578.000 | 11578.000 | n/a | n/a |
| GPU 0 utilization | percent | 1663 | 0.692 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1663 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1662 | 4.829 | 0.032 | 52.303 | 1.210 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1662 | 7.001 | 0.252 | 52.500 | 8.877 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1662 | 0.698 | 0.000 | 176.943 | 8.579 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1662 | 0.216 | 0.000 | 7.858 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1662 | 0.321 | 0.000 | 45.298 | 21.625 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1662 | 0.328 | 0.000 | 45.454 | 21.754 | n/a | n/a |
| host mem_total_mb | MB | 1663 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1663 | 7040.099 | 6314.348 | 9429.738 | 6977.824 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1662 | 0.001 | 0.000 | 1.185 | 0.015 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1662 | 0.001 | 0.000 | 1.310 | 0.015 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1662 | 0.006 | 0.000 | 0.147 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1662 | 0.019 | 0.000 | 0.528 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1958) CPU | percent | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1958) io read MB/s | MB/s | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1958) io write MB/s | MB/s | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1958) rss_mb | MB | 1663 | 2.902 | 2.902 | 2.902 | 2.902 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1958) main thread run-queue wait | percent | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1958) vms_mb | MB | 1663 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 7452) CPU | percent | 1662 | 3.061 | 0.000 | 100.909 | 0.000 | 51.330000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 7452) io read MB/s | MB/s | 1662 | 0.001 | 0.000 | 0.794 | 0.000 | 1.707031 MB | n/a |
| Agency harness — python -m lsbench (PID 7452) io write MB/s | MB/s | 1662 | 0.198 | 0.000 | 8.013 | 0.023 | 332.203125 MB | n/a |
| Agency harness — python -m lsbench (PID 7452) rss_mb | MB | 1663 | 2795.325 | 2156.043 | 2966.176 | 2966.176 | n/a | n/a |
| Agency harness — python -m lsbench (PID 7452) main thread run-queue wait | percent | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 7452) vms_mb | MB | 1663 | 16050.551 | 13603.867 | 16322.172 | 16290.035 | n/a | n/a |
| Python — vllm (PID 7457) CPU | percent | 1662 | 0.128 | 0.000 | 7.946 | 0.000 | 2.150000 CPU seconds | n/a |
| Python — vllm (PID 7457) io read MB/s | MB/s | 1662 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 7457) io write MB/s | MB/s | 1662 | 0.000 | 0.000 | 0.008 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 7457) rss_mb | MB | 1663 | 1804.258 | 1803.398 | 1804.273 | 1804.273 | n/a | n/a |
| Python — vllm (PID 7457) main thread run-queue wait | percent | 1662 | 0.003 | 0.000 | 0.342 | 0.007 | 0.053841 run-queue seconds | n/a |
| Python — vllm (PID 7457) vms_mb | MB | 1663 | 11043.829 | 10971.688 | 11044.707 | 11044.707 | n/a | n/a |
| Python — python -c (PID 7491) CPU | percent | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 7491) io read MB/s | MB/s | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 7491) io write MB/s | MB/s | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 7491) rss_mb | MB | 1663 | 12.121 | 12.121 | 12.121 | 12.121 | n/a | n/a |
| Python — python -c (PID 7491) main thread run-queue wait | percent | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 7491) vms_mb | MB | 1663 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 7492) CPU | percent | 1662 | 1.539 | 0.000 | 42.757 | 0.995 | 25.740000 CPU seconds | n/a |
| VLLM::EngineCore (PID 7492) io read MB/s | MB/s | 1662 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 7492) io write MB/s | MB/s | 1662 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 7492) rss_mb | MB | 1663 | 2321.477 | 2321.395 | 2321.520 | 2321.520 | n/a | n/a |
| VLLM::EngineCore (PID 7492) main thread run-queue wait | percent | 1662 | 0.000 | 0.000 | 0.099 | 0.000 | 0.002218 run-queue seconds | n/a |
| VLLM::EngineCore (PID 7492) vms_mb | MB | 1663 | 21203.375 | 21203.375 | 21203.375 | 21203.375 | n/a | n/a |
| docker run (PID 7669) rss_mb | MB | 1 | 30.324 | 30.324 | 30.324 | 30.324 | n/a | n/a |
| docker run (PID 7669) vms_mb | MB | 1 | 1907.340 | 1907.340 | 1907.340 | 1907.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 7710) CPU | percent | 1661 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 7710) rss_mb | MB | 1662 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 7710) main thread run-queue wait | percent | 1661 | 0.008 | 0.000 | 5.133 | 0.000 | 0.130301 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 7710) vms_mb | MB | 1662 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 7740) CPU | percent | 1661 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 7740) rss_mb | MB | 1662 | 1.293 | 1.293 | 1.293 | 1.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 7740) main thread run-queue wait | percent | 1661 | 0.006 | 0.000 | 5.148 | 0.000 | 0.094573 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 7740) vms_mb | MB | 1662 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7832) CPU | percent | 1661 | 4.085 | 0.000 | 99.517 | 0.000 | 68.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7832) rss_mb | MB | 1662 | 104.679 | 2.875 | 108.930 | 106.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7832) main thread run-queue wait | percent | 1661 | 0.000 | 0.000 | 0.029 | 0.000 | 0.000326 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 7832) vms_mb | MB | 1662 | 968.072 | 4.258 | 973.047 | 972.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 7838) CPU | percent | 1 | 59.657 | 59.657 | 59.657 | 59.657 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 7838) rss_mb | MB | 2 | 40.869 | 26.293 | 55.445 | 55.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 7838) main thread run-queue wait | percent | 1 | 0.016 | 0.016 | 0.016 | 0.016 | 0.000165 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 7838) vms_mb | MB | 2 | 49.676 | 35.520 | 63.832 | 63.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 7850) CPU | percent | 1638 | 0.218 | 0.000 | 61.524 | 0.000 | 3.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 7850) rss_mb | MB | 1639 | 72.013 | 30.934 | 73.988 | 73.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 7850) main thread run-queue wait | percent | 1638 | 0.028 | 0.000 | 5.534 | 0.000 | 0.456930 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 7850) vms_mb | MB | 1639 | 86.398 | 36.262 | 88.074 | 88.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8111) rss_mb | MB | 1 | 2.977 | 2.977 | 2.977 | 2.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8111) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — pip (PID 8113) rss_mb | MB | 1 | 11.938 | 11.938 | 11.938 | 11.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — pip (PID 8113) vms_mb | MB | 1 | 16.188 | 16.188 | 16.188 | 16.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 8114) rss_mb | MB | 1 | 1.664 | 1.664 | 1.664 | 1.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 8114) vms_mb | MB | 1 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8132) rss_mb | MB | 1 | 23.000 | 23.000 | 23.000 | 23.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8132) vms_mb | MB | 1 | 215.613 | 215.613 | 215.613 | 215.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sload.py (PID 8207) rss_mb | MB | 1 | 1008.414 | 1008.414 | 1008.414 | 1008.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sload.py (PID 8207) vms_mb | MB | 1 | 1670.891 | 1670.891 | 1670.891 | 1670.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8215) rss_mb | MB | 1 | 21.703 | 21.703 | 21.703 | 21.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8215) vms_mb | MB | 1 | 213.691 | 213.691 | 213.691 | 213.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8222) rss_mb | MB | 1 | 32.348 | 32.348 | 32.348 | 32.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8222) vms_mb | MB | 1 | 36.203 | 36.203 | 36.203 | 36.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8226) CPU | percent | 1 | 138.178 | 138.178 | 138.178 | 138.178 | 1.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8226) rss_mb | MB | 2 | 538.258 | 21.375 | 1055.141 | 1055.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8226) main thread run-queue wait | percent | 1 | 16.274 | 16.274 | 16.274 | 16.274 | 0.163704 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8226) vms_mb | MB | 2 | 746.322 | 213.699 | 1278.945 | 1278.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8273) rss_mb | MB | 1 | 90.027 | 90.027 | 90.027 | 90.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8273) vms_mb | MB | 1 | 700.867 | 700.867 | 700.867 | 700.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8312) rss_mb | MB | 1 | 101.715 | 101.715 | 101.715 | 101.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8312) vms_mb | MB | 1 | 106.328 | 106.328 | 106.328 | 106.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8318) CPU | percent | 1 | 131.231 | 131.231 | 131.231 | 131.231 | 1.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8318) rss_mb | MB | 2 | 589.195 | 45.699 | 1132.691 | 1132.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8318) main thread run-queue wait | percent | 1 | 9.564 | 9.564 | 9.564 | 9.564 | 0.096205 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8318) vms_mb | MB | 2 | 804.979 | 252.359 | 1357.598 | 1357.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8325) CPU | percent | 20 | 197.528 | 180.900 | 201.923 | 197.806 | 39.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8325) rss_mb | MB | 21 | 1104.391 | 532.605 | 1132.980 | 1132.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8325) main thread run-queue wait | percent | 20 | 49.090 | 31.659 | 54.398 | 48.886 | 9.886202 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8325) vms_mb | MB | 21 | 1333.029 | 840.648 | 1357.648 | 1357.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8335) CPU | percent | 2 | 179.981 | 160.009 | 199.953 | 199.953 | 3.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8335) rss_mb | MB | 3 | 808.797 | 160.883 | 1132.754 | 1132.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8335) main thread run-queue wait | percent | 2 | 36.809 | 23.770 | 49.849 | 49.849 | 0.742760 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8335) vms_mb | MB | 3 | 1023.290 | 354.621 | 1357.625 | 1357.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8357) CPU | percent | 8 | 197.858 | 196.899 | 200.698 | 196.899 | 15.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8357) rss_mb | MB | 9 | 1225.435 | 1134.039 | 1956.602 | 1134.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8357) main thread run-queue wait | percent | 8 | 48.784 | 40.200 | 50.838 | 50.098 | 3.925176 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8357) vms_mb | MB | 9 | 1515.745 | 1357.633 | 2780.641 | 1357.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 8379) CPU | percent | 6 | 181.765 | 100.165 | 198.886 | 197.927 | 10.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 8379) rss_mb | MB | 7 | 1162.421 | 72.074 | 2393.074 | 1134.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 8379) main thread run-queue wait | percent | 6 | 42.546 | 11.204 | 50.072 | 49.457 | 2.569863 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 8379) vms_mb | MB | 7 | 1379.289 | 86.168 | 2780.648 | 1357.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8452) rss_mb | MB | 1 | 248.328 | 248.328 | 248.328 | 248.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8452) vms_mb | MB | 1 | 700.863 | 700.863 | 700.863 | 700.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8465) rss_mb | MB | 1 | 81.523 | 81.523 | 81.523 | 81.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8465) vms_mb | MB | 1 | 278.754 | 278.754 | 278.754 | 278.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8472) rss_mb | MB | 1 | 146.641 | 146.641 | 146.641 | 146.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8472) vms_mb | MB | 1 | 339.617 | 339.617 | 339.617 | 339.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8479) rss_mb | MB | 1 | 607.945 | 607.945 | 607.945 | 607.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8479) vms_mb | MB | 1 | 840.617 | 840.617 | 840.617 | 840.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8489) CPU | percent | 1 | 151.089 | 151.089 | 151.089 | 151.089 | 1.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8489) rss_mb | MB | 2 | 1242.320 | 314.176 | 2170.465 | 2170.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8489) main thread run-queue wait | percent | 1 | 18.166 | 18.166 | 18.166 | 18.166 | 0.182759 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8489) vms_mb | MB | 2 | 1615.227 | 840.699 | 2389.754 | 2389.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8497) CPU | percent | 3 | 179.278 | 141.019 | 198.847 | 197.967 | 5.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8497) rss_mb | MB | 4 | 1663.675 | 237.570 | 2139.043 | 2139.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8497) main thread run-queue wait | percent | 3 | 38.283 | 14.743 | 50.575 | 49.530 | 1.155023 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8497) vms_mb | MB | 4 | 1979.715 | 840.664 | 2359.398 | 2359.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8505) CPU | percent | 2 | 174.387 | 148.952 | 199.822 | 199.822 | 3.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8505) rss_mb | MB | 3 | 1138.906 | 358.727 | 2169.477 | 888.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8505) main thread run-queue wait | percent | 2 | 35.482 | 19.399 | 51.566 | 51.566 | 0.716634 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8505) vms_mb | MB | 3 | 1873.333 | 840.633 | 2389.688 | 2389.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8516) CPU | percent | 3 | 158.391 | 97.438 | 199.795 | 199.795 | 4.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8516) rss_mb | MB | 4 | 1492.587 | 13.129 | 2169.914 | 2169.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8516) main thread run-queue wait | percent | 3 | 32.684 | 10.722 | 50.276 | 50.276 | 0.988889 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8516) vms_mb | MB | 4 | 1941.837 | 207.285 | 2780.660 | 2389.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8529) CPU | percent | 3 | 159.644 | 92.345 | 196.705 | 196.705 | 4.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8529) rss_mb | MB | 4 | 989.496 | 13.188 | 2170.266 | 166.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8529) main thread run-queue wait | percent | 3 | 30.033 | 0.625 | 49.213 | 49.213 | 0.906660 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8529) vms_mb | MB | 4 | 1562.199 | 207.309 | 3265.676 | 386.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8540) CPU | percent | 3 | 183.154 | 154.102 | 197.961 | 197.961 | 5.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8540) rss_mb | MB | 4 | 1739.565 | 385.516 | 2201.164 | 2201.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8540) main thread run-queue wait | percent | 3 | 39.784 | 19.708 | 50.249 | 49.394 | 1.201329 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8540) vms_mb | MB | 4 | 2017.647 | 840.703 | 2420.066 | 2420.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8554) CPU | percent | 2 | 155.985 | 110.352 | 201.617 | 201.617 | 3.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8554) rss_mb | MB | 3 | 1468.358 | 64.867 | 2200.426 | 2200.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8554) main thread run-queue wait | percent | 2 | 26.872 | 5.126 | 48.617 | 48.617 | 0.543479 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8554) vms_mb | MB | 3 | 1678.810 | 256.996 | 2420.031 | 2420.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sweep.py (PID 8562) CPU | percent | 18 | 196.065 | 138.206 | 202.177 | 201.767 | 35.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sweep.py (PID 8562) rss_mb | MB | 19 | 2056.050 | 213.156 | 2170.270 | 2169.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sweep.py (PID 8562) main thread run-queue wait | percent | 18 | 48.482 | 16.853 | 54.746 | 48.559 | 8.800655 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sweep.py (PID 8562) vms_mb | MB | 19 | 2297.046 | 840.695 | 2389.750 | 2389.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8589) CPU | percent | 5 | 184.210 | 117.893 | 201.194 | 201.054 | 9.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8589) rss_mb | MB | 6 | 1838.873 | 90.551 | 2200.785 | 2200.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8589) main thread run-queue wait | percent | 5 | 41.029 | 8.438 | 49.685 | 48.599 | 2.068981 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8589) vms_mb | MB | 6 | 2053.698 | 282.664 | 2420.035 | 2420.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8598) rss_mb | MB | 1 | 237.293 | 237.293 | 237.293 | 237.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8598) vms_mb | MB | 1 | 840.613 | 840.613 | 840.613 | 840.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8607) rss_mb | MB | 1 | 143.973 | 143.973 | 143.973 | 143.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8607) vms_mb | MB | 1 | 336.637 | 336.637 | 336.637 | 336.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8618) rss_mb | MB | 1 | 1383.875 | 1383.875 | 1383.875 | 1383.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8618) vms_mb | MB | 1 | 1810.594 | 1810.594 | 1810.594 | 1810.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8625) CPU | percent | 6 | 192.180 | 159.779 | 201.543 | 201.543 | 11.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8625) rss_mb | MB | 7 | 1937.681 | 638.934 | 2169.504 | 2169.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8625) main thread run-queue wait | percent | 6 | 46.346 | 23.856 | 53.494 | 50.225 | 2.805247 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8625) vms_mb | MB | 7 | 2155.479 | 840.715 | 2389.770 | 2389.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8637) CPU | percent | 8 | 194.733 | 164.009 | 201.699 | 198.842 | 15.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8637) rss_mb | MB | 9 | 1985.984 | 603.812 | 2170.133 | 2170.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8637) main thread run-queue wait | percent | 8 | 46.571 | 25.520 | 50.668 | 49.818 | 3.754871 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8637) vms_mb | MB | 9 | 2207.589 | 840.762 | 2389.816 | 2389.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8645) CPU | percent | 7 | 181.758 | 101.078 | 198.817 | 198.817 | 12.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8645) rss_mb | MB | 8 | 1918.328 | 0.000 | 2420.047 | 2139.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8645) main thread run-queue wait | percent | 7 | 42.539 | 11.181 | 50.970 | 50.538 | 2.995307 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8645) vms_mb | MB | 8 | 2128.630 | 0.387 | 2780.766 | 2359.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8663) CPU | percent | 9 | 191.001 | 124.260 | 202.816 | 202.816 | 17.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8663) rss_mb | MB | 10 | 1934.821 | 91.336 | 2139.719 | 2139.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8663) main thread run-queue wait | percent | 9 | 45.264 | 4.896 | 54.790 | 49.900 | 4.107337 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8663) vms_mb | MB | 10 | 2151.817 | 283.652 | 2359.395 | 2359.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8672) CPU | percent | 3 | 191.729 | 173.913 | 200.844 | 200.844 | 5.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8672) rss_mb | MB | 4 | 2123.070 | 2076.383 | 2138.633 | 2138.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8672) main thread run-queue wait | percent | 3 | 44.497 | 34.158 | 50.140 | 49.194 | 1.346265 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8672) vms_mb | MB | 4 | 2464.717 | 2359.398 | 2780.672 | 2359.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8682) CPU | percent | 3 | 183.035 | 151.727 | 199.397 | 197.982 | 5.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8682) rss_mb | MB | 4 | 1678.456 | 301.078 | 2137.582 | 2137.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8682) main thread run-queue wait | percent | 3 | 39.947 | 20.127 | 50.005 | 50.005 | 1.211813 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8682) vms_mb | MB | 4 | 1978.641 | 840.656 | 2357.969 | 2357.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8720) CPU | percent | 17 | 191.983 | 98.224 | 202.370 | 197.811 | 32.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8720) rss_mb | MB | 18 | 1945.697 | 13.176 | 2103.504 | 2103.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8720) main thread run-queue wait | percent | 17 | 47.062 | 10.369 | 54.557 | 49.378 | 8.076958 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8720) vms_mb | MB | 18 | 2181.129 | 207.223 | 2327.652 | 2327.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8732) rss_mb | MB | 1 | 21.637 | 21.637 | 21.637 | 21.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8732) vms_mb | MB | 1 | 213.777 | 213.777 | 213.777 | 213.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8746) CPU | percent | 9 | 196.223 | 179.804 | 199.475 | 197.764 | 17.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8746) rss_mb | MB | 10 | 2169.019 | 2139.129 | 2438.027 | 2139.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8746) main thread run-queue wait | percent | 9 | 48.363 | 36.129 | 50.663 | 50.663 | 4.379706 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8746) vms_mb | MB | 10 | 2401.557 | 2359.430 | 2780.703 | 2359.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8758) rss_mb | MB | 1 | 2.895 | 2.895 | 2.895 | 2.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8758) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8759) rss_mb | MB | 1 | 12.465 | 12.465 | 12.465 | 12.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8759) vms_mb | MB | 1 | 206.980 | 206.980 | 206.980 | 206.980 | n/a | n/a |
| docker commit (PID 8835) CPU | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 8835) io read MB/s | MB/s | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8835) io write MB/s | MB/s | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8835) rss_mb | MB | 18 | 30.137 | 30.137 | 30.137 | 30.137 | n/a | n/a |
| docker commit (PID 8835) main thread run-queue wait | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 8835) vms_mb | MB | 18 | 1843.262 | 1843.262 | 1843.262 | 1843.262 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 1661 | 23.812 | 0.000 | 204.813 | 0.000 | 398.738695 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1661 | 4.517 | 0.000 | 50.379 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1661 | 4.644 | 0.000 | 51.209 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 1661 | 0.041 | 0.000 | 39.695 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 1661 | 0.041 | 0.000 | 39.695 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 1661 | 0.031 | 0.000 | 11.541 | 0.000 | 51.996094 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 1661 | 0.001 | 0.000 | 0.587 | 0.000 | 1.625000 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 1662 | 380.525 | 39.961 | 2689.578 | 167.855 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1661 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1661 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 1661 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000854 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 1661 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 1662 | 4.741 | 1.500 | 101.629 | 1.724 | 79.422700 CPU seconds | n/a |
| workload total memory | MB | 1663 | 8794.067 | 8192.617 | 9001.508 | 9001.508 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
