# agprof summary

- Duration: **1500.174 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **32 calls**, 32 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1230.524 s total wait
- Tools: **90/90 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **138695** at 1.981 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1477378.501 / 1477378.501 ms |
| LLM latency p50 / p95 | 36523.800 / 76808.072 ms |
| LLM TTFT p50 / p95 | 8576.198 / 10231.472 ms |
| LLM input / output tokens | 4552496 / 125946 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 32 total, 32 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1069.027 / 7940.124 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 1/1 | 1 | 0 | 0 | 323.585 ms | 323.585 ms |
| bash | 31/31 | 31 | 0 | 0 | 431.234 ms | 26189.885 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 361.073 ms | 361.073 ms |
| generate | 12/12 | 12 | 0 | 0 | 3474.102 ms | 9379.126 ms |
| inspect | 2/2 | 2 | 0 | 0 | 1479.720 ms | 1578.566 ms |
| inspect_module_inputs | 6/6 | 6 | 0 | 0 | 1569.986 ms | 1879.684 ms |
| logit_lens | 2/2 | 2 | 0 | 0 | 912.545 ms | 1171.580 ms |
| patch | 15/15 | 15 | 0 | 0 | 412.117 ms | 425.750 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 225.797 ms | 225.797 ms |
| trace | 19/19 | 19 | 0 | 0 | 1624.991 ms | 3852.883 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 6.920% | 103.210% | 103.941 s | 13628.446 MB | 15434.551 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 14385 |  | 1491 | 4.270% | 103.074% | 64.140 s | 2862.654 MB | 3755.602 MB | 16512.389 MB | 17578.113 MB | 0.167969 MB | 5030.230469 MB |
| lsb_grid_worker | 2151 |  | 1491 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| tail | 14807 | sandbox_agent_lsb-native_0000_0000 | 1468 | 0.003% | 0.995% | 0.040 s | 1.473 MB | 1.473 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 14508 |  | 1491 | 0.000% | 0.000% | 0.000 s | 12.195 MB | 12.195 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 14768 | sandbox_agent_lsb-native_0000_0000 | 1468 | 0.003% | 0.995% | 0.040 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 14907 | sandbox_agent_lsb-native_0000_0000 | 1468 | 5.158% | 99.301% | 76.160 s | 107.943 MB | 116.414 MB | 968.645 MB | 974.023 MB | n/a MB | n/a MB |
| vllm | 14394 |  | 1491 | 0.221% | 6.944% | 3.320 s | 1804.875 MB | 1804.969 MB | 12013.803 MB | 12014.770 MB | 0.000000 MB | 0.054688 MB |
| python3 | 14913 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.761% | 99.761% | 1.010 s | 55.402 MB | 83.266 MB | 66.758 MB | 97.996 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 14509 |  | 1491 | 2.418% | 44.642% | 36.300 s | 2325.381 MB | 2325.516 MB | 21829.667 MB | 21829.777 MB | 0.000000 MB | 0.007812 MB |
| python3 | 14925 | sandbox_agent_lsb-native_0000_0000 | 1463 | 0.268% | 46.737% | 3.950 s | 75.887 MB | 81.711 MB | 88.983 MB | 94.664 MB | n/a MB | n/a MB |
| python | 15063 | sandbox_agent_lsb-native_0000_0000 | 10 | 0.773% | 1.988% | 0.070 s | 12.535 MB | 12.535 MB | 15.698 MB | 15.715 MB | n/a MB | n/a MB |
| python | 15085 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.883 MB | 6.883 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python | 15101 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.969 MB | 9.969 MB | 13.734 MB | 13.734 MB | n/a MB | n/a MB |
| python | 15102 | sandbox_agent_lsb-native_0000_0000 | 2 | 97.083% | 97.083% | 0.990 s | 44.533 MB | 82.988 MB | 51.406 MB | 91.156 MB | n/a MB | n/a MB |
| python | 15119 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.879 MB | 6.879 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python | 15134 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.426 MB | 12.426 MB | 15.621 MB | 15.621 MB | n/a MB | n/a MB |
| python | 15150 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.715 MB | 11.715 MB | 15.422 MB | 15.422 MB | n/a MB | n/a MB |
| python | 15166 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.168 MB | 11.168 MB | 15.199 MB | 15.199 MB | n/a MB | n/a MB |
| python | 15182 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.285 MB | 12.285 MB | 15.621 MB | 15.621 MB | n/a MB | n/a MB |
| python | 15223 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.566 MB | 5.566 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| python | 15217 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.663% | 1.989% | 0.020 s | 12.531 MB | 12.594 MB | 15.633 MB | 15.633 MB | n/a MB | n/a MB |
| bash | 15216 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.824 MB | 2.824 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 15239 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.777 MB | 10.777 MB | 15.074 MB | 15.074 MB | n/a MB | n/a MB |
| python | 15259 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.133 MB | 7.133 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python | 15275 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.809 MB | 9.809 MB | 13.688 MB | 13.688 MB | n/a MB | n/a MB |
| python | 15291 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.141 MB | 9.141 MB | 13.152 MB | 13.152 MB | n/a MB | n/a MB |
| python | 15350 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.497% | 0.994% | 0.010 s | 12.527 MB | 12.527 MB | 15.688 MB | 15.715 MB | n/a MB | n/a MB |
| python | 15357 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.469 MB | 7.469 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| tail | 15351 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.574 MB | 1.574 MB | 2.840 MB | 2.840 MB | n/a MB | n/a MB |
| bash | 15341 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.922 MB | 2.922 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 15373 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.730 MB | 9.730 MB | 13.688 MB | 13.688 MB | n/a MB | n/a MB |
| python | 15389 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.793 MB | 11.793 MB | 15.355 MB | 15.355 MB | n/a MB | n/a MB |
| python | 15523 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.367 MB | 13.367 MB | 367.059 MB | 367.059 MB | n/a MB | n/a MB |
| bash | 15522 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.023 MB | 3.023 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 15554 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.074 MB | 3.074 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 15555 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.793 MB | 20.793 MB | 372.285 MB | 372.285 MB | n/a MB | n/a MB |
| python | 15600 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.945 MB | 21.945 MB | 133.719 MB | 133.719 MB | n/a MB | n/a MB |
| python | 15669 | sandbox_agent_lsb-native_0000_0000 | 43 | 193.181% | 204.811% | 81.630 s | 287.257 MB | 356.914 MB | 722.334 MB | 799.023 MB | n/a MB | n/a MB |
| python | 15691 | sandbox_agent_lsb-native_0000_0000 | 2 | 173.957% | 173.957% | 1.750 s | 53.066 MB | 83.477 MB | 419.543 MB | 465.234 MB | n/a MB | n/a MB |
| bash | 15690 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.949 MB | 2.949 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 15708 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.449 MB | 13.449 MB | 367.191 MB | 367.191 MB | n/a MB | n/a MB |
| bash | 15707 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.059 MB | 3.059 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 15723 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.113 MB | 3.113 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 15724 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.258 MB | 22.258 MB | 373.969 MB | 373.969 MB | n/a MB | n/a MB |
| bash | 15738 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 15739 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 47.762 MB | 47.762 MB | 405.074 MB | 405.074 MB | n/a MB | n/a MB |
| python | 15771 | sandbox_agent_lsb-native_0000_0000 | 47 | 192.102% | 204.543% | 88.910 s | 339.252 MB | 401.281 MB | 776.390 MB | 899.129 MB | n/a MB | n/a MB |
| bash | 15805 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.961 MB | 2.961 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 15806 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 64.047 MB | 64.047 MB | 446.051 MB | 446.051 MB | n/a MB | n/a MB |
| python | 15828 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 116.566 MB | 116.566 MB | 553.355 MB | 553.355 MB | n/a MB | n/a MB |
| python | 15850 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 24.258 MB | 24.258 MB | 95.844 MB | 95.844 MB | n/a MB | n/a MB |
| bash | 15849 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 15868 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.695 MB | 5.695 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| python | 15851 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.597% | 0.994% | 0.030 s | 12.625 MB | 12.625 MB | 15.688 MB | 15.715 MB | n/a MB | n/a MB |
| grep | 15852 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.750 MB | 1.750 MB | 3.629 MB | 3.629 MB | n/a MB | n/a MB |
| python | 15884 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.852 MB | 10.852 MB | 15.199 MB | 15.199 MB | n/a MB | n/a MB |
| python | 15889 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 63.121 MB | 63.121 MB | 68.676 MB | 68.676 MB | n/a MB | n/a MB |
| python | 15890 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 62.621 MB | 62.621 MB | 68.676 MB | 68.676 MB | n/a MB | n/a MB |
| python | 15902 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.129 MB | 9.129 MB | 13.559 MB | 13.559 MB | n/a MB | n/a MB |
| python | 15918 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.652 MB | 10.652 MB | 14.945 MB | 14.945 MB | n/a MB | n/a MB |
| docker | 15980 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.148 MB | 30.148 MB | 2059.531 MB | 2059.531 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 4.117% | 100.000% | 12093.944 MB | 12740.000 MB | 30.875 W | 73.551 W | 46284.640 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 19.300% | 210.636% | 284.946 s | 169.008 MB | 531.633 MB | 0.000000 MB | 9.628906 MB | 0.000959 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 14640 | 1500.107 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1477.379 | n/a | n/a | 0.000 | 1477378.501 | 1477378.501 | 1477378.501 |
| engine:execute | 1/1 | 0 | 0 | 1477.377 | 2.034 | 1475.343 | 0.000 | 1477376.785 | 1477376.785 | 1477376.785 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1471.434 | 0.005 | 1471.429 | 0.000 | 1471434.070 | 1471434.070 | 1471434.070 |
| turn | 32/32 | 0 | 0 | 1468.008 | n/a | n/a | 0.000 | 45875.241 | 45266.579 | 83679.741 |
| llm:attempt | 32/32 | 0 | 0 | 1230.524 | 4.715 | 1225.808 | 0.000 | 38453.871 | 36523.800 | 76808.072 |
| tool:bash | 31/31 | 0 | 0 | 126.016 | n/a | n/a | 0.000 | 4065.022 | 431.234 | 26189.885 |
| process:bash | 31/31 | 1 | 0 | 125.742 | n/a | n/a | 0.000 | 4056.184 | 423.799 | 26179.715 |
| tool:generate | 12/12 | 0 | 0 | 50.306 | n/a | n/a | 0.000 | 4192.130 | 3474.102 | 9379.126 |
| tool:trace | 19/19 | 0 | 0 | 35.639 | n/a | n/a | 0.000 | 1875.747 | 1624.991 | 3852.883 |
| tool:inspect_module_inputs | 6/6 | 0 | 0 | 9.151 | n/a | n/a | 0.000 | 1525.113 | 1569.986 | 1879.684 |
| tool:patch | 15/15 | 0 | 0 | 6.205 | n/a | n/a | 0.000 | 413.694 | 412.117 | 425.750 |
| syscall:sendto | 1993/1993 | 0 | 0 | 3.989 | n/a | n/a | 0.000 | 2.002 | 1.778 | 3.685 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.140 | 0.728 | 2.412 | 0.000 | 3140.040 | 3140.040 | 3140.040 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.140 | 0.728 | 2.412 | 0.000 | 3139.783 | 3139.783 | 3139.783 |
| tool:inspect | 2/2 | 0 | 0 | 2.959 | n/a | n/a | 0.000 | 1479.720 | 1479.720 | 1578.566 |
| run:container_call | 13/13 | 0 | 0 | 2.519 | 0.002 | 2.517 | 0.000 | 193.788 | 33.030 | 864.358 |
| teardown:commit | 1/1 | 0 | 0 | 2.126 | 0.004 | 2.122 | 0.000 | 2125.776 | 2125.776 | 2125.776 |
| sandbox:commit | 1/1 | 0 | 0 | 1.940 | 0.002 | 1.937 | 0.000 | 1939.589 | 1939.589 | 1939.589 |
| checkpoint.total | 1/1 | 0 | 0 | 1.939 | 0.002 | 1.937 | 0.000 | 1939.443 | 1939.443 | 1939.443 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.939 | 0.002 | 1.937 | 0.000 | 1939.290 | 1939.290 | 1939.290 |
| tool:logit_lens | 2/2 | 0 | 0 | 1.825 | n/a | n/a | 0.000 | 912.545 | 912.545 | 1171.580 |
| syscall:connect | 528/528 | 0 | 0 | 1.049 | n/a | n/a | 0.000 | 1.987 | 1.737 | 3.892 |
| syscall:execve | 448/448 | 0 | 0 | 0.570 | n/a | n/a | 0.000 | 1.273 | 1.162 | 1.911 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.361 | n/a | n/a | 0.000 | 361.073 | 361.073 | 361.073 |
| sandbox:create | 1/1 | 0 | 0 | 0.355 | 0.269 | 0.086 | 0.000 | 354.831 | 354.831 | 354.831 |
| sandbox:start | 1/1 | 0 | 0 | 0.330 | 0.002 | 0.327 | 0.000 | 329.940 | 329.940 | 329.940 |
| runtime.container_create | 1/1 | 0 | 0 | 0.330 | 0.002 | 0.327 | 0.000 | 329.756 | 329.756 | 329.756 |
| tool:attention | 1/1 | 0 | 0 | 0.324 | n/a | n/a | 0.000 | 323.585 | 323.585 | 323.585 |
| tool:submit_output | 1/1 | 0 | 0 | 0.226 | n/a | n/a | 0.000 | 225.797 | 225.797 | 225.797 |
| sandbox:stop | 1/1 | 0 | 0 | 0.186 | 0.002 | 0.184 | 0.000 | 185.896 | 185.896 | 185.896 |
| agency:services_close | 1/1 | 0 | 0 | 0.146 | 0.000 | 0.145 | 0.000 | 145.713 | 145.713 | 145.713 |
| agency:services_start | 1/1 | 0 | 0 | 0.072 | 0.041 | 0.031 | 0.000 | 72.312 | 72.312 | 72.312 |
| agent:create | 1/1 | 0 | 0 | 0.051 | 0.008 | 0.043 | 0.000 | 50.881 | 50.881 | 50.881 |
| run:detect | 1/1 | 0 | 0 | 0.050 | 0.001 | 0.049 | 0.000 | 49.703 | 49.703 | 49.703 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.000 | 3.464 | 3.464 | 3.464 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.239 | 1.239 | 1.239 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.074 | 0.069 | 0.105 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.185 | 0.185 | 0.185 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.072 | 0.072 | 0.072 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1490 | 0.294 | 0.039 | 162.985 | 0.071 | 4.398674 CPU seconds | n/a |
| GPU 0 memory | MB | 1491 | 12093.944 | 11670.000 | 12740.000 | 12100.000 | n/a | n/a |
| GPU 0 power | W | 1491 | 30.875 | 28.068 | 73.551 | 28.915 | n/a | 46284.640 J |
| GPU 0 proc / 14385-560926 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 memory | MB | 1491 | 3246.987 | 3118.000 | 3882.000 | 3242.000 | n/a | n/a |
| GPU 0 proc / 14385-560926 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 estimated power | W | 1173 | 1.883 | 0.000 | 59.991 | 0.000 | n/a | n/a |
| GPU 0 proc / 14385-560926 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 utilization | percent | 1173 | 1.388 | 0.000 | 82.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 14509-562693 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 memory | MB | 1491 | 8364.954 | 8070.000 | 8376.000 | 8376.000 | n/a | n/a |
| GPU 0 proc / 14509-562693 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 estimated power | W | 306 | 11.076 | 0.000 | 72.683 | 0.000 | n/a | n/a |
| GPU 0 proc / 14509-562693 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 utilization | percent | 306 | 14.585 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1491 | 11611.941 | 11188.000 | 12258.000 | 11618.000 | n/a | n/a |
| GPU 0 utilization | percent | 1491 | 4.117 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1491 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1490 | 2.831 | 0.043 | 58.609 | 0.193 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1490 | 3.173 | 0.000 | 26.683 | 0.249 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1490 | 0.000 | 0.000 | 0.210 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1490 | 3.379 | 0.000 | 211.573 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1490 | 0.758 | 0.000 | 95.045 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1490 | 0.760 | 0.000 | 95.121 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1491 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1491 | 7176.318 | 6381.504 | 8195.406 | 7268.930 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1490 | 0.004 | 0.000 | 0.253 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1490 | 0.021 | 0.000 | 1.761 | 0.000 | n/a | n/a |
| Agency harness — python -m lsbench (PID 14385) CPU | percent | 1490 | 4.270 | 0.000 | 103.074 | 0.000 | 64.140000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 14385) io read MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.097 | 0.000 | 0.167969 MB | n/a |
| Agency harness — python -m lsbench (PID 14385) io write MB/s | MB/s | 1490 | 3.345 | 0.015 | 352.156 | 0.023 | 5030.230469 MB | n/a |
| Agency harness — python -m lsbench (PID 14385) rss_mb | MB | 1491 | 2862.654 | 2037.367 | 3755.602 | 3136.996 | n/a | n/a |
| Agency harness — python -m lsbench (PID 14385) main thread run-queue wait | percent | 1490 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000013 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 14385) vms_mb | MB | 1491 | 16512.389 | 14147.898 | 17578.113 | 16755.223 | n/a | n/a |
| Python — vllm (PID 14394) CPU | percent | 1490 | 0.221 | 0.000 | 6.944 | 0.000 | 3.320000 CPU seconds | n/a |
| Python — vllm (PID 14394) io read MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 14394) io write MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.008 | 0.000 | 0.054688 MB | n/a |
| Python — vllm (PID 14394) rss_mb | MB | 1491 | 1804.875 | 1803.219 | 1804.969 | 1804.969 | n/a | n/a |
| Python — vllm (PID 14394) main thread run-queue wait | percent | 1490 | 0.000 | 0.000 | 0.160 | 0.000 | 0.004990 run-queue seconds | n/a |
| Python — vllm (PID 14394) vms_mb | MB | 1491 | 12013.803 | 11942.750 | 12014.770 | 12014.770 | n/a | n/a |
| Python — python -c (PID 14508) CPU | percent | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 14508) io read MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 14508) io write MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 14508) rss_mb | MB | 1491 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| Python — python -c (PID 14508) main thread run-queue wait | percent | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 14508) vms_mb | MB | 1491 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 14509) CPU | percent | 1490 | 2.418 | 0.000 | 44.642 | 0.996 | 36.300000 CPU seconds | n/a |
| VLLM::EngineCore (PID 14509) io read MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 14509) io write MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 14509) rss_mb | MB | 1491 | 2325.381 | 2324.887 | 2325.516 | 2325.516 | n/a | n/a |
| VLLM::EngineCore (PID 14509) main thread run-queue wait | percent | 1490 | 0.000 | 0.000 | 0.026 | 0.000 | 0.003208 run-queue seconds | n/a |
| VLLM::EngineCore (PID 14509) vms_mb | MB | 1491 | 21829.667 | 21828.762 | 21829.777 | 21829.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 14768) CPU | percent | 1467 | 0.003 | 0.000 | 0.995 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 14768) rss_mb | MB | 1468 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 14768) main thread run-queue wait | percent | 1467 | 0.007 | 0.000 | 5.995 | 0.000 | 0.099153 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 14768) vms_mb | MB | 1468 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 14807) CPU | percent | 1467 | 0.003 | 0.000 | 0.995 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 14807) rss_mb | MB | 1468 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 14807) main thread run-queue wait | percent | 1467 | 0.002 | 0.000 | 2.854 | 0.000 | 0.028990 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 14807) vms_mb | MB | 1468 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 14907) CPU | percent | 1467 | 5.158 | 0.000 | 99.301 | 0.000 | 76.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 14907) rss_mb | MB | 1468 | 107.943 | 3.148 | 116.414 | 108.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 14907) main thread run-queue wait | percent | 1467 | 0.000 | 0.000 | 0.014 | 0.000 | 0.000162 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 14907) vms_mb | MB | 1468 | 968.645 | 4.258 | 974.023 | 973.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 14913) CPU | percent | 1 | 99.761 | 99.761 | 99.761 | 99.761 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 14913) rss_mb | MB | 2 | 55.402 | 27.539 | 83.266 | 83.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 14913) main thread run-queue wait | percent | 1 | 0.007 | 0.007 | 0.007 | 0.007 | 0.000069 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 14913) vms_mb | MB | 2 | 66.758 | 35.520 | 97.996 | 97.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 14925) CPU | percent | 1462 | 0.268 | 0.000 | 46.737 | 0.995 | 3.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 14925) rss_mb | MB | 1463 | 75.887 | 30.430 | 81.711 | 80.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 14925) main thread run-queue wait | percent | 1462 | 0.004 | 0.000 | 2.265 | 0.000 | 0.062101 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 14925) vms_mb | MB | 1463 | 88.983 | 35.730 | 94.664 | 93.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15063) CPU | percent | 9 | 0.773 | 0.000 | 1.988 | 1.988 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15063) rss_mb | MB | 10 | 12.535 | 12.535 | 12.535 | 12.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15063) main thread run-queue wait | percent | 9 | 0.002 | 0.000 | 0.004 | 0.004 | 0.000209 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15063) vms_mb | MB | 10 | 15.698 | 15.633 | 15.715 | 15.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15085) rss_mb | MB | 1 | 6.883 | 6.883 | 6.883 | 6.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15085) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15101) rss_mb | MB | 1 | 9.969 | 9.969 | 9.969 | 9.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15101) vms_mb | MB | 1 | 13.734 | 13.734 | 13.734 | 13.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15102) CPU | percent | 1 | 97.083 | 97.083 | 97.083 | 97.083 | 0.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15102) rss_mb | MB | 2 | 44.533 | 6.078 | 82.988 | 82.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15102) main thread run-queue wait | percent | 1 | 0.007 | 0.007 | 0.007 | 0.007 | 0.000070 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15102) vms_mb | MB | 2 | 51.406 | 11.656 | 91.156 | 91.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15119) rss_mb | MB | 1 | 6.879 | 6.879 | 6.879 | 6.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15119) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15134) rss_mb | MB | 1 | 12.426 | 12.426 | 12.426 | 12.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15134) vms_mb | MB | 1 | 15.621 | 15.621 | 15.621 | 15.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15150) rss_mb | MB | 1 | 11.715 | 11.715 | 11.715 | 11.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15150) vms_mb | MB | 1 | 15.422 | 15.422 | 15.422 | 15.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15166) rss_mb | MB | 1 | 11.168 | 11.168 | 11.168 | 11.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15166) vms_mb | MB | 1 | 15.199 | 15.199 | 15.199 | 15.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15182) rss_mb | MB | 1 | 12.285 | 12.285 | 12.285 | 12.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15182) vms_mb | MB | 1 | 15.621 | 15.621 | 15.621 | 15.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15216) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15216) rss_mb | MB | 5 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15216) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15216) vms_mb | MB | 5 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15217) CPU | percent | 3 | 0.663 | 0.000 | 1.989 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15217) rss_mb | MB | 4 | 12.531 | 12.469 | 12.594 | 12.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15217) main thread run-queue wait | percent | 3 | 0.005 | 0.002 | 0.007 | 0.005 | 0.000153 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15217) vms_mb | MB | 4 | 15.633 | 15.633 | 15.633 | 15.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15223) rss_mb | MB | 1 | 5.566 | 5.566 | 5.566 | 5.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15223) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15239) rss_mb | MB | 1 | 10.777 | 10.777 | 10.777 | 10.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15239) vms_mb | MB | 1 | 15.074 | 15.074 | 15.074 | 15.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15259) rss_mb | MB | 1 | 7.133 | 7.133 | 7.133 | 7.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15259) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15275) rss_mb | MB | 1 | 9.809 | 9.809 | 9.809 | 9.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15275) vms_mb | MB | 1 | 13.688 | 13.688 | 13.688 | 13.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15291) rss_mb | MB | 1 | 9.141 | 9.141 | 9.141 | 9.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15291) vms_mb | MB | 1 | 13.152 | 13.152 | 13.152 | 13.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15341) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15341) rss_mb | MB | 3 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15341) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15341) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15350) CPU | percent | 2 | 0.497 | 0.000 | 0.994 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15350) rss_mb | MB | 3 | 12.527 | 12.527 | 12.527 | 12.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15350) main thread run-queue wait | percent | 2 | 0.003 | 0.003 | 0.003 | 0.003 | 0.000059 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15350) vms_mb | MB | 3 | 15.688 | 15.633 | 15.715 | 15.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 15351) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 15351) rss_mb | MB | 3 | 1.574 | 1.574 | 1.574 | 1.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 15351) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 15351) vms_mb | MB | 3 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15357) rss_mb | MB | 1 | 7.469 | 7.469 | 7.469 | 7.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15357) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15373) rss_mb | MB | 1 | 9.730 | 9.730 | 9.730 | 9.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15373) vms_mb | MB | 1 | 13.688 | 13.688 | 13.688 | 13.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15389) rss_mb | MB | 1 | 11.793 | 11.793 | 11.793 | 11.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15389) vms_mb | MB | 1 | 15.355 | 15.355 | 15.355 | 15.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15522) rss_mb | MB | 1 | 3.023 | 3.023 | 3.023 | 3.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15522) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15523) rss_mb | MB | 1 | 13.367 | 13.367 | 13.367 | 13.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15523) vms_mb | MB | 1 | 367.059 | 367.059 | 367.059 | 367.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15554) rss_mb | MB | 1 | 3.074 | 3.074 | 3.074 | 3.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15554) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15555) rss_mb | MB | 1 | 20.793 | 20.793 | 20.793 | 20.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15555) vms_mb | MB | 1 | 372.285 | 372.285 | 372.285 | 372.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — compare.py (PID 15600) rss_mb | MB | 1 | 21.945 | 21.945 | 21.945 | 21.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — compare.py (PID 15600) vms_mb | MB | 1 | 133.719 | 133.719 | 133.719 | 133.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — keys.py (PID 15669) CPU | percent | 42 | 193.181 | 159.023 | 204.811 | 204.739 | 81.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — keys.py (PID 15669) rss_mb | MB | 43 | 287.257 | 41.320 | 356.914 | 117.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — keys.py (PID 15669) main thread run-queue wait | percent | 42 | 43.833 | 31.850 | 52.419 | 45.269 | 18.522589 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — keys.py (PID 15669) vms_mb | MB | 43 | 722.334 | 424.090 | 799.023 | 545.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15690) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15690) rss_mb | MB | 2 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15690) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15690) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15691) CPU | percent | 1 | 173.957 | 173.957 | 173.957 | 173.957 | 1.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15691) rss_mb | MB | 2 | 53.066 | 22.656 | 83.477 | 83.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15691) main thread run-queue wait | percent | 1 | 58.869 | 58.869 | 58.869 | 58.869 | 0.592218 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15691) vms_mb | MB | 2 | 419.543 | 373.852 | 465.234 | 465.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15707) rss_mb | MB | 1 | 3.059 | 3.059 | 3.059 | 3.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15707) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15708) rss_mb | MB | 1 | 13.449 | 13.449 | 13.449 | 13.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15708) vms_mb | MB | 1 | 367.191 | 367.191 | 367.191 | 367.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15723) rss_mb | MB | 1 | 3.113 | 3.113 | 3.113 | 3.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15723) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15724) rss_mb | MB | 1 | 22.258 | 22.258 | 22.258 | 22.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15724) vms_mb | MB | 1 | 373.969 | 373.969 | 373.969 | 373.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15738) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15738) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15739) rss_mb | MB | 1 | 47.762 | 47.762 | 47.762 | 47.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15739) vms_mb | MB | 1 | 405.074 | 405.074 | 405.074 | 405.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — finalkeys.py (PID 15771) CPU | percent | 46 | 192.102 | 149.195 | 204.543 | 199.827 | 88.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — finalkeys.py (PID 15771) rss_mb | MB | 47 | 339.252 | 128.875 | 401.281 | 392.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — finalkeys.py (PID 15771) main thread run-queue wait | percent | 46 | 44.554 | 29.407 | 51.734 | 44.574 | 20.620613 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — finalkeys.py (PID 15771) vms_mb | MB | 47 | 776.390 | 548.691 | 899.129 | 820.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15805) rss_mb | MB | 1 | 2.961 | 2.961 | 2.961 | 2.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15805) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15806) rss_mb | MB | 1 | 64.047 | 64.047 | 64.047 | 64.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 15806) vms_mb | MB | 1 | 446.051 | 446.051 | 446.051 | 446.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble.py (PID 15828) rss_mb | MB | 1 | 116.566 | 116.566 | 116.566 | 116.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — assemble.py (PID 15828) vms_mb | MB | 1 | 553.355 | 553.355 | 553.355 | 553.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15849) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15849) rss_mb | MB | 7 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15849) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 15849) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evalcheck.py (PID 15850) rss_mb | MB | 1 | 24.258 | 24.258 | 24.258 | 24.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evalcheck.py (PID 15850) vms_mb | MB | 1 | 95.844 | 95.844 | 95.844 | 95.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15851) CPU | percent | 5 | 0.597 | 0.000 | 0.994 | 0.994 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15851) rss_mb | MB | 6 | 12.625 | 12.625 | 12.625 | 12.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15851) main thread run-queue wait | percent | 5 | 0.002 | 0.001 | 0.006 | 0.002 | 0.000124 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15851) vms_mb | MB | 6 | 15.688 | 15.633 | 15.715 | 15.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 15852) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 15852) rss_mb | MB | 6 | 1.750 | 1.750 | 1.750 | 1.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 15852) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 15852) vms_mb | MB | 6 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15868) rss_mb | MB | 1 | 5.695 | 5.695 | 5.695 | 5.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15868) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15884) rss_mb | MB | 1 | 10.852 | 10.852 | 10.852 | 10.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15884) vms_mb | MB | 1 | 15.199 | 15.199 | 15.199 | 15.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15889) rss_mb | MB | 1 | 63.121 | 63.121 | 63.121 | 63.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15889) vms_mb | MB | 1 | 68.676 | 68.676 | 68.676 | 68.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15890) rss_mb | MB | 1 | 62.621 | 62.621 | 62.621 | 62.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15890) vms_mb | MB | 1 | 68.676 | 68.676 | 68.676 | 68.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15902) rss_mb | MB | 1 | 9.129 | 9.129 | 9.129 | 9.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15902) vms_mb | MB | 1 | 13.559 | 13.559 | 13.559 | 13.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15918) rss_mb | MB | 1 | 10.652 | 10.652 | 10.652 | 10.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaldev.py (PID 15918) vms_mb | MB | 1 | 14.945 | 14.945 | 14.945 | 14.945 | n/a | n/a |
| docker commit (PID 15980) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 15980) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 15980) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 15980) rss_mb | MB | 2 | 30.148 | 30.148 | 30.148 | 30.148 | n/a | n/a |
| docker commit (PID 15980) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 15980) vms_mb | MB | 2 | 2059.531 | 2059.531 | 2059.531 | 2059.531 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2151) CPU | percent | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2151) io read MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2151) io write MB/s | MB/s | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2151) rss_mb | MB | 1491 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2151) main thread run-queue wait | percent | 1490 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2151) vms_mb | MB | 1491 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 1467 | 19.300 | 0.000 | 210.636 | 0.000 | 284.945920 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1467 | 2.997 | 0.000 | 55.729 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1467 | 3.006 | 0.000 | 58.315 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 1467 | 0.000 | 0.000 | 0.045 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 1467 | 0.000 | 0.000 | 0.045 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 1467 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 1467 | 0.007 | 0.000 | 0.812 | 0.000 | 9.628906 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 1468 | 169.008 | 18.336 | 531.633 | 101.566 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1467 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1467 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 1467 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000959 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 1467 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 1490 | 6.920 | 1.510 | 103.210 | 1.948 | 103.941398 CPU seconds | n/a |
| workload total memory | MB | 1491 | 13628.446 | 11548.496 | 15434.551 | 15186.984 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
