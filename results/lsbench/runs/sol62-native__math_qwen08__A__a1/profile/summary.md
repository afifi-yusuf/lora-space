# agprof summary

- Duration: **1590.157 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **29 calls**, 29 succeeded, 0 failed, 0 interrupted, n/a reported retries, 575.661 s total wait
- Tools: **66/66 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **147553** at 1.976 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1567440.166 / 1567440.166 ms |
| LLM latency p50 / p95 | 18642.482 / 40777.238 ms |
| LLM TTFT p50 / p95 | 5725.054 / 6525.455 ms |
| LLM input / output tokens | 4422641 / 84725 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 29 total, 29 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1751.812 / 52504.821 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attribution | 1/1 | 1 | 0 | 0 | 315.671 ms | 315.671 ms |
| bash | 23/23 | 23 | 0 | 0 | 730.113 ms | 48326.378 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 304.222 ms | 304.222 ms |
| generate | 16/16 | 16 | 0 | 0 | 20546.480 ms | 131247.144 ms |
| inspect | 1/1 | 1 | 0 | 0 | 1703.153 ms | 1703.153 ms |
| inspect_module_inputs | 1/1 | 1 | 0 | 0 | 1747.201 ms | 1747.201 ms |
| logit_lens | 2/2 | 2 | 0 | 0 | 1000.910 ms | 1105.677 ms |
| patch | 2/2 | 2 | 0 | 0 | 736.515 ms | 1018.529 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 225.760 ms | 225.760 ms |
| trace | 12/12 | 12 | 0 | 0 | 4601.442 ms | 43428.949 ms |
| write | 6/6 | 6 | 0 | 0 | 0.396 ms | 0.762 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 24.397% | 104.376% | 388.236 s | 11056.634 MB | 14872.742 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lsb_grid_worker | 2144 |  | 1578 | 0.000% | 0.000% | 0.000 s | 3.402 MB | 3.402 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| docker | 2346 |  | 1 | n/a% | n/a% | n/a s | 30.156 MB | 30.156 MB | 2060.273 MB | 2060.273 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 2213 |  | 1578 | 13.040% | 41.544% | 207.500 s | 2330.033 MB | 2330.668 MB | 21864.229 MB | 21864.973 MB | 0.000000 MB | 0.007812 MB |
| python | 2212 |  | 1578 | 0.000% | 0.000% | 0.000 s | 12.207 MB | 12.207 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-buildx | 2359 |  | 1 | n/a% | n/a% | n/a s | 35.121 MB | 35.121 MB | 1298.711 MB | 1298.711 MB | n/a MB | n/a MB |
| vllm | 2162 |  | 1578 | 1.100% | 4.967% | 17.510 s | 1789.955 MB | 1790.363 MB | 12028.601 MB | 12029.652 MB | 0.007812 MB | 0.132812 MB |
| python | 2153 |  | 1578 | 10.231% | 103.880% | 162.830 s | 2547.112 MB | 6276.609 MB | 16092.012 MB | 22828.680 MB | 170.824219 MB | 7803.382812 MB |
| docker-init | 2472 | sandbox_agent_lsb-native_0000_0000 | 1554 | 0.002% | 0.995% | 0.030 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2516 | sandbox_agent_lsb-native_0000_0000 | 1554 | 0.002% | 0.995% | 0.030 s | 1.297 MB | 1.297 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 2618 | sandbox_agent_lsb-native_0000_0000 | 1554 | 3.479% | 98.559% | 54.410 s | 104.005 MB | 114.312 MB | 968.045 MB | 975.355 MB | n/a MB | n/a MB |
| python3 | 2624 | sandbox_agent_lsb-native_0000_0000 | 3 | 49.221% | 53.713% | 0.990 s | 35.634 MB | 60.277 MB | 43.212 MB | 69.297 MB | n/a MB | n/a MB |
| python3 | 2636 | sandbox_agent_lsb-native_0000_0000 | 1528 | 0.180% | 59.635% | 2.770 s | 73.371 MB | 79.762 MB | 87.495 MB | 93.840 MB | n/a MB | n/a MB |
| python | 2835 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.117 MB | 7.117 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| bash | 2833 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.715 MB | 2.715 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 2858 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.961 MB | 2.961 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2859 | sandbox_agent_lsb-native_0000_0000 | 2 | 95.433% | 95.433% | 0.960 s | 106.051 MB | 168.648 MB | 219.928 MB | 283.754 MB | n/a MB | n/a MB |
| python | 2879 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 470.477 MB | 470.477 MB | 647.094 MB | 647.094 MB | n/a MB | n/a MB |
| bash | 2878 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.055 MB | 3.055 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 2957 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.086 MB | 3.086 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2958 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 174.902 MB | 174.902 MB | 288.500 MB | 288.500 MB | n/a MB | n/a MB |
| bash | 2993 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.602 MB | 2.602 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 2994 | sandbox_agent_lsb-native_0000_0000 | 6 | 99.671% | 100.490% | 5.010 s | 178.919 MB | 218.145 MB | 292.600 MB | 331.781 MB | n/a MB | n/a MB |
| python | 3010 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.417% | 99.417% | 1.000 s | 123.117 MB | 175.188 MB | 236.895 MB | 289.547 MB | n/a MB | n/a MB |
| bash | 3008 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.078 MB | 3.078 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3017 | sandbox_agent_lsb-native_0000_0000 | 26 | 0.000% | 0.000% | 0.000 s | 3.051 MB | 3.051 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3018 | sandbox_agent_lsb-native_0000_0000 | 26 | 139.894% | 197.931% | 35.180 s | 1628.395 MB | 3610.578 MB | 2232.032 MB | 4182.184 MB | n/a MB | n/a MB |
| bash | 3043 | sandbox_agent_lsb-native_0000_0000 | 39 | 0.000% | 0.000% | 0.000 s | 2.844 MB | 2.844 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3047 | sandbox_agent_lsb-native_0000_0000 | 39 | 159.646% | 211.401% | 61.040 s | 2270.776 MB | 3989.703 MB | 2879.434 MB | 4560.793 MB | n/a MB | n/a MB |
| python | 3098 | sandbox_agent_lsb-native_0000_0000 | 2 | 74.537% | 74.537% | 0.750 s | 204.295 MB | 226.148 MB | 610.699 MB | 658.828 MB | n/a MB | n/a MB |
| bash | 3097 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.961 MB | 2.961 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3127 | sandbox_agent_lsb-native_0000_0000 | 49 | 141.951% | 208.485% | 68.550 s | 1747.597 MB | 3763.414 MB | 2401.058 MB | 4791.637 MB | n/a MB | n/a MB |
| bash | 3126 | sandbox_agent_lsb-native_0000_0000 | 49 | 0.000% | 0.000% | 0.000 s | 2.973 MB | 2.973 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3154 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 174.547 MB | 174.547 MB | 367.504 MB | 367.504 MB | n/a MB | n/a MB |
| bash | 3151 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.887 MB | 2.887 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3168 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.418 MB | 8.418 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| python | 3174 | sandbox_agent_lsb-native_0000_0000 | 53 | 146.452% | 202.539% | 76.580 s | 1794.369 MB | 4246.848 MB | 2422.254 MB | 4818.102 MB | n/a MB | n/a MB |
| bash | 3173 | sandbox_agent_lsb-native_0000_0000 | 53 | 0.000% | 0.000% | 0.000 s | 2.953 MB | 2.953 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| docker | 3260 |  | 21 | 0.000% | 0.000% | 0.000 s | 30.230 MB | 30.230 MB | 2059.766 MB | 2059.766 MB | 0.000000 MB | 0.000000 MB |
| docker | 3322 |  | 1 | n/a% | n/a% | n/a s | 29.445 MB | 29.445 MB | 1843.191 MB | 1843.191 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 45.989% | 100.000% | 12029.766 MB | 14522.000 MB | 49.107 W | 76.263 W | 78090.476 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 20.651% | 212.664% | 322.669 s | 432.401 MB | 4497.617 MB | 111.773438 MB | 1.988281 MB | 0.001337 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2344 | 1590.091 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1567.440 | n/a | n/a | 111.773 | 1567440.166 | 1567440.166 | 1567440.166 |
| engine:execute | 1/1 | 0 | 0 | 1567.438 | 2.476 | 1564.962 | 111.773 | 1567438.478 | 1567438.478 | 1567438.478 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1539.532 | 0.008 | 1539.524 | 72.033 | 1539531.765 | 1539531.765 | 1539531.765 |
| turn | 29/29 | 0 | 0 | 1536.461 | n/a | n/a | 69.195 | 52981.418 | 42665.618 | 147250.206 |
| tool:generate | 16/16 | 0 | 0 | 615.451 | n/a | n/a | 0.202 | 38465.716 | 20546.480 | 131247.144 |
| llm:attempt | 29/29 | 0 | 0 | 575.661 | 3.627 | 572.034 | 8.570 | 19850.395 | 18642.482 | 40777.238 |
| tool:bash | 23/23 | 0 | 0 | 185.259 | n/a | n/a | 58.591 | 8054.720 | 730.113 | 48326.378 |
| process:bash | 23/23 | 1 | 0 | 185.068 | n/a | n/a | 58.529 | 8046.451 | 722.017 | 48315.683 |
| tool:trace | 12/12 | 0 | 0 | 148.613 | n/a | n/a | 0.400 | 12384.402 | 4601.442 | 43428.949 |
| run:container_call | 13/13 | 0 | 0 | 21.997 | 0.002 | 21.994 | 0.010 | 1692.066 | 33.332 | 8699.413 |
| teardown:commit | 1/1 | 0 | 0 | 21.346 | 0.005 | 21.341 | 0.010 | 21346.399 | 21346.399 | 21346.399 |
| sandbox:commit | 1/1 | 0 | 0 | 21.167 | 0.003 | 21.164 | 0.010 | 21167.084 | 21167.084 | 21167.084 |
| checkpoint.total | 1/1 | 0 | 0 | 21.167 | 0.003 | 21.164 | 0.010 | 21166.942 | 21166.942 | 21166.942 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 21.167 | 0.003 | 21.164 | 0.010 | 21166.793 | 21166.793 | 21166.793 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 5.074 | 1.121 | 3.953 | 39.624 | 5073.637 | 5073.637 | 5073.637 |
| runtime.harness_start | 1/1 | 0 | 0 | 5.073 | 1.121 | 3.953 | 39.623 | 5073.334 | 5073.334 | 5073.334 |
| syscall:sendto | 1363/1363 | 0 | 0 | 2.676 | n/a | n/a | 0.541 | 1.964 | 1.703 | 3.660 |
| tool:logit_lens | 2/2 | 0 | 0 | 2.002 | n/a | n/a | 0.159 | 1000.910 | 1000.910 | 1105.677 |
| tool:inspect_module_inputs | 1/1 | 0 | 0 | 1.747 | n/a | n/a | 0.081 | 1747.201 | 1747.201 | 1747.201 |
| tool:inspect | 1/1 | 0 | 0 | 1.703 | n/a | n/a | 0.124 | 1703.153 | 1703.153 | 1703.153 |
| tool:patch | 2/2 | 0 | 0 | 1.473 | n/a | n/a | 0.000 | 736.515 | 736.515 | 1018.529 |
| sandbox:create | 1/1 | 0 | 0 | 1.129 | 0.243 | 0.886 | 0.000 | 1129.265 | 1129.265 | 1129.265 |
| run:detect | 1/1 | 0 | 0 | 0.830 | 0.001 | 0.829 | 0.000 | 829.724 | 829.724 | 829.724 |
| syscall:connect | 382/382 | 0 | 0 | 0.763 | n/a | n/a | 0.304 | 1.998 | 1.711 | 3.728 |
| sandbox:start | 1/1 | 0 | 0 | 0.588 | 0.002 | 0.586 | 0.000 | 588.232 | 588.232 | 588.232 |
| runtime.container_create | 1/1 | 0 | 0 | 0.588 | 0.002 | 0.586 | 0.000 | 588.086 | 588.086 | 588.086 |
| tool:attribution | 1/1 | 0 | 0 | 0.316 | n/a | n/a | 0.000 | 315.671 | 315.671 | 315.671 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.304 | n/a | n/a | 0.000 | 304.222 | 304.222 | 304.222 |
| tool:submit_output | 1/1 | 0 | 0 | 0.226 | n/a | n/a | 0.000 | 225.760 | 225.760 | 225.760 |
| sandbox:stop | 1/1 | 0 | 0 | 0.179 | 0.002 | 0.177 | 0.000 | 179.049 | 179.049 | 179.049 |
| agency:services_close | 1/1 | 0 | 0 | 0.152 | 0.000 | 0.152 | 0.011 | 152.317 | 152.317 | 152.317 |
| syscall:execve | 102/102 | 0 | 0 | 0.152 | n/a | n/a | 0.176 | 1.486 | 1.137 | 3.145 |
| agency:services_start | 1/1 | 0 | 0 | 0.108 | 0.043 | 0.065 | 0.000 | 108.326 | 108.326 | 108.326 |
| agent:create | 1/1 | 0 | 0 | 0.050 | 0.009 | 0.041 | 0.000 | 49.726 | 49.726 | 49.726 |
| tool:write | 6/6 | 0 | 0 | 0.003 | n/a | n/a | 0.001 | 0.503 | 0.396 | 0.762 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.000 | 2.840 | 2.840 | 2.840 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.235 | 1.235 | 1.235 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.069 | 0.066 | 0.097 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.175 | 0.175 | 0.175 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.062 | 0.062 | 0.062 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1576 | 0.499 | 0.031 | 57.891 | 0.072 | 7.914000 CPU seconds | n/a |
| GPU 0 memory | MB | 1578 | 12029.766 | 11670.000 | 14522.000 | 11896.000 | n/a | n/a |
| GPU 0 power | W | 1578 | 49.107 | 27.574 | 76.263 | 27.999 | n/a | 78090.476 J |
| GPU 0 proc / 2153-18088 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 memory | MB | 1578 | 3341.558 | 3118.000 | 5832.000 | 3206.000 | n/a | n/a |
| GPU 0 proc / 2153-18088 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 estimated power | W | 607 | 14.470 | 0.000 | 74.786 | 0.000 | n/a | n/a |
| GPU 0 proc / 2153-18088 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 utilization | percent | 607 | 18.990 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2213-22064 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 memory | MB | 1578 | 8206.208 | 8070.000 | 8208.000 | 8208.000 | n/a | n/a |
| GPU 0 proc / 2213-22064 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 estimated power | W | 955 | 44.287 | 0.000 | 72.533 | 0.000 | n/a | n/a |
| GPU 0 proc / 2213-22064 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 utilization | percent | 955 | 61.238 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1578 | 11547.766 | 11188.000 | 14040.000 | 11414.000 | n/a | n/a |
| GPU 0 utilization | percent | 1578 | 45.989 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1578 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1577 | 3.174 | 0.004 | 75.006 | 0.190 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1577 | 5.541 | 0.000 | 27.148 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1577 | 1.136 | 0.000 | 231.397 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1577 | 4.944 | 0.000 | 247.618 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1577 | 2.391 | 0.000 | 95.174 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1577 | 2.400 | 0.000 | 95.206 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1578 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1578 | 7042.636 | 6302.168 | 11173.488 | 6897.574 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1577 | 0.003 | 0.000 | 0.253 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1577 | 0.015 | 0.000 | 1.485 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2144) CPU | percent | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2144) io read MB/s | MB/s | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2144) io write MB/s | MB/s | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2144) rss_mb | MB | 1578 | 3.402 | 3.402 | 3.402 | 3.402 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2144) main thread run-queue wait | percent | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2144) vms_mb | MB | 1578 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2153) CPU | percent | 1577 | 10.231 | 0.000 | 103.880 | 0.000 | 162.830000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2153) io read MB/s | MB/s | 1577 | 0.107 | 0.000 | 94.069 | 0.000 | 170.824219 MB | n/a |
| Agency harness — python -m lsbench (PID 2153) io write MB/s | MB/s | 1577 | 4.918 | 0.015 | 1379.006 | 0.039 | 7803.382812 MB | n/a |
| Agency harness — python -m lsbench (PID 2153) rss_mb | MB | 1578 | 2547.112 | 1984.551 | 6276.609 | 2765.043 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2153) main thread run-queue wait | percent | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2153) vms_mb | MB | 1578 | 16092.012 | 14062.855 | 22828.680 | 16017.680 | n/a | n/a |
| Python — vllm (PID 2162) CPU | percent | 1577 | 1.100 | 0.000 | 4.967 | 0.000 | 17.510000 CPU seconds | n/a |
| Python — vllm (PID 2162) io read MB/s | MB/s | 1577 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 2162) io write MB/s | MB/s | 1577 | 0.000 | 0.000 | 0.008 | 0.000 | 0.132812 MB | n/a |
| Python — vllm (PID 2162) rss_mb | MB | 1578 | 1789.955 | 1786.188 | 1790.363 | 1790.363 | n/a | n/a |
| Python — vllm (PID 2162) main thread run-queue wait | percent | 1577 | 0.001 | 0.000 | 0.304 | 0.000 | 0.011525 run-queue seconds | n/a |
| Python — vllm (PID 2162) vms_mb | MB | 1578 | 12028.601 | 11954.633 | 12029.652 | 12029.652 | n/a | n/a |
| Python — python -c (PID 2212) CPU | percent | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2212) io read MB/s | MB/s | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2212) io write MB/s | MB/s | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2212) rss_mb | MB | 1578 | 12.207 | 12.207 | 12.207 | 12.207 | n/a | n/a |
| Python — python -c (PID 2212) main thread run-queue wait | percent | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2212) vms_mb | MB | 1578 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2213) CPU | percent | 1577 | 13.040 | 0.000 | 41.544 | 0.996 | 207.500000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2213) io read MB/s | MB/s | 1577 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 2213) io write MB/s | MB/s | 1577 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 2213) rss_mb | MB | 1578 | 2330.033 | 2326.668 | 2330.668 | 2330.668 | n/a | n/a |
| VLLM::EngineCore (PID 2213) main thread run-queue wait | percent | 1577 | 0.002 | 0.000 | 0.029 | 0.000 | 0.029346 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2213) vms_mb | MB | 1578 | 21864.229 | 21860.727 | 21864.973 | 21864.973 | n/a | n/a |
| docker info (PID 2346) rss_mb | MB | 1 | 30.156 | 30.156 | 30.156 | 30.156 | n/a | n/a |
| docker info (PID 2346) vms_mb | MB | 1 | 2060.273 | 2060.273 | 2060.273 | 2060.273 | n/a | n/a |
| docker-buildx (PID 2359) rss_mb | MB | 1 | 35.121 | 35.121 | 35.121 | 35.121 | n/a | n/a |
| docker-buildx (PID 2359) vms_mb | MB | 1 | 1298.711 | 1298.711 | 1298.711 | 1298.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2472) CPU | percent | 1553 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2472) rss_mb | MB | 1554 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2472) main thread run-queue wait | percent | 1553 | 0.007 | 0.000 | 6.293 | 0.000 | 0.109408 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2472) vms_mb | MB | 1554 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2516) CPU | percent | 1553 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2516) rss_mb | MB | 1554 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2516) main thread run-queue wait | percent | 1553 | 0.009 | 0.000 | 6.913 | 0.000 | 0.133979 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2516) vms_mb | MB | 1554 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2618) CPU | percent | 1553 | 3.479 | 0.000 | 98.559 | 0.000 | 54.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2618) rss_mb | MB | 1554 | 104.005 | 2.902 | 114.312 | 113.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2618) main thread run-queue wait | percent | 1553 | 0.000 | 0.000 | 0.008 | 0.000 | 0.000120 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2618) vms_mb | MB | 1554 | 968.045 | 4.258 | 975.355 | 975.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2624) CPU | percent | 2 | 49.221 | 44.728 | 53.713 | 53.713 | 0.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2624) rss_mb | MB | 3 | 35.634 | 6.160 | 60.277 | 60.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2624) main thread run-queue wait | percent | 2 | 0.050 | 0.041 | 0.059 | 0.041 | 0.001009 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2624) vms_mb | MB | 3 | 43.212 | 11.680 | 69.297 | 69.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2636) CPU | percent | 1527 | 0.180 | 0.000 | 59.635 | 0.000 | 2.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2636) rss_mb | MB | 1528 | 73.371 | 30.918 | 79.762 | 78.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2636) main thread run-queue wait | percent | 1527 | 0.002 | 0.000 | 2.858 | 0.000 | 0.031436 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2636) vms_mb | MB | 1528 | 87.495 | 36.215 | 93.840 | 92.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2833) rss_mb | MB | 1 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2833) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2835) rss_mb | MB | 1 | 7.117 | 7.117 | 7.117 | 7.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2835) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2858) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2858) rss_mb | MB | 2 | 2.961 | 2.961 | 2.961 | 2.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2858) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2858) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2859) CPU | percent | 1 | 95.433 | 95.433 | 95.433 | 95.433 | 0.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2859) rss_mb | MB | 2 | 106.051 | 43.453 | 168.648 | 43.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2859) main thread run-queue wait | percent | 1 | 0.011 | 0.011 | 0.011 | 0.011 | 0.000113 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2859) vms_mb | MB | 2 | 219.928 | 156.102 | 283.754 | 156.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2878) rss_mb | MB | 1 | 3.055 | 3.055 | 3.055 | 3.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2878) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2879) rss_mb | MB | 1 | 470.477 | 470.477 | 470.477 | 470.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2879) vms_mb | MB | 1 | 647.094 | 647.094 | 647.094 | 647.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2957) rss_mb | MB | 1 | 3.086 | 3.086 | 3.086 | 3.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2957) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2958) rss_mb | MB | 1 | 174.902 | 174.902 | 174.902 | 174.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 2958) vms_mb | MB | 1 | 288.500 | 288.500 | 288.500 | 288.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2993) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2993) rss_mb | MB | 6 | 2.602 | 2.602 | 2.602 | 2.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2993) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2993) vms_mb | MB | 6 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — phase_labels.py (PID 2994) CPU | percent | 5 | 99.671 | 98.409 | 100.490 | 99.502 | 5.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — phase_labels.py (PID 2994) rss_mb | MB | 6 | 178.919 | 80.332 | 218.145 | 218.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — phase_labels.py (PID 2994) main thread run-queue wait | percent | 5 | 0.005 | 0.001 | 0.007 | 0.006 | 0.000228 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — phase_labels.py (PID 2994) vms_mb | MB | 6 | 292.600 | 193.090 | 331.781 | 331.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3008) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3008) rss_mb | MB | 2 | 3.078 | 3.078 | 3.078 | 3.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3008) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3008) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3010) CPU | percent | 1 | 99.417 | 99.417 | 99.417 | 99.417 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3010) rss_mb | MB | 2 | 123.117 | 71.047 | 175.188 | 175.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3010) main thread run-queue wait | percent | 1 | 0.007 | 0.007 | 0.007 | 0.007 | 0.000066 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3010) vms_mb | MB | 2 | 236.895 | 184.242 | 289.547 | 289.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3017) CPU | percent | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3017) rss_mb | MB | 26 | 3.051 | 3.051 | 3.051 | 3.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3017) main thread run-queue wait | percent | 25 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3017) vms_mb | MB | 26 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gates.py (PID 3018) CPU | percent | 25 | 139.894 | 44.723 | 197.931 | 168.056 | 35.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gates.py (PID 3018) rss_mb | MB | 26 | 1628.395 | 180.906 | 3610.578 | 3610.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gates.py (PID 3018) main thread run-queue wait | percent | 25 | 27.299 | 0.002 | 67.661 | 33.617 | 6.863341 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gates.py (PID 3018) vms_mb | MB | 26 | 2232.032 | 724.293 | 4182.184 | 4182.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3043) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3043) rss_mb | MB | 39 | 2.844 | 2.844 | 2.844 | 2.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3043) main thread run-queue wait | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3043) vms_mb | MB | 39 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gaps.py (PID 3047) CPU | percent | 38 | 159.646 | 86.455 | 211.401 | 198.413 | 61.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gaps.py (PID 3047) rss_mb | MB | 39 | 2270.776 | 19.496 | 3989.703 | 2869.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gaps.py (PID 3047) main thread run-queue wait | percent | 38 | 35.207 | 0.001 | 67.177 | 50.288 | 13.461489 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — gaps.py (PID 3047) vms_mb | MB | 39 | 2879.434 | 291.438 | 4560.793 | 3440.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3097) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3097) rss_mb | MB | 2 | 2.961 | 2.961 | 2.961 | 2.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3097) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3097) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3098) CPU | percent | 1 | 74.537 | 74.537 | 74.537 | 74.537 | 0.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3098) rss_mb | MB | 2 | 204.295 | 182.441 | 226.148 | 226.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3098) main thread run-queue wait | percent | 1 | 0.044 | 0.044 | 0.044 | 0.044 | 0.000446 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3098) vms_mb | MB | 2 | 610.699 | 562.570 | 658.828 | 658.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3126) CPU | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3126) rss_mb | MB | 49 | 2.973 | 2.973 | 2.973 | 2.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3126) main thread run-queue wait | percent | 48 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3126) vms_mb | MB | 49 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — feature_design.py (PID 3127) CPU | percent | 48 | 141.951 | 87.495 | 208.485 | 160.825 | 68.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — feature_design.py (PID 3127) rss_mb | MB | 49 | 1747.597 | 164.625 | 3763.414 | 3763.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — feature_design.py (PID 3127) main thread run-queue wait | percent | 48 | 26.880 | 0.001 | 68.470 | 33.477 | 12.983398 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — feature_design.py (PID 3127) vms_mb | MB | 49 | 2401.058 | 438.461 | 4791.637 | 4791.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3151) rss_mb | MB | 1 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3151) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3154) rss_mb | MB | 1 | 174.547 | 174.547 | 174.547 | 174.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3154) vms_mb | MB | 1 | 367.504 | 367.504 | 367.504 | 367.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m py_compile (PID 3168) rss_mb | MB | 1 | 8.418 | 8.418 | 8.418 | 8.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m py_compile (PID 3168) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3173) CPU | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3173) rss_mb | MB | 53 | 2.953 | 2.953 | 2.953 | 2.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3173) main thread run-queue wait | percent | 52 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3173) vms_mb | MB | 53 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 3174) CPU | percent | 52 | 146.452 | 85.572 | 202.539 | 195.963 | 76.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 3174) rss_mb | MB | 53 | 1794.369 | 133.168 | 4246.848 | 2017.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 3174) main thread run-queue wait | percent | 52 | 29.881 | 0.000 | 74.206 | 69.181 | 15.627940 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 3174) vms_mb | MB | 53 | 2422.254 | 407.219 | 4818.102 | 2589.387 | n/a | n/a |
| docker commit (PID 3260) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 3260) io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3260) io write MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 3260) rss_mb | MB | 21 | 30.230 | 30.230 | 30.230 | 30.230 | n/a | n/a |
| docker commit (PID 3260) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 3260) vms_mb | MB | 21 | 2059.766 | 2059.766 | 2059.766 | 2059.766 | n/a | n/a |
| docker stop (PID 3322) rss_mb | MB | 1 | 29.445 | 29.445 | 29.445 | 29.445 | n/a | n/a |
| docker stop (PID 3322) vms_mb | MB | 1 | 1843.191 | 1843.191 | 1843.191 | 1843.191 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 1553 | 20.651 | 0.000 | 212.664 | 0.000 | 322.669421 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1553 | 3.344 | 0.000 | 69.306 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1553 | 3.350 | 0.000 | 74.614 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 1553 | 0.107 | 0.000 | 53.845 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 1553 | 0.107 | 0.000 | 53.845 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 1553 | 0.072 | 0.000 | 24.338 | 0.000 | 111.773438 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 1553 | 0.001 | 0.000 | 0.735 | 0.000 | 1.988281 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 1554 | 432.401 | 15.469 | 4497.617 | 232.266 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1553 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1553 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 1553 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001337 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 1553 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 1577 | 24.397 | 1.319 | 104.376 | 2.026 | 388.236198 CPU seconds | n/a |
| workload total memory | MB | 1578 | 11056.634 | 7907.070 | 14872.742 | 12641.797 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
