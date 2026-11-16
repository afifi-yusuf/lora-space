# agprof summary

- Duration: **570.106 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.002 runs/s**
- LLM: **32 calls**, 32 succeeded, 0 failed, 0 interrupted, n/a reported retries, 331.505 s total wait
- Tools: **40/40 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **59341** at 1.975 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 569076.374 / 569076.374 ms |
| LLM latency p50 / p95 | 8436.124 / 23996.591 ms |
| LLM TTFT p50 / p95 | 1774.584 / 2790.209 ms |
| LLM input / output tokens | 2171677 / 38646 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 32 total, 32 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 349.412 / 37389.102 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 21/21 | 21 | 0 | 0 | 110.351 ms | 782.701 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 329.797 ms | 329.797 ms |
| generate | 6/6 | 6 | 0 | 0 | 22549.166 ms | 70033.999 ms |
| inspect | 1/1 | 1 | 0 | 0 | 1764.599 ms | 1764.599 ms |
| inspect_module_inputs | 1/1 | 1 | 0 | 0 | 1911.119 ms | 1911.119 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 4382.994 ms | 4382.994 ms |
| read | 4/4 | 4 | 0 | 0 | 0.589 ms | 1.401 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 235.414 ms | 235.414 ms |
| todowrite | 2/2 | 2 | 0 | 0 | 0.172 ms | 0.187 ms |
| trace | 2/2 | 2 | 0 | 0 | 3846.383 ms | 6471.596 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 20.099% | 103.262% | 114.398 s | 5562.130 MB | 5890.762 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker-init | 3507 | sandbox_agent_lsb-native_0000_0000 | 564 | 0.004% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python | 3242 |  | 565 | 5.619% | 101.483% | 31.950 s | 2887.105 MB | 3193.000 MB | 15919.548 MB | 18886.906 MB | 75.035156 MB | 185.007812 MB |
| python3 | 3634 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.821% | 99.821% | 1.010 s | 52.744 MB | 80.254 MB | 64.379 MB | 94.742 MB | n/a MB | n/a MB |
| lsb_grid_worker | 3233 |  | 565 | 0.000% | 0.000% | 0.000 s | 3.430 MB | 3.430 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 3287 |  | 565 | 13.231% | 46.682% | 75.340 s | 2335.388 MB | 2335.727 MB | 21236.382 MB | 21236.652 MB | 0.000000 MB | 0.000000 MB |
| lsb_guard.sh | 3253 |  | 565 | 0.000% | 0.000% | 0.000 s | 3.371 MB | 3.371 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 3628 | sandbox_agent_lsb-native_0000_0000 | 564 | 3.903% | 88.516% | 22.130 s | 100.816 MB | 102.949 MB | 962.345 MB | 972.711 MB | n/a MB | n/a MB |
| sleep | 3256 |  | 16 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| vllm | 3247 |  | 565 | 1.196% | 6.930% | 6.810 s | 1783.720 MB | 1784.074 MB | 11019.867 MB | 11025.051 MB | 0.003906 MB | 0.046875 MB |
| tail | 3539 | sandbox_agent_lsb-native_0000_0000 | 564 | 0.002% | 0.994% | 0.010 s | 1.547 MB | 1.547 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 3286 |  | 565 | 0.000% | 0.000% | 0.000 s | 12.340 MB | 12.340 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python3 | 3646 | sandbox_agent_lsb-native_0000_0000 | 538 | 0.301% | 63.553% | 1.630 s | 71.296 MB | 73.109 MB | 85.577 MB | 87.328 MB | n/a MB | n/a MB |
| sleep | 3681 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3724 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 3740 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3741 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.117 MB | 7.117 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| sleep | 3764 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3775 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3805 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 3817 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 124.773 MB | 124.773 MB | 317.629 MB | 317.629 MB | n/a MB | n/a MB |
| sleep | 3838 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 3860 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.250 MB | 17.250 MB | 209.715 MB | 209.715 MB | n/a MB | n/a MB |
| sleep | 3894 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3939 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4034 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4049 | sandbox_agent_lsb-native_0000_0000 | 2 | 175.871% | 175.871% | 1.770 s | 68.412 MB | 123.410 MB | 274.744 MB | 342.113 MB | n/a MB | n/a MB |
| bash | 4047 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.887 MB | 2.887 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| docker | 4097 |  | 23 | 0.045% | 0.994% | 0.010 s | 29.473 MB | 30.547 MB | 1766.129 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4113 |  | 13 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 33.809% | 100.000% | 12025.019 MB | 14008.000 MB | 44.409 W | 73.050 W | 25266.658 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 5.697% | 193.094% | 32.305 s | 143.298 MB | 265.098 MB | 12.898438 MB | 1.386719 MB | 0.000978 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 3395 | 570.039 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 569.076 | n/a | n/a | 12.898 | 569076.374 | 569076.374 | 569076.374 |
| engine:execute | 1/1 | 0 | 0 | 569.075 | 1.409 | 567.666 | 12.898 | 569074.696 | 569074.696 | 569074.696 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 542.198 | 0.001 | 542.196 | 12.898 | 542197.557 | 542197.557 | 542197.557 |
| turn | 32/32 | 0 | 0 | 540.331 | n/a | n/a | 12.805 | 16885.345 | 10672.243 | 54206.357 |
| llm:attempt | 32/32 | 0 | 0 | 331.505 | 8.241 | 323.262 | 4.163 | 10359.534 | 8436.124 | 23996.591 |
| tool:generate | 6/6 | 0 | 0 | 183.060 | n/a | n/a | 0.020 | 30510.007 | 22549.166 | 70033.999 |
| run:container_call | 13/13 | 0 | 0 | 23.533 | 0.002 | 23.531 | 0.000 | 1810.232 | 36.024 | 9267.084 |
| teardown:commit | 1/1 | 0 | 0 | 23.108 | 0.005 | 23.102 | 0.000 | 23107.870 | 23107.870 | 23107.870 |
| sandbox:commit | 1/1 | 0 | 0 | 22.925 | 0.004 | 22.922 | 0.000 | 22925.450 | 22925.450 | 22925.450 |
| checkpoint.total | 1/1 | 0 | 0 | 22.925 | 0.004 | 22.922 | 0.000 | 22925.316 | 22925.316 | 22925.316 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.925 | 0.003 | 22.922 | 0.000 | 22925.182 | 22925.182 | 22925.182 |
| tool:trace | 2/2 | 0 | 0 | 7.693 | n/a | n/a | 0.000 | 3846.383 | 3846.383 | 6471.596 |
| tool:bash | 21/21 | 0 | 0 | 6.613 | n/a | n/a | 7.673 | 314.892 | 110.351 | 782.701 |
| process:bash | 21/21 | 1 | 0 | 6.431 | n/a | n/a | 7.557 | 306.257 | 101.823 | 771.578 |
| tool:logit_lens | 1/1 | 0 | 0 | 4.383 | n/a | n/a | 0.000 | 4382.994 | 4382.994 | 4382.994 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.153 | 0.711 | 2.441 | 0.000 | 3152.673 | 3152.673 | 3152.673 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.152 | 0.711 | 2.441 | 0.000 | 3152.355 | 3152.355 | 3152.355 |
| tool:inspect_module_inputs | 1/1 | 0 | 0 | 1.911 | n/a | n/a | 0.000 | 1911.119 | 1911.119 | 1911.119 |
| syscall:sendto | 741/741 | 0 | 0 | 1.830 | n/a | n/a | 0.469 | 2.469 | 2.047 | 4.301 |
| tool:inspect | 1/1 | 0 | 0 | 1.765 | n/a | n/a | 0.000 | 1764.599 | 1764.599 | 1764.599 |
| syscall:connect | 198/198 | 0 | 0 | 0.455 | n/a | n/a | 0.123 | 2.299 | 2.127 | 4.035 |
| sandbox:start | 1/1 | 0 | 0 | 0.358 | 0.002 | 0.355 | 0.000 | 357.549 | 357.549 | 357.549 |
| runtime.container_create | 1/1 | 0 | 0 | 0.357 | 0.002 | 0.355 | 0.000 | 357.407 | 357.407 | 357.407 |
| sandbox:create | 1/1 | 0 | 0 | 0.341 | 0.252 | 0.089 | 0.000 | 341.052 | 341.052 | 341.052 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.330 | n/a | n/a | 0.000 | 329.797 | 329.797 | 329.797 |
| tool:submit_output | 1/1 | 0 | 0 | 0.235 | n/a | n/a | 0.000 | 235.414 | 235.414 | 235.414 |
| sandbox:stop | 1/1 | 0 | 0 | 0.182 | 0.002 | 0.181 | 0.000 | 182.125 | 182.125 | 182.125 |
| agency:services_close | 1/1 | 0 | 0 | 0.154 | 0.000 | 0.154 | 0.000 | 154.257 | 154.257 | 154.257 |
| syscall:execve | 79/79 | 0 | 0 | 0.113 | n/a | n/a | 0.046 | 1.436 | 1.188 | 2.898 |
| agency:services_start | 1/1 | 0 | 0 | 0.072 | 0.041 | 0.032 | 0.000 | 72.466 | 72.466 | 72.466 |
| agent:create | 1/1 | 0 | 0 | 0.052 | 0.009 | 0.043 | 0.000 | 51.684 | 51.684 | 51.684 |
| run:detect | 1/1 | 0 | 0 | 0.052 | 0.001 | 0.051 | 0.000 | 51.629 | 51.629 | 51.629 |
| tool:read | 4/4 | 0 | 0 | 0.003 | n/a | n/a | 0.000 | 0.712 | 0.589 | 1.401 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.272 | 1.272 | 1.272 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.072 | 0.069 | 0.104 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.650 | 0.650 | 0.650 |
| tool:todowrite | 2/2 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.172 | 0.172 | 0.187 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.168 | 0.168 | 0.168 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.081 | 0.081 | 0.081 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 564 | 1.528 | 0.041 | 55.170 | 54.747 | 8.671551 CPU seconds | n/a |
| GPU 0 memory | MB | 565 | 12025.019 | 11670.000 | 14008.000 | 12048.000 | n/a | n/a |
| GPU 0 power | W | 565 | 44.409 | 28.852 | 73.050 | 29.110 | n/a | 25266.658 J |
| GPU 0 proc / 3242-76260 / sandbox / ~ / device / GPU-4090d980-b26a-4cce-2890-fc95a90ae7d1 memory | MB | 565 | 3227.313 | 3118.000 | 5190.000 | 3228.000 | n/a | n/a |
| GPU 0 proc / 3242-76260 / sandbox / ~ / device / GPU-4090d980-b26a-4cce-2890-fc95a90ae7d1 estimated power | W | 257 | 3.718 | 0.000 | 72.170 | 0.000 | n/a | n/a |
| GPU 0 proc / 3242-76260 / sandbox / ~ / device / GPU-4090d980-b26a-4cce-2890-fc95a90ae7d1 utilization | percent | 257 | 4.518 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 3287-78062 / sandbox / ~ / device / GPU-4090d980-b26a-4cce-2890-fc95a90ae7d1 memory | MB | 565 | 8315.706 | 8070.000 | 8338.000 | 8338.000 | n/a | n/a |
| GPU 0 proc / 3287-78062 / sandbox / ~ / device / GPU-4090d980-b26a-4cce-2890-fc95a90ae7d1 estimated power | W | 301 | 41.923 | 0.000 | 72.319 | 0.000 | n/a | n/a |
| GPU 0 proc / 3287-78062 / sandbox / ~ / device / GPU-4090d980-b26a-4cce-2890-fc95a90ae7d1 utilization | percent | 301 | 57.847 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 565 | 11543.019 | 11188.000 | 13526.000 | 11566.000 | n/a | n/a |
| GPU 0 utilization | percent | 565 | 33.809 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 565 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 564 | 0.694 | 0.015 | 38.074 | 4.242 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 564 | 6.598 | 0.252 | 49.005 | 19.010 | n/a | n/a |
| host disk_read_mb_s | MB/s | 564 | 3.029 | 0.000 | 189.628 | 5.962 | n/a | n/a |
| host disk_write_mb_s | MB/s | 564 | 0.366 | 0.000 | 7.889 | 7.889 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 564 | 1.252 | 0.000 | 40.061 | 17.164 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 564 | 1.260 | 0.000 | 40.209 | 17.661 | n/a | n/a |
| host mem_total_mb | MB | 565 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 565 | 6964.691 | 6666.980 | 7462.203 | 7177.828 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 564 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 564 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 564 | 0.021 | 0.000 | 0.119 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 564 | 0.015 | 0.000 | 0.400 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3233) CPU | percent | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 3233) io read MB/s | MB/s | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3233) io write MB/s | MB/s | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3233) rss_mb | MB | 565 | 3.430 | 3.430 | 3.430 | 3.430 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3233) main thread run-queue wait | percent | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 3233) vms_mb | MB | 565 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3242) CPU | percent | 564 | 5.619 | 0.000 | 101.483 | 1.989 | 31.950000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 3242) io read MB/s | MB/s | 564 | 0.132 | 0.000 | 59.002 | 0.000 | 75.035156 MB | n/a |
| Agency harness — python -m lsbench (PID 3242) io write MB/s | MB/s | 564 | 0.326 | 0.016 | 6.566 | 1.344 | 185.007812 MB | n/a |
| Agency harness — python -m lsbench (PID 3242) rss_mb | MB | 565 | 2887.105 | 2551.887 | 3193.000 | 3193.000 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3242) main thread run-queue wait | percent | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 3242) vms_mb | MB | 565 | 15919.548 | 14115.887 | 18886.906 | 16598.477 | n/a | n/a |
| Python — vllm (PID 3247) CPU | percent | 564 | 1.196 | 0.000 | 6.930 | 0.994 | 6.810000 CPU seconds | n/a |
| Python — vllm (PID 3247) io read MB/s | MB/s | 564 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 3247) io write MB/s | MB/s | 564 | 0.000 | 0.000 | 0.008 | 0.000 | 0.046875 MB | n/a |
| Python — vllm (PID 3247) rss_mb | MB | 565 | 1783.720 | 1781.949 | 1784.074 | 1784.074 | n/a | n/a |
| Python — vllm (PID 3247) main thread run-queue wait | percent | 564 | 0.003 | 0.000 | 0.264 | 0.001 | 0.018216 run-queue seconds | n/a |
| Python — vllm (PID 3247) vms_mb | MB | 565 | 11019.867 | 10951.031 | 11025.051 | 11025.051 | n/a | n/a |
| bash lsb_guard.sh (PID 3253) CPU | percent | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 3253) io read MB/s | MB/s | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3253) io write MB/s | MB/s | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3253) rss_mb | MB | 565 | 3.371 | 3.371 | 3.371 | 3.371 | n/a | n/a |
| bash lsb_guard.sh (PID 3253) main thread run-queue wait | percent | 564 | 0.000 | 0.000 | 0.102 | 0.000 | 0.001031 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 3253) vms_mb | MB | 565 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sleep (PID 3256) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3256) io read MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3256) io write MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3256) rss_mb | MB | 16 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3256) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3256) vms_mb | MB | 16 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — python -c (PID 3286) CPU | percent | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 3286) io read MB/s | MB/s | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3286) io write MB/s | MB/s | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3286) rss_mb | MB | 565 | 12.340 | 12.340 | 12.340 | 12.340 | n/a | n/a |
| Python — python -c (PID 3286) main thread run-queue wait | percent | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 3286) vms_mb | MB | 565 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 3287) CPU | percent | 564 | 13.231 | 0.000 | 46.682 | 1.989 | 75.340000 CPU seconds | n/a |
| VLLM::EngineCore (PID 3287) io read MB/s | MB/s | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 3287) io write MB/s | MB/s | 564 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 3287) rss_mb | MB | 565 | 2335.388 | 2334.727 | 2335.727 | 2335.727 | n/a | n/a |
| VLLM::EngineCore (PID 3287) main thread run-queue wait | percent | 564 | 0.004 | 0.000 | 0.107 | 0.000 | 0.021166 run-queue seconds | n/a |
| VLLM::EngineCore (PID 3287) vms_mb | MB | 565 | 21236.382 | 21235.090 | 21236.652 | 21236.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3507) CPU | percent | 563 | 0.004 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3507) rss_mb | MB | 564 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3507) main thread run-queue wait | percent | 563 | 0.009 | 0.000 | 5.069 | 0.000 | 0.051198 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3507) vms_mb | MB | 564 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3539) CPU | percent | 563 | 0.002 | 0.000 | 0.994 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3539) rss_mb | MB | 564 | 1.547 | 1.547 | 1.547 | 1.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3539) main thread run-queue wait | percent | 563 | 0.008 | 0.000 | 4.533 | 0.000 | 0.047085 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3539) vms_mb | MB | 564 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3628) CPU | percent | 563 | 3.903 | 0.000 | 88.516 | 0.000 | 22.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3628) rss_mb | MB | 564 | 100.816 | 3.000 | 102.949 | 102.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3628) main thread run-queue wait | percent | 563 | 0.000 | 0.000 | 0.008 | 0.000 | 0.000131 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3628) vms_mb | MB | 564 | 962.345 | 4.258 | 972.711 | 972.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3634) CPU | percent | 1 | 99.821 | 99.821 | 99.821 | 99.821 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3634) rss_mb | MB | 2 | 52.744 | 25.234 | 80.254 | 80.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3634) main thread run-queue wait | percent | 1 | 0.008 | 0.008 | 0.008 | 0.008 | 0.000083 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3634) vms_mb | MB | 2 | 64.379 | 34.016 | 94.742 | 94.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3646) CPU | percent | 537 | 0.301 | 0.000 | 63.553 | 0.000 | 1.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3646) rss_mb | MB | 538 | 71.296 | 30.324 | 73.109 | 72.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3646) main thread run-queue wait | percent | 537 | 0.020 | 0.000 | 4.007 | 0.000 | 0.107590 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3646) vms_mb | MB | 538 | 85.577 | 35.746 | 87.328 | 86.598 | n/a | n/a |
| sleep (PID 3681) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3681) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3681) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3681) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3681) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3681) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3724) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3724) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3724) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3724) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 3724) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3724) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3740) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3740) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3741) rss_mb | MB | 1 | 7.117 | 7.117 | 7.117 | 7.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3741) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sleep (PID 3764) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3764) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3764) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3764) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3764) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3764) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3775) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3775) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3775) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3775) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3775) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3775) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3805) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3805) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3805) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3805) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3805) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3805) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_weights.py (PID 3817) rss_mb | MB | 1 | 124.773 | 124.773 | 124.773 | 124.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_weights.py (PID 3817) vms_mb | MB | 1 | 317.629 | 317.629 | 317.629 | 317.629 | n/a | n/a |
| sleep (PID 3838) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3838) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3838) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3838) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3838) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3838) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design_gate.py (PID 3860) rss_mb | MB | 1 | 17.250 | 17.250 | 17.250 | 17.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design_gate.py (PID 3860) vms_mb | MB | 1 | 209.715 | 209.715 | 209.715 | 209.715 | n/a | n/a |
| sleep (PID 3894) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3894) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3894) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3894) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3894) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3894) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3939) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3939) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3939) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3939) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3939) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3939) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4034) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4034) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4034) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4034) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4034) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4034) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4047) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4047) rss_mb | MB | 2 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4047) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4047) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 4049) CPU | percent | 1 | 175.871 | 175.871 | 175.871 | 175.871 | 1.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 4049) rss_mb | MB | 2 | 68.412 | 13.414 | 123.410 | 123.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 4049) main thread run-queue wait | percent | 1 | 37.443 | 37.443 | 37.443 | 37.443 | 0.376830 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 4049) vms_mb | MB | 2 | 274.744 | 207.375 | 342.113 | 342.113 | n/a | n/a |
| docker commit (PID 4097) CPU | percent | 22 | 0.045 | 0.000 | 0.994 | 0.000 | 0.010000 CPU seconds | n/a |
| docker commit (PID 4097) io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4097) io write MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4097) rss_mb | MB | 23 | 29.473 | 5.855 | 30.547 | 30.547 | n/a | n/a |
| docker commit (PID 4097) main thread run-queue wait | percent | 22 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000018 run-queue seconds | n/a |
| docker commit (PID 4097) vms_mb | MB | 23 | 1766.129 | 69.043 | 1843.270 | 1843.270 | n/a | n/a |
| sleep (PID 4113) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4113) io read MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4113) io write MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4113) rss_mb | MB | 13 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4113) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4113) vms_mb | MB | 13 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 563 | 5.697 | 0.000 | 193.094 | 0.000 | 32.304518 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 563 | 0.441 | 0.000 | 36.696 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 563 | 0.486 | 0.000 | 37.450 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 563 | 0.005 | 0.000 | 0.733 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 563 | 0.005 | 0.000 | 0.733 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 563 | 0.023 | 0.000 | 6.348 | 0.000 | 12.898438 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 563 | 0.002 | 0.000 | 0.711 | 0.000 | 1.386719 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 564 | 143.298 | 16.898 | 265.098 | 100.992 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 563 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 563 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 563 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000978 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 563 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 564 | 20.099 | 1.795 | 103.262 | 12.579 | 114.398310 CPU seconds | n/a |
| workload total memory | MB | 565 | 5562.130 | 5205.281 | 5890.762 | 5880.480 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
