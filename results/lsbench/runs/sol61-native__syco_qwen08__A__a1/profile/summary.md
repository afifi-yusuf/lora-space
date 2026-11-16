# agprof summary

- Duration: **2280.205 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **43 calls**, 43 succeeded, 0 failed, 0 interrupted, n/a reported retries, 2193.360 s total wait
- Tools: **66/66 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **210645** at 1.976 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2272690.973 / 2272690.973 ms |
| LLM latency p50 / p95 | 41132.562 / 122101.859 ms |
| LLM TTFT p50 / p95 | 22867.865 / 29210.125 ms |
| LLM input / output tokens | 2697981 / 66199 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 43 total, 43 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 406.719 / 1853.062 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 1/1 | 1 | 0 | 0 | 310.439 ms | 310.439 ms |
| bash | 15/15 | 15 | 0 | 0 | 507.974 ms | 876.380 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 313.377 ms | 313.377 ms |
| generate | 9/9 | 9 | 0 | 0 | 750.392 ms | 1103.735 ms |
| inspect | 1/1 | 1 | 0 | 0 | 1520.632 ms | 1520.632 ms |
| inspect_module_inputs | 3/3 | 3 | 0 | 0 | 3473.770 ms | 3523.845 ms |
| patch | 21/21 | 21 | 0 | 0 | 403.582 ms | 409.392 ms |
| read | 4/4 | 4 | 0 | 0 | 0.544 ms | 0.708 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 219.792 ms | 219.792 ms |
| todowrite | 2/2 | 2 | 0 | 0 | 0.128 ms | 0.128 ms |
| trace | 7/7 | 7 | 0 | 0 | 1429.891 ms | 1863.185 ms |
| write | 1/1 | 1 | 0 | 0 | 0.387 ms | 0.387 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 3.862% | 125.988% | 88.099 s | 5376.328 MB | 5566.027 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 4459 |  | 2267 | 0.103% | 5.962% | 2.350 s | 1782.984 MB | 1783.102 MB | 11992.930 MB | 11994.105 MB | 0.000000 MB | 0.050781 MB |
| lsb_grid_worker | 4441 |  | 2267 | 0.000% | 0.000% | 0.000 s | 3.320 MB | 3.320 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 4510 |  | 2267 | 1.498% | 39.594% | 34.130 s | 2326.073 MB | 2326.172 MB | 21828.582 MB | 21828.598 MB | 0.000000 MB | 0.011719 MB |
| tail | 4813 | sandbox_agent_lsb-native_0000_0000 | 2260 | 0.003% | 0.995% | 0.070 s | 1.473 MB | 1.473 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 4509 |  | 2267 | 0.000% | 0.000% | 0.000 s | 12.195 MB | 12.195 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4922 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.897% | 99.897% | 1.010 s | 55.965 MB | 82.902 MB | 67.521 MB | 98.148 MB | n/a MB | n/a MB |
| docker-init | 4773 | sandbox_agent_lsb-native_0000_0000 | 2260 | 0.003% | 0.995% | 0.060 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 4916 | sandbox_agent_lsb-native_0000_0000 | 2260 | 2.647% | 89.193% | 60.160 s | 106.576 MB | 113.066 MB | 970.320 MB | 973.766 MB | n/a MB | n/a MB |
| python | 4450 |  | 2267 | 2.254% | 124.291% | 51.470 s | 2740.424 MB | 2902.262 MB | 16330.717 MB | 16602.680 MB | 4.660156 MB | 298.859375 MB |
| python3 | 4934 | sandbox_agent_lsb-native_0000_0000 | 2234 | 0.136% | 58.697% | 3.050 s | 72.455 MB | 74.777 MB | 86.821 MB | 89.043 MB | n/a MB | n/a MB |
| python | 5205 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.574 MB | 20.574 MB | 132.266 MB | 132.266 MB | n/a MB | n/a MB |
| bash | 5204 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.000 MB | 3.000 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 5293 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 54.586 MB | 54.586 MB | 276.672 MB | 276.672 MB | n/a MB | n/a MB |
| bash | 5328 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 5329 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 27.707 MB | 27.707 MB | 139.281 MB | 139.281 MB | n/a MB | n/a MB |
| bash | 5363 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.137 MB | 3.137 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 5364 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 44.527 MB | 44.527 MB | 266.574 MB | 266.574 MB | n/a MB | n/a MB |
| python | 5471 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 45.652 MB | 45.652 MB | 267.168 MB | 267.168 MB | n/a MB | n/a MB |
| bash | 5517 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.797 MB | 2.797 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 5518 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 45.637 MB | 45.637 MB | 266.977 MB | 266.977 MB | n/a MB | n/a MB |
| python | 5579 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.055 MB | 8.055 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| docker | 5674 |  | 23 | 0.000% | 0.000% | 0.000 s | 28.871 MB | 28.871 MB | 1843.449 MB | 1843.449 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.586% | 97.000% | 11867.084 MB | 12108.000 MB | 28.124 W | 63.629 W | 64081.934 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 3.202% | 120.850% | 72.767 s | 181.239 MB | 228.254 MB | 26.769531 MB | 30.097656 MB | 0.001112 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4645 | 2280.142 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2272.691 | n/a | n/a | 26.770 | 2272690.973 | 2272690.973 | 2272690.973 |
| engine:execute | 1/1 | 0 | 0 | 2272.690 | 2.422 | 2270.267 | 26.770 | 2272689.508 | 2272689.508 | 2272689.508 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2246.423 | 0.003 | 2246.420 | 26.770 | 2246422.757 | 2246422.757 | 2246422.757 |
| turn | 43/43 | 0 | 0 | 2241.952 | n/a | n/a | 26.726 | 52138.429 | 42455.984 | 124062.022 |
| llm:attempt | 43/43 | 0 | 0 | 2193.360 | 6.163 | 2187.196 | 10.026 | 51008.368 | 41132.562 | 122101.859 |
| run:container_call | 13/13 | 0 | 0 | 22.976 | 0.002 | 22.974 | 0.000 | 1767.387 | 33.710 | 9046.843 |
| teardown:commit | 1/1 | 0 | 0 | 22.581 | 0.004 | 22.577 | 0.000 | 22580.724 | 22580.724 | 22580.724 |
| sandbox:commit | 1/1 | 0 | 0 | 22.399 | 0.002 | 22.397 | 0.000 | 22398.869 | 22398.869 | 22398.869 |
| checkpoint.total | 1/1 | 0 | 0 | 22.399 | 0.002 | 22.397 | 0.000 | 22398.739 | 22398.739 | 22398.739 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.399 | 0.002 | 22.397 | 0.000 | 22398.604 | 22398.604 | 22398.604 |
| tool:trace | 7/7 | 0 | 0 | 10.200 | n/a | n/a | 0.000 | 1457.097 | 1429.891 | 1863.185 |
| tool:inspect_module_inputs | 3/3 | 0 | 0 | 8.843 | n/a | n/a | 0.000 | 2947.771 | 3473.770 | 3523.845 |
| tool:patch | 21/21 | 0 | 0 | 8.473 | n/a | n/a | 0.050 | 403.464 | 403.582 | 409.392 |
| tool:bash | 15/15 | 0 | 0 | 7.329 | n/a | n/a | 15.840 | 488.623 | 507.974 | 876.380 |
| process:bash | 15/15 | 0 | 0 | 7.164 | n/a | n/a | 15.674 | 477.590 | 499.240 | 868.027 |
| tool:generate | 9/9 | 0 | 0 | 6.851 | n/a | n/a | 0.000 | 761.248 | 750.392 | 1103.735 |
| syscall:sendto | 1569/1569 | 0 | 0 | 3.111 | n/a | n/a | 0.435 | 1.983 | 1.729 | 3.871 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.064 | 0.702 | 2.362 | 0.000 | 3064.247 | 3064.247 | 3064.247 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.064 | 0.702 | 2.362 | 0.000 | 3063.949 | 3063.949 | 3063.949 |
| tool:inspect | 1/1 | 0 | 0 | 1.521 | n/a | n/a | 0.000 | 1520.632 | 1520.632 | 1520.632 |
| syscall:connect | 390/390 | 0 | 0 | 0.783 | n/a | n/a | 0.157 | 2.007 | 1.763 | 3.858 |
| sandbox:create | 1/1 | 0 | 0 | 0.338 | 0.246 | 0.092 | 0.000 | 338.184 | 338.184 | 338.184 |
| sandbox:start | 1/1 | 0 | 0 | 0.331 | 0.002 | 0.328 | 0.000 | 330.594 | 330.594 | 330.594 |
| runtime.container_create | 1/1 | 0 | 0 | 0.330 | 0.002 | 0.328 | 0.000 | 330.444 | 330.444 | 330.444 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.313 | n/a | n/a | 0.000 | 313.377 | 313.377 | 313.377 |
| tool:attention | 1/1 | 0 | 0 | 0.310 | n/a | n/a | 0.000 | 310.439 | 310.439 | 310.439 |
| tool:submit_output | 1/1 | 0 | 0 | 0.220 | n/a | n/a | 0.000 | 219.792 | 219.792 | 219.792 |
| sandbox:stop | 1/1 | 0 | 0 | 0.182 | 0.002 | 0.180 | 0.000 | 181.594 | 181.594 | 181.594 |
| agency:services_close | 1/1 | 0 | 0 | 0.145 | 0.000 | 0.145 | 0.000 | 145.108 | 145.108 | 145.108 |
| agency:services_start | 1/1 | 0 | 0 | 0.070 | 0.040 | 0.031 | 0.000 | 70.257 | 70.257 | 70.257 |
| syscall:execve | 54/54 | 0 | 0 | 0.069 | n/a | n/a | 0.100 | 1.278 | 1.107 | 1.811 |
| run:detect | 1/1 | 0 | 0 | 0.055 | 0.001 | 0.054 | 0.000 | 55.173 | 55.173 | 55.173 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.007 | 0.041 | 0.000 | 48.198 | 48.198 | 48.198 |
| tool:read | 4/4 | 0 | 0 | 0.002 | n/a | n/a | 0.000 | 0.481 | 0.544 | 0.708 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.647 | 1.647 | 1.647 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.220 | 1.220 | 1.220 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.069 | 0.069 | 0.099 |
| tool:write | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.387 | 0.387 | 0.387 |
| tool:todowrite | 2/2 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.128 | 0.128 | 0.128 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.191 | 0.191 | 0.191 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.063 | 0.063 | 0.063 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2266 | 0.421 | 0.041 | 55.681 | 0.070 | 9.604942 CPU seconds | n/a |
| GPU 0 memory | MB | 2267 | 11867.084 | 11670.000 | 12108.000 | 11860.000 | n/a | n/a |
| GPU 0 power | W | 2267 | 28.124 | 27.395 | 63.629 | 27.698 | n/a | 64081.934 J |
| GPU 0 proc / 4450-303406 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e memory | MB | 2267 | 3231.052 | 3118.000 | 3482.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 4450-303406 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e estimated power | W | 1581 | 0.853 | 0.000 | 57.046 | 0.000 | n/a | n/a |
| GPU 0 proc / 4450-303406 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e utilization | percent | 1581 | 0.577 | 0.000 | 47.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 4510-305150 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e memory | MB | 2267 | 8154.034 | 8070.000 | 8164.000 | 8164.000 | n/a | n/a |
| GPU 0 proc / 4510-305150 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e estimated power | W | 656 | 0.626 | 0.000 | 63.629 | 0.000 | n/a | n/a |
| GPU 0 proc / 4510-305150 / sandbox / ~ / device / GPU-5cb292f1-7c13-50ae-3bfc-268f4717bc7e utilization | percent | 656 | 0.566 | 0.000 | 79.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2267 | 11385.085 | 11188.000 | 11626.000 | 11378.000 | n/a | n/a |
| GPU 0 utilization | percent | 2267 | 0.586 | 0.000 | 97.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2267 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2266 | 0.340 | 0.027 | 12.330 | 0.137 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2266 | 0.791 | 0.000 | 20.050 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2266 | 0.723 | 0.000 | 189.463 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2266 | 0.162 | 0.000 | 16.192 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2266 | 0.309 | 0.000 | 66.209 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2266 | 0.309 | 0.000 | 66.233 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 2267 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 2267 | 6909.460 | 6356.723 | 7086.043 | 6991.395 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2266 | 0.000 | 0.000 | 0.007 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2266 | 0.000 | 0.000 | 0.007 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2266 | 0.003 | 0.000 | 0.249 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2266 | 0.008 | 0.000 | 0.819 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4441) CPU | percent | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4441) io read MB/s | MB/s | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4441) io write MB/s | MB/s | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4441) rss_mb | MB | 2267 | 3.320 | 3.320 | 3.320 | 3.320 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4441) main thread run-queue wait | percent | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4441) vms_mb | MB | 2267 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4450) CPU | percent | 2266 | 2.254 | 0.000 | 124.291 | 0.995 | 51.470000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 4450) io read MB/s | MB/s | 2266 | 0.002 | 0.000 | 1.725 | 0.000 | 4.660156 MB | n/a |
| Agency harness — python -m lsbench (PID 4450) io write MB/s | MB/s | 2266 | 0.131 | 0.015 | 16.333 | 0.023 | 298.859375 MB | n/a |
| Agency harness — python -m lsbench (PID 4450) rss_mb | MB | 2267 | 2740.424 | 2077.379 | 2902.262 | 2902.262 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4450) main thread run-queue wait | percent | 2266 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000046 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 4450) vms_mb | MB | 2267 | 16330.717 | 14148.910 | 16602.680 | 16467.238 | n/a | n/a |
| Python — vllm (PID 4459) CPU | percent | 2266 | 0.103 | 0.000 | 5.962 | 0.995 | 2.350000 CPU seconds | n/a |
| Python — vllm (PID 4459) io read MB/s | MB/s | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 4459) io write MB/s | MB/s | 2266 | 0.000 | 0.000 | 0.008 | 0.000 | 0.050781 MB | n/a |
| Python — vllm (PID 4459) rss_mb | MB | 2267 | 1782.984 | 1782.227 | 1783.102 | 1783.102 | n/a | n/a |
| Python — vllm (PID 4459) main thread run-queue wait | percent | 2266 | 0.000 | 0.000 | 0.042 | 0.000 | 0.004584 run-queue seconds | n/a |
| Python — vllm (PID 4459) vms_mb | MB | 2267 | 11992.930 | 11922.086 | 11994.105 | 11994.105 | n/a | n/a |
| Python — python -c (PID 4509) CPU | percent | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 4509) io read MB/s | MB/s | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4509) io write MB/s | MB/s | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4509) rss_mb | MB | 2267 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| Python — python -c (PID 4509) main thread run-queue wait | percent | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 4509) vms_mb | MB | 2267 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 4510) CPU | percent | 2266 | 1.498 | 0.000 | 39.594 | 2.986 | 34.130000 CPU seconds | n/a |
| VLLM::EngineCore (PID 4510) io read MB/s | MB/s | 2266 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 4510) io write MB/s | MB/s | 2266 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 4510) rss_mb | MB | 2267 | 2326.073 | 2325.793 | 2326.172 | 2326.172 | n/a | n/a |
| VLLM::EngineCore (PID 4510) main thread run-queue wait | percent | 2266 | 0.000 | 0.000 | 0.007 | 0.000 | 0.000306 run-queue seconds | n/a |
| VLLM::EngineCore (PID 4510) vms_mb | MB | 2267 | 21828.582 | 21828.582 | 21828.598 | 21828.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 4773) CPU | percent | 2259 | 0.003 | 0.000 | 0.995 | 0.000 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 4773) rss_mb | MB | 2260 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 4773) main thread run-queue wait | percent | 2259 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000156 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 4773) vms_mb | MB | 2260 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4813) CPU | percent | 2259 | 0.003 | 0.000 | 0.995 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4813) rss_mb | MB | 2260 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4813) main thread run-queue wait | percent | 2259 | 0.000 | 0.000 | 0.025 | 0.000 | 0.000435 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 4813) vms_mb | MB | 2260 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4916) CPU | percent | 2259 | 2.647 | 0.000 | 89.193 | 0.000 | 60.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4916) rss_mb | MB | 2260 | 106.576 | 2.855 | 113.066 | 109.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4916) main thread run-queue wait | percent | 2259 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000171 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4916) vms_mb | MB | 2260 | 970.320 | 4.258 | 973.766 | 973.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4922) CPU | percent | 1 | 99.897 | 99.897 | 99.897 | 99.897 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4922) rss_mb | MB | 2 | 55.965 | 29.027 | 82.902 | 82.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4922) main thread run-queue wait | percent | 1 | 0.012 | 0.012 | 0.012 | 0.012 | 0.000125 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4922) vms_mb | MB | 2 | 67.521 | 36.895 | 98.148 | 98.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 4934) CPU | percent | 2233 | 0.136 | 0.000 | 58.697 | 0.000 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 4934) rss_mb | MB | 2234 | 72.455 | 30.727 | 74.777 | 74.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 4934) main thread run-queue wait | percent | 2233 | 0.001 | 0.000 | 1.463 | 0.000 | 0.019411 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 4934) vms_mb | MB | 2234 | 86.821 | 36.270 | 89.043 | 88.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5204) rss_mb | MB | 1 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5204) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5205) rss_mb | MB | 1 | 20.574 | 20.574 | 20.574 | 20.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5205) vms_mb | MB | 1 | 132.266 | 132.266 | 132.266 | 132.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 5293) rss_mb | MB | 1 | 54.586 | 54.586 | 54.586 | 54.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 5293) vms_mb | MB | 1 | 276.672 | 276.672 | 276.672 | 276.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5328) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5328) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5329) rss_mb | MB | 1 | 27.707 | 27.707 | 27.707 | 27.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5329) vms_mb | MB | 1 | 139.281 | 139.281 | 139.281 | 139.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5363) rss_mb | MB | 1 | 3.137 | 3.137 | 3.137 | 3.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5363) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5364) rss_mb | MB | 1 | 44.527 | 44.527 | 44.527 | 44.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5364) vms_mb | MB | 1 | 266.574 | 266.574 | 266.574 | 266.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design_geometry.py (PID 5471) rss_mb | MB | 1 | 45.652 | 45.652 | 45.652 | 45.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design_geometry.py (PID 5471) vms_mb | MB | 1 | 267.168 | 267.168 | 267.168 | 267.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5517) rss_mb | MB | 1 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5517) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5518) rss_mb | MB | 1 | 45.637 | 45.637 | 45.637 | 45.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 5518) vms_mb | MB | 1 | 266.977 | 266.977 | 266.977 | 266.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_geometry.py (PID 5579) rss_mb | MB | 1 | 8.055 | 8.055 | 8.055 | 8.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_geometry.py (PID 5579) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| docker commit (PID 5674) CPU | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 5674) io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5674) io write MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5674) rss_mb | MB | 23 | 28.871 | 28.871 | 28.871 | 28.871 | n/a | n/a |
| docker commit (PID 5674) main thread run-queue wait | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 5674) vms_mb | MB | 23 | 1843.449 | 1843.449 | 1843.449 | 1843.449 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 2259 | 3.202 | 0.000 | 120.850 | 0.000 | 72.766802 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2259 | 0.503 | 0.000 | 11.790 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2259 | 0.503 | 0.000 | 12.264 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 2259 | 0.005 | 0.000 | 7.156 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 2259 | 0.005 | 0.000 | 7.156 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 2259 | 0.012 | 0.000 | 13.520 | 0.000 | 26.769531 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 2259 | 0.013 | 0.000 | 14.057 | 0.000 | 30.097656 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 2260 | 181.239 | 19.836 | 228.254 | 152.773 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2259 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2259 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 2259 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001112 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 2259 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 2266 | 3.862 | 1.787 | 125.988 | 2.041 | 88.099330 CPU seconds | n/a |
| workload total memory | MB | 2267 | 5376.328 | 4725.863 | 5566.027 | 5560.574 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
