# agprof summary

- Duration: **925.312 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **87 calls**, 85 succeeded, 0 failed, 0 interrupted, n/a reported retries, 632.375 s total wait
- Tools: **86/86 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **85970** at 1.974 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 925244.566 / 925244.566 ms |
| LLM latency p50 / p95 | 5179.362 / 19722.548 ms |
| LLM TTFT p50 / p95 | 2469.733 / 6405.541 ms |
| LLM input / output tokens | 6910262 / 84705 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 87 total, 85 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 346.033 / 16466.098 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 1/1 | 1 | 0 | 0 | 1862.769 ms | 1862.769 ms |
| attribution | 2/2 | 2 | 0 | 0 | 371.857 ms | 395.720 ms |
| bash | 64/64 | 64 | 0 | 0 | 327.553 ms | 1415.345 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 362.584 ms | 362.584 ms |
| generate | 4/4 | 4 | 0 | 0 | 41435.845 ms | 84497.372 ms |
| logit_lens | 4/4 | 4 | 0 | 0 | 736.067 ms | 1472.881 ms |
| patch | 1/1 | 1 | 0 | 0 | 1077.405 ms | 1077.405 ms |
| read | 1/1 | 1 | 0 | 0 | 0.537 ms | 0.537 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 238.347 ms | 238.347 ms |
| trace | 7/7 | 7 | 0 | 0 | 485.704 ms | 691.575 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 12.048% | 101.670% | 111.560 s | 9107.828 MB | 9696.488 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VLLM::EngineCor | 17358 |  | 919 | 7.902% | 41.728% | 73.170 s | 2337.462 MB | 2337.586 MB | 21237.618 MB | 21237.730 MB | 0.000000 MB | 0.003906 MB |
| vllm | 17307 |  | 919 | 0.677% | 4.960% | 6.270 s | 1805.403 MB | 1805.582 MB | 11043.810 MB | 11045.719 MB | 0.000000 MB | 0.035156 MB |
| lsb_grid_worker | 4633 |  | 919 | 0.000% | 0.000% | 0.000 s | 3.422 MB | 3.422 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 17357 |  | 919 | 0.000% | 0.000% | 0.000 s | 12.180 MB | 12.180 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker | 17538 |  | 1 | n/a% | n/a% | n/a s | 30.570 MB | 30.570 MB | 1843.762 MB | 1843.762 MB | n/a MB | n/a MB |
| python | 17241 |  | 919 | 3.449% | 100.964% | 31.940 s | 2999.923 MB | 3609.297 MB | 15677.496 MB | 19186.176 MB | 1.195312 MB | 211.707031 MB |
| docker-init | 17582 | sandbox_agent_lsb-native_0000_0000 | 918 | 0.002% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 17607 | sandbox_agent_lsb-native_0000_0000 | 918 | 0.001% | 0.995% | 0.010 s | 1.316 MB | 1.316 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 17708 | sandbox_agent_lsb-native_0000_0000 | 918 | 4.575% | 94.527% | 42.210 s | 105.736 MB | 111.516 MB | 965.481 MB | 973.730 MB | n/a MB | n/a MB |
| python3 | 17714 | sandbox_agent_lsb-native_0000_0000 | 2 | 59.295% | 59.295% | 0.600 s | 50.832 MB | 63.453 MB | 58.467 MB | 71.805 MB | n/a MB | n/a MB |
| python3 | 17726 | sandbox_agent_lsb-native_0000_0000 | 895 | 0.254% | 34.812% | 2.280 s | 72.595 MB | 74.516 MB | 86.132 MB | 88.156 MB | n/a MB | n/a MB |
| python3 | 17762 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.316 MB | 9.316 MB | 13.277 MB | 13.277 MB | n/a MB | n/a MB |
| bash | 17788 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.992 MB | 2.992 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 17789 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.457 MB | 7.457 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| pip | 18144 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 34.836 MB | 34.836 MB | 41.543 MB | 41.543 MB | n/a MB | n/a MB |
| grep | 18145 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.887 MB | 1.887 MB | 3.770 MB | 3.770 MB | n/a MB | n/a MB |
| bash | 18139 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.852 MB | 2.852 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18150 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 97.988 MB | 97.988 MB | 102.234 MB | 102.234 MB | n/a MB | n/a MB |
| bash | 18149 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.840 MB | 2.840 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 18160 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.699 MB | 2.699 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18161 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.031 MB | 8.031 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 18236 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 72.906 MB | 72.906 MB | 86.355 MB | 86.355 MB | n/a MB | n/a MB |
| python3 | 18270 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.500 MB | 19.500 MB | 212.273 MB | 212.273 MB | n/a MB | n/a MB |
| bash | 18269 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.961 MB | 2.961 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 18286 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.832 MB | 2.832 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18287 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.961 MB | 22.961 MB | 215.469 MB | 215.469 MB | n/a MB | n/a MB |
| bash | 18304 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.777 MB | 2.777 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18305 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.863 MB | 9.863 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| python3 | 18312 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1237.176 MB | 1237.176 MB | 1670.922 MB | 1670.922 MB | n/a MB | n/a MB |
| python3 | 18354 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 511.766 MB | 511.766 MB | 1672.656 MB | 1672.656 MB | n/a MB | n/a MB |
| bash | 18353 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.879 MB | 2.879 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 18376 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.855 MB | 2.855 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18377 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1383.512 MB | 1383.512 MB | 1672.633 MB | 1672.633 MB | n/a MB | n/a MB |
| bash | 18399 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.059 MB | 3.059 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18400 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1409.793 MB | 1409.793 MB | 1672.812 MB | 1672.812 MB | n/a MB | n/a MB |
| python3 | 18416 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 25.262 MB | 25.262 MB | 217.383 MB | 217.383 MB | n/a MB | n/a MB |
| bash | 18415 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.707 MB | 2.707 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 18462 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.750 MB | 2.750 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18464 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 382.000 MB | 382.000 MB | 702.648 MB | 702.648 MB | n/a MB | n/a MB |
| bash | 18481 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.855 MB | 2.855 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18482 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1942.840 MB | 1942.840 MB | 2650.648 MB | 2650.648 MB | n/a MB | n/a MB |
| bash | 18492 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.930 MB | 2.930 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18493 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1653.730 MB | 1653.730 MB | 2642.801 MB | 2642.801 MB | n/a MB | n/a MB |
| bash | 18500 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.867 MB | 2.867 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18501 | sandbox_agent_lsb-native_0000_0000 | 7 | 198.068% | 200.172% | 11.960 s | 120.974 MB | 137.094 MB | 337.188 MB | 353.043 MB | n/a MB | n/a MB |
| bash | 18524 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.895 MB | 2.895 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18525 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 802.020 MB | 802.020 MB | 1672.758 MB | 1672.758 MB | n/a MB | n/a MB |
| bash | 18557 | sandbox_agent_lsb-native_0000_0000 | 20 | 0.000% | 0.000% | 0.000 s | 2.719 MB | 2.719 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18558 | sandbox_agent_lsb-native_0000_0000 | 20 | 197.871% | 202.562% | 37.890 s | 123.028 MB | 152.289 MB | 339.333 MB | 369.926 MB | n/a MB | n/a MB |
| bash | 18579 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.906 MB | 2.906 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18580 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.281 MB | 13.281 MB | 207.109 MB | 207.109 MB | n/a MB | n/a MB |
| bash | 18592 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.887 MB | 2.887 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18593 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.262 MB | 7.262 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| bash | 18600 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.844 MB | 2.844 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18601 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 264.219 MB | 264.219 MB | 702.812 MB | 702.812 MB | n/a MB | n/a MB |
| python3 | 18626 | sandbox_agent_lsb-native_0000_0000 | 20 | 199.629% | 207.219% | 38.200 s | 1100.669 MB | 1123.215 MB | 1318.262 MB | 1339.734 MB | n/a MB | n/a MB |
| bash | 18625 | sandbox_agent_lsb-native_0000_0000 | 20 | 0.000% | 0.000% | 0.000 s | 2.832 MB | 2.832 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python3 | 18645 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.266 MB | 23.266 MB | 215.508 MB | 215.508 MB | n/a MB | n/a MB |
| bash | 18644 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.965 MB | 2.965 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| docker | 18688 |  | 18 | 0.000% | 0.000% | 0.000 s | 30.562 MB | 30.562 MB | 1843.512 MB | 1843.512 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 19.768% | 100.000% | 11816.651 MB | 14512.000 MB | 37.342 W | 72.557 W | 34532.390 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 17.091% | 207.771% | 157.808 s | 227.969 MB | 2154.746 MB | 43.281250 MB | 2.320312 MB | 0.000706 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 17469 | 925.249 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 925.245 | n/a | n/a | 43.281 | 925244.566 | 925244.566 | 925244.566 |
| sync:result_wait | 1/1 | 0 | 0 | 925.244 | 0.000 | 925.244 | 43.281 | 925243.798 | 925243.798 | 925243.798 |
| engine:execute | 1/1 | 0 | 0 | 925.243 | 1.959 | 923.279 | 43.281 | 925243.118 | 925243.118 | 925243.118 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 902.280 | 0.002 | 902.279 | 23.726 | 902280.260 | 902280.260 | 902280.260 |
| turn | 87/87 | 0 | 0 | 898.922 | n/a | n/a | 21.716 | 10332.437 | 5884.472 | 29522.286 |
| llm:attempt | 87/87 | 0 | 0 | 632.375 | 9.097 | 623.275 | 12.530 | 7268.682 | 5179.362 | 19722.548 |
| tool:generate | 4/4 | 0 | 0 | 179.494 | n/a | n/a | 0.000 | 44873.446 | 41435.845 | 84497.372 |
| tool:bash | 64/64 | 0 | 0 | 68.278 | n/a | n/a | 8.369 | 1066.851 | 327.553 | 1415.345 |
| process:bash | 64/64 | 10 | 0 | 67.711 | n/a | n/a | 8.322 | 1057.979 | 318.672 | 1406.957 |
| run:container_call | 13/13 | 0 | 0 | 18.052 | 0.002 | 18.049 | 0.011 | 1388.614 | 37.470 | 7066.995 |
| teardown:commit | 1/1 | 0 | 0 | 17.600 | 0.004 | 17.596 | 0.011 | 17600.279 | 17600.279 | 17600.279 |
| sandbox:commit | 1/1 | 0 | 0 | 17.400 | 0.002 | 17.398 | 0.011 | 17399.796 | 17399.796 | 17399.796 |
| checkpoint.total | 1/1 | 0 | 0 | 17.400 | 0.002 | 17.398 | 0.011 | 17399.661 | 17399.661 | 17399.661 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 17.400 | 0.002 | 17.398 | 0.011 | 17399.523 | 17399.523 | 17399.523 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.304 | 1.026 | 3.277 | 19.477 | 4303.970 | 4303.970 | 4303.970 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.304 | 1.026 | 3.277 | 19.477 | 4303.649 | 4303.649 | 4303.649 |
| syscall:sendto | 1591/1591 | 0 | 0 | 3.831 | n/a | n/a | 0.375 | 2.408 | 2.121 | 4.681 |
| tool:logit_lens | 4/4 | 0 | 0 | 3.438 | n/a | n/a | 0.000 | 859.514 | 736.067 | 1472.881 |
| tool:trace | 7/7 | 0 | 0 | 3.095 | n/a | n/a | 0.040 | 442.194 | 485.704 | 691.575 |
| tool:attention | 1/1 | 0 | 0 | 1.863 | n/a | n/a | 0.000 | 1862.769 | 1862.769 | 1862.769 |
| tool:patch | 1/1 | 0 | 0 | 1.077 | n/a | n/a | 0.000 | 1077.405 | 1077.405 | 1077.405 |
| syscall:connect | 410/410 | 0 | 0 | 0.990 | n/a | n/a | 0.153 | 2.416 | 2.142 | 4.943 |
| tool:attribution | 2/2 | 0 | 0 | 0.744 | n/a | n/a | 0.000 | 371.857 | 371.857 | 395.720 |
| sandbox:create | 1/1 | 0 | 0 | 0.715 | 0.255 | 0.460 | 0.000 | 715.427 | 715.427 | 715.427 |
| run:detect | 1/1 | 0 | 0 | 0.416 | 0.001 | 0.415 | 0.000 | 415.596 | 415.596 | 415.596 |
| sandbox:start | 1/1 | 0 | 0 | 0.383 | 0.002 | 0.381 | 0.000 | 383.051 | 383.051 | 383.051 |
| runtime.container_create | 1/1 | 0 | 0 | 0.383 | 0.002 | 0.381 | 0.000 | 382.905 | 382.905 | 382.905 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.363 | n/a | n/a | 0.000 | 362.584 | 362.584 | 362.584 |
| syscall:execve | 216/216 | 0 | 0 | 0.318 | n/a | n/a | 0.128 | 1.472 | 1.198 | 2.758 |
| tool:submit_output | 1/1 | 0 | 0 | 0.238 | n/a | n/a | 0.000 | 238.347 | 238.347 | 238.347 |
| sandbox:stop | 1/1 | 0 | 0 | 0.200 | 0.001 | 0.199 | 0.000 | 200.223 | 200.223 | 200.223 |
| agency:services_close | 1/1 | 0 | 0 | 0.185 | 0.001 | 0.185 | 0.013 | 185.196 | 185.196 | 185.196 |
| agency:services_start | 1/1 | 0 | 0 | 0.091 | 0.043 | 0.048 | 0.000 | 91.303 | 91.303 | 91.303 |
| agent:create | 1/1 | 0 | 0 | 0.047 | 0.008 | 0.039 | 0.000 | 47.043 | 47.043 | 47.043 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.213 | 1.213 | 1.213 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.958 | 0.958 | 0.958 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.073 | 0.062 | 0.108 |
| tool:read | 1/1 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.537 | 0.537 | 0.537 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.191 | 0.191 | 0.191 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.049 | 0.049 | 0.049 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 917 | 0.724 | 0.021 | 46.781 | 46.781 | 6.675681 CPU seconds | n/a |
| GPU 0 memory | MB | 919 | 11816.651 | 11670.000 | 14512.000 | 11830.000 | n/a | n/a |
| GPU 0 power | W | 919 | 37.342 | 27.850 | 72.557 | 27.929 | n/a | 34532.390 J |
| GPU 0 proc / 17241-1279619 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b memory | MB | 919 | 3182.753 | 3118.000 | 5876.000 | 3194.000 | n/a | n/a |
| GPU 0 proc / 17241-1279619 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b estimated power | W | 641 | 1.049 | 0.000 | 55.773 | 0.000 | n/a | n/a |
| GPU 0 proc / 17241-1279619 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b utilization | percent | 641 | 0.732 | 0.000 | 68.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 17358-1281631 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b memory | MB | 919 | 8151.898 | 8070.000 | 8154.000 | 8154.000 | n/a | n/a |
| GPU 0 proc / 17358-1281631 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b estimated power | W | 265 | 46.122 | 0.000 | 71.831 | 0.000 | n/a | n/a |
| GPU 0 proc / 17358-1281631 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b utilization | percent | 265 | 63.362 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 919 | 11334.651 | 11188.000 | 14030.000 | 11348.000 | n/a | n/a |
| GPU 0 utilization | percent | 919 | 19.768 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 919 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 918 | 3.148 | 0.077 | 51.164 | 1.809 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 918 | 7.273 | 0.252 | 52.605 | 12.113 | n/a | n/a |
| host disk_read_mb_s | MB/s | 918 | 1.080 | 0.000 | 203.688 | 9.991 | n/a | n/a |
| host disk_write_mb_s | MB/s | 918 | 0.259 | 0.000 | 5.966 | 0.521 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 918 | 0.569 | 0.000 | 49.715 | 18.952 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 918 | 0.574 | 0.000 | 49.943 | 19.060 | n/a | n/a |
| host mem_total_mb | MB | 919 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 919 | 7172.219 | 6703.727 | 9207.246 | 7294.367 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 918 | 0.046 | 0.000 | 21.649 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 918 | 0.047 | 0.000 | 21.709 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 918 | 0.008 | 0.000 | 0.254 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 918 | 0.025 | 0.000 | 0.696 | 0.000 | n/a | n/a |
| Agency harness — python -m lsbench (PID 17241) CPU | percent | 918 | 3.449 | 0.000 | 100.964 | 1.990 | 31.940000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 17241) io read MB/s | MB/s | 918 | 0.001 | 0.000 | 0.463 | 0.000 | 1.195312 MB | n/a |
| Agency harness — python -m lsbench (PID 17241) io write MB/s | MB/s | 918 | 0.229 | 0.013 | 3.506 | 0.027 | 211.707031 MB | n/a |
| Agency harness — python -m lsbench (PID 17241) rss_mb | MB | 919 | 2999.923 | 2508.340 | 3609.297 | 3205.227 | n/a | n/a |
| Agency harness — python -m lsbench (PID 17241) main thread run-queue wait | percent | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 17241) vms_mb | MB | 919 | 15677.496 | 14051.945 | 19186.176 | 15899.457 | n/a | n/a |
| Python — vllm (PID 17307) CPU | percent | 918 | 0.677 | 0.000 | 4.960 | 0.000 | 6.270000 CPU seconds | n/a |
| Python — vllm (PID 17307) io read MB/s | MB/s | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 17307) io write MB/s | MB/s | 918 | 0.000 | 0.000 | 0.008 | 0.000 | 0.035156 MB | n/a |
| Python — vllm (PID 17307) rss_mb | MB | 919 | 1805.403 | 1803.332 | 1805.582 | 1805.582 | n/a | n/a |
| Python — vllm (PID 17307) main thread run-queue wait | percent | 918 | 0.003 | 0.000 | 0.462 | 0.013 | 0.030993 run-queue seconds | n/a |
| Python — vllm (PID 17307) vms_mb | MB | 919 | 11043.810 | 10971.699 | 11045.719 | 11045.719 | n/a | n/a |
| Python — python -c (PID 17357) CPU | percent | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 17357) io read MB/s | MB/s | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 17357) io write MB/s | MB/s | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 17357) rss_mb | MB | 919 | 12.180 | 12.180 | 12.180 | 12.180 | n/a | n/a |
| Python — python -c (PID 17357) main thread run-queue wait | percent | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 17357) vms_mb | MB | 919 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 17358) CPU | percent | 918 | 7.902 | 0.000 | 41.728 | 0.995 | 73.170000 CPU seconds | n/a |
| VLLM::EngineCore (PID 17358) io read MB/s | MB/s | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 17358) io write MB/s | MB/s | 918 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 17358) rss_mb | MB | 919 | 2337.462 | 2336.086 | 2337.586 | 2337.586 | n/a | n/a |
| VLLM::EngineCore (PID 17358) main thread run-queue wait | percent | 918 | 0.002 | 0.000 | 0.082 | 0.000 | 0.016144 run-queue seconds | n/a |
| VLLM::EngineCore (PID 17358) vms_mb | MB | 919 | 21237.618 | 21236.223 | 21237.730 | 21237.730 | n/a | n/a |
| docker run (PID 17538) rss_mb | MB | 1 | 30.570 | 30.570 | 30.570 | 30.570 | n/a | n/a |
| docker run (PID 17538) vms_mb | MB | 1 | 1843.762 | 1843.762 | 1843.762 | 1843.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 17582) CPU | percent | 917 | 0.002 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 17582) rss_mb | MB | 918 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 17582) main thread run-queue wait | percent | 917 | 0.005 | 0.000 | 4.405 | 0.000 | 0.048229 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 17582) vms_mb | MB | 918 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 17607) CPU | percent | 917 | 0.001 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 17607) rss_mb | MB | 918 | 1.316 | 1.316 | 1.316 | 1.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 17607) main thread run-queue wait | percent | 917 | 0.001 | 0.000 | 0.653 | 0.000 | 0.008423 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 17607) vms_mb | MB | 918 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 17708) CPU | percent | 917 | 4.575 | 0.000 | 94.527 | 0.000 | 42.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 17708) rss_mb | MB | 918 | 105.736 | 3.102 | 111.516 | 110.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 17708) main thread run-queue wait | percent | 917 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000111 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 17708) vms_mb | MB | 918 | 965.481 | 4.258 | 973.730 | 973.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 17714) CPU | percent | 1 | 59.295 | 59.295 | 59.295 | 59.295 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 17714) rss_mb | MB | 2 | 50.832 | 38.211 | 63.453 | 63.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 17714) main thread run-queue wait | percent | 1 | 0.011 | 0.011 | 0.011 | 0.011 | 0.000108 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 17714) vms_mb | MB | 2 | 58.467 | 45.129 | 71.805 | 71.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 17726) CPU | percent | 894 | 0.254 | 0.000 | 34.812 | 0.000 | 2.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 17726) rss_mb | MB | 895 | 72.595 | 47.473 | 74.516 | 73.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 17726) main thread run-queue wait | percent | 894 | 0.020 | 0.000 | 3.619 | 0.000 | 0.183814 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 17726) vms_mb | MB | 895 | 86.132 | 54.414 | 88.156 | 86.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test1.py (PID 17762) rss_mb | MB | 1 | 9.316 | 9.316 | 9.316 | 9.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — test1.py (PID 17762) vms_mb | MB | 1 | 13.277 | 13.277 | 13.277 | 13.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 17788) rss_mb | MB | 1 | 2.992 | 2.992 | 2.992 | 2.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 17788) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 17789) rss_mb | MB | 1 | 7.457 | 7.457 | 7.457 | 7.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 17789) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18139) rss_mb | MB | 1 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18139) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — pip (PID 18144) rss_mb | MB | 1 | 34.836 | 34.836 | 34.836 | 34.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — pip (PID 18144) vms_mb | MB | 1 | 41.543 | 41.543 | 41.543 | 41.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 18145) rss_mb | MB | 1 | 1.887 | 1.887 | 1.887 | 1.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 18145) vms_mb | MB | 1 | 3.770 | 3.770 | 3.770 | 3.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18149) rss_mb | MB | 1 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18149) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18150) rss_mb | MB | 1 | 97.988 | 97.988 | 97.988 | 97.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18150) vms_mb | MB | 1 | 102.234 | 102.234 | 102.234 | 102.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18160) rss_mb | MB | 1 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18160) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18161) rss_mb | MB | 1 | 8.031 | 8.031 | 8.031 | 8.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 18161) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 18236) rss_mb | MB | 1 | 72.906 | 72.906 | 72.906 | 72.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 18236) vms_mb | MB | 1 | 86.355 | 86.355 | 86.355 | 86.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18269) rss_mb | MB | 1 | 2.961 | 2.961 | 2.961 | 2.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18269) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18270) rss_mb | MB | 1 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18270) vms_mb | MB | 1 | 212.273 | 212.273 | 212.273 | 212.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18286) rss_mb | MB | 1 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18286) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18287) rss_mb | MB | 1 | 22.961 | 22.961 | 22.961 | 22.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18287) vms_mb | MB | 1 | 215.469 | 215.469 | 215.469 | 215.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18304) rss_mb | MB | 1 | 2.777 | 2.777 | 2.777 | 2.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18304) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18305) rss_mb | MB | 1 | 9.863 | 9.863 | 9.863 | 9.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18305) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 18312) rss_mb | MB | 1 | 1237.176 | 1237.176 | 1237.176 | 1237.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 18312) vms_mb | MB | 1 | 1670.922 | 1670.922 | 1670.922 | 1670.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18353) rss_mb | MB | 1 | 2.879 | 2.879 | 2.879 | 2.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18353) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18354) rss_mb | MB | 1 | 511.766 | 511.766 | 511.766 | 511.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18354) vms_mb | MB | 1 | 1672.656 | 1672.656 | 1672.656 | 1672.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18376) rss_mb | MB | 1 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18376) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18377) rss_mb | MB | 1 | 1383.512 | 1383.512 | 1383.512 | 1383.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18377) vms_mb | MB | 1 | 1672.633 | 1672.633 | 1672.633 | 1672.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18399) rss_mb | MB | 1 | 3.059 | 3.059 | 3.059 | 3.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18399) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18400) rss_mb | MB | 1 | 1409.793 | 1409.793 | 1409.793 | 1409.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18400) vms_mb | MB | 1 | 1672.812 | 1672.812 | 1672.812 | 1672.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18415) rss_mb | MB | 1 | 2.707 | 2.707 | 2.707 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18415) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18416) rss_mb | MB | 1 | 25.262 | 25.262 | 25.262 | 25.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18416) vms_mb | MB | 1 | 217.383 | 217.383 | 217.383 | 217.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18462) rss_mb | MB | 1 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18462) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18464) rss_mb | MB | 1 | 382.000 | 382.000 | 382.000 | 382.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18464) vms_mb | MB | 1 | 702.648 | 702.648 | 702.648 | 702.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18481) rss_mb | MB | 1 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18481) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18482) rss_mb | MB | 1 | 1942.840 | 1942.840 | 1942.840 | 1942.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18482) vms_mb | MB | 1 | 2650.648 | 2650.648 | 2650.648 | 2650.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18492) rss_mb | MB | 1 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18492) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18493) rss_mb | MB | 1 | 1653.730 | 1653.730 | 1653.730 | 1653.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18493) vms_mb | MB | 1 | 2642.801 | 2642.801 | 2642.801 | 2642.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18500) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18500) rss_mb | MB | 7 | 2.867 | 2.867 | 2.867 | 2.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18500) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18500) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18501) CPU | percent | 6 | 198.068 | 196.892 | 200.172 | 197.868 | 11.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18501) rss_mb | MB | 7 | 120.974 | 96.152 | 137.094 | 137.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18501) main thread run-queue wait | percent | 6 | 48.705 | 47.358 | 51.575 | 48.945 | 2.940929 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18501) vms_mb | MB | 7 | 337.188 | 313.887 | 353.043 | 353.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18524) rss_mb | MB | 1 | 2.895 | 2.895 | 2.895 | 2.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18524) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18525) rss_mb | MB | 1 | 802.020 | 802.020 | 802.020 | 802.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18525) vms_mb | MB | 1 | 1672.758 | 1672.758 | 1672.758 | 1672.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18557) CPU | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18557) rss_mb | MB | 20 | 2.719 | 2.719 | 2.719 | 2.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18557) main thread run-queue wait | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18557) vms_mb | MB | 20 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18558) CPU | percent | 19 | 197.871 | 174.066 | 202.562 | 201.010 | 37.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18558) rss_mb | MB | 20 | 123.028 | 13.418 | 152.289 | 102.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18558) main thread run-queue wait | percent | 19 | 48.696 | 36.124 | 54.588 | 50.170 | 9.325571 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18558) vms_mb | MB | 20 | 339.333 | 207.105 | 369.926 | 318.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18579) rss_mb | MB | 1 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18579) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18580) rss_mb | MB | 1 | 13.281 | 13.281 | 13.281 | 13.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18580) vms_mb | MB | 1 | 207.109 | 207.109 | 207.109 | 207.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18592) rss_mb | MB | 1 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18592) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18593) rss_mb | MB | 1 | 7.262 | 7.262 | 7.262 | 7.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18593) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18600) rss_mb | MB | 1 | 2.844 | 2.844 | 2.844 | 2.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18600) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18601) rss_mb | MB | 1 | 264.219 | 264.219 | 264.219 | 264.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18601) vms_mb | MB | 1 | 702.812 | 702.812 | 702.812 | 702.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18625) CPU | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18625) rss_mb | MB | 20 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18625) main thread run-queue wait | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18625) vms_mb | MB | 20 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18626) CPU | percent | 19 | 199.629 | 194.623 | 207.219 | 201.249 | 38.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18626) rss_mb | MB | 20 | 1100.669 | 1072.766 | 1123.215 | 1073.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18626) main thread run-queue wait | percent | 19 | 49.628 | 47.549 | 53.818 | 49.383 | 9.496607 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18626) vms_mb | MB | 20 | 1318.262 | 1288.734 | 1339.734 | 1288.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18644) rss_mb | MB | 1 | 2.965 | 2.965 | 2.965 | 2.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 18644) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18645) rss_mb | MB | 1 | 23.266 | 23.266 | 23.266 | 23.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — Python (PID 18645) vms_mb | MB | 1 | 215.508 | 215.508 | 215.508 | 215.508 | n/a | n/a |
| docker commit (PID 18688) CPU | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 18688) io read MB/s | MB/s | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 18688) io write MB/s | MB/s | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 18688) rss_mb | MB | 18 | 30.562 | 30.562 | 30.562 | 30.562 | n/a | n/a |
| docker commit (PID 18688) main thread run-queue wait | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 18688) vms_mb | MB | 18 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4633) CPU | percent | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4633) io read MB/s | MB/s | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4633) io write MB/s | MB/s | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4633) rss_mb | MB | 919 | 3.422 | 3.422 | 3.422 | 3.422 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4633) main thread run-queue wait | percent | 918 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4633) vms_mb | MB | 919 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 917 | 17.091 | 0.000 | 207.771 | 0.000 | 157.807747 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 917 | 2.848 | 0.000 | 50.304 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 917 | 2.947 | 0.000 | 50.467 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 917 | 0.052 | 0.000 | 15.895 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 917 | 0.052 | 0.000 | 15.896 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 917 | 0.047 | 0.000 | 10.219 | 0.000 | 43.281250 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 917 | 0.003 | 0.000 | 0.647 | 0.000 | 2.320312 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 918 | 227.969 | 54.594 | 2154.746 | 141.164 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 917 | 0.024 | 0.000 | 11.542 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 917 | 0.024 | 0.000 | 11.542 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 917 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000706 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 917 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 918 | 12.048 | 1.615 | 101.670 | 1.700 | 111.559956 CPU seconds | n/a |
| workload total memory | MB | 919 | 9107.828 | 8653.531 | 9696.488 | 9320.805 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
