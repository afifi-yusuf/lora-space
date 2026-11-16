# agprof summary

- Duration: **2117.401 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **54 calls**, 54 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1497.098 s total wait
- Tools: **56/56 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **195462** at 1.968 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2117329.683 / 2117329.683 ms |
| LLM latency p50 / p95 | 19460.320 / 71771.834 ms |
| LLM TTFT p50 / p95 | 12239.764 / 22245.965 ms |
| LLM input / output tokens | 5251621 / 49124 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 54 total, 54 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1270.979 / 52501.539 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attribution | 2/2 | 2 | 0 | 0 | 756.368 ms | 1126.538 ms |
| bash | 19/19 | 19 | 0 | 0 | 319.117 ms | 2518.942 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 324.364 ms | 324.364 ms |
| generate | 9/9 | 9 | 0 | 0 | 47557.198 ms | 77866.617 ms |
| inspect | 1/1 | 1 | 0 | 0 | 1166.670 ms | 1166.670 ms |
| inspect_module_inputs | 5/5 | 5 | 0 | 0 | 1489.217 ms | 1925.073 ms |
| patch | 2/2 | 2 | 0 | 0 | 2147.429 ms | 2836.119 ms |
| read | 1/1 | 1 | 0 | 0 | 0.524 ms | 0.524 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 230.766 ms | 230.766 ms |
| token_stats | 3/3 | 3 | 0 | 0 | 26865.044 ms | 60195.156 ms |
| top_activations | 3/3 | 3 | 0 | 0 | 20133.120 ms | 20168.612 ms |
| trace | 9/9 | 9 | 0 | 0 | 670.106 ms | 6713.687 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 27.677% | 431.201% | 587.092 s | 5578.769 MB | 7069.363 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 9559 |  | 2102 | 0.000% | 0.000% | 0.000 s | 12.371 MB | 12.371 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python3 | 9965 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.869% | 99.869% | 1.010 s | 54.324 MB | 82.684 MB | 64.773 MB | 95.531 MB | n/a MB | n/a MB |
| tail | 9859 | sandbox_agent_lsb-native_0000_0000 | 2102 | 0.002% | 0.995% | 0.050 s | 1.562 MB | 1.562 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 9560 |  | 2102 | 7.623% | 42.588% | 161.660 s | 2341.201 MB | 2341.457 MB | 21861.998 MB | 21862.633 MB | 0.000000 MB | 0.011719 MB |
| vllm | 9505 |  | 2102 | 0.671% | 4.973% | 14.230 s | 1796.902 MB | 1797.012 MB | 12004.218 MB | 12005.301 MB | 0.000000 MB | 0.089844 MB |
| bash | 9959 | sandbox_agent_lsb-native_0000_0000 | 2102 | 2.546% | 86.402% | 53.890 s | 105.481 MB | 113.590 MB | 969.362 MB | 974.383 MB | n/a MB | n/a MB |
| docker-init | 9820 | sandbox_agent_lsb-native_0000_0000 | 2102 | 0.003% | 0.995% | 0.060 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| lsb_grid_worker | 9487 |  | 2102 | 0.000% | 0.000% | 0.000 s | 3.414 MB | 3.414 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 9496 |  | 2102 | 19.384% | 430.493% | 411.120 s | 2770.817 MB | 4209.305 MB | 16332.801 MB | 19770.445 MB | 0.617188 MB | 814.421875 MB |
| python3 | 9977 | sandbox_agent_lsb-native_0000_0000 | 2096 | 0.137% | 59.666% | 2.900 s | 73.887 MB | 77.094 MB | 86.787 MB | 89.879 MB | n/a MB | n/a MB |
| ls | 9992 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| bash | 9991 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.926 MB | 2.926 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10217 | sandbox_agent_lsb-native_0000_0000 | 5 | 180.933% | 191.175% | 7.290 s | 208.734 MB | 352.809 MB | 1766.912 MB | 2212.262 MB | n/a MB | n/a MB |
| python | 10357 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 47.512 MB | 47.512 MB | 1904.766 MB | 1904.766 MB | n/a MB | n/a MB |
| python | 10407 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 251.395 MB | 251.395 MB | 1951.539 MB | 1951.539 MB | n/a MB | n/a MB |
| python | 10430 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 165.223 MB | 165.223 MB | 1976.465 MB | 1976.465 MB | n/a MB | n/a MB |
| python | 10624 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.801 MB | 20.801 MB | 371.988 MB | 371.988 MB | n/a MB | n/a MB |
| bash | 10623 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.992 MB | 2.992 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10639 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.777 MB | 20.777 MB | 372.273 MB | 372.273 MB | n/a MB | n/a MB |
| bash | 10638 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.707 MB | 2.707 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10670 | sandbox_agent_lsb-native_0000_0000 | 2 | 184.512% | 184.512% | 1.860 s | 168.744 MB | 197.672 MB | 2287.465 MB | 2336.816 MB | n/a MB | n/a MB |
| bash | 10711 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.969 MB | 2.969 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10712 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.711 MB | 13.711 MB | 367.191 MB | 367.191 MB | n/a MB | n/a MB |
| docker | 10827 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.312 MB | 30.312 MB | 1988.020 MB | 1988.020 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 23.089% | 100.000% | 11975.808 MB | 13744.000 MB | 39.007 W | 75.305 W | 82601.245 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 3.671% | 204.925% | 77.694 s | 161.518 MB | 357.805 MB | 0.000000 MB | 33.148438 MB | 0.001030 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 9692 | 2117.335 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2117.330 | n/a | n/a | 0.000 | 2117329.683 | 2117329.683 | 2117329.683 |
| sync:result_wait | 1/1 | 0 | 0 | 2117.329 | 0.000 | 2117.329 | 0.000 | 2117329.246 | 2117329.246 | 2117329.246 |
| engine:execute | 1/1 | 0 | 0 | 2117.328 | 2.416 | 2114.912 | 0.000 | 2117328.037 | 2117328.037 | 2117328.037 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2111.384 | 0.003 | 2111.381 | 0.000 | 2111383.809 | 2111383.809 | 2111383.809 |
| turn | 54/54 | 0 | 0 | 2108.633 | n/a | n/a | 0.000 | 39048.768 | 26976.175 | 94057.475 |
| llm:attempt | 54/54 | 0 | 0 | 1497.098 | 6.614 | 1490.482 | 0.000 | 27724.044 | 19460.320 | 71771.834 |
| tool:generate | 9/9 | 0 | 0 | 397.640 | n/a | n/a | 0.000 | 44182.228 | 47557.198 | 77866.617 |
| tool:token_stats | 3/3 | 0 | 0 | 101.992 | n/a | n/a | 0.000 | 33997.294 | 26865.044 | 60195.156 |
| tool:top_activations | 3/3 | 0 | 0 | 58.863 | n/a | n/a | 0.000 | 19621.122 | 20133.120 | 20168.612 |
| tool:trace | 9/9 | 0 | 0 | 19.482 | n/a | n/a | 0.000 | 2164.670 | 670.106 | 6713.687 |
| tool:bash | 19/19 | 0 | 0 | 12.928 | n/a | n/a | 0.000 | 680.443 | 319.117 | 2518.942 |
| process:bash | 19/19 | 1 | 0 | 12.691 | n/a | n/a | 0.000 | 667.938 | 311.289 | 2509.956 |
| tool:inspect_module_inputs | 5/5 | 0 | 0 | 7.899 | n/a | n/a | 0.000 | 1579.751 | 1489.217 | 1925.073 |
| tool:patch | 2/2 | 0 | 0 | 4.295 | n/a | n/a | 0.000 | 2147.429 | 2147.429 | 2836.119 |
| syscall:sendto | 1435/1435 | 0 | 0 | 3.266 | n/a | n/a | 0.000 | 2.276 | 1.861 | 4.141 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.085 | 0.700 | 2.385 | 0.000 | 3084.742 | 3084.742 | 3084.742 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.084 | 0.700 | 2.385 | 0.000 | 3084.481 | 3084.481 | 3084.481 |
| run:container_call | 13/13 | 0 | 0 | 2.592 | 0.003 | 2.590 | 0.000 | 199.415 | 34.395 | 883.200 |
| teardown:commit | 1/1 | 0 | 0 | 2.176 | 0.004 | 2.172 | 0.000 | 2175.868 | 2175.868 | 2175.868 |
| sandbox:commit | 1/1 | 0 | 0 | 1.974 | 0.002 | 1.972 | 0.000 | 1974.284 | 1974.284 | 1974.284 |
| checkpoint.total | 1/1 | 0 | 0 | 1.974 | 0.002 | 1.972 | 0.000 | 1974.140 | 1974.140 | 1974.140 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.974 | 0.002 | 1.972 | 0.000 | 1973.991 | 1973.991 | 1973.991 |
| tool:attribution | 2/2 | 0 | 0 | 1.513 | n/a | n/a | 0.000 | 756.368 | 756.368 | 1126.538 |
| tool:inspect | 1/1 | 0 | 0 | 1.167 | n/a | n/a | 0.000 | 1166.670 | 1166.670 | 1166.670 |
| syscall:connect | 388/388 | 0 | 0 | 0.812 | n/a | n/a | 0.000 | 2.093 | 1.822 | 4.053 |
| sandbox:start | 1/1 | 0 | 0 | 0.350 | 0.003 | 0.347 | 0.000 | 349.933 | 349.933 | 349.933 |
| runtime.container_create | 1/1 | 0 | 0 | 0.350 | 0.003 | 0.347 | 0.000 | 349.760 | 349.760 | 349.760 |
| sandbox:create | 1/1 | 0 | 0 | 0.338 | 0.250 | 0.088 | 0.000 | 338.371 | 338.371 | 338.371 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.324 | n/a | n/a | 0.000 | 324.364 | 324.364 | 324.364 |
| tool:submit_output | 1/1 | 0 | 0 | 0.231 | n/a | n/a | 0.000 | 230.766 | 230.766 | 230.766 |
| sandbox:stop | 1/1 | 0 | 0 | 0.201 | 0.002 | 0.200 | 0.000 | 201.331 | 201.331 | 201.331 |
| agency:services_close | 1/1 | 0 | 0 | 0.169 | 0.001 | 0.168 | 0.000 | 168.547 | 168.547 | 168.547 |
| syscall:execve | 70/70 | 0 | 0 | 0.096 | n/a | n/a | 0.000 | 1.364 | 1.131 | 2.341 |
| agency:services_start | 1/1 | 0 | 0 | 0.081 | 0.047 | 0.034 | 0.000 | 81.476 | 81.476 | 81.476 |
| agent:create | 1/1 | 0 | 0 | 0.050 | 0.009 | 0.042 | 0.000 | 50.322 | 50.322 | 50.322 |
| run:detect | 1/1 | 0 | 0 | 0.050 | 0.001 | 0.050 | 0.000 | 50.265 | 50.265 | 50.265 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.736 | 1.736 | 1.736 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.310 | 1.310 | 1.310 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.084 | 0.093 | 0.119 |
| tool:read | 1/1 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.524 | 0.524 | 0.524 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.206 | 0.206 | 0.206 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.068 | 0.068 | 0.068 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2101 | 0.191 | 0.032 | 163.256 | 163.256 | 4.036570 CPU seconds | n/a |
| GPU 0 memory | MB | 2102 | 11975.808 | 11670.000 | 13744.000 | 12116.000 | n/a | n/a |
| GPU 0 power | W | 2102 | 39.007 | 28.212 | 75.305 | 28.394 | n/a | 82601.245 J |
| GPU 0 proc / 9496-478345 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c memory | MB | 2102 | 3311.826 | 3118.000 | 5078.000 | 3450.000 | n/a | n/a |
| GPU 0 proc / 9496-478345 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c estimated power | W | 1278 | 7.142 | 0.000 | 74.407 | 0.000 | n/a | n/a |
| GPU 0 proc / 9496-478345 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c utilization | percent | 1278 | 7.302 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 9560-480125 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c memory | MB | 2102 | 8181.982 | 8070.000 | 8184.000 | 8184.000 | n/a | n/a |
| GPU 0 proc / 9560-480125 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c estimated power | W | 786 | 34.700 | 0.000 | 72.454 | 0.000 | n/a | n/a |
| GPU 0 proc / 9560-480125 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c utilization | percent | 786 | 47.963 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2102 | 11493.808 | 11188.000 | 13262.000 | 11634.000 | n/a | n/a |
| GPU 0 utilization | percent | 2102 | 23.089 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2102 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2101 | 0.496 | 0.010 | 66.020 | 0.979 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2101 | 3.824 | 0.000 | 54.827 | 30.230 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2101 | 0.029 | 0.000 | 59.761 | 59.761 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2101 | 0.415 | 0.000 | 196.768 | 0.713 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2101 | 0.055 | 0.000 | 44.099 | 3.050 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2101 | 0.056 | 0.000 | 44.147 | 3.115 | n/a | n/a |
| host mem_total_mb | MB | 2102 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 2102 | 7091.170 | 6527.680 | 9093.887 | 7363.746 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2101 | 0.003 | 0.000 | 0.252 | 0.002 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2101 | 0.012 | 0.000 | 0.872 | 0.002 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_weights.py (PID 10217) CPU | percent | 4 | 180.933 | 155.124 | 191.175 | 187.593 | 7.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_weights.py (PID 10217) rss_mb | MB | 5 | 208.734 | 9.809 | 352.809 | 352.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_weights.py (PID 10217) main thread run-queue wait | percent | 4 | 46.195 | 32.706 | 57.573 | 51.596 | 1.861117 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_weights.py (PID 10217) vms_mb | MB | 5 | 1766.912 | 13.512 | 2212.262 | 2184.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — neuron_analysis.py (PID 10357) rss_mb | MB | 1 | 47.512 | 47.512 | 47.512 | 47.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — neuron_analysis.py (PID 10357) vms_mb | MB | 1 | 1904.766 | 1904.766 | 1904.766 | 1904.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — feature_tokens.py (PID 10407) rss_mb | MB | 1 | 251.395 | 251.395 | 251.395 | 251.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — feature_tokens.py (PID 10407) vms_mb | MB | 1 | 1951.539 | 1951.539 | 1951.539 | 1951.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — other_neurons.py (PID 10430) rss_mb | MB | 1 | 165.223 | 165.223 | 165.223 | 165.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — other_neurons.py (PID 10430) vms_mb | MB | 1 | 1976.465 | 1976.465 | 1976.465 | 1976.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10623) rss_mb | MB | 1 | 2.992 | 2.992 | 2.992 | 2.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10623) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10624) rss_mb | MB | 1 | 20.801 | 20.801 | 20.801 | 20.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10624) vms_mb | MB | 1 | 371.988 | 371.988 | 371.988 | 371.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10638) rss_mb | MB | 1 | 2.707 | 2.707 | 2.707 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10638) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10639) rss_mb | MB | 1 | 20.777 | 20.777 | 20.777 | 20.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10639) vms_mb | MB | 1 | 372.273 | 372.273 | 372.273 | 372.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_directions.py (PID 10670) CPU | percent | 1 | 184.512 | 184.512 | 184.512 | 184.512 | 1.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_directions.py (PID 10670) rss_mb | MB | 2 | 168.744 | 139.816 | 197.672 | 197.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_directions.py (PID 10670) main thread run-queue wait | percent | 1 | 41.520 | 41.520 | 41.520 | 41.520 | 0.418544 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_directions.py (PID 10670) vms_mb | MB | 2 | 2287.465 | 2238.113 | 2336.816 | 2336.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10711) rss_mb | MB | 1 | 2.969 | 2.969 | 2.969 | 2.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10711) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10712) rss_mb | MB | 1 | 13.711 | 13.711 | 13.711 | 13.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10712) vms_mb | MB | 1 | 367.191 | 367.191 | 367.191 | 367.191 | n/a | n/a |
| docker commit (PID 10827) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 10827) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 10827) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 10827) rss_mb | MB | 2 | 30.312 | 30.312 | 30.312 | 30.312 | n/a | n/a |
| docker commit (PID 10827) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 10827) vms_mb | MB | 2 | 1988.020 | 1988.020 | 1988.020 | 1988.020 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 9487) CPU | percent | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 9487) io read MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 9487) io write MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 9487) rss_mb | MB | 2102 | 3.414 | 3.414 | 3.414 | 3.414 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 9487) main thread run-queue wait | percent | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 9487) vms_mb | MB | 2102 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9496) CPU | percent | 2101 | 19.384 | 0.000 | 430.493 | 0.000 | 411.120000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 9496) io read MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.427 | 0.000 | 0.617188 MB | n/a |
| Agency harness — python -m lsbench (PID 9496) io write MB/s | MB/s | 2101 | 0.384 | 0.015 | 197.662 | 0.085 | 814.421875 MB | n/a |
| Agency harness — python -m lsbench (PID 9496) rss_mb | MB | 2102 | 2770.817 | 2169.863 | 4209.305 | 3096.320 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9496) main thread run-queue wait | percent | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 9496) vms_mb | MB | 2102 | 16332.801 | 14275.887 | 19770.445 | 16772.867 | n/a | n/a |
| Python — vllm (PID 9505) CPU | percent | 2101 | 0.671 | 0.000 | 4.973 | 0.000 | 14.230000 CPU seconds | n/a |
| Python — vllm (PID 9505) io read MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 9505) io write MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.008 | 0.000 | 0.089844 MB | n/a |
| Python — vllm (PID 9505) rss_mb | MB | 2102 | 1796.902 | 1794.762 | 1797.012 | 1797.012 | n/a | n/a |
| Python — vllm (PID 9505) main thread run-queue wait | percent | 2101 | 0.003 | 0.000 | 0.407 | 0.000 | 0.066797 run-queue seconds | n/a |
| Python — vllm (PID 9505) vms_mb | MB | 2102 | 12004.218 | 11932.281 | 12005.301 | 12005.301 | n/a | n/a |
| Python — python -c (PID 9559) CPU | percent | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 9559) io read MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9559) io write MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9559) rss_mb | MB | 2102 | 12.371 | 12.371 | 12.371 | 12.371 | n/a | n/a |
| Python — python -c (PID 9559) main thread run-queue wait | percent | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 9559) vms_mb | MB | 2102 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 9560) CPU | percent | 2101 | 7.623 | 0.000 | 42.588 | 0.993 | 161.660000 CPU seconds | n/a |
| VLLM::EngineCore (PID 9560) io read MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 9560) io write MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 9560) rss_mb | MB | 2102 | 2341.201 | 2339.332 | 2341.457 | 2341.457 | n/a | n/a |
| VLLM::EngineCore (PID 9560) main thread run-queue wait | percent | 2101 | 0.001 | 0.000 | 0.045 | 0.000 | 0.021747 run-queue seconds | n/a |
| VLLM::EngineCore (PID 9560) vms_mb | MB | 2102 | 21861.998 | 21859.762 | 21862.633 | 21862.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 9820) CPU | percent | 2101 | 0.003 | 0.000 | 0.995 | 0.000 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 9820) rss_mb | MB | 2102 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 9820) main thread run-queue wait | percent | 2101 | 0.000 | 0.000 | 0.225 | 0.000 | 0.004142 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 9820) vms_mb | MB | 2102 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 9859) CPU | percent | 2101 | 0.002 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 9859) rss_mb | MB | 2102 | 1.562 | 1.562 | 1.562 | 1.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 9859) main thread run-queue wait | percent | 2101 | 0.000 | 0.000 | 0.175 | 0.000 | 0.005201 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 9859) vms_mb | MB | 2102 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9959) CPU | percent | 2101 | 2.546 | 0.000 | 86.402 | 0.000 | 53.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9959) rss_mb | MB | 2102 | 105.481 | 3.125 | 113.590 | 113.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9959) main thread run-queue wait | percent | 2101 | 0.000 | 0.000 | 0.008 | 0.000 | 0.000143 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9959) vms_mb | MB | 2102 | 969.362 | 4.258 | 974.383 | 974.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 9965) CPU | percent | 1 | 99.869 | 99.869 | 99.869 | 99.869 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 9965) rss_mb | MB | 2 | 54.324 | 25.965 | 82.684 | 82.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 9965) main thread run-queue wait | percent | 1 | 0.007 | 0.007 | 0.007 | 0.007 | 0.000070 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 9965) vms_mb | MB | 2 | 64.773 | 34.016 | 95.531 | 95.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9977) CPU | percent | 2095 | 0.137 | 0.000 | 59.666 | 0.000 | 2.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9977) rss_mb | MB | 2096 | 73.887 | 31.270 | 77.094 | 76.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9977) main thread run-queue wait | percent | 2095 | 0.015 | 0.000 | 14.141 | 0.000 | 0.319276 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9977) vms_mb | MB | 2096 | 86.787 | 36.262 | 89.879 | 89.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9991) rss_mb | MB | 1 | 2.926 | 2.926 | 2.926 | 2.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9991) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ls (PID 9992) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ls (PID 9992) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 2101 | 3.671 | 0.000 | 204.925 | 0.000 | 77.693646 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2101 | 0.634 | 0.000 | 65.278 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2101 | 0.635 | 0.000 | 65.408 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 2101 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 2101 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 2101 | 0.016 | 0.000 | 13.253 | 0.000 | 33.148438 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 2102 | 161.518 | 17.988 | 357.805 | 131.055 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001030 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 2101 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 2101 | 27.677 | 1.465 | 431.201 | 1.738 | 587.091784 CPU seconds | n/a |
| workload total memory | MB | 2102 | 5578.769 | 4838.328 | 7069.363 | 6121.980 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
