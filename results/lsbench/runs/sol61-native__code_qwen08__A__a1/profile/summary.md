# agprof summary

- Duration: **2554.901 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **33 calls**, 33 succeeded, 0 failed, 0 interrupted, n/a reported retries, 2092.203 s total wait
- Tools: **58/58 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **236797** at 1.975 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2554833.486 / 2554833.486 ms |
| LLM latency p50 / p95 | 53762.512 / 130804.386 ms |
| LLM TTFT p50 / p95 | 20143.721 / 24257.326 ms |
| LLM input / output tokens | 3271957 / 79245 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 33 total, 33 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1816.058 / 10833.433 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attribution | 4/4 | 4 | 0 | 0 | 330.598 ms | 333.264 ms |
| bash | 16/16 | 16 | 0 | 0 | 1044.171 ms | 4148.205 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 313.399 ms | 313.399 ms |
| generate | 14/14 | 14 | 0 | 0 | 2485.551 ms | 14726.123 ms |
| inspect | 1/1 | 1 | 0 | 0 | 1140.848 ms | 1140.848 ms |
| inspect_module_inputs | 2/2 | 2 | 0 | 0 | 1063.521 ms | 1080.179 ms |
| logit_lens | 2/2 | 2 | 0 | 0 | 1353.328 ms | 1801.439 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 245.079 ms | 245.079 ms |
| todowrite | 2/2 | 2 | 0 | 0 | 0.219 ms | 0.276 ms |
| token_stats | 3/3 | 3 | 0 | 0 | 10517.953 ms | 14126.600 ms |
| top_activations | 6/6 | 6 | 0 | 0 | 4807.622 ms | 4965.986 ms |
| trace | 6/6 | 6 | 0 | 0 | 2088.650 ms | 4137.730 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 6.908% | 370.337% | 176.779 s | 7733.777 MB | 8876.090 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lsb_grid_worker | 4616 |  | 2540 | 0.000% | 0.000% | 0.000 s | 3.391 MB | 3.391 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| docker | 10075 |  | 1 | n/a% | n/a% | n/a s | 30.680 MB | 30.680 MB | 1915.523 MB | 1915.523 MB | n/a MB | n/a MB |
| python | 9899 |  | 2540 | 0.000% | 0.000% | 0.000 s | 12.191 MB | 12.191 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python | 9859 |  | 2540 | 4.811% | 370.010% | 123.150 s | 2874.499 MB | 4142.828 MB | 15966.527 MB | 18138.625 MB | 2.054688 MB | 2324.964844 MB |
| vllm | 9864 |  | 2540 | 0.183% | 6.934% | 4.680 s | 1784.203 MB | 1784.328 MB | 11023.764 MB | 11027.172 MB | 0.007812 MB | 0.066406 MB |
| VLLM::EngineCor | 9900 |  | 2540 | 1.905% | 50.520% | 48.730 s | 2320.274 MB | 2320.363 MB | 21205.003 MB | 21205.094 MB | 0.000000 MB | 0.015625 MB |
| python3 | 10248 | sandbox_agent_lsb-native_0000_0000 | 2 | 73.191% | 73.191% | 0.740 s | 65.123 MB | 82.395 MB | 77.066 MB | 97.996 MB | n/a MB | n/a MB |
| tail | 10152 | sandbox_agent_lsb-native_0000_0000 | 2539 | 0.002% | 0.995% | 0.050 s | 1.566 MB | 1.566 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 10242 | sandbox_agent_lsb-native_0000_0000 | 2539 | 2.324% | 100.246% | 59.380 s | 104.408 MB | 108.168 MB | 970.290 MB | 973.492 MB | n/a MB | n/a MB |
| docker-init | 10120 | sandbox_agent_lsb-native_0000_0000 | 2539 | 0.002% | 0.995% | 0.040 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 10260 | sandbox_agent_lsb-native_0000_0000 | 2257 | 0.137% | 47.739% | 3.120 s | 73.090 MB | 76.242 MB | 87.287 MB | 90.129 MB | n/a MB | n/a MB |
| python | 10318 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.219 MB | 12.219 MB | 15.859 MB | 15.859 MB | n/a MB | n/a MB |
| bash | 10441 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.039 MB | 3.039 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10442 | sandbox_agent_lsb-native_0000_0000 | 2 | 27.730% | 27.730% | 0.280 s | 20.836 MB | 26.730 MB | 1879.525 MB | 1884.801 MB | n/a MB | n/a MB |
| bash | 10598 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.844 MB | 2.844 MB | 4.328 MB | 4.328 MB | n/a MB | n/a MB |
| python | 10601 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.773 MB | 7.773 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python | 10670 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 54.934 MB | 54.934 MB | 252.648 MB | 252.648 MB | n/a MB | n/a MB |
| bash | 10668 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.652 MB | 2.652 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10724 | sandbox_agent_lsb-native_0000_0000 | 6 | 140.196% | 157.822% | 7.060 s | 173.616 MB | 246.035 MB | 434.150 MB | 524.883 MB | n/a MB | n/a MB |
| python | 10750 | sandbox_agent_lsb-native_0000_0000 | 2 | 118.144% | 118.144% | 1.190 s | 121.711 MB | 125.754 MB | 391.748 MB | 413.242 MB | n/a MB | n/a MB |
| python | 10762 | sandbox_agent_lsb-native_0000_0000 | 2 | 116.358% | 116.358% | 1.170 s | 122.455 MB | 181.543 MB | 318.145 MB | 461.238 MB | n/a MB | n/a MB |
| bash | 10776 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.922 MB | 2.922 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10777 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.695 MB | 20.695 MB | 212.387 MB | 212.387 MB | n/a MB | n/a MB |
| python | 10852 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 96.547 MB | 96.547 MB | 288.781 MB | 288.781 MB | n/a MB | n/a MB |
| bash | 10851 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.902 MB | 2.902 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10922 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 36.844 MB | 36.844 MB | 416.945 MB | 416.945 MB | n/a MB | n/a MB |
| bash | 10921 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.051 MB | 3.051 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10995 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.891 MB | 6.891 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| bash | 10985 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.867 MB | 2.867 MB | 4.219 MB | 4.219 MB | n/a MB | n/a MB |
| python | 10989 | sandbox_agent_lsb-native_0000_0000 | 4 | 44.000% | 71.463% | 1.330 s | 105.800 MB | 113.051 MB | 297.557 MB | 304.492 MB | n/a MB | n/a MB |
| python | 11034 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.422 MB | 7.422 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| bash | 11050 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.809 MB | 2.809 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 11052 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.363 MB | 21.363 MB | 133.602 MB | 133.602 MB | n/a MB | n/a MB |
| docker | 11127 |  | 119 | 0.000% | 0.000% | 0.000 s | 30.184 MB | 30.184 MB | 1843.512 MB | 1843.512 MB | 0.000000 MB | 0.000000 MB |
| docker | 11153 |  | 119 | 0.000% | 0.000% | 0.000 s | 29.027 MB | 29.027 MB | 1770.938 MB | 1770.938 MB | 0.000000 MB | 0.000000 MB |
| docker | 11174 |  | 38 | 0.000% | 0.000% | 0.000 s | 30.707 MB | 30.707 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 3.708% | 100.000% | 12049.303 MB | 12816.000 MB | 30.349 W | 73.103 W | 77507.585 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 3.324% | 202.722% | 84.929 s | 173.608 MB | 378.836 MB | 24.312500 MB | 8.960938 MB | 0.000839 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 10007 | 2554.838 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2554.833 | n/a | n/a | 24.312 | 2554833.486 | 2554833.486 | 2554833.486 |
| sync:result_wait | 1/1 | 0 | 0 | 2554.833 | 0.000 | 2554.833 | 24.312 | 2554832.782 | 2554832.782 | 2554832.782 |
| engine:execute | 1/1 | 0 | 0 | 2554.832 | 2.684 | 2552.147 | 24.312 | 2554831.822 | 2554831.822 | 2554831.822 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2269.406 | 0.004 | 2269.402 | 17.491 | 2269405.517 | 2269405.517 | 2269405.517 |
| turn | 33/33 | 0 | 0 | 2265.990 | n/a | n/a | 16.425 | 68666.368 | 57732.013 | 136502.074 |
| llm:attempt | 33/33 | 0 | 0 | 2092.203 | 4.443 | 2087.759 | 0.470 | 63400.104 | 53762.512 | 130804.386 |
| teardown:commit | 1/1 | 0 | 0 | 280.626 | 0.010 | 280.616 | 0.008 | 280626.028 | 280626.028 | 280626.028 |
| sandbox:commit | 1/1 | 0 | 0 | 280.436 | 0.008 | 280.428 | 0.008 | 280435.808 | 280435.808 | 280435.808 |
| checkpoint.total | 1/1 | 0 | 0 | 280.436 | 0.007 | 280.428 | 0.008 | 280435.674 | 280435.674 | 280435.674 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 280.436 | 0.007 | 280.428 | 0.008 | 280435.535 | 280435.535 | 280435.535 |
| run:container_call | 15/15 | 2 | 0 | 278.943 | 0.003 | 278.940 | 0.008 | 18596.232 | 52.814 | 120094.396 |
| tool:generate | 14/14 | 0 | 0 | 69.691 | n/a | n/a | 1.386 | 4977.921 | 2485.551 | 14726.123 |
| tool:top_activations | 6/6 | 0 | 0 | 28.982 | n/a | n/a | 0.000 | 4830.395 | 4807.622 | 4965.986 |
| tool:token_stats | 3/3 | 0 | 0 | 27.447 | n/a | n/a | 0.185 | 9148.974 | 10517.953 | 14126.600 |
| tool:bash | 16/16 | 0 | 0 | 22.402 | n/a | n/a | 12.690 | 1400.097 | 1044.171 | 4148.205 |
| process:bash | 16/16 | 0 | 0 | 22.252 | n/a | n/a | 12.665 | 1390.720 | 1035.125 | 4139.122 |
| tool:trace | 6/6 | 0 | 0 | 13.735 | n/a | n/a | 0.000 | 2289.164 | 2088.650 | 4137.730 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.832 | 0.908 | 2.924 | 6.742 | 3832.243 | 3832.243 | 3832.243 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.832 | 0.908 | 2.924 | 6.741 | 3832.005 | 3832.005 | 3832.005 |
| syscall:sendto | 1393/1393 | 0 | 0 | 3.184 | n/a | n/a | 0.253 | 2.285 | 2.027 | 4.505 |
| tool:logit_lens | 2/2 | 0 | 0 | 2.707 | n/a | n/a | 1.529 | 1353.328 | 1353.328 | 1801.439 |
| tool:inspect_module_inputs | 2/2 | 0 | 0 | 2.127 | n/a | n/a | 0.000 | 1063.521 | 1063.521 | 1080.179 |
| tool:attribution | 4/4 | 0 | 0 | 1.319 | n/a | n/a | 0.000 | 329.658 | 330.598 | 333.264 |
| tool:inspect | 1/1 | 0 | 0 | 1.141 | n/a | n/a | 0.000 | 1140.848 | 1140.848 | 1140.848 |
| syscall:connect | 364/364 | 0 | 0 | 0.784 | n/a | n/a | 0.063 | 2.155 | 1.912 | 4.470 |
| sandbox:create | 1/1 | 0 | 0 | 0.687 | 0.263 | 0.423 | 0.000 | 686.868 | 686.868 | 686.868 |
| syscall:execve | 298/298 | 0 | 0 | 0.429 | n/a | n/a | 0.148 | 1.438 | 1.190 | 1.572 |
| run:detect | 1/1 | 0 | 0 | 0.376 | 0.001 | 0.375 | 0.000 | 375.916 | 375.916 | 375.916 |
| sandbox:start | 1/1 | 0 | 0 | 0.369 | 0.002 | 0.366 | 0.000 | 368.878 | 368.878 | 368.878 |
| runtime.container_create | 1/1 | 0 | 0 | 0.369 | 0.002 | 0.366 | 0.000 | 368.711 | 368.711 | 368.711 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.313 | n/a | n/a | 0.000 | 313.399 | 313.399 | 313.399 |
| tool:submit_output | 1/1 | 0 | 0 | 0.245 | n/a | n/a | 0.000 | 245.079 | 245.079 | 245.079 |
| sandbox:stop | 1/1 | 0 | 0 | 0.190 | 0.002 | 0.188 | 0.000 | 189.966 | 189.966 | 189.966 |
| agency:services_close | 1/1 | 0 | 0 | 0.140 | 0.000 | 0.140 | 0.002 | 140.023 | 140.023 | 140.023 |
| agency:services_start | 1/1 | 0 | 0 | 0.076 | 0.043 | 0.034 | 0.000 | 76.088 | 76.088 | 76.088 |
| agent:create | 1/1 | 0 | 0 | 0.047 | 0.007 | 0.039 | 0.000 | 46.566 | 46.566 | 46.566 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 2.195 | 2.195 | 2.195 |
| sync:container | 15/15 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.095 | 0.087 | 0.157 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.256 | 1.256 | 1.256 |
| tool:todowrite | 2/2 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.219 | 0.219 | 0.276 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.180 | 0.180 | 0.180 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.052 | 0.052 | 0.052 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2538 | 0.369 | 0.024 | 91.608 | 14.550 | 9.420853 CPU seconds | n/a |
| GPU 0 memory | MB | 2540 | 12049.303 | 11670.000 | 12816.000 | 12244.000 | n/a | n/a |
| GPU 0 power | W | 2540 | 30.349 | 27.869 | 73.103 | 28.697 | n/a | 77507.585 J |
| GPU 0 proc / 9859-673969 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 memory | MB | 2540 | 3270.247 | 3118.000 | 4014.000 | 3442.000 | n/a | n/a |
| GPU 0 proc / 9859-673969 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 estimated power | W | 1540 | 2.164 | 0.000 | 71.109 | 0.000 | n/a | n/a |
| GPU 0 proc / 9859-673969 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 utilization | percent | 1540 | 1.921 | 0.000 | 86.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 9900-676024 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 memory | MB | 2540 | 8297.056 | 8070.000 | 8320.000 | 8320.000 | n/a | n/a |
| GPU 0 proc / 9900-676024 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 estimated power | W | 964 | 4.739 | 0.000 | 72.313 | 0.000 | n/a | n/a |
| GPU 0 proc / 9900-676024 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 utilization | percent | 964 | 6.409 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2540 | 11567.303 | 11188.000 | 12334.000 | 11762.000 | n/a | n/a |
| GPU 0 utilization | percent | 2540 | 3.708 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2540 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2539 | 0.363 | 0.032 | 19.878 | 0.479 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2539 | 2.509 | 0.000 | 93.052 | 3.788 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2539 | 0.650 | 0.000 | 82.531 | 6.706 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2539 | 0.776 | 0.000 | 213.195 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2539 | 8.708 | 0.000 | 98.713 | 40.646 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2539 | 8.754 | 0.000 | 99.246 | 40.886 | n/a | n/a |
| host mem_total_mb | MB | 2540 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 2540 | 6952.303 | 6425.469 | 8989.188 | 7118.613 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2539 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2539 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2539 | 0.002 | 0.000 | 0.249 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2539 | 0.007 | 0.000 | 1.100 | 0.000 | n/a | n/a |
| docker run (PID 10075) rss_mb | MB | 1 | 30.680 | 30.680 | 30.680 | 30.680 | n/a | n/a |
| docker run (PID 10075) vms_mb | MB | 1 | 1915.523 | 1915.523 | 1915.523 | 1915.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 10120) CPU | percent | 2538 | 0.002 | 0.000 | 0.995 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 10120) rss_mb | MB | 2539 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 10120) main thread run-queue wait | percent | 2538 | 0.000 | 0.000 | 0.945 | 0.000 | 0.009969 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 10120) vms_mb | MB | 2539 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 10152) CPU | percent | 2538 | 0.002 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 10152) rss_mb | MB | 2539 | 1.566 | 1.566 | 1.566 | 1.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 10152) main thread run-queue wait | percent | 2538 | 0.001 | 0.000 | 2.581 | 0.000 | 0.026784 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 10152) vms_mb | MB | 2539 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10242) CPU | percent | 2538 | 2.324 | 0.000 | 100.246 | 0.000 | 59.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10242) rss_mb | MB | 2539 | 104.408 | 3.180 | 108.168 | 108.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10242) main thread run-queue wait | percent | 2538 | 0.000 | 0.000 | 0.018 | 0.000 | 0.000221 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10242) vms_mb | MB | 2539 | 970.290 | 4.258 | 973.492 | 973.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 10248) CPU | percent | 1 | 73.191 | 73.191 | 73.191 | 73.191 | 0.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 10248) rss_mb | MB | 2 | 65.123 | 47.852 | 82.395 | 82.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 10248) main thread run-queue wait | percent | 1 | 0.013 | 0.013 | 0.013 | 0.013 | 0.000135 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 10248) vms_mb | MB | 2 | 77.066 | 56.137 | 97.996 | 97.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 10260) CPU | percent | 2256 | 0.137 | 0.000 | 47.739 | 0.995 | 3.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 10260) rss_mb | MB | 2257 | 73.090 | 29.379 | 76.242 | 76.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 10260) main thread run-queue wait | percent | 2256 | 0.008 | 0.000 | 4.782 | 0.013 | 0.182159 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 10260) vms_mb | MB | 2257 | 87.287 | 36.109 | 90.129 | 90.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 10318) rss_mb | MB | 1 | 12.219 | 12.219 | 12.219 | 12.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 10318) vms_mb | MB | 1 | 15.859 | 15.859 | 15.859 | 15.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10441) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10441) rss_mb | MB | 2 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10441) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10441) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10442) CPU | percent | 1 | 27.730 | 27.730 | 27.730 | 27.730 | 0.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10442) rss_mb | MB | 2 | 20.836 | 14.941 | 26.730 | 26.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10442) main thread run-queue wait | percent | 1 | 8.511 | 8.511 | 8.511 | 8.511 | 0.085934 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10442) vms_mb | MB | 2 | 1879.525 | 1874.250 | 1884.801 | 1884.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10598) rss_mb | MB | 1 | 2.844 | 2.844 | 2.844 | 2.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10598) vms_mb | MB | 1 | 4.328 | 4.328 | 4.328 | 4.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10601) rss_mb | MB | 1 | 7.773 | 7.773 | 7.773 | 7.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10601) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10668) rss_mb | MB | 1 | 2.652 | 2.652 | 2.652 | 2.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10668) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10670) rss_mb | MB | 1 | 54.934 | 54.934 | 54.934 | 54.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10670) vms_mb | MB | 1 | 252.648 | 252.648 | 252.648 | 252.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_components.py (PID 10724) CPU | percent | 5 | 140.196 | 107.185 | 157.822 | 157.822 | 7.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_components.py (PID 10724) rss_mb | MB | 6 | 173.616 | 21.152 | 246.035 | 246.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_components.py (PID 10724) main thread run-queue wait | percent | 5 | 14.800 | 1.741 | 22.759 | 9.145 | 0.745225 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_components.py (PID 10724) vms_mb | MB | 6 | 434.150 | 132.758 | 524.883 | 524.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_neurons.py (PID 10750) CPU | percent | 1 | 118.144 | 118.144 | 118.144 | 118.144 | 1.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_neurons.py (PID 10750) rss_mb | MB | 2 | 121.711 | 117.668 | 125.754 | 117.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_neurons.py (PID 10750) main thread run-queue wait | percent | 1 | 16.414 | 16.414 | 16.414 | 16.414 | 0.165329 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_neurons.py (PID 10750) vms_mb | MB | 2 | 391.748 | 370.254 | 413.242 | 370.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_feature_candidates.py (PID 10762) CPU | percent | 1 | 116.358 | 116.358 | 116.358 | 116.358 | 1.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_feature_candidates.py (PID 10762) rss_mb | MB | 2 | 122.455 | 63.367 | 181.543 | 181.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_feature_candidates.py (PID 10762) main thread run-queue wait | percent | 1 | 7.384 | 7.384 | 7.384 | 7.384 | 0.074246 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_feature_candidates.py (PID 10762) vms_mb | MB | 2 | 318.145 | 175.051 | 461.238 | 461.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10776) rss_mb | MB | 1 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10776) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10777) rss_mb | MB | 1 | 20.695 | 20.695 | 20.695 | 20.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10777) vms_mb | MB | 1 | 212.387 | 212.387 | 212.387 | 212.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10851) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10851) rss_mb | MB | 2 | 2.902 | 2.902 | 2.902 | 2.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10851) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10851) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10852) rss_mb | MB | 1 | 96.547 | 96.547 | 96.547 | 96.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10852) vms_mb | MB | 1 | 288.781 | 288.781 | 288.781 | 288.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10921) rss_mb | MB | 1 | 3.051 | 3.051 | 3.051 | 3.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10921) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10922) rss_mb | MB | 1 | 36.844 | 36.844 | 36.844 | 36.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10922) vms_mb | MB | 1 | 416.945 | 416.945 | 416.945 | 416.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10985) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10985) rss_mb | MB | 4 | 2.867 | 2.867 | 2.867 | 2.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10985) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10985) vms_mb | MB | 4 | 4.219 | 4.219 | 4.219 | 4.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10989) CPU | percent | 3 | 44.000 | 2.975 | 71.463 | 71.463 | 1.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10989) rss_mb | MB | 4 | 105.800 | 98.551 | 113.051 | 113.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10989) main thread run-queue wait | percent | 3 | 0.064 | 0.019 | 0.089 | 0.084 | 0.001938 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10989) vms_mb | MB | 4 | 297.557 | 290.621 | 304.492 | 304.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp6_ituerd.py (PID 10995) rss_mb | MB | 1 | 6.891 | 6.891 | 6.891 | 6.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmp6_ituerd.py (PID 10995) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpuk_xg4b6.py (PID 11034) rss_mb | MB | 1 | 7.422 | 7.422 | 7.422 | 7.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tmpuk_xg4b6.py (PID 11034) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 11050) rss_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 11050) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — finalize_adapter.py (PID 11052) rss_mb | MB | 1 | 21.363 | 21.363 | 21.363 | 21.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — finalize_adapter.py (PID 11052) vms_mb | MB | 1 | 133.602 | 133.602 | 133.602 | 133.602 | n/a | n/a |
| docker commit (PID 11127) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 11127) io read MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 11127) io write MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 11127) rss_mb | MB | 119 | 30.184 | 30.184 | 30.184 | 30.184 | n/a | n/a |
| docker commit (PID 11127) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 11127) vms_mb | MB | 119 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| docker commit (PID 11153) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 11153) io read MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 11153) io write MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 11153) rss_mb | MB | 119 | 29.027 | 29.027 | 29.027 | 29.027 | n/a | n/a |
| docker commit (PID 11153) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 11153) vms_mb | MB | 119 | 1770.938 | 1770.938 | 1770.938 | 1770.938 | n/a | n/a |
| docker commit (PID 11174) CPU | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 11174) io read MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 11174) io write MB/s | MB/s | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 11174) rss_mb | MB | 38 | 30.707 | 30.707 | 30.707 | 30.707 | n/a | n/a |
| docker commit (PID 11174) main thread run-queue wait | percent | 37 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 11174) vms_mb | MB | 38 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4616) CPU | percent | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4616) io read MB/s | MB/s | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4616) io write MB/s | MB/s | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4616) rss_mb | MB | 2540 | 3.391 | 3.391 | 3.391 | 3.391 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4616) main thread run-queue wait | percent | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4616) vms_mb | MB | 2540 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9859) CPU | percent | 2539 | 4.811 | 0.000 | 370.010 | 0.995 | 123.150000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 9859) io read MB/s | MB/s | 2539 | 0.001 | 0.000 | 0.514 | 0.000 | 2.054688 MB | n/a |
| Agency harness — python -m lsbench (PID 9859) io write MB/s | MB/s | 2539 | 0.907 | 0.015 | 626.263 | 0.035 | 2324.964844 MB | n/a |
| Agency harness — python -m lsbench (PID 9859) rss_mb | MB | 2540 | 2874.499 | 2273.242 | 4142.828 | 3097.340 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9859) main thread run-queue wait | percent | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 9859) vms_mb | MB | 2540 | 15966.527 | 13731.867 | 18138.625 | 16251.512 | n/a | n/a |
| Python — vllm (PID 9864) CPU | percent | 2539 | 0.183 | 0.000 | 6.934 | 0.000 | 4.680000 CPU seconds | n/a |
| Python — vllm (PID 9864) io read MB/s | MB/s | 2539 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 9864) io write MB/s | MB/s | 2539 | 0.000 | 0.000 | 0.008 | 0.000 | 0.066406 MB | n/a |
| Python — vllm (PID 9864) rss_mb | MB | 2540 | 1784.203 | 1782.703 | 1784.328 | 1784.328 | n/a | n/a |
| Python — vllm (PID 9864) main thread run-queue wait | percent | 2539 | 0.001 | 0.000 | 0.345 | 0.000 | 0.036471 run-queue seconds | n/a |
| Python — vllm (PID 9864) vms_mb | MB | 2540 | 11023.764 | 10954.152 | 11027.172 | 11027.172 | n/a | n/a |
| Python — python -c (PID 9899) CPU | percent | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 9899) io read MB/s | MB/s | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9899) io write MB/s | MB/s | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9899) rss_mb | MB | 2540 | 12.191 | 12.191 | 12.191 | 12.191 | n/a | n/a |
| Python — python -c (PID 9899) main thread run-queue wait | percent | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 9899) vms_mb | MB | 2540 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 9900) CPU | percent | 2539 | 1.905 | 0.000 | 50.520 | 0.000 | 48.730000 CPU seconds | n/a |
| VLLM::EngineCore (PID 9900) io read MB/s | MB/s | 2539 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 9900) io write MB/s | MB/s | 2539 | 0.000 | 0.000 | 0.004 | 0.000 | 0.015625 MB | n/a |
| VLLM::EngineCore (PID 9900) rss_mb | MB | 2540 | 2320.274 | 2319.863 | 2320.363 | 2320.363 | n/a | n/a |
| VLLM::EngineCore (PID 9900) main thread run-queue wait | percent | 2539 | 0.000 | 0.000 | 0.088 | 0.000 | 0.007255 run-queue seconds | n/a |
| VLLM::EngineCore (PID 9900) vms_mb | MB | 2540 | 21205.003 | 21204.094 | 21205.094 | 21205.094 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 2538 | 3.324 | 0.000 | 202.722 | 0.000 | 84.928677 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2538 | 0.248 | 0.000 | 19.472 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2538 | 0.259 | 0.000 | 19.476 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 2538 | 0.018 | 0.000 | 25.887 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 2538 | 0.018 | 0.000 | 25.887 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 2538 | 0.010 | 0.000 | 7.866 | 0.000 | 24.312500 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 2538 | 0.004 | 0.000 | 6.921 | 0.000 | 8.960938 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 2539 | 173.608 | 47.660 | 378.836 | 136.402 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2538 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2538 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 2538 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000839 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 2538 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 2539 | 6.908 | 1.386 | 370.337 | 1.643 | 176.778612 CPU seconds | n/a |
| workload total memory | MB | 2540 | 7733.777 | 6420.734 | 8876.090 | 8296.141 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
