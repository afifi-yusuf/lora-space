# agprof summary

- Duration: **1498.224 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **38 calls**, 38 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1319.748 s total wait
- Tools: **48/48 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **138555** at 1.981 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1498164.261 / 1498164.261 ms |
| LLM latency p50 / p95 | 18866.339 / 80574.423 ms |
| LLM TTFT p50 / p95 | 8507.788 / 20772.562 ms |
| LLM input / output tokens | 2908528 / 58813 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 38 total, 38 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 838.989 / 16262.788 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 18/18 | 18 | 0 | 0 | 474.125 ms | 2886.332 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 326.967 ms | 326.967 ms |
| edit | 1/1 | 1 | 0 | 0 | 0.795 ms | 0.795 ms |
| generate | 8/8 | 8 | 0 | 0 | 15183.845 ms | 27558.905 ms |
| inspect | 5/5 | 5 | 0 | 0 | 390.712 ms | 1848.674 ms |
| inspect_module_inputs | 2/2 | 2 | 0 | 0 | 1814.940 ms | 1912.813 ms |
| patch | 3/3 | 3 | 0 | 0 | 482.557 ms | 495.721 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 223.812 ms | 223.812 ms |
| trace | 5/5 | 5 | 0 | 0 | 3060.607 ms | 3261.963 ms |
| write | 4/4 | 4 | 0 | 0 | 0.538 ms | 0.603 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 7.252% | 101.717% | 108.785 s | 9275.813 MB | 9925.930 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lsb_grid_worker | 2292 |  | 1489 | 0.000% | 0.000% | 0.000 s | 3.387 MB | 3.387 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 4220 |  | 1489 | 2.637% | 101.453% | 39.530 s | 2607.985 MB | 3216.461 MB | 16174.553 MB | 16996.668 MB | 0.097656 MB | 835.175781 MB |
| python | 4279 |  | 1489 | 0.000% | 0.000% | 0.000 s | 12.199 MB | 12.199 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| bash | 4680 | sandbox_agent_lsb-native_0000_0000 | 1489 | 2.819% | 90.896% | 42.210 s | 105.818 MB | 114.488 MB | 968.138 MB | 973.953 MB | n/a MB | n/a MB |
| python3 | 4686 | sandbox_agent_lsb-native_0000_0000 | 2 | 98.895% | 98.895% | 1.000 s | 60.076 MB | 83.891 MB | 70.879 MB | 98.996 MB | n/a MB | n/a MB |
| tail | 4578 | sandbox_agent_lsb-native_0000_0000 | 1489 | 0.003% | 0.995% | 0.040 s | 1.449 MB | 1.449 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| docker-init | 4541 | sandbox_agent_lsb-native_0000_0000 | 1489 | 0.002% | 0.995% | 0.030 s | 0.582 MB | 0.582 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| vllm | 4229 |  | 1489 | 0.405% | 6.959% | 6.080 s | 1796.378 MB | 1796.602 MB | 12001.304 MB | 12007.328 MB | 0.003906 MB | 0.058594 MB |
| VLLM::EngineCor | 4280 |  | 1489 | 4.204% | 51.455% | 63.100 s | 2326.977 MB | 2327.117 MB | 21828.599 MB | 21828.742 MB | 0.000000 MB | 0.007812 MB |
| python3 | 4699 | sandbox_agent_lsb-native_0000_0000 | 1483 | 0.152% | 60.649% | 2.270 s | 74.852 MB | 77.605 MB | 87.565 MB | 89.934 MB | n/a MB | n/a MB |
| bash | 4713 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.918 MB | 2.918 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| ls | 4714 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.117 MB | 2.117 MB | 3.695 MB | 3.695 MB | n/a MB | n/a MB |
| python | 4772 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.995% | 1.990% | 0.020 s | 12.812 MB | 12.812 MB | 16.406 MB | 16.406 MB | n/a MB | n/a MB |
| python | 4778 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.426% | 99.426% | 1.000 s | 8.918 MB | 8.918 MB | 13.121 MB | 13.121 MB | n/a MB | n/a MB |
| python | 4790 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.980 MB | 4.980 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| python | 4843 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.660 MB | 12.660 MB | 16.527 MB | 16.527 MB | n/a MB | n/a MB |
| python | 4858 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.926 MB | 6.926 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| bash | 4840 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.004 MB | 3.004 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4909 | sandbox_agent_lsb-native_0000_0000 | 3 | 178.485% | 180.940% | 3.590 s | 74.493 MB | 82.602 MB | 336.475 MB | 363.402 MB | n/a MB | n/a MB |
| bash | 4907 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.082 MB | 3.082 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4939 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.605 MB | 12.605 MB | 16.379 MB | 16.379 MB | n/a MB | n/a MB |
| bash | 4938 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.961 MB | 2.961 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4952 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.730 MB | 9.730 MB | 13.535 MB | 13.535 MB | n/a MB | n/a MB |
| python | 5023 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.793 MB | 12.793 MB | 16.410 MB | 16.410 MB | n/a MB | n/a MB |
| bash | 5022 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.906 MB | 2.906 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 5044 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.355 MB | 8.355 MB | 13.152 MB | 13.152 MB | n/a MB | n/a MB |
| python | 5097 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 36.387 MB | 36.387 MB | 416.934 MB | 416.934 MB | n/a MB | n/a MB |
| bash | 5096 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.895 MB | 2.895 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 5275 | sandbox_agent_lsb-native_0000_0000 | 2 | 161.073% | 161.073% | 1.620 s | 207.434 MB | 374.680 MB | 598.471 MB | 775.977 MB | n/a MB | n/a MB |
| python | 5291 | sandbox_agent_lsb-native_0000_0000 | 3 | 167.304% | 187.773% | 3.370 s | 218.716 MB | 359.336 MB | 492.275 MB | 760.461 MB | n/a MB | n/a MB |
| docker | 5385 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.625 MB | 30.625 MB | 2060.281 MB | 2060.281 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 9.038% | 100.000% | 12076.449 MB | 12640.000 MB | 32.562 W | 73.941 W | 48762.418 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 4.424% | 200.606% | 66.255 s | 153.376 MB | 510.645 MB | 0.000000 MB | 9.582031 MB | 0.001045 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4412 | 1498.170 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 1/1 | 0 | 0 | 1498.165 | 0.000 | 1498.165 | 0.000 | 1498164.653 | 1498164.653 | 1498164.653 |
| run:write_lora_adapter | 1/1 | 0 | 0 | 1498.164 | n/a | n/a | 0.000 | 1498164.261 | 1498164.261 | 1498164.261 |
| engine:execute | 1/1 | 0 | 0 | 1498.163 | 2.027 | 1496.136 | 0.000 | 1498162.528 | 1498162.528 | 1498162.528 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1492.368 | 0.003 | 1492.366 | 0.000 | 1492368.428 | 1492368.428 | 1492368.428 |
| turn | 38/38 | 0 | 0 | 1488.834 | n/a | n/a | 0.000 | 39179.842 | 27271.193 | 80953.779 |
| llm:attempt | 38/38 | 0 | 0 | 1319.748 | 4.879 | 1314.867 | 0.000 | 34730.219 | 18866.339 | 80574.423 |
| tool:generate | 8/8 | 0 | 0 | 126.732 | n/a | n/a | 0.000 | 15841.442 | 15183.845 | 27558.905 |
| tool:bash | 18/18 | 0 | 0 | 16.417 | n/a | n/a | 0.000 | 912.047 | 474.125 | 2886.332 |
| process:bash | 18/18 | 0 | 0 | 16.269 | n/a | n/a | 0.000 | 903.853 | 466.145 | 2878.071 |
| tool:trace | 5/5 | 0 | 0 | 12.415 | n/a | n/a | 0.000 | 2483.065 | 3060.607 | 3261.963 |
| tool:inspect | 5/5 | 0 | 0 | 4.162 | n/a | n/a | 0.000 | 832.381 | 390.712 | 1848.674 |
| tool:inspect_module_inputs | 2/2 | 0 | 0 | 3.630 | n/a | n/a | 0.000 | 1814.940 | 1814.940 | 1912.813 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.053 | 0.723 | 2.330 | 0.000 | 3053.319 | 3053.319 | 3053.319 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.053 | 0.723 | 2.330 | 0.000 | 3052.996 | 3052.996 | 3052.996 |
| run:container_call | 13/13 | 0 | 0 | 2.405 | 0.002 | 2.403 | 0.000 | 185.029 | 35.349 | 815.810 |
| syscall:sendto | 1061/1061 | 0 | 0 | 2.373 | n/a | n/a | 0.000 | 2.237 | 1.811 | 4.397 |
| teardown:commit | 1/1 | 0 | 0 | 2.041 | 0.004 | 2.037 | 0.000 | 2041.043 | 2041.043 | 2041.043 |
| sandbox:commit | 1/1 | 0 | 0 | 1.877 | 0.002 | 1.874 | 0.000 | 1876.844 | 1876.844 | 1876.844 |
| checkpoint.total | 1/1 | 0 | 0 | 1.877 | 0.002 | 1.874 | 0.000 | 1876.709 | 1876.709 | 1876.709 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.877 | 0.002 | 1.874 | 0.000 | 1876.556 | 1876.556 | 1876.556 |
| tool:patch | 3/3 | 0 | 0 | 1.410 | n/a | n/a | 0.000 | 469.930 | 482.557 | 495.721 |
| syscall:connect | 288/288 | 0 | 0 | 0.621 | n/a | n/a | 0.000 | 2.157 | 1.860 | 4.099 |
| sandbox:create | 1/1 | 0 | 0 | 0.344 | 0.248 | 0.096 | 0.000 | 344.259 | 344.259 | 344.259 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.327 | n/a | n/a | 0.000 | 326.967 | 326.967 | 326.967 |
| sandbox:start | 1/1 | 0 | 0 | 0.300 | 0.003 | 0.298 | 0.000 | 300.110 | 300.110 | 300.110 |
| runtime.container_create | 1/1 | 0 | 0 | 0.300 | 0.002 | 0.298 | 0.000 | 299.959 | 299.959 | 299.959 |
| syscall:execve | 181/181 | 0 | 0 | 0.238 | n/a | n/a | 0.000 | 1.317 | 1.197 | 1.873 |
| tool:submit_output | 1/1 | 0 | 0 | 0.224 | n/a | n/a | 0.000 | 223.812 | 223.812 | 223.812 |
| agency:services_close | 1/1 | 0 | 0 | 0.201 | 0.000 | 0.200 | 0.000 | 200.777 | 200.777 | 200.777 |
| sandbox:stop | 1/1 | 0 | 0 | 0.164 | 0.001 | 0.162 | 0.000 | 163.927 | 163.927 | 163.927 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.042 | 0.031 | 0.000 | 72.978 | 72.978 | 72.978 |
| run:detect | 1/1 | 0 | 0 | 0.058 | 0.001 | 0.058 | 0.000 | 58.480 | 58.480 | 58.480 |
| agent:create | 1/1 | 0 | 0 | 0.038 | 0.008 | 0.029 | 0.000 | 37.732 | 37.732 | 37.732 |
| tool:write | 4/4 | 0 | 0 | 0.002 | n/a | n/a | 0.000 | 0.534 | 0.538 | 0.603 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.969 | 1.969 | 1.969 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.287 | 1.287 | 1.287 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.071 | 0.068 | 0.100 |
| tool:edit | 1/1 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.795 | 0.795 | 0.795 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.169 | 0.169 | 0.169 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.055 | 0.055 | 0.055 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1488 | 0.260 | 0.037 | 172.025 | 172.025 | 3.882896 CPU seconds | n/a |
| GPU 0 memory | MB | 1489 | 12076.449 | 11670.000 | 12640.000 | 11998.000 | n/a | n/a |
| GPU 0 power | W | 1489 | 32.562 | 28.070 | 73.941 | 28.136 | n/a | 48762.418 J |
| GPU 0 proc / 4220-252686 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c memory | MB | 1489 | 3313.913 | 3118.000 | 3828.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 4220-252686 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c estimated power | W | 1098 | 1.214 | 0.000 | 70.323 | 0.000 | n/a | n/a |
| GPU 0 proc / 4220-252686 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c utilization | percent | 1098 | 1.020 | 0.000 | 98.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 4280-254486 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c memory | MB | 1489 | 8280.536 | 8070.000 | 8330.000 | 8330.000 | n/a | n/a |
| GPU 0 proc / 4280-254486 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c estimated power | W | 380 | 22.642 | 0.000 | 73.064 | 0.000 | n/a | n/a |
| GPU 0 proc / 4280-254486 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c utilization | percent | 380 | 31.126 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1489 | 11594.449 | 11188.000 | 12158.000 | 11516.000 | n/a | n/a |
| GPU 0 utilization | percent | 1489 | 9.038 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1489 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1488 | 0.471 | 0.007 | 40.354 | 1.185 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1488 | 1.371 | 0.000 | 25.898 | 20.721 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1488 | 0.000 | 0.000 | 0.097 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1488 | 0.575 | 0.000 | 223.698 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1488 | 0.069 | 0.000 | 38.985 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1488 | 0.069 | 0.000 | 39.116 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1489 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1489 | 6851.224 | 6381.863 | 7449.660 | 7028.531 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1488 | 0.004 | 0.000 | 0.248 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1488 | 0.010 | 0.000 | 0.739 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2292) CPU | percent | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2292) io read MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2292) io write MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2292) rss_mb | MB | 1489 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2292) main thread run-queue wait | percent | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2292) vms_mb | MB | 1489 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4220) CPU | percent | 1488 | 2.637 | 0.000 | 101.453 | 0.000 | 39.530000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 4220) io read MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.097 | 0.000 | 0.097656 MB | n/a |
| Agency harness — python -m lsbench (PID 4220) io write MB/s | MB/s | 1488 | 0.557 | 0.000 | 224.113 | 0.051 | 835.175781 MB | n/a |
| Agency harness — python -m lsbench (PID 4220) rss_mb | MB | 1489 | 2607.985 | 2063.637 | 3216.461 | 2824.766 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4220) main thread run-queue wait | percent | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 4220) vms_mb | MB | 1489 | 16174.553 | 14147.887 | 16996.668 | 16394.262 | n/a | n/a |
| Python — vllm (PID 4229) CPU | percent | 1488 | 0.405 | 0.000 | 6.959 | 0.000 | 6.080000 CPU seconds | n/a |
| Python — vllm (PID 4229) io read MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 4229) io write MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.008 | 0.000 | 0.058594 MB | n/a |
| Python — vllm (PID 4229) rss_mb | MB | 1489 | 1796.378 | 1794.727 | 1796.602 | 1796.602 | n/a | n/a |
| Python — vllm (PID 4229) main thread run-queue wait | percent | 1488 | 0.000 | 0.000 | 0.246 | 0.000 | 0.006828 run-queue seconds | n/a |
| Python — vllm (PID 4229) vms_mb | MB | 1489 | 12001.304 | 11934.309 | 12007.328 | 12007.328 | n/a | n/a |
| Python — python -c (PID 4279) CPU | percent | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 4279) io read MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4279) io write MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4279) rss_mb | MB | 1489 | 12.199 | 12.199 | 12.199 | 12.199 | n/a | n/a |
| Python — python -c (PID 4279) main thread run-queue wait | percent | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 4279) vms_mb | MB | 1489 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 4280) CPU | percent | 1488 | 4.204 | 0.000 | 51.455 | 0.000 | 63.100000 CPU seconds | n/a |
| VLLM::EngineCore (PID 4280) io read MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 4280) io write MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 4280) rss_mb | MB | 1489 | 2326.977 | 2326.367 | 2327.117 | 2327.117 | n/a | n/a |
| VLLM::EngineCore (PID 4280) main thread run-queue wait | percent | 1488 | 0.000 | 0.000 | 0.018 | 0.000 | 0.007083 run-queue seconds | n/a |
| VLLM::EngineCore (PID 4280) vms_mb | MB | 1489 | 21828.599 | 21827.605 | 21828.742 | 21828.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 4541) CPU | percent | 1488 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 4541) rss_mb | MB | 1489 | 0.582 | 0.582 | 0.582 | 0.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 4541) main thread run-queue wait | percent | 1488 | 0.006 | 0.000 | 5.577 | 0.000 | 0.095884 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 4541) vms_mb | MB | 1489 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4578) CPU | percent | 1488 | 0.003 | 0.000 | 0.995 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4578) rss_mb | MB | 1489 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4578) main thread run-queue wait | percent | 1488 | 0.006 | 0.000 | 5.011 | 0.000 | 0.087401 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4578) vms_mb | MB | 1489 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4680) CPU | percent | 1488 | 2.819 | 0.000 | 90.896 | 0.000 | 42.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4680) rss_mb | MB | 1489 | 105.818 | 3.164 | 114.488 | 114.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4680) main thread run-queue wait | percent | 1488 | 0.000 | 0.000 | 0.015 | 0.000 | 0.000200 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4680) vms_mb | MB | 1489 | 968.138 | 4.258 | 973.953 | 972.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4686) CPU | percent | 1 | 98.895 | 98.895 | 98.895 | 98.895 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4686) rss_mb | MB | 2 | 60.076 | 36.262 | 83.891 | 83.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4686) main thread run-queue wait | percent | 1 | 0.007 | 0.007 | 0.007 | 0.007 | 0.000069 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4686) vms_mb | MB | 2 | 70.879 | 42.762 | 98.996 | 98.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 4699) CPU | percent | 1482 | 0.152 | 0.000 | 60.649 | 0.000 | 2.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 4699) rss_mb | MB | 1483 | 74.852 | 31.152 | 77.605 | 76.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 4699) main thread run-queue wait | percent | 1482 | 0.003 | 0.000 | 3.509 | 0.000 | 0.041183 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 4699) vms_mb | MB | 1483 | 87.565 | 36.254 | 89.934 | 88.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4713) rss_mb | MB | 1 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4713) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ls (PID 4714) rss_mb | MB | 1 | 2.117 | 2.117 | 2.117 | 2.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ls (PID 4714) vms_mb | MB | 1 | 3.695 | 3.695 | 3.695 | 3.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4772) CPU | percent | 2 | 0.995 | 0.000 | 1.990 | 1.990 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4772) rss_mb | MB | 3 | 12.812 | 12.812 | 12.812 | 12.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4772) main thread run-queue wait | percent | 2 | 0.002 | 0.000 | 0.005 | 0.005 | 0.000047 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4772) vms_mb | MB | 3 | 16.406 | 16.406 | 16.406 | 16.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4778) CPU | percent | 1 | 99.426 | 99.426 | 99.426 | 99.426 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4778) rss_mb | MB | 2 | 8.918 | 8.918 | 8.918 | 8.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4778) main thread run-queue wait | percent | 1 | 0.002 | 0.002 | 0.002 | 0.002 | 0.000021 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4778) vms_mb | MB | 2 | 13.121 | 13.121 | 13.121 | 13.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4790) rss_mb | MB | 1 | 4.980 | 4.980 | 4.980 | 4.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4790) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4840) rss_mb | MB | 1 | 3.004 | 3.004 | 3.004 | 3.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4840) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4843) rss_mb | MB | 1 | 12.660 | 12.660 | 12.660 | 12.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4843) vms_mb | MB | 1 | 16.527 | 16.527 | 16.527 | 16.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4858) rss_mb | MB | 1 | 6.926 | 6.926 | 6.926 | 6.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4858) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4907) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4907) rss_mb | MB | 3 | 3.082 | 3.082 | 3.082 | 3.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4907) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4907) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4909) CPU | percent | 2 | 178.485 | 176.029 | 180.940 | 176.029 | 3.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4909) rss_mb | MB | 3 | 74.493 | 58.277 | 82.602 | 82.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4909) main thread run-queue wait | percent | 2 | 36.391 | 33.389 | 39.392 | 39.392 | 0.731940 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4909) vms_mb | MB | 3 | 336.475 | 282.621 | 363.402 | 363.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4938) rss_mb | MB | 1 | 2.961 | 2.961 | 2.961 | 2.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4938) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4939) rss_mb | MB | 1 | 12.605 | 12.605 | 12.605 | 12.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4939) vms_mb | MB | 1 | 16.379 | 16.379 | 16.379 | 16.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4952) rss_mb | MB | 1 | 9.730 | 9.730 | 9.730 | 9.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4952) vms_mb | MB | 1 | 13.535 | 13.535 | 13.535 | 13.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5022) rss_mb | MB | 1 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5022) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 5023) rss_mb | MB | 1 | 12.793 | 12.793 | 12.793 | 12.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 5023) vms_mb | MB | 1 | 16.410 | 16.410 | 16.410 | 16.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5044) rss_mb | MB | 1 | 8.355 | 8.355 | 8.355 | 8.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5044) vms_mb | MB | 1 | 13.152 | 13.152 | 13.152 | 13.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5096) rss_mb | MB | 1 | 2.895 | 2.895 | 2.895 | 2.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5096) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5097) rss_mb | MB | 1 | 36.387 | 36.387 | 36.387 | 36.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5097) vms_mb | MB | 1 | 416.934 | 416.934 | 416.934 | 416.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — construct_readouts.py (PID 5275) CPU | percent | 1 | 161.073 | 161.073 | 161.073 | 161.073 | 1.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — construct_readouts.py (PID 5275) rss_mb | MB | 2 | 207.434 | 40.188 | 374.680 | 374.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — construct_readouts.py (PID 5275) main thread run-queue wait | percent | 1 | 35.844 | 35.844 | 35.844 | 35.844 | 0.360502 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — construct_readouts.py (PID 5275) vms_mb | MB | 2 | 598.471 | 420.965 | 775.977 | 775.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — construct_readouts.py (PID 5291) CPU | percent | 2 | 167.304 | 146.834 | 187.773 | 187.773 | 3.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — construct_readouts.py (PID 5291) rss_mb | MB | 3 | 218.716 | 0.000 | 359.336 | 296.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — construct_readouts.py (PID 5291) main thread run-queue wait | percent | 2 | 35.369 | 26.771 | 43.966 | 43.966 | 0.712367 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — construct_readouts.py (PID 5291) vms_mb | MB | 3 | 492.275 | 0.387 | 760.461 | 715.977 | n/a | n/a |
| docker commit (PID 5385) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 5385) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5385) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5385) rss_mb | MB | 2 | 30.625 | 30.625 | 30.625 | 30.625 | n/a | n/a |
| docker commit (PID 5385) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 5385) vms_mb | MB | 2 | 2060.281 | 2060.281 | 2060.281 | 2060.281 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 1488 | 4.424 | 0.000 | 200.606 | 0.000 | 66.254747 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1488 | 0.597 | 0.000 | 38.624 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1488 | 0.599 | 0.000 | 40.015 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 1488 | 0.000 | 0.000 | 0.002 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 1488 | 0.000 | 0.000 | 0.002 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 1488 | 0.006 | 0.000 | 7.646 | 0.000 | 9.582031 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 1489 | 153.376 | 25.605 | 510.645 | 108.043 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001045 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 1488 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 1488 | 7.252 | 1.393 | 101.717 | 1.520 | 108.784739 CPU seconds | n/a |
| workload total memory | MB | 1489 | 9275.813 | 8558.797 | 9925.930 | 9638.211 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
