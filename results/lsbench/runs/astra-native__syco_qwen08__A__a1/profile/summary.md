# agprof summary

- Duration: **1797.533 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **38 calls**, 38 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1712.138 s total wait
- Tools: **60/60 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **166270** at 1.981 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1797462.576 / 1797462.576 ms |
| LLM latency p50 / p95 | 38078.178 / 99621.989 ms |
| LLM TTFT p50 / p95 | 18659.738 / 22132.634 ms |
| LLM input / output tokens | 2505535 / 65239 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 38 total, 38 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 463.888 / 2688.466 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 1/1 | 1 | 0 | 0 | 376.277 ms | 376.277 ms |
| attribution | 2/2 | 2 | 0 | 0 | 302.071 ms | 304.466 ms |
| bash | 18/18 | 18 | 0 | 0 | 731.987 ms | 3555.933 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 388.892 ms | 388.892 ms |
| generate | 10/10 | 10 | 0 | 0 | 435.029 ms | 1280.819 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 2675.187 ms | 2675.187 ms |
| patch | 12/12 | 12 | 0 | 0 | 403.725 ms | 415.428 ms |
| read | 5/5 | 5 | 0 | 0 | 0.360 ms | 0.474 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 243.636 ms | 243.636 ms |
| trace | 9/9 | 9 | 0 | 0 | 1738.575 ms | 2118.996 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 3.741% | 101.556% | 67.264 s | 8694.362 MB | 8880.172 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VLLM::EngineCor | 2357 |  | 1787 | 1.325% | 58.420% | 23.800 s | 2552.383 MB | 2552.418 MB | 21437.289 MB | 21437.289 MB | 0.000000 MB | 0.011719 MB |
| python | 2356 |  | 1787 | 0.000% | 0.000% | 0.000 s | 12.371 MB | 12.371 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 2306 |  | 1787 | 0.104% | 5.969% | 1.860 s | 1787.457 MB | 1787.477 MB | 12022.419 MB | 12023.668 MB | 0.003906 MB | 0.042969 MB |
| docker | 2683 |  | 1 | n/a% | n/a% | n/a s | 29.352 MB | 29.352 MB | 2060.523 MB | 2060.523 MB | n/a MB | n/a MB |
| docker-buildx | 2697 |  | 1 | n/a% | n/a% | n/a s | 41.660 MB | 41.660 MB | 1298.969 MB | 1298.969 MB | n/a MB | n/a MB |
| lsb_grid_worker | 2292 |  | 1787 | 0.000% | 0.000% | 0.000 s | 3.387 MB | 3.387 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 2297 |  | 1787 | 2.295% | 101.099% | 41.290 s | 2537.154 MB | 2682.555 MB | 16153.505 MB | 16331.320 MB | 170.609375 MB | 417.277344 MB |
| docker-init | 2810 | sandbox_agent_lsb-native_0000_0000 | 1786 | 0.003% | 0.995% | 0.050 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2852 | sandbox_agent_lsb-native_0000_0000 | 1786 | 0.003% | 0.995% | 0.050 s | 1.402 MB | 1.402 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 2957 | sandbox_agent_lsb-native_0000_0000 | 3 | 56.193% | 63.674% | 1.130 s | 40.250 MB | 66.402 MB | 47.201 MB | 75.137 MB | n/a MB | n/a MB |
| bash | 2951 | sandbox_agent_lsb-native_0000_0000 | 1786 | 3.115% | 99.438% | 55.950 s | 104.726 MB | 110.957 MB | 967.878 MB | 973.332 MB | n/a MB | n/a MB |
| python3 | 2969 | sandbox_agent_lsb-native_0000_0000 | 1759 | 0.158% | 59.669% | 2.790 s | 72.744 MB | 75.266 MB | 87.030 MB | 89.402 MB | n/a MB | n/a MB |
| bash | 3133 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.715 MB | 2.715 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3135 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 47.688 MB | 47.688 MB | 190.035 MB | 190.035 MB | n/a MB | n/a MB |
| python | 3232 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 24.355 MB | 24.355 MB | 95.848 MB | 95.848 MB | n/a MB | n/a MB |
| python | 3303 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 37.949 MB | 37.949 MB | 177.715 MB | 177.715 MB | n/a MB | n/a MB |
| bash | 3302 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.051 MB | 3.051 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3347 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 24.090 MB | 24.090 MB | 95.812 MB | 95.812 MB | n/a MB | n/a MB |
| bash | 3342 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.910 MB | 2.910 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3406 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.965 MB | 2.965 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3408 | sandbox_agent_lsb-native_0000_0000 | 3 | 94.689% | 100.069% | 1.910 s | 152.820 MB | 221.000 MB | 629.240 MB | 899.086 MB | n/a MB | n/a MB |
| python | 3415 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 176.480 MB | 176.480 MB | 347.625 MB | 347.625 MB | n/a MB | n/a MB |
| python | 3422 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 139.680 MB | 139.680 MB | 289.348 MB | 289.348 MB | n/a MB | n/a MB |
| python | 3449 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 72.965 MB | 72.965 MB | 245.000 MB | 245.000 MB | n/a MB | n/a MB |
| bash | 3448 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.898 MB | 2.898 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3454 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.074 MB | 3.074 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3455 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 72.117 MB | 72.117 MB | 213.832 MB | 213.832 MB | n/a MB | n/a MB |
| python | 3461 | sandbox_agent_lsb-native_0000_0000 | 4 | 67.954% | 68.640% | 2.050 s | 142.998 MB | 171.742 MB | 316.317 MB | 373.691 MB | n/a MB | n/a MB |
| python | 3529 | sandbox_agent_lsb-native_0000_0000 | 4 | 66.927% | 68.634% | 2.020 s | 148.968 MB | 180.785 MB | 320.585 MB | 382.441 MB | n/a MB | n/a MB |
| docker | 3590 |  | 1 | n/a% | n/a% | n/a s | 22.152 MB | 22.152 MB | 1625.848 MB | 1625.848 MB | n/a MB | n/a MB |
| docker | 3623 |  | 21 | 0.000% | 0.000% | 0.000 s | 31.027 MB | 31.027 MB | 2196.598 MB | 2196.598 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.434% | 100.000% | 11515.605 MB | 11554.000 MB | 28.531 W | 72.528 W | 51240.299 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 4.193% | 168.522% | 75.320 s | 241.267 MB | 432.277 MB | 80.765625 MB | 1.628906 MB | 0.001251 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2681 | 1797.468 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1797.463 | n/a | n/a | 80.766 | 1797462.576 | 1797462.576 | 1797462.576 |
| sync:result_wait | 1/1 | 0 | 0 | 1797.462 | 0.000 | 1797.462 | 80.766 | 1797462.480 | 1797462.480 | 1797462.480 |
| engine:execute | 1/1 | 0 | 0 | 1797.461 | 2.556 | 1794.904 | 80.766 | 1797461.015 | 1797461.015 | 1797461.015 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1769.341 | 0.003 | 1769.338 | 42.235 | 1769340.541 | 1769340.541 | 1769340.541 |
| turn | 38/38 | 0 | 0 | 1765.842 | n/a | n/a | 39.837 | 46469.523 | 39826.618 | 101879.133 |
| llm:attempt | 38/38 | 0 | 0 | 1712.138 | 4.863 | 1707.273 | 17.764 | 45056.252 | 38078.178 | 99621.989 |
| run:container_call | 13/13 | 0 | 0 | 22.427 | 0.003 | 22.424 | 0.001 | 1725.127 | 35.605 | 8869.931 |
| teardown:commit | 1/1 | 0 | 0 | 21.750 | 0.004 | 21.746 | 0.001 | 21750.419 | 21750.419 | 21750.419 |
| sandbox:commit | 1/1 | 0 | 0 | 21.569 | 0.003 | 21.566 | 0.001 | 21568.578 | 21568.578 | 21568.578 |
| checkpoint.total | 1/1 | 0 | 0 | 21.568 | 0.002 | 21.566 | 0.001 | 21568.413 | 21568.413 | 21568.413 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 21.568 | 0.002 | 21.566 | 0.001 | 21568.236 | 21568.236 | 21568.236 |
| tool:bash | 18/18 | 0 | 0 | 20.510 | n/a | n/a | 20.325 | 1139.442 | 731.987 | 3555.933 |
| process:bash | 18/18 | 0 | 0 | 20.342 | n/a | n/a | 20.096 | 1130.129 | 722.593 | 3547.020 |
| tool:trace | 9/9 | 0 | 0 | 14.517 | n/a | n/a | 0.000 | 1612.948 | 1738.575 | 2118.996 |
| tool:generate | 10/10 | 0 | 0 | 5.669 | n/a | n/a | 0.000 | 566.864 | 435.029 | 1280.819 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.972 | 1.099 | 3.873 | 38.465 | 4971.836 | 4971.836 | 4971.836 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.972 | 1.098 | 3.873 | 38.464 | 4971.640 | 4971.640 | 4971.640 |
| tool:patch | 12/12 | 0 | 0 | 4.871 | n/a | n/a | 0.000 | 405.938 | 403.725 | 415.428 |
| syscall:sendto | 1373/1373 | 0 | 0 | 2.994 | n/a | n/a | 0.918 | 2.181 | 1.799 | 4.116 |
| tool:logit_lens | 1/1 | 0 | 0 | 2.675 | n/a | n/a | 0.000 | 2675.187 | 2675.187 | 2675.187 |
| sandbox:create | 1/1 | 0 | 0 | 1.049 | 0.260 | 0.789 | 0.000 | 1048.725 | 1048.725 | 1048.725 |
| run:detect | 1/1 | 0 | 0 | 0.737 | 0.001 | 0.736 | 0.000 | 737.233 | 737.233 | 737.233 |
| syscall:connect | 340/340 | 0 | 0 | 0.701 | n/a | n/a | 0.215 | 2.062 | 1.782 | 4.216 |
| sandbox:start | 1/1 | 0 | 0 | 0.610 | 0.002 | 0.607 | 0.000 | 609.570 | 609.570 | 609.570 |
| runtime.container_create | 1/1 | 0 | 0 | 0.609 | 0.002 | 0.607 | 0.000 | 609.429 | 609.429 | 609.429 |
| tool:attribution | 2/2 | 0 | 0 | 0.604 | n/a | n/a | 0.000 | 302.071 | 302.071 | 304.466 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.389 | n/a | n/a | 0.000 | 388.892 | 388.892 | 388.892 |
| tool:attention | 1/1 | 0 | 0 | 0.376 | n/a | n/a | 0.000 | 376.277 | 376.277 | 376.277 |
| tool:submit_output | 1/1 | 0 | 0 | 0.244 | n/a | n/a | 0.000 | 243.636 | 243.636 | 243.636 |
| sandbox:stop | 1/1 | 0 | 0 | 0.182 | 0.002 | 0.180 | 0.000 | 181.582 | 181.582 | 181.582 |
| agency:services_close | 1/1 | 0 | 0 | 0.158 | 0.000 | 0.158 | 0.011 | 158.352 | 158.352 | 158.352 |
| agency:services_start | 1/1 | 0 | 0 | 0.108 | 0.045 | 0.063 | 0.000 | 107.599 | 107.599 | 107.599 |
| syscall:execve | 72/72 | 0 | 0 | 0.107 | n/a | n/a | 0.163 | 1.490 | 1.174 | 3.206 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.007 | 0.041 | 0.000 | 48.311 | 48.311 | 48.311 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.658 | 1.658 | 1.658 |
| tool:read | 5/5 | 0 | 0 | 0.001 | n/a | n/a | 0.006 | 0.298 | 0.360 | 0.474 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.267 | 1.267 | 1.267 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.075 | 0.079 | 0.109 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.196 | 0.196 | 0.196 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.066 | 0.066 | 0.066 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1785 | 0.413 | 0.041 | 40.296 | 39.772 | 7.413210 CPU seconds | n/a |
| GPU 0 memory | MB | 1787 | 11515.605 | 11326.000 | 11554.000 | 11522.000 | n/a | n/a |
| GPU 0 power | W | 1787 | 28.531 | 28.056 | 72.528 | 28.137 | n/a | 51240.299 J |
| GPU 0 proc / 2297-26509 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c memory | MB | 1787 | 3218.385 | 3118.000 | 3254.000 | 3222.000 | n/a | n/a |
| GPU 0 proc / 2297-26509 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c estimated power | W | 1440 | 0.773 | 0.000 | 53.146 | 0.000 | n/a | n/a |
| GPU 0 proc / 2297-26509 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c utilization | percent | 1440 | 0.452 | 0.000 | 47.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2357-29920 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c memory | MB | 1787 | 7815.220 | 7726.000 | 7818.000 | 7818.000 | n/a | n/a |
| GPU 0 proc / 2357-29920 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c estimated power | W | 331 | 1.036 | 0.000 | 63.099 | 6.553 | n/a | n/a |
| GPU 0 proc / 2357-29920 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c utilization | percent | 331 | 0.677 | 0.000 | 87.000 | 6.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1787 | 11033.605 | 10844.000 | 11072.000 | 11040.000 | n/a | n/a |
| GPU 0 utilization | percent | 1787 | 0.434 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1787 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1786 | 0.284 | 0.013 | 7.487 | 0.696 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1786 | 0.929 | 0.000 | 21.231 | 4.087 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1786 | 1.018 | 0.000 | 191.759 | 8.847 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1786 | 0.262 | 0.000 | 61.247 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1786 | 0.526 | 0.000 | 87.874 | 17.686 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1786 | 0.527 | 0.000 | 87.946 | 17.715 | n/a | n/a |
| host mem_total_mb | MB | 1787 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1787 | 6954.698 | 6392.137 | 7210.664 | 7052.691 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1786 | 0.000 | 0.000 | 0.013 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1786 | 0.000 | 0.000 | 0.013 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1786 | 0.003 | 0.000 | 0.249 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1786 | 0.008 | 0.000 | 0.827 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2292) CPU | percent | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2292) io read MB/s | MB/s | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2292) io write MB/s | MB/s | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2292) rss_mb | MB | 1787 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2292) main thread run-queue wait | percent | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2292) vms_mb | MB | 1787 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2297) CPU | percent | 1786 | 2.295 | 0.000 | 101.099 | 0.000 | 41.290000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2297) io read MB/s | MB/s | 1786 | 0.095 | 0.000 | 93.105 | 0.000 | 170.609375 MB | n/a |
| Agency harness — python -m lsbench (PID 2297) io write MB/s | MB/s | 1786 | 0.232 | 0.016 | 61.645 | 0.023 | 417.277344 MB | n/a |
| Agency harness — python -m lsbench (PID 2297) rss_mb | MB | 1787 | 2537.154 | 1875.871 | 2682.555 | 2672.055 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2297) main thread run-queue wait | percent | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2297) vms_mb | MB | 1787 | 16153.505 | 13935.828 | 16331.320 | 16236.199 | n/a | n/a |
| Python — vllm (PID 2306) CPU | percent | 1786 | 0.104 | 0.000 | 5.969 | 0.000 | 1.860000 CPU seconds | n/a |
| Python — vllm (PID 2306) io read MB/s | MB/s | 1786 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 2306) io write MB/s | MB/s | 1786 | 0.000 | 0.000 | 0.008 | 0.000 | 0.042969 MB | n/a |
| Python — vllm (PID 2306) rss_mb | MB | 1787 | 1787.457 | 1786.727 | 1787.477 | 1787.477 | n/a | n/a |
| Python — vllm (PID 2306) main thread run-queue wait | percent | 1786 | 0.000 | 0.000 | 0.099 | 0.000 | 0.003791 run-queue seconds | n/a |
| Python — vllm (PID 2306) vms_mb | MB | 1787 | 12022.419 | 11951.648 | 12023.668 | 12023.668 | n/a | n/a |
| Python — python -c (PID 2356) CPU | percent | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2356) io read MB/s | MB/s | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2356) io write MB/s | MB/s | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2356) rss_mb | MB | 1787 | 12.371 | 12.371 | 12.371 | 12.371 | n/a | n/a |
| Python — python -c (PID 2356) main thread run-queue wait | percent | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2356) vms_mb | MB | 1787 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2357) CPU | percent | 1786 | 1.325 | 0.000 | 58.420 | 0.000 | 23.800000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2357) io read MB/s | MB/s | 1786 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 2357) io write MB/s | MB/s | 1786 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 2357) rss_mb | MB | 1787 | 2552.383 | 2552.168 | 2552.418 | 2552.418 | n/a | n/a |
| VLLM::EngineCore (PID 2357) main thread run-queue wait | percent | 1786 | 0.000 | 0.000 | 0.006 | 0.000 | 0.000257 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2357) vms_mb | MB | 1787 | 21437.289 | 21437.289 | 21437.289 | 21437.289 | n/a | n/a |
| docker info (PID 2683) rss_mb | MB | 1 | 29.352 | 29.352 | 29.352 | 29.352 | n/a | n/a |
| docker info (PID 2683) vms_mb | MB | 1 | 2060.523 | 2060.523 | 2060.523 | 2060.523 | n/a | n/a |
| docker-buildx (PID 2697) rss_mb | MB | 1 | 41.660 | 41.660 | 41.660 | 41.660 | n/a | n/a |
| docker-buildx (PID 2697) vms_mb | MB | 1 | 1298.969 | 1298.969 | 1298.969 | 1298.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2810) CPU | percent | 1785 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2810) rss_mb | MB | 1786 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2810) main thread run-queue wait | percent | 1785 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000171 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2810) vms_mb | MB | 1786 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2852) CPU | percent | 1785 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2852) rss_mb | MB | 1786 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2852) main thread run-queue wait | percent | 1785 | 0.000 | 0.000 | 0.004 | 0.000 | 0.000269 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2852) vms_mb | MB | 1786 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2951) CPU | percent | 1785 | 3.115 | 0.000 | 99.438 | 0.000 | 55.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2951) rss_mb | MB | 1786 | 104.726 | 2.992 | 110.957 | 107.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2951) main thread run-queue wait | percent | 1785 | 0.000 | 0.000 | 0.006 | 0.000 | 0.000073 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2951) vms_mb | MB | 1786 | 967.878 | 4.258 | 973.332 | 973.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2957) CPU | percent | 2 | 56.193 | 48.713 | 63.674 | 63.674 | 1.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2957) rss_mb | MB | 3 | 40.250 | 9.223 | 66.402 | 66.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2957) main thread run-queue wait | percent | 2 | 0.042 | 0.039 | 0.044 | 0.039 | 0.000843 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2957) vms_mb | MB | 3 | 47.201 | 13.410 | 75.137 | 75.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2969) CPU | percent | 1758 | 0.158 | 0.000 | 59.669 | 0.000 | 2.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2969) rss_mb | MB | 1759 | 72.744 | 30.793 | 75.266 | 74.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2969) main thread run-queue wait | percent | 1758 | 0.003 | 0.000 | 4.674 | 0.000 | 0.050240 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2969) vms_mb | MB | 1759 | 87.030 | 36.262 | 89.402 | 88.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3133) rss_mb | MB | 1 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3133) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_geometry.py (PID 3135) rss_mb | MB | 1 | 47.688 | 47.688 | 47.688 | 47.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_geometry.py (PID 3135) vms_mb | MB | 1 | 190.035 | 190.035 | 190.035 | 190.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_heads.py (PID 3232) rss_mb | MB | 1 | 24.355 | 24.355 | 24.355 | 24.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_heads.py (PID 3232) vms_mb | MB | 1 | 95.848 | 95.848 | 95.848 | 95.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3302) rss_mb | MB | 1 | 3.051 | 3.051 | 3.051 | 3.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3302) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3303) rss_mb | MB | 1 | 37.949 | 37.949 | 37.949 | 37.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3303) vms_mb | MB | 1 | 177.715 | 177.715 | 177.715 | 177.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3342) rss_mb | MB | 1 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3342) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry_generalization.py (PID 3347) rss_mb | MB | 1 | 24.090 | 24.090 | 24.090 | 24.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry_generalization.py (PID 3347) vms_mb | MB | 1 | 95.812 | 95.812 | 95.812 | 95.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3406) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3406) rss_mb | MB | 3 | 2.965 | 2.965 | 2.965 | 2.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3406) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3406) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — component_attribution.py (PID 3408) CPU | percent | 2 | 94.689 | 89.309 | 100.069 | 100.069 | 1.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — component_attribution.py (PID 3408) rss_mb | MB | 3 | 152.820 | 25.855 | 221.000 | 221.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — component_attribution.py (PID 3408) main thread run-queue wait | percent | 2 | 0.012 | 0.005 | 0.019 | 0.005 | 0.000246 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — component_attribution.py (PID 3408) vms_mb | MB | 3 | 629.240 | 97.547 | 899.086 | 899.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gate_geometry.py (PID 3415) rss_mb | MB | 1 | 176.480 | 176.480 | 176.480 | 176.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gate_geometry.py (PID 3415) vms_mb | MB | 1 | 347.625 | 347.625 | 347.625 | 347.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gate_control_design.py (PID 3422) rss_mb | MB | 1 | 139.680 | 139.680 | 139.680 | 139.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gate_control_design.py (PID 3422) vms_mb | MB | 1 | 289.348 | 289.348 | 289.348 | 289.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3448) rss_mb | MB | 1 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3448) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3449) rss_mb | MB | 1 | 72.965 | 72.965 | 72.965 | 72.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3449) vms_mb | MB | 1 | 245.000 | 245.000 | 245.000 | 245.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3454) rss_mb | MB | 1 | 3.074 | 3.074 | 3.074 | 3.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3454) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3455) rss_mb | MB | 1 | 72.117 | 72.117 | 72.117 | 72.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3455) vms_mb | MB | 1 | 213.832 | 213.832 | 213.832 | 213.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — guarded_readout.py (PID 3461) CPU | percent | 3 | 67.954 | 67.604 | 68.640 | 67.618 | 2.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — guarded_readout.py (PID 3461) rss_mb | MB | 4 | 142.998 | 76.680 | 171.742 | 171.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — guarded_readout.py (PID 3461) main thread run-queue wait | percent | 3 | 0.080 | 0.073 | 0.083 | 0.083 | 0.002402 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — guarded_readout.py (PID 3461) vms_mb | MB | 4 | 316.317 | 223.609 | 373.691 | 373.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — robust_readout.py (PID 3529) CPU | percent | 3 | 66.927 | 65.620 | 68.634 | 66.528 | 2.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — robust_readout.py (PID 3529) rss_mb | MB | 4 | 148.968 | 93.973 | 180.785 | 180.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — robust_readout.py (PID 3529) main thread run-queue wait | percent | 3 | 0.087 | 0.077 | 0.094 | 0.094 | 0.002617 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — robust_readout.py (PID 3529) vms_mb | MB | 4 | 320.585 | 235.598 | 382.441 | 382.441 | n/a | n/a |
| docker inspect (PID 3590) rss_mb | MB | 1 | 22.152 | 22.152 | 22.152 | 22.152 | n/a | n/a |
| docker inspect (PID 3590) vms_mb | MB | 1 | 1625.848 | 1625.848 | 1625.848 | 1625.848 | n/a | n/a |
| docker commit (PID 3623) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 3623) io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3623) io write MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3623) rss_mb | MB | 21 | 31.027 | 31.027 | 31.027 | 31.027 | n/a | n/a |
| docker commit (PID 3623) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 3623) vms_mb | MB | 21 | 2196.598 | 2196.598 | 2196.598 | 2196.598 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 1785 | 4.193 | 0.000 | 168.522 | 0.000 | 75.319510 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1785 | 0.413 | 0.000 | 7.055 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1785 | 0.413 | 0.000 | 7.392 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 1785 | 0.058 | 0.000 | 36.756 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 1785 | 0.058 | 0.000 | 36.756 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 1785 | 0.045 | 0.000 | 20.496 | 0.000 | 80.765625 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 1785 | 0.001 | 0.000 | 0.761 | 0.000 | 1.628906 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 1786 | 241.267 | 19.473 | 432.277 | 193.969 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1785 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1785 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 1785 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001251 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 1785 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 1786 | 3.741 | 1.430 | 101.556 | 1.914 | 67.264290 CPU seconds | n/a |
| workload total memory | MB | 1787 | 8694.362 | 7925.398 | 8880.172 | 8879.996 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
