# agprof summary

- Duration: **720.104 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **88 calls**, 85 succeeded, 3 failed, 0 interrupted, n/a reported retries, 576.238 s total wait
- Tools: **84/84 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **66201** at 1.977 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 693975.608 / 693975.608 ms |
| LLM latency p50 / p95 | 5183.322 / 19814.246 ms |
| LLM TTFT p50 / p95 | 2238.942 / 7942.042 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 88 total, 85 succeeded, 3 failed, 0 interrupted |
| Tool latency p50 / p95 | 437.753 / 2563.962 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 1/1 | 1 | 0 | 0 | 432.991 ms | 432.991 ms |
| attribution | 1/1 | 1 | 0 | 0 | 418.778 ms | 418.778 ms |
| bash | 63/63 | 63 | 0 | 0 | 343.375 ms | 1157.982 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 326.511 ms | 326.511 ms |
| generate | 5/5 | 5 | 0 | 0 | 2598.061 ms | 6813.600 ms |
| logit_lens | 5/5 | 5 | 0 | 0 | 1177.571 ms | 1604.738 ms |
| read | 1/1 | 1 | 0 | 0 | 0.474 ms | 0.474 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 221.479 ms | 221.479 ms |
| token_stats | 1/1 | 1 | 0 | 0 | 1857.709 ms | 1857.709 ms |
| trace | 5/5 | 5 | 0 | 0 | 1310.199 ms | 2331.848 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 7.457% | 227.420% | 53.633 s | 5649.944 MB | 6528.168 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VLLM::EngineCor | 17955 |  | 715 | 2.297% | 54.490% | 16.520 s | 2326.598 MB | 2326.598 MB | 21891.594 MB | 21891.594 MB | 0.000000 MB | 0.003906 MB |
| python | 17894 |  | 715 | 4.938% | 226.273% | 35.520 s | 2672.959 MB | 3447.355 MB | 16290.336 MB | 17196.980 MB | 0.000000 MB | 980.136719 MB |
| python | 17954 |  | 715 | 0.000% | 0.000% | 0.000 s | 12.336 MB | 12.336 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| tail | 18256 | sandbox_agent_lsb-native_0000_0000 | 689 | 0.003% | 0.995% | 0.020 s | 1.527 MB | 1.527 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 18364 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.879% | 99.879% | 1.010 s | 58.674 MB | 83.973 MB | 69.059 MB | 98.148 MB | n/a MB | n/a MB |
| lsb_grid_worker | 16555 |  | 715 | 0.000% | 0.000% | 0.000 s | 3.312 MB | 3.312 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 18358 | sandbox_agent_lsb-native_0000_0000 | 689 | 10.319% | 101.451% | 71.430 s | 104.238 MB | 108.480 MB | 963.925 MB | 972.984 MB | n/a MB | n/a MB |
| vllm | 17903 |  | 715 | 0.195% | 5.944% | 1.400 s | 1775.425 MB | 1775.508 MB | 11984.466 MB | 11985.977 MB | 0.000000 MB | 0.023438 MB |
| docker-init | 18217 | sandbox_agent_lsb-native_0000_0000 | 689 | 0.003% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 18376 | sandbox_agent_lsb-native_0000_0000 | 684 | 0.352% | 58.700% | 2.420 s | 73.099 MB | 74.660 MB | 86.242 MB | 87.578 MB | n/a MB | n/a MB |
| python3 | 18430 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.359 MB | 7.359 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 18723 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 963.023 MB | 963.023 MB | 2528.051 MB | 2528.051 MB | n/a MB | n/a MB |
| bash | 18722 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.824 MB | 2.824 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18747 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.629 MB | 15.629 MB | 2034.176 MB | 2034.176 MB | n/a MB | n/a MB |
| bash | 18746 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.980 MB | 2.980 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18774 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1623.477 MB | 1623.477 MB | 2800.965 MB | 2800.965 MB | n/a MB | n/a MB |
| bash | 18772 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.770 MB | 2.770 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18786 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 995.559 MB | 995.559 MB | 1378.797 MB | 1378.797 MB | n/a MB | n/a MB |
| bash | 18785 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.020 MB | 3.020 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 18835 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.117 MB | 3.117 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18836 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.410 MB | 14.410 MB | 367.289 MB | 367.289 MB | n/a MB | n/a MB |
| bash | 18855 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.871 MB | 2.871 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18856 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 471.680 MB | 471.680 MB | 1499.488 MB | 1499.488 MB | n/a MB | n/a MB |
| bash | 18870 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.012 MB | 3.012 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18871 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.309 MB | 7.309 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| bash | 18882 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.148 MB | 3.148 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18883 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1161.980 MB | 1161.980 MB | 1514.465 MB | 1514.465 MB | n/a MB | n/a MB |
| bash | 18894 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.875 MB | 2.875 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18895 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 126.992 MB | 126.992 MB | 479.621 MB | 479.621 MB | n/a MB | n/a MB |
| bash | 18906 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.910 MB | 2.910 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18907 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.836 MB | 13.836 MB | 367.152 MB | 367.152 MB | n/a MB | n/a MB |
| bash | 18920 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.777 MB | 2.777 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18921 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 70.770 MB | 70.770 MB | 429.160 MB | 429.160 MB | n/a MB | n/a MB |
| bash | 18933 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.840 MB | 2.840 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18934 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 128.402 MB | 128.402 MB | 480.086 MB | 480.086 MB | n/a MB | n/a MB |
| bash | 18964 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.809 MB | 2.809 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18965 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.594 MB | 13.594 MB | 367.133 MB | 367.133 MB | n/a MB | n/a MB |
| bash | 18986 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.832 MB | 2.832 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18987 | sandbox_agent_lsb-native_0000_0000 | 2 | 150.131% | 150.131% | 1.510 s | 642.992 MB | 1231.488 MB | 1035.121 MB | 1657.809 MB | n/a MB | n/a MB |
| bash | 19001 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.934 MB | 2.934 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 19002 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 148.125 MB | 148.125 MB | 499.070 MB | 499.070 MB | n/a MB | n/a MB |
| bash | 19059 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.977 MB | 2.977 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 19060 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.617 MB | 13.617 MB | 367.129 MB | 367.129 MB | n/a MB | n/a MB |
| python3 | 19086 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 55.109 MB | 55.109 MB | 66.758 MB | 66.758 MB | n/a MB | n/a MB |
| python3 | 19091 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 148.414 MB | 148.414 MB | 153.320 MB | 153.320 MB | n/a MB | n/a MB |
| python3 | 19109 | sandbox_agent_lsb-native_0000_0000 | 19 | 70.295% | 100.020% | 12.730 s | 1166.056 MB | 1230.941 MB | 1500.482 MB | 1583.820 MB | n/a MB | n/a MB |
| bash | 19108 | sandbox_agent_lsb-native_0000_0000 | 19 | 0.000% | 0.000% | 0.000 s | 2.941 MB | 2.941 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 19124 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 775.930 MB | 775.930 MB | 1485.602 MB | 1485.602 MB | n/a MB | n/a MB |
| bash | 19123 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.137 MB | 3.137 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 19155 | sandbox_agent_lsb-native_0000_0000 | 19 | 68.782% | 78.521% | 12.460 s | 1182.965 MB | 1245.496 MB | 1535.316 MB | 1597.867 MB | n/a MB | n/a MB |
| bash | 19154 | sandbox_agent_lsb-native_0000_0000 | 19 | 0.000% | 0.000% | 0.000 s | 3.082 MB | 3.082 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 19169 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.949 MB | 2.949 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 19170 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.516 MB | 20.516 MB | 371.832 MB | 371.832 MB | n/a MB | n/a MB |
| docker | 19224 |  | 2 | 0.000% | 0.000% | 0.000 s | 29.785 MB | 29.785 MB | 2060.539 MB | 2060.539 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 3.351% | 100.000% | 11818.168 MB | 12412.000 MB | 29.634 W | 73.378 W | 21286.730 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 18.627% | 172.046% | 128.940 s | 796.637 MB | 2379.555 MB | 0.000000 MB | 971.425781 MB | 0.000893 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 18087 | 720.049 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 693.976 | n/a | n/a | 0.000 | 693975.608 | 693975.608 | 693975.608 |
| engine:execute | 1/1 | 0 | 0 | 693.974 | 1.463 | 692.510 | 0.000 | 693974.033 | 693974.033 | 693974.033 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 688.226 | 0.002 | 688.224 | 0.000 | 688226.315 | 688226.315 | 688226.315 |
| turn | 85/85 | 0 | 0 | 684.327 | n/a | n/a | 0.000 | 8050.903 | 6181.483 | 22999.288 |
| llm:attempt | 88/88 | 3 | 0 | 576.238 | 8.837 | 567.400 | 0.000 | 6548.163 | 5183.322 | 19814.246 |
| tool:bash | 63/63 | 0 | 0 | 63.027 | n/a | n/a | 0.000 | 1000.429 | 343.375 | 1157.982 |
| process:bash | 63/63 | 6 | 0 | 62.488 | n/a | n/a | 0.000 | 991.879 | 329.269 | 1149.971 |
| tool:generate | 5/5 | 0 | 0 | 19.666 | n/a | n/a | 0.000 | 3933.257 | 2598.061 | 6813.600 |
| tool:trace | 5/5 | 0 | 0 | 7.204 | n/a | n/a | 0.000 | 1440.756 | 1310.199 | 2331.848 |
| tool:logit_lens | 5/5 | 0 | 0 | 5.707 | n/a | n/a | 0.000 | 1141.425 | 1177.571 | 1604.738 |
| syscall:sendto | 1575/1575 | 0 | 0 | 3.605 | n/a | n/a | 0.000 | 2.289 | 2.008 | 4.285 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.038 | 0.689 | 2.348 | 0.000 | 3037.841 | 3037.841 | 3037.841 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.038 | 0.689 | 2.348 | 0.000 | 3037.536 | 3037.536 | 3037.536 |
| run:container_call | 13/13 | 0 | 0 | 2.457 | 0.002 | 2.454 | 0.000 | 188.983 | 35.665 | 837.955 |
| teardown:commit | 1/1 | 0 | 0 | 2.075 | 0.004 | 2.071 | 0.000 | 2074.996 | 2074.996 | 2074.996 |
| sandbox:commit | 1/1 | 0 | 0 | 1.899 | 0.002 | 1.896 | 0.000 | 1898.730 | 1898.730 | 1898.730 |
| checkpoint.total | 1/1 | 0 | 0 | 1.899 | 0.002 | 1.896 | 0.000 | 1898.579 | 1898.579 | 1898.579 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.898 | 0.002 | 1.896 | 0.000 | 1898.438 | 1898.438 | 1898.438 |
| tool:token_stats | 1/1 | 0 | 0 | 1.858 | n/a | n/a | 0.000 | 1857.709 | 1857.709 | 1857.709 |
| syscall:connect | 395/395 | 0 | 0 | 0.959 | n/a | n/a | 0.000 | 2.427 | 2.031 | 5.074 |
| llm:retry_backoff | 3/3 | 0 | 0 | 0.954 | n/a | n/a | 0.000 | 318.045 | 296.768 | 440.298 |
| tool:attention | 1/1 | 0 | 0 | 0.433 | n/a | n/a | 0.000 | 432.991 | 432.991 | 432.991 |
| tool:attribution | 1/1 | 0 | 0 | 0.419 | n/a | n/a | 0.000 | 418.778 | 418.778 | 418.778 |
| sandbox:create | 1/1 | 0 | 0 | 0.337 | 0.253 | 0.084 | 0.000 | 337.310 | 337.310 | 337.310 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.327 | n/a | n/a | 0.000 | 326.511 | 326.511 | 326.511 |
| sandbox:start | 1/1 | 0 | 0 | 0.318 | 0.002 | 0.315 | 0.000 | 317.634 | 317.634 | 317.634 |
| runtime.container_create | 1/1 | 0 | 0 | 0.318 | 0.002 | 0.315 | 0.000 | 317.500 | 317.500 | 317.500 |
| syscall:execve | 209/209 | 0 | 0 | 0.278 | n/a | n/a | 0.000 | 1.332 | 1.142 | 2.386 |
| tool:submit_output | 1/1 | 0 | 0 | 0.221 | n/a | n/a | 0.000 | 221.479 | 221.479 | 221.479 |
| sandbox:stop | 1/1 | 0 | 0 | 0.176 | 0.002 | 0.174 | 0.000 | 175.981 | 175.981 | 175.981 |
| agency:services_close | 1/1 | 0 | 0 | 0.158 | 0.001 | 0.158 | 0.000 | 158.283 | 158.283 | 158.283 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.031 | 0.000 | 72.603 | 72.603 | 72.603 |
| run:detect | 1/1 | 0 | 0 | 0.046 | 0.001 | 0.046 | 0.000 | 46.403 | 46.403 | 46.403 |
| agent:create | 1/1 | 0 | 0 | 0.039 | 0.009 | 0.030 | 0.000 | 39.225 | 39.225 | 39.225 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.240 | 1.240 | 1.240 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 1.115 | 1.115 | 1.115 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.071 | 0.061 | 0.118 |
| tool:read | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.474 | 0.474 | 0.474 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.180 | 0.180 | 0.180 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.061 | 0.061 | 0.061 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 714 | 0.500 | 0.043 | 155.767 | 0.104 | 3.590698 CPU seconds | n/a |
| GPU 0 memory | MB | 715 | 11818.168 | 11670.000 | 12412.000 | 11832.000 | n/a | n/a |
| GPU 0 power | W | 715 | 29.634 | 27.961 | 73.378 | 28.108 | n/a | 21286.730 J |
| GPU 0 proc / 17894-2324372 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c memory | MB | 715 | 3179.510 | 3118.000 | 3782.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 17894-2324372 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c estimated power | W | 576 | 1.269 | 0.000 | 61.900 | 0.000 | n/a | n/a |
| GPU 0 proc / 17894-2324372 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c utilization | percent | 576 | 0.835 | 0.000 | 84.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 17955-2326143 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c memory | MB | 715 | 8156.657 | 8070.000 | 8164.000 | 8164.000 | n/a | n/a |
| GPU 0 proc / 17955-2326143 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c estimated power | W | 130 | 10.195 | 0.000 | 71.668 | 0.000 | n/a | n/a |
| GPU 0 proc / 17955-2326143 / sandbox / ~ / device / GPU-0330525c-9189-2c14-01e5-20398058228c utilization | percent | 130 | 12.846 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 715 | 11336.168 | 11188.000 | 11930.000 | 11350.000 | n/a | n/a |
| GPU 0 utilization | percent | 715 | 3.351 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 715 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 714 | 0.942 | 0.033 | 33.017 | 0.112 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 714 | 3.140 | 0.000 | 28.856 | 0.250 | n/a | n/a |
| host disk_read_mb_s | MB/s | 714 | 0.000 | 0.000 | 0.210 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 714 | 2.745 | 0.000 | 244.403 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 714 | 0.910 | 0.000 | 94.642 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 714 | 0.915 | 0.000 | 95.008 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 715 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 715 | 7067.274 | 6362.141 | 9113.168 | 7029.219 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 714 | 0.000 | 0.000 | 0.004 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 714 | 0.000 | 0.000 | 0.004 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 714 | 0.010 | 0.000 | 0.249 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 714 | 0.029 | 0.000 | 0.418 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 16555) CPU | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 16555) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 16555) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 16555) rss_mb | MB | 715 | 3.312 | 3.312 | 3.312 | 3.312 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 16555) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 16555) vms_mb | MB | 715 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 17894) CPU | percent | 714 | 4.938 | 0.000 | 226.273 | 0.000 | 35.520000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 17894) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Agency harness — python -m lsbench (PID 17894) io write MB/s | MB/s | 714 | 1.358 | 0.000 | 218.771 | 0.035 | 980.136719 MB | n/a |
| Agency harness — python -m lsbench (PID 17894) rss_mb | MB | 715 | 2672.959 | 2034.809 | 3447.355 | 2937.047 | n/a | n/a |
| Agency harness — python -m lsbench (PID 17894) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000005 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 17894) vms_mb | MB | 715 | 16290.336 | 14148.020 | 17196.980 | 16573.902 | n/a | n/a |
| Python — vllm (PID 17903) CPU | percent | 714 | 0.195 | 0.000 | 5.944 | 0.000 | 1.400000 CPU seconds | n/a |
| Python — vllm (PID 17903) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 17903) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.008 | 0.000 | 0.023438 MB | n/a |
| Python — vllm (PID 17903) rss_mb | MB | 715 | 1775.425 | 1774.383 | 1775.508 | 1775.508 | n/a | n/a |
| Python — vllm (PID 17903) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.048 | 0.000 | 0.002048 run-queue seconds | n/a |
| Python — vllm (PID 17903) vms_mb | MB | 715 | 11984.466 | 11913.957 | 11985.977 | 11985.977 | n/a | n/a |
| Python — python -c (PID 17954) CPU | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 17954) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 17954) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 17954) rss_mb | MB | 715 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| Python — python -c (PID 17954) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 17954) vms_mb | MB | 715 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 17955) CPU | percent | 714 | 2.297 | 0.000 | 54.490 | 0.995 | 16.520000 CPU seconds | n/a |
| VLLM::EngineCore (PID 17955) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 17955) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 17955) rss_mb | MB | 715 | 2326.598 | 2326.598 | 2326.598 | 2326.598 | n/a | n/a |
| VLLM::EngineCore (PID 17955) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.016 | 0.000 | 0.001350 run-queue seconds | n/a |
| VLLM::EngineCore (PID 17955) vms_mb | MB | 715 | 21891.594 | 21891.594 | 21891.594 | 21891.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 18217) CPU | percent | 688 | 0.003 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 18217) rss_mb | MB | 689 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 18217) main thread run-queue wait | percent | 688 | 0.000 | 0.000 | 0.066 | 0.000 | 0.001067 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 18217) vms_mb | MB | 689 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 18256) CPU | percent | 688 | 0.003 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 18256) rss_mb | MB | 689 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 18256) main thread run-queue wait | percent | 688 | 0.000 | 0.000 | 0.075 | 0.000 | 0.001565 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 18256) vms_mb | MB | 689 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18358) CPU | percent | 688 | 10.319 | 0.000 | 101.451 | 0.000 | 71.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18358) rss_mb | MB | 689 | 104.238 | 3.051 | 108.480 | 107.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18358) main thread run-queue wait | percent | 688 | 0.000 | 0.000 | 0.009 | 0.000 | 0.000134 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18358) vms_mb | MB | 689 | 963.925 | 4.258 | 972.984 | 972.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 18364) CPU | percent | 1 | 99.879 | 99.879 | 99.879 | 99.879 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 18364) rss_mb | MB | 2 | 58.674 | 33.375 | 83.973 | 83.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 18364) main thread run-queue wait | percent | 1 | 0.012 | 0.012 | 0.012 | 0.012 | 0.000121 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 18364) vms_mb | MB | 2 | 69.059 | 39.969 | 98.148 | 98.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 18376) CPU | percent | 683 | 0.352 | 0.000 | 58.700 | 0.000 | 2.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 18376) rss_mb | MB | 684 | 73.099 | 31.266 | 74.660 | 73.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 18376) main thread run-queue wait | percent | 683 | 0.013 | 0.000 | 3.848 | 0.000 | 0.090305 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 18376) vms_mb | MB | 684 | 86.242 | 36.254 | 87.578 | 87.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 18430) rss_mb | MB | 1 | 7.359 | 7.359 | 7.359 | 7.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 18430) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18722) rss_mb | MB | 1 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18722) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18723) rss_mb | MB | 1 | 963.023 | 963.023 | 963.023 | 963.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18723) vms_mb | MB | 1 | 2528.051 | 2528.051 | 2528.051 | 2528.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18746) rss_mb | MB | 1 | 2.980 | 2.980 | 2.980 | 2.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18746) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18747) rss_mb | MB | 1 | 15.629 | 15.629 | 15.629 | 15.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18747) vms_mb | MB | 1 | 2034.176 | 2034.176 | 2034.176 | 2034.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18772) rss_mb | MB | 1 | 2.770 | 2.770 | 2.770 | 2.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18772) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18774) rss_mb | MB | 1 | 1623.477 | 1623.477 | 1623.477 | 1623.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18774) vms_mb | MB | 1 | 2800.965 | 2800.965 | 2800.965 | 2800.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18785) rss_mb | MB | 1 | 3.020 | 3.020 | 3.020 | 3.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18785) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18786) rss_mb | MB | 1 | 995.559 | 995.559 | 995.559 | 995.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18786) vms_mb | MB | 1 | 1378.797 | 1378.797 | 1378.797 | 1378.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18835) rss_mb | MB | 1 | 3.117 | 3.117 | 3.117 | 3.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18835) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18836) rss_mb | MB | 1 | 14.410 | 14.410 | 14.410 | 14.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18836) vms_mb | MB | 1 | 367.289 | 367.289 | 367.289 | 367.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18855) rss_mb | MB | 1 | 2.871 | 2.871 | 2.871 | 2.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18855) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18856) rss_mb | MB | 1 | 471.680 | 471.680 | 471.680 | 471.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18856) vms_mb | MB | 1 | 1499.488 | 1499.488 | 1499.488 | 1499.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18870) rss_mb | MB | 1 | 3.012 | 3.012 | 3.012 | 3.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18870) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18871) rss_mb | MB | 1 | 7.309 | 7.309 | 7.309 | 7.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18871) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18882) rss_mb | MB | 1 | 3.148 | 3.148 | 3.148 | 3.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18882) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18883) rss_mb | MB | 1 | 1161.980 | 1161.980 | 1161.980 | 1161.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18883) vms_mb | MB | 1 | 1514.465 | 1514.465 | 1514.465 | 1514.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18894) rss_mb | MB | 1 | 2.875 | 2.875 | 2.875 | 2.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18894) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18895) rss_mb | MB | 1 | 126.992 | 126.992 | 126.992 | 126.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18895) vms_mb | MB | 1 | 479.621 | 479.621 | 479.621 | 479.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18906) rss_mb | MB | 1 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18906) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18907) rss_mb | MB | 1 | 13.836 | 13.836 | 13.836 | 13.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18907) vms_mb | MB | 1 | 367.152 | 367.152 | 367.152 | 367.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18920) rss_mb | MB | 1 | 2.777 | 2.777 | 2.777 | 2.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18920) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18921) rss_mb | MB | 1 | 70.770 | 70.770 | 70.770 | 70.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18921) vms_mb | MB | 1 | 429.160 | 429.160 | 429.160 | 429.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18933) rss_mb | MB | 1 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18933) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18934) rss_mb | MB | 1 | 128.402 | 128.402 | 128.402 | 128.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18934) vms_mb | MB | 1 | 480.086 | 480.086 | 480.086 | 480.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18964) rss_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18964) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18965) rss_mb | MB | 1 | 13.594 | 13.594 | 13.594 | 13.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18965) vms_mb | MB | 1 | 367.133 | 367.133 | 367.133 | 367.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18986) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18986) rss_mb | MB | 2 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18986) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18986) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18987) CPU | percent | 1 | 150.131 | 150.131 | 150.131 | 150.131 | 1.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18987) rss_mb | MB | 2 | 642.992 | 54.496 | 1231.488 | 1231.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18987) main thread run-queue wait | percent | 1 | 33.646 | 33.646 | 33.646 | 33.646 | 0.338409 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18987) vms_mb | MB | 2 | 1035.121 | 412.434 | 1657.809 | 1657.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19001) rss_mb | MB | 1 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19001) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19002) rss_mb | MB | 1 | 148.125 | 148.125 | 148.125 | 148.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19002) vms_mb | MB | 1 | 499.070 | 499.070 | 499.070 | 499.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19059) rss_mb | MB | 1 | 2.977 | 2.977 | 2.977 | 2.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19059) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19060) rss_mb | MB | 1 | 13.617 | 13.617 | 13.617 | 13.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19060) vms_mb | MB | 1 | 367.129 | 367.129 | 367.129 | 367.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — postok.py (PID 19086) rss_mb | MB | 1 | 55.109 | 55.109 | 55.109 | 55.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — postok.py (PID 19086) vms_mb | MB | 1 | 66.758 | 66.758 | 66.758 | 66.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 19091) rss_mb | MB | 1 | 148.414 | 148.414 | 148.414 | 148.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 19091) vms_mb | MB | 1 | 153.320 | 153.320 | 153.320 | 153.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19108) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19108) rss_mb | MB | 19 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19108) main thread run-queue wait | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19108) vms_mb | MB | 19 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19109) CPU | percent | 18 | 70.295 | 67.501 | 100.020 | 68.622 | 12.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19109) rss_mb | MB | 19 | 1166.056 | 0.000 | 1230.941 | 1230.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19109) main thread run-queue wait | percent | 18 | 0.526 | 0.048 | 8.406 | 0.048 | 0.095497 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19109) vms_mb | MB | 19 | 1500.482 | 0.387 | 1583.820 | 1583.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19123) rss_mb | MB | 1 | 3.137 | 3.137 | 3.137 | 3.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19123) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19124) rss_mb | MB | 1 | 775.930 | 775.930 | 775.930 | 775.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19124) vms_mb | MB | 1 | 1485.602 | 1485.602 | 1485.602 | 1485.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19154) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19154) rss_mb | MB | 19 | 3.082 | 3.082 | 3.082 | 3.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19154) main thread run-queue wait | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19154) vms_mb | MB | 19 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19155) CPU | percent | 18 | 68.782 | 67.528 | 78.521 | 67.629 | 12.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19155) rss_mb | MB | 19 | 1182.965 | 57.660 | 1245.496 | 1245.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19155) main thread run-queue wait | percent | 18 | 0.060 | 0.046 | 0.069 | 0.052 | 0.010866 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19155) vms_mb | MB | 19 | 1535.316 | 409.395 | 1597.867 | 1597.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19169) rss_mb | MB | 1 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 19169) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19170) rss_mb | MB | 1 | 20.516 | 20.516 | 20.516 | 20.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 19170) vms_mb | MB | 1 | 371.832 | 371.832 | 371.832 | 371.832 | n/a | n/a |
| docker commit (PID 19224) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 19224) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 19224) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 19224) rss_mb | MB | 2 | 29.785 | 29.785 | 29.785 | 29.785 | n/a | n/a |
| docker commit (PID 19224) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 19224) vms_mb | MB | 2 | 2060.539 | 2060.539 | 2060.539 | 2060.539 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 688 | 18.627 | 0.000 | 172.046 | 0.000 | 128.939806 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 688 | 1.037 | 0.000 | 32.075 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 688 | 1.070 | 0.000 | 32.855 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 688 | 0.000 | 0.000 | 0.054 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 688 | 0.000 | 0.000 | 0.054 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 688 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 688 | 1.398 | 0.000 | 187.031 | 0.000 | 971.425781 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 689 | 796.637 | 25.855 | 2379.555 | 1089.414 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 688 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 688 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 688 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000893 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 688 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 714 | 7.457 | 1.483 | 227.420 | 2.003 | 53.633092 CPU seconds | n/a |
| workload total memory | MB | 715 | 5649.944 | 4802.879 | 6528.168 | 6290.090 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
