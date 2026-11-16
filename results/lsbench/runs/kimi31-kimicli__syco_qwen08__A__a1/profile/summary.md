# agprof summary

- Duration: **2940.717 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **302 calls**, 288 succeeded, 14 failed, 0 interrupted, 1 reported retries, 1767.834 s total wait
- Tools: **100/100 completed**, 27 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **327089** at 1.965 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2914095.303 / 2914095.303 ms |
| LLM latency p50 / p95 | 4684.318 / 10493.565 ms |
| LLM TTFT p50 / p95 | 4059.073 / 9801.306 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 303 total, 288 succeeded, 14 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {"unmatched_completions": 1}
- kimi: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 73/73 | 48 | 25 | 0 | n/a | n/a |
| Edit | 6/6 | 6 | 0 | 0 | n/a | n/a |
| Glob | 2/2 | 1 | 1 | 0 | n/a | n/a |
| Grep | 1/1 | 0 | 1 | 0 | n/a | n/a |
| Read | 7/7 | 7 | 0 | 0 | n/a | n/a |
| TodoList | 6/6 | 6 | 0 | 0 | n/a | n/a |
| Write | 5/5 | 5 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 6.470% | 103.001% | 190.670 s | 9201.595 MB | 9674.785 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 4289 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 99.777% | 99.777% | 1.010 s | 45.574 MB | 70.012 MB | 55.238 MB | 78.457 MB | n/a MB | n/a MB |
| python | 3941 |  | 2917 | 0.000% | 0.000% | 0.000 s | 12.188 MB | 12.188 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| bash | 4283 | sandbox_agent_lsb-kimi_0000_0000 | 2890 | 51.847% | 106.794% | 1510.560 s | 132.106 MB | 155.695 MB | 901.989 MB | 917.621 MB | n/a MB | n/a MB |
| vllm | 3904 |  | 2917 | 0.139% | 7.932% | 4.100 s | 1783.331 MB | 1783.422 MB | 11021.164 MB | 11024.043 MB | 0.000000 MB | 0.050781 MB |
| sleep | 3910 |  | 11 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 4160 | sandbox_agent_lsb-kimi_0000_0000 | 2890 | 0.001% | 0.994% | 0.040 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| kimi_seq.sh | 1928 |  | 2917 | 0.000% | 0.000% | 0.000 s | 3.293 MB | 3.293 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 3942 |  | 2917 | 1.047% | 30.735% | 30.800 s | 2322.076 MB | 2322.082 MB | 21203.227 MB | 21203.227 MB | 0.000000 MB | 0.015625 MB |
| tail | 4191 | sandbox_agent_lsb-kimi_0000_0000 | 2890 | 0.002% | 0.994% | 0.060 s | 1.461 MB | 1.461 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| lsb_grid_worker | 3890 |  | 2917 | 0.000% | 0.000% | 0.000 s | 3.387 MB | 3.387 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| lsb_guard.sh | 3862 |  | 2917 | 0.001% | 0.994% | 0.030 s | 3.367 MB | 3.367 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 3899 |  | 2917 | 5.253% | 101.994% | 154.800 s | 3164.241 MB | 3561.727 MB | 16106.040 MB | 16504.930 MB | 4.691406 MB | 1273.855469 MB |
| MainThread | 4297 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 162.652 MB | 162.652 MB | 1572.348 MB | 1572.348 MB | n/a MB | n/a MB |
| MainThread | 4314 | sandbox_agent_lsb-kimi_0000_0000 | 191 | 5.260% | 72.383% | 10.070 s | 380.937 MB | 396.344 MB | 10101.021 MB | 10214.203 MB | n/a MB | n/a MB |
| sleep | 4351 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 4363 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4364 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.824 MB | 15.824 MB | 20.844 MB | 20.844 MB | n/a MB | n/a MB |
| bash | 4483 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.738 MB | 2.738 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 4485 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 49.789 MB | 49.789 MB | 56.828 MB | 56.828 MB | n/a MB | n/a MB |
| python3 | 4499 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.992 MB | 13.992 MB | 19.902 MB | 19.902 MB | n/a MB | n/a MB |
| sh | 4498 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4504 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.406 MB | 21.406 MB | 26.977 MB | 26.977 MB | n/a MB | n/a MB |
| sh | 4503 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 4523 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp | 4527 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 43.809 MB | 43.809 MB | 50.984 MB | 50.984 MB | n/a MB | n/a MB |
| bash | 4535 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.750 MB | 2.750 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 4539 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.043 MB | 8.043 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| sleep | 4547 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4557 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 26.117 MB | 26.117 MB | 35.055 MB | 35.055 MB | n/a MB | n/a MB |
| sh | 4558 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4559 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.934 MB | 6.934 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python | 4573 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 34.637 MB | 34.637 MB | 41.988 MB | 41.988 MB | n/a MB | n/a MB |
| sh | 4574 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4575 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.363 MB | 21.363 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| python | 4588 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 75.482% | 75.482% | 0.760 s | 35.363 MB | 61.242 MB | 44.732 MB | 75.953 MB | n/a MB | n/a MB |
| python3 | 4596 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.160 MB | 21.160 MB | 25.707 MB | 25.707 MB | n/a MB | n/a MB |
| sh | 4595 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 4598 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 61.238 MB | 61.238 MB | 75.910 MB | 75.910 MB | n/a MB | n/a MB |
| bash | 4597 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.863 MB | 2.863 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 4613 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 37.137 MB | 37.137 MB | 45.656 MB | 45.656 MB | n/a MB | n/a MB |
| python3 | 4615 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.828 MB | 8.828 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 4614 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 4626 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4627 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.262 MB | 21.262 MB | 27.066 MB | 27.066 MB | n/a MB | n/a MB |
| python | 4630 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 10.895 MB | 10.895 MB | 14.906 MB | 14.906 MB | n/a MB | n/a MB |
| bash | 4629 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.715 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 4631 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 17.846% | 17.846% | 0.180 s | 62.178 MB | 66.098 MB | 76.500 MB | 80.141 MB | n/a MB | n/a MB |
| python | 4657 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 11.121 MB | 11.121 MB | 14.898 MB | 14.898 MB | n/a MB | n/a MB |
| python | 4658 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.106% | 61.106% | 0.620 s | 50.621 MB | 66.016 MB | 62.092 MB | 80.148 MB | n/a MB | n/a MB |
| bash | 4656 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.719 MB | 2.719 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 4675 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4676 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.270 MB | 21.270 MB | 26.980 MB | 26.980 MB | n/a MB | n/a MB |
| sh | 4683 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4684 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.238 MB | 17.238 MB | 22.141 MB | 22.141 MB | n/a MB | n/a MB |
| sleep | 4689 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 4692 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.805 MB | 2.805 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 4693 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 0.165% | 0.992% | 0.010 s | 11.160 MB | 11.160 MB | 14.915 MB | 14.918 MB | n/a MB | n/a MB |
| python | 4694 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 47.685% | 47.685% | 0.480 s | 52.482 MB | 66.363 MB | 63.719 MB | 80.145 MB | n/a MB | n/a MB |
| python | 4711 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 34.762% | 34.762% | 0.350 s | 55.963 MB | 66.562 MB | 67.410 MB | 81.414 MB | n/a MB | n/a MB |
| python | 4728 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 49.863 MB | 49.863 MB | 57.797 MB | 57.797 MB | n/a MB | n/a MB |
| python | 4745 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 71.357% | 71.357% | 0.720 s | 41.885 MB | 66.121 MB | 51.834 MB | 79.887 MB | n/a MB | n/a MB |
| python | 4771 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 46.066 MB | 46.066 MB | 54.660 MB | 54.660 MB | n/a MB | n/a MB |
| bash | 4769 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.793 MB | 2.793 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 4770 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 11.215 MB | 11.215 MB | 14.910 MB | 14.910 MB | n/a MB | n/a MB |
| python | 4788 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 77.505% | 77.505% | 0.780 s | 35.100 MB | 61.855 MB | 45.123 MB | 77.090 MB | n/a MB | n/a MB |
| python | 4813 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 11.027 MB | 11.027 MB | 14.906 MB | 14.906 MB | n/a MB | n/a MB |
| bash | 4812 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.629 MB | 2.629 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 4814 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 77.272% | 77.272% | 0.780 s | 40.846 MB | 64.020 MB | 51.252 MB | 78.738 MB | n/a MB | n/a MB |
| python | 4832 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.406% | 63.406% | 0.640 s | 45.998 MB | 66.086 MB | 56.068 MB | 80.148 MB | n/a MB | n/a MB |
| python | 4850 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 36.763% | 36.763% | 0.370 s | 55.088 MB | 66.551 MB | 66.482 MB | 81.395 MB | n/a MB | n/a MB |
| python | 4867 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 52.246 MB | 52.246 MB | 61.332 MB | 61.332 MB | n/a MB | n/a MB |
| python3 | 4885 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.664 MB | 8.664 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 4884 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 4892 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 4894 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 75.266% | 75.266% | 0.760 s | 41.021 MB | 65.734 MB | 50.957 MB | 79.574 MB | n/a MB | n/a MB |
| python | 4893 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 10.816 MB | 10.816 MB | 14.949 MB | 14.949 MB | n/a MB | n/a MB |
| python | 4913 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.438% | 57.438% | 0.580 s | 49.062 MB | 65.922 MB | 60.762 MB | 80.129 MB | n/a MB | n/a MB |
| sh | 4937 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4938 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.414 MB | 7.414 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| python | 4947 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 15.628% | 62.513% | 0.630 s | 59.066 MB | 66.066 MB | 72.412 MB | 80.160 MB | n/a MB | n/a MB |
| python | 4946 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 10.520 MB | 10.520 MB | 14.938 MB | 14.938 MB | n/a MB | n/a MB |
| bash | 4945 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.840 MB | 2.840 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 4953 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 5080 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.539% | 71.573% | 2.620 s | 359.364 MB | 385.559 MB | 8782.948 MB | 10206.898 MB | n/a MB | n/a MB |
| MainThread | 5108 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 277.469 MB | 277.469 MB | 1672.793 MB | 1672.793 MB | n/a MB | n/a MB |
| sh | 5122 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5123 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.055 MB | 7.055 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 5127 | sandbox_agent_lsb-kimi_0000_0000 | 26 | 13.214% | 71.469% | 3.330 s | 374.281 MB | 386.465 MB | 9552.260 MB | 10209.863 MB | n/a MB | n/a MB |
| MainThread | 5186 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 290.320 MB | 290.320 MB | 1685.293 MB | 1685.293 MB | n/a MB | n/a MB |
| gzip | 5199 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| tar | 5198 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.203 MB | 2.203 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| python3 | 5220 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.270 MB | 7.270 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 5219 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 5226 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.672 MB | 2.672 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 5227 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.094 MB | 13.094 MB | 207.207 MB | 207.207 MB | n/a MB | n/a MB |
| MainThread | 5241 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 18.327% | 68.460% | 2.770 s | 363.441 MB | 384.258 MB | 9136.627 MB | 10206.707 MB | n/a MB | n/a MB |
| MainThread | 5261 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.484% | 62.484% | 0.630 s | 208.994 MB | 256.922 MB | 1485.650 MB | 1653.578 MB | n/a MB | n/a MB |
| sleep | 5285 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 5291 | sandbox_agent_lsb-kimi_0000_0000 | 89 | 5.638% | 89.330% | 5.000 s | 381.487 MB | 387.379 MB | 10114.743 MB | 10215.023 MB | n/a MB | n/a MB |
| MainThread | 5319 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 91.453% | 91.453% | 0.920 s | 199.588 MB | 302.805 MB | 1505.432 MB | 1727.168 MB | n/a MB | n/a MB |
| tar | 5331 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.191 MB | 2.191 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 5332 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| bash | 5345 | sandbox_agent_lsb-kimi_0000_0000 | 46 | 0.000% | 0.000% | 0.000 s | 2.570 MB | 2.570 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 5346 | sandbox_agent_lsb-kimi_0000_0000 | 45 | 129.070% | 174.930% | 57.270 s | 1575.142 MB | 2050.504 MB | 1795.654 MB | 2307.473 MB | n/a MB | n/a MB |
| sleep | 5353 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 5366 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.754 MB | 2.754 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 5368 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.568% | 61.568% | 0.620 s | 51.992 MB | 66.613 MB | 63.607 MB | 81.426 MB | n/a MB | n/a MB |
| python | 5367 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 10.539 MB | 10.539 MB | 14.938 MB | 14.938 MB | n/a MB | n/a MB |
| python | 5457 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 11.587% | 34.760% | 0.350 s | 60.646 MB | 66.062 MB | 73.366 MB | 80.164 MB | n/a MB | n/a MB |
| python | 5456 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 11.129 MB | 11.129 MB | 14.938 MB | 14.938 MB | n/a MB | n/a MB |
| bash | 5455 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.691 MB | 2.691 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 5468 | sandbox_agent_lsb-kimi_0000_0000 | 30 | 11.485% | 83.457% | 3.360 s | 372.988 MB | 389.391 MB | 9614.695 MB | 10186.246 MB | n/a MB | n/a MB |
| sh | 5485 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5486 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.453 MB | 9.453 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| MainThread | 5498 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 278.219 MB | 278.219 MB | 1673.047 MB | 1673.047 MB | n/a MB | n/a MB |
| bash | 5514 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 5515 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 11.115 MB | 11.172 MB | 14.909 MB | 14.938 MB | n/a MB | n/a MB |
| python | 5516 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 60.004 MB | 60.004 MB | 74.383 MB | 74.383 MB | n/a MB | n/a MB |
| python | 5517 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 69.458% | 69.458% | 0.700 s | 45.695 MB | 65.641 MB | 55.842 MB | 79.863 MB | n/a MB | n/a MB |
| python | 5518 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.659% | 51.659% | 0.520 s | 52.963 MB | 66.418 MB | 64.680 MB | 81.383 MB | n/a MB | n/a MB |
| python | 5519 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 60.828 MB | 60.828 MB | 75.781 MB | 75.781 MB | n/a MB | n/a MB |
| python | 5520 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.455% | 59.455% | 0.600 s | 50.777 MB | 65.996 MB | 62.625 MB | 81.117 MB | n/a MB | n/a MB |
| python | 5531 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.458% | 66.458% | 0.670 s | 45.523 MB | 66.012 MB | 55.873 MB | 80.117 MB | n/a MB | n/a MB |
| bash | 5529 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.809 MB | 2.809 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 5530 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 10.812 MB | 10.812 MB | 14.918 MB | 14.918 MB | n/a MB | n/a MB |
| python | 5532 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 43.685% | 43.685% | 0.440 s | 54.635 MB | 66.227 MB | 66.398 MB | 81.387 MB | n/a MB | n/a MB |
| sleep | 5539 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 5545 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 14.881% | 62.479% | 2.550 s | 373.775 MB | 386.637 MB | 9726.803 MB | 10209.625 MB | n/a MB | n/a MB |
| python3 | 5567 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.570 MB | 8.570 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 5566 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 5570 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 193.367 MB | 193.367 MB | 1614.723 MB | 1614.723 MB | n/a MB | n/a MB |
| bash | 5590 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.879 MB | 2.879 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 5591 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 24.539 MB | 24.539 MB | 215.965 MB | 215.965 MB | n/a MB | n/a MB |
| MainThread | 5606 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.531% | 71.319% | 2.690 s | 367.796 MB | 389.742 MB | 8985.847 MB | 10208.527 MB | n/a MB | n/a MB |
| stty | 5622 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| MainThread | 5628 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.611% | 66.611% | 0.670 s | 242.537 MB | 296.336 MB | 1642.346 MB | 1690.719 MB | n/a MB | n/a MB |
| MainThread | 5654 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 26.251% | 73.484% | 2.910 s | 364.599 MB | 387.113 MB | 9483.201 MB | 10212.148 MB | n/a MB | n/a MB |
| MainThread | 5682 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 294.328 MB | 294.328 MB | 1688.574 MB | 1688.574 MB | n/a MB | n/a MB |
| sh | 5701 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.418 MB | 1.418 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5702 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.344 MB | 20.344 MB | 25.320 MB | 25.320 MB | n/a MB | n/a MB |
| MainThread | 5713 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 38.388% | 68.625% | 2.340 s | 349.744 MB | 381.516 MB | 8956.232 MB | 10206.145 MB | n/a MB | n/a MB |
| MainThread | 5733 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.450% | 67.450% | 0.680 s | 228.541 MB | 278.863 MB | 1632.395 MB | 1673.566 MB | n/a MB | n/a MB |
| sh | 5745 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.383 MB | 1.383 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5746 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.043 MB | 8.043 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| MainThread | 5762 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 23.981% | 62.521% | 2.440 s | 362.627 MB | 386.535 MB | 9411.327 MB | 10207.816 MB | n/a MB | n/a MB |
| MainThread | 5781 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.154% | 59.154% | 0.600 s | 213.672 MB | 260.625 MB | 1617.547 MB | 1657.121 MB | n/a MB | n/a MB |
| python3 | 5794 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.980 MB | 9.980 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 5793 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 5803 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 5811 | sandbox_agent_lsb-kimi_0000_0000 | 10 | 28.892% | 77.525% | 2.630 s | 347.548 MB | 385.945 MB | 8490.721 MB | 10203.547 MB | n/a MB | n/a MB |
| MainThread | 5839 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.285 MB | 229.285 MB | 1631.961 MB | 1631.961 MB | n/a MB | n/a MB |
| MainThread | 5858 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 30.109% | 67.787% | 2.130 s | 356.114 MB | 385.992 MB | 9121.569 MB | 10206.566 MB | n/a MB | n/a MB |
| sh | 5880 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| MainThread | 5887 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 189.262 MB | 189.262 MB | 1594.223 MB | 1594.223 MB | n/a MB | n/a MB |
| MainThread | 5906 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 34.169% | 73.500% | 2.410 s | 352.407 MB | 387.016 MB | 8076.461 MB | 10210.762 MB | n/a MB | n/a MB |
| MainThread | 5927 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 210.379 MB | 210.379 MB | 1621.160 MB | 1621.160 MB | n/a MB | n/a MB |
| MainThread | 5953 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 22.706% | 61.513% | 1.600 s | 359.008 MB | 384.535 MB | 9095.322 MB | 10185.602 MB | n/a MB | n/a MB |
| MainThread | 5981 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 187.453 MB | 187.453 MB | 1593.973 MB | 1593.973 MB | n/a MB | n/a MB |
| MainThread | 6000 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 29.927% | 61.471% | 1.810 s | 354.439 MB | 378.047 MB | 8964.350 MB | 10199.676 MB | n/a MB | n/a MB |
| sh | 6029 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 6019 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.426% | 58.426% | 0.590 s | 225.234 MB | 262.059 MB | 1625.637 MB | 1657.301 MB | n/a MB | n/a MB |
| python3 | 6030 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.785 MB | 6.785 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 6045 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 42.703% | 88.387% | 2.580 s | 336.712 MB | 383.512 MB | 7755.180 MB | 10202.500 MB | n/a MB | n/a MB |
| kimi-code | 6076 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 48.027 MB | 48.027 MB | 860.820 MB | 860.820 MB | n/a MB | n/a MB |
| MainThread | 6064 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.638% | 58.638% | 0.590 s | 265.562 MB | 302.090 MB | 1679.195 MB | 1726.395 MB | n/a MB | n/a MB |
| kimi | 6092 | sandbox_agent_lsb-kimi_0000_0000 | 48 | 7.857% | 97.328% | 3.720 s | 372.819 MB | 386.180 MB | 9810.117 MB | 10204.211 MB | n/a MB | n/a MB |
| sleep | 6108 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 6113 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.605% | 55.605% | 0.560 s | 224.385 MB | 261.242 MB | 1625.021 MB | 1656.070 MB | n/a MB | n/a MB |
| bash | 6138 | sandbox_agent_lsb-kimi_0000_0000 | 32 | 0.000% | 0.000% | 0.000 s | 2.711 MB | 2.711 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 6139 | sandbox_agent_lsb-kimi_0000_0000 | 32 | 172.461% | 176.362% | 53.920 s | 112.218 MB | 163.141 MB | 329.987 MB | 378.891 MB | n/a MB | n/a MB |
| MainThread | 6173 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 23.876% | 92.430% | 2.410 s | 346.169 MB | 384.242 MB | 8618.488 MB | 10204.938 MB | n/a MB | n/a MB |
| MainThread | 6202 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 160.918 MB | 160.918 MB | 1317.723 MB | 1317.723 MB | n/a MB | n/a MB |
| MainThread | 6221 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 31.365% | 69.584% | 1.580 s | 353.179 MB | 383.438 MB | 8759.614 MB | 10204.020 MB | n/a MB | n/a MB |
| python3 | 6246 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.902 MB | 8.902 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 6245 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 6239 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 6253 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 159.781 MB | 159.781 MB | 1500.219 MB | 1500.219 MB | n/a MB | n/a MB |
| MainThread | 6272 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 42.299% | 93.339% | 2.570 s | 308.480 MB | 370.004 MB | 7704.366 MB | 10202.027 MB | n/a MB | n/a MB |
| sh | 6296 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6297 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.648 MB | 8.648 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| kimi | 6298 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.262% | 65.262% | 0.670 s | 119.574 MB | 239.148 MB | 899.373 MB | 1638.602 MB | n/a MB | n/a MB |
| MainThread | 6318 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 39.345% | 89.277% | 2.380 s | 348.294 MB | 379.848 MB | 7794.886 MB | 10208.680 MB | n/a MB | n/a MB |
| MainThread | 6346 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 89.436% | 89.436% | 0.900 s | 228.119 MB | 302.578 MB | 1521.598 MB | 1727.227 MB | n/a MB | n/a MB |
| MainThread | 6365 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 36.894% | 64.502% | 1.860 s | 351.144 MB | 376.746 MB | 8758.312 MB | 10199.215 MB | n/a MB | n/a MB |
| MainThread | 6384 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.432% | 56.432% | 0.570 s | 228.049 MB | 269.145 MB | 1629.516 MB | 1665.309 MB | n/a MB | n/a MB |
| MainThread | 6411 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 35.106% | 68.425% | 2.480 s | 345.867 MB | 385.801 MB | 8068.739 MB | 10207.641 MB | n/a MB | n/a MB |
| MainThread | 6433 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 71.322% | 71.322% | 0.720 s | 248.346 MB | 302.648 MB | 1670.807 MB | 1727.141 MB | n/a MB | n/a MB |
| MainThread | 6457 | sandbox_agent_lsb-kimi_0000_0000 | 26 | 11.845% | 67.522% | 3.020 s | 374.820 MB | 387.570 MB | 9546.382 MB | 10205.207 MB | n/a MB | n/a MB |
| MainThread | 6476 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.177% | 63.177% | 0.640 s | 203.586 MB | 253.996 MB | 1479.902 MB | 1650.566 MB | n/a MB | n/a MB |
| python | 6577 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 10.926 MB | 10.926 MB | 14.934 MB | 14.934 MB | n/a MB | n/a MB |
| python | 6578 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.634% | 54.634% | 0.550 s | 51.955 MB | 66.145 MB | 63.025 MB | 80.117 MB | n/a MB | n/a MB |
| bash | 6576 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 2.648 MB | 2.648 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 6579 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 42.702% | 42.702% | 0.430 s | 55.709 MB | 66.281 MB | 67.381 MB | 81.383 MB | n/a MB | n/a MB |
| python | 6580 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 59.141 MB | 59.141 MB | 74.238 MB | 74.238 MB | n/a MB | n/a MB |
| python | 6581 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 72.338% | 72.338% | 0.730 s | 42.232 MB | 65.117 MB | 52.387 MB | 79.555 MB | n/a MB | n/a MB |
| python | 6582 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 48.536% | 48.536% | 0.600 s | 49.891 MB | 65.938 MB | 61.297 MB | 79.863 MB | n/a MB | n/a MB |
| python | 6583 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.454% | 61.454% | 0.620 s | 48.787 MB | 66.070 MB | 60.625 MB | 80.117 MB | n/a MB | n/a MB |
| python | 6584 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 40.662% | 40.662% | 0.410 s | 56.020 MB | 66.535 MB | 66.922 MB | 80.387 MB | n/a MB | n/a MB |
| python | 6585 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 59.605 MB | 59.605 MB | 74.234 MB | 74.234 MB | n/a MB | n/a MB |
| sleep | 6592 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 6598 | sandbox_agent_lsb-kimi_0000_0000 | 21 | 12.496% | 65.563% | 2.520 s | 378.357 MB | 389.605 MB | 9791.526 MB | 10204.496 MB | n/a MB | n/a MB |
| MainThread | 6620 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 45.468% | 45.468% | 0.460 s | 187.764 MB | 229.551 MB | 1466.988 MB | 1632.242 MB | n/a MB | n/a MB |
| python3 | 6627 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.582 MB | 10.582 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 6626 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 6644 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 10.746 MB | 10.746 MB | 14.941 MB | 14.941 MB | n/a MB | n/a MB |
| python | 6645 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 41.961 MB | 41.961 MB | 49.910 MB | 49.910 MB | n/a MB | n/a MB |
| bash | 6643 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.742 MB | 2.742 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 6646 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 61.164 MB | 61.164 MB | 75.781 MB | 75.781 MB | n/a MB | n/a MB |
| python | 6647 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.458% | 57.458% | 0.580 s | 51.398 MB | 66.176 MB | 62.262 MB | 80.125 MB | n/a MB | n/a MB |
| MainThread | 6660 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 36.491% | 63.268% | 1.840 s | 349.835 MB | 373.016 MB | 8758.052 MB | 10200.262 MB | n/a MB | n/a MB |
| MainThread | 6679 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.437% | 67.437% | 0.680 s | 234.230 MB | 280.328 MB | 1634.510 MB | 1675.047 MB | n/a MB | n/a MB |
| MainThread | 6706 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 36.570% | 67.476% | 2.220 s | 351.556 MB | 380.555 MB | 8946.376 MB | 10200.141 MB | n/a MB | n/a MB |
| MainThread | 6725 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.476% | 61.476% | 0.620 s | 215.611 MB | 260.586 MB | 1618.012 MB | 1656.301 MB | n/a MB | n/a MB |
| kimi-code | 6750 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 56.586 MB | 56.586 MB | 899.430 MB | 899.430 MB | n/a MB | n/a MB |
| MainThread | 6753 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 35.289% | 70.496% | 2.490 s | 344.309 MB | 385.363 MB | 8063.345 MB | 10204.070 MB | n/a MB | n/a MB |
| MainThread | 6772 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.445% | 60.445% | 0.610 s | 129.404 MB | 229.543 MB | 939.453 MB | 1631.605 MB | n/a MB | n/a MB |
| sh | 6770 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6771 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.305 MB | 9.305 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 6784 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6785 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.473 MB | 7.473 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 6800 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 43.683% | 95.388% | 3.080 s | 312.472 MB | 374.172 MB | 7889.896 MB | 10208.223 MB | n/a MB | n/a MB |
| sh | 6822 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.609 MB | 1.609 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6823 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.227 MB | 10.227 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 6827 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 187.477 MB | 187.477 MB | 1593.973 MB | 1593.973 MB | n/a MB | n/a MB |
| MainThread | 6846 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 41.873% | 72.500% | 2.110 s | 338.852 MB | 377.051 MB | 7361.656 MB | 10202.438 MB | n/a MB | n/a MB |
| MainThread | 6874 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 93.297% | 93.297% | 0.940 s | 168.568 MB | 301.945 MB | 1447.371 MB | 1726.328 MB | n/a MB | n/a MB |
| sleep | 6883 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 6893 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 52.157% | 91.422% | 2.630 s | 319.293 MB | 374.656 MB | 7305.921 MB | 10203.051 MB | n/a MB | n/a MB |
| sh | 6917 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6918 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.270 MB | 7.270 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 6919 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.566 MB | 228.566 MB | 1635.121 MB | 1635.121 MB | n/a MB | n/a MB |
| MainThread | 6941 | sandbox_agent_lsb-kimi_0000_0000 | 22 | 15.918% | 97.322% | 3.370 s | 362.823 MB | 388.340 MB | 9401.038 MB | 10204.684 MB | n/a MB | n/a MB |
| MainThread | 6960 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.445% | 59.445% | 0.600 s | 230.842 MB | 272.457 MB | 1631.391 MB | 1668.309 MB | n/a MB | n/a MB |
| sh | 6970 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6971 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.516 MB | 8.516 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 6983 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6984 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.520 MB | 19.520 MB | 24.934 MB | 24.934 MB | n/a MB | n/a MB |
| python | 6986 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 10.812 MB | 10.812 MB | 14.996 MB | 14.996 MB | n/a MB | n/a MB |
| python | 6987 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 7.593% | 22.779% | 0.230 s | 61.924 MB | 65.906 MB | 74.862 MB | 80.156 MB | n/a MB | n/a MB |
| bash | 6985 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.703 MB | 2.703 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 6990 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 30.760% | 30.760% | 0.310 s | 55.730 MB | 66.238 MB | 66.795 MB | 80.117 MB | n/a MB | n/a MB |
| python | 6991 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 70.516% | 70.516% | 0.710 s | 42.904 MB | 66.254 MB | 52.699 MB | 79.859 MB | n/a MB | n/a MB |
| MainThread | 7002 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 41.786% | 73.342% | 2.110 s | 340.710 MB | 375.953 MB | 7384.213 MB | 10200.012 MB | n/a MB | n/a MB |
| MainThread | 7023 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 205.973 MB | 205.973 MB | 1619.016 MB | 1619.016 MB | n/a MB | n/a MB |
| MainThread | 7047 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 22.014% | 95.265% | 3.330 s | 354.845 MB | 390.156 MB | 9108.829 MB | 10208.980 MB | n/a MB | n/a MB |
| MainThread | 7066 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 68.340% | 68.340% | 0.690 s | 232.846 MB | 280.688 MB | 1634.154 MB | 1675.336 MB | n/a MB | n/a MB |
| python3 | 7095 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.008 MB | 21.008 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| sh | 7094 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7109 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7110 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.355 MB | 9.355 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| MainThread | 7119 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 41.510% | 73.410% | 2.510 s | 338.828 MB | 382.254 MB | 7759.130 MB | 10205.871 MB | n/a MB | n/a MB |
| MainThread | 7138 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.377% | 59.377% | 0.600 s | 259.918 MB | 297.316 MB | 1675.248 MB | 1724.504 MB | n/a MB | n/a MB |
| sleep | 7162 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 7168 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 36.339% | 67.497% | 1.830 s | 354.189 MB | 383.059 MB | 8765.446 MB | 10207.832 MB | n/a MB | n/a MB |
| python3 | 7198 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.984 MB | 6.984 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 7197 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 7210 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 48.821% | 82.399% | 2.950 s | 332.540 MB | 381.328 MB | 7762.769 MB | 10210.797 MB | n/a MB | n/a MB |
| python3 | 7232 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.695 MB | 8.695 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 7231 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 7243 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 45.584% | 72.550% | 2.310 s | 338.213 MB | 376.117 MB | 7356.701 MB | 10207.500 MB | n/a MB | n/a MB |
| MainThread | 7262 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.316% | 60.316% | 0.610 s | 172.896 MB | 235.793 MB | 1460.258 MB | 1636.820 MB | n/a MB | n/a MB |
| python3 | 7275 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.949 MB | 8.949 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 7274 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 7290 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 40.106% | 72.582% | 2.020 s | 346.513 MB | 378.199 MB | 8756.130 MB | 10204.621 MB | n/a MB | n/a MB |
| MainThread | 7313 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 199.953 MB | 199.953 MB | 1617.484 MB | 1617.484 MB | n/a MB | n/a MB |
| MainThread | 7335 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 41.199% | 71.597% | 2.490 s | 338.132 MB | 377.105 MB | 7759.617 MB | 10204.695 MB | n/a MB | n/a MB |
| MainThread | 7355 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.560% | 59.560% | 0.600 s | 266.252 MB | 303.445 MB | 1679.543 MB | 1727.379 MB | n/a MB | n/a MB |
| MainThread | 7381 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 42.113% | 75.565% | 2.120 s | 340.298 MB | 375.285 MB | 7385.519 MB | 10204.414 MB | n/a MB | n/a MB |
| MainThread | 7407 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 166.824 MB | 166.824 MB | 1577.723 MB | 1577.723 MB | n/a MB | n/a MB |
| MainThread | 7426 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 38.928% | 74.534% | 1.960 s | 348.385 MB | 376.715 MB | 8760.228 MB | 10204.148 MB | n/a MB | n/a MB |
| MainThread | 7454 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 166.828 MB | 166.828 MB | 1577.973 MB | 1577.973 MB | n/a MB | n/a MB |
| kimi-code | 7466 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 52.531 MB | 52.531 MB | 904.129 MB | 904.129 MB | n/a MB | n/a MB |
| MainThread | 7471 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 18.787% | 71.567% | 2.840 s | 369.089 MB | 392.789 MB | 9138.208 MB | 10209.094 MB | n/a MB | n/a MB |
| MainThread | 7490 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.519% | 61.519% | 0.620 s | 160.375 MB | 235.559 MB | 1460.033 MB | 1636.371 MB | n/a MB | n/a MB |
| sleep | 7514 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 7515 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7516 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.867 MB | 20.867 MB | 25.578 MB | 25.578 MB | n/a MB | n/a MB |
| MainThread | 7534 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 14.937% | 79.453% | 2.860 s | 376.203 MB | 399.715 MB | 9344.948 MB | 10202.367 MB | n/a MB | n/a MB |
| python3 | 7558 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.043 MB | 8.043 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 7557 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 7562 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 184.945 MB | 184.945 MB | 1593.223 MB | 1593.223 MB | n/a MB | n/a MB |
| sh | 7576 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7577 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.516 MB | 16.516 MB | 21.844 MB | 21.844 MB | n/a MB | n/a MB |
| bash | 7578 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.809 MB | 2.809 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 7579 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 150.502% | 153.875% | 3.030 s | 86.987 MB | 111.398 MB | 306.276 MB | 330.859 MB | n/a MB | n/a MB |
| MainThread | 7610 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 37.168% | 70.138% | 2.250 s | 346.379 MB | 382.738 MB | 7762.286 MB | 10200.969 MB | n/a MB | n/a MB |
| MainThread | 7629 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.624% | 52.624% | 0.530 s | 197.090 MB | 235.859 MB | 1568.533 MB | 1637.098 MB | n/a MB | n/a MB |
| sh | 7641 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7642 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.535 MB | 8.535 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| python3 | 7653 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.355 MB | 9.355 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 7652 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 7657 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 16.407% | 72.428% | 2.810 s | 370.324 MB | 390.949 MB | 9256.510 MB | 10208.887 MB | n/a MB | n/a MB |
| MainThread | 7676 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.525% | 58.525% | 0.590 s | 263.010 MB | 296.707 MB | 1661.471 MB | 1690.969 MB | n/a MB | n/a MB |
| MainThread | 7704 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 29.025% | 68.446% | 2.050 s | 362.005 MB | 388.539 MB | 9120.477 MB | 10204.711 MB | n/a MB | n/a MB |
| MainThread | 7724 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.499% | 66.499% | 0.670 s | 223.494 MB | 271.738 MB | 1628.398 MB | 1666.574 MB | n/a MB | n/a MB |
| kimi-code | 7754 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 28.778% | 67.479% | 1.450 s | 355.342 MB | 378.910 MB | 8767.839 MB | 10197.637 MB | n/a MB | n/a MB |
| sleep | 7764 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 7784 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 144.020 MB | 144.020 MB | 1299.805 MB | 1299.805 MB | n/a MB | n/a MB |
| MainThread | 7803 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 45.475% | 93.256% | 2.750 s | 311.120 MB | 385.090 MB | 7688.887 MB | 10208.574 MB | n/a MB | n/a MB |
| sh | 7825 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7826 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.137 MB | 10.137 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 7834 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 214.895 MB | 214.895 MB | 1622.973 MB | 1622.973 MB | n/a MB | n/a MB |
| MainThread | 7851 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 20.154% | 70.550% | 2.260 s | 363.461 MB | 383.930 MB | 9475.433 MB | 10204.680 MB | n/a MB | n/a MB |
| MainThread | 7870 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 68.055% | 68.055% | 0.690 s | 211.760 MB | 262.398 MB | 1578.777 MB | 1657.086 MB | n/a MB | n/a MB |
| MainThread | 7898 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 30.079% | 75.525% | 2.120 s | 360.405 MB | 390.184 MB | 9123.706 MB | 10208.965 MB | n/a MB | n/a MB |
| MainThread | 7921 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 44.666% | 44.666% | 0.450 s | 171.344 MB | 228.809 MB | 1457.811 MB | 1631.926 MB | n/a MB | n/a MB |
| MainThread | 7945 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.003% | 71.596% | 2.550 s | 364.800 MB | 392.102 MB | 8781.160 MB | 10207.398 MB | n/a MB | n/a MB |
| sh | 7962 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 7964 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.443% | 61.443% | 0.620 s | 141.877 MB | 235.480 MB | 1437.598 MB | 1636.586 MB | n/a MB | n/a MB |
| python3 | 7963 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.945 MB | 8.945 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 7992 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 23.772% | 70.492% | 2.400 s | 357.941 MB | 383.344 MB | 8664.443 MB | 10207.914 MB | n/a MB | n/a MB |
| MainThread | 8094 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 76.354% | 76.354% | 0.780 s | 223.994 MB | 294.012 MB | 1594.381 MB | 1689.293 MB | n/a MB | n/a MB |
| MainThread | 8116 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 17.431% | 67.491% | 1.930 s | 363.067 MB | 385.883 MB | 8785.264 MB | 10191.180 MB | n/a MB | n/a MB |
| sleep | 8126 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 8147 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 160.086 MB | 160.086 MB | 1316.840 MB | 1316.840 MB | n/a MB | n/a MB |
| MainThread | 8166 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 42.279% | 82.322% | 2.130 s | 351.559 MB | 377.020 MB | 8763.417 MB | 10208.254 MB | n/a MB | n/a MB |
| sh | 8189 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8190 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.715 MB | 9.715 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| MainThread | 8196 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 237.562 MB | 237.562 MB | 1637.324 MB | 1637.324 MB | n/a MB | n/a MB |
| MainThread | 8213 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 17.234% | 61.648% | 1.910 s | 369.439 MB | 386.227 MB | 9482.662 MB | 10203.594 MB | n/a MB | n/a MB |
| sh | 8242 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 8232 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.403% | 61.403% | 0.620 s | 233.441 MB | 279.336 MB | 1634.086 MB | 1674.199 MB | n/a MB | n/a MB |
| python3 | 8243 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.746 MB | 10.746 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 8260 | sandbox_agent_lsb-kimi_0000_0000 | 24 | 13.476% | 83.901% | 3.130 s | 376.938 MB | 391.836 MB | 9500.335 MB | 10210.285 MB | n/a MB | n/a MB |
| sh | 8279 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8280 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.691 MB | 10.691 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 8285 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8286 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.562 MB | 9.562 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| MainThread | 8291 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 295.367 MB | 295.367 MB | 1690.000 MB | 1690.000 MB | n/a MB | n/a MB |
| bash | 8309 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.766 MB | 2.766 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 8310 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.438 MB | 21.438 MB | 213.723 MB | 213.723 MB | n/a MB | n/a MB |
| kimi | 8325 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 40.504% | 91.154% | 2.860 s | 312.870 MB | 383.168 MB | 7869.741 MB | 10203.719 MB | n/a MB | n/a MB |
| sleep | 8345 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 8348 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.488 MB | 1.488 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 8349 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.488 MB | 1.488 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 8355 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 171.727 MB | 171.727 MB | 1579.473 MB | 1579.473 MB | n/a MB | n/a MB |
| MainThread | 8374 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.394% | 76.082% | 3.030 s | 361.484 MB | 383.387 MB | 9062.776 MB | 10202.934 MB | n/a MB | n/a MB |
| MainThread | 8402 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 160.320 MB | 160.320 MB | 1316.840 MB | 1316.840 MB | n/a MB | n/a MB |
| MainThread | 8421 | sandbox_agent_lsb-kimi_0000_0000 | 23 | 12.911% | 70.464% | 2.860 s | 378.292 MB | 392.871 MB | 9463.564 MB | 10208.488 MB | n/a MB | n/a MB |
| MainThread | 8445 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 207.258 MB | 207.258 MB | 1619.465 MB | 1619.465 MB | n/a MB | n/a MB |
| gzip | 8465 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| tar | 8464 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.133 MB | 2.133 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| sh | 8466 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8467 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.230 MB | 15.230 MB | 20.242 MB | 20.242 MB | n/a MB | n/a MB |
| MainThread | 8482 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 33.046% | 77.454% | 2.330 s | 356.603 MB | 393.680 MB | 8089.350 MB | 10212.215 MB | n/a MB | n/a MB |
| MainThread | 8506 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 208.250 MB | 208.250 MB | 1619.465 MB | 1619.465 MB | n/a MB | n/a MB |
| MainThread | 8532 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 24.794% | 77.558% | 2.500 s | 363.844 MB | 387.594 MB | 9399.942 MB | 10210.434 MB | n/a MB | n/a MB |
| MainThread | 8553 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 68.069% | 68.069% | 0.690 s | 236.928 MB | 294.207 MB | 1640.012 MB | 1688.801 MB | n/a MB | n/a MB |
| sh | 8563 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8564 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.980 MB | 8.980 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sleep | 8573 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 8581 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 20.845% | 78.381% | 2.100 s | 366.685 MB | 390.156 MB | 9398.070 MB | 10184.176 MB | n/a MB | n/a MB |
| MainThread | 8618 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.409% | 86.261% | 3.080 s | 356.477 MB | 390.777 MB | 8876.016 MB | 10209.172 MB | n/a MB | n/a MB |
| MainThread | 8637 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.440% | 59.440% | 0.600 s | 235.615 MB | 277.566 MB | 1643.529 MB | 1673.086 MB | n/a MB | n/a MB |
| MainThread | 8666 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 38.311% | 73.598% | 2.700 s | 344.032 MB | 388.191 MB | 8066.019 MB | 10209.918 MB | n/a MB | n/a MB |
| sh | 8696 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8697 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.102 MB | 10.102 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 8686 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.430% | 57.430% | 0.580 s | 262.900 MB | 296.352 MB | 1661.527 MB | 1690.820 MB | n/a MB | n/a MB |
| MainThread | 8712 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.922% | 79.369% | 2.430 s | 367.384 MB | 389.676 MB | 9478.321 MB | 10208.801 MB | n/a MB | n/a MB |
| MainThread | 8734 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 196.480 MB | 196.480 MB | 1616.480 MB | 1616.480 MB | n/a MB | n/a MB |
| MainThread | 8760 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.401% | 75.382% | 2.710 s | 368.331 MB | 394.324 MB | 8899.218 MB | 10216.996 MB | n/a MB | n/a MB |
| sh | 8779 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8780 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.934 MB | 8.934 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| python3 | 8794 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sh | 8793 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 8783 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.461% | 54.461% | 0.550 s | 235.887 MB | 278.320 MB | 1643.770 MB | 1673.316 MB | n/a MB | n/a MB |
| sleep | 8803 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 8811 | sandbox_agent_lsb-kimi_0000_0000 | 25 | 12.207% | 72.518% | 2.950 s | 379.641 MB | 394.020 MB | 9525.863 MB | 10211.680 MB | n/a MB | n/a MB |
| MainThread | 8832 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.519% | 63.519% | 0.640 s | 205.992 MB | 256.227 MB | 1481.668 MB | 1651.582 MB | n/a MB | n/a MB |
| python3 | 8856 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.977 MB | 15.977 MB | 20.602 MB | 20.602 MB | n/a MB | n/a MB |
| sh | 8855 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 8858 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.008 MB | 11.008 MB | 14.883 MB | 14.883 MB | n/a MB | n/a MB |
| python | 8859 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.746 MB | 50.746 MB | 59.133 MB | 59.133 MB | n/a MB | n/a MB |
| bash | 8857 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.879 MB | 2.879 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 8878 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.500 MB | 9.500 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sh | 8877 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 8906 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 33.004% | 70.357% | 1.670 s | 354.439 MB | 381.504 MB | 8761.980 MB | 10195.184 MB | n/a MB | n/a MB |
| MainThread | 8938 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 188.793 MB | 188.793 MB | 1594.223 MB | 1594.223 MB | n/a MB | n/a MB |
| MainThread | 8955 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.433% | 71.570% | 2.200 s | 370.790 MB | 388.887 MB | 9482.090 MB | 10209.039 MB | n/a MB | n/a MB |
| MainThread | 8974 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.656% | 57.656% | 0.580 s | 226.246 MB | 269.910 MB | 1629.029 MB | 1665.086 MB | n/a MB | n/a MB |
| sh | 8986 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8987 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.977 MB | 8.977 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 9002 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.527% | 90.301% | 2.960 s | 361.335 MB | 391.906 MB | 8963.227 MB | 10208.156 MB | n/a MB | n/a MB |
| MainThread | 9024 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.528% | 55.528% | 0.560 s | 209.660 MB | 252.754 MB | 1613.410 MB | 1648.848 MB | n/a MB | n/a MB |
| sh | 9031 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9032 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.898 MB | 9.898 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sleep | 9046 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 9053 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 25.032% | 94.375% | 3.280 s | 351.869 MB | 387.469 MB | 8959.030 MB | 10211.402 MB | n/a MB | n/a MB |
| python3 | 9078 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.703 MB | 10.703 MB | 14.730 MB | 14.730 MB | n/a MB | n/a MB |
| sh | 9077 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 9084 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 296.762 MB | 296.762 MB | 1691.566 MB | 1691.566 MB | n/a MB | n/a MB |
| sh | 9098 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9099 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.387 MB | 9.387 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| MainThread | 9103 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 40.287% | 81.267% | 2.840 s | 342.596 MB | 390.887 MB | 8061.425 MB | 10210.332 MB | n/a MB | n/a MB |
| MainThread | 9124 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.504% | 66.504% | 0.670 s | 241.393 MB | 288.793 MB | 1648.764 MB | 1683.055 MB | n/a MB | n/a MB |
| sh | 9145 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9146 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.270 MB | 9.270 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 9150 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.080% | 87.242% | 3.070 s | 359.852 MB | 390.344 MB | 8887.257 MB | 10211.750 MB | n/a MB | n/a MB |
| MainThread | 9169 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.502% | 67.502% | 0.680 s | 236.963 MB | 285.992 MB | 1637.416 MB | 1680.859 MB | n/a MB | n/a MB |
| MainThread | 9197 | sandbox_agent_lsb-kimi_0000_0000 | 29 | 12.116% | 79.222% | 3.430 s | 382.780 MB | 396.242 MB | 9621.754 MB | 10214.238 MB | n/a MB | n/a MB |
| MainThread | 9217 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.483% | 58.483% | 0.590 s | 257.689 MB | 296.723 MB | 1665.611 MB | 1707.238 MB | n/a MB | n/a MB |
| tar | 9234 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.242 MB | 2.242 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| sh | 9240 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9241 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.422 MB | 18.422 MB | 24.234 MB | 24.234 MB | n/a MB | n/a MB |
| bash | 9242 | sandbox_agent_lsb-kimi_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.555 MB | 2.555 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 9243 | sandbox_agent_lsb-kimi_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 11.172 MB | 11.172 MB | 14.941 MB | 14.941 MB | n/a MB | n/a MB |
| python | 9244 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 13.878% | 27.756% | 0.280 s | 60.279 MB | 66.375 MB | 72.197 MB | 80.148 MB | n/a MB | n/a MB |
| python | 9321 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 25.398% | 67.278% | 0.770 s | 56.413 MB | 66.902 MB | 68.386 MB | 81.410 MB | n/a MB | n/a MB |
| sleep | 9323 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 9324 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 9.438% | 18.876% | 0.190 s | 63.277 MB | 65.980 MB | 78.415 MB | 81.176 MB | n/a MB | n/a MB |
| MainThread | 9336 | sandbox_agent_lsb-kimi_0000_0000 | 29 | 10.382% | 78.491% | 2.930 s | 380.562 MB | 392.051 MB | 9625.181 MB | 10210.203 MB | n/a MB | n/a MB |
| MainThread | 9359 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 76.430% | 76.430% | 0.770 s | 241.766 MB | 303.055 MB | 1659.477 MB | 1727.730 MB | n/a MB | n/a MB |
| MainThread | 9398 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 22.239% | 72.408% | 2.240 s | 370.781 MB | 394.887 MB | 9416.539 MB | 10212.219 MB | n/a MB | n/a MB |
| MainThread | 9417 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.605% | 59.605% | 0.600 s | 215.963 MB | 261.637 MB | 1619.059 MB | 1658.645 MB | n/a MB | n/a MB |
| MainThread | 9445 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 36.881% | 72.547% | 2.240 s | 345.690 MB | 383.664 MB | 7763.118 MB | 10203.832 MB | n/a MB | n/a MB |
| MainThread | 9464 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.600% | 57.600% | 0.580 s | 206.346 MB | 254.746 MB | 1482.652 MB | 1650.625 MB | n/a MB | n/a MB |
| python3 | 9477 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.480 MB | 8.480 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 9476 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 9492 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 26.529% | 74.403% | 2.140 s | 361.295 MB | 390.621 MB | 9241.466 MB | 10210.516 MB | n/a MB | n/a MB |
| sleep | 9510 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 9522 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 158.176 MB | 158.176 MB | 1499.969 MB | 1499.969 MB | n/a MB | n/a MB |
| MainThread | 9541 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.745% | 90.201% | 2.980 s | 358.412 MB | 390.137 MB | 8956.259 MB | 10209.000 MB | n/a MB | n/a MB |
| MainThread | 9560 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.433% | 63.433% | 0.640 s | 239.445 MB | 285.254 MB | 1647.646 MB | 1680.820 MB | n/a MB | n/a MB |
| MainThread | 9589 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 25.719% | 84.282% | 2.850 s | 352.680 MB | 388.234 MB | 8769.463 MB | 10209.359 MB | n/a MB | n/a MB |
| python3 | 9619 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.094 MB | 9.094 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 9618 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 9611 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.516% | 51.516% | 0.520 s | 184.521 MB | 228.938 MB | 1466.100 MB | 1635.848 MB | n/a MB | n/a MB |
| MainThread | 9637 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 25.921% | 74.560% | 2.610 s | 362.913 MB | 388.344 MB | 8656.632 MB | 10212.746 MB | n/a MB | n/a MB |
| MainThread | 9656 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 56.555% | 61.500% | 1.140 s | 191.141 MB | 296.152 MB | 1520.533 MB | 1690.992 MB | n/a MB | n/a MB |
| python3 | 9655 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.895 MB | 8.895 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 9654 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 9684 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.566% | 83.451% | 2.690 s | 367.966 MB | 397.344 MB | 8979.427 MB | 10205.180 MB | n/a MB | n/a MB |
| sh | 9712 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9713 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.430 MB | 7.430 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 9705 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.622% | 55.622% | 0.560 s | 198.656 MB | 236.836 MB | 1477.350 MB | 1637.359 MB | n/a MB | n/a MB |
| sleep | 9730 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 9733 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 17.327% | 70.460% | 1.920 s | 375.124 MB | 396.184 MB | 9477.711 MB | 10195.445 MB | n/a MB | n/a MB |
| MainThread | 9763 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 193.836 MB | 193.836 MB | 1614.223 MB | 1614.223 MB | n/a MB | n/a MB |
| tar | 9775 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.969 MB | 1.969 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| tar | 9776 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.535 MB | 1.535 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| MainThread | 9782 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 24.107% | 73.398% | 3.160 s | 365.616 MB | 392.180 MB | 8984.413 MB | 10208.688 MB | n/a MB | n/a MB |
| kimi-code | 9795 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.520 MB | 16.520 MB | 706.961 MB | 706.961 MB | n/a MB | n/a MB |
| MainThread | 9801 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.474% | 56.474% | 0.570 s | 228.355 MB | 263.141 MB | 1636.506 MB | 1658.539 MB | n/a MB | n/a MB |
| MainThread | 9829 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 43.185% | 82.294% | 3.050 s | 348.041 MB | 389.289 MB | 8062.834 MB | 10206.859 MB | n/a MB | n/a MB |
| MainThread | 9852 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.480% | 53.480% | 0.540 s | 195.477 MB | 229.969 MB | 1474.842 MB | 1631.961 MB | n/a MB | n/a MB |
| python3 | 9860 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.922 MB | 8.922 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 9859 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 9878 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.140% | 74.398% | 2.770 s | 364.251 MB | 388.078 MB | 8982.235 MB | 10206.293 MB | n/a MB | n/a MB |
| env | 9891 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.418 MB | 0.418 MB | n/a MB | n/a MB |
| MainThread | 9897 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.478% | 61.478% | 0.620 s | 250.682 MB | 295.156 MB | 1654.516 MB | 1689.809 MB | n/a MB | n/a MB |
| MainThread | 9928 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 29.194% | 91.263% | 2.940 s | 336.314 MB | 388.484 MB | 8596.117 MB | 10205.586 MB | n/a MB | n/a MB |
| MainThread | 9957 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 167.621 MB | 167.621 MB | 1578.473 MB | 1578.473 MB | n/a MB | n/a MB |
| sleep | 9972 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 9978 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 13.342% | 72.404% | 2.560 s | 371.337 MB | 392.082 MB | 9352.260 MB | 10210.926 MB | n/a MB | n/a MB |
| python3 | 10004 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.312 MB | 8.312 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 10003 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 10008 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 262.449 MB | 262.449 MB | 1658.605 MB | 1658.605 MB | n/a MB | n/a MB |
| MainThread | 10050 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 33.742% | 72.629% | 2.050 s | 353.706 MB | 385.375 MB | 8963.788 MB | 10205.750 MB | n/a MB | n/a MB |
| git | 10073 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.059 MB | 4.059 MB | n/a MB | n/a MB |
| MainThread | 10077 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 193.605 MB | 193.605 MB | 1614.473 MB | 1614.473 MB | n/a MB | n/a MB |
| MainThread | 10101 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 20.751% | 69.459% | 2.090 s | 371.092 MB | 391.141 MB | 9419.000 MB | 10207.418 MB | n/a MB | n/a MB |
| MainThread | 10122 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 217.926 MB | 217.926 MB | 1623.734 MB | 1623.734 MB | n/a MB | n/a MB |
| MainThread | 10148 | sandbox_agent_lsb-kimi_0000_0000 | 26 | 11.484% | 72.420% | 2.910 s | 379.426 MB | 393.449 MB | 9547.870 MB | 10206.438 MB | n/a MB | n/a MB |
| MainThread | 10168 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.347% | 60.347% | 0.610 s | 203.939 MB | 250.387 MB | 1481.006 MB | 1647.332 MB | n/a MB | n/a MB |
| python3 | 10181 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.785 MB | 7.785 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 10180 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 10194 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 10195 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.906 MB | 20.906 MB | 213.461 MB | 213.461 MB | n/a MB | n/a MB |
| sleep | 10206 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 10212 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 13.313% | 82.314% | 2.280 s | 379.691 MB | 394.191 MB | 9724.833 MB | 10207.449 MB | n/a MB | n/a MB |
| tar | 10244 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.031 MB | 2.031 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 10245 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.281 MB | 0.281 MB | 3.152 MB | 3.152 MB | n/a MB | n/a MB |
| MainThread | 10251 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 32.538% | 70.454% | 2.650 s | 350.625 MB | 393.855 MB | 8305.068 MB | 10209.453 MB | n/a MB | n/a MB |
| sh | 10276 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.297 MB | 1.297 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10277 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.164 MB | 9.164 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 10281 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 236.398 MB | 236.398 MB | 1636.602 MB | 1636.602 MB | n/a MB | n/a MB |
| MainThread | 10300 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.415% | 74.478% | 2.420 s | 372.576 MB | 392.723 MB | 9584.278 MB | 10208.918 MB | n/a MB | n/a MB |
| MainThread | 10319 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.521% | 61.521% | 0.620 s | 210.094 MB | 259.242 MB | 1486.426 MB | 1655.129 MB | n/a MB | n/a MB |
| sh | 10331 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10332 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.965 MB | 6.965 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 10347 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 23.463% | 88.452% | 3.070 s | 359.583 MB | 390.887 MB | 8954.722 MB | 10207.125 MB | n/a MB | n/a MB |
| MainThread | 10369 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.541% | 66.541% | 0.670 s | 240.939 MB | 288.863 MB | 1641.012 MB | 1683.301 MB | n/a MB | n/a MB |
| sleep | 10469 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 10475 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.097% | 77.540% | 2.560 s | 363.048 MB | 390.164 MB | 8780.508 MB | 10205.578 MB | n/a MB | n/a MB |
| MainThread | 10494 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.450% | 58.450% | 0.590 s | 134.422 MB | 229.148 MB | 1401.992 MB | 1631.605 MB | n/a MB | n/a MB |
| sh | 10492 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10493 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.855 MB | 8.855 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| kimi-code | 10506 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.398 MB | 50.398 MB | 864.867 MB | 864.867 MB | n/a MB | n/a MB |
| MainThread | 10522 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 21.821% | 76.295% | 2.200 s | 362.811 MB | 382.535 MB | 9413.518 MB | 10203.727 MB | n/a MB | n/a MB |
| MainThread | 10552 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 142.438 MB | 142.438 MB | 1298.680 MB | 1298.680 MB | n/a MB | n/a MB |
| MainThread | 10571 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 23.119% | 90.237% | 3.030 s | 364.540 MB | 397.367 MB | 8975.437 MB | 10209.594 MB | n/a MB | n/a MB |
| python3 | 10601 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.895 MB | 8.895 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 10594 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 44.576% | 44.576% | 0.450 s | 149.080 MB | 214.629 MB | 1453.355 MB | 1623.016 MB | n/a MB | n/a MB |
| sh | 10600 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 10620 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.130% | 90.321% | 3.040 s | 359.838 MB | 394.469 MB | 8865.870 MB | 10209.066 MB | n/a MB | n/a MB |
| MainThread | 10641 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.550% | 53.550% | 0.540 s | 223.756 MB | 260.895 MB | 1625.260 MB | 1656.797 MB | n/a MB | n/a MB |
| MainThread | 10669 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 23.641% | 75.515% | 2.430 s | 367.968 MB | 394.566 MB | 9405.382 MB | 10206.809 MB | n/a MB | n/a MB |
| sleep | 10689 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 10693 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.108% | 62.108% | 0.700 s | 248.504 MB | 301.754 MB | 1670.949 MB | 1726.363 MB | n/a MB | n/a MB |
| MainThread | 10719 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.732% | 91.286% | 2.990 s | 357.812 MB | 392.195 MB | 8861.072 MB | 10210.480 MB | n/a MB | n/a MB |
| kimi-code | 10748 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 47.730 MB | 47.730 MB | 854.703 MB | 854.703 MB | n/a MB | n/a MB |
| MainThread | 10741 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 45.521% | 45.521% | 0.460 s | 133.326 MB | 219.297 MB | 1431.418 MB | 1624.227 MB | n/a MB | n/a MB |
| MainThread | 10767 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.396% | 86.348% | 2.540 s | 356.170 MB | 387.031 MB | 8925.321 MB | 10197.574 MB | n/a MB | n/a MB |
| sh | 10793 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10794 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.395 MB | 6.395 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 10798 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 217.688 MB | 217.688 MB | 1623.484 MB | 1623.484 MB | n/a MB | n/a MB |
| MainThread | 10817 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 22.953% | 79.362% | 2.550 s | 363.870 MB | 391.062 MB | 8780.161 MB | 10206.711 MB | n/a MB | n/a MB |
| kimi | 10836 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 57.603% | 59.633% | 1.170 s | 178.970 MB | 304.559 MB | 1175.727 MB | 1729.004 MB | n/a MB | n/a MB |
| python3 | 10835 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.121 MB | 8.121 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 10834 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 10848 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10849 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.773 MB | 4.773 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| MainThread | 10864 | sandbox_agent_lsb-kimi_0000_0000 | 35 | 8.291% | 72.549% | 2.840 s | 380.170 MB | 387.164 MB | 9959.084 MB | 10207.453 MB | n/a MB | n/a MB |
| MainThread | 10895 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 175.090 MB | 175.090 MB | 1582.223 MB | 1582.223 MB | n/a MB | n/a MB |
| kimi-code | 10910 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 54.898 MB | 54.898 MB | 898.574 MB | 898.574 MB | n/a MB | n/a MB |
| sleep | 10913 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 10916 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.805 MB | 2.805 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 10917 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 11.133 MB | 11.133 MB | 14.906 MB | 14.906 MB | n/a MB | n/a MB |
| python | 10918 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 28.243% | 56.487% | 0.570 s | 55.355 MB | 66.266 MB | 67.647 MB | 80.141 MB | n/a MB | n/a MB |
| python | 10919 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 26.423% | 72.325% | 0.800 s | 51.483 MB | 66.297 MB | 63.084 MB | 80.141 MB | n/a MB | n/a MB |
| MainThread | 10933 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 26.932% | 76.500% | 2.170 s | 367.814 MB | 394.309 MB | 9245.006 MB | 10209.129 MB | n/a MB | n/a MB |
| MainThread | 10964 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 159.742 MB | 159.742 MB | 1315.719 MB | 1315.719 MB | n/a MB | n/a MB |
| MainThread | 10983 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.106% | 77.064% | 2.980 s | 367.868 MB | 392.305 MB | 9067.289 MB | 10209.965 MB | n/a MB | n/a MB |
| bash | 10996 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.434 MB | 0.434 MB | 3.715 MB | 3.715 MB | n/a MB | n/a MB |
| MainThread | 11002 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.321% | 62.321% | 0.630 s | 251.660 MB | 293.898 MB | 1654.668 MB | 1688.836 MB | n/a MB | n/a MB |
| MainThread | 11030 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 34.027% | 74.543% | 2.740 s | 351.434 MB | 395.988 MB | 8304.271 MB | 10211.031 MB | n/a MB | n/a MB |
| MainThread | 11053 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 48.553% | 48.553% | 0.490 s | 211.443 MB | 252.457 MB | 1614.016 MB | 1648.559 MB | n/a MB | n/a MB |
| sleep | 11089 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 11079 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.567% | 76.712% | 2.510 s | 367.177 MB | 388.578 MB | 8897.304 MB | 10209.832 MB | n/a MB | n/a MB |
| MainThread | 11109 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 76.917% | 76.917% | 0.810 s | 224.439 MB | 295.477 MB | 1499.604 MB | 1689.969 MB | n/a MB | n/a MB |
| MainThread | 11151 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 26.945% | 93.213% | 3.530 s | 361.691 MB | 395.641 MB | 8968.895 MB | 10211.191 MB | n/a MB | n/a MB |
| MainThread | 11172 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.612% | 61.612% | 0.620 s | 209.682 MB | 252.656 MB | 1613.154 MB | 1648.336 MB | n/a MB | n/a MB |
| sh | 11184 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11185 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.367 MB | 7.367 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 11216 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 26.653% | 78.071% | 3.230 s | 365.715 MB | 392.227 MB | 8890.448 MB | 10210.301 MB | n/a MB | n/a MB |
| bash | 11229 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.805 MB | 2.805 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 11230 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.625 MB | 1.625 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 11239 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.508 MB | 1.508 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11240 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.242 MB | 7.242 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 11246 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 84.201% | 84.201% | 0.850 s | 231.297 MB | 295.797 MB | 1633.977 MB | 1690.230 MB | n/a MB | n/a MB |
| MainThread | 11265 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 18.649% | 73.545% | 2.260 s | 376.294 MB | 394.734 MB | 9542.209 MB | 10211.367 MB | n/a MB | n/a MB |
| kimi-code | 11285 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 49.172 MB | 49.172 MB | 847.215 MB | 847.215 MB | n/a MB | n/a MB |
| MainThread | 11287 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 211.109 MB | 211.109 MB | 1622.730 MB | 1622.730 MB | n/a MB | n/a MB |
| MainThread | 11316 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 17.304% | 68.539% | 2.090 s | 377.261 MB | 395.418 MB | 9542.435 MB | 10210.816 MB | n/a MB | n/a MB |
| MainThread | 11335 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.564% | 63.564% | 0.640 s | 232.580 MB | 278.996 MB | 1633.633 MB | 1673.543 MB | n/a MB | n/a MB |
| sleep | 11359 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 11368 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.394% | 72.412% | 2.800 s | 365.512 MB | 396.680 MB | 8985.896 MB | 10211.238 MB | n/a MB | n/a MB |
| MainThread | 11392 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 50.611% | 50.611% | 0.510 s | 202.146 MB | 243.148 MB | 1478.412 MB | 1639.102 MB | n/a MB | n/a MB |
| MainThread | 11420 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.057% | 91.436% | 2.970 s | 356.991 MB | 392.703 MB | 9043.651 MB | 10211.715 MB | n/a MB | n/a MB |
| MainThread | 11441 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.524% | 54.524% | 0.550 s | 230.361 MB | 271.875 MB | 1630.760 MB | 1667.297 MB | n/a MB | n/a MB |
| MainThread | 11472 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.512% | 78.366% | 2.900 s | 367.362 MB | 396.039 MB | 9070.167 MB | 10215.816 MB | n/a MB | n/a MB |
| MainThread | 11499 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 172.844 MB | 172.844 MB | 1579.973 MB | 1579.973 MB | n/a MB | n/a MB |
| sh | 11521 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11522 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.254 MB | 7.254 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 11526 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.321% | 75.319% | 3.060 s | 365.277 MB | 393.707 MB | 8896.184 MB | 10213.891 MB | n/a MB | n/a MB |
| MainThread | 11550 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 42.615% | 42.615% | 0.430 s | 197.770 MB | 228.684 MB | 1604.975 MB | 1631.977 MB | n/a MB | n/a MB |
| sleep | 11572 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 11654 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.220% | 87.328% | 2.780 s | 372.076 MB | 393.977 MB | 8990.351 MB | 10212.715 MB | n/a MB | n/a MB |
| sh | 11673 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| python3 | 11689 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.859 MB | 7.859 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| MainThread | 11678 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.573% | 55.573% | 0.560 s | 217.902 MB | 259.734 MB | 1623.031 MB | 1655.590 MB | n/a MB | n/a MB |
| sh | 11688 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 11704 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 26.058% | 98.348% | 3.430 s | 355.511 MB | 392.355 MB | 8950.223 MB | 10209.715 MB | n/a MB | n/a MB |
| MainThread | 11729 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 71.987% | 71.987% | 0.750 s | 240.369 MB | 295.527 MB | 1641.584 MB | 1689.945 MB | n/a MB | n/a MB |
| MainThread | 11753 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.911% | 75.572% | 2.650 s | 366.349 MB | 396.695 MB | 8783.894 MB | 10210.609 MB | n/a MB | n/a MB |
| sh | 11783 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| MainThread | 11772 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.421% | 59.421% | 0.600 s | 250.047 MB | 295.707 MB | 1654.656 MB | 1690.574 MB | n/a MB | n/a MB |
| MainThread | 11801 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.081% | 78.439% | 2.690 s | 372.591 MB | 396.461 MB | 9070.806 MB | 10211.281 MB | n/a MB | n/a MB |
| python3 | 11821 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.734 MB | 7.734 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| kimi | 11822 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 58.063% | 63.447% | 1.170 s | 178.318 MB | 302.715 MB | 1176.639 MB | 1727.852 MB | n/a MB | n/a MB |
| sh | 11820 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11849 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 11855 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.995% | 71.593% | 2.880 s | 365.537 MB | 392.711 MB | 8985.881 MB | 10212.484 MB | n/a MB | n/a MB |
| MainThread | 11879 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 48.596% | 48.596% | 0.490 s | 211.180 MB | 252.250 MB | 1613.654 MB | 1648.336 MB | n/a MB | n/a MB |
| MainThread | 11909 | sandbox_agent_lsb-kimi_0000_0000 | 41 | 8.104% | 77.369% | 3.280 s | 387.916 MB | 399.293 MB | 9997.332 MB | 10212.262 MB | n/a MB | n/a MB |
| MainThread | 11931 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 207.316 MB | 207.316 MB | 1618.969 MB | 1618.969 MB | n/a MB | n/a MB |
| sleep | 11967 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 11973 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 39.278% | 75.290% | 2.770 s | 342.589 MB | 392.449 MB | 8063.562 MB | 10211.062 MB | n/a MB | n/a MB |
| MainThread | 11994 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 48.607% | 48.607% | 0.490 s | 194.934 MB | 235.527 MB | 1567.658 MB | 1635.848 MB | n/a MB | n/a MB |
| sh | 12015 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12016 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.922 MB | 6.922 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 12020 | sandbox_agent_lsb-kimi_0000_0000 | 25 | 14.826% | 74.561% | 3.590 s | 381.265 MB | 399.422 MB | 9526.305 MB | 10215.129 MB | n/a MB | n/a MB |
| sh | 12048 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12049 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.059 MB | 10.059 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 12041 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 40.559% | 40.559% | 0.410 s | 187.582 MB | 220.055 MB | 1467.551 MB | 1623.980 MB | n/a MB | n/a MB |
| python3 | 12069 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.598 MB | 21.598 MB | 26.977 MB | 26.977 MB | n/a MB | n/a MB |
| sh | 12068 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 12076 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 12081 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.412% | 74.406% | 2.830 s | 363.691 MB | 392.055 MB | 8891.735 MB | 10210.758 MB | n/a MB | n/a MB |
| python3 | 12114 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.957 MB | 6.957 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 12103 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.537% | 54.537% | 0.550 s | 256.777 MB | 294.645 MB | 1656.965 MB | 1689.633 MB | n/a MB | n/a MB |
| sh | 12113 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12127 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.680 MB | 10.680 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 12126 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 12131 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.061% | 83.319% | 2.890 s | 371.995 MB | 396.566 MB | 8990.558 MB | 10212.223 MB | n/a MB | n/a MB |
| MainThread | 12162 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 188.512 MB | 188.512 MB | 1593.973 MB | 1593.973 MB | n/a MB | n/a MB |
| sleep | 12177 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| kimi | 12183 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 25.726% | 91.240% | 3.660 s | 347.971 MB | 386.574 MB | 8963.436 MB | 10213.668 MB | n/a MB | n/a MB |
| kimi | 12212 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 68.542% | 68.542% | 0.740 s | 132.229 MB | 261.867 MB | 911.137 MB | 1657.070 MB | n/a MB | n/a MB |
| python3 | 12208 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.941 MB | 9.941 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 12207 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 12232 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 26.424% | 69.479% | 2.940 s | 363.601 MB | 395.707 MB | 8778.066 MB | 10211.984 MB | n/a MB | n/a MB |
| MainThread | 12253 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.116% | 65.116% | 0.660 s | 241.102 MB | 288.012 MB | 1648.533 MB | 1682.594 MB | n/a MB | n/a MB |
| MainThread | 12301 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.544% | 75.423% | 2.830 s | 365.221 MB | 396.793 MB | 8979.093 MB | 10208.988 MB | n/a MB | n/a MB |
| MainThread | 12321 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 70.015% | 70.015% | 0.710 s | 244.182 MB | 294.691 MB | 1651.775 MB | 1689.078 MB | n/a MB | n/a MB |
| MainThread | 12352 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.466% | 80.356% | 2.680 s | 369.388 MB | 394.812 MB | 8987.211 MB | 10211.348 MB | n/a MB | n/a MB |
| kimi-code | 12369 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 41.570 MB | 41.570 MB | 835.461 MB | 835.461 MB | n/a MB | n/a MB |
| MainThread | 12374 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 50.527% | 50.527% | 0.510 s | 211.795 MB | 254.223 MB | 1614.275 MB | 1649.828 MB | n/a MB | n/a MB |
| MainThread | 12400 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.133% | 80.496% | 2.560 s | 381.312 MB | 401.551 MB | 9631.343 MB | 10213.914 MB | n/a MB | n/a MB |
| sleep | 12410 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 12433 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 236.367 MB | 236.367 MB | 1636.605 MB | 1636.605 MB | n/a MB | n/a MB |
| MainThread | 12456 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 22.554% | 88.462% | 3.180 s | 367.377 MB | 400.504 MB | 9047.344 MB | 10214.219 MB | n/a MB | n/a MB |
| sh | 12480 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| MainThread | 12484 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 187.043 MB | 187.043 MB | 1593.723 MB | 1593.723 MB | n/a MB | n/a MB |
| sh | 12504 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12505 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.230 MB | 9.230 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 12509 | sandbox_agent_lsb-kimi_0000_0000 | 146 | 5.138% | 71.553% | 7.500 s | 385.882 MB | 401.867 MB | 10087.343 MB | 10216.289 MB | n/a MB | n/a MB |
| python3 | 12542 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.355 MB | 0.355 MB | n/a MB | n/a MB |
| sh | 12541 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 12530 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.248% | 67.248% | 0.680 s | 245.990 MB | 293.160 MB | 1652.922 MB | 1688.340 MB | n/a MB | n/a MB |
| sleep | 12559 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12659 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12660 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.883 MB | 17.883 MB | 23.184 MB | 23.184 MB | n/a MB | n/a MB |
| python3 | 12691 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.043 MB | 17.043 MB | 22.180 MB | 22.180 MB | n/a MB | n/a MB |
| sh | 12690 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 12698 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.234 MB | 13.234 MB | 207.250 MB | 207.250 MB | n/a MB | n/a MB |
| bash | 12697 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.809 MB | 2.809 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 12708 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 12711 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.450% | 64.450% | 0.650 s | 45.443 MB | 65.969 MB | 55.867 MB | 80.109 MB | n/a MB | n/a MB |
| python | 12733 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.665% | 54.665% | 0.550 s | 51.850 MB | 65.902 MB | 63.527 MB | 81.117 MB | n/a MB | n/a MB |
| python | 12742 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 10.883 MB | 10.883 MB | 14.871 MB | 14.871 MB | n/a MB | n/a MB |
| python | 12743 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 69.558% | 69.558% | 0.710 s | 42.332 MB | 65.961 MB | 51.779 MB | 79.559 MB | n/a MB | n/a MB |
| bash | 12741 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.746 MB | 2.746 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 12746 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.487% | 52.487% | 0.530 s | 51.357 MB | 66.105 MB | 62.756 MB | 80.117 MB | n/a MB | n/a MB |
| bash | 12767 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 12768 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 53.125 MB | 53.125 MB | 273.570 MB | 273.570 MB | n/a MB | n/a MB |
| MainThread | 12782 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 17.412% | 86.423% | 2.980 s | 364.077 MB | 390.867 MB | 9206.694 MB | 10190.250 MB | n/a MB | n/a MB |
| sh | 12805 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12806 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.641 MB | 5.641 MB | 11.645 MB | 11.645 MB | n/a MB | n/a MB |
| pgrep | 12807 |  | 1 | n/a% | n/a% | n/a s | 3.465 MB | 3.465 MB | 10.102 MB | 10.102 MB | n/a MB | n/a MB |
| sleep | 12808 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 12814 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 298.094 MB | 298.094 MB | 1692.848 MB | 1692.848 MB | n/a MB | n/a MB |
| python | 12831 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.473 MB | 8.473 MB | 13.273 MB | 13.273 MB | n/a MB | n/a MB |
| bash | 12830 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.598 MB | 2.598 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 12845 | sandbox_agent_lsb-kimi_0000_0000 | 39 | 9.483% | 80.452% | 3.630 s | 380.619 MB | 389.848 MB | 9772.058 MB | 10211.312 MB | n/a MB | n/a MB |
| MainThread | 12868 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.503% | 55.503% | 0.560 s | 225.742 MB | 263.875 MB | 1626.525 MB | 1659.078 MB | n/a MB | n/a MB |
| bash | 12892 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 12893 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.996 MB | 20.996 MB | 212.293 MB | 212.293 MB | n/a MB | n/a MB |
| sh | 12897 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12898 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.879 MB | 21.879 MB | 27.066 MB | 27.066 MB | n/a MB | n/a MB |
| python | 12905 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.715 MB | 20.715 MB | 212.145 MB | 212.145 MB | n/a MB | n/a MB |
| bash | 12904 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.809 MB | 2.809 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 12917 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 10.809 MB | 10.809 MB | 14.898 MB | 14.898 MB | n/a MB | n/a MB |
| python | 12918 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.553% | 49.553% | 0.500 s | 51.551 MB | 66.355 MB | 62.816 MB | 80.117 MB | n/a MB | n/a MB |
| bash | 12916 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.746 MB | 2.746 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 12920 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 47.020 MB | 47.020 MB | 56.117 MB | 56.117 MB | n/a MB | n/a MB |
| sh | 12921 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12922 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.859 MB | 8.859 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| MainThread | 12933 | sandbox_agent_lsb-kimi_0000_0000 | 23 | 16.593% | 83.098% | 3.680 s | 376.924 MB | 390.422 MB | 9473.920 MB | 10214.441 MB | n/a MB | n/a MB |
| sh | 12959 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12958 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12960 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.309 MB | 8.309 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 12966 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 167.266 MB | 167.266 MB | 1578.473 MB | 1578.473 MB | n/a MB | n/a MB |
| sh | 12989 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| sh | 12994 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12995 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.801 MB | 10.801 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 12999 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 22.486% | 92.078% | 3.640 s | 367.480 MB | 396.363 MB | 9170.071 MB | 10210.164 MB | n/a MB | n/a MB |
| python3 | 13040 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.320 MB | 9.320 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 13039 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 13044 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 168.453 MB | 168.453 MB | 1578.473 MB | 1578.473 MB | n/a MB | n/a MB |
| python3 | 13059 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.535 MB | 21.535 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| sh | 13058 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 13076 | sandbox_agent_lsb-kimi_0000_0000 | 21 | 14.301% | 75.497% | 2.880 s | 381.802 MB | 395.898 MB | 9794.097 MB | 10210.887 MB | n/a MB | n/a MB |
| MainThread | 13107 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 72.492% | 72.492% | 0.730 s | 154.711 MB | 260.949 MB | 1447.459 MB | 1656.309 MB | n/a MB | n/a MB |
| MainThread | 13134 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 40.191% | 78.458% | 2.430 s | 345.691 MB | 384.605 MB | 7764.455 MB | 10207.359 MB | n/a MB | n/a MB |
| sleep | 13144 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13169 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.621 MB | 10.621 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 13168 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 13158 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.498% | 56.498% | 0.570 s | 256.494 MB | 296.004 MB | 1656.963 MB | 1690.461 MB | n/a MB | n/a MB |
| kimi | 13187 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 42.694% | 87.217% | 2.580 s | 306.642 MB | 381.031 MB | 7530.911 MB | 10200.281 MB | n/a MB | n/a MB |
| MainThread | 13238 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 289.832 MB | 289.832 MB | 1684.570 MB | 1684.570 MB | n/a MB | n/a MB |
| MainThread | 13257 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 40.531% | 77.555% | 2.040 s | 356.215 MB | 384.867 MB | 8764.344 MB | 10209.438 MB | n/a MB | n/a MB |
| MainThread | 13286 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 166.691 MB | 166.691 MB | 1577.723 MB | 1577.723 MB | n/a MB | n/a MB |
| MainThread | 13305 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 16.876% | 79.379% | 2.550 s | 377.378 MB | 392.891 MB | 9667.449 MB | 10211.145 MB | n/a MB | n/a MB |
| MainThread | 13333 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 205.914 MB | 205.914 MB | 1618.715 MB | 1618.715 MB | n/a MB | n/a MB |
| sh | 13347 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13348 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.754 MB | 21.754 MB | 27.066 MB | 27.066 MB | n/a MB | n/a MB |
| MainThread | 13364 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 36.763% | 76.508% | 2.590 s | 347.971 MB | 388.738 MB | 8066.449 MB | 10209.594 MB | n/a MB | n/a MB |
| python3 | 13395 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.098 MB | 8.098 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| MainThread | 13384 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 45.673% | 45.673% | 0.460 s | 262.703 MB | 296.238 MB | 1661.596 MB | 1690.969 MB | n/a MB | n/a MB |
| sh | 13394 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 13414 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 45.144% | 83.293% | 2.730 s | 329.907 MB | 381.773 MB | 7741.484 MB | 10205.023 MB | n/a MB | n/a MB |
| MainThread | 13577 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 182.398 MB | 182.398 MB | 1592.973 MB | 1592.973 MB | n/a MB | n/a MB |
| sh | 13591 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 13596 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 25.361% | 80.306% | 3.580 s | 364.260 MB | 392.988 MB | 9064.772 MB | 10211.766 MB | n/a MB | n/a MB |
| MainThread | 13617 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.501% | 49.501% | 0.500 s | 118.693 MB | 208.297 MB | 937.391 MB | 1619.477 MB | n/a MB | n/a MB |
| sleep | 13637 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 13642 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.703 MB | 2.703 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 13643 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.324 MB | 50.324 MB | 270.051 MB | 270.051 MB | n/a MB | n/a MB |
| MainThread | 13657 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 46.465% | 73.561% | 2.810 s | 345.842 MB | 383.188 MB | 7763.549 MB | 10209.129 MB | n/a MB | n/a MB |
| MainThread | 13680 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 42.628% | 42.628% | 0.430 s | 181.855 MB | 221.375 MB | 1461.459 MB | 1624.488 MB | n/a MB | n/a MB |
| MainThread | 13706 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 51.765% | 80.123% | 2.610 s | 338.051 MB | 377.469 MB | 7356.800 MB | 10207.453 MB | n/a MB | n/a MB |
| bash | 13719 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| MainThread | 13731 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 184.477 MB | 184.477 MB | 1592.973 MB | 1592.973 MB | n/a MB | n/a MB |
| MainThread | 13751 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.781% | 81.486% | 2.590 s | 371.914 MB | 390.160 MB | 9588.378 MB | 10210.383 MB | n/a MB | n/a MB |
| MainThread | 13780 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 160.695 MB | 160.695 MB | 1500.469 MB | 1500.469 MB | n/a MB | n/a MB |
| sh | 13792 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13793 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.609 MB | 18.609 MB | 24.570 MB | 24.570 MB | n/a MB | n/a MB |
| sh | 13806 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13807 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.988 MB | 8.988 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 13811 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 45.703% | 83.471% | 2.760 s | 331.891 MB | 380.816 MB | 7749.850 MB | 10202.910 MB | n/a MB | n/a MB |
| MainThread | 13832 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.505% | 56.505% | 0.570 s | 215.586 MB | 260.539 MB | 1617.949 MB | 1656.176 MB | n/a MB | n/a MB |
| MainThread | 13858 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 31.616% | 77.525% | 1.910 s | 353.864 MB | 386.535 MB | 8954.763 MB | 10205.355 MB | n/a MB | n/a MB |
| MainThread | 13877 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.664% | 49.664% | 0.500 s | 186.094 MB | 228.969 MB | 1467.566 MB | 1635.578 MB | n/a MB | n/a MB |
| python3 | 13890 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.805 MB | 7.805 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 13889 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 13906 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 37.688% | 75.419% | 1.900 s | 347.407 MB | 383.812 MB | 8733.647 MB | 10166.992 MB | n/a MB | n/a MB |
| MainThread | 13926 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.286% | 58.286% | 0.590 s | 164.119 MB | 235.656 MB | 1459.510 MB | 1635.324 MB | n/a MB | n/a MB |
| sh | 13924 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13925 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.141 MB | 9.141 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sleep | 13954 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 13956 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.398% | 74.552% | 2.600 s | 362.521 MB | 390.762 MB | 8774.754 MB | 10203.129 MB | n/a MB | n/a MB |
| python3 | 13980 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.496 MB | 9.496 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| sh | 13979 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 13984 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 272.547 MB | 272.547 MB | 1667.547 MB | 1667.547 MB | n/a MB | n/a MB |
| MainThread | 14015 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.104% | 75.407% | 2.980 s | 369.040 MB | 391.363 MB | 9069.790 MB | 10212.012 MB | n/a MB | n/a MB |
| MainThread | 14039 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 42.660% | 42.660% | 0.430 s | 190.617 MB | 229.227 MB | 1565.281 MB | 1631.344 MB | n/a MB | n/a MB |
| python | 14062 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.531 MB | 13.531 MB | 207.367 MB | 207.367 MB | n/a MB | n/a MB |
| bash | 14061 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.715 MB | 2.715 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 14076 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 44.646% | 66.450% | 2.700 s | 342.027 MB | 381.934 MB | 7759.066 MB | 10202.980 MB | n/a MB | n/a MB |
| kimi-code | 14105 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.043 MB | 50.043 MB | 858.992 MB | 858.992 MB | n/a MB | n/a MB |
| MainThread | 14098 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.344% | 62.344% | 0.630 s | 209.094 MB | 260.012 MB | 1577.902 MB | 1655.836 MB | n/a MB | n/a MB |
| python3 | 14120 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.070 MB | 7.070 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 14119 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 14124 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 41.197% | 73.373% | 2.490 s | 339.699 MB | 388.109 MB | 7748.600 MB | 10193.984 MB | n/a MB | n/a MB |
| python3 | 14153 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.082 MB | 10.082 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 14151 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 14145 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.383% | 57.383% | 0.580 s | 171.600 MB | 236.188 MB | 1459.795 MB | 1635.895 MB | n/a MB | n/a MB |
| MainThread | 14171 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 18.336% | 77.059% | 2.960 s | 369.301 MB | 390.355 MB | 9201.516 MB | 10211.309 MB | n/a MB | n/a MB |
| bash | 14184 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.672 MB | 2.672 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 14190 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.549% | 53.549% | 0.540 s | 248.709 MB | 289.672 MB | 1651.863 MB | 1684.281 MB | n/a MB | n/a MB |
| sh | 14213 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 14214 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.605 MB | 20.605 MB | 25.707 MB | 25.707 MB | n/a MB | n/a MB |
| python3 | 14221 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.258 MB | 21.258 MB | 27.070 MB | 27.070 MB | n/a MB | n/a MB |
| sh | 14220 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 14226 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 14232 | sandbox_agent_lsb-kimi_0000_0000 | 41 | 8.858% | 76.539% | 3.580 s | 388.692 MB | 401.664 MB | 9794.099 MB | 10215.363 MB | n/a MB | n/a MB |
| MainThread | 14258 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 72.676% | 72.676% | 0.770 s | 166.107 MB | 262.215 MB | 1470.492 MB | 1657.289 MB | n/a MB | n/a MB |
| sh | 14256 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 14257 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.676 MB | 9.676 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| python | 14279 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.348 MB | 17.348 MB | 209.723 MB | 209.723 MB | n/a MB | n/a MB |
| bash | 14278 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.652 MB | 2.652 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14289 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.746 MB | 8.746 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 14288 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 14315 | sandbox_agent_lsb-kimi_0000_0000 | 21 | 16.436% | 72.324% | 3.310 s | 374.736 MB | 394.215 MB | 9394.541 MB | 10212.734 MB | n/a MB | n/a MB |
| MainThread | 14337 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 206.051 MB | 206.051 MB | 1618.980 MB | 1618.980 MB | n/a MB | n/a MB |
| sleep | 14374 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 14380 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 33.658% | 87.315% | 3.390 s | 351.942 MB | 393.379 MB | 8621.034 MB | 10211.441 MB | n/a MB | n/a MB |
| git | 14400 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.059 MB | 4.059 MB | n/a MB | n/a MB |
| MainThread | 14409 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 68.467% | 68.467% | 0.690 s | 215.801 MB | 264.914 MB | 1619.029 MB | 1660.336 MB | n/a MB | n/a MB |
| python | 14423 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.859 MB | 8.859 MB | 13.391 MB | 13.391 MB | n/a MB | n/a MB |
| MainThread | 14439 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 37.352% | 81.313% | 3.010 s | 341.250 MB | 387.453 MB | 8294.886 MB | 10210.863 MB | n/a MB | n/a MB |
| MainThread | 14456 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.491% | 59.491% | 0.600 s | 256.596 MB | 295.645 MB | 1656.770 MB | 1689.812 MB | n/a MB | n/a MB |
| MainThread | 14505 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 39.725% | 81.377% | 2.410 s | 353.360 MB | 385.445 MB | 8957.112 MB | 10208.965 MB | n/a MB | n/a MB |
| MainThread | 14522 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 55.166% | 61.451% | 1.120 s | 193.931 MB | 299.367 MB | 1533.518 MB | 1725.594 MB | n/a MB | n/a MB |
| python3 | 14529 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.707 MB | 6.707 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 14528 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.285 MB | 1.285 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 14535 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.738 MB | 7.738 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 14534 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 14550 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 42.115% | 78.507% | 2.970 s | 342.176 MB | 381.586 MB | 8058.524 MB | 10207.211 MB | n/a MB | n/a MB |
| MainThread | 14569 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.497% | 61.497% | 0.620 s | 236.570 MB | 282.902 MB | 1636.516 MB | 1677.809 MB | n/a MB | n/a MB |
| sh | 14590 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 14591 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.547 MB | 5.547 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| MainThread | 14595 | sandbox_agent_lsb-kimi_0000_0000 | 33 | 11.985% | 76.516% | 3.860 s | 385.300 MB | 398.754 MB | 9690.172 MB | 10213.656 MB | n/a MB | n/a MB |
| kimi | 14612 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 59.047% | 65.572% | 1.190 s | 173.712 MB | 302.441 MB | 1171.676 MB | 1726.840 MB | n/a MB | n/a MB |
| sh | 14644 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 14645 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.305 MB | 7.305 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 14646 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 138.922 MB | 138.922 MB | 354.938 MB | 354.938 MB | n/a MB | n/a MB |
| sleep | 14656 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 14667 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 40.366% | 90.323% | 2.860 s | 325.788 MB | 395.516 MB | 7998.241 MB | 10201.191 MB | n/a MB | n/a MB |
| sh | 14701 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 14691 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 194.281 MB | 194.281 MB | 1614.723 MB | 1614.723 MB | n/a MB | n/a MB |
| python3 | 14702 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.145 MB | 9.145 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| MainThread | 14717 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 39.982% | 87.421% | 3.220 s | 337.987 MB | 387.148 MB | 8256.418 MB | 10211.293 MB | n/a MB | n/a MB |
| MainThread | 14745 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 234.703 MB | 234.703 MB | 1635.840 MB | 1635.840 MB | n/a MB | n/a MB |
| MainThread | 14762 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 31.770% | 82.429% | 2.240 s | 360.618 MB | 396.070 MB | 9114.561 MB | 10203.094 MB | n/a MB | n/a MB |
| kimi-code | 14779 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 44.301 MB | 44.301 MB | 836.441 MB | 836.441 MB | n/a MB | n/a MB |
| MainThread | 14791 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.520 MB | 229.520 MB | 1632.156 MB | 1632.156 MB | n/a MB | n/a MB |
| MainThread | 14808 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.768% | 86.262% | 2.650 s | 336.771 MB | 394.391 MB | 7737.361 MB | 10200.926 MB | n/a MB | n/a MB |
| MainThread | 14827 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.117% | 56.117% | 0.570 s | 218.662 MB | 261.953 MB | 1623.654 MB | 1657.336 MB | n/a MB | n/a MB |
| sh | 14840 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 14841 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.371 MB | 9.371 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| MainThread | 14856 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 36.175% | 78.522% | 2.550 s | 358.012 MB | 397.340 MB | 8071.054 MB | 10208.535 MB | n/a MB | n/a MB |
| MainThread | 14951 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.523% | 57.523% | 0.580 s | 249.346 MB | 290.328 MB | 1652.016 MB | 1684.559 MB | n/a MB | n/a MB |
| git | 14976 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| MainThread | 14979 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 37.003% | 74.429% | 2.610 s | 347.245 MB | 388.047 MB | 8063.510 MB | 10207.996 MB | n/a MB | n/a MB |
| sh | 15010 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 14998 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.516% | 60.516% | 0.610 s | 241.699 MB | 289.203 MB | 1649.277 MB | 1683.582 MB | n/a MB | n/a MB |
| sh | 15011 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 15007 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 15026 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 40.697% | 80.376% | 2.050 s | 357.990 MB | 386.879 MB | 8762.434 MB | 10207.488 MB | n/a MB | n/a MB |
| MainThread | 15047 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 205.898 MB | 205.898 MB | 1619.465 MB | 1619.465 MB | n/a MB | n/a MB |
| kimi | 15073 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 52.486% | 87.288% | 3.180 s | 303.915 MB | 378.387 MB | 7535.857 MB | 10209.441 MB | n/a MB | n/a MB |
| MainThread | 15102 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 254.723 MB | 254.723 MB | 1650.598 MB | 1650.598 MB | n/a MB | n/a MB |
| MainThread | 15119 | sandbox_agent_lsb-kimi_0000_0000 | 10 | 26.911% | 80.361% | 2.440 s | 363.056 MB | 391.355 MB | 8502.594 MB | 10211.195 MB | n/a MB | n/a MB |
| MainThread | 15147 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 87.438% | 87.438% | 0.880 s | 200.301 MB | 299.910 MB | 1504.094 MB | 1724.492 MB | n/a MB | n/a MB |
| MainThread | 15166 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 42.942% | 88.304% | 3.040 s | 330.089 MB | 389.859 MB | 8007.875 MB | 10209.766 MB | n/a MB | n/a MB |
| MainThread | 15185 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.443% | 57.443% | 0.580 s | 207.012 MB | 255.742 MB | 1575.646 MB | 1651.324 MB | n/a MB | n/a MB |
| python3 | 15198 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.312 MB | 8.312 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 15197 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| gzip | 15207 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| tar | 15206 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.176 MB | 2.176 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| MainThread | 15213 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 37.137% | 76.420% | 2.620 s | 349.809 MB | 390.562 MB | 8066.191 MB | 10207.652 MB | n/a MB | n/a MB |
| MainThread | 15232 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.529% | 55.529% | 0.560 s | 250.352 MB | 289.398 MB | 1653.398 MB | 1684.566 MB | n/a MB | n/a MB |
| MainThread | 15258 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 38.953% | 79.373% | 2.360 s | 343.585 MB | 377.512 MB | 7767.385 MB | 10205.574 MB | n/a MB | n/a MB |
| MainThread | 15287 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.918 MB | 228.918 MB | 1631.094 MB | 1631.094 MB | n/a MB | n/a MB |
| MainThread | 15306 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 20.479% | 75.499% | 2.270 s | 374.648 MB | 394.863 MB | 9481.537 MB | 10207.426 MB | n/a MB | n/a MB |
| MainThread | 15325 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.365% | 51.365% | 0.520 s | 199.689 MB | 238.543 MB | 1477.900 MB | 1638.078 MB | n/a MB | n/a MB |
| sleep | 15347 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 15355 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 16.823% | 79.557% | 3.050 s | 377.694 MB | 396.535 MB | 9307.831 MB | 10207.922 MB | n/a MB | n/a MB |
| sh | 15377 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.277 MB | 1.277 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 15378 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.566 MB | 10.566 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 15386 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 90.442% | 90.442% | 0.910 s | 167.492 MB | 294.473 MB | 1430.504 MB | 1688.809 MB | n/a MB | n/a MB |
| python | 15401 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.641 MB | 13.641 MB | 207.289 MB | 207.289 MB | n/a MB | n/a MB |
| bash | 15400 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.652 MB | 2.652 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 15424 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 49.489% | 87.451% | 2.990 s | 314.065 MB | 386.992 MB | 7684.477 MB | 10202.918 MB | n/a MB | n/a MB |
| MainThread | 15449 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.540% | 66.540% | 0.670 s | 216.705 MB | 277.602 MB | 1586.123 MB | 1672.777 MB | n/a MB | n/a MB |
| MainThread | 15471 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 18.914% | 73.585% | 3.240 s | 373.889 MB | 394.164 MB | 9256.586 MB | 10210.125 MB | n/a MB | n/a MB |
| python3 | 15501 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.859 MB | 8.859 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 15490 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.533% | 53.533% | 0.540 s | 225.918 MB | 263.070 MB | 1626.262 MB | 1658.301 MB | n/a MB | n/a MB |
| sh | 15500 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 15514 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sh | 15513 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 15523 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 137.879 MB | 137.879 MB | 354.074 MB | 354.074 MB | n/a MB | n/a MB |
| bash | 15522 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.816 MB | 2.816 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 15527 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.316 MB | 9.316 MB | 13.301 MB | 13.301 MB | n/a MB | n/a MB |
| MainThread | 15542 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 19.676% | 71.517% | 3.570 s | 375.157 MB | 396.211 MB | 9303.318 MB | 10209.285 MB | n/a MB | n/a MB |
| git | 15571 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.059 MB | 4.059 MB | n/a MB | n/a MB |
| MainThread | 15562 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.022% | 61.022% | 0.620 s | 222.209 MB | 269.684 MB | 1627.643 MB | 1665.312 MB | n/a MB | n/a MB |
| sleep | 15586 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 15588 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.164 MB | 9.164 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 15587 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.352 MB | 1.352 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 15597 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 10.537 MB | 10.688 MB | 14.736 MB | 14.852 MB | n/a MB | n/a MB |
| bash | 15596 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.672 MB | 2.672 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 15598 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 54.059 MB | 54.059 MB | 72.289 MB | 72.289 MB | n/a MB | n/a MB |
| sh | 15599 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 15600 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.430 MB | 21.430 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| MainThread | 15609 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 46.398% | 92.399% | 3.270 s | 324.311 MB | 386.930 MB | 8004.877 MB | 10209.492 MB | n/a MB | n/a MB |
| MainThread | 15628 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 52.171% | 55.651% | 1.050 s | 204.724 MB | 296.137 MB | 1535.548 MB | 1690.973 MB | n/a MB | n/a MB |
| MainThread | 15654 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 44.823% | 68.534% | 2.710 s | 341.866 MB | 387.383 MB | 7760.028 MB | 10207.703 MB | n/a MB | n/a MB |
| sh | 15676 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 15677 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.105 MB | 9.105 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 15688 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 47.081% | 85.295% | 3.320 s | 339.238 MB | 387.305 MB | 8044.765 MB | 10214.250 MB | n/a MB | n/a MB |
| MainThread | 15716 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 199.977 MB | 199.977 MB | 1618.234 MB | 1618.234 MB | n/a MB | n/a MB |
| MainThread | 15733 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 33.336% | 75.051% | 2.690 s | 356.363 MB | 395.566 MB | 8310.426 MB | 10210.859 MB | n/a MB | n/a MB |
| bash | 15747 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 15746 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 15765 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 170.277 MB | 170.277 MB | 1579.723 MB | 1579.723 MB | n/a MB | n/a MB |
| MainThread | 15782 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 16.337% | 73.476% | 3.140 s | 378.604 MB | 398.211 MB | 9353.427 MB | 10211.383 MB | n/a MB | n/a MB |
| MainThread | 15801 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.585% | 53.585% | 0.540 s | 245.439 MB | 285.719 MB | 1650.023 MB | 1681.066 MB | n/a MB | n/a MB |
| python | 15828 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.444% | 56.444% | 0.570 s | 51.342 MB | 66.332 MB | 62.842 MB | 81.398 MB | n/a MB | n/a MB |
| python | 15827 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 10.809 MB | 10.809 MB | 14.871 MB | 14.871 MB | n/a MB | n/a MB |
| bash | 15826 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.699 MB | 2.699 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 15840 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.695 MB | 20.695 MB | 25.578 MB | 25.578 MB | n/a MB | n/a MB |
| sh | 15839 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 15836 |  | 48 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 15845 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.160 MB | 7.160 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 15844 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| docker | 15875 |  | 17 | 0.000% | 0.000% | 0.000 s | 30.527 MB | 30.527 MB | 1843.512 MB | 1843.512 MB | 0.000000 MB | 0.000000 MB |
| docker | 15945 |  | 1 | n/a% | n/a% | n/a s | 29.832 MB | 29.832 MB | 1771.195 MB | 1771.195 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.411% | 79.000% | 11878.527 MB | 12072.000 MB | 28.459 W | 55.007 W | 83647.261 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-kimi_0000_0000 | 89.588% | 215.658% | 2610.996 s | 439.208 MB | 2440.633 MB | 4.734375 MB | 360.855469 MB | 285.327623 MB | 4.027377 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4049 | 2940.654 | interrupted |
| harness:retire | -1 | 0.124 | interrupted |
| harness:retire | -1 | 0.122 | interrupted |
| harness:retire | -1 | 0.121 | interrupted |
| harness:retire | -1 | 0.119 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.116 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.105 | interrupted |
| harness:retire | -1 | 0.105 | interrupted |
| harness:retire | -1 | 0.105 | interrupted |
| harness:retire | -1 | 0.105 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.101 | interrupted |
| harness:retire | -1 | 0.101 | interrupted |
| harness:retire | -1 | 0.101 | interrupted |
| harness:retire | -1 | 0.101 | interrupted |
| harness:retire | -1 | 0.101 | interrupted |
| harness:retire | -1 | 0.101 | interrupted |
| harness:retire | -1 | 0.101 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.100 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.098 | interrupted |
| harness:retire | -1 | 0.098 | interrupted |
| harness:retire | -1 | 0.098 | interrupted |
| harness:retire | -1 | 0.098 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.094 | interrupted |
| harness:retire | -1 | 0.094 | interrupted |
| harness:retire | -1 | 0.094 | interrupted |
| harness:retire | -1 | 0.094 | interrupted |
| harness:retire | -1 | 0.093 | interrupted |
| harness:retire | -1 | 0.093 | interrupted |
| harness:retire | -1 | 0.093 | interrupted |
| harness:retire | -1 | 0.093 | interrupted |
| harness:retire | -1 | 0.093 | interrupted |
| harness:retire | -1 | 0.093 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.091 | interrupted |
| harness:retire | -1 | 0.091 | interrupted |
| harness:retire | -1 | 0.091 | interrupted |
| harness:retire | -1 | 0.091 | interrupted |
| harness:retire | -1 | 0.091 | interrupted |
| harness:retire | -1 | 0.091 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
| harness:retire | -1 | 0.088 | interrupted |
| harness:retire | -1 | 0.088 | interrupted |
| harness:retire | -1 | 0.088 | interrupted |
| harness:retire | -1 | 0.088 | interrupted |
| harness:retire | -1 | 0.088 | interrupted |
| harness:retire | -1 | 0.088 | interrupted |
| harness:retire | -1 | 0.088 | interrupted |
| harness:retire | -1 | 0.088 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.086 | interrupted |
| harness:retire | -1 | 0.086 | interrupted |
| harness:retire | -1 | 0.086 | interrupted |
| harness:retire | -1 | 0.086 | interrupted |
| harness:retire | -1 | 0.086 | interrupted |
| harness:retire | -1 | 0.086 | interrupted |
| harness:retire | -1 | 0.086 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.080 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.078 | interrupted |
| harness:retire | -1 | 0.078 | interrupted |
| harness:retire | -1 | 0.078 | interrupted |
| syscall:execve | -1 | 0.077 | interrupted |
| harness:retire | -1 | 0.077 | interrupted |
| harness:retire | -1 | 0.076 | interrupted |
| harness:retire | -1 | 0.076 | interrupted |
| harness:retire | -1 | 0.076 | interrupted |
| harness:retire | -1 | 0.075 | interrupted |
| harness:retire | -1 | 0.075 | interrupted |
| harness:retire | -1 | 0.071 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2914.095 | n/a | n/a | 4.734 | 2914095.303 | 2914095.303 | 2914095.303 |
| engine:execute | 1/1 | 0 | 0 | 2914.094 | 1.767 | 2912.317 | 4.734 | 2914093.645 | 2914093.645 | 2914093.645 |
| harness:attempt_rpc | 187/187 | 0 | 0 | 2891.292 | 4.971 | 2886.320 | 4.734 | 15461.457 | 12466.161 | 30349.963 |
| harness:await_cli | 187/187 | 0 | 0 | 2076.654 | n/a | n/a | 4.726 | 11105.101 | 8171.735 | 26665.963 |
| llm:attempt | 303/303 | 14 | 0 | 1767.834 | 41.746 | 1725.721 | 1.601 | 5834.435 | 4684.318 | 10493.565 |
| harness:startup_ready | 187/187 | 0 | 0 | 572.617 | n/a | n/a | 0.000 | 3062.121 | 3014.096 | 3556.243 |
| tool:Bash | 73/73 | 25 | 0 | 240.084 | n/a | n/a | 3.231 | 3288.818 | 1284.553 | 9669.357 |
| harness:submit | 187/187 | 0 | 0 | 159.310 | n/a | n/a | 0.008 | 851.925 | 869.300 | 1085.005 |
| run:container_call | 13/13 | 0 | 0 | 18.089 | 0.003 | 18.086 | 0.000 | 1391.431 | 38.121 | 7075.006 |
| teardown:commit | 1/1 | 0 | 0 | 17.641 | 0.004 | 17.636 | 0.000 | 17640.511 | 17640.511 | 17640.511 |
| syscall:connect | 6416/6416 | 0 | 0 | 17.639 | n/a | n/a | 0.020 | 2.749 | 2.270 | 5.218 |
| sandbox:commit | 1/1 | 0 | 0 | 17.443 | 0.003 | 17.440 | 0.000 | 17442.697 | 17442.697 | 17442.697 |
| checkpoint.total | 1/1 | 0 | 0 | 17.443 | 0.002 | 17.440 | 0.000 | 17442.562 | 17442.562 | 17442.562 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 17.442 | 0.002 | 17.440 | 0.000 | 17442.394 | 17442.394 | 17442.394 |
| tool:Glob | 2/2 | 1 | 0 | 13.434 | n/a | n/a | 0.000 | 6717.018 | 6717.018 | 10163.030 |
| syscall:execve | 4427/4428 | 0 | 1 | 13.182 | n/a | n/a | 0.038 | 2.978 | 2.381 | 6.582 |
| syscall:sendto | 4546/4546 | 0 | 0 | 12.239 | n/a | n/a | 0.035 | 2.692 | 2.231 | 5.090 |
| harness:snapshot | 187/187 | 0 | 0 | 7.624 | n/a | n/a | 0.000 | 40.769 | 39.888 | 58.958 |
| harness:launch | 187/187 | 0 | 0 | 3.668 | n/a | n/a | 0.000 | 19.615 | 18.884 | 24.845 |
| syscall:bind | 1103/1103 | 0 | 0 | 3.566 | n/a | n/a | 0.000 | 3.233 | 2.655 | 5.589 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.370 | 0.807 | 2.563 | 0.000 | 3370.117 | 3370.117 | 3370.117 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.370 | 0.807 | 2.563 | 0.000 | 3369.843 | 3369.843 | 3369.843 |
| tool:Grep | 1/1 | 1 | 0 | 2.443 | n/a | n/a | 0.000 | 2443.049 | 2443.049 | 2443.049 |
| tool:Read | 7/7 | 0 | 0 | 1.833 | n/a | n/a | 0.000 | 261.928 | 258.069 | 291.917 |
| tool:TodoList | 6/6 | 0 | 0 | 1.728 | n/a | n/a | 0.000 | 288.082 | 279.055 | 330.439 |
| tool:Write | 5/5 | 0 | 0 | 1.578 | n/a | n/a | 0.000 | 315.513 | 329.904 | 386.625 |
| tool:Edit | 6/6 | 0 | 0 | 1.575 | n/a | n/a | 0.000 | 262.510 | 264.877 | 286.821 |
| agency:decode_harness_result | 187/187 | 0 | 0 | 0.927 | 0.927 | 0.001 | 0.000 | 4.957 | 4.368 | 9.277 |
| sandbox:start | 1/1 | 0 | 0 | 0.373 | 0.003 | 0.370 | 0.000 | 373.444 | 373.444 | 373.444 |
| runtime.container_create | 1/1 | 0 | 0 | 0.373 | 0.003 | 0.370 | 0.000 | 373.222 | 373.222 | 373.222 |
| sandbox:create | 1/1 | 0 | 0 | 0.345 | 0.251 | 0.094 | 0.000 | 345.493 | 345.493 | 345.493 |
| sandbox:stop | 1/1 | 0 | 0 | 0.198 | 0.002 | 0.196 | 0.000 | 197.567 | 197.567 | 197.567 |
| agency:services_close | 1/1 | 0 | 0 | 0.112 | 0.002 | 0.111 | 0.000 | 112.335 | 112.335 | 112.335 |
| agency:services_start | 1/1 | 0 | 0 | 0.077 | 0.044 | 0.034 | 0.000 | 77.487 | 77.487 | 77.487 |
| run:detect | 1/1 | 0 | 0 | 0.057 | 0.001 | 0.056 | 0.000 | 56.605 | 56.605 | 56.605 |
| agent:create | 1/1 | 0 | 0 | 0.047 | 0.007 | 0.040 | 0.000 | 47.108 | 47.108 | 47.108 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.215 | 1.215 | 1.215 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.085 | 0.099 | 0.119 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.200 | 0.200 | 0.200 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.087 | 0.087 | 0.087 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/187 | 0 | 187 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2916 | 0.239 | 0.037 | 57.333 | 0.060 | 7.010240 CPU seconds | n/a |
| GPU 0 memory | MB | 2917 | 11878.527 | 11670.000 | 12072.000 | 11852.000 | n/a | n/a |
| GPU 0 power | W | 2917 | 28.459 | 27.530 | 55.007 | 28.246 | n/a | 83647.261 J |
| GPU 0 proc / 3899-119944 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 memory | MB | 2917 | 3251.729 | 3118.000 | 3442.000 | 3222.000 | n/a | n/a |
| GPU 0 proc / 3899-119944 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 estimated power | W | 2695 | 0.653 | 0.000 | 55.007 | 0.000 | n/a | n/a |
| GPU 0 proc / 3899-119944 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 utilization | percent | 2695 | 0.317 | 0.000 | 44.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 3942-121931 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 memory | MB | 2917 | 8144.798 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 3942-121931 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 estimated power | W | 165 | 2.931 | 0.000 | 42.899 | 0.000 | n/a | n/a |
| GPU 0 proc / 3942-121931 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 utilization | percent | 165 | 1.673 | 0.000 | 34.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2917 | 11396.527 | 11188.000 | 11590.000 | 11370.000 | n/a | n/a |
| GPU 0 utilization | percent | 2917 | 0.411 | 0.000 | 79.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2917 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2916 | 4.687 | 0.110 | 70.406 | 0.124 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2916 | 23.949 | 0.000 | 59.902 | 0.000 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2916 | 0.558 | 0.000 | 239.562 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2916 | 0.763 | 0.000 | 11.277 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2916 | 0.433 | 0.000 | 92.374 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2916 | 0.483 | 0.000 | 92.574 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 2917 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 2917 | 7500.273 | 6567.285 | 9169.168 | 7486.559 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2916 | 0.000 | 0.000 | 0.028 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2916 | 0.000 | 0.000 | 0.028 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2916 | 0.133 | 0.000 | 2.245 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2916 | 0.034 | 0.000 | 0.503 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10003) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10003) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10004) rss_mb | MB | 1 | 8.312 | 8.312 | 8.312 | 8.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10004) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10008) rss_mb | MB | 1 | 262.449 | 262.449 | 262.449 | 262.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10008) vms_mb | MB | 1 | 1658.605 | 1658.605 | 1658.605 | 1658.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10050) CPU | percent | 6 | 33.742 | 1.989 | 72.629 | 1.989 | 2.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10050) rss_mb | MB | 7 | 353.706 | 261.309 | 385.375 | 385.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10050) main thread run-queue wait | percent | 6 | 4.575 | 0.003 | 15.189 | 0.003 | 0.277570 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10050) vms_mb | MB | 7 | 8963.788 | 1656.477 | 10205.750 | 10205.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 10073) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 10073) vms_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10077) rss_mb | MB | 1 | 193.605 | 193.605 | 193.605 | 193.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10077) vms_mb | MB | 1 | 1614.473 | 1614.473 | 1614.473 | 1614.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10101) CPU | percent | 10 | 20.751 | 0.995 | 69.459 | 8.950 | 2.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10101) rss_mb | MB | 11 | 371.092 | 296.227 | 391.141 | 391.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10101) main thread run-queue wait | percent | 10 | 3.308 | 0.000 | 19.493 | 0.115 | 0.332981 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10101) vms_mb | MB | 11 | 9419.000 | 1690.754 | 10207.418 | 10207.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10122) rss_mb | MB | 1 | 217.926 | 217.926 | 217.926 | 217.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10122) vms_mb | MB | 1 | 1623.734 | 1623.734 | 1623.734 | 1623.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10148) CPU | percent | 25 | 11.484 | 0.994 | 72.420 | 1.989 | 2.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10148) rss_mb | MB | 26 | 379.426 | 231.801 | 393.449 | 393.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10148) main thread run-queue wait | percent | 25 | 1.845 | 0.001 | 15.763 | 0.007 | 0.468601 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10148) vms_mb | MB | 26 | 9547.870 | 1636.059 | 10206.438 | 10206.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10168) CPU | percent | 1 | 60.347 | 60.347 | 60.347 | 60.347 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10168) rss_mb | MB | 2 | 203.939 | 157.492 | 250.387 | 250.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10168) main thread run-queue wait | percent | 1 | 19.384 | 19.384 | 19.384 | 19.384 | 0.195935 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10168) vms_mb | MB | 2 | 1481.006 | 1314.680 | 1647.332 | 1647.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10180) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10180) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10181) rss_mb | MB | 1 | 7.785 | 7.785 | 7.785 | 7.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10181) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 10194) rss_mb | MB | 1 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 10194) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 10195) rss_mb | MB | 1 | 20.906 | 20.906 | 20.906 | 20.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 10195) vms_mb | MB | 1 | 213.461 | 213.461 | 213.461 | 213.461 | n/a | n/a |
| sleep (PID 10206) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10206) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10206) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10206) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10206) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10206) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10212) CPU | percent | 17 | 13.313 | 0.994 | 82.314 | 1.989 | 2.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10212) rss_mb | MB | 18 | 379.691 | 288.543 | 394.191 | 394.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10212) main thread run-queue wait | percent | 17 | 0.370 | 0.005 | 3.770 | 0.041 | 0.063464 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10212) vms_mb | MB | 18 | 9724.833 | 1683.746 | 10207.449 | 10207.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 10244) rss_mb | MB | 1 | 2.031 | 2.031 | 2.031 | 2.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 10244) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 10245) rss_mb | MB | 1 | 0.281 | 0.281 | 0.281 | 0.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 10245) vms_mb | MB | 1 | 3.152 | 3.152 | 3.152 | 3.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10251) CPU | percent | 8 | 32.538 | 2.982 | 70.454 | 2.984 | 2.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10251) rss_mb | MB | 9 | 350.625 | 188.172 | 393.855 | 393.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10251) main thread run-queue wait | percent | 8 | 2.667 | 0.004 | 16.590 | 0.009 | 0.225856 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10251) vms_mb | MB | 9 | 8305.068 | 1594.219 | 10209.453 | 10209.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10276) rss_mb | MB | 1 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10276) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10277) rss_mb | MB | 1 | 9.164 | 9.164 | 9.164 | 9.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10277) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10281) rss_mb | MB | 1 | 236.398 | 236.398 | 236.398 | 236.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10281) vms_mb | MB | 1 | 1636.602 | 1636.602 | 1636.602 | 1636.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10300) CPU | percent | 13 | 18.415 | 0.994 | 74.478 | 2.983 | 2.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10300) rss_mb | MB | 14 | 372.576 | 261.922 | 392.723 | 392.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10300) main thread run-queue wait | percent | 13 | 2.249 | 0.004 | 13.669 | 0.010 | 0.296732 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10300) vms_mb | MB | 14 | 9584.278 | 1656.988 | 10208.918 | 10208.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10319) CPU | percent | 1 | 61.521 | 61.521 | 61.521 | 61.521 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10319) rss_mb | MB | 2 | 210.094 | 160.945 | 259.242 | 259.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10319) main thread run-queue wait | percent | 1 | 14.800 | 14.800 | 14.800 | 14.800 | 0.149156 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10319) vms_mb | MB | 2 | 1486.426 | 1317.723 | 1655.129 | 1655.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10331) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10331) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10332) rss_mb | MB | 1 | 6.965 | 6.965 | 6.965 | 6.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10332) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10347) CPU | percent | 13 | 23.463 | 1.988 | 88.452 | 6.962 | 3.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10347) rss_mb | MB | 14 | 359.583 | 157.832 | 390.887 | 390.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10347) main thread run-queue wait | percent | 13 | 2.960 | 0.005 | 21.176 | 0.010 | 0.387452 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10347) vms_mb | MB | 14 | 8954.722 | 1314.289 | 10207.125 | 10207.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10369) CPU | percent | 1 | 66.541 | 66.541 | 66.541 | 66.541 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10369) rss_mb | MB | 2 | 240.939 | 193.016 | 288.863 | 288.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10369) main thread run-queue wait | percent | 1 | 18.130 | 18.130 | 18.130 | 18.130 | 0.182546 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10369) vms_mb | MB | 2 | 1641.012 | 1598.723 | 1683.301 | 1683.301 | n/a | n/a |
| sleep (PID 10469) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10469) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10469) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10469) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10469) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10469) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10475) CPU | percent | 11 | 23.097 | 1.986 | 77.540 | 5.967 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10475) rss_mb | MB | 12 | 363.048 | 229.309 | 390.164 | 390.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10475) main thread run-queue wait | percent | 11 | 3.408 | 0.006 | 22.373 | 0.011 | 0.377719 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10475) vms_mb | MB | 12 | 8780.508 | 1636.035 | 10205.578 | 10205.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10492) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10492) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10493) rss_mb | MB | 1 | 8.855 | 8.855 | 8.855 | 8.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10493) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10494) CPU | percent | 1 | 58.450 | 58.450 | 58.450 | 58.450 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10494) rss_mb | MB | 2 | 134.422 | 39.695 | 229.148 | 229.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10494) main thread run-queue wait | percent | 1 | 12.098 | 12.098 | 12.098 | 12.098 | 0.122114 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10494) vms_mb | MB | 2 | 1401.992 | 1172.379 | 1631.605 | 1631.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 10506) rss_mb | MB | 1 | 50.398 | 50.398 | 50.398 | 50.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 10506) vms_mb | MB | 1 | 864.867 | 864.867 | 864.867 | 864.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10522) CPU | percent | 10 | 21.821 | 1.987 | 76.295 | 1.987 | 2.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10522) rss_mb | MB | 11 | 362.811 | 269.812 | 382.535 | 382.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10522) main thread run-queue wait | percent | 10 | 0.959 | 0.002 | 6.571 | 0.012 | 0.096592 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10522) vms_mb | MB | 11 | 9413.518 | 1665.254 | 10203.727 | 10203.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10552) rss_mb | MB | 1 | 142.438 | 142.438 | 142.438 | 142.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10552) vms_mb | MB | 1 | 1298.680 | 1298.680 | 1298.680 | 1298.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10571) CPU | percent | 13 | 23.119 | 0.994 | 90.237 | 0.995 | 3.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10571) rss_mb | MB | 14 | 364.540 | 154.344 | 397.367 | 397.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10571) main thread run-queue wait | percent | 13 | 2.467 | 0.000 | 21.779 | 0.004 | 0.323639 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10571) vms_mb | MB | 14 | 8975.437 | 1499.465 | 10209.594 | 10209.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10594) CPU | percent | 1 | 44.576 | 44.576 | 44.576 | 44.576 | 0.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10594) rss_mb | MB | 2 | 149.080 | 83.531 | 214.629 | 214.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10594) main thread run-queue wait | percent | 1 | 20.272 | 20.272 | 20.272 | 20.272 | 0.204648 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10594) vms_mb | MB | 2 | 1453.355 | 1283.695 | 1623.016 | 1623.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10600) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10600) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10601) rss_mb | MB | 1 | 8.895 | 8.895 | 8.895 | 8.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10601) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10620) CPU | percent | 12 | 25.130 | 0.994 | 90.321 | 0.994 | 3.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10620) rss_mb | MB | 13 | 359.838 | 160.852 | 394.469 | 394.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10620) main thread run-queue wait | percent | 12 | 3.501 | 0.007 | 26.030 | 0.012 | 0.424332 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10620) vms_mb | MB | 13 | 8865.870 | 1317.719 | 10209.066 | 10209.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10641) CPU | percent | 1 | 53.550 | 53.550 | 53.550 | 53.550 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10641) rss_mb | MB | 2 | 223.756 | 186.617 | 260.895 | 260.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10641) main thread run-queue wait | percent | 1 | 20.429 | 20.429 | 20.429 | 20.429 | 0.206007 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10641) vms_mb | MB | 2 | 1625.260 | 1593.723 | 1656.797 | 1656.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10669) CPU | percent | 10 | 23.641 | 1.986 | 75.515 | 1.988 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10669) rss_mb | MB | 11 | 367.968 | 259.418 | 394.566 | 394.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10669) main thread run-queue wait | percent | 10 | 2.899 | 0.008 | 16.078 | 0.025 | 0.311774 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10669) vms_mb | MB | 11 | 9405.382 | 1656.043 | 10206.809 | 10206.809 | n/a | n/a |
| sleep (PID 10689) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10689) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10689) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10689) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10689) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10689) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10693) CPU | percent | 1 | 62.108 | 62.108 | 62.108 | 62.108 | 0.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10693) rss_mb | MB | 2 | 248.504 | 195.254 | 301.754 | 301.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10693) main thread run-queue wait | percent | 1 | 17.636 | 17.636 | 17.636 | 17.636 | 0.198767 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10693) vms_mb | MB | 2 | 1670.949 | 1615.535 | 1726.363 | 1726.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10719) CPU | percent | 12 | 24.732 | 0.994 | 91.286 | 0.994 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10719) rss_mb | MB | 13 | 357.812 | 147.414 | 392.195 | 392.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10719) main thread run-queue wait | percent | 12 | 3.132 | 0.001 | 22.867 | 0.001 | 0.379263 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10719) vms_mb | MB | 13 | 8861.072 | 1303.598 | 10210.480 | 10210.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10741) CPU | percent | 1 | 45.521 | 45.521 | 45.521 | 45.521 | 0.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10741) rss_mb | MB | 2 | 133.326 | 47.355 | 219.297 | 219.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10741) main thread run-queue wait | percent | 1 | 22.718 | 22.718 | 22.718 | 22.718 | 0.229576 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10741) vms_mb | MB | 2 | 1431.418 | 1238.609 | 1624.227 | 1624.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 10748) rss_mb | MB | 1 | 47.730 | 47.730 | 47.730 | 47.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 10748) vms_mb | MB | 1 | 854.703 | 854.703 | 854.703 | 854.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10767) CPU | percent | 13 | 19.396 | 0.994 | 86.348 | 5.967 | 2.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10767) rss_mb | MB | 14 | 356.170 | 146.957 | 387.031 | 387.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10767) main thread run-queue wait | percent | 13 | 0.618 | 0.004 | 4.838 | 0.013 | 0.080983 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10767) vms_mb | MB | 14 | 8925.321 | 1303.469 | 10197.574 | 10154.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10793) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10793) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10794) rss_mb | MB | 1 | 6.395 | 6.395 | 6.395 | 6.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10794) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10798) rss_mb | MB | 1 | 217.688 | 217.688 | 217.688 | 217.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10798) vms_mb | MB | 1 | 1623.484 | 1623.484 | 1623.484 | 1623.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10817) CPU | percent | 11 | 22.953 | 0.995 | 79.362 | 1.989 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10817) rss_mb | MB | 12 | 363.870 | 217.836 | 391.062 | 391.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10817) main thread run-queue wait | percent | 11 | 3.120 | 0.003 | 21.936 | 0.026 | 0.349056 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10817) vms_mb | MB | 12 | 8780.161 | 1623.762 | 10206.711 | 10206.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10834) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10834) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10835) rss_mb | MB | 1 | 8.121 | 8.121 | 8.121 | 8.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10835) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10836) CPU | percent | 2 | 57.603 | 55.574 | 59.633 | 59.633 | 1.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10836) rss_mb | MB | 3 | 178.970 | 2.590 | 304.559 | 304.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10836) main thread run-queue wait | percent | 2 | 13.534 | 12.474 | 14.594 | 14.594 | 0.274975 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10836) vms_mb | MB | 3 | 1175.727 | 165.203 | 1729.004 | 1729.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10848) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 10848) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10849) rss_mb | MB | 1 | 4.773 | 4.773 | 4.773 | 4.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 10849) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10864) CPU | percent | 34 | 8.291 | 0.994 | 72.549 | 0.994 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10864) rss_mb | MB | 35 | 380.170 | 295.039 | 387.164 | 387.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10864) main thread run-queue wait | percent | 34 | 0.325 | 0.002 | 5.572 | 0.006 | 0.111169 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10864) vms_mb | MB | 35 | 9959.084 | 1689.480 | 10207.453 | 10207.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10895) rss_mb | MB | 1 | 175.090 | 175.090 | 175.090 | 175.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10895) vms_mb | MB | 1 | 1582.223 | 1582.223 | 1582.223 | 1582.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 10910) rss_mb | MB | 1 | 54.898 | 54.898 | 54.898 | 54.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 10910) vms_mb | MB | 1 | 898.574 | 898.574 | 898.574 | 898.574 | n/a | n/a |
| sleep (PID 10913) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10913) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10913) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10913) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10913) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10913) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 10916) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 10916) rss_mb | MB | 7 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 10916) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 10916) vms_mb | MB | 7 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 10917) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 10917) rss_mb | MB | 7 | 11.133 | 11.133 | 11.133 | 11.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 10917) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 10917) vms_mb | MB | 7 | 14.906 | 14.906 | 14.906 | 14.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 10918) CPU | percent | 2 | 28.243 | 0.000 | 56.487 | 0.000 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 10918) rss_mb | MB | 3 | 55.355 | 33.535 | 66.266 | 66.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 10918) main thread run-queue wait | percent | 2 | 0.175 | 0.000 | 0.350 | 0.000 | 0.003533 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 10918) vms_mb | MB | 3 | 67.647 | 42.660 | 80.141 | 80.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 10919) CPU | percent | 3 | 26.423 | 0.000 | 72.325 | 0.000 | 0.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 10919) rss_mb | MB | 4 | 51.483 | 11.164 | 66.297 | 66.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 10919) main thread run-queue wait | percent | 3 | 0.125 | 0.065 | 0.201 | 0.109 | 0.003787 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 10919) vms_mb | MB | 4 | 63.084 | 14.781 | 80.141 | 80.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10933) CPU | percent | 8 | 26.932 | 3.975 | 76.500 | 6.960 | 2.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10933) rss_mb | MB | 9 | 367.814 | 293.984 | 394.309 | 394.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10933) main thread run-queue wait | percent | 8 | 1.004 | 0.003 | 5.364 | 0.016 | 0.081016 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10933) vms_mb | MB | 9 | 9245.006 | 1688.969 | 10209.129 | 10209.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10964) rss_mb | MB | 1 | 159.742 | 159.742 | 159.742 | 159.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10964) vms_mb | MB | 1 | 1315.719 | 1315.719 | 1315.719 | 1315.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10983) CPU | percent | 14 | 21.106 | 1.989 | 77.064 | 7.955 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10983) rss_mb | MB | 15 | 367.868 | 205.672 | 392.305 | 392.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10983) main thread run-queue wait | percent | 14 | 2.912 | 0.002 | 23.452 | 0.038 | 0.411484 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 10983) vms_mb | MB | 15 | 9067.289 | 1618.781 | 10209.965 | 10209.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 10996) rss_mb | MB | 1 | 0.434 | 0.434 | 0.434 | 0.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 10996) vms_mb | MB | 1 | 3.715 | 3.715 | 3.715 | 3.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11002) CPU | percent | 1 | 62.321 | 62.321 | 62.321 | 62.321 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11002) rss_mb | MB | 2 | 251.660 | 209.422 | 293.898 | 293.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11002) main thread run-queue wait | percent | 1 | 26.964 | 26.964 | 26.964 | 26.964 | 0.272582 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11002) vms_mb | MB | 2 | 1654.668 | 1620.500 | 1688.836 | 1688.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11030) CPU | percent | 8 | 34.027 | 3.975 | 74.543 | 9.946 | 2.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11030) rss_mb | MB | 9 | 351.434 | 186.328 | 395.988 | 395.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11030) main thread run-queue wait | percent | 8 | 4.277 | 0.005 | 23.487 | 0.128 | 0.344979 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11030) vms_mb | MB | 9 | 8304.271 | 1593.469 | 10211.031 | 10211.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11053) CPU | percent | 1 | 48.553 | 48.553 | 48.553 | 48.553 | 0.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11053) rss_mb | MB | 2 | 211.443 | 170.430 | 252.457 | 252.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11053) main thread run-queue wait | percent | 1 | 22.251 | 22.251 | 22.251 | 22.251 | 0.224563 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11053) vms_mb | MB | 2 | 1614.016 | 1579.473 | 1648.559 | 1648.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11079) CPU | percent | 12 | 20.567 | 0.993 | 76.712 | 4.923 | 2.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11079) rss_mb | MB | 13 | 367.177 | 244.863 | 388.578 | 388.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11079) main thread run-queue wait | percent | 12 | 1.097 | 0.005 | 6.315 | 0.137 | 0.135853 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11079) vms_mb | MB | 13 | 8897.304 | 1640.777 | 10209.832 | 10209.832 | n/a | n/a |
| sleep (PID 11089) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11089) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11089) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11089) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11089) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11089) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11109) CPU | percent | 1 | 76.917 | 76.917 | 76.917 | 76.917 | 0.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11109) rss_mb | MB | 2 | 224.439 | 153.402 | 295.477 | 295.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11109) main thread run-queue wait | percent | 1 | 10.186 | 10.186 | 10.186 | 10.186 | 0.107262 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11109) vms_mb | MB | 2 | 1499.604 | 1309.238 | 1689.969 | 1689.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11151) CPU | percent | 13 | 26.945 | 1.988 | 93.213 | 9.937 | 3.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11151) rss_mb | MB | 14 | 361.691 | 158.949 | 395.641 | 395.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11151) main thread run-queue wait | percent | 13 | 3.829 | 0.004 | 17.513 | 0.027 | 0.501578 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11151) vms_mb | MB | 14 | 8968.895 | 1499.965 | 10211.191 | 10211.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11172) CPU | percent | 1 | 61.612 | 61.612 | 61.612 | 61.612 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11172) rss_mb | MB | 2 | 209.682 | 166.707 | 252.656 | 252.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11172) main thread run-queue wait | percent | 1 | 17.715 | 17.715 | 17.715 | 17.715 | 0.178266 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11172) vms_mb | MB | 2 | 1613.154 | 1577.973 | 1648.336 | 1648.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11184) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11184) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11185) rss_mb | MB | 1 | 7.367 | 7.367 | 7.367 | 7.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11185) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11216) CPU | percent | 12 | 26.653 | 1.988 | 78.071 | 2.984 | 3.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11216) rss_mb | MB | 13 | 365.715 | 229.105 | 392.227 | 392.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11216) main thread run-queue wait | percent | 12 | 2.245 | 0.001 | 14.828 | 0.001 | 0.272163 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11216) vms_mb | MB | 13 | 8890.448 | 1631.766 | 10210.301 | 10210.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 11229) rss_mb | MB | 1 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 11229) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 11230) rss_mb | MB | 1 | 1.625 | 1.625 | 1.625 | 1.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 11230) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11239) rss_mb | MB | 1 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11239) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11240) rss_mb | MB | 1 | 7.242 | 7.242 | 7.242 | 7.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11240) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11246) CPU | percent | 1 | 84.201 | 84.201 | 84.201 | 84.201 | 0.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11246) rss_mb | MB | 2 | 231.297 | 166.797 | 295.797 | 295.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11246) main thread run-queue wait | percent | 1 | 8.293 | 8.293 | 8.293 | 8.293 | 0.083716 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11246) vms_mb | MB | 2 | 1633.977 | 1577.723 | 1690.230 | 1690.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11265) CPU | percent | 12 | 18.649 | 1.989 | 73.545 | 1.989 | 2.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11265) rss_mb | MB | 13 | 376.294 | 279.930 | 394.734 | 394.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11265) main thread run-queue wait | percent | 12 | 2.204 | 0.001 | 15.254 | 0.005 | 0.268545 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11265) vms_mb | MB | 13 | 9542.209 | 1675.512 | 10211.367 | 10211.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 11285) rss_mb | MB | 1 | 49.172 | 49.172 | 49.172 | 49.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 11285) vms_mb | MB | 1 | 847.215 | 847.215 | 847.215 | 847.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11287) rss_mb | MB | 1 | 211.109 | 211.109 | 211.109 | 211.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11287) vms_mb | MB | 1 | 1622.730 | 1622.730 | 1622.730 | 1622.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11316) CPU | percent | 12 | 17.304 | 0.994 | 68.539 | 1.987 | 2.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11316) rss_mb | MB | 13 | 377.261 | 296.043 | 395.418 | 395.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11316) main thread run-queue wait | percent | 12 | 3.238 | 0.003 | 23.087 | 0.011 | 0.391237 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11316) vms_mb | MB | 13 | 9542.435 | 1690.504 | 10210.816 | 10210.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11335) CPU | percent | 1 | 63.564 | 63.564 | 63.564 | 63.564 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11335) rss_mb | MB | 2 | 232.580 | 186.164 | 278.996 | 278.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11335) main thread run-queue wait | percent | 1 | 19.043 | 19.043 | 19.043 | 19.043 | 0.191733 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11335) vms_mb | MB | 2 | 1633.633 | 1593.723 | 1673.543 | 1673.543 | n/a | n/a |
| sleep (PID 11359) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11359) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11359) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11359) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11359) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11359) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11368) CPU | percent | 13 | 21.394 | 0.994 | 72.412 | 1.989 | 2.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11368) rss_mb | MB | 14 | 365.512 | 178.660 | 396.680 | 396.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11368) main thread run-queue wait | percent | 13 | 2.086 | 0.004 | 13.827 | 0.005 | 0.273226 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11368) vms_mb | MB | 14 | 8985.896 | 1590.969 | 10211.238 | 10211.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11392) CPU | percent | 1 | 50.611 | 50.611 | 50.611 | 50.611 | 0.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11392) rss_mb | MB | 2 | 202.146 | 161.145 | 243.148 | 243.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11392) main thread run-queue wait | percent | 1 | 12.451 | 12.451 | 12.451 | 12.451 | 0.125462 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11392) vms_mb | MB | 2 | 1478.412 | 1317.723 | 1639.102 | 1639.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11420) CPU | percent | 14 | 21.057 | 1.988 | 91.436 | 1.990 | 2.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11420) rss_mb | MB | 15 | 356.991 | 84.520 | 392.703 | 391.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11420) main thread run-queue wait | percent | 14 | 2.473 | 0.004 | 20.189 | 0.004 | 0.349089 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11420) vms_mb | MB | 15 | 9043.651 | 1283.598 | 10211.715 | 10210.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11441) CPU | percent | 1 | 54.524 | 54.524 | 54.524 | 54.524 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11441) rss_mb | MB | 2 | 230.361 | 188.848 | 271.875 | 271.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11441) main thread run-queue wait | percent | 1 | 25.315 | 25.315 | 25.315 | 25.315 | 0.255356 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11441) vms_mb | MB | 2 | 1630.760 | 1594.223 | 1667.297 | 1667.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11472) CPU | percent | 14 | 20.512 | 0.995 | 78.366 | 4.965 | 2.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11472) rss_mb | MB | 15 | 367.362 | 175.598 | 396.039 | 395.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11472) main thread run-queue wait | percent | 14 | 1.842 | 0.000 | 12.889 | 0.013 | 0.260365 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11472) vms_mb | MB | 15 | 9070.167 | 1589.969 | 10215.816 | 10214.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11499) rss_mb | MB | 1 | 172.844 | 172.844 | 172.844 | 172.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11499) vms_mb | MB | 1 | 1579.973 | 1579.973 | 1579.973 | 1579.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11521) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11521) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11522) rss_mb | MB | 1 | 7.254 | 7.254 | 7.254 | 7.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11522) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11526) CPU | percent | 12 | 25.321 | 1.986 | 75.319 | 1.989 | 3.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11526) rss_mb | MB | 13 | 365.277 | 206.176 | 393.707 | 393.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11526) main thread run-queue wait | percent | 12 | 2.675 | 0.005 | 17.387 | 0.008 | 0.323579 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11526) vms_mb | MB | 13 | 8896.184 | 1619.816 | 10213.891 | 10213.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11550) CPU | percent | 1 | 42.615 | 42.615 | 42.615 | 42.615 | 0.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11550) rss_mb | MB | 2 | 197.770 | 166.855 | 228.684 | 228.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11550) main thread run-queue wait | percent | 1 | 15.381 | 15.381 | 15.381 | 15.381 | 0.155202 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11550) vms_mb | MB | 2 | 1604.975 | 1577.973 | 1631.977 | 1631.977 | n/a | n/a |
| sleep (PID 11572) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11572) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11572) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11572) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11572) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11572) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11654) CPU | percent | 13 | 21.220 | 1.987 | 87.328 | 1.987 | 2.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11654) rss_mb | MB | 14 | 372.076 | 255.305 | 393.977 | 393.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11654) main thread run-queue wait | percent | 13 | 3.095 | 0.000 | 31.395 | 0.000 | 0.405497 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11654) vms_mb | MB | 14 | 8990.351 | 1651.285 | 10212.715 | 10212.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11673) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11673) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11678) CPU | percent | 1 | 55.573 | 55.573 | 55.573 | 55.573 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11678) rss_mb | MB | 2 | 217.902 | 176.070 | 259.734 | 259.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11678) main thread run-queue wait | percent | 1 | 26.778 | 26.778 | 26.778 | 26.778 | 0.269836 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11678) vms_mb | MB | 2 | 1623.031 | 1590.473 | 1655.590 | 1655.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11688) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11688) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11689) rss_mb | MB | 1 | 7.859 | 7.859 | 7.859 | 7.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11689) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11704) CPU | percent | 13 | 26.058 | 1.986 | 98.348 | 1.986 | 3.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11704) rss_mb | MB | 14 | 355.511 | 118.141 | 392.355 | 392.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11704) main thread run-queue wait | percent | 13 | 2.544 | 0.002 | 14.247 | 0.015 | 0.338943 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11704) vms_mb | MB | 14 | 8950.223 | 1296.254 | 10209.715 | 10209.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11729) CPU | percent | 1 | 71.987 | 71.987 | 71.987 | 71.987 | 0.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11729) rss_mb | MB | 2 | 240.369 | 185.211 | 295.527 | 295.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11729) main thread run-queue wait | percent | 1 | 12.824 | 12.824 | 12.824 | 12.824 | 0.133609 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11729) vms_mb | MB | 2 | 1641.584 | 1593.223 | 1689.945 | 1689.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11753) CPU | percent | 11 | 23.911 | 0.993 | 75.572 | 3.976 | 2.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11753) rss_mb | MB | 12 | 366.349 | 229.574 | 396.695 | 396.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11753) main thread run-queue wait | percent | 11 | 3.217 | 0.003 | 24.478 | 0.082 | 0.357058 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11753) vms_mb | MB | 12 | 8783.894 | 1632.527 | 10210.609 | 10210.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11772) CPU | percent | 1 | 59.421 | 59.421 | 59.421 | 59.421 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11772) rss_mb | MB | 2 | 250.047 | 204.387 | 295.707 | 295.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11772) main thread run-queue wait | percent | 1 | 22.661 | 22.661 | 22.661 | 22.661 | 0.228823 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11772) vms_mb | MB | 2 | 1654.656 | 1618.738 | 1690.574 | 1690.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11783) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11783) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11801) CPU | percent | 14 | 19.081 | 1.965 | 78.439 | 5.966 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11801) rss_mb | MB | 15 | 372.591 | 234.852 | 396.461 | 396.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11801) main thread run-queue wait | percent | 14 | 2.370 | 0.005 | 14.149 | 0.024 | 0.334181 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11801) vms_mb | MB | 15 | 9070.806 | 1635.535 | 10211.281 | 10211.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11820) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 11820) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11821) rss_mb | MB | 1 | 7.734 | 7.734 | 7.734 | 7.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 11821) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11822) CPU | percent | 2 | 58.063 | 52.680 | 63.447 | 52.680 | 1.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11822) rss_mb | MB | 3 | 178.318 | 2.582 | 302.715 | 302.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11822) main thread run-queue wait | percent | 2 | 15.146 | 13.543 | 16.749 | 16.749 | 0.305115 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11822) vms_mb | MB | 3 | 1176.639 | 165.203 | 1727.852 | 1727.852 | n/a | n/a |
| sleep (PID 11849) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11849) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11849) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11849) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11849) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11849) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11855) CPU | percent | 13 | 21.995 | 0.994 | 71.593 | 1.988 | 2.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11855) rss_mb | MB | 14 | 365.537 | 193.762 | 392.711 | 391.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11855) main thread run-queue wait | percent | 13 | 1.840 | 0.006 | 13.091 | 0.011 | 0.241169 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11855) vms_mb | MB | 14 | 8985.881 | 1614.219 | 10212.484 | 10211.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11879) CPU | percent | 1 | 48.596 | 48.596 | 48.596 | 48.596 | 0.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11879) rss_mb | MB | 2 | 211.180 | 170.109 | 252.250 | 252.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11879) main thread run-queue wait | percent | 1 | 17.816 | 17.816 | 17.816 | 17.816 | 0.179643 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11879) vms_mb | MB | 2 | 1613.654 | 1578.973 | 1648.336 | 1648.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11909) CPU | percent | 40 | 8.104 | 0.994 | 77.369 | 4.972 | 3.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11909) rss_mb | MB | 41 | 387.916 | 275.883 | 399.293 | 399.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11909) main thread run-queue wait | percent | 40 | 0.608 | 0.001 | 12.391 | 0.014 | 0.250043 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11909) vms_mb | MB | 41 | 9997.332 | 1671.520 | 10212.262 | 10212.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11931) rss_mb | MB | 1 | 207.316 | 207.316 | 207.316 | 207.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11931) vms_mb | MB | 1 | 1618.969 | 1618.969 | 1618.969 | 1618.969 | n/a | n/a |
| sleep (PID 11967) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11967) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11967) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11967) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 11967) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11967) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11973) CPU | percent | 7 | 39.278 | 4.973 | 75.290 | 10.938 | 2.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11973) rss_mb | MB | 8 | 342.589 | 181.645 | 392.449 | 392.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11973) main thread run-queue wait | percent | 7 | 3.455 | 0.006 | 16.615 | 0.040 | 0.243746 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11973) vms_mb | MB | 8 | 8063.562 | 1591.469 | 10211.062 | 10211.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11994) CPU | percent | 1 | 48.607 | 48.607 | 48.607 | 48.607 | 0.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11994) rss_mb | MB | 2 | 194.934 | 154.340 | 235.527 | 235.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11994) main thread run-queue wait | percent | 1 | 18.027 | 18.027 | 18.027 | 18.027 | 0.181726 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 11994) vms_mb | MB | 2 | 1567.658 | 1499.469 | 1635.848 | 1635.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12015) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12015) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12016) rss_mb | MB | 1 | 6.922 | 6.922 | 6.922 | 6.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12016) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12020) CPU | percent | 24 | 14.826 | 0.995 | 74.561 | 3.978 | 3.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12020) rss_mb | MB | 25 | 381.265 | 197.301 | 399.422 | 398.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12020) main thread run-queue wait | percent | 24 | 1.797 | 0.001 | 13.954 | 0.014 | 0.435931 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12020) vms_mb | MB | 25 | 9526.305 | 1616.805 | 10215.129 | 10214.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12041) CPU | percent | 1 | 40.559 | 40.559 | 40.559 | 40.559 | 0.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12041) rss_mb | MB | 2 | 187.582 | 155.109 | 220.055 | 220.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12041) main thread run-queue wait | percent | 1 | 13.469 | 13.469 | 13.469 | 13.469 | 0.136150 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12041) vms_mb | MB | 2 | 1467.551 | 1311.121 | 1623.980 | 1623.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12048) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12048) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12049) rss_mb | MB | 1 | 10.059 | 10.059 | 10.059 | 10.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12049) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12068) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12068) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12069) rss_mb | MB | 1 | 21.598 | 21.598 | 21.598 | 21.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12069) vms_mb | MB | 1 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12076) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12076) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12081) CPU | percent | 12 | 23.412 | 0.995 | 74.406 | 4.968 | 2.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12081) rss_mb | MB | 13 | 363.691 | 194.859 | 392.055 | 392.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12081) main thread run-queue wait | percent | 12 | 2.934 | 0.006 | 25.527 | 0.006 | 0.354928 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12081) vms_mb | MB | 13 | 8891.735 | 1614.969 | 10210.758 | 10210.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12103) CPU | percent | 1 | 54.537 | 54.537 | 54.537 | 54.537 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12103) rss_mb | MB | 2 | 256.777 | 218.910 | 294.645 | 294.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12103) main thread run-queue wait | percent | 1 | 23.061 | 23.061 | 23.061 | 23.061 | 0.232569 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12103) vms_mb | MB | 2 | 1656.965 | 1624.297 | 1689.633 | 1689.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12113) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12113) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12114) rss_mb | MB | 1 | 6.957 | 6.957 | 6.957 | 6.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12114) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12126) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12126) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12127) rss_mb | MB | 1 | 10.680 | 10.680 | 10.680 | 10.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12127) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12131) CPU | percent | 13 | 22.061 | 1.986 | 83.319 | 1.988 | 2.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12131) rss_mb | MB | 14 | 371.995 | 229.195 | 396.566 | 396.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12131) main thread run-queue wait | percent | 13 | 1.284 | 0.004 | 8.522 | 0.009 | 0.168228 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12131) vms_mb | MB | 14 | 8990.558 | 1632.289 | 10212.223 | 10212.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12162) rss_mb | MB | 1 | 188.512 | 188.512 | 188.512 | 188.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12162) vms_mb | MB | 1 | 1593.973 | 1593.973 | 1593.973 | 1593.973 | n/a | n/a |
| sleep (PID 12177) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12177) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12177) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12177) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12177) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12177) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12183) CPU | percent | 14 | 25.726 | 1.987 | 91.240 | 8.935 | 3.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12183) rss_mb | MB | 15 | 347.971 | 23.469 | 386.574 | 386.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12183) main thread run-queue wait | percent | 14 | 2.117 | 0.005 | 14.448 | 0.036 | 0.307383 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12183) vms_mb | MB | 15 | 8963.436 | 165.848 | 10213.668 | 10213.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12207) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12207) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12208) rss_mb | MB | 1 | 9.941 | 9.941 | 9.941 | 9.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12208) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12212) CPU | percent | 1 | 68.542 | 68.542 | 68.542 | 68.542 | 0.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12212) rss_mb | MB | 2 | 132.229 | 2.590 | 261.867 | 261.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12212) main thread run-queue wait | percent | 1 | 15.842 | 15.842 | 15.842 | 15.842 | 0.171036 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12212) vms_mb | MB | 2 | 911.137 | 165.203 | 1657.070 | 1657.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12232) CPU | percent | 11 | 26.424 | 1.989 | 69.479 | 4.972 | 2.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12232) rss_mb | MB | 12 | 363.601 | 211.156 | 395.707 | 395.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12232) main thread run-queue wait | percent | 11 | 4.223 | 0.007 | 22.948 | 0.056 | 0.473002 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12232) vms_mb | MB | 12 | 8778.066 | 1622.539 | 10211.984 | 10211.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12253) CPU | percent | 1 | 65.116 | 65.116 | 65.116 | 65.116 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12253) rss_mb | MB | 2 | 241.102 | 194.191 | 288.012 | 288.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12253) main thread run-queue wait | percent | 1 | 17.999 | 17.999 | 17.999 | 17.999 | 0.182431 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12253) vms_mb | MB | 2 | 1648.533 | 1614.473 | 1682.594 | 1682.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12301) CPU | percent | 13 | 21.544 | 0.994 | 75.423 | 0.994 | 2.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12301) rss_mb | MB | 14 | 365.221 | 188.891 | 396.793 | 395.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12301) main thread run-queue wait | percent | 13 | 3.003 | 0.001 | 20.534 | 0.008 | 0.395209 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12301) vms_mb | MB | 14 | 8979.093 | 1594.219 | 10208.988 | 10207.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12321) CPU | percent | 1 | 70.015 | 70.015 | 70.015 | 70.015 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12321) rss_mb | MB | 2 | 244.182 | 193.672 | 294.691 | 294.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12321) main thread run-queue wait | percent | 1 | 20.301 | 20.301 | 20.301 | 20.301 | 0.205868 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12321) vms_mb | MB | 2 | 1651.775 | 1614.473 | 1689.078 | 1689.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12352) CPU | percent | 13 | 20.466 | 0.994 | 80.356 | 1.989 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12352) rss_mb | MB | 14 | 369.388 | 228.898 | 394.812 | 394.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12352) main thread run-queue wait | percent | 13 | 2.873 | 0.004 | 26.363 | 0.013 | 0.376708 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12352) vms_mb | MB | 14 | 8987.211 | 1635.789 | 10211.348 | 10211.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 12369) rss_mb | MB | 1 | 41.570 | 41.570 | 41.570 | 41.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 12369) vms_mb | MB | 1 | 835.461 | 835.461 | 835.461 | 835.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12374) CPU | percent | 1 | 50.527 | 50.527 | 50.527 | 50.527 | 0.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12374) rss_mb | MB | 2 | 211.795 | 169.367 | 254.223 | 254.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12374) main thread run-queue wait | percent | 1 | 30.253 | 30.253 | 30.253 | 30.253 | 0.305369 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12374) vms_mb | MB | 2 | 1614.275 | 1578.723 | 1649.828 | 1649.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12400) CPU | percent | 14 | 18.133 | 1.988 | 80.496 | 1.989 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12400) rss_mb | MB | 15 | 381.312 | 261.207 | 401.551 | 400.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12400) main thread run-queue wait | percent | 14 | 0.942 | 0.002 | 7.386 | 0.008 | 0.133130 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12400) vms_mb | MB | 15 | 9631.343 | 1656.754 | 10213.914 | 10212.895 | n/a | n/a |
| sleep (PID 12410) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12410) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12410) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12410) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12410) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12410) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12433) rss_mb | MB | 1 | 236.367 | 236.367 | 236.367 | 236.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12433) vms_mb | MB | 1 | 1636.605 | 1636.605 | 1636.605 | 1636.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12456) CPU | percent | 14 | 22.554 | 1.985 | 88.462 | 3.978 | 3.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12456) rss_mb | MB | 15 | 367.377 | 161.184 | 400.504 | 399.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12456) main thread run-queue wait | percent | 14 | 1.712 | 0.002 | 16.288 | 0.018 | 0.241915 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12456) vms_mb | MB | 15 | 9047.344 | 1317.719 | 10214.219 | 10213.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12480) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12480) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12484) rss_mb | MB | 1 | 187.043 | 187.043 | 187.043 | 187.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12484) vms_mb | MB | 1 | 1593.723 | 1593.723 | 1593.723 | 1593.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12504) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12504) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12505) rss_mb | MB | 1 | 9.230 | 9.230 | 9.230 | 9.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12505) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12509) CPU | percent | 145 | 5.138 | 0.992 | 71.553 | 1.986 | 7.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12509) rss_mb | MB | 146 | 385.882 | 193.680 | 401.867 | 381.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12509) main thread run-queue wait | percent | 145 | 0.406 | 0.001 | 15.547 | 0.006 | 0.594466 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12509) vms_mb | MB | 146 | 10087.343 | 1614.219 | 10216.289 | 10196.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12530) CPU | percent | 1 | 67.248 | 67.248 | 67.248 | 67.248 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12530) rss_mb | MB | 2 | 245.990 | 198.820 | 293.160 | 293.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12530) main thread run-queue wait | percent | 1 | 14.700 | 14.700 | 14.700 | 14.700 | 0.148647 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12530) vms_mb | MB | 2 | 1652.922 | 1617.504 | 1688.340 | 1688.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12541) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12541) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12542) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12542) vms_mb | MB | 1 | 0.355 | 0.355 | 0.355 | 0.355 | n/a | n/a |
| sleep (PID 12559) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12559) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12559) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12559) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12559) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12559) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12659) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12659) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12660) rss_mb | MB | 1 | 17.883 | 17.883 | 17.883 | 17.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12660) vms_mb | MB | 1 | 23.184 | 23.184 | 23.184 | 23.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12690) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12690) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12691) rss_mb | MB | 1 | 17.043 | 17.043 | 17.043 | 17.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12691) vms_mb | MB | 1 | 22.180 | 22.180 | 22.180 | 22.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12697) rss_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12697) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12698) rss_mb | MB | 1 | 13.234 | 13.234 | 13.234 | 13.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12698) vms_mb | MB | 1 | 207.250 | 207.250 | 207.250 | 207.250 | n/a | n/a |
| sleep (PID 12708) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12708) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12708) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12708) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 12708) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12708) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12711) CPU | percent | 1 | 64.450 | 64.450 | 64.450 | 64.450 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12711) rss_mb | MB | 2 | 45.443 | 24.918 | 65.969 | 65.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12711) main thread run-queue wait | percent | 1 | 0.257 | 0.257 | 0.257 | 0.257 | 0.002592 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12711) vms_mb | MB | 2 | 55.867 | 31.625 | 80.109 | 80.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12733) CPU | percent | 1 | 54.665 | 54.665 | 54.665 | 54.665 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12733) rss_mb | MB | 2 | 51.850 | 37.797 | 65.902 | 65.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12733) main thread run-queue wait | percent | 1 | 0.439 | 0.439 | 0.439 | 0.439 | 0.004414 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12733) vms_mb | MB | 2 | 63.527 | 45.938 | 81.117 | 81.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12741) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12741) rss_mb | MB | 4 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12741) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12741) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12742) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12742) rss_mb | MB | 4 | 10.883 | 10.883 | 10.883 | 10.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12742) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000012 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12742) vms_mb | MB | 4 | 14.871 | 14.871 | 14.871 | 14.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12743) CPU | percent | 1 | 69.558 | 69.558 | 69.558 | 69.558 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12743) rss_mb | MB | 2 | 42.332 | 18.703 | 65.961 | 65.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12743) main thread run-queue wait | percent | 1 | 0.106 | 0.106 | 0.106 | 0.106 | 0.001085 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12743) vms_mb | MB | 2 | 51.779 | 24.000 | 79.559 | 79.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12746) CPU | percent | 1 | 52.487 | 52.487 | 52.487 | 52.487 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12746) rss_mb | MB | 2 | 51.357 | 36.609 | 66.105 | 66.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12746) main thread run-queue wait | percent | 1 | 0.299 | 0.299 | 0.299 | 0.299 | 0.003017 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12746) vms_mb | MB | 2 | 62.756 | 45.395 | 80.117 | 80.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12767) rss_mb | MB | 1 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12767) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12768) rss_mb | MB | 1 | 53.125 | 53.125 | 53.125 | 53.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12768) vms_mb | MB | 1 | 273.570 | 273.570 | 273.570 | 273.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12782) CPU | percent | 17 | 17.412 | 0.994 | 86.423 | 2.984 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12782) rss_mb | MB | 18 | 364.077 | 156.098 | 390.867 | 390.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12782) main thread run-queue wait | percent | 17 | 0.841 | 0.002 | 6.064 | 0.006 | 0.144081 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12782) vms_mb | MB | 18 | 9206.694 | 1499.465 | 10190.250 | 10158.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12805) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12805) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12806) rss_mb | MB | 1 | 5.641 | 5.641 | 5.641 | 5.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12806) vms_mb | MB | 1 | 11.645 | 11.645 | 11.645 | 11.645 | n/a | n/a |
| pgrep (PID 12807) rss_mb | MB | 1 | 3.465 | 3.465 | 3.465 | 3.465 | n/a | n/a |
| pgrep (PID 12807) vms_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sleep (PID 12808) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12808) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12808) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12808) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12808) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12808) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12814) rss_mb | MB | 1 | 298.094 | 298.094 | 298.094 | 298.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12814) vms_mb | MB | 1 | 1692.848 | 1692.848 | 1692.848 | 1692.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12830) rss_mb | MB | 1 | 2.598 | 2.598 | 2.598 | 2.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12830) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12831) rss_mb | MB | 1 | 8.473 | 8.473 | 8.473 | 8.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12831) vms_mb | MB | 1 | 13.273 | 13.273 | 13.273 | 13.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12845) CPU | percent | 38 | 9.483 | 0.993 | 80.452 | 1.987 | 3.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12845) rss_mb | MB | 39 | 380.619 | 252.012 | 389.848 | 389.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12845) main thread run-queue wait | percent | 38 | 1.814 | 0.000 | 20.504 | 0.005 | 0.694685 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12845) vms_mb | MB | 39 | 9772.058 | 1648.781 | 10211.312 | 10211.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12868) CPU | percent | 1 | 55.503 | 55.503 | 55.503 | 55.503 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12868) rss_mb | MB | 2 | 225.742 | 187.609 | 263.875 | 263.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12868) main thread run-queue wait | percent | 1 | 17.385 | 17.385 | 17.385 | 17.385 | 0.175406 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12868) vms_mb | MB | 2 | 1626.525 | 1593.973 | 1659.078 | 1659.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12892) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12892) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12893) rss_mb | MB | 1 | 20.996 | 20.996 | 20.996 | 20.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12893) vms_mb | MB | 1 | 212.293 | 212.293 | 212.293 | 212.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12897) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12897) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12898) rss_mb | MB | 1 | 21.879 | 21.879 | 21.879 | 21.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12898) vms_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12904) rss_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12904) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12905) rss_mb | MB | 1 | 20.715 | 20.715 | 20.715 | 20.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12905) vms_mb | MB | 1 | 212.145 | 212.145 | 212.145 | 212.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12916) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12916) rss_mb | MB | 3 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12916) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 12916) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12917) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12917) rss_mb | MB | 3 | 10.809 | 10.809 | 10.809 | 10.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12917) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 12917) vms_mb | MB | 3 | 14.898 | 14.898 | 14.898 | 14.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12918) CPU | percent | 1 | 49.553 | 49.553 | 49.553 | 49.553 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12918) rss_mb | MB | 2 | 51.551 | 36.746 | 66.355 | 66.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12918) main thread run-queue wait | percent | 1 | 0.174 | 0.174 | 0.174 | 0.174 | 0.001755 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12918) vms_mb | MB | 2 | 62.816 | 45.516 | 80.117 | 80.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12920) rss_mb | MB | 1 | 47.020 | 47.020 | 47.020 | 47.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 12920) vms_mb | MB | 1 | 56.117 | 56.117 | 56.117 | 56.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12921) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12921) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12922) rss_mb | MB | 1 | 8.859 | 8.859 | 8.859 | 8.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 12922) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12933) CPU | percent | 22 | 16.593 | 1.986 | 83.098 | 3.974 | 3.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12933) rss_mb | MB | 23 | 376.924 | 260.031 | 390.422 | 390.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12933) main thread run-queue wait | percent | 22 | 1.907 | 0.002 | 20.726 | 0.017 | 0.422750 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12933) vms_mb | MB | 23 | 9473.920 | 1655.805 | 10214.441 | 10214.441 | n/a | n/a |
| sleep (PID 12958) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12958) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12958) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12958) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12958) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12958) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12959) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12959) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12960) rss_mb | MB | 1 | 8.309 | 8.309 | 8.309 | 8.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12960) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12966) rss_mb | MB | 1 | 167.266 | 167.266 | 167.266 | 167.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12966) vms_mb | MB | 1 | 1578.473 | 1578.473 | 1578.473 | 1578.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12989) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12989) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12994) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 12994) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12995) rss_mb | MB | 1 | 10.801 | 10.801 | 10.801 | 10.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 12995) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12999) CPU | percent | 16 | 22.486 | 0.995 | 92.078 | 1.988 | 3.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12999) rss_mb | MB | 17 | 367.480 | 171.547 | 396.363 | 396.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12999) main thread run-queue wait | percent | 16 | 1.125 | 0.002 | 6.984 | 0.007 | 0.181938 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 12999) vms_mb | MB | 17 | 9170.071 | 1579.719 | 10210.164 | 10175.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13039) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13039) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13040) rss_mb | MB | 1 | 9.320 | 9.320 | 9.320 | 9.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13040) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13044) rss_mb | MB | 1 | 168.453 | 168.453 | 168.453 | 168.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13044) vms_mb | MB | 1 | 1578.473 | 1578.473 | 1578.473 | 1578.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13058) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13058) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 13059) rss_mb | MB | 1 | 21.535 | 21.535 | 21.535 | 21.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 13059) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13076) CPU | percent | 20 | 14.301 | 0.995 | 75.497 | 7.956 | 2.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13076) rss_mb | MB | 21 | 381.802 | 278.262 | 395.898 | 395.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13076) main thread run-queue wait | percent | 20 | 1.200 | 0.004 | 18.551 | 0.017 | 0.241616 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13076) vms_mb | MB | 21 | 9794.097 | 1673.230 | 10210.887 | 10210.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13107) CPU | percent | 1 | 72.492 | 72.492 | 72.492 | 72.492 | 0.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13107) rss_mb | MB | 2 | 154.711 | 48.473 | 260.949 | 260.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13107) main thread run-queue wait | percent | 1 | 18.836 | 18.836 | 18.836 | 18.836 | 0.189676 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13107) vms_mb | MB | 2 | 1447.459 | 1238.609 | 1656.309 | 1656.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13134) CPU | percent | 6 | 40.191 | 1.987 | 78.458 | 1.987 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13134) rss_mb | MB | 7 | 345.691 | 229.723 | 384.605 | 384.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13134) main thread run-queue wait | percent | 6 | 3.161 | 0.002 | 10.725 | 0.002 | 0.191279 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13134) vms_mb | MB | 7 | 7764.455 | 1632.559 | 10207.359 | 10207.359 | n/a | n/a |
| sleep (PID 13144) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13144) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13144) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13144) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13144) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13144) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13158) CPU | percent | 1 | 56.498 | 56.498 | 56.498 | 56.498 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13158) rss_mb | MB | 2 | 256.494 | 216.984 | 296.004 | 296.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13158) main thread run-queue wait | percent | 1 | 15.290 | 15.290 | 15.290 | 15.290 | 0.154258 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13158) vms_mb | MB | 2 | 1656.963 | 1623.465 | 1690.461 | 1690.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13168) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13168) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13169) rss_mb | MB | 1 | 10.621 | 10.621 | 10.621 | 10.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13169) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13187) CPU | percent | 6 | 42.694 | 5.963 | 87.217 | 6.950 | 2.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13187) rss_mb | MB | 7 | 306.642 | 10.770 | 381.031 | 380.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13187) main thread run-queue wait | percent | 6 | 1.005 | 0.184 | 2.422 | 1.139 | 0.060773 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13187) vms_mb | MB | 7 | 7530.911 | 165.719 | 10200.281 | 10155.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13238) rss_mb | MB | 1 | 289.832 | 289.832 | 289.832 | 289.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13238) vms_mb | MB | 1 | 1684.570 | 1684.570 | 1684.570 | 1684.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13257) CPU | percent | 5 | 40.531 | 4.958 | 77.555 | 4.958 | 2.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13257) rss_mb | MB | 6 | 356.215 | 294.312 | 384.867 | 384.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13257) main thread run-queue wait | percent | 5 | 2.803 | 0.378 | 5.766 | 3.119 | 0.141151 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13257) vms_mb | MB | 6 | 8764.344 | 1689.281 | 10209.438 | 10209.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13286) rss_mb | MB | 1 | 166.691 | 166.691 | 166.691 | 166.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13286) vms_mb | MB | 1 | 1577.723 | 1577.723 | 1577.723 | 1577.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13305) CPU | percent | 15 | 16.876 | 0.994 | 79.379 | 5.969 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13305) rss_mb | MB | 16 | 377.378 | 272.559 | 392.891 | 392.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13305) main thread run-queue wait | percent | 15 | 1.867 | 0.002 | 10.664 | 0.019 | 0.281983 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13305) vms_mb | MB | 16 | 9667.449 | 1667.750 | 10211.145 | 10211.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13333) rss_mb | MB | 1 | 205.914 | 205.914 | 205.914 | 205.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13333) vms_mb | MB | 1 | 1618.715 | 1618.715 | 1618.715 | 1618.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13347) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13347) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 13348) rss_mb | MB | 1 | 21.754 | 21.754 | 21.754 | 21.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 13348) vms_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13364) CPU | percent | 7 | 36.763 | 3.978 | 76.508 | 8.950 | 2.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13364) rss_mb | MB | 8 | 347.971 | 207.137 | 388.738 | 388.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13364) main thread run-queue wait | percent | 7 | 5.005 | 0.013 | 19.333 | 0.273 | 0.352661 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13364) vms_mb | MB | 8 | 8066.449 | 1619.520 | 10209.594 | 10209.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13384) CPU | percent | 1 | 45.673 | 45.673 | 45.673 | 45.673 | 0.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13384) rss_mb | MB | 2 | 262.703 | 229.168 | 296.238 | 296.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13384) main thread run-queue wait | percent | 1 | 21.317 | 21.317 | 21.317 | 21.317 | 0.214699 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13384) vms_mb | MB | 2 | 1661.596 | 1632.223 | 1690.969 | 1690.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13394) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13394) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13395) rss_mb | MB | 1 | 8.098 | 8.098 | 8.098 | 8.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13395) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13414) CPU | percent | 6 | 45.144 | 5.961 | 83.293 | 5.967 | 2.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13414) rss_mb | MB | 7 | 329.907 | 164.621 | 381.773 | 381.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13414) main thread run-queue wait | percent | 6 | 3.045 | 0.012 | 9.266 | 0.012 | 0.184204 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13414) vms_mb | MB | 7 | 7741.484 | 1572.719 | 10205.023 | 10205.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13577) rss_mb | MB | 1 | 182.398 | 182.398 | 182.398 | 182.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13577) vms_mb | MB | 1 | 1592.973 | 1592.973 | 1592.973 | 1592.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13591) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13591) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13596) CPU | percent | 14 | 25.361 | 1.986 | 80.306 | 9.939 | 3.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13596) rss_mb | MB | 15 | 364.260 | 186.188 | 392.988 | 392.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13596) main thread run-queue wait | percent | 14 | 3.229 | 0.004 | 14.414 | 0.011 | 0.456350 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13596) vms_mb | MB | 15 | 9064.772 | 1593.719 | 10211.766 | 10211.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13617) CPU | percent | 1 | 49.501 | 49.501 | 49.501 | 49.501 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13617) rss_mb | MB | 2 | 118.693 | 29.090 | 208.297 | 208.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13617) main thread run-queue wait | percent | 1 | 11.899 | 11.899 | 11.899 | 11.899 | 0.120189 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13617) vms_mb | MB | 2 | 937.391 | 255.305 | 1619.477 | 1619.477 | n/a | n/a |
| sleep (PID 13637) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13637) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13637) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13637) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 13637) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13637) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 13642) rss_mb | MB | 1 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 13642) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 13643) rss_mb | MB | 1 | 50.324 | 50.324 | 50.324 | 50.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 13643) vms_mb | MB | 1 | 270.051 | 270.051 | 270.051 | 270.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13657) CPU | percent | 6 | 46.465 | 4.970 | 73.561 | 4.970 | 2.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13657) rss_mb | MB | 7 | 345.842 | 230.062 | 383.188 | 383.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13657) main thread run-queue wait | percent | 6 | 5.181 | 0.012 | 16.572 | 0.012 | 0.313614 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13657) vms_mb | MB | 7 | 7763.549 | 1632.766 | 10209.129 | 10208.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13680) CPU | percent | 1 | 42.628 | 42.628 | 42.628 | 42.628 | 0.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13680) rss_mb | MB | 2 | 181.855 | 142.336 | 221.375 | 221.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13680) main thread run-queue wait | percent | 1 | 13.726 | 13.726 | 13.726 | 13.726 | 0.138460 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13680) vms_mb | MB | 2 | 1461.459 | 1298.430 | 1624.488 | 1624.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13706) CPU | percent | 5 | 51.765 | 6.956 | 80.123 | 6.956 | 2.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13706) rss_mb | MB | 6 | 338.051 | 229.535 | 377.469 | 377.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13706) main thread run-queue wait | percent | 5 | 5.126 | 0.945 | 15.092 | 7.072 | 0.258006 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13706) vms_mb | MB | 6 | 7356.800 | 1636.039 | 10207.453 | 10207.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 13719) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 13719) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13731) rss_mb | MB | 1 | 184.477 | 184.477 | 184.477 | 184.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13731) vms_mb | MB | 1 | 1592.973 | 1592.973 | 1592.973 | 1592.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13751) CPU | percent | 13 | 19.781 | 2.981 | 81.486 | 5.966 | 2.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13751) rss_mb | MB | 14 | 371.914 | 270.098 | 390.160 | 390.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13751) main thread run-queue wait | percent | 13 | 1.468 | 0.005 | 13.466 | 0.295 | 0.192277 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13751) vms_mb | MB | 14 | 9588.378 | 1665.723 | 10210.383 | 10210.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13780) rss_mb | MB | 1 | 160.695 | 160.695 | 160.695 | 160.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13780) vms_mb | MB | 1 | 1500.469 | 1500.469 | 1500.469 | 1500.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13792) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13792) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 13793) rss_mb | MB | 1 | 18.609 | 18.609 | 18.609 | 18.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 13793) vms_mb | MB | 1 | 24.570 | 24.570 | 24.570 | 24.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13806) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13806) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13807) rss_mb | MB | 1 | 8.988 | 8.988 | 8.988 | 8.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13807) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13811) CPU | percent | 6 | 45.703 | 2.984 | 83.471 | 2.984 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13811) rss_mb | MB | 7 | 331.891 | 173.012 | 380.816 | 380.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13811) main thread run-queue wait | percent | 6 | 5.427 | 0.049 | 19.073 | 0.049 | 0.328100 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13811) vms_mb | MB | 7 | 7749.850 | 1579.719 | 10202.910 | 10202.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13832) CPU | percent | 1 | 56.505 | 56.505 | 56.505 | 56.505 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13832) rss_mb | MB | 2 | 215.586 | 170.633 | 260.539 | 260.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13832) main thread run-queue wait | percent | 1 | 17.488 | 17.488 | 17.488 | 17.488 | 0.176408 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13832) vms_mb | MB | 2 | 1617.949 | 1579.723 | 1656.176 | 1656.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13858) CPU | percent | 6 | 31.616 | 3.974 | 77.525 | 3.974 | 1.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13858) rss_mb | MB | 7 | 353.864 | 271.152 | 386.535 | 386.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13858) main thread run-queue wait | percent | 6 | 3.647 | 0.003 | 11.402 | 0.003 | 0.220321 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13858) vms_mb | MB | 7 | 8954.763 | 1666.598 | 10205.355 | 10205.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13877) CPU | percent | 1 | 49.664 | 49.664 | 49.664 | 49.664 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13877) rss_mb | MB | 2 | 186.094 | 143.219 | 228.969 | 228.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13877) main thread run-queue wait | percent | 1 | 10.020 | 10.020 | 10.020 | 10.020 | 0.100880 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13877) vms_mb | MB | 2 | 1467.566 | 1299.555 | 1635.578 | 1635.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13889) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13889) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13890) rss_mb | MB | 1 | 7.805 | 7.805 | 7.805 | 7.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13890) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13906) CPU | percent | 5 | 37.688 | 3.975 | 75.419 | 3.975 | 1.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13906) rss_mb | MB | 6 | 347.407 | 261.574 | 383.812 | 383.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13906) main thread run-queue wait | percent | 5 | 5.308 | 0.009 | 13.784 | 0.009 | 0.268048 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13906) vms_mb | MB | 6 | 8733.647 | 1656.750 | 10166.992 | 10166.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13924) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13924) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13925) rss_mb | MB | 1 | 9.141 | 9.141 | 9.141 | 9.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13925) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13926) CPU | percent | 1 | 58.286 | 58.286 | 58.286 | 58.286 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13926) rss_mb | MB | 2 | 164.119 | 92.582 | 235.656 | 235.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13926) main thread run-queue wait | percent | 1 | 15.890 | 15.890 | 15.890 | 15.890 | 0.160847 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13926) vms_mb | MB | 2 | 1459.510 | 1283.695 | 1635.324 | 1635.324 | n/a | n/a |
| sleep (PID 13954) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13954) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13954) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13954) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13954) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13954) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13956) CPU | percent | 11 | 23.398 | 2.970 | 74.552 | 4.973 | 2.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13956) rss_mb | MB | 12 | 362.521 | 220.332 | 390.762 | 390.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13956) main thread run-queue wait | percent | 11 | 1.419 | 0.002 | 5.014 | 0.016 | 0.157739 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13956) vms_mb | MB | 12 | 8774.754 | 1624.293 | 10203.129 | 10203.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13979) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 13979) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13980) rss_mb | MB | 1 | 9.496 | 9.496 | 9.496 | 9.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 13980) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13984) rss_mb | MB | 1 | 272.547 | 272.547 | 272.547 | 272.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 13984) vms_mb | MB | 1 | 1667.547 | 1667.547 | 1667.547 | 1667.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14015) CPU | percent | 14 | 21.104 | 1.988 | 75.407 | 8.950 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14015) rss_mb | MB | 15 | 369.040 | 229.250 | 391.363 | 391.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14015) main thread run-queue wait | percent | 14 | 2.977 | 0.003 | 20.402 | 0.051 | 0.420682 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14015) vms_mb | MB | 15 | 9069.790 | 1632.793 | 10212.012 | 10211.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14039) CPU | percent | 1 | 42.660 | 42.660 | 42.660 | 42.660 | 0.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14039) rss_mb | MB | 2 | 190.617 | 152.008 | 229.227 | 229.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14039) main thread run-queue wait | percent | 1 | 23.033 | 23.033 | 23.033 | 23.033 | 0.232161 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14039) vms_mb | MB | 2 | 1565.281 | 1499.219 | 1631.344 | 1631.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 14061) rss_mb | MB | 1 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 14061) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 14062) rss_mb | MB | 1 | 13.531 | 13.531 | 13.531 | 13.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 14062) vms_mb | MB | 1 | 207.367 | 207.367 | 207.367 | 207.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14076) CPU | percent | 6 | 44.646 | 5.965 | 66.450 | 5.965 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14076) rss_mb | MB | 7 | 342.027 | 211.887 | 381.934 | 381.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14076) main thread run-queue wait | percent | 6 | 6.009 | 0.010 | 14.964 | 0.010 | 0.363798 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14076) vms_mb | MB | 7 | 7759.066 | 1622.551 | 10202.980 | 10202.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14098) CPU | percent | 1 | 62.344 | 62.344 | 62.344 | 62.344 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14098) rss_mb | MB | 2 | 209.094 | 158.176 | 260.012 | 260.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14098) main thread run-queue wait | percent | 1 | 14.091 | 14.091 | 14.091 | 14.091 | 0.142392 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14098) vms_mb | MB | 2 | 1577.902 | 1499.969 | 1655.836 | 1655.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 14105) rss_mb | MB | 1 | 50.043 | 50.043 | 50.043 | 50.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 14105) vms_mb | MB | 1 | 858.992 | 858.992 | 858.992 | 858.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14119) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14119) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14120) rss_mb | MB | 1 | 7.070 | 7.070 | 7.070 | 7.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14120) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14124) CPU | percent | 6 | 41.197 | 7.932 | 73.373 | 9.932 | 2.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14124) rss_mb | MB | 7 | 339.699 | 188.402 | 388.109 | 388.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14124) main thread run-queue wait | percent | 6 | 2.984 | 0.035 | 9.387 | 0.035 | 0.180747 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14124) vms_mb | MB | 7 | 7748.600 | 1594.219 | 10193.984 | 10193.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14145) CPU | percent | 1 | 57.383 | 57.383 | 57.383 | 57.383 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14145) rss_mb | MB | 2 | 171.600 | 107.012 | 236.188 | 236.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14145) main thread run-queue wait | percent | 1 | 16.112 | 16.112 | 16.112 | 16.112 | 0.162854 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14145) vms_mb | MB | 2 | 1459.795 | 1283.695 | 1635.895 | 1635.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14151) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14151) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14153) rss_mb | MB | 1 | 10.082 | 10.082 | 10.082 | 10.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14153) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14171) CPU | percent | 16 | 18.336 | 0.993 | 77.059 | 0.993 | 2.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14171) rss_mb | MB | 17 | 369.301 | 207.078 | 390.355 | 389.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14171) main thread run-queue wait | percent | 16 | 3.212 | 0.002 | 22.839 | 0.011 | 0.518193 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14171) vms_mb | MB | 17 | 9201.516 | 1619.535 | 10211.309 | 10210.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 14184) rss_mb | MB | 1 | 2.672 | 2.672 | 2.672 | 2.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 14184) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14190) CPU | percent | 1 | 53.549 | 53.549 | 53.549 | 53.549 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14190) rss_mb | MB | 2 | 248.709 | 207.746 | 289.672 | 289.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14190) main thread run-queue wait | percent | 1 | 15.689 | 15.689 | 15.689 | 15.689 | 0.158209 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14190) vms_mb | MB | 2 | 1651.863 | 1619.445 | 1684.281 | 1684.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14213) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14213) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 14214) rss_mb | MB | 1 | 20.605 | 20.605 | 20.605 | 20.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 14214) vms_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14220) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14220) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 14221) rss_mb | MB | 1 | 21.258 | 21.258 | 21.258 | 21.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 14221) vms_mb | MB | 1 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| sleep (PID 14226) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14226) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14226) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14226) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14226) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14226) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14232) CPU | percent | 40 | 8.858 | 0.994 | 76.539 | 8.950 | 3.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14232) rss_mb | MB | 41 | 388.692 | 229.344 | 401.664 | 401.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14232) main thread run-queue wait | percent | 40 | 0.795 | 0.002 | 9.682 | 0.019 | 0.324648 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14232) vms_mb | MB | 41 | 9794.099 | 1636.031 | 10215.363 | 10215.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14256) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14256) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14257) rss_mb | MB | 1 | 9.676 | 9.676 | 9.676 | 9.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14257) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14258) CPU | percent | 1 | 72.676 | 72.676 | 72.676 | 72.676 | 0.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14258) rss_mb | MB | 2 | 166.107 | 70.000 | 262.215 | 262.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14258) main thread run-queue wait | percent | 1 | 13.073 | 13.073 | 13.073 | 13.073 | 0.138510 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14258) vms_mb | MB | 2 | 1470.492 | 1283.695 | 1657.289 | 1657.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 14278) rss_mb | MB | 1 | 2.652 | 2.652 | 2.652 | 2.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 14278) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 14279) rss_mb | MB | 1 | 17.348 | 17.348 | 17.348 | 17.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 14279) vms_mb | MB | 1 | 209.723 | 209.723 | 209.723 | 209.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14288) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14288) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 14289) rss_mb | MB | 1 | 8.746 | 8.746 | 8.746 | 8.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 14289) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14315) CPU | percent | 20 | 16.436 | 0.994 | 72.324 | 1.988 | 3.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14315) rss_mb | MB | 21 | 374.736 | 197.332 | 394.215 | 394.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14315) main thread run-queue wait | percent | 20 | 1.634 | 0.003 | 15.398 | 0.005 | 0.329437 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14315) vms_mb | MB | 21 | 9394.541 | 1616.812 | 10212.734 | 10212.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14337) rss_mb | MB | 1 | 206.051 | 206.051 | 206.051 | 206.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14337) vms_mb | MB | 1 | 1618.980 | 1618.980 | 1618.980 | 1618.980 | n/a | n/a |
| sleep (PID 14374) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14374) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14374) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14374) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14374) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14374) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14380) CPU | percent | 10 | 33.658 | 2.983 | 87.315 | 4.970 | 3.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14380) rss_mb | MB | 11 | 351.942 | 156.172 | 393.379 | 393.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14380) main thread run-queue wait | percent | 10 | 3.729 | 0.002 | 16.472 | 0.002 | 0.375778 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14380) vms_mb | MB | 11 | 8621.034 | 1312.488 | 10211.441 | 10211.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 14400) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 14400) vms_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14409) CPU | percent | 1 | 68.467 | 68.467 | 68.467 | 68.467 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14409) rss_mb | MB | 2 | 215.801 | 166.688 | 264.914 | 264.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14409) main thread run-queue wait | percent | 1 | 16.560 | 16.560 | 16.560 | 16.560 | 0.166890 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14409) vms_mb | MB | 2 | 1619.029 | 1577.723 | 1660.336 | 1660.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — finalize_adapter.py (PID 14423) rss_mb | MB | 1 | 8.859 | 8.859 | 8.859 | 8.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — finalize_adapter.py (PID 14423) vms_mb | MB | 1 | 13.391 | 13.391 | 13.391 | 13.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14439) CPU | percent | 8 | 37.352 | 3.978 | 81.313 | 6.960 | 3.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14439) rss_mb | MB | 9 | 341.250 | 168.484 | 387.453 | 387.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14439) main thread run-queue wait | percent | 8 | 6.034 | 0.006 | 15.252 | 0.006 | 0.486375 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14439) vms_mb | MB | 9 | 8294.886 | 1578.469 | 10210.863 | 10210.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14456) CPU | percent | 1 | 59.491 | 59.491 | 59.491 | 59.491 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14456) rss_mb | MB | 2 | 256.596 | 217.547 | 295.645 | 295.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14456) main thread run-queue wait | percent | 1 | 14.319 | 14.319 | 14.319 | 14.319 | 0.144414 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14456) vms_mb | MB | 2 | 1656.770 | 1623.727 | 1689.812 | 1689.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14505) CPU | percent | 6 | 39.725 | 3.978 | 81.377 | 3.978 | 2.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14505) rss_mb | MB | 7 | 353.360 | 261.992 | 385.445 | 385.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14505) main thread run-queue wait | percent | 6 | 5.764 | 0.006 | 22.230 | 0.006 | 0.352042 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14505) vms_mb | MB | 7 | 8957.112 | 1657.254 | 10208.965 | 10208.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14522) CPU | percent | 2 | 55.166 | 48.880 | 61.451 | 48.880 | 1.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14522) rss_mb | MB | 3 | 193.931 | 47.297 | 299.367 | 299.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14522) main thread run-queue wait | percent | 2 | 18.488 | 12.161 | 24.815 | 24.815 | 0.376530 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14522) vms_mb | MB | 3 | 1533.518 | 1238.609 | 1725.594 | 1725.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14528) rss_mb | MB | 1 | 1.285 | 1.285 | 1.285 | 1.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14528) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14529) rss_mb | MB | 1 | 6.707 | 6.707 | 6.707 | 6.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14529) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14534) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14534) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14535) rss_mb | MB | 1 | 7.738 | 7.738 | 7.738 | 7.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14535) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14550) CPU | percent | 7 | 42.115 | 3.977 | 78.507 | 5.967 | 2.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14550) rss_mb | MB | 8 | 342.176 | 183.051 | 381.586 | 381.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14550) main thread run-queue wait | percent | 7 | 5.584 | 0.004 | 13.463 | 0.013 | 0.394096 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14550) vms_mb | MB | 8 | 8058.524 | 1593.219 | 10207.211 | 10207.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14569) CPU | percent | 1 | 61.497 | 61.497 | 61.497 | 61.497 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14569) rss_mb | MB | 2 | 236.570 | 190.238 | 282.902 | 282.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14569) main thread run-queue wait | percent | 1 | 16.509 | 16.509 | 16.509 | 16.509 | 0.166440 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14569) vms_mb | MB | 2 | 1636.516 | 1595.223 | 1677.809 | 1677.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14590) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14590) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14591) rss_mb | MB | 1 | 5.547 | 5.547 | 5.547 | 5.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14591) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14595) CPU | percent | 32 | 11.985 | 0.993 | 76.516 | 0.994 | 3.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14595) rss_mb | MB | 33 | 385.300 | 189.270 | 398.754 | 398.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14595) main thread run-queue wait | percent | 32 | 2.237 | 0.002 | 15.300 | 0.003 | 0.721313 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14595) vms_mb | MB | 33 | 9690.172 | 1594.219 | 10213.656 | 10213.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14612) CPU | percent | 2 | 59.047 | 52.522 | 65.572 | 65.572 | 1.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14612) rss_mb | MB | 3 | 173.712 | 2.500 | 302.441 | 302.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14612) main thread run-queue wait | percent | 2 | 15.308 | 12.918 | 17.697 | 12.918 | 0.308604 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14612) vms_mb | MB | 3 | 1171.676 | 165.203 | 1726.840 | 1726.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14644) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14644) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 14645) rss_mb | MB | 1 | 7.305 | 7.305 | 7.305 | 7.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 14645) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — finalize_adapter.py (PID 14646) rss_mb | MB | 1 | 138.922 | 138.922 | 138.922 | 138.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — finalize_adapter.py (PID 14646) vms_mb | MB | 1 | 354.938 | 354.938 | 354.938 | 354.938 | n/a | n/a |
| sleep (PID 14656) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14656) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14656) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14656) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14656) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14656) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14667) CPU | percent | 7 | 40.366 | 3.977 | 90.323 | 3.977 | 2.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14667) rss_mb | MB | 8 | 325.788 | 47.250 | 395.516 | 395.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14667) main thread run-queue wait | percent | 7 | 3.307 | 0.015 | 9.743 | 0.166 | 0.237012 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14667) vms_mb | MB | 8 | 7998.241 | 1238.512 | 10201.191 | 10201.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14691) rss_mb | MB | 1 | 194.281 | 194.281 | 194.281 | 194.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14691) vms_mb | MB | 1 | 1614.723 | 1614.723 | 1614.723 | 1614.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14701) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14701) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14702) rss_mb | MB | 1 | 9.145 | 9.145 | 9.145 | 9.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14702) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14717) CPU | percent | 8 | 39.982 | 4.963 | 87.421 | 4.971 | 3.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14717) rss_mb | MB | 9 | 337.987 | 141.234 | 387.148 | 387.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14717) main thread run-queue wait | percent | 8 | 2.201 | 0.094 | 8.340 | 0.094 | 0.177215 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14717) vms_mb | MB | 9 | 8256.418 | 1297.703 | 10211.293 | 10211.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14745) rss_mb | MB | 1 | 234.703 | 234.703 | 234.703 | 234.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14745) vms_mb | MB | 1 | 1635.840 | 1635.840 | 1635.840 | 1635.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14762) CPU | percent | 7 | 31.770 | 3.921 | 82.429 | 8.951 | 2.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14762) rss_mb | MB | 8 | 360.618 | 270.863 | 396.070 | 396.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14762) main thread run-queue wait | percent | 7 | 0.765 | 0.018 | 3.320 | 0.042 | 0.054020 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14762) vms_mb | MB | 8 | 9114.561 | 1666.242 | 10203.094 | 10203.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 14779) rss_mb | MB | 1 | 44.301 | 44.301 | 44.301 | 44.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 14779) vms_mb | MB | 1 | 836.441 | 836.441 | 836.441 | 836.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14791) rss_mb | MB | 1 | 229.520 | 229.520 | 229.520 | 229.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14791) vms_mb | MB | 1 | 1632.156 | 1632.156 | 1632.156 | 1632.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14808) CPU | percent | 6 | 43.768 | 7.956 | 86.262 | 7.956 | 2.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14808) rss_mb | MB | 7 | 336.771 | 167.047 | 394.391 | 394.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14808) main thread run-queue wait | percent | 6 | 4.492 | 0.013 | 17.083 | 0.013 | 0.273078 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14808) vms_mb | MB | 7 | 7737.361 | 1578.219 | 10200.926 | 10200.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14827) CPU | percent | 1 | 56.117 | 56.117 | 56.117 | 56.117 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14827) rss_mb | MB | 2 | 218.662 | 175.371 | 261.953 | 261.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14827) main thread run-queue wait | percent | 1 | 18.715 | 18.715 | 18.715 | 18.715 | 0.190092 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14827) vms_mb | MB | 2 | 1623.654 | 1589.973 | 1657.336 | 1657.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14840) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 14840) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14841) rss_mb | MB | 1 | 9.371 | 9.371 | 9.371 | 9.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 14841) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14856) CPU | percent | 7 | 36.175 | 2.983 | 78.522 | 14.919 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14856) rss_mb | MB | 8 | 358.012 | 256.070 | 397.340 | 397.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14856) main thread run-queue wait | percent | 7 | 5.902 | 0.004 | 28.378 | 0.285 | 0.416444 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14856) vms_mb | MB | 8 | 8071.054 | 1651.535 | 10208.535 | 10208.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14951) CPU | percent | 1 | 57.523 | 57.523 | 57.523 | 57.523 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14951) rss_mb | MB | 2 | 249.346 | 208.363 | 290.328 | 290.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14951) main thread run-queue wait | percent | 1 | 30.019 | 30.019 | 30.019 | 30.019 | 0.302678 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14951) vms_mb | MB | 2 | 1652.016 | 1619.473 | 1684.559 | 1684.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 14976) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 14976) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14979) CPU | percent | 7 | 37.003 | 2.978 | 74.429 | 6.963 | 2.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14979) rss_mb | MB | 8 | 347.245 | 205.062 | 388.047 | 388.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14979) main thread run-queue wait | percent | 7 | 4.835 | 0.007 | 18.888 | 0.007 | 0.341103 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14979) vms_mb | MB | 8 | 8063.510 | 1619.059 | 10207.996 | 10207.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14998) CPU | percent | 1 | 60.516 | 60.516 | 60.516 | 60.516 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14998) rss_mb | MB | 2 | 241.699 | 194.195 | 289.203 | 289.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14998) main thread run-queue wait | percent | 1 | 17.968 | 17.968 | 17.968 | 17.968 | 0.181118 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 14998) vms_mb | MB | 2 | 1649.277 | 1614.973 | 1683.582 | 1683.582 | n/a | n/a |
| sleep (PID 15007) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 15007) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 15007) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 15007) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 15007) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 15007) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15010) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15010) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15011) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15011) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15026) CPU | percent | 5 | 40.697 | 2.983 | 80.376 | 2.983 | 2.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15026) rss_mb | MB | 6 | 357.990 | 296.035 | 386.879 | 386.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15026) main thread run-queue wait | percent | 5 | 4.659 | 0.010 | 15.938 | 0.010 | 0.234639 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15026) vms_mb | MB | 6 | 8762.434 | 1691.176 | 10207.488 | 10207.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15047) rss_mb | MB | 1 | 205.898 | 205.898 | 205.898 | 205.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15047) vms_mb | MB | 1 | 1619.465 | 1619.465 | 1619.465 | 1619.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15073) CPU | percent | 6 | 52.486 | 3.973 | 87.288 | 3.973 | 3.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15073) rss_mb | MB | 7 | 303.915 | 8.957 | 378.387 | 378.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15073) main thread run-queue wait | percent | 6 | 4.911 | 0.312 | 11.655 | 0.364 | 0.298112 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15073) vms_mb | MB | 7 | 7535.857 | 165.590 | 10209.441 | 10209.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15102) rss_mb | MB | 1 | 254.723 | 254.723 | 254.723 | 254.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15102) vms_mb | MB | 1 | 1650.598 | 1650.598 | 1650.598 | 1650.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15119) CPU | percent | 9 | 26.911 | 2.983 | 80.361 | 4.972 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15119) rss_mb | MB | 10 | 363.056 | 237.082 | 391.355 | 391.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15119) main thread run-queue wait | percent | 9 | 0.936 | 0.007 | 2.976 | 0.017 | 0.084804 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15119) vms_mb | MB | 10 | 8502.594 | 1637.805 | 10211.195 | 10211.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15147) CPU | percent | 1 | 87.438 | 87.438 | 87.438 | 87.438 | 0.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15147) rss_mb | MB | 2 | 200.301 | 100.691 | 299.910 | 299.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15147) main thread run-queue wait | percent | 1 | 8.877 | 8.877 | 8.877 | 8.877 | 0.089336 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15147) vms_mb | MB | 2 | 1504.094 | 1283.695 | 1724.492 | 1724.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15166) CPU | percent | 7 | 42.942 | 6.960 | 88.304 | 8.916 | 3.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15166) rss_mb | MB | 8 | 330.089 | 106.648 | 389.859 | 389.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15166) main thread run-queue wait | percent | 7 | 4.977 | 0.024 | 14.184 | 0.024 | 0.354789 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15166) vms_mb | MB | 8 | 8007.875 | 1283.598 | 10209.766 | 10209.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15185) CPU | percent | 1 | 57.443 | 57.443 | 57.443 | 57.443 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15185) rss_mb | MB | 2 | 207.012 | 158.281 | 255.742 | 255.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15185) main thread run-queue wait | percent | 1 | 14.707 | 14.707 | 14.707 | 14.707 | 0.148497 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15185) vms_mb | MB | 2 | 1575.646 | 1499.969 | 1651.324 | 1651.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15197) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15197) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15198) rss_mb | MB | 1 | 8.312 | 8.312 | 8.312 | 8.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15198) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 15206) rss_mb | MB | 1 | 2.176 | 2.176 | 2.176 | 2.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 15206) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 15207) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 15207) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15213) CPU | percent | 7 | 37.137 | 3.978 | 76.420 | 12.930 | 2.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15213) rss_mb | MB | 8 | 349.809 | 217.445 | 390.562 | 390.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15213) main thread run-queue wait | percent | 7 | 6.008 | 0.012 | 26.897 | 0.056 | 0.424042 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15213) vms_mb | MB | 8 | 8066.191 | 1623.789 | 10207.652 | 10207.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15232) CPU | percent | 1 | 55.529 | 55.529 | 55.529 | 55.529 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15232) rss_mb | MB | 2 | 250.352 | 211.305 | 289.398 | 289.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15232) main thread run-queue wait | percent | 1 | 25.189 | 25.189 | 25.189 | 25.189 | 0.254026 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15232) vms_mb | MB | 2 | 1653.398 | 1622.230 | 1684.566 | 1684.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15258) CPU | percent | 6 | 38.953 | 2.978 | 79.373 | 3.979 | 2.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15258) rss_mb | MB | 7 | 343.585 | 229.285 | 377.512 | 377.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15258) main thread run-queue wait | percent | 6 | 3.526 | 0.007 | 15.791 | 0.007 | 0.214284 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15258) vms_mb | MB | 7 | 7767.385 | 1632.070 | 10205.574 | 10205.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15287) rss_mb | MB | 1 | 228.918 | 228.918 | 228.918 | 228.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15287) vms_mb | MB | 1 | 1631.094 | 1631.094 | 1631.094 | 1631.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15306) CPU | percent | 11 | 20.479 | 1.985 | 75.499 | 8.952 | 2.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15306) rss_mb | MB | 12 | 374.648 | 296.305 | 394.863 | 394.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15306) main thread run-queue wait | percent | 11 | 2.407 | 0.005 | 13.353 | 0.010 | 0.267080 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15306) vms_mb | MB | 12 | 9481.537 | 1690.922 | 10207.426 | 10207.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15325) CPU | percent | 1 | 51.365 | 51.365 | 51.365 | 51.365 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15325) rss_mb | MB | 2 | 199.689 | 160.836 | 238.543 | 238.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15325) main thread run-queue wait | percent | 1 | 12.310 | 12.310 | 12.310 | 12.310 | 0.124621 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15325) vms_mb | MB | 2 | 1477.900 | 1317.723 | 1638.078 | 1638.078 | n/a | n/a |
| sleep (PID 15347) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 15347) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 15347) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 15347) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 15347) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 15347) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15355) CPU | percent | 18 | 16.823 | 1.988 | 79.557 | 1.989 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15355) rss_mb | MB | 19 | 377.694 | 228.641 | 396.535 | 396.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15355) main thread run-queue wait | percent | 18 | 1.701 | 0.004 | 13.062 | 0.009 | 0.309312 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15355) vms_mb | MB | 19 | 9307.831 | 1631.770 | 10207.922 | 10207.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15377) rss_mb | MB | 1 | 1.277 | 1.277 | 1.277 | 1.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15377) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15378) rss_mb | MB | 1 | 10.566 | 10.566 | 10.566 | 10.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15378) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15386) CPU | percent | 1 | 90.442 | 90.442 | 90.442 | 90.442 | 0.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15386) rss_mb | MB | 2 | 167.492 | 40.512 | 294.473 | 294.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15386) main thread run-queue wait | percent | 1 | 4.230 | 4.230 | 4.230 | 4.230 | 0.042561 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15386) vms_mb | MB | 2 | 1430.504 | 1172.199 | 1688.809 | 1688.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15400) rss_mb | MB | 1 | 2.652 | 2.652 | 2.652 | 2.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15400) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15401) rss_mb | MB | 1 | 13.641 | 13.641 | 13.641 | 13.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15401) vms_mb | MB | 1 | 207.289 | 207.289 | 207.289 | 207.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15424) CPU | percent | 6 | 49.489 | 6.961 | 87.451 | 6.961 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15424) rss_mb | MB | 7 | 314.065 | 57.039 | 386.992 | 386.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15424) main thread run-queue wait | percent | 6 | 5.062 | 0.219 | 17.392 | 0.293 | 0.305738 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15424) vms_mb | MB | 7 | 7684.477 | 1238.512 | 10202.918 | 10202.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15449) CPU | percent | 1 | 66.540 | 66.540 | 66.540 | 66.540 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15449) rss_mb | MB | 2 | 216.705 | 155.809 | 277.602 | 277.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15449) main thread run-queue wait | percent | 1 | 23.603 | 23.603 | 23.603 | 23.603 | 0.237659 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15449) vms_mb | MB | 2 | 1586.123 | 1499.469 | 1672.777 | 1672.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15471) CPU | percent | 17 | 18.914 | 1.978 | 73.585 | 8.945 | 3.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15471) rss_mb | MB | 18 | 373.889 | 235.891 | 394.164 | 393.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15471) main thread run-queue wait | percent | 17 | 3.865 | 0.004 | 24.671 | 0.015 | 0.662961 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15471) vms_mb | MB | 18 | 9256.586 | 1636.793 | 10210.125 | 10209.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15490) CPU | percent | 1 | 53.533 | 53.533 | 53.533 | 53.533 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15490) rss_mb | MB | 2 | 225.918 | 188.766 | 263.070 | 263.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15490) main thread run-queue wait | percent | 1 | 17.049 | 17.049 | 17.049 | 17.049 | 0.171974 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15490) vms_mb | MB | 2 | 1626.262 | 1594.223 | 1658.301 | 1658.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15500) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15500) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15501) rss_mb | MB | 1 | 8.859 | 8.859 | 8.859 | 8.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15501) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15513) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15513) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15514) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15514) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15522) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15522) rss_mb | MB | 2 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15522) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15522) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — finalize_adapter.py (PID 15523) rss_mb | MB | 1 | 137.879 | 137.879 | 137.879 | 137.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — finalize_adapter.py (PID 15523) vms_mb | MB | 1 | 354.074 | 354.074 | 354.074 | 354.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15527) rss_mb | MB | 1 | 9.316 | 9.316 | 9.316 | 9.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15527) vms_mb | MB | 1 | 13.301 | 13.301 | 13.301 | 13.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15542) CPU | percent | 18 | 19.676 | 1.985 | 71.517 | 1.987 | 3.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15542) rss_mb | MB | 19 | 375.157 | 207.734 | 396.211 | 396.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15542) main thread run-queue wait | percent | 18 | 2.709 | 0.006 | 17.881 | 0.011 | 0.492939 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15542) vms_mb | MB | 19 | 9303.318 | 1619.781 | 10209.285 | 10209.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15562) CPU | percent | 1 | 61.022 | 61.022 | 61.022 | 61.022 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15562) rss_mb | MB | 2 | 222.209 | 174.734 | 269.684 | 269.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15562) main thread run-queue wait | percent | 1 | 14.820 | 14.820 | 14.820 | 14.820 | 0.150574 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15562) vms_mb | MB | 2 | 1627.643 | 1589.973 | 1665.312 | 1665.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 15571) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 15571) vms_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sleep (PID 15586) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 15586) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 15586) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 15586) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 15586) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 15586) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15587) rss_mb | MB | 1 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15587) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15588) rss_mb | MB | 1 | 9.164 | 9.164 | 9.164 | 9.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15588) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15596) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15596) rss_mb | MB | 2 | 2.672 | 2.672 | 2.672 | 2.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15596) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15596) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15597) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15597) rss_mb | MB | 2 | 10.537 | 10.387 | 10.688 | 10.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15597) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15597) vms_mb | MB | 2 | 14.736 | 14.621 | 14.852 | 14.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 15598) rss_mb | MB | 1 | 54.059 | 54.059 | 54.059 | 54.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 15598) vms_mb | MB | 1 | 72.289 | 72.289 | 72.289 | 72.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15599) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15599) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15600) rss_mb | MB | 1 | 21.430 | 21.430 | 21.430 | 21.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15600) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15609) CPU | percent | 7 | 46.398 | 4.961 | 92.399 | 13.911 | 3.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15609) rss_mb | MB | 8 | 324.311 | 72.910 | 386.930 | 386.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15609) main thread run-queue wait | percent | 7 | 6.148 | 0.023 | 22.488 | 0.023 | 0.433116 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15609) vms_mb | MB | 8 | 8004.877 | 1283.598 | 10209.492 | 10209.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15628) CPU | percent | 2 | 52.171 | 48.692 | 55.651 | 48.692 | 1.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15628) rss_mb | MB | 3 | 204.724 | 88.539 | 296.137 | 296.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15628) main thread run-queue wait | percent | 2 | 18.474 | 16.437 | 20.511 | 20.511 | 0.371812 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15628) vms_mb | MB | 3 | 1535.548 | 1283.695 | 1690.973 | 1690.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15654) CPU | percent | 6 | 44.823 | 3.976 | 68.534 | 4.973 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15654) rss_mb | MB | 7 | 341.866 | 202.152 | 387.383 | 387.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15654) main thread run-queue wait | percent | 6 | 1.583 | 0.007 | 3.720 | 0.007 | 0.095729 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15654) vms_mb | MB | 7 | 7760.028 | 1618.266 | 10207.703 | 10207.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15676) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15676) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15677) rss_mb | MB | 1 | 9.105 | 9.105 | 9.105 | 9.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15677) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15688) CPU | percent | 7 | 47.081 | 3.977 | 85.295 | 13.873 | 3.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15688) rss_mb | MB | 8 | 339.238 | 161.480 | 387.305 | 387.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15688) main thread run-queue wait | percent | 7 | 4.148 | 0.198 | 12.236 | 2.833 | 0.292385 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15688) vms_mb | MB | 8 | 8044.765 | 1500.465 | 10214.250 | 10214.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15716) rss_mb | MB | 1 | 199.977 | 199.977 | 199.977 | 199.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15716) vms_mb | MB | 1 | 1618.234 | 1618.234 | 1618.234 | 1618.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15733) CPU | percent | 8 | 33.336 | 3.966 | 75.051 | 5.966 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15733) rss_mb | MB | 9 | 356.363 | 216.910 | 395.566 | 395.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15733) main thread run-queue wait | percent | 8 | 1.307 | 0.013 | 3.922 | 0.023 | 0.105320 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15733) vms_mb | MB | 9 | 8310.426 | 1623.512 | 10210.859 | 10210.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 15746) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 15746) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 15747) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 15747) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15765) rss_mb | MB | 1 | 170.277 | 170.277 | 170.277 | 170.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15765) vms_mb | MB | 1 | 1579.723 | 1579.723 | 1579.723 | 1579.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15782) CPU | percent | 19 | 16.337 | 1.843 | 73.476 | 4.972 | 3.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15782) rss_mb | MB | 20 | 378.604 | 229.629 | 398.211 | 397.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15782) main thread run-queue wait | percent | 19 | 2.137 | 0.006 | 26.915 | 0.008 | 0.409558 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15782) vms_mb | MB | 20 | 9353.427 | 1632.262 | 10211.383 | 10210.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15801) CPU | percent | 1 | 53.585 | 53.585 | 53.585 | 53.585 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15801) rss_mb | MB | 2 | 245.439 | 205.160 | 285.719 | 285.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15801) main thread run-queue wait | percent | 1 | 28.380 | 28.380 | 28.380 | 28.380 | 0.285993 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15801) vms_mb | MB | 2 | 1650.023 | 1618.980 | 1681.066 | 1681.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15826) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15826) rss_mb | MB | 2 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15826) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15826) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15827) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15827) rss_mb | MB | 2 | 10.809 | 10.809 | 10.809 | 10.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15827) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15827) vms_mb | MB | 2 | 14.871 | 14.871 | 14.871 | 14.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 15828) CPU | percent | 1 | 56.444 | 56.444 | 56.444 | 56.444 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 15828) rss_mb | MB | 2 | 51.342 | 36.352 | 66.332 | 66.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 15828) main thread run-queue wait | percent | 1 | 0.627 | 0.627 | 0.627 | 0.627 | 0.006336 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 15828) vms_mb | MB | 2 | 62.842 | 44.285 | 81.398 | 81.398 | n/a | n/a |
| sleep (PID 15836) CPU | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 15836) io read MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 15836) io write MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 15836) rss_mb | MB | 48 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 15836) main thread run-queue wait | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 15836) vms_mb | MB | 48 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15839) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15839) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15840) rss_mb | MB | 1 | 20.695 | 20.695 | 20.695 | 20.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15840) vms_mb | MB | 1 | 25.578 | 25.578 | 25.578 | 25.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15844) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15844) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15845) rss_mb | MB | 1 | 7.160 | 7.160 | 7.160 | 7.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 15845) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| docker commit (PID 15875) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 15875) io read MB/s | MB/s | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 15875) io write MB/s | MB/s | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 15875) rss_mb | MB | 17 | 30.527 | 30.527 | 30.527 | 30.527 | n/a | n/a |
| docker commit (PID 15875) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 15875) vms_mb | MB | 17 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| docker stop (PID 15945) rss_mb | MB | 1 | 29.832 | 29.832 | 29.832 | 29.832 | n/a | n/a |
| docker stop (PID 15945) vms_mb | MB | 1 | 1771.195 | 1771.195 | 1771.195 | 1771.195 | n/a | n/a |
| bash kimi_seq.sh (PID 1928) CPU | percent | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash kimi_seq.sh (PID 1928) io read MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash kimi_seq.sh (PID 1928) io write MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash kimi_seq.sh (PID 1928) rss_mb | MB | 2917 | 3.293 | 3.293 | 3.293 | 3.293 | n/a | n/a |
| bash kimi_seq.sh (PID 1928) main thread run-queue wait | percent | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash kimi_seq.sh (PID 1928) vms_mb | MB | 2917 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| bash lsb_guard.sh (PID 3862) CPU | percent | 2916 | 0.001 | 0.000 | 0.994 | 0.000 | 0.030000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 3862) io read MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3862) io write MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3862) rss_mb | MB | 2917 | 3.367 | 3.367 | 3.367 | 3.367 | n/a | n/a |
| bash lsb_guard.sh (PID 3862) main thread run-queue wait | percent | 2916 | 0.000 | 0.000 | 0.143 | 0.000 | 0.003318 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 3862) vms_mb | MB | 2917 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3890) CPU | percent | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 3890) io read MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3890) io write MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3890) rss_mb | MB | 2917 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3890) main thread run-queue wait | percent | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 3890) vms_mb | MB | 2917 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3899) CPU | percent | 2916 | 5.253 | 0.000 | 101.994 | 0.995 | 154.800000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 3899) io read MB/s | MB/s | 2916 | 0.002 | 0.000 | 1.710 | 0.000 | 4.691406 MB | n/a |
| Agency harness — python -m lsbench (PID 3899) io write MB/s | MB/s | 2916 | 0.433 | 0.000 | 9.868 | 0.027 | 1273.855469 MB | n/a |
| Agency harness — python -m lsbench (PID 3899) rss_mb | MB | 2917 | 3164.241 | 2278.633 | 3561.727 | 3561.727 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3899) main thread run-queue wait | percent | 2916 | 0.000 | 0.000 | 0.477 | 0.000 | 0.011835 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 3899) vms_mb | MB | 2917 | 16106.040 | 13733.000 | 16504.930 | 16464.758 | n/a | n/a |
| Python — vllm (PID 3904) CPU | percent | 2916 | 0.139 | 0.000 | 7.932 | 0.000 | 4.100000 CPU seconds | n/a |
| Python — vllm (PID 3904) io read MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 3904) io write MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.008 | 0.000 | 0.050781 MB | n/a |
| Python — vllm (PID 3904) rss_mb | MB | 2917 | 1783.331 | 1782.297 | 1783.422 | 1783.422 | n/a | n/a |
| Python — vllm (PID 3904) main thread run-queue wait | percent | 2916 | 0.012 | 0.000 | 0.901 | 0.000 | 0.355921 run-queue seconds | n/a |
| Python — vllm (PID 3904) vms_mb | MB | 2917 | 11021.164 | 10951.023 | 11024.043 | 11024.043 | n/a | n/a |
| sleep (PID 3910) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3910) io read MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3910) io write MB/s | MB/s | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3910) rss_mb | MB | 11 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3910) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3910) vms_mb | MB | 11 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — python -c (PID 3941) CPU | percent | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 3941) io read MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3941) io write MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3941) rss_mb | MB | 2917 | 12.188 | 12.188 | 12.188 | 12.188 | n/a | n/a |
| Python — python -c (PID 3941) main thread run-queue wait | percent | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 3941) vms_mb | MB | 2917 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 3942) CPU | percent | 2916 | 1.047 | 0.000 | 30.735 | 0.995 | 30.800000 CPU seconds | n/a |
| VLLM::EngineCore (PID 3942) io read MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 3942) io write MB/s | MB/s | 2916 | 0.000 | 0.000 | 0.004 | 0.000 | 0.015625 MB | n/a |
| VLLM::EngineCore (PID 3942) rss_mb | MB | 2917 | 2322.076 | 2321.957 | 2322.082 | 2322.082 | n/a | n/a |
| VLLM::EngineCore (PID 3942) main thread run-queue wait | percent | 2916 | 0.001 | 0.000 | 0.364 | 0.000 | 0.020731 run-queue seconds | n/a |
| VLLM::EngineCore (PID 3942) vms_mb | MB | 2917 | 21203.227 | 21203.227 | 21203.227 | 21203.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 4160) CPU | percent | 2889 | 0.001 | 0.000 | 0.994 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 4160) rss_mb | MB | 2890 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 4160) main thread run-queue wait | percent | 2889 | 0.014 | 0.000 | 5.150 | 0.000 | 0.410190 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 4160) vms_mb | MB | 2890 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 4191) CPU | percent | 2889 | 0.002 | 0.000 | 0.994 | 0.000 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 4191) rss_mb | MB | 2890 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 4191) main thread run-queue wait | percent | 2889 | 0.010 | 0.000 | 4.730 | 0.000 | 0.282100 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 4191) vms_mb | MB | 2890 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4283) CPU | percent | 2889 | 51.847 | 0.000 | 106.794 | 0.000 | 1510.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4283) rss_mb | MB | 2890 | 132.106 | 3.094 | 155.695 | 155.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4283) main thread run-queue wait | percent | 2889 | 0.000 | 0.000 | 0.030 | 0.000 | 0.000378 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4283) vms_mb | MB | 2890 | 901.989 | 4.258 | 917.621 | 904.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 4289) CPU | percent | 1 | 99.777 | 99.777 | 99.777 | 99.777 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 4289) rss_mb | MB | 2 | 45.574 | 21.137 | 70.012 | 70.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 4289) main thread run-queue wait | percent | 1 | 0.017 | 0.017 | 0.017 | 0.017 | 0.000175 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 4289) vms_mb | MB | 2 | 55.238 | 32.020 | 78.457 | 78.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 4297) rss_mb | MB | 1 | 162.652 | 162.652 | 162.652 | 162.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 4297) vms_mb | MB | 1 | 1572.348 | 1572.348 | 1572.348 | 1572.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 4314) CPU | percent | 190 | 5.260 | 0.981 | 72.383 | 5.956 | 10.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 4314) rss_mb | MB | 191 | 380.937 | 175.301 | 396.344 | 392.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 4314) main thread run-queue wait | percent | 190 | 0.239 | 0.001 | 10.536 | 0.006 | 0.458446 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 4314) vms_mb | MB | 191 | 10101.021 | 1589.723 | 10214.203 | 10183.723 | n/a | n/a |
| sleep (PID 4351) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4351) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4351) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4351) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4351) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4351) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4363) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4363) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4364) rss_mb | MB | 1 | 15.824 | 15.824 | 15.824 | 15.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4364) vms_mb | MB | 1 | 20.844 | 20.844 | 20.844 | 20.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4483) rss_mb | MB | 1 | 2.738 | 2.738 | 2.738 | 2.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4483) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4485) rss_mb | MB | 1 | 49.789 | 49.789 | 49.789 | 49.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4485) vms_mb | MB | 1 | 56.828 | 56.828 | 56.828 | 56.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4498) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4498) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4499) rss_mb | MB | 1 | 13.992 | 13.992 | 13.992 | 13.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4499) vms_mb | MB | 1 | 19.902 | 19.902 | 19.902 | 19.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4503) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4503) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4504) rss_mb | MB | 1 | 21.406 | 21.406 | 21.406 | 21.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4504) vms_mb | MB | 1 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4523) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4523) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp (PID 4527) rss_mb | MB | 1 | 43.809 | 43.809 | 43.809 | 43.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp (PID 4527) vms_mb | MB | 1 | 50.984 | 50.984 | 50.984 | 50.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4535) rss_mb | MB | 1 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4535) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4539) rss_mb | MB | 1 | 8.043 | 8.043 | 8.043 | 8.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4539) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sleep (PID 4547) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4547) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4547) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4547) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4547) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4547) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4557) rss_mb | MB | 1 | 26.117 | 26.117 | 26.117 | 26.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4557) vms_mb | MB | 1 | 35.055 | 35.055 | 35.055 | 35.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4558) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4558) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4559) rss_mb | MB | 1 | 6.934 | 6.934 | 6.934 | 6.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4559) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4573) rss_mb | MB | 1 | 34.637 | 34.637 | 34.637 | 34.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4573) vms_mb | MB | 1 | 41.988 | 41.988 | 41.988 | 41.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4574) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4574) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4575) rss_mb | MB | 1 | 21.363 | 21.363 | 21.363 | 21.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4575) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4588) CPU | percent | 1 | 75.482 | 75.482 | 75.482 | 75.482 | 0.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4588) rss_mb | MB | 2 | 35.363 | 9.484 | 61.242 | 61.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4588) main thread run-queue wait | percent | 1 | 0.066 | 0.066 | 0.066 | 0.066 | 0.000669 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4588) vms_mb | MB | 2 | 44.732 | 13.512 | 75.953 | 75.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4595) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4595) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4596) rss_mb | MB | 1 | 21.160 | 21.160 | 21.160 | 21.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4596) vms_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4597) rss_mb | MB | 1 | 2.863 | 2.863 | 2.863 | 2.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4597) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4598) rss_mb | MB | 1 | 61.238 | 61.238 | 61.238 | 61.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4598) vms_mb | MB | 1 | 75.910 | 75.910 | 75.910 | 75.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4613) rss_mb | MB | 1 | 37.137 | 37.137 | 37.137 | 37.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4613) vms_mb | MB | 1 | 45.656 | 45.656 | 45.656 | 45.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4614) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4614) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4615) rss_mb | MB | 1 | 8.828 | 8.828 | 8.828 | 8.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4615) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4626) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4626) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4627) rss_mb | MB | 1 | 21.262 | 21.262 | 21.262 | 21.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4627) vms_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4629) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4629) rss_mb | MB | 2 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4629) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4629) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4630) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4630) rss_mb | MB | 2 | 10.895 | 10.895 | 10.895 | 10.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4630) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4630) vms_mb | MB | 2 | 14.906 | 14.906 | 14.906 | 14.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4631) CPU | percent | 1 | 17.846 | 17.846 | 17.846 | 17.846 | 0.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4631) rss_mb | MB | 2 | 62.178 | 58.258 | 66.098 | 66.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4631) main thread run-queue wait | percent | 1 | 0.346 | 0.346 | 0.346 | 0.346 | 0.003492 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4631) vms_mb | MB | 2 | 76.500 | 72.859 | 80.141 | 80.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4656) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4656) rss_mb | MB | 2 | 2.719 | 2.719 | 2.719 | 2.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4656) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4656) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4657) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4657) rss_mb | MB | 2 | 11.121 | 11.121 | 11.121 | 11.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4657) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4657) vms_mb | MB | 2 | 14.898 | 14.898 | 14.898 | 14.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4658) CPU | percent | 1 | 61.106 | 61.106 | 61.106 | 61.106 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4658) rss_mb | MB | 2 | 50.621 | 35.227 | 66.016 | 66.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4658) main thread run-queue wait | percent | 1 | 0.291 | 0.291 | 0.291 | 0.291 | 0.002954 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4658) vms_mb | MB | 2 | 62.092 | 44.035 | 80.148 | 80.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4675) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4675) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4676) rss_mb | MB | 1 | 21.270 | 21.270 | 21.270 | 21.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4676) vms_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4683) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4683) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4684) rss_mb | MB | 1 | 17.238 | 17.238 | 17.238 | 17.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4684) vms_mb | MB | 1 | 22.141 | 22.141 | 22.141 | 22.141 | n/a | n/a |
| sleep (PID 4689) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4689) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4689) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4689) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4689) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4689) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4692) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4692) rss_mb | MB | 7 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4692) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4692) vms_mb | MB | 7 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4693) CPU | percent | 6 | 0.165 | 0.000 | 0.992 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4693) rss_mb | MB | 7 | 11.160 | 11.160 | 11.160 | 11.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4693) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000010 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4693) vms_mb | MB | 7 | 14.915 | 14.914 | 14.918 | 14.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4694) CPU | percent | 1 | 47.685 | 47.685 | 47.685 | 47.685 | 0.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4694) rss_mb | MB | 2 | 52.482 | 38.602 | 66.363 | 66.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4694) main thread run-queue wait | percent | 1 | 0.309 | 0.309 | 0.309 | 0.309 | 0.003109 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4694) vms_mb | MB | 2 | 63.719 | 47.293 | 80.145 | 80.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4711) CPU | percent | 1 | 34.762 | 34.762 | 34.762 | 34.762 | 0.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4711) rss_mb | MB | 2 | 55.963 | 45.363 | 66.562 | 66.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4711) main thread run-queue wait | percent | 1 | 0.619 | 0.619 | 0.619 | 0.619 | 0.006232 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4711) vms_mb | MB | 2 | 67.410 | 53.406 | 81.414 | 81.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4728) rss_mb | MB | 1 | 49.863 | 49.863 | 49.863 | 49.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4728) vms_mb | MB | 1 | 57.797 | 57.797 | 57.797 | 57.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4745) CPU | percent | 1 | 71.357 | 71.357 | 71.357 | 71.357 | 0.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4745) rss_mb | MB | 2 | 41.885 | 17.648 | 66.121 | 66.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4745) main thread run-queue wait | percent | 1 | 0.287 | 0.287 | 0.287 | 0.287 | 0.002897 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4745) vms_mb | MB | 2 | 51.834 | 23.781 | 79.887 | 79.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4769) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4769) rss_mb | MB | 3 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4769) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4769) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4770) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4770) rss_mb | MB | 3 | 11.215 | 11.215 | 11.215 | 11.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4770) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4770) vms_mb | MB | 3 | 14.910 | 14.910 | 14.910 | 14.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4771) rss_mb | MB | 1 | 46.066 | 46.066 | 46.066 | 46.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4771) vms_mb | MB | 1 | 54.660 | 54.660 | 54.660 | 54.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4788) CPU | percent | 1 | 77.505 | 77.505 | 77.505 | 77.505 | 0.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4788) rss_mb | MB | 2 | 35.100 | 8.344 | 61.855 | 61.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4788) main thread run-queue wait | percent | 1 | 0.068 | 0.068 | 0.068 | 0.068 | 0.000682 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4788) vms_mb | MB | 2 | 45.123 | 13.156 | 77.090 | 77.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4812) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4812) rss_mb | MB | 7 | 2.629 | 2.629 | 2.629 | 2.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4812) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4812) vms_mb | MB | 7 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4813) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4813) rss_mb | MB | 7 | 11.027 | 11.027 | 11.027 | 11.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4813) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4813) vms_mb | MB | 7 | 14.906 | 14.906 | 14.906 | 14.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4814) CPU | percent | 1 | 77.272 | 77.272 | 77.272 | 77.272 | 0.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4814) rss_mb | MB | 2 | 40.846 | 17.672 | 64.020 | 64.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4814) main thread run-queue wait | percent | 1 | 0.070 | 0.070 | 0.070 | 0.070 | 0.000705 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4814) vms_mb | MB | 2 | 51.252 | 23.766 | 78.738 | 78.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4832) CPU | percent | 1 | 63.406 | 63.406 | 63.406 | 63.406 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4832) rss_mb | MB | 2 | 45.998 | 25.910 | 66.086 | 66.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4832) main thread run-queue wait | percent | 1 | 0.190 | 0.190 | 0.190 | 0.190 | 0.001922 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4832) vms_mb | MB | 2 | 56.068 | 31.988 | 80.148 | 80.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4850) CPU | percent | 1 | 36.763 | 36.763 | 36.763 | 36.763 | 0.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4850) rss_mb | MB | 2 | 55.088 | 43.625 | 66.551 | 66.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4850) main thread run-queue wait | percent | 1 | 0.589 | 0.589 | 0.589 | 0.589 | 0.005930 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4850) vms_mb | MB | 2 | 66.482 | 51.570 | 81.395 | 81.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4867) rss_mb | MB | 1 | 52.246 | 52.246 | 52.246 | 52.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4867) vms_mb | MB | 1 | 61.332 | 61.332 | 61.332 | 61.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4884) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4884) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4885) rss_mb | MB | 1 | 8.664 | 8.664 | 8.664 | 8.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4885) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4892) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4892) rss_mb | MB | 4 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4892) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4892) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4893) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4893) rss_mb | MB | 4 | 10.816 | 10.816 | 10.816 | 10.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4893) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4893) vms_mb | MB | 4 | 14.949 | 14.949 | 14.949 | 14.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4894) CPU | percent | 1 | 75.266 | 75.266 | 75.266 | 75.266 | 0.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4894) rss_mb | MB | 2 | 41.021 | 16.309 | 65.734 | 65.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4894) main thread run-queue wait | percent | 1 | 0.076 | 0.076 | 0.076 | 0.076 | 0.000769 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4894) vms_mb | MB | 2 | 50.957 | 22.340 | 79.574 | 79.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4913) CPU | percent | 1 | 57.438 | 57.438 | 57.438 | 57.438 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4913) rss_mb | MB | 2 | 49.062 | 32.203 | 65.922 | 65.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4913) main thread run-queue wait | percent | 1 | 0.380 | 0.380 | 0.380 | 0.380 | 0.003841 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4913) vms_mb | MB | 2 | 60.762 | 41.395 | 80.129 | 80.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4937) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 4937) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4938) rss_mb | MB | 1 | 7.414 | 7.414 | 7.414 | 7.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 4938) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4945) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4945) rss_mb | MB | 5 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4945) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 4945) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4946) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4946) rss_mb | MB | 5 | 10.520 | 10.520 | 10.520 | 10.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4946) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 4946) vms_mb | MB | 5 | 14.938 | 14.938 | 14.938 | 14.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4947) CPU | percent | 4 | 15.628 | 0.000 | 62.513 | 0.000 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4947) rss_mb | MB | 5 | 59.066 | 31.812 | 66.066 | 66.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4947) main thread run-queue wait | percent | 4 | 0.104 | 0.000 | 0.310 | 0.106 | 0.004202 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 4947) vms_mb | MB | 5 | 72.412 | 41.422 | 80.160 | 80.160 | n/a | n/a |
| sleep (PID 4953) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4953) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4953) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4953) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4953) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4953) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5080) CPU | percent | 11 | 23.539 | 1.989 | 71.573 | 5.968 | 2.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5080) rss_mb | MB | 12 | 359.364 | 216.551 | 385.559 | 385.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5080) main thread run-queue wait | percent | 11 | 1.237 | 0.002 | 6.964 | 0.024 | 0.139551 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5080) vms_mb | MB | 12 | 8782.948 | 1623.309 | 10206.898 | 10206.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5108) rss_mb | MB | 1 | 277.469 | 277.469 | 277.469 | 277.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5108) vms_mb | MB | 1 | 1672.793 | 1672.793 | 1672.793 | 1672.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5122) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5122) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5123) rss_mb | MB | 1 | 7.055 | 7.055 | 7.055 | 7.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5123) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5127) CPU | percent | 25 | 13.214 | 1.985 | 71.469 | 7.949 | 3.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5127) rss_mb | MB | 26 | 374.281 | 229.234 | 386.465 | 386.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5127) main thread run-queue wait | percent | 25 | 0.805 | 0.001 | 5.700 | 0.009 | 0.202789 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5127) vms_mb | MB | 26 | 9552.260 | 1632.305 | 10209.863 | 10209.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5186) rss_mb | MB | 1 | 290.320 | 290.320 | 290.320 | 290.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5186) vms_mb | MB | 1 | 1685.293 | 1685.293 | 1685.293 | 1685.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 5198) rss_mb | MB | 1 | 2.203 | 2.203 | 2.203 | 2.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 5198) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 5199) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 5199) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5219) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5219) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 5220) rss_mb | MB | 1 | 7.270 | 7.270 | 7.270 | 7.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 5220) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5226) rss_mb | MB | 1 | 2.672 | 2.672 | 2.672 | 2.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5226) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5227) rss_mb | MB | 1 | 13.094 | 13.094 | 13.094 | 13.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5227) vms_mb | MB | 1 | 207.207 | 207.207 | 207.207 | 207.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5241) CPU | percent | 15 | 18.327 | 1.988 | 68.460 | 1.988 | 2.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5241) rss_mb | MB | 16 | 363.441 | 212.227 | 384.258 | 384.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5241) main thread run-queue wait | percent | 15 | 2.446 | 0.003 | 14.409 | 0.003 | 0.370022 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5241) vms_mb | MB | 16 | 9136.627 | 1622.305 | 10206.707 | 10206.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5261) CPU | percent | 1 | 62.484 | 62.484 | 62.484 | 62.484 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5261) rss_mb | MB | 2 | 208.994 | 161.066 | 256.922 | 256.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5261) main thread run-queue wait | percent | 1 | 14.066 | 14.066 | 14.066 | 14.066 | 0.141826 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5261) vms_mb | MB | 2 | 1485.650 | 1317.723 | 1653.578 | 1653.578 | n/a | n/a |
| sleep (PID 5285) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5285) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5285) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5285) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5285) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5285) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5291) CPU | percent | 88 | 5.638 | 0.993 | 89.330 | 1.989 | 5.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5291) rss_mb | MB | 89 | 381.487 | 269.895 | 387.379 | 387.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5291) main thread run-queue wait | percent | 88 | 15.446 | 0.003 | 57.569 | 0.009 | 13.706835 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5291) vms_mb | MB | 89 | 10114.743 | 1666.098 | 10215.023 | 10214.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5319) CPU | percent | 1 | 91.453 | 91.453 | 91.453 | 91.453 | 0.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5319) rss_mb | MB | 2 | 199.588 | 96.371 | 302.805 | 302.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5319) main thread run-queue wait | percent | 1 | 9.849 | 9.849 | 9.849 | 9.849 | 0.099080 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5319) vms_mb | MB | 2 | 1505.432 | 1283.695 | 1727.168 | 1727.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 5331) rss_mb | MB | 1 | 2.191 | 2.191 | 2.191 | 2.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 5331) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 5332) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 5332) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5345) CPU | percent | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5345) rss_mb | MB | 46 | 2.570 | 2.570 | 2.570 | 2.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5345) main thread run-queue wait | percent | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5345) vms_mb | MB | 46 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5346) CPU | percent | 44 | 129.070 | 34.719 | 174.930 | 169.990 | 57.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5346) rss_mb | MB | 45 | 1575.142 | 15.914 | 2050.504 | 2050.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5346) main thread run-queue wait | percent | 44 | 36.069 | 0.113 | 64.512 | 52.028 | 16.006547 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5346) vms_mb | MB | 45 | 1795.654 | 208.340 | 2307.473 | 2272.473 | n/a | n/a |
| sleep (PID 5353) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5353) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5353) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5353) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5353) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5353) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5366) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5366) rss_mb | MB | 2 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5366) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5366) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5367) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5367) rss_mb | MB | 2 | 10.539 | 10.539 | 10.539 | 10.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5367) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5367) vms_mb | MB | 2 | 14.938 | 14.938 | 14.938 | 14.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5368) CPU | percent | 1 | 61.568 | 61.568 | 61.568 | 61.568 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5368) rss_mb | MB | 2 | 51.992 | 37.371 | 66.613 | 66.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5368) main thread run-queue wait | percent | 1 | 0.594 | 0.594 | 0.594 | 0.594 | 0.005984 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5368) vms_mb | MB | 2 | 63.607 | 45.789 | 81.426 | 81.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5455) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5455) rss_mb | MB | 4 | 2.691 | 2.691 | 2.691 | 2.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5455) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5455) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5456) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5456) rss_mb | MB | 4 | 11.129 | 11.129 | 11.129 | 11.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5456) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5456) vms_mb | MB | 4 | 14.938 | 14.938 | 14.938 | 14.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5457) CPU | percent | 3 | 11.587 | 0.000 | 34.760 | 0.000 | 0.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5457) rss_mb | MB | 4 | 60.646 | 44.395 | 66.062 | 66.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5457) main thread run-queue wait | percent | 3 | 0.232 | 0.000 | 0.696 | 0.000 | 0.007005 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5457) vms_mb | MB | 4 | 73.366 | 52.973 | 80.164 | 80.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5468) CPU | percent | 29 | 11.485 | 1.987 | 83.457 | 2.982 | 3.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5468) rss_mb | MB | 30 | 372.988 | 166.613 | 389.391 | 389.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5468) main thread run-queue wait | percent | 29 | 0.415 | 0.002 | 3.553 | 0.006 | 0.121915 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5468) vms_mb | MB | 30 | 9614.695 | 1577.719 | 10186.246 | 10185.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5485) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5485) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5486) rss_mb | MB | 1 | 9.453 | 9.453 | 9.453 | 9.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5486) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5498) rss_mb | MB | 1 | 278.219 | 278.219 | 278.219 | 278.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5498) vms_mb | MB | 1 | 1673.047 | 1673.047 | 1673.047 | 1673.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5514) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5514) rss_mb | MB | 9 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5514) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5514) vms_mb | MB | 9 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5515) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5515) rss_mb | MB | 9 | 11.115 | 10.664 | 11.172 | 11.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5515) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5515) vms_mb | MB | 9 | 14.909 | 14.680 | 14.938 | 14.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5516) rss_mb | MB | 1 | 60.004 | 60.004 | 60.004 | 60.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5516) vms_mb | MB | 1 | 74.383 | 74.383 | 74.383 | 74.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5517) CPU | percent | 1 | 69.458 | 69.458 | 69.458 | 69.458 | 0.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5517) rss_mb | MB | 2 | 45.695 | 25.750 | 65.641 | 65.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5517) main thread run-queue wait | percent | 1 | 0.264 | 0.264 | 0.264 | 0.264 | 0.002656 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5517) vms_mb | MB | 2 | 55.842 | 31.820 | 79.863 | 79.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5518) CPU | percent | 1 | 51.659 | 51.659 | 51.659 | 51.659 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5518) rss_mb | MB | 2 | 52.963 | 39.508 | 66.418 | 66.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5518) main thread run-queue wait | percent | 1 | 0.664 | 0.664 | 0.664 | 0.664 | 0.006683 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5518) vms_mb | MB | 2 | 64.680 | 47.977 | 81.383 | 81.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5519) rss_mb | MB | 1 | 60.828 | 60.828 | 60.828 | 60.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5519) vms_mb | MB | 1 | 75.781 | 75.781 | 75.781 | 75.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5520) CPU | percent | 1 | 59.455 | 59.455 | 59.455 | 59.455 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5520) rss_mb | MB | 2 | 50.777 | 35.559 | 65.996 | 65.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5520) main thread run-queue wait | percent | 1 | 0.164 | 0.164 | 0.164 | 0.164 | 0.001654 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5520) vms_mb | MB | 2 | 62.625 | 44.133 | 81.117 | 81.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5529) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5529) rss_mb | MB | 4 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5529) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5529) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5530) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5530) rss_mb | MB | 4 | 10.812 | 10.812 | 10.812 | 10.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5530) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5530) vms_mb | MB | 4 | 14.918 | 14.918 | 14.918 | 14.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5531) CPU | percent | 1 | 66.458 | 66.458 | 66.458 | 66.458 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5531) rss_mb | MB | 2 | 45.523 | 25.035 | 66.012 | 66.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5531) main thread run-queue wait | percent | 1 | 0.222 | 0.222 | 0.222 | 0.222 | 0.002237 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5531) vms_mb | MB | 2 | 55.873 | 31.629 | 80.117 | 80.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5532) CPU | percent | 1 | 43.685 | 43.685 | 43.685 | 43.685 | 0.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5532) rss_mb | MB | 2 | 54.635 | 43.043 | 66.227 | 66.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5532) main thread run-queue wait | percent | 1 | 0.427 | 0.427 | 0.427 | 0.427 | 0.004305 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 5532) vms_mb | MB | 2 | 66.398 | 51.410 | 81.387 | 81.387 | n/a | n/a |
| sleep (PID 5539) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5539) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5539) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5539) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5539) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5539) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5545) CPU | percent | 17 | 14.881 | 1.962 | 62.479 | 9.940 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5545) rss_mb | MB | 18 | 373.775 | 296.086 | 386.637 | 386.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5545) main thread run-queue wait | percent | 17 | 1.570 | 0.002 | 12.272 | 0.020 | 0.269394 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5545) vms_mb | MB | 18 | 9726.803 | 1690.867 | 10209.625 | 10209.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5566) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5566) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5567) rss_mb | MB | 1 | 8.570 | 8.570 | 8.570 | 8.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5567) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5570) rss_mb | MB | 1 | 193.367 | 193.367 | 193.367 | 193.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5570) vms_mb | MB | 1 | 1614.723 | 1614.723 | 1614.723 | 1614.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5590) rss_mb | MB | 1 | 2.879 | 2.879 | 2.879 | 2.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 5590) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5591) rss_mb | MB | 1 | 24.539 | 24.539 | 24.539 | 24.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 5591) vms_mb | MB | 1 | 215.965 | 215.965 | 215.965 | 215.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5606) CPU | percent | 13 | 20.531 | 0.994 | 71.319 | 7.955 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5606) rss_mb | MB | 14 | 367.796 | 235.945 | 389.742 | 389.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5606) main thread run-queue wait | percent | 13 | 2.421 | 0.003 | 14.850 | 0.022 | 0.317010 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5606) vms_mb | MB | 14 | 8985.847 | 1636.285 | 10208.527 | 10208.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — stty (PID 5622) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — stty (PID 5622) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5628) CPU | percent | 1 | 66.611 | 66.611 | 66.611 | 66.611 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5628) rss_mb | MB | 2 | 242.537 | 188.738 | 296.336 | 296.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5628) main thread run-queue wait | percent | 1 | 23.710 | 23.710 | 23.710 | 23.710 | 0.238486 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5628) vms_mb | MB | 2 | 1642.346 | 1593.973 | 1690.719 | 1690.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5654) CPU | percent | 11 | 26.251 | 2.984 | 73.484 | 3.977 | 2.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5654) rss_mb | MB | 12 | 364.599 | 237.297 | 387.113 | 387.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5654) main thread run-queue wait | percent | 11 | 3.937 | 0.011 | 14.607 | 0.011 | 0.435824 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5654) vms_mb | MB | 12 | 9483.201 | 1637.785 | 10212.148 | 10212.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5682) rss_mb | MB | 1 | 294.328 | 294.328 | 294.328 | 294.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5682) vms_mb | MB | 1 | 1688.574 | 1688.574 | 1688.574 | 1688.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5701) rss_mb | MB | 1 | 1.418 | 1.418 | 1.418 | 1.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5701) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 5702) rss_mb | MB | 1 | 20.344 | 20.344 | 20.344 | 20.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 5702) vms_mb | MB | 1 | 25.320 | 25.320 | 25.320 | 25.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5713) CPU | percent | 6 | 38.388 | 3.968 | 68.625 | 11.930 | 2.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5713) rss_mb | MB | 7 | 349.744 | 259.531 | 381.516 | 381.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5713) main thread run-queue wait | percent | 6 | 8.055 | 0.009 | 24.592 | 0.032 | 0.492663 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5713) vms_mb | MB | 7 | 8956.232 | 1655.527 | 10206.145 | 10206.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5733) CPU | percent | 1 | 67.450 | 67.450 | 67.450 | 67.450 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5733) rss_mb | MB | 2 | 228.541 | 178.219 | 278.863 | 278.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5733) main thread run-queue wait | percent | 1 | 20.938 | 20.938 | 20.938 | 20.938 | 0.211091 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5733) vms_mb | MB | 2 | 1632.395 | 1591.223 | 1673.566 | 1673.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5745) rss_mb | MB | 1 | 1.383 | 1.383 | 1.383 | 1.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5745) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5746) rss_mb | MB | 1 | 8.043 | 8.043 | 8.043 | 8.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5746) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5762) CPU | percent | 10 | 23.981 | 1.989 | 62.521 | 3.978 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5762) rss_mb | MB | 11 | 362.627 | 259.227 | 386.535 | 386.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5762) main thread run-queue wait | percent | 10 | 3.811 | 0.004 | 18.301 | 0.007 | 0.391266 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5762) vms_mb | MB | 11 | 9411.327 | 1655.293 | 10207.816 | 10207.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5781) CPU | percent | 1 | 59.154 | 59.154 | 59.154 | 59.154 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5781) rss_mb | MB | 2 | 213.672 | 166.719 | 260.625 | 260.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5781) main thread run-queue wait | percent | 1 | 25.092 | 25.092 | 25.092 | 25.092 | 0.254504 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5781) vms_mb | MB | 2 | 1617.547 | 1577.973 | 1657.121 | 1657.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5793) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5793) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5794) rss_mb | MB | 1 | 9.980 | 9.980 | 9.980 | 9.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 5794) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sleep (PID 5803) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5803) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5803) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5803) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5803) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5803) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5811) CPU | percent | 9 | 28.892 | 1.989 | 77.525 | 2.982 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5811) rss_mb | MB | 10 | 347.548 | 178.422 | 385.945 | 385.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5811) main thread run-queue wait | percent | 9 | 2.111 | 0.006 | 6.220 | 0.007 | 0.192883 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5811) vms_mb | MB | 10 | 8490.721 | 1590.969 | 10203.547 | 10203.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5839) rss_mb | MB | 1 | 229.285 | 229.285 | 229.285 | 229.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5839) vms_mb | MB | 1 | 1631.961 | 1631.961 | 1631.961 | 1631.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5858) CPU | percent | 7 | 30.109 | 3.970 | 67.787 | 11.932 | 2.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5858) rss_mb | MB | 8 | 356.114 | 272.059 | 385.992 | 385.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5858) main thread run-queue wait | percent | 7 | 3.123 | 0.012 | 17.217 | 0.012 | 0.220407 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5858) vms_mb | MB | 8 | 9121.569 | 1667.273 | 10206.566 | 10206.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5880) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 5880) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5887) rss_mb | MB | 1 | 189.262 | 189.262 | 189.262 | 189.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5887) vms_mb | MB | 1 | 1594.223 | 1594.223 | 1594.223 | 1594.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5906) CPU | percent | 7 | 34.169 | 2.981 | 73.500 | 7.953 | 2.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5906) rss_mb | MB | 8 | 352.407 | 230.449 | 387.016 | 387.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5906) main thread run-queue wait | percent | 7 | 5.017 | 0.002 | 19.278 | 0.009 | 0.354006 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5906) vms_mb | MB | 8 | 8076.461 | 1633.273 | 10210.762 | 10210.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5927) rss_mb | MB | 1 | 210.379 | 210.379 | 210.379 | 210.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5927) vms_mb | MB | 1 | 1621.160 | 1621.160 | 1621.160 | 1621.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5953) CPU | percent | 7 | 22.706 | 3.976 | 61.513 | 3.976 | 1.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5953) rss_mb | MB | 8 | 359.008 | 295.438 | 384.535 | 384.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5953) main thread run-queue wait | percent | 7 | 0.423 | 0.004 | 1.857 | 0.010 | 0.029791 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5953) vms_mb | MB | 8 | 9095.322 | 1690.414 | 10185.602 | 10151.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5981) rss_mb | MB | 1 | 187.453 | 187.453 | 187.453 | 187.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 5981) vms_mb | MB | 1 | 1593.973 | 1593.973 | 1593.973 | 1593.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6000) CPU | percent | 6 | 29.927 | 1.988 | 61.471 | 4.973 | 1.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6000) rss_mb | MB | 7 | 354.439 | 295.887 | 378.047 | 378.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6000) main thread run-queue wait | percent | 6 | 7.807 | 0.003 | 27.303 | 0.003 | 0.472724 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6000) vms_mb | MB | 7 | 8964.350 | 1690.672 | 10199.676 | 10199.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6019) CPU | percent | 1 | 58.426 | 58.426 | 58.426 | 58.426 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6019) rss_mb | MB | 2 | 225.234 | 188.410 | 262.059 | 262.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6019) main thread run-queue wait | percent | 1 | 31.010 | 31.010 | 31.010 | 31.010 | 0.313144 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6019) vms_mb | MB | 2 | 1625.637 | 1593.973 | 1657.301 | 1657.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6029) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6029) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6030) rss_mb | MB | 1 | 6.785 | 6.785 | 6.785 | 6.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6030) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6045) CPU | percent | 6 | 42.703 | 2.983 | 88.387 | 2.983 | 2.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6045) rss_mb | MB | 7 | 336.712 | 175.266 | 383.512 | 383.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6045) main thread run-queue wait | percent | 6 | 8.579 | 0.006 | 34.323 | 0.006 | 0.518391 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6045) vms_mb | MB | 7 | 7755.180 | 1590.219 | 10202.500 | 10202.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6064) CPU | percent | 1 | 58.638 | 58.638 | 58.638 | 58.638 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6064) rss_mb | MB | 2 | 265.562 | 229.035 | 302.090 | 302.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6064) main thread run-queue wait | percent | 1 | 31.108 | 31.108 | 31.108 | 31.108 | 0.312998 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6064) vms_mb | MB | 2 | 1679.195 | 1631.996 | 1726.395 | 1726.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 6076) rss_mb | MB | 1 | 48.027 | 48.027 | 48.027 | 48.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 6076) vms_mb | MB | 1 | 860.820 | 860.820 | 860.820 | 860.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6092) CPU | percent | 47 | 7.857 | 0.980 | 97.328 | 1.988 | 3.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6092) rss_mb | MB | 48 | 372.819 | 0.000 | 386.180 | 386.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6092) main thread run-queue wait | percent | 47 | 27.373 | 0.004 | 52.131 | 0.004 | 12.973618 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6092) vms_mb | MB | 48 | 9810.117 | 0.129 | 10204.211 | 10204.211 | n/a | n/a |
| sleep (PID 6108) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6108) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6108) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6108) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6108) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6108) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6113) CPU | percent | 1 | 55.605 | 55.605 | 55.605 | 55.605 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6113) rss_mb | MB | 2 | 224.385 | 187.527 | 261.242 | 261.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6113) main thread run-queue wait | percent | 1 | 15.131 | 15.131 | 15.131 | 15.131 | 0.152383 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6113) vms_mb | MB | 2 | 1625.021 | 1593.973 | 1656.070 | 1656.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6138) CPU | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6138) rss_mb | MB | 32 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6138) main thread run-queue wait | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6138) vms_mb | MB | 32 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6139) CPU | percent | 31 | 172.461 | 167.884 | 176.362 | 171.478 | 53.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6139) rss_mb | MB | 32 | 112.218 | 66.438 | 163.141 | 163.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6139) main thread run-queue wait | percent | 31 | 54.865 | 48.254 | 74.065 | 53.504 | 17.155963 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6139) vms_mb | MB | 32 | 329.987 | 283.742 | 378.891 | 378.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6173) CPU | percent | 10 | 23.876 | 1.989 | 92.430 | 1.989 | 2.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6173) rss_mb | MB | 11 | 346.169 | 139.965 | 384.242 | 384.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6173) main thread run-queue wait | percent | 10 | 0.912 | 0.003 | 3.894 | 0.006 | 0.091997 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6173) vms_mb | MB | 11 | 8618.488 | 1296.418 | 10204.938 | 10204.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6202) rss_mb | MB | 1 | 160.918 | 160.918 | 160.918 | 160.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6202) vms_mb | MB | 1 | 1317.723 | 1317.723 | 1317.723 | 1317.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6221) CPU | percent | 5 | 31.365 | 3.974 | 69.584 | 3.974 | 1.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6221) rss_mb | MB | 6 | 353.179 | 289.672 | 383.438 | 383.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6221) main thread run-queue wait | percent | 5 | 1.864 | 0.005 | 7.316 | 0.005 | 0.094018 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6221) vms_mb | MB | 6 | 8759.614 | 1685.023 | 10204.020 | 10204.020 | n/a | n/a |
| sleep (PID 6239) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6239) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6239) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6239) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6239) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6239) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6245) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6245) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6246) rss_mb | MB | 1 | 8.902 | 8.902 | 8.902 | 8.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6246) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6253) rss_mb | MB | 1 | 159.781 | 159.781 | 159.781 | 159.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6253) vms_mb | MB | 1 | 1500.219 | 1500.219 | 1500.219 | 1500.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6272) CPU | percent | 6 | 42.299 | 2.980 | 93.339 | 2.980 | 2.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6272) rss_mb | MB | 7 | 308.480 | 50.414 | 370.004 | 369.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6272) main thread run-queue wait | percent | 6 | 5.656 | 0.012 | 26.965 | 0.012 | 0.347121 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6272) vms_mb | MB | 7 | 7704.366 | 1238.512 | 10202.027 | 10202.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6296) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6296) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6297) rss_mb | MB | 1 | 8.648 | 8.648 | 8.648 | 8.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6297) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6298) CPU | percent | 1 | 65.262 | 65.262 | 65.262 | 65.262 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6298) rss_mb | MB | 2 | 119.574 | 0.000 | 239.148 | 239.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6298) main thread run-queue wait | percent | 1 | 26.480 | 26.480 | 26.480 | 26.480 | 0.271849 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6298) vms_mb | MB | 2 | 899.373 | 160.145 | 1638.602 | 1638.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6318) CPU | percent | 6 | 39.345 | 2.982 | 89.277 | 2.982 | 2.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6318) rss_mb | MB | 7 | 348.294 | 260.242 | 379.848 | 379.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6318) main thread run-queue wait | percent | 6 | 2.987 | 0.015 | 15.361 | 0.015 | 0.180653 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6318) vms_mb | MB | 7 | 7794.886 | 1656.191 | 10208.680 | 10208.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6346) CPU | percent | 1 | 89.436 | 89.436 | 89.436 | 89.436 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6346) rss_mb | MB | 2 | 228.119 | 153.660 | 302.578 | 302.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6346) main thread run-queue wait | percent | 1 | 11.164 | 11.164 | 11.164 | 11.164 | 0.112347 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6346) vms_mb | MB | 2 | 1521.598 | 1315.969 | 1727.227 | 1727.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6365) CPU | percent | 5 | 36.894 | 6.961 | 64.502 | 6.961 | 1.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6365) rss_mb | MB | 6 | 351.144 | 294.852 | 376.746 | 376.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6365) main thread run-queue wait | percent | 5 | 10.111 | 0.014 | 36.545 | 0.014 | 0.510232 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6365) vms_mb | MB | 6 | 8758.312 | 1689.656 | 10199.215 | 10198.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6384) CPU | percent | 1 | 56.432 | 56.432 | 56.432 | 56.432 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6384) rss_mb | MB | 2 | 228.049 | 186.953 | 269.145 | 269.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6384) main thread run-queue wait | percent | 1 | 31.887 | 31.887 | 31.887 | 31.887 | 0.322074 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6384) vms_mb | MB | 2 | 1629.516 | 1593.723 | 1665.309 | 1665.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6411) CPU | percent | 7 | 35.106 | 3.978 | 68.425 | 13.914 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6411) rss_mb | MB | 8 | 345.867 | 213.012 | 385.801 | 385.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6411) main thread run-queue wait | percent | 7 | 5.520 | 0.006 | 25.250 | 0.064 | 0.390421 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6411) vms_mb | MB | 8 | 8068.739 | 1622.523 | 10207.641 | 10207.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6433) CPU | percent | 1 | 71.322 | 71.322 | 71.322 | 71.322 | 0.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6433) rss_mb | MB | 2 | 248.346 | 194.043 | 302.648 | 302.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6433) main thread run-queue wait | percent | 1 | 26.611 | 26.611 | 26.611 | 26.611 | 0.268643 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6433) vms_mb | MB | 2 | 1670.807 | 1614.473 | 1727.141 | 1727.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6457) CPU | percent | 25 | 11.845 | 0.994 | 67.522 | 0.994 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6457) rss_mb | MB | 26 | 374.820 | 229.199 | 387.570 | 387.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6457) main thread run-queue wait | percent | 25 | 1.355 | 0.005 | 11.501 | 0.006 | 0.349726 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6457) vms_mb | MB | 26 | 9546.382 | 1632.301 | 10205.207 | 10204.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6476) CPU | percent | 1 | 63.177 | 63.177 | 63.177 | 63.177 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6476) rss_mb | MB | 2 | 203.586 | 153.176 | 253.996 | 253.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6476) main thread run-queue wait | percent | 1 | 14.529 | 14.529 | 14.529 | 14.529 | 0.147188 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6476) vms_mb | MB | 2 | 1479.902 | 1309.238 | 1650.566 | 1650.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6576) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6576) rss_mb | MB | 14 | 2.648 | 2.648 | 2.648 | 2.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6576) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6576) vms_mb | MB | 14 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6577) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6577) rss_mb | MB | 14 | 10.926 | 10.926 | 10.926 | 10.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6577) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000026 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6577) vms_mb | MB | 14 | 14.934 | 14.934 | 14.934 | 14.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6578) CPU | percent | 1 | 54.634 | 54.634 | 54.634 | 54.634 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6578) rss_mb | MB | 2 | 51.955 | 37.766 | 66.145 | 66.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6578) main thread run-queue wait | percent | 1 | 0.678 | 0.678 | 0.678 | 0.678 | 0.006827 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6578) vms_mb | MB | 2 | 63.025 | 45.934 | 80.117 | 80.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6579) CPU | percent | 1 | 42.702 | 42.702 | 42.702 | 42.702 | 0.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6579) rss_mb | MB | 2 | 55.709 | 45.137 | 66.281 | 66.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6579) main thread run-queue wait | percent | 1 | 0.457 | 0.457 | 0.457 | 0.457 | 0.004602 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6579) vms_mb | MB | 2 | 67.381 | 53.379 | 81.383 | 81.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6580) rss_mb | MB | 1 | 59.141 | 59.141 | 59.141 | 59.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6580) vms_mb | MB | 1 | 74.238 | 74.238 | 74.238 | 74.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6581) CPU | percent | 1 | 72.338 | 72.338 | 72.338 | 72.338 | 0.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6581) rss_mb | MB | 2 | 42.232 | 19.348 | 65.117 | 65.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6581) main thread run-queue wait | percent | 1 | 0.108 | 0.108 | 0.108 | 0.108 | 0.001092 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6581) vms_mb | MB | 2 | 52.387 | 25.219 | 79.555 | 79.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6582) CPU | percent | 1 | 48.536 | 48.536 | 48.536 | 48.536 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6582) rss_mb | MB | 2 | 49.891 | 33.844 | 65.938 | 65.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6582) main thread run-queue wait | percent | 1 | 0.063 | 0.063 | 0.063 | 0.063 | 0.000773 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6582) vms_mb | MB | 2 | 61.297 | 42.730 | 79.863 | 79.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6583) CPU | percent | 1 | 61.454 | 61.454 | 61.454 | 61.454 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6583) rss_mb | MB | 2 | 48.787 | 31.504 | 66.070 | 66.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6583) main thread run-queue wait | percent | 1 | 0.212 | 0.212 | 0.212 | 0.212 | 0.002142 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6583) vms_mb | MB | 2 | 60.625 | 41.133 | 80.117 | 80.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6584) CPU | percent | 1 | 40.662 | 40.662 | 40.662 | 40.662 | 0.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6584) rss_mb | MB | 2 | 56.020 | 45.504 | 66.535 | 66.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6584) main thread run-queue wait | percent | 1 | 0.815 | 0.815 | 0.815 | 0.815 | 0.008222 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6584) vms_mb | MB | 2 | 66.922 | 53.457 | 80.387 | 80.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6585) rss_mb | MB | 1 | 59.605 | 59.605 | 59.605 | 59.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6585) vms_mb | MB | 1 | 74.234 | 74.234 | 74.234 | 74.234 | n/a | n/a |
| sleep (PID 6592) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6592) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6592) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6592) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6592) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6592) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6598) CPU | percent | 20 | 12.496 | 0.994 | 65.563 | 1.989 | 2.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6598) rss_mb | MB | 21 | 378.357 | 294.391 | 389.605 | 389.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6598) main thread run-queue wait | percent | 20 | 1.269 | 0.002 | 15.610 | 0.011 | 0.256366 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6598) vms_mb | MB | 21 | 9791.526 | 1689.266 | 10204.496 | 10204.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6620) CPU | percent | 1 | 45.468 | 45.468 | 45.468 | 45.468 | 0.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6620) rss_mb | MB | 2 | 187.764 | 145.977 | 229.551 | 229.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6620) main thread run-queue wait | percent | 1 | 12.156 | 12.156 | 12.156 | 12.156 | 0.122978 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6620) vms_mb | MB | 2 | 1466.988 | 1301.734 | 1632.242 | 1632.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6626) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6626) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6627) rss_mb | MB | 1 | 10.582 | 10.582 | 10.582 | 10.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6627) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6643) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6643) rss_mb | MB | 5 | 2.742 | 2.742 | 2.742 | 2.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6643) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6643) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6644) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6644) rss_mb | MB | 5 | 10.746 | 10.746 | 10.746 | 10.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6644) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6644) vms_mb | MB | 5 | 14.941 | 14.941 | 14.941 | 14.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6645) rss_mb | MB | 1 | 41.961 | 41.961 | 41.961 | 41.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6645) vms_mb | MB | 1 | 49.910 | 49.910 | 49.910 | 49.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6646) rss_mb | MB | 1 | 61.164 | 61.164 | 61.164 | 61.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6646) vms_mb | MB | 1 | 75.781 | 75.781 | 75.781 | 75.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6647) CPU | percent | 1 | 57.458 | 57.458 | 57.458 | 57.458 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6647) rss_mb | MB | 2 | 51.398 | 36.621 | 66.176 | 66.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6647) main thread run-queue wait | percent | 1 | 0.412 | 0.412 | 0.412 | 0.412 | 0.004163 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6647) vms_mb | MB | 2 | 62.262 | 44.398 | 80.125 | 80.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6660) CPU | percent | 5 | 36.491 | 3.978 | 63.268 | 3.978 | 1.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6660) rss_mb | MB | 6 | 349.835 | 294.211 | 373.016 | 373.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6660) main thread run-queue wait | percent | 5 | 7.429 | 0.022 | 22.512 | 0.022 | 0.374573 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6660) vms_mb | MB | 6 | 8758.052 | 1689.496 | 10200.262 | 10199.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6679) CPU | percent | 1 | 67.437 | 67.437 | 67.437 | 67.437 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6679) rss_mb | MB | 2 | 234.230 | 188.133 | 280.328 | 280.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6679) main thread run-queue wait | percent | 1 | 23.952 | 23.952 | 23.952 | 23.952 | 0.241516 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6679) vms_mb | MB | 2 | 1634.510 | 1593.973 | 1675.047 | 1675.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6706) CPU | percent | 6 | 36.570 | 4.966 | 67.476 | 6.960 | 2.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6706) rss_mb | MB | 7 | 351.556 | 261.402 | 380.555 | 380.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6706) main thread run-queue wait | percent | 6 | 7.715 | 0.011 | 21.308 | 0.022 | 0.469941 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6706) vms_mb | MB | 7 | 8946.376 | 1656.723 | 10200.141 | 10200.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6725) CPU | percent | 1 | 61.476 | 61.476 | 61.476 | 61.476 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6725) rss_mb | MB | 2 | 215.611 | 170.637 | 260.586 | 260.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6725) main thread run-queue wait | percent | 1 | 21.787 | 21.787 | 21.787 | 21.787 | 0.219729 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6725) vms_mb | MB | 2 | 1618.012 | 1579.723 | 1656.301 | 1656.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 6750) rss_mb | MB | 1 | 56.586 | 56.586 | 56.586 | 56.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 6750) vms_mb | MB | 1 | 899.430 | 899.430 | 899.430 | 899.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6753) CPU | percent | 7 | 35.289 | 3.978 | 70.496 | 7.955 | 2.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6753) rss_mb | MB | 8 | 344.309 | 215.148 | 385.363 | 385.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6753) main thread run-queue wait | percent | 7 | 6.010 | 0.007 | 18.953 | 0.010 | 0.424333 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6753) vms_mb | MB | 8 | 8063.345 | 1623.043 | 10204.070 | 10204.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6770) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6770) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6771) rss_mb | MB | 1 | 9.305 | 9.305 | 9.305 | 9.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6771) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6772) CPU | percent | 1 | 60.445 | 60.445 | 60.445 | 60.445 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6772) rss_mb | MB | 2 | 129.404 | 29.266 | 229.543 | 229.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6772) main thread run-queue wait | percent | 1 | 14.023 | 14.023 | 14.023 | 14.023 | 0.141516 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6772) vms_mb | MB | 2 | 939.453 | 247.301 | 1631.605 | 1631.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6784) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6784) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6785) rss_mb | MB | 1 | 7.473 | 7.473 | 7.473 | 7.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6785) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6800) CPU | percent | 7 | 43.683 | 2.981 | 95.388 | 12.931 | 3.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6800) rss_mb | MB | 8 | 312.472 | 28.902 | 374.172 | 374.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6800) main thread run-queue wait | percent | 7 | 3.619 | 0.003 | 15.519 | 0.022 | 0.255431 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6800) vms_mb | MB | 8 | 7889.896 | 255.305 | 10208.223 | 10208.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6822) rss_mb | MB | 1 | 1.609 | 1.609 | 1.609 | 1.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6822) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6823) rss_mb | MB | 1 | 10.227 | 10.227 | 10.227 | 10.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6823) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6827) rss_mb | MB | 1 | 187.477 | 187.477 | 187.477 | 187.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6827) vms_mb | MB | 1 | 1593.973 | 1593.973 | 1593.973 | 1593.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6846) CPU | percent | 5 | 41.873 | 5.966 | 72.500 | 8.933 | 2.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6846) rss_mb | MB | 6 | 338.852 | 236.051 | 377.051 | 377.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6846) main thread run-queue wait | percent | 5 | 2.950 | 0.009 | 10.236 | 1.867 | 0.148882 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6846) vms_mb | MB | 6 | 7361.656 | 1636.516 | 10202.438 | 10202.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6874) CPU | percent | 1 | 93.297 | 93.297 | 93.297 | 93.297 | 0.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6874) rss_mb | MB | 2 | 168.568 | 35.191 | 301.945 | 301.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6874) main thread run-queue wait | percent | 1 | 6.434 | 6.434 | 6.434 | 6.434 | 0.064822 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6874) vms_mb | MB | 2 | 1447.371 | 1168.414 | 1726.328 | 1726.328 | n/a | n/a |
| sleep (PID 6883) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6883) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6883) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6883) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6883) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6883) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6893) CPU | percent | 5 | 52.157 | 8.947 | 91.422 | 8.947 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6893) rss_mb | MB | 6 | 319.293 | 161.035 | 374.656 | 374.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6893) main thread run-queue wait | percent | 5 | 4.174 | 0.341 | 11.951 | 0.450 | 0.210420 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6893) vms_mb | MB | 6 | 7305.921 | 1317.719 | 10203.051 | 10203.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6917) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6917) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6918) rss_mb | MB | 1 | 7.270 | 7.270 | 7.270 | 7.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6918) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6919) rss_mb | MB | 1 | 228.566 | 228.566 | 228.566 | 228.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6919) vms_mb | MB | 1 | 1635.121 | 1635.121 | 1635.121 | 1635.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6941) CPU | percent | 21 | 15.918 | 0.995 | 97.322 | 1.985 | 3.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6941) rss_mb | MB | 22 | 362.823 | 35.160 | 388.340 | 388.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6941) main thread run-queue wait | percent | 21 | 1.597 | 0.005 | 18.491 | 0.006 | 0.338492 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6941) vms_mb | MB | 22 | 9401.038 | 1168.414 | 10204.684 | 10204.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6960) CPU | percent | 1 | 59.445 | 59.445 | 59.445 | 59.445 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6960) rss_mb | MB | 2 | 230.842 | 189.227 | 272.457 | 272.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6960) main thread run-queue wait | percent | 1 | 18.271 | 18.271 | 18.271 | 18.271 | 0.184415 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 6960) vms_mb | MB | 2 | 1631.391 | 1594.473 | 1668.309 | 1668.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6970) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6970) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6971) rss_mb | MB | 1 | 8.516 | 8.516 | 8.516 | 8.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 6971) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6983) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 6983) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 6984) rss_mb | MB | 1 | 19.520 | 19.520 | 19.520 | 19.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 6984) vms_mb | MB | 1 | 24.934 | 24.934 | 24.934 | 24.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6985) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6985) rss_mb | MB | 8 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6985) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 6985) vms_mb | MB | 8 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6986) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6986) rss_mb | MB | 8 | 10.812 | 10.812 | 10.812 | 10.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6986) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 6986) vms_mb | MB | 8 | 14.996 | 14.996 | 14.996 | 14.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6987) CPU | percent | 3 | 7.593 | 0.000 | 22.779 | 0.000 | 0.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6987) rss_mb | MB | 4 | 61.924 | 49.977 | 65.906 | 65.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6987) main thread run-queue wait | percent | 3 | 0.128 | 0.000 | 0.383 | 0.000 | 0.003865 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6987) vms_mb | MB | 4 | 74.862 | 58.980 | 80.156 | 80.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6990) CPU | percent | 1 | 30.760 | 30.760 | 30.760 | 30.760 | 0.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6990) rss_mb | MB | 2 | 55.730 | 45.223 | 66.238 | 66.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6990) main thread run-queue wait | percent | 1 | 0.286 | 0.286 | 0.286 | 0.286 | 0.002885 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6990) vms_mb | MB | 2 | 66.795 | 53.473 | 80.117 | 80.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6991) CPU | percent | 1 | 70.516 | 70.516 | 70.516 | 70.516 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6991) rss_mb | MB | 2 | 42.904 | 19.555 | 66.254 | 66.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6991) main thread run-queue wait | percent | 1 | 0.182 | 0.182 | 0.182 | 0.182 | 0.001833 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 6991) vms_mb | MB | 2 | 52.699 | 25.539 | 79.859 | 79.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7002) CPU | percent | 5 | 41.786 | 3.969 | 73.342 | 3.969 | 2.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7002) rss_mb | MB | 6 | 340.710 | 237.539 | 375.953 | 375.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7002) main thread run-queue wait | percent | 5 | 4.776 | 0.003 | 12.495 | 0.003 | 0.242478 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7002) vms_mb | MB | 6 | 7384.213 | 1637.781 | 10200.012 | 10199.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7023) rss_mb | MB | 1 | 205.973 | 205.973 | 205.973 | 205.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7023) vms_mb | MB | 1 | 1619.016 | 1619.016 | 1619.016 | 1619.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7047) CPU | percent | 15 | 22.014 | 0.994 | 95.265 | 2.984 | 3.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7047) rss_mb | MB | 16 | 354.845 | 71.500 | 390.156 | 389.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7047) main thread run-queue wait | percent | 15 | 4.054 | 0.000 | 18.289 | 0.000 | 0.613134 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7047) vms_mb | MB | 16 | 9108.829 | 1283.598 | 10208.980 | 10208.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7066) CPU | percent | 1 | 68.340 | 68.340 | 68.340 | 68.340 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7066) rss_mb | MB | 2 | 232.846 | 185.004 | 280.688 | 280.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7066) main thread run-queue wait | percent | 1 | 18.217 | 18.217 | 18.217 | 18.217 | 0.183934 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7066) vms_mb | MB | 2 | 1634.154 | 1592.973 | 1675.336 | 1675.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7094) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7094) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 7095) rss_mb | MB | 1 | 21.008 | 21.008 | 21.008 | 21.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 7095) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7109) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7109) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 7110) rss_mb | MB | 1 | 9.355 | 9.355 | 9.355 | 9.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 7110) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7119) CPU | percent | 6 | 41.510 | 2.979 | 73.410 | 2.979 | 2.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7119) rss_mb | MB | 7 | 338.828 | 189.309 | 382.254 | 382.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7119) main thread run-queue wait | percent | 6 | 4.908 | 0.006 | 16.818 | 0.006 | 0.297151 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7119) vms_mb | MB | 7 | 7759.130 | 1594.469 | 10205.871 | 10205.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7138) CPU | percent | 1 | 59.377 | 59.377 | 59.377 | 59.377 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7138) rss_mb | MB | 2 | 259.918 | 222.520 | 297.316 | 297.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7138) main thread run-queue wait | percent | 1 | 15.363 | 15.363 | 15.363 | 15.363 | 0.155242 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7138) vms_mb | MB | 2 | 1675.248 | 1625.992 | 1724.504 | 1724.504 | n/a | n/a |
| sleep (PID 7162) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7162) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7162) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7162) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7162) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7162) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7168) CPU | percent | 5 | 36.339 | 5.963 | 67.497 | 5.967 | 1.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7168) rss_mb | MB | 6 | 354.189 | 294.375 | 383.059 | 383.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7168) main thread run-queue wait | percent | 5 | 1.848 | 0.016 | 8.060 | 0.016 | 0.092991 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7168) vms_mb | MB | 6 | 8765.446 | 1689.273 | 10207.832 | 10207.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7197) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7197) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7198) rss_mb | MB | 1 | 6.984 | 6.984 | 6.984 | 6.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7198) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7210) CPU | percent | 6 | 48.821 | 2.981 | 82.399 | 7.949 | 2.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7210) rss_mb | MB | 7 | 332.540 | 175.961 | 381.328 | 381.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7210) main thread run-queue wait | percent | 6 | 3.467 | 0.006 | 9.385 | 0.020 | 0.209581 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7210) vms_mb | MB | 7 | 7762.769 | 1590.469 | 10210.797 | 10210.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7231) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7231) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7232) rss_mb | MB | 1 | 8.695 | 8.695 | 8.695 | 8.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7232) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7243) CPU | percent | 5 | 45.584 | 3.976 | 72.550 | 3.976 | 2.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7243) rss_mb | MB | 6 | 338.213 | 230.367 | 376.117 | 376.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7243) main thread run-queue wait | percent | 5 | 8.232 | 0.005 | 19.186 | 0.005 | 0.419580 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7243) vms_mb | MB | 6 | 7356.701 | 1633.055 | 10207.500 | 10207.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7262) CPU | percent | 1 | 60.316 | 60.316 | 60.316 | 60.316 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7262) rss_mb | MB | 2 | 172.896 | 110.000 | 235.793 | 235.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7262) main thread run-queue wait | percent | 1 | 20.569 | 20.569 | 20.569 | 20.569 | 0.208022 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7262) vms_mb | MB | 2 | 1460.258 | 1283.695 | 1636.820 | 1636.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7274) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7274) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7275) rss_mb | MB | 1 | 8.949 | 8.949 | 8.949 | 8.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7275) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7290) CPU | percent | 5 | 40.106 | 3.978 | 72.582 | 3.978 | 2.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7290) rss_mb | MB | 6 | 346.513 | 261.383 | 378.199 | 378.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7290) main thread run-queue wait | percent | 5 | 4.616 | 0.081 | 17.444 | 0.081 | 0.232742 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7290) vms_mb | MB | 6 | 8756.130 | 1657.023 | 10204.621 | 10204.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7313) rss_mb | MB | 1 | 199.953 | 199.953 | 199.953 | 199.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7313) vms_mb | MB | 1 | 1617.484 | 1617.484 | 1617.484 | 1617.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7335) CPU | percent | 6 | 41.199 | 2.981 | 71.597 | 9.946 | 2.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7335) rss_mb | MB | 7 | 338.132 | 204.266 | 377.105 | 377.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7335) main thread run-queue wait | percent | 6 | 7.232 | 0.013 | 28.231 | 0.022 | 0.437270 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7335) vms_mb | MB | 7 | 7759.617 | 1618.527 | 10204.695 | 10204.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7355) CPU | percent | 1 | 59.560 | 59.560 | 59.560 | 59.560 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7355) rss_mb | MB | 2 | 266.252 | 229.059 | 303.445 | 303.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7355) main thread run-queue wait | percent | 1 | 19.374 | 19.374 | 19.374 | 19.374 | 0.195167 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7355) vms_mb | MB | 2 | 1679.543 | 1631.707 | 1727.379 | 1727.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7381) CPU | percent | 5 | 42.113 | 3.971 | 75.565 | 3.971 | 2.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7381) rss_mb | MB | 6 | 340.298 | 237.344 | 375.285 | 375.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7381) main thread run-queue wait | percent | 5 | 4.904 | 0.007 | 17.542 | 0.007 | 0.247001 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7381) vms_mb | MB | 6 | 7385.519 | 1637.738 | 10204.414 | 10204.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7407) rss_mb | MB | 1 | 166.824 | 166.824 | 166.824 | 166.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7407) vms_mb | MB | 1 | 1577.723 | 1577.723 | 1577.723 | 1577.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7426) CPU | percent | 5 | 38.928 | 4.956 | 74.534 | 5.966 | 1.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7426) rss_mb | MB | 6 | 348.385 | 277.812 | 376.715 | 376.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7426) main thread run-queue wait | percent | 5 | 3.679 | 0.005 | 15.387 | 0.005 | 0.185340 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7426) vms_mb | MB | 6 | 8760.228 | 1672.996 | 10204.148 | 10204.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7454) rss_mb | MB | 1 | 166.828 | 166.828 | 166.828 | 166.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7454) vms_mb | MB | 1 | 1577.973 | 1577.973 | 1577.973 | 1577.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 7466) rss_mb | MB | 1 | 52.531 | 52.531 | 52.531 | 52.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 7466) vms_mb | MB | 1 | 904.129 | 904.129 | 904.129 | 904.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7471) CPU | percent | 15 | 18.787 | 1.988 | 71.567 | 2.983 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7471) rss_mb | MB | 16 | 369.089 | 229.152 | 392.789 | 392.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7471) main thread run-queue wait | percent | 15 | 2.978 | 0.001 | 16.172 | 0.008 | 0.450151 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7471) vms_mb | MB | 16 | 9138.208 | 1632.262 | 10209.094 | 10208.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7490) CPU | percent | 1 | 61.519 | 61.519 | 61.519 | 61.519 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7490) rss_mb | MB | 2 | 160.375 | 85.191 | 235.559 | 235.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7490) main thread run-queue wait | percent | 1 | 13.091 | 13.091 | 13.091 | 13.091 | 0.131931 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7490) vms_mb | MB | 2 | 1460.033 | 1283.695 | 1636.371 | 1636.371 | n/a | n/a |
| sleep (PID 7514) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7514) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7514) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7514) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7514) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7514) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7515) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7515) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 7516) rss_mb | MB | 1 | 20.867 | 20.867 | 20.867 | 20.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 7516) vms_mb | MB | 1 | 25.578 | 25.578 | 25.578 | 25.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7534) CPU | percent | 19 | 14.937 | 1.985 | 79.453 | 7.956 | 2.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7534) rss_mb | MB | 20 | 376.203 | 177.598 | 399.715 | 399.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7534) main thread run-queue wait | percent | 19 | 3.230 | 0.003 | 23.006 | 0.018 | 0.618055 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7534) vms_mb | MB | 20 | 9344.948 | 1590.969 | 10202.367 | 10202.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7557) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7557) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7558) rss_mb | MB | 1 | 8.043 | 8.043 | 8.043 | 8.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7558) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7562) rss_mb | MB | 1 | 184.945 | 184.945 | 184.945 | 184.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7562) vms_mb | MB | 1 | 1593.223 | 1593.223 | 1593.223 | 1593.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7576) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7576) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 7577) rss_mb | MB | 1 | 16.516 | 16.516 | 16.516 | 16.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 7577) vms_mb | MB | 1 | 21.844 | 21.844 | 21.844 | 21.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 7578) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 7578) rss_mb | MB | 3 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 7578) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 7578) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 7579) CPU | percent | 2 | 150.502 | 147.128 | 153.875 | 147.128 | 3.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 7579) rss_mb | MB | 3 | 86.987 | 72.309 | 111.398 | 111.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 7579) main thread run-queue wait | percent | 2 | 26.901 | 24.027 | 29.775 | 24.027 | 0.541623 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 7579) vms_mb | MB | 3 | 306.276 | 291.484 | 330.859 | 330.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7610) CPU | percent | 6 | 37.168 | 5.964 | 70.138 | 5.964 | 2.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7610) rss_mb | MB | 7 | 346.379 | 235.695 | 382.738 | 382.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7610) main thread run-queue wait | percent | 6 | 5.097 | 0.005 | 16.036 | 0.025 | 0.308675 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7610) vms_mb | MB | 7 | 7762.286 | 1636.293 | 10200.969 | 10200.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7629) CPU | percent | 1 | 52.624 | 52.624 | 52.624 | 52.624 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7629) rss_mb | MB | 2 | 197.090 | 158.320 | 235.859 | 235.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7629) main thread run-queue wait | percent | 1 | 15.226 | 15.226 | 15.226 | 15.226 | 0.153346 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7629) vms_mb | MB | 2 | 1568.533 | 1499.969 | 1637.098 | 1637.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7641) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7641) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7642) rss_mb | MB | 1 | 8.535 | 8.535 | 8.535 | 8.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7642) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7652) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7652) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7653) rss_mb | MB | 1 | 9.355 | 9.355 | 9.355 | 9.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7653) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7657) CPU | percent | 17 | 16.407 | 0.981 | 72.428 | 0.995 | 2.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7657) rss_mb | MB | 18 | 370.324 | 199.195 | 390.949 | 390.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7657) main thread run-queue wait | percent | 17 | 2.412 | 0.003 | 20.528 | 0.004 | 0.413035 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7657) vms_mb | MB | 18 | 9256.510 | 1617.523 | 10208.887 | 10208.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7676) CPU | percent | 1 | 58.525 | 58.525 | 58.525 | 58.525 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7676) rss_mb | MB | 2 | 263.010 | 229.312 | 296.707 | 296.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7676) main thread run-queue wait | percent | 1 | 19.013 | 19.013 | 19.013 | 19.013 | 0.191670 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7676) vms_mb | MB | 2 | 1661.471 | 1631.973 | 1690.969 | 1690.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7704) CPU | percent | 7 | 29.025 | 2.983 | 68.446 | 3.975 | 2.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7704) rss_mb | MB | 8 | 362.005 | 289.504 | 388.539 | 388.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7704) main thread run-queue wait | percent | 7 | 5.509 | 0.003 | 21.004 | 0.010 | 0.389478 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7704) vms_mb | MB | 8 | 9120.477 | 1684.277 | 10204.711 | 10204.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7724) CPU | percent | 1 | 66.499 | 66.499 | 66.499 | 66.499 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7724) rss_mb | MB | 2 | 223.494 | 175.250 | 271.738 | 271.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7724) main thread run-queue wait | percent | 1 | 18.283 | 18.283 | 18.283 | 18.283 | 0.184203 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7724) vms_mb | MB | 2 | 1628.398 | 1590.223 | 1666.574 | 1666.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 7754) CPU | percent | 5 | 28.778 | 3.968 | 67.479 | 5.955 | 1.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 7754) rss_mb | MB | 6 | 355.342 | 306.305 | 378.910 | 378.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 7754) main thread run-queue wait | percent | 5 | 1.082 | 0.021 | 3.065 | 0.021 | 0.054536 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 7754) vms_mb | MB | 6 | 8767.839 | 1725.965 | 10197.637 | 10197.637 | n/a | n/a |
| sleep (PID 7764) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7764) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7764) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7764) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7764) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7764) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7784) rss_mb | MB | 1 | 144.020 | 144.020 | 144.020 | 144.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7784) vms_mb | MB | 1 | 1299.805 | 1299.805 | 1299.805 | 1299.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7803) CPU | percent | 6 | 45.475 | 3.966 | 93.256 | 3.966 | 2.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7803) rss_mb | MB | 7 | 311.120 | 40.266 | 385.090 | 385.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7803) main thread run-queue wait | percent | 6 | 3.874 | 0.024 | 13.851 | 1.714 | 0.234321 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7803) vms_mb | MB | 7 | 7688.887 | 1172.289 | 10208.574 | 10208.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7825) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7825) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7826) rss_mb | MB | 1 | 10.137 | 10.137 | 10.137 | 10.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7826) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7834) rss_mb | MB | 1 | 214.895 | 214.895 | 214.895 | 214.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7834) vms_mb | MB | 1 | 1622.973 | 1622.973 | 1622.973 | 1622.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7851) CPU | percent | 11 | 20.154 | 1.989 | 70.550 | 1.989 | 2.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7851) rss_mb | MB | 12 | 363.461 | 262.418 | 383.930 | 383.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7851) main thread run-queue wait | percent | 11 | 3.043 | 0.002 | 14.956 | 0.004 | 0.344844 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7851) vms_mb | MB | 12 | 9475.433 | 1658.012 | 10204.680 | 10204.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7870) CPU | percent | 1 | 68.055 | 68.055 | 68.055 | 68.055 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7870) rss_mb | MB | 2 | 211.760 | 161.121 | 262.398 | 262.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7870) main thread run-queue wait | percent | 1 | 12.223 | 12.223 | 12.223 | 12.223 | 0.123925 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7870) vms_mb | MB | 2 | 1578.777 | 1500.469 | 1657.086 | 1657.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7898) CPU | percent | 7 | 30.079 | 2.983 | 75.525 | 12.927 | 2.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7898) rss_mb | MB | 8 | 360.405 | 281.078 | 390.184 | 390.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7898) main thread run-queue wait | percent | 7 | 3.689 | 0.003 | 19.717 | 0.032 | 0.260098 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7898) vms_mb | MB | 8 | 9123.706 | 1676.750 | 10208.965 | 10208.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7921) CPU | percent | 1 | 44.666 | 44.666 | 44.666 | 44.666 | 0.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7921) rss_mb | MB | 2 | 171.344 | 113.879 | 228.809 | 228.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7921) main thread run-queue wait | percent | 1 | 22.298 | 22.298 | 22.298 | 22.298 | 0.224642 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7921) vms_mb | MB | 2 | 1457.811 | 1283.695 | 1631.926 | 1631.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7945) CPU | percent | 11 | 23.003 | 0.994 | 71.596 | 6.896 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7945) rss_mb | MB | 12 | 364.800 | 230.367 | 392.102 | 392.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7945) main thread run-queue wait | percent | 11 | 4.077 | 0.002 | 27.299 | 0.016 | 0.452282 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7945) vms_mb | MB | 12 | 8781.160 | 1633.297 | 10207.398 | 10207.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7962) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 7962) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7963) rss_mb | MB | 1 | 8.945 | 8.945 | 8.945 | 8.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 7963) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7964) CPU | percent | 1 | 61.443 | 61.443 | 61.443 | 61.443 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7964) rss_mb | MB | 2 | 141.877 | 48.273 | 235.480 | 235.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7964) main thread run-queue wait | percent | 1 | 13.131 | 13.131 | 13.131 | 13.131 | 0.132496 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7964) vms_mb | MB | 2 | 1437.598 | 1238.609 | 1636.586 | 1636.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7992) CPU | percent | 10 | 23.772 | 1.989 | 70.492 | 2.983 | 2.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7992) rss_mb | MB | 11 | 357.941 | 244.426 | 383.344 | 383.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7992) main thread run-queue wait | percent | 10 | 2.211 | 0.000 | 12.387 | 0.009 | 0.224513 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 7992) vms_mb | MB | 11 | 8664.443 | 1640.781 | 10207.914 | 10207.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8094) CPU | percent | 1 | 76.354 | 76.354 | 76.354 | 76.354 | 0.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8094) rss_mb | MB | 2 | 223.994 | 153.977 | 294.012 | 294.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8094) main thread run-queue wait | percent | 1 | 19.222 | 19.222 | 19.222 | 19.222 | 0.196363 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8094) vms_mb | MB | 2 | 1594.381 | 1499.469 | 1689.293 | 1689.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8116) CPU | percent | 11 | 17.431 | 0.994 | 67.491 | 0.994 | 1.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8116) rss_mb | MB | 12 | 363.067 | 260.105 | 385.883 | 385.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8116) main thread run-queue wait | percent | 11 | 0.578 | 0.001 | 3.799 | 0.003 | 0.063992 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8116) vms_mb | MB | 12 | 8785.264 | 1655.516 | 10191.180 | 10191.180 | n/a | n/a |
| sleep (PID 8126) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8126) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8126) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8126) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8126) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8126) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8147) rss_mb | MB | 1 | 160.086 | 160.086 | 160.086 | 160.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8147) vms_mb | MB | 1 | 1316.840 | 1316.840 | 1316.840 | 1316.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8166) CPU | percent | 5 | 42.279 | 4.971 | 82.322 | 4.971 | 2.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8166) rss_mb | MB | 6 | 351.559 | 286.945 | 377.020 | 377.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8166) main thread run-queue wait | percent | 5 | 5.255 | 0.057 | 24.592 | 0.726 | 0.264869 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8166) vms_mb | MB | 6 | 8763.417 | 1682.000 | 10208.254 | 10208.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8189) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8189) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8190) rss_mb | MB | 1 | 9.715 | 9.715 | 9.715 | 9.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8190) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8196) rss_mb | MB | 1 | 237.562 | 237.562 | 237.562 | 237.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8196) vms_mb | MB | 1 | 1637.324 | 1637.324 | 1637.324 | 1637.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8213) CPU | percent | 11 | 17.234 | 1.988 | 61.648 | 1.988 | 1.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8213) rss_mb | MB | 12 | 369.439 | 295.824 | 386.227 | 386.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8213) main thread run-queue wait | percent | 11 | 2.863 | 0.002 | 24.756 | 0.004 | 0.317711 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8213) vms_mb | MB | 12 | 9482.662 | 1690.656 | 10203.594 | 10203.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8232) CPU | percent | 1 | 61.403 | 61.403 | 61.403 | 61.403 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8232) rss_mb | MB | 2 | 233.441 | 187.547 | 279.336 | 279.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8232) main thread run-queue wait | percent | 1 | 29.031 | 29.031 | 29.031 | 29.031 | 0.293132 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8232) vms_mb | MB | 2 | 1634.086 | 1593.973 | 1674.199 | 1674.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8242) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8242) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8243) rss_mb | MB | 1 | 10.746 | 10.746 | 10.746 | 10.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8243) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8260) CPU | percent | 23 | 13.476 | 0.993 | 83.901 | 1.988 | 3.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8260) rss_mb | MB | 24 | 376.938 | 260.062 | 391.836 | 391.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8260) main thread run-queue wait | percent | 23 | 1.306 | 0.001 | 13.082 | 0.004 | 0.303285 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8260) vms_mb | MB | 24 | 9500.335 | 1656.055 | 10210.285 | 10210.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8279) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8279) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8280) rss_mb | MB | 1 | 10.691 | 10.691 | 10.691 | 10.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8280) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8285) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8285) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8286) rss_mb | MB | 1 | 9.562 | 9.562 | 9.562 | 9.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8286) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8291) rss_mb | MB | 1 | 295.367 | 295.367 | 295.367 | 295.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8291) vms_mb | MB | 1 | 1690.000 | 1690.000 | 1690.000 | 1690.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 8309) rss_mb | MB | 1 | 2.766 | 2.766 | 2.766 | 2.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 8309) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 8310) rss_mb | MB | 1 | 21.438 | 21.438 | 21.438 | 21.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 8310) vms_mb | MB | 1 | 213.723 | 213.723 | 213.723 | 213.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8325) CPU | percent | 7 | 40.504 | 3.968 | 91.154 | 4.971 | 2.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8325) rss_mb | MB | 8 | 312.870 | 0.000 | 383.168 | 383.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8325) main thread run-queue wait | percent | 7 | 2.407 | 0.009 | 11.831 | 0.010 | 0.170125 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8325) vms_mb | MB | 8 | 7869.741 | 160.145 | 10203.719 | 10203.719 | n/a | n/a |
| sleep (PID 8345) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8345) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8345) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8345) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8345) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8345) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8348) rss_mb | MB | 1 | 1.488 | 1.488 | 1.488 | 1.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8348) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8349) rss_mb | MB | 1 | 1.488 | 1.488 | 1.488 | 1.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8349) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8355) rss_mb | MB | 1 | 171.727 | 171.727 | 171.727 | 171.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8355) vms_mb | MB | 1 | 1579.473 | 1579.473 | 1579.473 | 1579.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8374) CPU | percent | 14 | 21.394 | 0.995 | 76.082 | 32.826 | 3.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8374) rss_mb | MB | 15 | 361.484 | 180.340 | 383.387 | 383.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8374) main thread run-queue wait | percent | 14 | 1.798 | 0.002 | 7.862 | 7.862 | 0.254319 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8374) vms_mb | MB | 15 | 9062.776 | 1591.219 | 10202.934 | 10202.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8402) rss_mb | MB | 1 | 160.320 | 160.320 | 160.320 | 160.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8402) vms_mb | MB | 1 | 1316.840 | 1316.840 | 1316.840 | 1316.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8421) CPU | percent | 22 | 12.911 | 0.994 | 70.464 | 5.967 | 2.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8421) rss_mb | MB | 23 | 378.292 | 235.355 | 392.871 | 392.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8421) main thread run-queue wait | percent | 22 | 1.272 | 0.001 | 14.417 | 0.028 | 0.281630 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8421) vms_mb | MB | 23 | 9463.564 | 1636.016 | 10208.488 | 10207.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8445) rss_mb | MB | 1 | 207.258 | 207.258 | 207.258 | 207.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8445) vms_mb | MB | 1 | 1619.465 | 1619.465 | 1619.465 | 1619.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 8464) rss_mb | MB | 1 | 2.133 | 2.133 | 2.133 | 2.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 8464) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 8465) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 8465) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8466) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8466) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 8467) rss_mb | MB | 1 | 15.230 | 15.230 | 15.230 | 15.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 8467) vms_mb | MB | 1 | 20.242 | 20.242 | 20.242 | 20.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8482) CPU | percent | 7 | 33.046 | 3.972 | 77.454 | 5.967 | 2.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8482) rss_mb | MB | 8 | 356.603 | 241.973 | 393.680 | 393.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8482) main thread run-queue wait | percent | 7 | 2.873 | 0.002 | 9.354 | 0.006 | 0.202533 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8482) vms_mb | MB | 8 | 8089.350 | 1640.051 | 10212.215 | 10212.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8506) rss_mb | MB | 1 | 208.250 | 208.250 | 208.250 | 208.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8506) vms_mb | MB | 1 | 1619.465 | 1619.465 | 1619.465 | 1619.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8532) CPU | percent | 10 | 24.794 | 2.977 | 77.558 | 4.972 | 2.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8532) rss_mb | MB | 11 | 363.844 | 256.441 | 387.594 | 387.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8532) main thread run-queue wait | percent | 10 | 3.355 | 0.005 | 22.467 | 0.014 | 0.339388 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8532) vms_mb | MB | 11 | 9399.942 | 1652.809 | 10210.434 | 10210.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8553) CPU | percent | 1 | 68.069 | 68.069 | 68.069 | 68.069 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8553) rss_mb | MB | 2 | 236.928 | 179.648 | 294.207 | 294.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8553) main thread run-queue wait | percent | 1 | 28.337 | 28.337 | 28.337 | 28.337 | 0.287241 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8553) vms_mb | MB | 2 | 1640.012 | 1591.223 | 1688.801 | 1688.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8563) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8563) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8564) rss_mb | MB | 1 | 8.980 | 8.980 | 8.980 | 8.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8564) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sleep (PID 8573) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8573) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8573) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8573) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8573) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8573) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8581) CPU | percent | 10 | 20.845 | 0.995 | 78.381 | 0.995 | 2.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8581) rss_mb | MB | 11 | 366.685 | 259.434 | 390.156 | 390.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8581) main thread run-queue wait | percent | 10 | 0.466 | 0.005 | 2.404 | 0.005 | 0.046942 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8581) vms_mb | MB | 11 | 9398.070 | 1655.781 | 10184.176 | 10184.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8618) CPU | percent | 12 | 25.409 | 2.983 | 86.261 | 4.973 | 3.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8618) rss_mb | MB | 13 | 356.477 | 158.762 | 390.777 | 390.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8618) main thread run-queue wait | percent | 12 | 3.694 | 0.004 | 18.161 | 0.043 | 0.447942 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8618) vms_mb | MB | 13 | 8876.016 | 1499.965 | 10209.172 | 10209.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8637) CPU | percent | 1 | 59.440 | 59.440 | 59.440 | 59.440 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8637) rss_mb | MB | 2 | 235.615 | 193.664 | 277.566 | 277.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8637) main thread run-queue wait | percent | 1 | 22.379 | 22.379 | 22.379 | 22.379 | 0.225896 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8637) vms_mb | MB | 2 | 1643.529 | 1613.973 | 1673.086 | 1673.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8666) CPU | percent | 7 | 38.311 | 3.973 | 73.598 | 7.953 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8666) rss_mb | MB | 8 | 344.032 | 193.434 | 388.191 | 388.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8666) main thread run-queue wait | percent | 7 | 5.542 | 0.007 | 23.542 | 0.007 | 0.391284 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8666) vms_mb | MB | 8 | 8066.019 | 1614.469 | 10209.918 | 10209.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8686) CPU | percent | 1 | 57.430 | 57.430 | 57.430 | 57.430 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8686) rss_mb | MB | 2 | 262.900 | 229.449 | 296.352 | 296.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8686) main thread run-queue wait | percent | 1 | 25.602 | 25.602 | 25.602 | 25.602 | 0.258562 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8686) vms_mb | MB | 2 | 1661.527 | 1632.234 | 1690.820 | 1690.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8696) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8696) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8697) rss_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8697) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8712) CPU | percent | 11 | 21.922 | 1.988 | 79.369 | 2.984 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8712) rss_mb | MB | 12 | 367.384 | 260.215 | 389.676 | 389.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8712) main thread run-queue wait | percent | 11 | 2.332 | 0.002 | 13.729 | 0.002 | 0.258559 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8712) vms_mb | MB | 12 | 9478.321 | 1656.520 | 10208.801 | 10208.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8734) rss_mb | MB | 1 | 196.480 | 196.480 | 196.480 | 196.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8734) vms_mb | MB | 1 | 1616.480 | 1616.480 | 1616.480 | 1616.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8760) CPU | percent | 12 | 22.401 | 1.989 | 75.382 | 7.956 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8760) rss_mb | MB | 13 | 368.331 | 230.137 | 394.324 | 394.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8760) main thread run-queue wait | percent | 12 | 2.280 | 0.003 | 18.907 | 0.016 | 0.276165 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8760) vms_mb | MB | 13 | 8899.218 | 1632.801 | 10216.996 | 10216.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8779) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8779) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8780) rss_mb | MB | 1 | 8.934 | 8.934 | 8.934 | 8.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8780) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8783) CPU | percent | 1 | 54.461 | 54.461 | 54.461 | 54.461 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8783) rss_mb | MB | 2 | 235.887 | 193.453 | 278.320 | 278.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8783) main thread run-queue wait | percent | 1 | 12.721 | 12.721 | 12.721 | 12.721 | 0.128466 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8783) vms_mb | MB | 2 | 1643.770 | 1614.223 | 1673.316 | 1673.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8793) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8793) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8794) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8794) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sleep (PID 8803) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8803) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8803) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8803) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 8803) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8803) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8811) CPU | percent | 24 | 12.207 | 0.993 | 72.518 | 0.994 | 2.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8811) rss_mb | MB | 25 | 379.641 | 236.090 | 394.020 | 393.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8811) main thread run-queue wait | percent | 24 | 2.039 | 0.002 | 23.771 | 0.006 | 0.492944 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8811) vms_mb | MB | 25 | 9525.863 | 1636.770 | 10211.680 | 10210.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8832) CPU | percent | 1 | 63.519 | 63.519 | 63.519 | 63.519 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8832) rss_mb | MB | 2 | 205.992 | 155.758 | 256.227 | 256.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8832) main thread run-queue wait | percent | 1 | 19.393 | 19.393 | 19.393 | 19.393 | 0.195400 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8832) vms_mb | MB | 2 | 1481.668 | 1311.754 | 1651.582 | 1651.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8855) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8855) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 8856) rss_mb | MB | 1 | 15.977 | 15.977 | 15.977 | 15.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 8856) vms_mb | MB | 1 | 20.602 | 20.602 | 20.602 | 20.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 8857) rss_mb | MB | 1 | 2.879 | 2.879 | 2.879 | 2.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 8857) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 8858) rss_mb | MB | 1 | 11.008 | 11.008 | 11.008 | 11.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 8858) vms_mb | MB | 1 | 14.883 | 14.883 | 14.883 | 14.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 8859) rss_mb | MB | 1 | 50.746 | 50.746 | 50.746 | 50.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 8859) vms_mb | MB | 1 | 59.133 | 59.133 | 59.133 | 59.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8877) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8877) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 8878) rss_mb | MB | 1 | 9.500 | 9.500 | 9.500 | 9.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 8878) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8906) CPU | percent | 5 | 33.004 | 3.973 | 70.357 | 3.973 | 1.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8906) rss_mb | MB | 6 | 354.439 | 295.035 | 381.504 | 381.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8906) main thread run-queue wait | percent | 5 | 0.954 | 0.194 | 1.795 | 1.795 | 0.048077 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8906) vms_mb | MB | 6 | 8761.980 | 1689.480 | 10195.184 | 10195.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8938) rss_mb | MB | 1 | 188.793 | 188.793 | 188.793 | 188.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8938) vms_mb | MB | 1 | 1594.223 | 1594.223 | 1594.223 | 1594.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8955) CPU | percent | 11 | 19.433 | 0.994 | 71.570 | 0.994 | 2.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8955) rss_mb | MB | 12 | 370.790 | 294.852 | 388.887 | 388.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8955) main thread run-queue wait | percent | 11 | 3.361 | 0.004 | 17.305 | 0.006 | 0.387075 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8955) vms_mb | MB | 12 | 9482.090 | 1689.762 | 10209.039 | 10209.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8974) CPU | percent | 1 | 57.656 | 57.656 | 57.656 | 57.656 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8974) rss_mb | MB | 2 | 226.246 | 182.582 | 269.910 | 269.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8974) main thread run-queue wait | percent | 1 | 15.687 | 15.687 | 15.687 | 15.687 | 0.157806 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 8974) vms_mb | MB | 2 | 1629.029 | 1592.973 | 1665.086 | 1665.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8986) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 8986) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8987) rss_mb | MB | 1 | 8.977 | 8.977 | 8.977 | 8.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 8987) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9002) CPU | percent | 13 | 22.527 | 0.994 | 90.301 | 1.989 | 2.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9002) rss_mb | MB | 14 | 361.335 | 158.238 | 391.906 | 391.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9002) main thread run-queue wait | percent | 13 | 2.756 | 0.004 | 24.230 | 0.006 | 0.362063 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9002) vms_mb | MB | 14 | 8963.227 | 1315.172 | 10208.156 | 10208.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9024) CPU | percent | 1 | 55.528 | 55.528 | 55.528 | 55.528 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9024) rss_mb | MB | 2 | 209.660 | 166.566 | 252.754 | 252.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9024) main thread run-queue wait | percent | 1 | 25.739 | 25.739 | 25.739 | 25.739 | 0.259578 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9024) vms_mb | MB | 2 | 1613.410 | 1577.973 | 1648.848 | 1648.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9031) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9031) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9032) rss_mb | MB | 1 | 9.898 | 9.898 | 9.898 | 9.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9032) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sleep (PID 9046) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9046) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9046) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9046) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9046) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9046) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9053) CPU | percent | 13 | 25.032 | 1.985 | 94.375 | 4.971 | 3.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9053) rss_mb | MB | 14 | 351.869 | 94.871 | 387.469 | 387.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9053) main thread run-queue wait | percent | 13 | 1.215 | 0.004 | 7.342 | 0.021 | 0.159256 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9053) vms_mb | MB | 14 | 8959.030 | 1283.598 | 10211.402 | 10211.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9077) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9077) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9078) rss_mb | MB | 1 | 10.703 | 10.703 | 10.703 | 10.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9078) vms_mb | MB | 1 | 14.730 | 14.730 | 14.730 | 14.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9084) rss_mb | MB | 1 | 296.762 | 296.762 | 296.762 | 296.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9084) vms_mb | MB | 1 | 1691.566 | 1691.566 | 1691.566 | 1691.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9098) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9098) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9099) rss_mb | MB | 1 | 9.387 | 9.387 | 9.387 | 9.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9099) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9103) CPU | percent | 7 | 40.287 | 3.978 | 81.267 | 12.927 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9103) rss_mb | MB | 8 | 342.596 | 175.641 | 390.887 | 390.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9103) main thread run-queue wait | percent | 7 | 5.036 | 0.005 | 22.987 | 0.051 | 0.355105 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9103) vms_mb | MB | 8 | 8061.425 | 1590.219 | 10210.332 | 10210.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9124) CPU | percent | 1 | 66.504 | 66.504 | 66.504 | 66.504 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9124) rss_mb | MB | 2 | 241.393 | 193.992 | 288.793 | 288.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9124) main thread run-queue wait | percent | 1 | 18.668 | 18.668 | 18.668 | 18.668 | 0.188076 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9124) vms_mb | MB | 2 | 1648.764 | 1614.473 | 1683.055 | 1683.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9145) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9145) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9146) rss_mb | MB | 1 | 9.270 | 9.270 | 9.270 | 9.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9146) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9150) CPU | percent | 12 | 25.080 | 0.994 | 87.242 | 6.961 | 3.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9150) rss_mb | MB | 13 | 359.852 | 169.500 | 390.344 | 390.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9150) main thread run-queue wait | percent | 12 | 3.269 | 0.001 | 19.767 | 0.019 | 0.395355 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9150) vms_mb | MB | 13 | 8887.257 | 1578.719 | 10211.750 | 10211.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9169) CPU | percent | 1 | 67.502 | 67.502 | 67.502 | 67.502 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9169) rss_mb | MB | 2 | 236.963 | 187.934 | 285.992 | 285.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9169) main thread run-queue wait | percent | 1 | 21.540 | 21.540 | 21.540 | 21.540 | 0.216984 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9169) vms_mb | MB | 2 | 1637.416 | 1593.973 | 1680.859 | 1680.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9197) CPU | percent | 28 | 12.116 | 0.994 | 79.222 | 6.962 | 3.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9197) rss_mb | MB | 29 | 382.780 | 230.316 | 396.242 | 395.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9197) main thread run-queue wait | percent | 28 | 1.833 | 0.001 | 35.421 | 0.012 | 0.519277 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9197) vms_mb | MB | 29 | 9621.754 | 1633.305 | 10214.238 | 10213.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9217) CPU | percent | 1 | 58.483 | 58.483 | 58.483 | 58.483 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9217) rss_mb | MB | 2 | 257.689 | 218.656 | 296.723 | 296.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9217) main thread run-queue wait | percent | 1 | 27.307 | 27.307 | 27.307 | 27.307 | 0.275486 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9217) vms_mb | MB | 2 | 1665.611 | 1623.984 | 1707.238 | 1707.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 9234) rss_mb | MB | 1 | 2.242 | 2.242 | 2.242 | 2.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 9234) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9240) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9240) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 9241) rss_mb | MB | 1 | 18.422 | 18.422 | 18.422 | 18.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 9241) vms_mb | MB | 1 | 24.234 | 24.234 | 24.234 | 24.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 9242) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 9242) rss_mb | MB | 10 | 2.555 | 2.555 | 2.555 | 2.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 9242) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 9242) vms_mb | MB | 10 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 9243) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 9243) rss_mb | MB | 10 | 11.172 | 11.172 | 11.172 | 11.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 9243) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 9243) vms_mb | MB | 10 | 14.941 | 14.941 | 14.941 | 14.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9244) CPU | percent | 2 | 13.878 | 0.000 | 27.756 | 0.000 | 0.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9244) rss_mb | MB | 3 | 60.279 | 48.086 | 66.375 | 66.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9244) main thread run-queue wait | percent | 2 | 0.377 | 0.000 | 0.755 | 0.000 | 0.007612 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9244) vms_mb | MB | 3 | 72.197 | 56.293 | 80.148 | 80.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9321) CPU | percent | 3 | 25.398 | 0.000 | 67.278 | 8.916 | 0.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9321) rss_mb | MB | 4 | 56.413 | 26.000 | 66.902 | 66.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9321) main thread run-queue wait | percent | 3 | 0.304 | 0.000 | 0.554 | 0.554 | 0.009205 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9321) vms_mb | MB | 4 | 68.386 | 31.844 | 81.410 | 81.410 | n/a | n/a |
| sleep (PID 9323) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9323) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9323) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9323) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9323) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9323) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9324) CPU | percent | 2 | 9.438 | 0.000 | 18.876 | 0.000 | 0.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9324) rss_mb | MB | 3 | 63.277 | 57.871 | 65.980 | 65.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9324) main thread run-queue wait | percent | 2 | 0.197 | 0.000 | 0.395 | 0.000 | 0.003975 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp_client.py (PID 9324) vms_mb | MB | 3 | 78.415 | 72.895 | 81.176 | 81.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9336) CPU | percent | 28 | 10.382 | 0.993 | 78.491 | 2.984 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9336) rss_mb | MB | 29 | 380.562 | 252.195 | 392.051 | 392.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9336) main thread run-queue wait | percent | 28 | 1.275 | 0.003 | 16.287 | 0.004 | 0.360148 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9336) vms_mb | MB | 29 | 9625.181 | 1648.504 | 10210.203 | 10210.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9359) CPU | percent | 1 | 76.430 | 76.430 | 76.430 | 76.430 | 0.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9359) rss_mb | MB | 2 | 241.766 | 180.477 | 303.055 | 303.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9359) main thread run-queue wait | percent | 1 | 15.512 | 15.512 | 15.512 | 15.512 | 0.156280 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9359) vms_mb | MB | 2 | 1659.477 | 1591.223 | 1727.730 | 1727.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9398) CPU | percent | 10 | 22.239 | 0.993 | 72.408 | 8.951 | 2.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9398) rss_mb | MB | 11 | 370.781 | 274.277 | 394.887 | 394.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9398) main thread run-queue wait | percent | 10 | 4.274 | 0.003 | 20.760 | 0.018 | 0.430196 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9398) vms_mb | MB | 11 | 9416.539 | 1669.270 | 10212.219 | 10212.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9417) CPU | percent | 1 | 59.605 | 59.605 | 59.605 | 59.605 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9417) rss_mb | MB | 2 | 215.963 | 170.289 | 261.637 | 261.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9417) main thread run-queue wait | percent | 1 | 17.987 | 17.987 | 17.987 | 17.987 | 0.181065 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9417) vms_mb | MB | 2 | 1619.059 | 1579.473 | 1658.645 | 1658.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9445) CPU | percent | 6 | 36.881 | 3.976 | 72.547 | 4.972 | 2.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9445) rss_mb | MB | 7 | 345.690 | 229.223 | 383.664 | 383.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9445) main thread run-queue wait | percent | 6 | 7.622 | 0.006 | 24.368 | 0.006 | 0.462209 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9445) vms_mb | MB | 7 | 7763.118 | 1632.289 | 10203.832 | 10203.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9464) CPU | percent | 1 | 57.600 | 57.600 | 57.600 | 57.600 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9464) rss_mb | MB | 2 | 206.346 | 157.945 | 254.746 | 254.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9464) main thread run-queue wait | percent | 1 | 16.258 | 16.258 | 16.258 | 16.258 | 0.163708 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9464) vms_mb | MB | 2 | 1482.652 | 1314.680 | 1650.625 | 1650.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9476) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9476) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9477) rss_mb | MB | 1 | 8.480 | 8.480 | 8.480 | 8.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9477) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9492) CPU | percent | 8 | 26.529 | 1.989 | 74.403 | 3.975 | 2.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9492) rss_mb | MB | 9 | 361.295 | 264.293 | 390.621 | 390.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9492) main thread run-queue wait | percent | 8 | 2.234 | 0.008 | 13.946 | 0.009 | 0.180376 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9492) vms_mb | MB | 9 | 9241.466 | 1659.734 | 10210.516 | 10210.516 | n/a | n/a |
| sleep (PID 9510) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9510) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9510) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9510) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9510) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9510) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9522) rss_mb | MB | 1 | 158.176 | 158.176 | 158.176 | 158.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9522) vms_mb | MB | 1 | 1499.969 | 1499.969 | 1499.969 | 1499.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9541) CPU | percent | 13 | 22.745 | 0.994 | 90.201 | 1.989 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9541) rss_mb | MB | 14 | 358.412 | 147.656 | 390.137 | 390.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9541) main thread run-queue wait | percent | 13 | 3.351 | 0.003 | 21.139 | 0.005 | 0.439220 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9541) vms_mb | MB | 14 | 8956.259 | 1303.309 | 10209.000 | 10209.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9560) CPU | percent | 1 | 63.433 | 63.433 | 63.433 | 63.433 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9560) rss_mb | MB | 2 | 239.445 | 193.637 | 285.254 | 285.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9560) main thread run-queue wait | percent | 1 | 19.904 | 19.904 | 19.904 | 19.904 | 0.200817 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9560) vms_mb | MB | 2 | 1647.646 | 1614.473 | 1680.820 | 1680.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9589) CPU | percent | 11 | 25.719 | 0.995 | 84.282 | 0.995 | 2.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9589) rss_mb | MB | 12 | 352.680 | 160.172 | 388.234 | 388.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9589) main thread run-queue wait | percent | 11 | 3.579 | 0.002 | 27.569 | 0.005 | 0.397279 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9589) vms_mb | MB | 12 | 8769.463 | 1499.965 | 10209.359 | 10209.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9611) CPU | percent | 1 | 51.516 | 51.516 | 51.516 | 51.516 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9611) rss_mb | MB | 2 | 184.521 | 140.105 | 228.938 | 228.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9611) main thread run-queue wait | percent | 1 | 24.606 | 24.606 | 24.606 | 24.606 | 0.248371 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9611) vms_mb | MB | 2 | 1466.100 | 1296.352 | 1635.848 | 1635.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9618) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9618) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9619) rss_mb | MB | 1 | 9.094 | 9.094 | 9.094 | 9.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9619) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9637) CPU | percent | 10 | 25.921 | 1.988 | 74.560 | 4.971 | 2.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9637) rss_mb | MB | 11 | 362.913 | 241.195 | 388.344 | 388.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9637) main thread run-queue wait | percent | 10 | 4.729 | 0.003 | 26.307 | 0.014 | 0.476593 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9637) vms_mb | MB | 11 | 8656.632 | 1640.293 | 10212.746 | 10212.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9654) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9654) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9655) rss_mb | MB | 1 | 8.895 | 8.895 | 8.895 | 8.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9655) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9656) CPU | percent | 2 | 56.555 | 51.609 | 61.500 | 51.609 | 1.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9656) rss_mb | MB | 3 | 191.141 | 48.012 | 296.152 | 296.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9656) main thread run-queue wait | percent | 2 | 21.662 | 18.528 | 24.796 | 24.796 | 0.436624 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9656) vms_mb | MB | 3 | 1520.533 | 1238.609 | 1690.992 | 1690.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9684) CPU | percent | 13 | 20.566 | 0.994 | 83.451 | 0.994 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9684) rss_mb | MB | 14 | 367.966 | 179.316 | 397.344 | 397.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9684) main thread run-queue wait | percent | 13 | 1.671 | 0.000 | 13.501 | 0.004 | 0.218625 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9684) vms_mb | MB | 14 | 8979.427 | 1590.969 | 10205.180 | 10205.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9705) CPU | percent | 1 | 55.622 | 55.622 | 55.622 | 55.622 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9705) rss_mb | MB | 2 | 198.656 | 160.477 | 236.836 | 236.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9705) main thread run-queue wait | percent | 1 | 16.484 | 16.484 | 16.484 | 16.484 | 0.165962 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9705) vms_mb | MB | 2 | 1477.350 | 1317.340 | 1637.359 | 1637.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9712) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9712) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9713) rss_mb | MB | 1 | 7.430 | 7.430 | 7.430 | 7.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9713) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sleep (PID 9730) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9730) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9730) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9730) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9730) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9730) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9733) CPU | percent | 11 | 17.327 | 1.976 | 70.460 | 7.857 | 1.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9733) rss_mb | MB | 12 | 375.124 | 294.188 | 396.184 | 396.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9733) main thread run-queue wait | percent | 11 | 0.599 | 0.006 | 3.398 | 0.025 | 0.066394 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9733) vms_mb | MB | 12 | 9477.711 | 1689.242 | 10195.445 | 10195.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9763) rss_mb | MB | 1 | 193.836 | 193.836 | 193.836 | 193.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9763) vms_mb | MB | 1 | 1614.223 | 1614.223 | 1614.223 | 1614.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 9775) rss_mb | MB | 1 | 1.969 | 1.969 | 1.969 | 1.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 9775) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 9776) rss_mb | MB | 1 | 1.535 | 1.535 | 1.535 | 1.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 9776) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9782) CPU | percent | 13 | 24.107 | 0.994 | 73.398 | 10.928 | 3.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9782) rss_mb | MB | 14 | 365.616 | 217.375 | 392.180 | 392.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9782) main thread run-queue wait | percent | 13 | 3.912 | 0.004 | 24.531 | 0.016 | 0.513023 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9782) vms_mb | MB | 14 | 8984.413 | 1623.535 | 10208.688 | 10208.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 9795) rss_mb | MB | 1 | 16.520 | 16.520 | 16.520 | 16.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 9795) vms_mb | MB | 1 | 706.961 | 706.961 | 706.961 | 706.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9801) CPU | percent | 1 | 56.474 | 56.474 | 56.474 | 56.474 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9801) rss_mb | MB | 2 | 228.355 | 193.570 | 263.141 | 263.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9801) main thread run-queue wait | percent | 1 | 23.827 | 23.827 | 23.827 | 23.827 | 0.240492 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9801) vms_mb | MB | 2 | 1636.506 | 1614.473 | 1658.539 | 1658.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9829) CPU | percent | 7 | 43.185 | 6.956 | 82.294 | 6.956 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9829) rss_mb | MB | 8 | 348.041 | 229.605 | 389.289 | 389.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9829) main thread run-queue wait | percent | 7 | 6.103 | 0.007 | 19.299 | 0.007 | 0.430960 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9829) vms_mb | MB | 8 | 8062.834 | 1632.520 | 10206.859 | 10206.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9852) CPU | percent | 1 | 53.480 | 53.480 | 53.480 | 53.480 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9852) rss_mb | MB | 2 | 195.477 | 160.984 | 229.969 | 229.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9852) main thread run-queue wait | percent | 1 | 16.397 | 16.397 | 16.397 | 16.397 | 0.165563 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9852) vms_mb | MB | 2 | 1474.842 | 1317.723 | 1631.961 | 1631.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9859) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 9859) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9860) rss_mb | MB | 1 | 8.922 | 8.922 | 8.922 | 8.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 9860) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9878) CPU | percent | 13 | 21.140 | 0.994 | 74.398 | 1.989 | 2.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9878) rss_mb | MB | 14 | 364.251 | 229.148 | 388.078 | 388.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9878) main thread run-queue wait | percent | 13 | 2.951 | 0.003 | 23.866 | 0.007 | 0.386787 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9878) vms_mb | MB | 14 | 8982.235 | 1632.023 | 10206.293 | 10206.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — env (PID 9891) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — env (PID 9891) vms_mb | MB | 1 | 0.418 | 0.418 | 0.418 | 0.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9897) CPU | percent | 1 | 61.478 | 61.478 | 61.478 | 61.478 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9897) rss_mb | MB | 2 | 250.682 | 206.207 | 295.156 | 295.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9897) main thread run-queue wait | percent | 1 | 23.955 | 23.955 | 23.955 | 23.955 | 0.241584 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9897) vms_mb | MB | 2 | 1654.516 | 1619.223 | 1689.809 | 1689.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9928) CPU | percent | 10 | 29.194 | 0.995 | 91.263 | 0.995 | 2.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9928) rss_mb | MB | 11 | 336.314 | 35.707 | 388.484 | 388.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9928) main thread run-queue wait | percent | 10 | 2.523 | 0.003 | 15.868 | 0.007 | 0.254091 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9928) vms_mb | MB | 11 | 8596.117 | 1169.414 | 10205.586 | 10205.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9957) rss_mb | MB | 1 | 167.621 | 167.621 | 167.621 | 167.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9957) vms_mb | MB | 1 | 1578.473 | 1578.473 | 1578.473 | 1578.473 | n/a | n/a |
| sleep (PID 9972) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9972) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9972) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9972) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9972) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9972) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9978) CPU | percent | 19 | 13.342 | 0.993 | 72.404 | 1.987 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9978) rss_mb | MB | 20 | 371.337 | 185.379 | 392.082 | 391.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9978) main thread run-queue wait | percent | 19 | 0.718 | 0.000 | 5.688 | 0.020 | 0.140447 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 9978) vms_mb | MB | 20 | 9352.260 | 1593.469 | 10210.926 | 10210.570 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 CPU | percent | 2889 | 89.588 | 0.000 | 215.658 | 0.000 | 2610.996289 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2889 | 2.850 | 0.000 | 50.364 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2889 | 4.420 | 0.000 | 70.008 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io_psi_full_pct | percent of wall time stalled | 2889 | 0.050 | 0.000 | 0.534 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io_psi_some_pct | percent of wall time stalled | 2889 | 0.063 | 0.000 | 0.684 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io read MB/s | MB/s | 2889 | 0.002 | 0.000 | 1.358 | 0.000 | 4.734375 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io write MB/s | MB/s | 2889 | 0.124 | 0.000 | 10.877 | 0.000 | 360.855469 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory | MB | 2890 | 439.208 | 14.141 | 2440.633 | 159.004 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2889 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2889 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 net rx MB/s | MB/s | 2889 | 0.098 | 0.000 | 2.168 | 0.000 | 285.327623 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 net tx MB/s | MB/s | 2889 | 0.001 | 0.000 | 0.015 | 0.000 | 4.027377 MB | n/a |
| workload total CPU | percent | 2916 | 6.470 | 1.398 | 103.001 | 1.572 | 190.669962 CPU seconds | n/a |
| workload total memory | MB | 2917 | 9201.595 | 8285.957 | 9674.785 | 9666.840 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
