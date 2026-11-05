# agprof summary

- Duration: **60.574 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.017 runs/s**
- LLM: **7 calls**, 7 succeeded, 0 failed, 0 interrupted, n/a reported retries, 49.802 s total wait
- Tools: **6/6 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **9686** at 1.992 Hz effective (2 Hz configured)
- GPU sampling: **unavailable** (not requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 60530.922 / 60530.922 ms |
| LLM latency p50 / p95 | 3989.671 / 20939.144 ms |
| LLM TTFT p50 / p95 | 3449.024 / 15815.381 ms |
| LLM input / output tokens | 22072 / 1668 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 7 total, 7 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 239.450 / 322.060 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {"unmatched_completions": 228}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 2/2 | 2 | 0 | 0 | 265.465 ms | 338.984 ms |
| submit_output | 4/4 | 4 | 0 | 0 | 239.450 ms | 246.329 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 4.165% | 90.064% | 2.488 s | 179.294 MB | 203.418 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 3954 |  | 120 | 3.950% | 89.569% | 2.360 s | 187.426 MB | 198.652 MB | 967.616 MB | 1000.438 MB | 0.425781 MB | 14.046875 MB |
| timeout | 3940 |  | 120 | 0.000% | 0.000% | 0.000 s | 1.816 MB | 1.816 MB | 5.641 MB | 5.641 MB | 0.000000 MB | 0.000000 MB |
| sshd | 3937 |  | 120 | 0.000% | 0.000% | 0.000 s | 6.852 MB | 6.852 MB | 14.656 MB | 14.656 MB | n/a MB | n/a MB |
| docker | 4036 |  | 5 | 0.000% | 0.000% | 0.000 s | 31.004 MB | 31.207 MB | 1771.500 MB | 1771.500 MB | 0.132812 MB | 0.000000 MB |
| bash | 3938 |  | 120 | 0.000% | 0.000% | 0.000 s | 3.496 MB | 3.496 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| sshd | 3888 |  | 120 | 0.000% | 0.000% | 0.000 s | 10.273 MB | 10.273 MB | 14.406 MB | 14.406 MB | n/a MB | n/a MB |
| uv | 3942 |  | 120 | 0.000% | 0.000% | 0.000 s | 33.578 MB | 33.727 MB | 568.735 MB | 568.762 MB | 0.000000 MB | 0.000000 MB |
| tail | 3941 |  | 120 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 5.664 MB | 5.664 MB | 0.000000 MB | 0.000000 MB |
| docker | 4111 |  | 1 | n/a% | n/a% | n/a s | 22.102 MB | 22.102 MB | 1625.848 MB | 1625.848 MB | n/a MB | n/a MB |
| tail | 4108 | sandbox_agent_lso-native_0000_0000 | 114 | 0.000% | 0.000% | 0.000 s | 1.562 MB | 1.562 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 4205 | sandbox_agent_lso-native_0000_0000 | 2 | 99.588% | 99.588% | 0.500 s | 63.023 MB | 78.707 MB | 73.752 MB | 92.676 MB | n/a MB | n/a MB |
| bash | 4199 | sandbox_agent_lso-native_0000_0000 | 114 | 4.461% | 99.651% | 2.530 s | 97.646 MB | 101.809 MB | 758.252 MB | 899.113 MB | n/a MB | n/a MB |
| docker-init | 4076 | sandbox_agent_lso-native_0000_0000 | 114 | 0.000% | 0.000% | 0.000 s | 0.547 MB | 0.547 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 4217 | sandbox_agent_lso-native_0000_0000 | 107 | 1.334% | 69.729% | 0.710 s | 69.804 MB | 71.461 MB | 82.538 MB | 85.012 MB | n/a MB | n/a MB |
| bash | 4227 | sandbox_agent_lso-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.949 MB | 2.949 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4230 | sandbox_agent_lso-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.281 MB | 21.281 MB | 212.414 MB | 212.414 MB | n/a MB | n/a MB |
| docker | 4289 |  | 2 | 0.000% | 0.000% | 0.000 s | 29.523 MB | 29.523 MB | 1835.586 MB | 1835.586 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lso-native_0000_0000 | 8.412% | 100.047% | 4.772 s | 131.033 MB | 145.281 MB | 0.000000 MB | 0.835938 MB | 0.000525 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 3966 | 60.533 | interrupted |
| syscall:connect | -1 | 53.874 | interrupted |
| syscall:sendto | -1 | 53.869 | interrupted |
| syscall:sendto | -1 | 53.866 | interrupted |
| syscall:sendto | -1 | 53.229 | interrupted |
| syscall:connect | -1 | 52.767 | interrupted |
| syscall:sendto | -1 | 52.765 | interrupted |
| syscall:sendto | -1 | 52.761 | interrupted |
| syscall:sendto | -1 | 52.646 | interrupted |
| syscall:sendto | -1 | 52.644 | interrupted |
| syscall:sendto | -1 | 52.641 | interrupted |
| syscall:connect | -1 | 52.637 | interrupted |
| syscall:connect | -1 | 52.632 | interrupted |
| syscall:sendto | -1 | 52.629 | interrupted |
| syscall:sendto | -1 | 52.625 | interrupted |
| syscall:sendto | -1 | 52.621 | interrupted |
| syscall:sendto | -1 | 52.616 | interrupted |
| syscall:connect | -1 | 52.579 | interrupted |
| syscall:sendto | -1 | 52.576 | interrupted |
| syscall:sendto | -1 | 52.572 | interrupted |
| syscall:sendto | -1 | 52.551 | interrupted |
| syscall:sendto | -1 | 52.547 | interrupted |
| syscall:sendto | -1 | 52.543 | interrupted |
| syscall:sendto | -1 | 52.539 | interrupted |
| syscall:connect | -1 | 52.535 | interrupted |
| syscall:sendto | -1 | 52.530 | interrupted |
| syscall:sendto | -1 | 52.507 | interrupted |
| syscall:sendto | -1 | 52.503 | interrupted |
| syscall:connect | -1 | 52.499 | interrupted |
| syscall:sendto | -1 | 52.495 | interrupted |
| syscall:sendto | -1 | 52.491 | interrupted |
| syscall:connect | -1 | 45.978 | interrupted |
| syscall:sendto | -1 | 45.974 | interrupted |
| syscall:sendto | -1 | 45.970 | interrupted |
| syscall:sendto | -1 | 45.955 | interrupted |
| syscall:sendto | -1 | 45.951 | interrupted |
| syscall:connect | -1 | 45.949 | interrupted |
| syscall:connect | -1 | 45.945 | interrupted |
| syscall:connect | -1 | 45.932 | interrupted |
| syscall:connect | -1 | 45.928 | interrupted |
| syscall:connect | -1 | 45.924 | interrupted |
| syscall:connect | -1 | 45.920 | interrupted |
| syscall:sendto | -1 | 45.791 | interrupted |
| syscall:sendto | -1 | 45.787 | interrupted |
| syscall:sendto | -1 | 45.783 | interrupted |
| syscall:sendto | -1 | 45.781 | interrupted |
| syscall:sendto | -1 | 45.777 | interrupted |
| syscall:sendto | -1 | 45.772 | interrupted |
| syscall:sendto | -1 | 45.769 | interrupted |
| syscall:sendto | -1 | 45.766 | interrupted |
| syscall:connect | -1 | 45.762 | interrupted |
| syscall:sendto | -1 | 45.758 | interrupted |
| syscall:sendto | -1 | 45.754 | interrupted |
| syscall:connect | -1 | 18.585 | interrupted |
| syscall:sendto | -1 | 18.582 | interrupted |
| syscall:sendto | -1 | 18.577 | interrupted |
| syscall:sendto | -1 | 18.563 | interrupted |
| syscall:sendto | -1 | 18.561 | interrupted |
| syscall:connect | -1 | 18.559 | interrupted |
| syscall:connect | -1 | 18.555 | interrupted |
| syscall:sendto | -1 | 18.235 | interrupted |
| syscall:sendto | -1 | 18.231 | interrupted |
| syscall:sendto | -1 | 18.226 | interrupted |
| syscall:sendto | -1 | 18.221 | interrupted |
| syscall:sendto | -1 | 18.217 | interrupted |
| syscall:sendto | -1 | 18.213 | interrupted |
| syscall:sendto | -1 | 18.208 | interrupted |
| syscall:sendto | -1 | 18.204 | interrupted |
| syscall:connect | -1 | 18.200 | interrupted |
| syscall:sendto | -1 | 18.196 | interrupted |
| syscall:sendto | -1 | 18.192 | interrupted |
| syscall:sendto | -1 | 14.527 | interrupted |
| syscall:sendto | -1 | 14.522 | interrupted |
| syscall:connect | -1 | 14.495 | interrupted |
| syscall:sendto | -1 | 14.491 | interrupted |
| syscall:sendto | -1 | 14.488 | interrupted |
| syscall:sendto | -1 | 14.468 | interrupted |
| syscall:sendto | -1 | 14.463 | interrupted |
| syscall:sendto | -1 | 14.459 | interrupted |
| syscall:connect | -1 | 14.455 | interrupted |
| syscall:connect | -1 | 14.451 | interrupted |
| syscall:sendto | -1 | 14.446 | interrupted |
| syscall:sendto | -1 | 14.441 | interrupted |
| syscall:sendto | -1 | 14.437 | interrupted |
| syscall:sendto | -1 | 14.433 | interrupted |
| syscall:connect | -1 | 14.398 | interrupted |
| syscall:sendto | -1 | 14.394 | interrupted |
| syscall:sendto | -1 | 14.389 | interrupted |
| syscall:sendto | -1 | 14.368 | interrupted |
| syscall:sendto | -1 | 14.366 | interrupted |
| syscall:sendto | -1 | 14.361 | interrupted |
| syscall:connect | -1 | 14.359 | interrupted |
| syscall:sendto | -1 | 14.355 | interrupted |
| syscall:sendto | -1 | 14.351 | interrupted |
| syscall:sendto | -1 | 14.347 | interrupted |
| syscall:sendto | -1 | 14.326 | interrupted |
| syscall:sendto | -1 | 14.323 | interrupted |
| syscall:sendto | -1 | 14.319 | interrupted |
| syscall:sendto | -1 | 14.317 | interrupted |
| syscall:connect | -1 | 14.313 | interrupted |
| syscall:sendto | -1 | 14.309 | interrupted |
| syscall:sendto | -1 | 14.286 | interrupted |
| syscall:sendto | -1 | 14.282 | interrupted |
| syscall:sendto | -1 | 14.277 | interrupted |
| syscall:sendto | -1 | 14.275 | interrupted |
| syscall:sendto | -1 | 14.270 | interrupted |
| syscall:sendto | -1 | 14.266 | interrupted |
| syscall:connect | -1 | 14.262 | interrupted |
| syscall:sendto | -1 | 14.258 | interrupted |
| syscall:sendto | -1 | 14.254 | interrupted |
| syscall:sendto | -1 | 12.797 | interrupted |
| syscall:sendto | -1 | 12.793 | interrupted |
| syscall:connect | -1 | 12.766 | interrupted |
| syscall:sendto | -1 | 12.762 | interrupted |
| syscall:sendto | -1 | 12.757 | interrupted |
| syscall:sendto | -1 | 12.734 | interrupted |
| syscall:sendto | -1 | 12.730 | interrupted |
| syscall:sendto | -1 | 12.726 | interrupted |
| syscall:connect | -1 | 12.722 | interrupted |
| syscall:connect | -1 | 12.717 | interrupted |
| syscall:sendto | -1 | 12.713 | interrupted |
| syscall:sendto | -1 | 12.709 | interrupted |
| syscall:sendto | -1 | 12.704 | interrupted |
| syscall:sendto | -1 | 12.702 | interrupted |
| syscall:connect | -1 | 12.660 | interrupted |
| syscall:sendto | -1 | 12.657 | interrupted |
| syscall:sendto | -1 | 12.653 | interrupted |
| syscall:sendto | -1 | 12.632 | interrupted |
| syscall:sendto | -1 | 12.628 | interrupted |
| syscall:sendto | -1 | 12.624 | interrupted |
| syscall:connect | -1 | 12.622 | interrupted |
| syscall:sendto | -1 | 12.617 | interrupted |
| syscall:sendto | -1 | 12.615 | interrupted |
| syscall:sendto | -1 | 12.609 | interrupted |
| syscall:sendto | -1 | 12.585 | interrupted |
| syscall:sendto | -1 | 12.581 | interrupted |
| syscall:sendto | -1 | 12.579 | interrupted |
| syscall:sendto | -1 | 12.575 | interrupted |
| syscall:connect | -1 | 12.570 | interrupted |
| syscall:sendto | -1 | 12.566 | interrupted |
| syscall:sendto | -1 | 12.543 | interrupted |
| syscall:sendto | -1 | 12.539 | interrupted |
| syscall:sendto | -1 | 12.535 | interrupted |
| syscall:sendto | -1 | 12.531 | interrupted |
| syscall:sendto | -1 | 12.526 | interrupted |
| syscall:sendto | -1 | 12.522 | interrupted |
| syscall:connect | -1 | 12.518 | interrupted |
| syscall:sendto | -1 | 12.514 | interrupted |
| syscall:sendto | -1 | 12.510 | interrupted |
| syscall:sendto | -1 | 9.810 | interrupted |
| syscall:sendto | -1 | 9.806 | interrupted |
| syscall:connect | -1 | 9.781 | interrupted |
| syscall:sendto | -1 | 9.776 | interrupted |
| syscall:sendto | -1 | 9.772 | interrupted |
| syscall:sendto | -1 | 9.749 | interrupted |
| syscall:sendto | -1 | 9.745 | interrupted |
| syscall:sendto | -1 | 9.741 | interrupted |
| syscall:connect | -1 | 9.737 | interrupted |
| syscall:connect | -1 | 9.732 | interrupted |
| syscall:sendto | -1 | 9.728 | interrupted |
| syscall:sendto | -1 | 9.724 | interrupted |
| syscall:sendto | -1 | 9.719 | interrupted |
| syscall:sendto | -1 | 9.715 | interrupted |
| syscall:connect | -1 | 9.677 | interrupted |
| syscall:sendto | -1 | 9.673 | interrupted |
| syscall:sendto | -1 | 9.669 | interrupted |
| syscall:sendto | -1 | 9.648 | interrupted |
| syscall:sendto | -1 | 9.644 | interrupted |
| syscall:sendto | -1 | 9.642 | interrupted |
| syscall:connect | -1 | 9.637 | interrupted |
| syscall:sendto | -1 | 9.633 | interrupted |
| syscall:sendto | -1 | 9.631 | interrupted |
| syscall:sendto | -1 | 9.625 | interrupted |
| syscall:sendto | -1 | 9.603 | interrupted |
| syscall:sendto | -1 | 9.599 | interrupted |
| syscall:sendto | -1 | 9.595 | interrupted |
| syscall:sendto | -1 | 9.590 | interrupted |
| syscall:connect | -1 | 9.586 | interrupted |
| syscall:sendto | -1 | 9.581 | interrupted |
| syscall:sendto | -1 | 9.560 | interrupted |
| syscall:sendto | -1 | 9.558 | interrupted |
| syscall:sendto | -1 | 9.554 | interrupted |
| syscall:sendto | -1 | 9.550 | interrupted |
| syscall:sendto | -1 | 9.546 | interrupted |
| syscall:sendto | -1 | 9.542 | interrupted |
| syscall:connect | -1 | 9.537 | interrupted |
| syscall:sendto | -1 | 9.533 | interrupted |
| syscall:sendto | -1 | 9.529 | interrupted |
| syscall:sendto | -1 | 5.024 | interrupted |
| syscall:sendto | -1 | 5.019 | interrupted |
| syscall:connect | -1 | 4.994 | interrupted |
| syscall:sendto | -1 | 4.992 | interrupted |
| syscall:sendto | -1 | 4.990 | interrupted |
| syscall:sendto | -1 | 4.967 | interrupted |
| syscall:sendto | -1 | 4.964 | interrupted |
| syscall:sendto | -1 | 4.960 | interrupted |
| syscall:connect | -1 | 4.956 | interrupted |
| syscall:connect | -1 | 4.952 | interrupted |
| syscall:sendto | -1 | 4.948 | interrupted |
| syscall:sendto | -1 | 4.945 | interrupted |
| syscall:sendto | -1 | 4.941 | interrupted |
| syscall:sendto | -1 | 4.938 | interrupted |
| syscall:connect | -1 | 4.896 | interrupted |
| syscall:sendto | -1 | 4.896 | interrupted |
| syscall:sendto | -1 | 4.893 | interrupted |
| syscall:sendto | -1 | 4.872 | interrupted |
| syscall:sendto | -1 | 4.868 | interrupted |
| syscall:sendto | -1 | 4.863 | interrupted |
| syscall:connect | -1 | 4.859 | interrupted |
| syscall:sendto | -1 | 4.855 | interrupted |
| syscall:sendto | -1 | 4.851 | interrupted |
| syscall:sendto | -1 | 4.846 | interrupted |
| syscall:sendto | -1 | 4.825 | interrupted |
| syscall:sendto | -1 | 4.820 | interrupted |
| syscall:sendto | -1 | 4.818 | interrupted |
| syscall:sendto | -1 | 4.816 | interrupted |
| syscall:connect | -1 | 4.812 | interrupted |
| syscall:sendto | -1 | 4.807 | interrupted |
| syscall:sendto | -1 | 4.787 | interrupted |
| syscall:sendto | -1 | 4.783 | interrupted |
| syscall:sendto | -1 | 4.778 | interrupted |
| syscall:sendto | -1 | 4.774 | interrupted |
| syscall:sendto | -1 | 4.770 | interrupted |
| syscall:sendto | -1 | 4.766 | interrupted |
| syscall:connect | -1 | 4.761 | interrupted |
| syscall:sendto | -1 | 4.757 | interrupted |
| syscall:sendto | -1 | 4.754 | interrupted |
| syscall:sendto | -1 | 0.731 | interrupted |
| syscall:sendto | -1 | 0.727 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:recover_rank1_edit | 1/1 | 0 | 0 | 60.531 | n/a | n/a | 0.000 | 60530.922 | 60530.922 | 60530.922 |
| sync:result_wait | 1/1 | 0 | 0 | 60.531 | 0.000 | 60.530 | 0.000 | 60530.575 | 60530.575 | 60530.575 |
| engine:execute | 1/1 | 0 | 0 | 60.529 | 0.763 | 59.766 | 0.000 | 60529.446 | 60529.446 | 60529.446 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 54.084 | 0.001 | 54.083 | 0.000 | 54084.281 | 54084.281 | 54084.281 |
| turn | 7/7 | 0 | 0 | 51.737 | n/a | n/a | 0.000 | 7390.981 | 4039.549 | 21305.669 |
| llm:attempt | 7/7 | 0 | 0 | 49.802 | 0.630 | 49.172 | 0.000 | 7114.554 | 3989.671 | 20939.144 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.956 | 0.566 | 4.390 | 0.000 | 4955.833 | 4955.833 | 4955.833 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.956 | 0.566 | 4.390 | 0.000 | 4955.633 | 4955.633 | 4955.633 |
| run:container_call | 13/13 | 0 | 0 | 3.855 | 0.002 | 3.853 | 0.000 | 296.557 | 26.771 | 1559.919 |
| sandbox:start | 1/1 | 0 | 0 | 2.773 | 0.002 | 2.771 | 0.000 | 2773.358 | 2773.358 | 2773.358 |
| runtime.container_create | 1/1 | 0 | 0 | 2.773 | 0.002 | 2.771 | 0.000 | 2773.252 | 2773.252 | 2773.252 |
| teardown:commit | 1/1 | 0 | 0 | 1.030 | 0.004 | 1.026 | 0.000 | 1030.223 | 1030.223 | 1030.223 |
| tool:submit_output | 4/4 | 0 | 0 | 0.957 | n/a | n/a | 0.000 | 239.150 | 239.450 | 246.329 |
| sandbox:commit | 1/1 | 0 | 0 | 0.892 | 0.002 | 0.890 | 0.000 | 891.790 | 891.790 | 891.790 |
| checkpoint.total | 1/1 | 0 | 0 | 0.892 | 0.002 | 0.890 | 0.000 | 891.689 | 891.689 | 891.689 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 0.892 | 0.002 | 0.890 | 0.000 | 891.585 | 891.585 | 891.585 |
| tool:bash | 2/2 | 0 | 0 | 0.531 | n/a | n/a | 0.000 | 265.465 | 265.465 | 338.984 |
| process:bash | 2/2 | 0 | 0 | 0.513 | n/a | n/a | 0.000 | 256.578 | 256.578 | 330.643 |
| agency:services_start | 1/1 | 0 | 0 | 0.160 | 0.080 | 0.080 | 0.000 | 160.169 | 160.169 | 160.169 |
| sandbox:stop | 1/1 | 0 | 0 | 0.138 | 0.002 | 0.137 | 0.000 | 138.217 | 138.217 | 138.217 |
| agency:services_close | 1/1 | 0 | 0 | 0.129 | 0.001 | 0.128 | 0.000 | 129.212 | 129.212 | 129.212 |
| sandbox:create | 1/1 | 0 | 0 | 0.102 | 0.036 | 0.067 | 0.000 | 102.427 | 102.427 | 102.427 |
| agent:create | 1/1 | 0 | 0 | 0.039 | 0.005 | 0.035 | 0.000 | 39.322 | 39.322 | 39.322 |
| run:detect | 1/1 | 0 | 0 | 0.036 | 0.001 | 0.035 | 0.000 | 35.873 | 35.873 | 35.873 |
| syscall:execve | 7/7 | 0 | 0 | 0.022 | n/a | n/a | 0.000 | 3.210 | 3.116 | 3.783 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.315 | 1.315 | 1.315 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.077 | 0.089 | 0.110 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.196 | 0.196 | 0.196 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.130 | 0.130 | 0.130 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.041 | 0.041 | 0.041 |
| syscall:connect | 0/47 | 0 | 47 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| syscall:sendto | 0/181 | 0 | 181 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 113 | 1.894 | 0.021 | 168.062 | 168.062 | 1.076664 CPU seconds | n/a |
| host cpu_count | CPUs | 120 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 119 | 0.196 | 0.010 | 2.377 | 1.573 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 119 | 3.710 | 0.000 | 41.361 | 41.361 | n/a | n/a |
| host disk_read_mb_s | MB/s | 119 | 0.140 | 0.000 | 14.623 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 119 | 5.016 | 0.000 | 235.772 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 119 | 3.091 | 0.000 | 98.763 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 119 | 3.098 | 0.000 | 98.798 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 120 | 15701.543 | 15701.543 | 15701.543 | 15701.543 | n/a | n/a |
| host mem_used_mb | MB | 120 | 1020.876 | 867.969 | 1076.797 | 990.266 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 119 | 0.000 | 0.000 | 0.002 | 0.002 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 119 | 0.000 | 0.000 | 0.002 | 0.002 | n/a | n/a |
| host net_rx_mb_s | MB/s | 119 | 0.010 | 0.000 | 0.492 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 119 | 0.003 | 0.000 | 0.052 | 0.000 | n/a | n/a |
| sshd: ubuntu [priv] (PID 3888) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sshd: ubuntu [priv] (PID 3888) rss_mb | MB | 120 | 10.273 | 10.273 | 10.273 | 10.273 | n/a | n/a |
| sshd: ubuntu [priv] (PID 3888) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sshd: ubuntu [priv] (PID 3888) vms_mb | MB | 120 | 14.406 | 14.406 | 14.406 | 14.406 | n/a | n/a |
| sshd: ubuntu@notty (PID 3937) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sshd: ubuntu@notty (PID 3937) rss_mb | MB | 120 | 6.852 | 6.852 | 6.852 | 6.852 | n/a | n/a |
| sshd: ubuntu@notty (PID 3937) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sshd: ubuntu@notty (PID 3937) vms_mb | MB | 120 | 14.656 | 14.656 | 14.656 | 14.656 | n/a | n/a |
| bash (PID 3938) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash (PID 3938) io read MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash (PID 3938) io write MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash (PID 3938) rss_mb | MB | 120 | 3.496 | 3.496 | 3.496 | 3.496 | n/a | n/a |
| bash (PID 3938) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash (PID 3938) vms_mb | MB | 120 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| timeout (PID 3940) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| timeout (PID 3940) io read MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| timeout (PID 3940) io write MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| timeout (PID 3940) rss_mb | MB | 120 | 1.816 | 1.816 | 1.816 | 1.816 | n/a | n/a |
| timeout (PID 3940) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| timeout (PID 3940) vms_mb | MB | 120 | 5.641 | 5.641 | 5.641 | 5.641 | n/a | n/a |
| tail (PID 3941) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail (PID 3941) io read MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| tail (PID 3941) io write MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| tail (PID 3941) rss_mb | MB | 120 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| tail (PID 3941) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| tail (PID 3941) vms_mb | MB | 120 | 5.664 | 5.664 | 5.664 | 5.664 | n/a | n/a |
| uv (PID 3942) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| uv (PID 3942) io read MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| uv (PID 3942) io write MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| uv (PID 3942) rss_mb | MB | 120 | 33.578 | 33.555 | 33.727 | 33.555 | n/a | n/a |
| uv (PID 3942) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| uv (PID 3942) vms_mb | MB | 120 | 568.735 | 568.730 | 568.762 | 568.730 | n/a | n/a |
| Agency harness — run_agency.py (PID 3954) CPU | percent | 119 | 3.950 | 0.000 | 89.569 | 0.000 | 2.360000 CPU seconds | n/a |
| Agency harness — run_agency.py (PID 3954) io read MB/s | MB/s | 119 | 0.007 | 0.000 | 0.715 | 0.000 | 0.425781 MB | n/a |
| Agency harness — run_agency.py (PID 3954) io write MB/s | MB/s | 119 | 0.235 | 0.000 | 6.539 | 0.000 | 14.046875 MB | n/a |
| Agency harness — run_agency.py (PID 3954) rss_mb | MB | 120 | 187.426 | 143.801 | 198.652 | 198.652 | n/a | n/a |
| Agency harness — run_agency.py (PID 3954) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — run_agency.py (PID 3954) vms_mb | MB | 120 | 967.616 | 691.426 | 1000.438 | 985.316 | n/a | n/a |
| docker run (PID 4036) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker run (PID 4036) io read MB/s | MB/s | 4 | 0.066 | 0.000 | 0.265 | 0.265 | 0.132812 MB | n/a |
| docker run (PID 4036) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker run (PID 4036) rss_mb | MB | 5 | 31.004 | 30.953 | 31.207 | 31.207 | n/a | n/a |
| docker run (PID 4036) main thread run-queue wait | percent | 4 | 0.001 | 0.000 | 0.002 | 0.002 | 0.000012 run-queue seconds | n/a |
| docker run (PID 4036) vms_mb | MB | 5 | 1771.500 | 1771.500 | 1771.500 | 1771.500 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — docker-init (PID 4076) CPU | percent | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — docker-init (PID 4076) rss_mb | MB | 114 | 0.547 | 0.547 | 0.547 | 0.547 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — docker-init (PID 4076) main thread run-queue wait | percent | 113 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000007 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — docker-init (PID 4076) vms_mb | MB | 114 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — tail (PID 4108) CPU | percent | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — tail (PID 4108) rss_mb | MB | 114 | 1.562 | 1.562 | 1.562 | 1.562 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — tail (PID 4108) main thread run-queue wait | percent | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — tail (PID 4108) vms_mb | MB | 114 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| docker exec (PID 4111) rss_mb | MB | 1 | 22.102 | 22.102 | 22.102 | 22.102 | n/a | n/a |
| docker exec (PID 4111) vms_mb | MB | 1 | 1625.848 | 1625.848 | 1625.848 | 1625.848 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — bash (PID 4199) CPU | percent | 113 | 4.461 | 0.000 | 99.651 | 0.000 | 2.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — bash (PID 4199) rss_mb | MB | 114 | 97.646 | 3.113 | 101.809 | 101.809 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — bash (PID 4199) main thread run-queue wait | percent | 113 | 0.000 | 0.000 | 0.013 | 0.000 | 0.000112 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — bash (PID 4199) vms_mb | MB | 114 | 758.252 | 4.258 | 899.113 | 899.066 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python -c (PID 4205) CPU | percent | 1 | 99.588 | 99.588 | 99.588 | 99.588 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python -c (PID 4205) rss_mb | MB | 2 | 63.023 | 47.340 | 78.707 | 78.707 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python -c (PID 4205) main thread run-queue wait | percent | 1 | 0.021 | 0.021 | 0.021 | 0.021 | 0.000103 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python -c (PID 4205) vms_mb | MB | 2 | 73.752 | 54.828 | 92.676 | 92.676 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python -m native_harness.cli (PID 4217) CPU | percent | 106 | 1.334 | 0.000 | 69.729 | 9.962 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python -m native_harness.cli (PID 4217) rss_mb | MB | 107 | 69.804 | 31.383 | 71.461 | 71.461 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python -m native_harness.cli (PID 4217) main thread run-queue wait | percent | 106 | 0.002 | 0.000 | 0.086 | 0.000 | 0.000987 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python -m native_harness.cli (PID 4217) vms_mb | MB | 107 | 82.538 | 36.180 | 85.012 | 85.012 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — bash (PID 4227) rss_mb | MB | 1 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — bash (PID 4227) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python stdin (PID 4230) rss_mb | MB | 1 | 21.281 | 21.281 | 21.281 | 21.281 | n/a | n/a |
| sandbox:sandbox_agent_lso-native_0000_0000 — python stdin (PID 4230) vms_mb | MB | 1 | 212.414 | 212.414 | 212.414 | 212.414 | n/a | n/a |
| docker commit (PID 4289) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4289) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4289) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4289) rss_mb | MB | 2 | 29.523 | 29.523 | 29.523 | 29.523 | n/a | n/a |
| docker commit (PID 4289) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4289) vms_mb | MB | 2 | 1835.586 | 1835.586 | 1835.586 | 1835.586 | n/a | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 CPU | percent | 113 | 8.412 | 0.000 | 100.047 | 0.000 | 4.771680 CPU seconds | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 113 | 0.204 | 0.000 | 0.281 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 113 | 0.210 | 0.000 | 0.520 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 113 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 113 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 io read MB/s | MB/s | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 io write MB/s | MB/s | 113 | 0.015 | 0.000 | 1.502 | 0.000 | 0.835938 MB | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 memory | MB | 114 | 131.033 | 35.324 | 145.281 | 86.152 | n/a | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 113 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 113 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 net rx MB/s | MB/s | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000525 MB | n/a |
| sandbox sandbox_agent_lso-native_0000_0000 net tx MB/s | MB/s | 113 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 119 | 4.165 | 0.326 | 90.064 | 0.670 | 2.488212 CPU seconds | n/a |
| workload total memory | MB | 120 | 179.294 | 130.297 | 203.418 | 203.418 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
