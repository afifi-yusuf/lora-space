# agprof summary

- Duration: **14401.248 s**
- Runs: **0/1 completed**, 0 succeeded, 0 failed, 1 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **145 calls**, 144 succeeded, 0 failed, 1 interrupted, n/a reported retries, 12036.876 s total wait
- Tools: **159/159 completed**, 2 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **1419367** at 1.973 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | n/a / n/a ms |
| LLM latency p50 / p95 | 59254.951 / 243825.077 ms |
| LLM TTFT p50 / p95 | 40286.628 / 238023.215 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 145 total, 144 succeeded, 0 failed, 1 interrupted |
| Tool latency p50 / p95 | 84.569 / 64071.338 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attribution | 4/4 | 4 | 0 | 0 | 1360.894 ms | 1376.577 ms |
| bash | 103/103 | 101 | 2 | 0 | 84.114 ms | 25492.454 ms |
| edit | 5/5 | 5 | 0 | 0 | 0.785 ms | 0.822 ms |
| generate | 11/11 | 11 | 0 | 0 | 15503.046 ms | 528631.643 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 5651.621 ms | 5651.621 ms |
| read | 2/2 | 2 | 0 | 0 | 0.602 ms | 0.725 ms |
| todowrite | 2/2 | 2 | 0 | 0 | 0.329 ms | 0.495 ms |
| token_stats | 1/1 | 1 | 0 | 0 | 38750.990 ms | 38750.990 ms |
| top_activations | 8/8 | 8 | 0 | 0 | 23443.246 ms | 23798.299 ms |
| trace | 5/5 | 5 | 0 | 0 | 4712.390 ms | 47389.085 ms |
| write | 17/17 | 17 | 0 | 0 | 0.416 ms | 0.772 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 7.713% | 222.330% | 1114.195 s | 8832.887 MB | 12963.586 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lsb_grid_worker | 1730 |  | 14316 | 0.000% | 0.000% | 0.000 s | 3.335 MB | 3.395 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| docker | 1916 |  | 1 | n/a% | n/a% | n/a s | 29.504 MB | 29.504 MB | 1843.270 MB | 1843.270 MB | n/a MB | n/a MB |
| python | 1908 |  | 14316 | 0.031% | 4.952% | 4.510 s | 44.740 MB | 46.230 MB | 131.272 MB | 132.203 MB | 0.671875 MB | 0.449219 MB |
| python | 1739 |  | 14316 | 3.567% | 222.346% | 515.490 s | 2943.148 MB | 5443.797 MB | 15936.202 MB | 20108.074 MB | 188.878906 MB | 3691.609375 MB |
| docker-buildx | 1926 |  | 1 | n/a% | n/a% | n/a s | 35.539 MB | 35.539 MB | 1362.281 MB | 1362.281 MB | n/a MB | n/a MB |
| vllm | 1751 |  | 14316 | 0.310% | 6.916% | 44.710 s | 1789.759 MB | 1793.984 MB | 11058.964 MB | 11064.719 MB | 0.019531 MB | 0.199219 MB |
| python | 1786 |  | 14316 | 0.000% | 0.000% | 0.000 s | 11.887 MB | 12.195 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 1787 |  | 14316 | 3.804% | 45.598% | 549.240 s | 2322.034 MB | 2332.387 MB | 21243.666 MB | 21244.215 MB | 0.101562 MB | 0.097656 MB |
| docker-init | 2024 | sandbox_agent_lsb-native_0000_0000 | 14315 | 0.002% | 0.996% | 0.340 s | 0.594 MB | 0.594 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2058 | sandbox_agent_lsb-native_0000_0000 | 14315 | 0.003% | 0.996% | 0.390 s | 1.414 MB | 1.414 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 2155 | sandbox_agent_lsb-native_0000_0000 | 3 | 55.668% | 63.678% | 1.120 s | 40.884 MB | 68.172 MB | 48.128 MB | 76.938 MB | n/a MB | n/a MB |
| bash | 2149 | sandbox_agent_lsb-native_0000_0000 | 14315 | 2.300% | 100.471% | 331.150 s | 104.158 MB | 111.023 MB | 971.043 MB | 972.887 MB | n/a MB | n/a MB |
| python3 | 2167 | sandbox_agent_lsb-native_0000_0000 | 14310 | 0.027% | 40.695% | 3.830 s | 73.447 MB | 77.324 MB | 88.058 MB | 92.367 MB | n/a MB | n/a MB |
| bash | 2230 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.730 MB | 2.730 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 2636 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.227 MB | 12.227 MB | 16.586 MB | 16.586 MB | n/a MB | n/a MB |
| python3 | 2760 | sandbox_agent_lsb-native_0000_0000 | 2 | 144.123% | 144.123% | 1.450 s | 730.111 MB | 1067.945 MB | 995.814 MB | 1290.695 MB | n/a MB | n/a MB |
| bash | 3227 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| python3 | 3261 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.723 MB | 7.723 MB | 12.930 MB | 12.930 MB | n/a MB | n/a MB |
| python3 | 3315 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 74.258 MB | 74.258 MB | 269.246 MB | 269.246 MB | n/a MB | n/a MB |
| python3 | 3326 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2280.379 MB | 2280.379 MB | 2729.770 MB | 2729.770 MB | n/a MB | n/a MB |
| python3 | 3367 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1936.055 MB | 1936.055 MB | 2724.922 MB | 2724.922 MB | n/a MB | n/a MB |
| python3 | 3658 | sandbox_agent_lsb-native_0000_0000 | 3 | 157.112% | 197.886% | 3.160 s | 727.529 MB | 1084.523 MB | 941.655 MB | 1308.668 MB | n/a MB | n/a MB |
| python3 | 3695 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 26.914 MB | 26.914 MB | 218.070 MB | 218.070 MB | n/a MB | n/a MB |
| python3 | 3874 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.285 MB | 9.285 MB | 13.266 MB | 13.266 MB | n/a MB | n/a MB |
| bash | 3921 | sandbox_agent_lsb-native_0000_0000 | 2 | 105.647% | 105.647% | 1.070 s | 542.072 MB | 1081.281 MB | 654.205 MB | 1304.195 MB | n/a MB | n/a MB |
| sed | 4017 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.250 MB | 0.250 MB | n/a MB | n/a MB |
| bash | 4016 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.039 MB | 3.039 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 4051 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.508 MB | 7.508 MB | 11.934 MB | 11.934 MB | n/a MB | n/a MB |
| bash | 4106 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.074 MB | 3.074 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 4242 | sandbox_agent_lsb-native_0000_0000 | 2 | 123.258% | 123.258% | 1.240 s | 561.229 MB | 1105.852 MB | 768.498 MB | 1328.246 MB | n/a MB | n/a MB |
| python3 | 4253 | sandbox_agent_lsb-native_0000_0000 | 2 | 184.225% | 184.225% | 1.860 s | 1126.541 MB | 1170.098 MB | 1348.861 MB | 1392.203 MB | n/a MB | n/a MB |
| python3 | 4293 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 367.352 MB | 367.352 MB | 703.141 MB | 703.141 MB | n/a MB | n/a MB |
| python3 | 4468 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1045.543 MB | 1045.543 MB | 1268.777 MB | 1268.777 MB | n/a MB | n/a MB |
| python3 | 4585 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.473 MB | 12.473 MB | 15.977 MB | 15.977 MB | n/a MB | n/a MB |
| python3 | 4630 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.898 MB | 6.898 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python3 | 4706 | sandbox_agent_lsb-native_0000_0000 | 119 | 197.772% | 204.820% | 235.080 s | 239.396 MB | 387.496 MB | 650.754 MB | 651.055 MB | n/a MB | n/a MB |
| python3 | 4758 | sandbox_agent_lsb-native_0000_0000 | 119 | 195.560% | 202.760% | 232.450 s | 481.107 MB | 765.914 MB | 838.510 MB | 978.457 MB | n/a MB | n/a MB |
| python3 | 4780 | sandbox_agent_lsb-native_0000_0000 | 26 | 188.729% | 202.559% | 47.530 s | 2351.222 MB | 2688.844 MB | 2777.328 MB | 3121.121 MB | n/a MB | n/a MB |
| python3 | 4824 | sandbox_agent_lsb-native_0000_0000 | 14 | 179.960% | 201.236% | 23.550 s | 2359.587 MB | 2913.523 MB | 2793.009 MB | 3332.988 MB | n/a MB | n/a MB |
| python3 | 4874 | sandbox_agent_lsb-native_0000_0000 | 99 | 109.730% | 202.474% | 108.250 s | 4203.608 MB | 5457.035 MB | 5430.877 MB | 5888.781 MB | n/a MB | n/a MB |
| python3 | 4948 | sandbox_agent_lsb-native_0000_0000 | 108 | 110.485% | 203.754% | 118.930 s | 4170.970 MB | 5466.680 MB | 5334.244 MB | 5898.312 MB | n/a MB | n/a MB |
| python3 | 4972 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.023 MB | 13.023 MB | 207.172 MB | 207.172 MB | n/a MB | n/a MB |
| python3 | 5022 | sandbox_agent_lsb-native_0000_0000 | 100 | 113.702% | 202.180% | 113.290 s | 4228.103 MB | 5473.664 MB | 5441.903 MB | 5905.488 MB | n/a MB | n/a MB |
| python3 | 5075 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.711 MB | 20.711 MB | 212.383 MB | 212.383 MB | n/a MB | n/a MB |
| python3 | 5117 | sandbox_agent_lsb-native_0000_0000 | 18 | 145.844% | 201.752% | 25.000 s | 2192.115 MB | 2714.773 MB | 2632.728 MB | 3147.121 MB | n/a MB | n/a MB |
| python3 | 5214 | sandbox_agent_lsb-native_0000_0000 | 2 | 145.188% | 145.188% | 1.460 s | 519.412 MB | 1018.051 MB | 726.547 MB | 1240.754 MB | n/a MB | n/a MB |
| python3 | 5228 | sandbox_agent_lsb-native_0000_0000 | 5 | 100.010% | 100.524% | 4.020 s | 11.980 MB | 11.980 MB | 15.906 MB | 15.906 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10.900% | 100.000% | 11976.589 MB | 14614.000 MB | 34.224 W | 77.531 W | 493113.586 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 8.946% | 207.868% | 1289.135 s | 438.143 MB | 6609.176 MB | 3714.140625 MB | 3.121094 MB | 0.001671 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 1914 | 14401.181 | interrupted |
| run0:write_lora_adapter:agent_lsb-native_0000 | -1 | 14401.180 | interrupted |
| engine:execute | 1915 | 14401.179 | interrupted |
| harness:attempt_rpc | 2162 | 14395.060 | interrupted |
| turn143 | -1 | 51.000 | interrupted |
| llm:attempt[0] | 5233 | 50.915 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| turn | 143/144 | 0 | 1 | 14341.307 | n/a | n/a | 3673.263 | 100288.862 | 64721.205 | 310634.091 |
| llm:attempt | 144/145 | 0 | 1 | 12036.876 | 6.316 | 12030.560 | 13.358 | 83589.418 | 59254.951 | 243825.077 |
| tool:generate | 11/11 | 0 | 0 | 1339.162 | n/a | n/a | 0.020 | 121742.014 | 15503.046 | 528631.643 |
| tool:bash | 103/103 | 2 | 0 | 641.233 | n/a | n/a | 3657.204 | 6225.562 | 84.114 | 25492.454 |
| process:bash | 103/103 | 12 | 0 | 640.332 | n/a | n/a | 3656.933 | 6216.812 | 75.812 | 25480.483 |
| tool:top_activations | 8/8 | 0 | 0 | 177.855 | n/a | n/a | 0.078 | 22231.827 | 23443.246 | 23798.299 |
| llm:compact | 1/1 | 0 | 0 | 108.079 | n/a | n/a | 0.000 | 108078.541 | 108078.541 | 108078.541 |
| tool:trace | 5/5 | 0 | 0 | 83.193 | n/a | n/a | 0.000 | 16638.559 | 4712.390 | 47389.085 |
| tool:token_stats | 1/1 | 0 | 0 | 38.751 | n/a | n/a | 0.000 | 38750.990 | 38750.990 | 38750.990 |
| syscall:sendto | 2595/2595 | 0 | 0 | 6.251 | n/a | n/a | 0.964 | 2.409 | 2.099 | 4.756 |
| tool:logit_lens | 1/1 | 0 | 0 | 5.652 | n/a | n/a | 0.000 | 5651.621 | 5651.621 | 5651.621 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.879 | 1.139 | 3.739 | 39.250 | 4879.088 | 4879.088 | 4879.088 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.879 | 1.139 | 3.739 | 39.250 | 4878.828 | 4878.828 | 4878.828 |
| tool:attribution | 4/4 | 0 | 0 | 4.666 | n/a | n/a | 0.000 | 1166.498 | 1360.894 | 1376.577 |
| syscall:connect | 721/721 | 0 | 0 | 1.753 | n/a | n/a | 0.355 | 2.431 | 2.083 | 5.108 |
| sandbox:create | 1/1 | 0 | 0 | 1.113 | 0.251 | 0.861 | 0.000 | 1112.548 | 1112.548 | 1112.548 |
| run:detect | 1/1 | 0 | 0 | 0.811 | 0.001 | 0.810 | 0.000 | 810.773 | 810.773 | 810.773 |
| run:container_call | 6/6 | 0 | 0 | 0.646 | 0.001 | 0.644 | 0.000 | 107.677 | 54.893 | 331.851 |
| sandbox:start | 1/1 | 0 | 0 | 0.577 | 0.003 | 0.574 | 0.000 | 577.397 | 577.397 | 577.397 |
| runtime.container_create | 1/1 | 0 | 0 | 0.577 | 0.003 | 0.574 | 0.000 | 577.263 | 577.263 | 577.263 |
| syscall:execve | 323/323 | 0 | 0 | 0.503 | n/a | n/a | 0.222 | 1.557 | 1.154 | 3.460 |
| agency:services_start | 1/1 | 0 | 0 | 0.084 | 0.041 | 0.043 | 0.000 | 84.127 | 84.127 | 84.127 |
| agent:create | 1/1 | 0 | 0 | 0.051 | 0.010 | 0.041 | 0.000 | 50.557 | 50.557 | 50.557 |
| tool:write | 17/17 | 0 | 0 | 0.008 | n/a | n/a | 0.000 | 0.487 | 0.416 | 0.772 |
| tool:edit | 5/5 | 0 | 0 | 0.004 | n/a | n/a | 0.000 | 0.782 | 0.785 | 0.822 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.290 | 1.290 | 1.290 |
| tool:read | 2/2 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.602 | 0.602 | 0.725 |
| tool:todowrite | 2/2 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.329 | 0.329 | 0.495 |
| sync:container | 6/6 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.087 | 0.083 | 0.137 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.205 | 0.205 | 0.205 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.097 | 0.097 | 0.097 |
| engine:execute | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| run:write_lora_adapter | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:attempt_rpc | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 14314 | 0.097 | 0.031 | 0.719 | 0.079 | 13.970542 CPU seconds | n/a |
| GPU 0 memory | MB | 14316 | 11976.589 | 11670.000 | 14614.000 | 11996.000 | n/a | n/a |
| GPU 0 power | W | 14316 | 34.224 | 28.891 | 77.531 | 29.430 | n/a | 493113.586 J |
| GPU 0 proc / 1739-2951 / sandbox / ~ / device / GPU-49f48660-27b2-aba8-db67-9aacc9a39ec8 memory | MB | 14316 | 3206.734 | 3118.000 | 5832.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 1739-2951 / sandbox / ~ / device / GPU-49f48660-27b2-aba8-db67-9aacc9a39ec8 estimated power | W | 7759 | 2.267 | 0.000 | 75.980 | 0.000 | n/a | n/a |
| GPU 0 proc / 1739-2951 / sandbox / ~ / device / GPU-49f48660-27b2-aba8-db67-9aacc9a39ec8 utilization | percent | 7759 | 2.964 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 1787-6880 / sandbox / ~ / device / GPU-49f48660-27b2-aba8-db67-9aacc9a39ec8 memory | MB | 14316 | 8287.855 | 8070.000 | 8300.000 | 8300.000 | n/a | n/a |
| GPU 0 proc / 1787-6880 / sandbox / ~ / device / GPU-49f48660-27b2-aba8-db67-9aacc9a39ec8 estimated power | W | 6339 | 14.553 | 0.000 | 72.682 | 0.000 | n/a | n/a |
| GPU 0 proc / 1787-6880 / sandbox / ~ / device / GPU-49f48660-27b2-aba8-db67-9aacc9a39ec8 utilization | percent | 6339 | 20.203 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 14316 | 11494.589 | 11188.000 | 14132.000 | 11514.000 | n/a | n/a |
| GPU 0 utilization | percent | 14316 | 10.900 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 14316 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 14315 | 1.623 | 0.008 | 66.982 | 0.500 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 14315 | 3.962 | 0.252 | 55.831 | 0.505 | n/a | n/a |
| host disk_read_mb_s | MB/s | 14315 | 0.277 | 0.000 | 212.429 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 14315 | 0.267 | 0.000 | 243.689 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 14315 | 0.141 | 0.000 | 94.314 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 14315 | 0.143 | 0.000 | 94.891 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 14316 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 14316 | 7166.074 | 6363.176 | 13228.289 | 8004.879 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 14315 | 0.007 | 0.000 | 9.657 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 14315 | 0.007 | 0.000 | 9.658 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 14315 | 0.000 | 0.000 | 0.078 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 14315 | 0.005 | 0.000 | 1.064 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1730) CPU | percent | 14315 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1730) io read MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1730) io write MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1730) rss_mb | MB | 14316 | 3.335 | 2.887 | 3.395 | 2.887 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1730) main thread run-queue wait | percent | 14315 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1730) vms_mb | MB | 14316 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1739) CPU | percent | 14315 | 3.567 | 0.000 | 222.346 | 0.995 | 515.490000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 1739) io read MB/s | MB/s | 14315 | 0.013 | 0.000 | 92.751 | 0.000 | 188.878906 MB | n/a |
| Agency harness — python -m lsbench (PID 1739) io write MB/s | MB/s | 14315 | 0.256 | 0.015 | 891.827 | 0.027 | 3691.609375 MB | n/a |
| Agency harness — python -m lsbench (PID 1739) rss_mb | MB | 14316 | 2943.148 | 2208.289 | 5443.797 | 3845.152 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1739) main thread run-queue wait | percent | 14315 | 0.000 | 0.000 | 0.301 | 0.000 | 0.006959 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 1739) vms_mb | MB | 14316 | 15936.202 | 13646.812 | 20108.074 | 16858.996 | n/a | n/a |
| Python — vllm (PID 1751) CPU | percent | 14315 | 0.310 | 0.000 | 6.916 | 0.000 | 44.710000 CPU seconds | n/a |
| Python — vllm (PID 1751) io read MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.008 | 0.000 | 0.019531 MB | n/a |
| Python — vllm (PID 1751) io write MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.008 | 0.000 | 0.199219 MB | n/a |
| Python — vllm (PID 1751) rss_mb | MB | 14316 | 1789.759 | 1776.773 | 1793.984 | 1776.773 | n/a | n/a |
| Python — vllm (PID 1751) main thread run-queue wait | percent | 14315 | 0.002 | 0.000 | 0.518 | 0.000 | 0.338027 run-queue seconds | n/a |
| Python — vllm (PID 1751) vms_mb | MB | 14316 | 11058.964 | 10986.699 | 11064.719 | 11062.719 | n/a | n/a |
| Python — python -c (PID 1786) CPU | percent | 14315 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 1786) io read MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1786) io write MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1786) rss_mb | MB | 14316 | 11.887 | 9.566 | 12.195 | 9.566 | n/a | n/a |
| Python — python -c (PID 1786) main thread run-queue wait | percent | 14315 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 1786) vms_mb | MB | 14316 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 1787) CPU | percent | 14315 | 3.804 | 0.000 | 45.598 | 1.989 | 549.240000 CPU seconds | n/a |
| VLLM::EngineCore (PID 1787) io read MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.089 | 0.000 | 0.101562 MB | n/a |
| VLLM::EngineCore (PID 1787) io write MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.008 | 0.000 | 0.097656 MB | n/a |
| VLLM::EngineCore (PID 1787) rss_mb | MB | 14316 | 2322.034 | 2240.699 | 2332.387 | 2240.699 | n/a | n/a |
| VLLM::EngineCore (PID 1787) main thread run-queue wait | percent | 14315 | 0.001 | 0.000 | 0.148 | 0.000 | 0.082223 run-queue seconds | n/a |
| VLLM::EngineCore (PID 1787) vms_mb | MB | 14316 | 21243.666 | 21236.094 | 21244.215 | 21244.215 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1908) CPU | percent | 14315 | 0.031 | 0.000 | 4.952 | 0.000 | 4.510000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1908) io read MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.476 | 0.000 | 0.671875 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1908) io write MB/s | MB/s | 14315 | 0.000 | 0.000 | 0.008 | 0.000 | 0.449219 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1908) rss_mb | MB | 14316 | 44.740 | 41.062 | 46.230 | 41.883 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1908) main thread run-queue wait | percent | 14315 | 0.001 | 0.000 | 0.227 | 0.000 | 0.081436 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1908) vms_mb | MB | 14316 | 131.272 | 131.172 | 132.203 | 131.188 | n/a | n/a |
| docker info (PID 1916) rss_mb | MB | 1 | 29.504 | 29.504 | 29.504 | 29.504 | n/a | n/a |
| docker info (PID 1916) vms_mb | MB | 1 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| docker-buildx (PID 1926) rss_mb | MB | 1 | 35.539 | 35.539 | 35.539 | 35.539 | n/a | n/a |
| docker-buildx (PID 1926) vms_mb | MB | 1 | 1362.281 | 1362.281 | 1362.281 | 1362.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2024) CPU | percent | 14314 | 0.002 | 0.000 | 0.996 | 0.000 | 0.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2024) rss_mb | MB | 14315 | 0.594 | 0.594 | 0.594 | 0.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2024) main thread run-queue wait | percent | 14314 | 0.002 | 0.000 | 5.238 | 0.000 | 0.317300 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2024) vms_mb | MB | 14315 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2058) CPU | percent | 14314 | 0.003 | 0.000 | 0.996 | 0.000 | 0.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2058) rss_mb | MB | 14315 | 1.414 | 1.414 | 1.414 | 1.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2058) main thread run-queue wait | percent | 14314 | 0.003 | 0.000 | 5.201 | 0.000 | 0.393788 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2058) vms_mb | MB | 14315 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2149) CPU | percent | 14314 | 2.300 | 0.000 | 100.471 | 2.984 | 331.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2149) rss_mb | MB | 14315 | 104.158 | 2.902 | 111.023 | 110.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2149) main thread run-queue wait | percent | 14314 | 0.000 | 0.000 | 0.007 | 0.000 | 0.000081 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2149) vms_mb | MB | 14315 | 971.043 | 4.258 | 972.887 | 972.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2155) CPU | percent | 2 | 55.668 | 47.657 | 63.678 | 63.678 | 1.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2155) rss_mb | MB | 3 | 40.884 | 8.684 | 68.172 | 68.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2155) main thread run-queue wait | percent | 2 | 0.025 | 0.020 | 0.030 | 0.020 | 0.000506 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2155) vms_mb | MB | 3 | 48.128 | 13.281 | 76.938 | 76.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2167) CPU | percent | 14309 | 0.027 | 0.000 | 40.695 | 0.000 | 3.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2167) rss_mb | MB | 14310 | 73.447 | 44.867 | 77.324 | 75.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2167) main thread run-queue wait | percent | 14309 | 0.002 | 0.000 | 4.773 | 0.000 | 0.337543 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2167) vms_mb | MB | 14310 | 88.058 | 52.246 | 92.367 | 90.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2230) rss_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2230) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2636) rss_mb | MB | 1 | 12.227 | 12.227 | 12.227 | 12.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2636) vms_mb | MB | 1 | 16.586 | 16.586 | 16.586 | 16.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2760) CPU | percent | 1 | 144.123 | 144.123 | 144.123 | 144.123 | 1.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2760) rss_mb | MB | 2 | 730.111 | 392.277 | 1067.945 | 1067.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2760) main thread run-queue wait | percent | 1 | 16.328 | 16.328 | 16.328 | 16.328 | 0.164276 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2760) vms_mb | MB | 2 | 995.814 | 700.934 | 1290.695 | 1290.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3227) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3227) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3261) rss_mb | MB | 1 | 7.723 | 7.723 | 7.723 | 7.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3261) vms_mb | MB | 1 | 12.930 | 12.930 | 12.930 | 12.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3315) rss_mb | MB | 1 | 74.258 | 74.258 | 74.258 | 74.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3315) vms_mb | MB | 1 | 269.246 | 269.246 | 269.246 | 269.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3326) rss_mb | MB | 1 | 2280.379 | 2280.379 | 2280.379 | 2280.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3326) vms_mb | MB | 1 | 2729.770 | 2729.770 | 2729.770 | 2729.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3367) rss_mb | MB | 1 | 1936.055 | 1936.055 | 1936.055 | 1936.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3367) vms_mb | MB | 1 | 2724.922 | 2724.922 | 2724.922 | 2724.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_6.py (PID 3658) CPU | percent | 2 | 157.112 | 116.338 | 197.886 | 197.886 | 3.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_6.py (PID 3658) rss_mb | MB | 3 | 727.529 | 13.539 | 1084.523 | 1084.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_6.py (PID 3658) main thread run-queue wait | percent | 2 | 30.338 | 10.641 | 50.034 | 50.034 | 0.610178 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_6.py (PID 3658) vms_mb | MB | 3 | 941.655 | 207.629 | 1308.668 | 1308.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_subspaces_t6.py (PID 3695) rss_mb | MB | 1 | 26.914 | 26.914 | 26.914 | 26.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_subspaces_t6.py (PID 3695) vms_mb | MB | 1 | 218.070 | 218.070 | 218.070 | 218.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3874) rss_mb | MB | 1 | 9.285 | 9.285 | 9.285 | 9.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3874) vms_mb | MB | 1 | 13.266 | 13.266 | 13.266 | 13.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3921) CPU | percent | 1 | 105.647 | 105.647 | 105.647 | 105.647 | 1.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3921) rss_mb | MB | 2 | 542.072 | 2.863 | 1081.281 | 1081.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3921) main thread run-queue wait | percent | 1 | 15.580 | 15.580 | 15.580 | 15.580 | 0.157793 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3921) vms_mb | MB | 2 | 654.205 | 4.215 | 1304.195 | 1304.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4016) rss_mb | MB | 1 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4016) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sed (PID 4017) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — sed (PID 4017) vms_mb | MB | 1 | 0.250 | 0.250 | 0.250 | 0.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4051) rss_mb | MB | 1 | 7.508 | 7.508 | 7.508 | 7.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4051) vms_mb | MB | 1 | 11.934 | 11.934 | 11.934 | 11.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4106) rss_mb | MB | 1 | 3.074 | 3.074 | 3.074 | 3.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4106) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_9.py (PID 4242) CPU | percent | 1 | 123.258 | 123.258 | 123.258 | 123.258 | 1.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_9.py (PID 4242) rss_mb | MB | 2 | 561.229 | 16.605 | 1105.852 | 1105.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_9.py (PID 4242) main thread run-queue wait | percent | 1 | 12.708 | 12.708 | 12.708 | 12.708 | 0.127849 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_9.py (PID 4242) vms_mb | MB | 2 | 768.498 | 208.750 | 1328.246 | 1328.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_9.py (PID 4253) CPU | percent | 1 | 184.225 | 184.225 | 184.225 | 184.225 | 1.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_9.py (PID 4253) rss_mb | MB | 2 | 1126.541 | 1082.984 | 1170.098 | 1170.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_9.py (PID 4253) main thread run-queue wait | percent | 1 | 47.540 | 47.540 | 47.540 | 47.540 | 0.479976 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_trace_9.py (PID 4253) vms_mb | MB | 2 | 1348.861 | 1305.520 | 1392.203 | 1392.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_wait_circuit.py (PID 4293) rss_mb | MB | 1 | 367.352 | 367.352 | 367.352 | 367.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — inspect_wait_circuit.py (PID 4293) vms_mb | MB | 1 | 703.141 | 703.141 | 703.141 | 703.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4468) rss_mb | MB | 1 | 1045.543 | 1045.543 | 1045.543 | 1045.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4468) vms_mb | MB | 1 | 1268.777 | 1268.777 | 1268.777 | 1268.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4585) rss_mb | MB | 1 | 12.473 | 12.473 | 12.473 | 12.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4585) vms_mb | MB | 1 | 15.977 | 15.977 | 15.977 | 15.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4630) rss_mb | MB | 1 | 6.898 | 6.898 | 6.898 | 6.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4630) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4706) CPU | percent | 118 | 197.772 | 184.923 | 204.820 | 197.858 | 235.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4706) rss_mb | MB | 119 | 239.396 | 122.637 | 387.496 | 172.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4706) main thread run-queue wait | percent | 118 | 47.266 | 37.204 | 55.226 | 49.541 | 56.182137 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4706) vms_mb | MB | 119 | 650.754 | 618.418 | 651.055 | 651.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4758) CPU | percent | 118 | 195.560 | 162.889 | 202.760 | 200.152 | 232.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4758) rss_mb | MB | 119 | 481.107 | 133.391 | 765.914 | 619.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4758) main thread run-queue wait | percent | 118 | 47.193 | 29.721 | 54.899 | 48.979 | 56.096722 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4758) vms_mb | MB | 119 | 838.510 | 345.258 | 978.457 | 929.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4780) CPU | percent | 25 | 188.729 | 44.736 | 202.559 | 198.960 | 47.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4780) rss_mb | MB | 26 | 2351.222 | 32.203 | 2688.844 | 2687.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4780) main thread run-queue wait | percent | 25 | 46.671 | 2.921 | 55.017 | 50.610 | 11.751935 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_nullspace_subspaces.py (PID 4780) vms_mb | MB | 26 | 2777.328 | 412.480 | 3121.121 | 3121.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design_and_verify_exploration.py (PID 4824) CPU | percent | 13 | 179.960 | 70.271 | 201.236 | 201.181 | 23.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design_and_verify_exploration.py (PID 4824) rss_mb | MB | 14 | 2359.587 | 32.984 | 2913.523 | 2683.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design_and_verify_exploration.py (PID 4824) main thread run-queue wait | percent | 13 | 42.917 | 0.049 | 55.427 | 50.863 | 5.615765 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design_and_verify_exploration.py (PID 4824) vms_mb | MB | 14 | 2793.009 | 412.758 | 3332.988 | 3115.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_vocab_and_items.py (PID 4874) CPU | percent | 98 | 109.730 | 9.945 | 202.474 | 122.317 | 108.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_vocab_and_items.py (PID 4874) rss_mb | MB | 99 | 4203.608 | 4.367 | 5457.035 | 3495.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_vocab_and_items.py (PID 4874) main thread run-queue wait | percent | 98 | 6.716 | 0.001 | 54.397 | 4.004 | 6.636421 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_vocab_and_items.py (PID 4874) vms_mb | MB | 99 | 5430.877 | 10.000 | 5888.781 | 3926.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_combined_loo.py (PID 4948) CPU | percent | 107 | 110.485 | 8.953 | 203.754 | 99.465 | 118.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_combined_loo.py (PID 4948) rss_mb | MB | 108 | 4170.970 | 161.035 | 5466.680 | 5406.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_combined_loo.py (PID 4948) main thread run-queue wait | percent | 107 | 8.798 | 0.001 | 54.208 | 0.004 | 9.478738 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_combined_loo.py (PID 4948) vms_mb | MB | 108 | 5334.244 | 981.816 | 5898.312 | 5898.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4972) rss_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 4972) vms_mb | MB | 1 | 207.172 | 207.172 | 207.172 | 207.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_combined_loo.py (PID 5022) CPU | percent | 99 | 113.702 | 10.940 | 202.180 | 101.450 | 113.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_combined_loo.py (PID 5022) rss_mb | MB | 100 | 4228.103 | 24.133 | 5473.664 | 5265.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_combined_loo.py (PID 5022) main thread run-queue wait | percent | 99 | 8.270 | 0.001 | 51.575 | 0.005 | 8.245371 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test_combined_loo.py (PID 5022) vms_mb | MB | 100 | 5441.903 | 216.590 | 5905.488 | 5905.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5075) rss_mb | MB | 1 | 20.711 | 20.711 | 20.711 | 20.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5075) vms_mb | MB | 1 | 212.383 | 212.383 | 212.383 | 212.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 5117) CPU | percent | 17 | 145.844 | 12.933 | 201.752 | 195.870 | 25.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 5117) rss_mb | MB | 18 | 2192.115 | 14.555 | 2714.773 | 2592.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 5117) main thread run-queue wait | percent | 17 | 34.527 | 0.015 | 55.942 | 55.942 | 5.919258 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 5117) vms_mb | MB | 18 | 2632.728 | 209.172 | 3147.121 | 3024.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5214) CPU | percent | 1 | 145.188 | 145.188 | 145.188 | 145.188 | 1.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5214) rss_mb | MB | 2 | 519.412 | 20.773 | 1018.051 | 1018.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5214) main thread run-queue wait | percent | 1 | 16.843 | 16.843 | 16.843 | 16.843 | 0.169376 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5214) vms_mb | MB | 2 | 726.547 | 212.340 | 1240.754 | 1240.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5228) CPU | percent | 4 | 100.010 | 99.465 | 100.524 | 100.517 | 4.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5228) rss_mb | MB | 5 | 11.980 | 11.980 | 11.980 | 11.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5228) main thread run-queue wait | percent | 4 | 0.002 | 0.002 | 0.003 | 0.003 | 0.000094 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5228) vms_mb | MB | 5 | 15.906 | 15.906 | 15.906 | 15.906 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 14314 | 8.946 | 0.844 | 207.868 | 1.898 | 1289.135166 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 14314 | 1.422 | 0.002 | 50.807 | 0.649 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 14314 | 1.476 | 0.002 | 66.551 | 0.649 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 14314 | 0.048 | 0.000 | 36.316 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 14314 | 0.049 | 0.000 | 36.327 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 14314 | 0.258 | 0.000 | 212.740 | 0.000 | 3714.140625 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 14314 | 0.000 | 0.000 | 0.502 | 0.000 | 3.121094 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 14315 | 438.143 | 18.426 | 6609.176 | 1665.191 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 14314 | 0.007 | 0.000 | 9.339 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 14314 | 0.007 | 0.000 | 9.339 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 14314 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001671 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 14314 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 14315 | 7.713 | 1.340 | 222.330 | 2.295 | 1114.194518 CPU seconds | n/a |
| workload total memory | MB | 14316 | 8832.887 | 7460.047 | 12963.586 | 7678.043 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
