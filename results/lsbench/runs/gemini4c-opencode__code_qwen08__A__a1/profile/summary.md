# agprof summary

- Duration: **13651.495 s**
- Runs: **0/1 completed**, 0 succeeded, 0 failed, 1 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **121 calls**, 121 succeeded, 0 failed, 0 interrupted, n/a reported retries, 12207.977 s total wait
- Tools: **179/179 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **1349750** at 1.974 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | n/a / n/a ms |
| LLM latency p50 / p95 | 71151.273 / 268336.896 ms |
| LLM TTFT p50 / p95 | 44071.222 / 264743.793 ms |
| LLM input / output tokens | 10246515 / 136620 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 121 total, 121 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- opencode: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 100/100 | 100 | 0 | 0 | n/a | n/a |
| edit | 11/11 | 11 | 0 | 0 | n/a | n/a |
| read | 38/38 | 38 | 0 | 0 | n/a | n/a |
| todowrite | 4/4 | 4 | 0 | 0 | n/a | n/a |
| write | 26/26 | 26 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 3.608% | 164.168% | 493.324 s | 8921.623 MB | 9542.672 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker | 2003 |  | 1 | n/a% | n/a% | n/a s | 29.926 MB | 29.926 MB | 1843.520 MB | 1843.520 MB | n/a MB | n/a MB |
| lsb_grid_worker | 1843 |  | 13576 | 0.000% | 0.000% | 0.000 s | 3.363 MB | 3.363 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 1852 |  | 13576 | 1.345% | 163.464% | 183.900 s | 2911.261 MB | 3468.078 MB | 15733.619 MB | 17825.988 MB | 169.250000 MB | 1352.519531 MB |
| docker-buildx | 2012 |  | 1 | n/a% | n/a% | n/a s | 41.828 MB | 41.828 MB | 1298.477 MB | 1298.477 MB | n/a MB | n/a MB |
| python | 1891 |  | 13576 | 0.000% | 0.000% | 0.000 s | 12.285 MB | 12.285 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 1857 |  | 13576 | 0.156% | 7.910% | 21.350 s | 1768.331 MB | 1769.066 MB | 11010.363 MB | 11024.168 MB | 0.007812 MB | 0.117188 MB |
| python | 1995 |  | 13576 | 0.030% | 4.975% | 4.100 s | 44.971 MB | 45.570 MB | 131.199 MB | 131.719 MB | 0.007812 MB | 0.402344 MB |
| VLLM::EngineCor | 1892 |  | 13576 | 2.075% | 61.514% | 283.680 s | 2313.235 MB | 2313.719 MB | 21204.001 MB | 21204.289 MB | 0.003906 MB | 0.085938 MB |
| python3 | 2242 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 58.318% | 64.961% | 1.180 s | 46.454 MB | 76.793 MB | 57.158 MB | 92.770 MB | n/a MB | n/a MB |
| tail | 2146 | sandbox_agent_lsb-opencode_0000_0000 | 13575 | 0.003% | 1.989% | 0.360 s | 1.391 MB | 1.391 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| docker-init | 2110 | sandbox_agent_lsb-opencode_0000_0000 | 13575 | 0.002% | 0.996% | 0.300 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 2236 | sandbox_agent_lsb-opencode_0000_0000 | 13575 | 31.279% | 101.285% | 4269.480 s | 110.781 MB | 139.637 MB | 973.285 MB | 975.660 MB | n/a MB | n/a MB |
| opencode | 2250 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.000 MB | 14.000 MB | 6358.133 MB | 6358.133 MB | n/a MB | n/a MB |
| opencode | 2264 | sandbox_agent_lsb-opencode_0000_0000 | 13559 | 2.943% | 128.299% | 401.250 s | 715.815 MB | 986.297 MB | 15720.058 MB | 16739.410 MB | n/a MB | n/a MB |
| python3 | 2764 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.906 MB | 20.906 MB | 26.738 MB | 26.738 MB | n/a MB | n/a MB |
| python3 | 2882 | sandbox_agent_lsb-opencode_0000_0000 | 16 | 172.981% | 177.053% | 26.130 s | 132.703 MB | 179.066 MB | 1980.767 MB | 2007.273 MB | n/a MB | n/a MB |
| python3 | 2962 | sandbox_agent_lsb-opencode_0000_0000 | 22 | 0.236% | 4.962% | 0.050 s | 21.593 MB | 21.852 MB | 27.592 MB | 27.875 MB | n/a MB | n/a MB |
| python3 | 3042 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.168 MB | 7.168 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 3022 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 2.978% | 2.978% | 0.030 s | 12.230 MB | 12.230 MB | 15.977 MB | 15.977 MB | n/a MB | n/a MB |
| python3 | 3076 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| python3 | 3101 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 1.985% | 1.985% | 0.020 s | 12.270 MB | 12.270 MB | 15.945 MB | 15.945 MB | n/a MB | n/a MB |
| python3 | 3107 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.512 MB | 7.512 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 3138 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 3182 | sandbox_agent_lsb-opencode_0000_0000 | 41 | 0.050% | 1.982% | 0.020 s | 21.827 MB | 21.949 MB | 26.967 MB | 27.227 MB | n/a MB | n/a MB |
| python3 | 3234 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.949 MB | 21.949 MB | 27.227 MB | 27.227 MB | n/a MB | n/a MB |
| python3 | 3277 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 2.484% | 2.983% | 0.050 s | 12.339 MB | 12.422 MB | 16.164 MB | 16.207 MB | n/a MB | n/a MB |
| python3 | 3300 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.820 MB | 7.820 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 3330 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.938 MB | 5.938 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 3363 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.602 MB | 7.602 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 3447 | sandbox_agent_lsb-opencode_0000_0000 | 20 | 0.209% | 2.976% | 0.040 s | 21.951 MB | 22.176 MB | 27.978 MB | 28.129 MB | n/a MB | n/a MB |
| python3 | 3487 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| python3 | 3523 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.332 MB | 7.332 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 3576 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 3567 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 2.484% | 2.982% | 0.050 s | 12.612 MB | 12.742 MB | 17.112 MB | 17.156 MB | n/a MB | n/a MB |
| python3 | 3614 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.633 MB | 6.633 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 3664 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 3703 | sandbox_agent_lsb-opencode_0000_0000 | 49 | 0.207% | 4.965% | 0.100 s | 21.864 MB | 22.207 MB | 27.905 MB | 28.188 MB | n/a MB | n/a MB |
| bash | 3702 | sandbox_agent_lsb-opencode_0000_0000 | 54 | 0.299% | 3.964% | 0.160 s | 3.569 MB | 13.070 MB | 5.080 MB | 17.363 MB | n/a MB | n/a MB |
| python3 | 3726 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.012 MB | 6.012 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 3761 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.797 MB | 7.797 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 3796 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.465 MB | 8.465 MB | 13.145 MB | 13.145 MB | n/a MB | n/a MB |
| python3 | 3855 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.602 MB | 7.602 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 3892 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.070 MB | 9.070 MB | 13.270 MB | 13.270 MB | n/a MB | n/a MB |
| python3 | 3928 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.469 MB | 7.469 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 3964 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.934 MB | 7.934 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 4027 | sandbox_agent_lsb-opencode_0000_0000 | 10 | 2.976% | 3.969% | 0.270 s | 13.054 MB | 13.223 MB | 17.342 MB | 17.449 MB | n/a MB | n/a MB |
| python3 | 4055 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.469 MB | 7.469 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 4091 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.777 MB | 7.777 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 4127 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.805 MB | 12.805 MB | 17.141 MB | 17.141 MB | n/a MB | n/a MB |
| python3 | 4164 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.078 MB | 13.078 MB | 17.422 MB | 17.422 MB | n/a MB | n/a MB |
| python3 | 4200 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.469 MB | 8.469 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 4239 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.410 MB | 6.410 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 4276 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.805 MB | 7.805 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 4312 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.277 MB | 8.277 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 4348 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.473 MB | 8.473 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 4385 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.914 MB | 6.914 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 4495 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.906 MB | 4.906 MB | 11.383 MB | 11.383 MB | n/a MB | n/a MB |
| python3 | 4509 | sandbox_agent_lsb-opencode_0000_0000 | 36 | 0.511% | 3.969% | 0.180 s | 22.268 MB | 22.371 MB | 28.083 MB | 28.230 MB | n/a MB | n/a MB |
| python3 | 4526 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.121 MB | 7.121 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 4562 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.242 MB | 7.242 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 4623 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.793 MB | 8.793 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 4661 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.207 MB | 7.207 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 4715 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.750 MB | 4.750 MB | 11.383 MB | 11.383 MB | n/a MB | n/a MB |
| python3 | 4751 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.473 MB | 7.473 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 4808 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.211 MB | 6.211 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 4791 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 2.649% | 2.983% | 0.080 s | 12.465 MB | 12.496 MB | 15.965 MB | 15.965 MB | n/a MB | n/a MB |
| python3 | 4844 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.930 MB | 6.930 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 4880 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.711 MB | 7.711 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 4932 | sandbox_agent_lsb-opencode_0000_0000 | 24 | 1.122% | 8.936% | 0.260 s | 22.053 MB | 22.633 MB | 28.059 MB | 28.508 MB | n/a MB | n/a MB |
| python3 | 4971 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.219 MB | 8.219 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5008 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.480 MB | 8.480 MB | 13.086 MB | 13.086 MB | n/a MB | n/a MB |
| python3 | 5059 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.305 MB | 7.305 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5071 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.371 MB | 9.371 MB | 13.250 MB | 13.250 MB | n/a MB | n/a MB |
| python3 | 5082 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.078 MB | 1.078 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| python3 | 5126 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 1.984% | 1.984% | 0.020 s | 12.387 MB | 12.387 MB | 15.859 MB | 15.859 MB | n/a MB | n/a MB |
| python3 | 5144 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.652 MB | 8.652 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5181 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.117 MB | 7.117 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5242 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.672 MB | 7.672 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5232 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 3.453% | 3.928% | 0.070 s | 13.242 MB | 13.367 MB | 17.219 MB | 17.254 MB | n/a MB | n/a MB |
| python3 | 5279 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.492 MB | 7.492 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5317 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.039 MB | 7.039 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 5356 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.152 MB | 8.152 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5340 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 2.977% | 2.978% | 0.060 s | 13.060 MB | 13.102 MB | 17.125 MB | 17.137 MB | n/a MB | n/a MB |
| bash | 5339 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.746 MB | 2.746 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5392 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.680 MB | 8.680 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5429 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.734 MB | 7.734 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 5446 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.582 MB | 9.582 MB | 13.590 MB | 13.590 MB | n/a MB | n/a MB |
| python3 | 5513 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.188 MB | 10.188 MB | 14.730 MB | 14.730 MB | n/a MB | n/a MB |
| python3 | 5593 | sandbox_agent_lsb-opencode_0000_0000 | 25 | 0.207% | 2.978% | 0.050 s | 22.035 MB | 22.035 MB | 28.195 MB | 28.195 MB | n/a MB | n/a MB |
| python3 | 5635 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| python3 | 5669 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.970% | 100.433% | 2.010 s | 8.266 MB | 8.266 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5671 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.943% | 100.449% | 2.010 s | 8.301 MB | 8.301 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5730 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.543 MB | 18.543 MB | 24.047 MB | 24.047 MB | n/a MB | n/a MB |
| python3 | 5802 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.566 MB | 8.566 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5775 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.494% | 0.995% | 0.020 s | 12.836 MB | 12.836 MB | 16.930 MB | 16.930 MB | n/a MB | n/a MB |
| bash | 5774 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.816 MB | 2.816 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5813 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.814% | 100.379% | 2.010 s | 8.230 MB | 8.230 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 5852 | sandbox_agent_lsb-opencode_0000_0000 | 33 | 0.062% | 1.980% | 0.020 s | 21.821 MB | 21.887 MB | 26.922 MB | 27.051 MB | n/a MB | n/a MB |
| python3 | 5889 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| python3 | 5954 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.248% | 0.993% | 0.010 s | 22.375 MB | 22.375 MB | 28.077 MB | 28.184 MB | n/a MB | n/a MB |
| python3 | 5971 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.348 MB | 7.348 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| bash | 5970 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.918 MB | 2.918 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 6013 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| python3 | 6043 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 4.790% | 43.573% | 0.580 s | 168.040 MB | 1782.984 MB | 510.280 MB | 3907.703 MB | n/a MB | n/a MB |
| python3 | 6092 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.355 MB | 7.355 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| bash | 6090 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.559 MB | 2.559 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 6105 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 164.716% | 173.543% | 8.290 s | 1369.230 MB | 1785.176 MB | 2813.268 MB | 3021.996 MB | n/a MB | n/a MB |
| python3 | 6147 | sandbox_agent_lsb-opencode_0000_0000 | 12 | 168.211% | 176.049% | 18.680 s | 2167.268 MB | 3155.895 MB | 4082.190 MB | 5678.398 MB | n/a MB | n/a MB |
| python3 | 6206 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 6.447% | 38.685% | 0.390 s | 31.919 MB | 35.008 MB | 198.781 MB | 228.809 MB | n/a MB | n/a MB |
| python3 | 6236 | sandbox_agent_lsb-opencode_0000_0000 | 10 | 171.993% | 174.757% | 15.590 s | 1686.938 MB | 2515.035 MB | 3071.641 MB | 3889.160 MB | n/a MB | n/a MB |
| python3 | 6278 | sandbox_agent_lsb-opencode_0000_0000 | 11 | 173.758% | 177.424% | 17.520 s | 1713.594 MB | 1807.516 MB | 3912.571 MB | 4688.941 MB | n/a MB | n/a MB |
| bash | 6277 | sandbox_agent_lsb-opencode_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.891 MB | 2.891 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 6310 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.719 MB | 2.719 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 6311 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.629 MB | 20.629 MB | 212.207 MB | 212.207 MB | n/a MB | n/a MB |
| python3 | 6362 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 175.963% | 175.963% | 1.790 s | 76.900 MB | 93.191 MB | 1948.711 MB | 1951.195 MB | n/a MB | n/a MB |
| bash | 6361 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.000 MB | 3.000 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 6384 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.645 MB | 2.645 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 6385 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 173.320% | 174.011% | 8.720 s | 150.408 MB | 187.785 MB | 2061.370 MB | 2066.703 MB | n/a MB | n/a MB |
| python3 | 6523 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 1.390% | 2.979% | 0.070 s | 12.466 MB | 12.508 MB | 15.903 MB | 15.906 MB | n/a MB | n/a MB |
| bash | 6522 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.727 MB | 2.727 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 6553 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.535 MB | 8.535 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 6590 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 6626 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.566 MB | 8.566 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 6637 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.921% | 100.399% | 2.010 s | 8.285 MB | 8.285 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| bash | 6701 | sandbox_agent_lsb-opencode_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 6702 | sandbox_agent_lsb-opencode_0000_0000 | 8 | 1.703% | 2.984% | 0.120 s | 12.336 MB | 12.336 MB | 15.877 MB | 15.887 MB | n/a MB | n/a MB |
| python3 | 6742 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.016 MB | 8.016 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 6753 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 100.448% | 100.473% | 2.020 s | 8.406 MB | 8.406 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 6782 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 6818 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.789 MB | 5.789 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 6856 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.086 MB | 7.086 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 6958 | sandbox_agent_lsb-opencode_0000_0000 | 49 | 0.435% | 3.977% | 0.210 s | 22.363 MB | 22.363 MB | 28.182 MB | 28.238 MB | n/a MB | n/a MB |
| python3 | 6991 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.293 MB | 7.293 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7029 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.750 MB | 4.750 MB | 11.383 MB | 11.383 MB | n/a MB | n/a MB |
| python3 | 7065 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.047 MB | 7.047 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 7139 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.395 MB | 4.395 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 7154 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.857% | 100.367% | 2.010 s | 8.316 MB | 8.316 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7155 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 100.385% | 100.466% | 2.020 s | 8.348 MB | 8.348 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7179 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.672 MB | 7.672 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 7192 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.781% | 100.238% | 2.010 s | 86.108 MB | 132.566 MB | 97.875 MB | 149.250 MB | n/a MB | n/a MB |
| python3 | 7193 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.950% | 100.448% | 2.010 s | 81.238 MB | 122.988 MB | 89.686 MB | 134.125 MB | n/a MB | n/a MB |
| python3 | 7219 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.551 MB | 8.551 MB | 13.133 MB | 13.133 MB | n/a MB | n/a MB |
| python3 | 7222 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.982% | 100.456% | 2.010 s | 8.141 MB | 8.141 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7223 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.852% | 100.395% | 2.010 s | 8.363 MB | 8.363 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7224 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.898% | 100.323% | 2.010 s | 160.488 MB | 238.738 MB | 167.016 MB | 245.312 MB | n/a MB | n/a MB |
| python3 | 7225 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.907% | 100.356% | 2.010 s | 156.322 MB | 232.863 MB | 162.332 MB | 240.312 MB | n/a MB | n/a MB |
| python3 | 7245 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.923% | 100.420% | 2.010 s | 8.227 MB | 8.227 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| bash | 7265 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 7273 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.340 MB | 7.340 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 7266 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 2.645% | 2.976% | 0.080 s | 13.016 MB | 13.141 MB | 17.129 MB | 17.152 MB | n/a MB | n/a MB |
| python3 | 7306 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.547 MB | 7.547 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 7342 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.383 MB | 4.383 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 7380 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.922 MB | 5.922 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| bash | 7444 | sandbox_agent_lsb-opencode_0000_0000 | 73 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 7445 | sandbox_agent_lsb-opencode_0000_0000 | 73 | 2.067% | 12.909% | 1.500 s | 13.218 MB | 13.633 MB | 17.427 MB | 17.832 MB | n/a MB | n/a MB |
| python3 | 7513 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.484 MB | 7.484 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7543 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.766 MB | 9.766 MB | 14.578 MB | 14.578 MB | n/a MB | n/a MB |
| python3 | 7579 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.613 MB | 8.613 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7617 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.836 MB | 6.836 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 7654 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.875 MB | 8.875 MB | 13.129 MB | 13.129 MB | n/a MB | n/a MB |
| python3 | 7691 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.547 MB | 7.547 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7730 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.062 MB | 13.062 MB | 17.406 MB | 17.406 MB | n/a MB | n/a MB |
| python3 | 7767 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 7804 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.371 MB | 7.371 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7840 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.035 MB | 7.035 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 7878 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.285 MB | 7.285 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 7916 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.922 MB | 6.922 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 7953 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.441 MB | 8.441 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 7991 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.480 MB | 7.480 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 8027 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.668 MB | 4.668 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 8065 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.320 MB | 4.320 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 8102 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.047 MB | 7.047 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 8176 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.730 MB | 7.730 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python3 | 8250 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.414 MB | 5.414 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| python3 | 8287 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.414 MB | 4.414 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 8322 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.141 MB | 0.141 MB | 6.734 MB | 6.734 MB | n/a MB | n/a MB |
| python3 | 8360 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.184 MB | 13.184 MB | 17.410 MB | 17.410 MB | n/a MB | n/a MB |
| python3 | 8397 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.602 MB | 7.602 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 8435 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.609 MB | 7.609 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 8472 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.602 MB | 8.602 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 8503 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.277 MB | 9.277 MB | 13.250 MB | 13.250 MB | n/a MB | n/a MB |
| python3 | 8504 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.301 MB | 9.301 MB | 13.250 MB | 13.250 MB | n/a MB | n/a MB |
| python3 | 8537 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.285 MB | 7.285 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 8575 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.105 MB | 7.105 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 8611 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.051 MB | 8.051 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 8650 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 8688 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 8697 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.971% | 100.439% | 2.010 s | 8.238 MB | 8.238 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 8698 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.926% | 100.395% | 2.010 s | 8.301 MB | 8.301 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 8767 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.047 MB | 7.047 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 8805 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.039 MB | 8.039 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 8844 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 8882 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.391 MB | 7.391 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 8921 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.496 MB | 7.496 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 8958 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.602 MB | 5.602 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| python3 | 8996 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.094 MB | 7.094 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python3 | 9033 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.684 MB | 7.684 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 9055 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.866% | 100.429% | 2.010 s | 75.556 MB | 122.223 MB | 85.539 MB | 134.125 MB | n/a MB | n/a MB |
| python3 | 9056 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.920% | 100.398% | 2.010 s | 75.697 MB | 122.488 MB | 85.539 MB | 134.125 MB | n/a MB | n/a MB |
| python3 | 9073 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.461 MB | 7.461 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 9083 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.836% | 100.378% | 2.010 s | 8.230 MB | 8.230 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 9084 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.890% | 100.367% | 2.010 s | 8.340 MB | 8.340 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 9085 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.892% | 100.342% | 2.010 s | 141.738 MB | 215.488 MB | 147.732 MB | 221.406 MB | n/a MB | n/a MB |
| python3 | 9087 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.827% | 100.332% | 2.010 s | 138.891 MB | 214.516 MB | 145.133 MB | 221.406 MB | n/a MB | n/a MB |
| python3 | 9105 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 99.922% | 100.350% | 2.010 s | 8.316 MB | 8.316 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| python3 | 9128 | sandbox_agent_lsb-opencode_0000_0000 | 32 | 0.288% | 2.975% | 0.090 s | 22.330 MB | 22.461 MB | 28.070 MB | 28.191 MB | n/a MB | n/a MB |
| bash | 9127 | sandbox_agent_lsb-opencode_0000_0000 | 32 | 0.000% | 0.000% | 0.000 s | 2.887 MB | 2.887 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 9180 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 9218 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.375 MB | 22.375 MB | 28.098 MB | 28.098 MB | n/a MB | n/a MB |
| python3 | 9251 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.602 MB | 7.602 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 9289 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.461 MB | 22.461 MB | 28.191 MB | 28.191 MB | n/a MB | n/a MB |
| bash | 9330 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.676 MB | 2.676 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 9331 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 2.975% | 2.975% | 0.030 s | 12.945 MB | 12.945 MB | 17.066 MB | 17.066 MB | n/a MB | n/a MB |
| python3 | 9389 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| bash | 9434 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.000 MB | 3.000 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 9435 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.582 MB | 13.582 MB | 207.277 MB | 207.277 MB | n/a MB | n/a MB |
| python3 | 9535 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 2.485% | 14.910% | 0.150 s | 95.590 MB | 100.637 MB | 289.948 MB | 295.055 MB | n/a MB | n/a MB |
| python3 | 9550 | sandbox_agent_lsb-opencode_0000_0000 | 18 | 1.637% | 25.842% | 0.280 s | 98.328 MB | 100.809 MB | 292.797 MB | 295.320 MB | n/a MB | n/a MB |
| bash | 9549 | sandbox_agent_lsb-opencode_0000_0000 | 18 | 0.000% | 0.000% | 0.000 s | 2.703 MB | 2.703 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 9595 | sandbox_agent_lsb-opencode_0000_0000 | 120 | 166.597% | 183.864% | 199.690 s | 1996.653 MB | 2123.191 MB | 3365.758 MB | 3493.008 MB | n/a MB | n/a MB |
| python3 | 9696 | sandbox_agent_lsb-opencode_0000_0000 | 119 | 166.014% | 176.246% | 197.340 s | 1994.813 MB | 2123.438 MB | 3378.090 MB | 3493.004 MB | n/a MB | n/a MB |
| python3 | 9747 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 112.466% | 160.426% | 2.270 s | 1408.882 MB | 1742.930 MB | 3043.779 MB | 3121.336 MB | n/a MB | n/a MB |
| bash | 9765 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.727 MB | 2.727 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 9766 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 111.940% | 156.047% | 3.380 s | 1863.062 MB | 3718.250 MB | 3955.185 MB | 6759.688 MB | n/a MB | n/a MB |
| python3 | 9823 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.129 MB | 22.129 MB | 28.047 MB | 28.047 MB | n/a MB | n/a MB |
| bash | 9822 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.684 MB | 2.684 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 9853 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 22.289 MB | 22.289 MB | 28.027 MB | 28.027 MB | n/a MB | n/a MB |
| bash | 9852 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 9887 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 82.488 MB | 82.488 MB | 1933.312 MB | 1933.312 MB | n/a MB | n/a MB |
| bash | 9886 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.812 MB | 2.812 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 9919 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 171.955% | 171.955% | 1.730 s | 106.041 MB | 116.961 MB | 1989.648 MB | 1990.684 MB | n/a MB | n/a MB |
| python3 | 9939 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 172.242% | 175.146% | 13.870 s | 2562.643 MB | 2664.387 MB | 3978.486 MB | 4064.586 MB | n/a MB | n/a MB |
| bash | 9938 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.699 MB | 2.699 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 9980 | sandbox_agent_lsb-opencode_0000_0000 | 12 | 172.657% | 176.837% | 19.130 s | 2574.484 MB | 2738.105 MB | 4005.055 MB | 4167.395 MB | n/a MB | n/a MB |
| bash | 9979 | sandbox_agent_lsb-opencode_0000_0000 | 12 | 0.000% | 0.000% | 0.000 s | 2.641 MB | 2.641 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 10007 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 0.827% | 3.968% | 0.050 s | 34.448 MB | 34.988 MB | 228.422 MB | 228.941 MB | n/a MB | n/a MB |
| python3 | 10023 | sandbox_agent_lsb-opencode_0000_0000 | 11 | 158.077% | 174.293% | 15.920 s | 1602.161 MB | 1783.953 MB | 2871.653 MB | 3161.543 MB | n/a MB | n/a MB |
| bash | 10022 | sandbox_agent_lsb-opencode_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 10057 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.789 MB | 21.789 MB | 213.863 MB | 213.863 MB | n/a MB | n/a MB |
| bash | 10056 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.762 MB | 2.762 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 10098 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.848 MB | 13.848 MB | 207.449 MB | 207.449 MB | n/a MB | n/a MB |
| bash | 10097 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.809 MB | 2.809 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 10193 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.617 MB | 2.617 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 10194 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.582 MB | 50.582 MB | 1908.828 MB | 1908.828 MB | n/a MB | n/a MB |
| bash | 10206 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.590 MB | 2.590 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 10207 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.574 MB | 7.574 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python3 | 10242 | sandbox_agent_lsb-opencode_0000_0000 | 56 | 170.771% | 176.962% | 94.570 s | 2941.683 MB | 3167.895 MB | 4308.439 MB | 4438.094 MB | n/a MB | n/a MB |
| python3 | 10282 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 170.850% | 181.507% | 20.660 s | 1629.904 MB | 1824.727 MB | 3120.841 MB | 3885.500 MB | n/a MB | n/a MB |
| bash | 10281 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 0.000% | 0.000% | 0.000 s | 2.688 MB | 2.688 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 10312 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.785 MB | 2.785 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 10313 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 163.366% | 163.366% | 1.650 s | 892.938 MB | 1653.602 MB | 2521.654 MB | 3034.023 MB | n/a MB | n/a MB |
| bash | 10327 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 10328 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 145.052% | 145.052% | 1.460 s | 849.939 MB | 1629.855 MB | 2478.209 MB | 3021.059 MB | n/a MB | n/a MB |
| python3 | 10341 | sandbox_agent_lsb-opencode_0000_0000 | 56 | 172.075% | 177.779% | 95.290 s | 2954.827 MB | 3175.594 MB | 4318.680 MB | 4439.094 MB | n/a MB | n/a MB |
| python3 | 10427 | sandbox_agent_lsb-opencode_0000_0000 | 56 | 172.558% | 178.073% | 95.580 s | 2971.142 MB | 3146.598 MB | 4340.611 MB | 4437.016 MB | n/a MB | n/a MB |
| docker | 10614 |  | 10 | 0.000% | 0.000% | 0.000 s | 29.652 MB | 29.652 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.042% | 100.000% | 11965.038 MB | 13524.000 MB | 29.343 W | 73.787 W | 400571.832 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-opencode_0000_0000 | 41.876% | 211.491% | 5717.506 s | 1220.324 MB | 4001.336 MB | 170.816406 MB | 815.800781 MB | 26.256117 MB | 0.509228 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2001 | 13651.430 | interrupted |
| run0:write_lora_adapter:agent_lsb-opencode_0000 | -1 | 13651.429 | interrupted |
| engine:execute | 2002 | 13651.428 | interrupted |
| teardown:commit | 2002 | 10.579 | interrupted |
| sandbox:commit | 2002 | 10.579 | interrupted |
| checkpoint.total | 2002 | 10.579 | interrupted |
| checkpoint.fs_snapshot | 2002 | 10.579 | interrupted |
| runtime:container_call:commit | 2002 | 10.530 | interrupted |
| harness:retire | -1 | 0.373 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| harness:attempt_rpc | 1/1 | 0 | 0 | 13634.874 | 0.021 | 13634.854 | 113.786 | 13634874.092 | 13634874.092 | 13634874.092 |
| harness:await_cli | 1/1 | 0 | 0 | 13616.099 | n/a | n/a | 24.653 | 13616098.677 | 13616098.677 | 13616098.677 |
| llm:attempt | 121/121 | 0 | 0 | 12207.977 | 4.896 | 12203.079 | 8.233 | 100892.373 | 71151.273 | 268336.896 |
| tool:bash | 100/100 | 0 | 0 | 1083.956 | n/a | n/a | 11.144 | 10839.563 | 1891.669 | 56465.877 |
| harness:startup_ready | 1/1 | 0 | 0 | 16.092 | n/a | n/a | 57.902 | 16091.868 | 16091.868 | 16091.868 |
| syscall:execve | 4775/4775 | 0 | 0 | 5.651 | n/a | n/a | 0.087 | 1.183 | 1.150 | 1.349 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.651 | 1.081 | 3.570 | 55.884 | 4651.163 | 4651.163 | 4651.163 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.651 | 1.081 | 3.570 | 55.881 | 4650.969 | 4650.969 | 4650.969 |
| tool:read | 38/38 | 0 | 0 | 4.016 | n/a | n/a | 5.096 | 105.684 | 106.627 | 222.313 |
| tool:write | 26/26 | 0 | 0 | 2.504 | n/a | n/a | 0.553 | 96.301 | 78.238 | 182.087 |
| syscall:sendto | 1016/1016 | 0 | 0 | 2.257 | n/a | n/a | 0.446 | 2.221 | 1.800 | 4.370 |
| tool:edit | 11/11 | 0 | 0 | 1.399 | n/a | n/a | 0.000 | 127.220 | 105.488 | 270.830 |
| syscall:connect | 532/532 | 0 | 0 | 1.293 | n/a | n/a | 0.444 | 2.431 | 2.082 | 4.885 |
| harness:submit | 1/1 | 0 | 0 | 1.208 | n/a | n/a | 1.997 | 1207.668 | 1207.668 | 1207.668 |
| sandbox:create | 1/1 | 0 | 0 | 1.045 | 0.244 | 0.800 | 0.000 | 1044.665 | 1044.665 | 1044.665 |
| run:detect | 1/1 | 0 | 0 | 0.745 | 0.001 | 0.744 | 0.000 | 745.216 | 745.216 | 745.216 |
| run:container_call | 8/9 | 0 | 1 | 0.674 | 0.001 | 0.672 | 0.009 | 84.191 | 40.478 | 284.465 |
| sandbox:start | 1/1 | 0 | 0 | 0.555 | 0.002 | 0.552 | 0.000 | 554.562 | 554.562 | 554.562 |
| runtime.container_create | 1/1 | 0 | 0 | 0.554 | 0.002 | 0.552 | 0.000 | 554.435 | 554.435 | 554.435 |
| tool:todowrite | 4/4 | 0 | 0 | 0.158 | n/a | n/a | 0.001 | 39.468 | 38.839 | 54.515 |
| agency:services_close | 1/1 | 0 | 0 | 0.128 | 0.001 | 0.127 | 0.025 | 127.932 | 127.932 | 127.932 |
| harness:snapshot | 1/1 | 0 | 0 | 0.099 | n/a | n/a | 0.029 | 99.059 | 99.059 | 99.059 |
| agency:services_start | 1/1 | 0 | 0 | 0.076 | 0.041 | 0.035 | 0.000 | 76.068 | 76.068 | 76.068 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.009 | 0.039 | 0.000 | 48.758 | 48.758 | 48.758 |
| harness:launch | 1/1 | 0 | 0 | 0.049 | n/a | n/a | 1.240 | 48.602 | 48.602 | 48.602 |
| syscall:bind | 10/10 | 0 | 0 | 0.027 | n/a | n/a | 0.089 | 2.652 | 2.396 | 4.215 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.020 | 0.020 | 0.000 | 0.004 | 20.278 | 20.278 | 20.278 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.392 | 1.392 | 1.392 |
| sync:container | 9/9 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.069 | 0.072 | 0.095 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.204 | 0.204 | 0.204 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.074 | 0.074 | 0.074 |
| sandbox:commit | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| checkpoint.total | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| teardown:commit | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| run:write_lora_adapter | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| engine:execute | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| checkpoint.fs_snapshot | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 13574 | 0.109 | 0.033 | 39.249 | 39.249 | 14.848757 CPU seconds | n/a |
| GPU 0 memory | MB | 13576 | 11965.038 | 11670.000 | 13524.000 | 12032.000 | n/a | n/a |
| GPU 0 power | W | 13576 | 29.343 | 27.378 | 73.787 | 28.510 | n/a | 400571.832 J |
| GPU 0 proc / 1852-6268 / sandbox / ~ / device / GPU-20b315da-5ee3-7117-5185-d5ea66a7ca1b memory | MB | 13576 | 3215.195 | 3118.000 | 4708.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 1852-6268 / sandbox / ~ / device / GPU-20b315da-5ee3-7117-5185-d5ea66a7ca1b estimated power | W | 9860 | 0.307 | 0.000 | 63.317 | 0.000 | n/a | n/a |
| GPU 0 proc / 1852-6268 / sandbox / ~ / device / GPU-20b315da-5ee3-7117-5185-d5ea66a7ca1b utilization | percent | 9860 | 0.232 | 0.000 | 59.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 1892-10230 / sandbox / ~ / device / GPU-20b315da-5ee3-7117-5185-d5ea66a7ca1b memory | MB | 13576 | 8267.843 | 8070.000 | 8336.000 | 8336.000 | n/a | n/a |
| GPU 0 proc / 1892-10230 / sandbox / ~ / device / GPU-20b315da-5ee3-7117-5185-d5ea66a7ca1b estimated power | W | 3510 | 5.126 | 0.000 | 73.476 | 0.000 | n/a | n/a |
| GPU 0 proc / 1892-10230 / sandbox / ~ / device / GPU-20b315da-5ee3-7117-5185-d5ea66a7ca1b utilization | percent | 3510 | 6.991 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 13576 | 11483.038 | 11188.000 | 13042.000 | 11550.000 | n/a | n/a |
| GPU 0 utilization | percent | 13576 | 2.042 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 13576 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 13575 | 3.017 | 0.092 | 73.605 | 1.252 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 13575 | 11.161 | 1.535 | 64.838 | 7.407 | n/a | n/a |
| host disk_read_mb_s | MB/s | 13575 | 0.092 | 0.000 | 194.056 | 27.520 | n/a | n/a |
| host disk_write_mb_s | MB/s | 13575 | 0.169 | 0.000 | 98.434 | 1.527 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 13575 | 0.043 | 0.000 | 48.791 | 32.188 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 13575 | 0.044 | 0.000 | 48.923 | 32.504 | n/a | n/a |
| host mem_total_mb | MB | 13576 | 15363.539 | 15363.539 | 15363.539 | 15363.539 | n/a | n/a |
| host mem_used_mb | MB | 13576 | 7633.052 | 6593.828 | 10691.609 | 7533.566 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 13575 | 0.001 | 0.000 | 8.141 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 13575 | 0.001 | 0.000 | 8.163 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 13575 | 0.002 | 0.000 | 13.184 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 13575 | 0.003 | 0.000 | 0.589 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_edge_guards.py (PID 10007) CPU | percent | 6 | 0.827 | 0.000 | 3.968 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_edge_guards.py (PID 10007) rss_mb | MB | 7 | 34.448 | 31.457 | 34.988 | 34.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_edge_guards.py (PID 10007) main thread run-queue wait | percent | 6 | 0.023 | 0.000 | 0.087 | 0.000 | 0.001374 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_edge_guards.py (PID 10007) vms_mb | MB | 7 | 228.422 | 225.305 | 228.941 | 228.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10022) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10022) rss_mb | MB | 11 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10022) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10022) vms_mb | MB | 11 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10023) CPU | percent | 10 | 158.077 | 84.267 | 174.293 | 171.929 | 15.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10023) rss_mb | MB | 11 | 1602.161 | 13.660 | 1783.953 | 1773.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10023) main thread run-queue wait | percent | 10 | 52.284 | 4.898 | 74.296 | 74.296 | 5.265451 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10023) vms_mb | MB | 11 | 2871.653 | 207.426 | 3161.543 | 3151.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10056) rss_mb | MB | 1 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10056) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10057) rss_mb | MB | 1 | 21.789 | 21.789 | 21.789 | 21.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10057) vms_mb | MB | 1 | 213.863 | 213.863 | 213.863 | 213.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10097) rss_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10097) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10098) rss_mb | MB | 1 | 13.848 | 13.848 | 13.848 | 13.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10098) vms_mb | MB | 1 | 207.449 | 207.449 | 207.449 | 207.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10193) rss_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10193) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10194) rss_mb | MB | 1 | 50.582 | 50.582 | 50.582 | 50.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10194) vms_mb | MB | 1 | 1908.828 | 1908.828 | 1908.828 | 1908.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10206) rss_mb | MB | 1 | 2.590 | 2.590 | 2.590 | 2.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10206) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10207) rss_mb | MB | 1 | 7.574 | 7.574 | 7.574 | 7.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10207) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10242) CPU | percent | 55 | 170.771 | 151.103 | 176.962 | 162.020 | 94.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10242) rss_mb | MB | 56 | 2941.683 | 105.742 | 3167.895 | 3167.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10242) main thread run-queue wait | percent | 55 | 54.237 | 26.885 | 79.284 | 69.043 | 30.035900 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10242) vms_mb | MB | 56 | 4308.439 | 1963.738 | 4438.094 | 4438.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10281) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10281) rss_mb | MB | 13 | 2.688 | 2.688 | 2.688 | 2.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10281) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10281) vms_mb | MB | 13 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10282) CPU | percent | 12 | 170.850 | 160.152 | 181.507 | 171.016 | 20.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10282) rss_mb | MB | 13 | 1629.904 | 1528.387 | 1824.727 | 1708.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10282) main thread run-queue wait | percent | 12 | 61.112 | 47.548 | 77.877 | 58.449 | 7.391314 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10282) vms_mb | MB | 13 | 3120.841 | 2919.074 | 3885.500 | 3064.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10312) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10312) rss_mb | MB | 2 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10312) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10312) vms_mb | MB | 2 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10313) CPU | percent | 1 | 163.366 | 163.366 | 163.366 | 163.366 | 1.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10313) rss_mb | MB | 2 | 892.938 | 132.273 | 1653.602 | 1653.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10313) main thread run-queue wait | percent | 1 | 41.150 | 41.150 | 41.150 | 41.150 | 0.415615 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10313) vms_mb | MB | 2 | 2521.654 | 2009.285 | 3034.023 | 3034.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10327) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10327) rss_mb | MB | 2 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10327) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 10327) vms_mb | MB | 2 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10328) CPU | percent | 1 | 145.052 | 145.052 | 145.052 | 145.052 | 1.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10328) rss_mb | MB | 2 | 849.939 | 70.023 | 1629.855 | 1629.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10328) main thread run-queue wait | percent | 1 | 22.432 | 22.432 | 22.432 | 22.432 | 0.225789 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 10328) vms_mb | MB | 2 | 2478.209 | 1935.359 | 3021.059 | 3021.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10341) CPU | percent | 55 | 172.075 | 160.923 | 177.779 | 166.443 | 95.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10341) rss_mb | MB | 56 | 2954.827 | 1106.250 | 3175.594 | 3033.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10341) main thread run-queue wait | percent | 55 | 54.538 | 34.311 | 74.173 | 67.277 | 30.202126 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10341) vms_mb | MB | 56 | 4318.680 | 2926.164 | 4439.094 | 4286.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10427) CPU | percent | 55 | 172.558 | 161.122 | 178.073 | 171.674 | 95.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10427) rss_mb | MB | 56 | 2971.142 | 1737.836 | 3146.598 | 3087.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10427) main thread run-queue wait | percent | 55 | 55.312 | 44.988 | 78.500 | 54.850 | 30.637526 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 10427) vms_mb | MB | 56 | 4340.611 | 3959.352 | 4437.016 | 4340.883 | n/a | n/a |
| docker commit (PID 10614) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 10614) io read MB/s | MB/s | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 10614) io write MB/s | MB/s | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 10614) rss_mb | MB | 10 | 29.652 | 29.652 | 29.652 | 29.652 | n/a | n/a |
| docker commit (PID 10614) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 10614) vms_mb | MB | 10 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1843) CPU | percent | 13575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1843) io read MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1843) io write MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1843) rss_mb | MB | 13576 | 3.363 | 3.363 | 3.363 | 3.363 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1843) main thread run-queue wait | percent | 13575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1843) vms_mb | MB | 13576 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1852) CPU | percent | 13575 | 1.345 | 0.000 | 163.464 | 0.995 | 183.900000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 1852) io read MB/s | MB/s | 13575 | 0.012 | 0.000 | 90.786 | 0.000 | 169.250000 MB | n/a |
| Agency harness — python -m lsbench (PID 1852) io write MB/s | MB/s | 13575 | 0.099 | 0.015 | 49.500 | 0.023 | 1352.519531 MB | n/a |
| Agency harness — python -m lsbench (PID 1852) rss_mb | MB | 13576 | 2911.261 | 2314.230 | 3468.078 | 3468.078 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1852) main thread run-queue wait | percent | 13575 | 0.000 | 0.000 | 0.411 | 0.000 | 0.020651 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 1852) vms_mb | MB | 13576 | 15733.619 | 13774.812 | 17825.988 | 16446.887 | n/a | n/a |
| Python — vllm (PID 1857) CPU | percent | 13575 | 0.156 | 0.000 | 7.910 | 0.000 | 21.350000 CPU seconds | n/a |
| Python — vllm (PID 1857) io read MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 1857) io write MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.008 | 0.000 | 0.117188 MB | n/a |
| Python — vllm (PID 1857) rss_mb | MB | 13576 | 1768.331 | 1766.566 | 1769.066 | 1768.539 | n/a | n/a |
| Python — vllm (PID 1857) main thread run-queue wait | percent | 13575 | 0.003 | 0.000 | 0.701 | 0.000 | 0.437824 run-queue seconds | n/a |
| Python — vllm (PID 1857) vms_mb | MB | 13576 | 11010.363 | 10951.148 | 11024.168 | 11024.168 | n/a | n/a |
| Python — python -c (PID 1891) CPU | percent | 13575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 1891) io read MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1891) io write MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1891) rss_mb | MB | 13576 | 12.285 | 12.285 | 12.285 | 12.285 | n/a | n/a |
| Python — python -c (PID 1891) main thread run-queue wait | percent | 13575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 1891) vms_mb | MB | 13576 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 1892) CPU | percent | 13575 | 2.075 | 0.000 | 61.514 | 1.989 | 283.680000 CPU seconds | n/a |
| VLLM::EngineCore (PID 1892) io read MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 1892) io write MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.004 | 0.000 | 0.085938 MB | n/a |
| VLLM::EngineCore (PID 1892) rss_mb | MB | 13576 | 2313.235 | 2312.344 | 2313.719 | 2313.312 | n/a | n/a |
| VLLM::EngineCore (PID 1892) main thread run-queue wait | percent | 13575 | 0.001 | 0.000 | 0.544 | 0.000 | 0.103916 run-queue seconds | n/a |
| VLLM::EngineCore (PID 1892) vms_mb | MB | 13576 | 21204.001 | 21203.145 | 21204.289 | 21204.273 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1995) CPU | percent | 13575 | 0.030 | 0.000 | 4.975 | 0.000 | 4.100000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1995) io read MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.008 | 0.000 | 0.007812 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1995) io write MB/s | MB/s | 13575 | 0.000 | 0.000 | 0.008 | 0.000 | 0.402344 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1995) rss_mb | MB | 13576 | 44.971 | 43.582 | 45.570 | 45.152 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1995) main thread run-queue wait | percent | 13575 | 0.001 | 0.000 | 0.305 | 0.001 | 0.080378 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 1995) vms_mb | MB | 13576 | 131.199 | 131.176 | 131.719 | 131.176 | n/a | n/a |
| docker info (PID 2003) rss_mb | MB | 1 | 29.926 | 29.926 | 29.926 | 29.926 | n/a | n/a |
| docker info (PID 2003) vms_mb | MB | 1 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker-buildx (PID 2012) rss_mb | MB | 1 | 41.828 | 41.828 | 41.828 | 41.828 | n/a | n/a |
| docker-buildx (PID 2012) vms_mb | MB | 1 | 1298.477 | 1298.477 | 1298.477 | 1298.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2110) CPU | percent | 13574 | 0.002 | 0.000 | 0.996 | 0.000 | 0.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2110) rss_mb | MB | 13575 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2110) main thread run-queue wait | percent | 13574 | 0.004 | 0.000 | 5.260 | 0.000 | 0.531881 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2110) vms_mb | MB | 13575 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2146) CPU | percent | 13574 | 0.003 | 0.000 | 1.989 | 0.000 | 0.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2146) rss_mb | MB | 13575 | 1.391 | 1.391 | 1.391 | 1.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2146) main thread run-queue wait | percent | 13574 | 0.004 | 0.000 | 5.438 | 0.000 | 0.513482 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2146) vms_mb | MB | 13575 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2236) CPU | percent | 13574 | 31.279 | 0.000 | 101.285 | 0.000 | 4269.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2236) rss_mb | MB | 13575 | 110.781 | 2.906 | 139.637 | 139.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2236) main thread run-queue wait | percent | 13574 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000154 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2236) vms_mb | MB | 13575 | 973.285 | 4.262 | 975.660 | 975.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2242) CPU | percent | 2 | 58.318 | 51.675 | 64.961 | 64.961 | 1.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2242) rss_mb | MB | 3 | 46.454 | 15.039 | 76.793 | 76.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2242) main thread run-queue wait | percent | 2 | 0.042 | 0.013 | 0.071 | 0.013 | 0.000847 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2242) vms_mb | MB | 3 | 57.158 | 22.539 | 92.770 | 92.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2250) rss_mb | MB | 1 | 14.000 | 14.000 | 14.000 | 14.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2250) vms_mb | MB | 1 | 6358.133 | 6358.133 | 6358.133 | 6358.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2264) CPU | percent | 13558 | 2.943 | 0.000 | 128.299 | 0.995 | 401.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2264) rss_mb | MB | 13559 | 715.815 | 30.613 | 986.297 | 781.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2264) main thread run-queue wait | percent | 13558 | 1.852 | 0.000 | 75.759 | 0.000 | 252.865683 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2264) vms_mb | MB | 13559 | 15720.058 | 6358.195 | 16739.410 | 16731.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — mcp_client.py (PID 2764) rss_mb | MB | 1 | 20.906 | 20.906 | 20.906 | 20.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — mcp_client.py (PID 2764) vms_mb | MB | 1 | 26.738 | 26.738 | 26.738 | 26.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — weights_util.py (PID 2882) CPU | percent | 15 | 172.981 | 167.961 | 177.053 | 171.053 | 26.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — weights_util.py (PID 2882) rss_mb | MB | 16 | 132.703 | 73.777 | 179.066 | 179.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — weights_util.py (PID 2882) main thread run-queue wait | percent | 15 | 54.144 | 47.589 | 76.516 | 49.056 | 8.177725 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — weights_util.py (PID 2882) vms_mb | MB | 16 | 1980.767 | 1955.266 | 2007.273 | 1993.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2962) CPU | percent | 21 | 0.236 | 0.000 | 4.962 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2962) rss_mb | MB | 22 | 21.593 | 16.168 | 21.852 | 21.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2962) main thread run-queue wait | percent | 21 | 0.005 | 0.000 | 0.098 | 0.000 | 0.000999 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2962) vms_mb | MB | 22 | 27.592 | 21.641 | 27.875 | 27.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3022) CPU | percent | 1 | 2.978 | 2.978 | 2.978 | 2.978 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3022) rss_mb | MB | 2 | 12.230 | 12.230 | 12.230 | 12.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3022) main thread run-queue wait | percent | 1 | 0.034 | 0.034 | 0.034 | 0.034 | 0.000341 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3022) vms_mb | MB | 2 | 15.977 | 15.977 | 15.977 | 15.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpszyyukma.py (PID 3042) rss_mb | MB | 1 | 7.168 | 7.168 | 7.168 | 7.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpszyyukma.py (PID 3042) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python3 (PID 3076) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python3 (PID 3076) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — inspect_gen0.py (PID 3101) CPU | percent | 1 | 1.985 | 1.985 | 1.985 | 1.985 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — inspect_gen0.py (PID 3101) rss_mb | MB | 2 | 12.270 | 12.270 | 12.270 | 12.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — inspect_gen0.py (PID 3101) main thread run-queue wait | percent | 1 | 0.007 | 0.007 | 0.007 | 0.007 | 0.000068 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — inspect_gen0.py (PID 3101) vms_mb | MB | 2 | 15.945 | 15.945 | 15.945 | 15.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmper_fdvgf.py (PID 3107) rss_mb | MB | 1 | 7.512 | 7.512 | 7.512 | 7.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmper_fdvgf.py (PID 3107) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp8zfr9rif.py (PID 3138) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp8zfr9rif.py (PID 3138) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3182) CPU | percent | 40 | 0.050 | 0.000 | 1.982 | 1.982 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3182) rss_mb | MB | 41 | 21.827 | 21.824 | 21.949 | 21.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3182) main thread run-queue wait | percent | 40 | 0.000 | 0.000 | 0.009 | 0.009 | 0.000091 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3182) vms_mb | MB | 41 | 26.967 | 26.961 | 27.227 | 27.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3234) rss_mb | MB | 1 | 21.949 | 21.949 | 21.949 | 21.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3234) vms_mb | MB | 1 | 27.227 | 27.227 | 27.227 | 27.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3277) CPU | percent | 2 | 2.484 | 1.985 | 2.983 | 1.985 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3277) rss_mb | MB | 3 | 12.339 | 12.297 | 12.422 | 12.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3277) main thread run-queue wait | percent | 2 | 0.019 | 0.017 | 0.022 | 0.022 | 0.000386 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3277) vms_mb | MB | 3 | 16.164 | 16.078 | 16.207 | 16.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp9oram3du.py (PID 3300) rss_mb | MB | 1 | 7.820 | 7.820 | 7.820 | 7.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp9oram3du.py (PID 3300) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpu9t7kv_c.py (PID 3330) rss_mb | MB | 1 | 5.938 | 5.938 | 5.938 | 5.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpu9t7kv_c.py (PID 3330) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmparciajex.py (PID 3363) rss_mb | MB | 1 | 7.602 | 7.602 | 7.602 | 7.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmparciajex.py (PID 3363) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3447) CPU | percent | 19 | 0.209 | 0.000 | 2.976 | 2.976 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3447) rss_mb | MB | 20 | 21.951 | 21.926 | 22.176 | 22.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3447) main thread run-queue wait | percent | 19 | 0.001 | 0.000 | 0.014 | 0.014 | 0.000216 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3447) vms_mb | MB | 20 | 27.978 | 27.961 | 28.129 | 28.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python3 (PID 3487) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python3 (PID 3487) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpblrkv6mz.py (PID 3523) rss_mb | MB | 1 | 7.332 | 7.332 | 7.332 | 7.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpblrkv6mz.py (PID 3523) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — inspect_gen2.py (PID 3567) CPU | percent | 2 | 2.484 | 1.985 | 2.982 | 2.982 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — inspect_gen2.py (PID 3567) rss_mb | MB | 3 | 12.612 | 12.484 | 12.742 | 12.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — inspect_gen2.py (PID 3567) main thread run-queue wait | percent | 2 | 0.036 | 0.029 | 0.042 | 0.029 | 0.000718 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — inspect_gen2.py (PID 3567) vms_mb | MB | 3 | 17.112 | 17.090 | 17.156 | 17.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpbeydksx7.py (PID 3576) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpbeydksx7.py (PID 3576) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpji51j85j.py (PID 3614) rss_mb | MB | 1 | 6.633 | 6.633 | 6.633 | 6.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpji51j85j.py (PID 3614) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpr2v6klq9.py (PID 3664) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpr2v6klq9.py (PID 3664) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3702) CPU | percent | 53 | 0.299 | 0.000 | 3.964 | 2.977 | 0.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3702) rss_mb | MB | 54 | 3.569 | 2.621 | 13.070 | 13.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3702) main thread run-queue wait | percent | 53 | 0.002 | 0.000 | 0.024 | 0.012 | 0.000870 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3702) vms_mb | MB | 54 | 5.080 | 3.848 | 17.363 | 17.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3703) CPU | percent | 48 | 0.207 | 0.000 | 4.965 | 0.000 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3703) rss_mb | MB | 49 | 21.864 | 19.945 | 22.207 | 22.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3703) main thread run-queue wait | percent | 48 | 0.004 | 0.000 | 0.078 | 0.000 | 0.001779 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3703) vms_mb | MB | 49 | 27.905 | 25.871 | 28.188 | 28.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp_9lch29r.py (PID 3726) rss_mb | MB | 1 | 6.012 | 6.012 | 6.012 | 6.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp_9lch29r.py (PID 3726) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpbxuzimfg.py (PID 3761) rss_mb | MB | 1 | 7.797 | 7.797 | 7.797 | 7.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpbxuzimfg.py (PID 3761) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpajr8ejq5.py (PID 3796) rss_mb | MB | 1 | 8.465 | 8.465 | 8.465 | 8.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpajr8ejq5.py (PID 3796) vms_mb | MB | 1 | 13.145 | 13.145 | 13.145 | 13.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnlukhiiq.py (PID 3855) rss_mb | MB | 1 | 7.602 | 7.602 | 7.602 | 7.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnlukhiiq.py (PID 3855) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnvp0hw97.py (PID 3892) rss_mb | MB | 1 | 9.070 | 9.070 | 9.070 | 9.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnvp0hw97.py (PID 3892) vms_mb | MB | 1 | 13.270 | 13.270 | 13.270 | 13.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpqozs14x3.py (PID 3928) rss_mb | MB | 1 | 7.469 | 7.469 | 7.469 | 7.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpqozs14x3.py (PID 3928) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmphn_oqiok.py (PID 3964) rss_mb | MB | 1 | 7.934 | 7.934 | 7.934 | 7.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmphn_oqiok.py (PID 3964) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gen1_gen3.py (PID 4027) CPU | percent | 9 | 2.976 | 1.986 | 3.969 | 2.980 | 0.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gen1_gen3.py (PID 4027) rss_mb | MB | 10 | 13.054 | 12.805 | 13.223 | 13.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gen1_gen3.py (PID 4027) main thread run-queue wait | percent | 9 | 0.039 | 0.009 | 0.191 | 0.030 | 0.003557 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gen1_gen3.py (PID 4027) vms_mb | MB | 10 | 17.342 | 17.066 | 17.449 | 17.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpxbejqiha.py (PID 4055) rss_mb | MB | 1 | 7.469 | 7.469 | 7.469 | 7.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpxbejqiha.py (PID 4055) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpoe2183ry.py (PID 4091) rss_mb | MB | 1 | 7.777 | 7.777 | 7.777 | 7.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpoe2183ry.py (PID 4091) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gen1_gen3.py (PID 4127) rss_mb | MB | 1 | 12.805 | 12.805 | 12.805 | 12.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gen1_gen3.py (PID 4127) vms_mb | MB | 1 | 17.141 | 17.141 | 17.141 | 17.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gen1_gen3.py (PID 4164) rss_mb | MB | 1 | 13.078 | 13.078 | 13.078 | 13.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gen1_gen3.py (PID 4164) vms_mb | MB | 1 | 17.422 | 17.422 | 17.422 | 17.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpwf5cbq8e.py (PID 4200) rss_mb | MB | 1 | 8.469 | 8.469 | 8.469 | 8.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpwf5cbq8e.py (PID 4200) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpy85d2hb6.py (PID 4239) rss_mb | MB | 1 | 6.410 | 6.410 | 6.410 | 6.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpy85d2hb6.py (PID 4239) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzizst763.py (PID 4276) rss_mb | MB | 1 | 7.805 | 7.805 | 7.805 | 7.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzizst763.py (PID 4276) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4lxqx8sq.py (PID 4312) rss_mb | MB | 1 | 8.277 | 8.277 | 8.277 | 8.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4lxqx8sq.py (PID 4312) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp497devuu.py (PID 4348) rss_mb | MB | 1 | 8.473 | 8.473 | 8.473 | 8.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp497devuu.py (PID 4348) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpx96x0jgz.py (PID 4385) rss_mb | MB | 1 | 6.914 | 6.914 | 6.914 | 6.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpx96x0jgz.py (PID 4385) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4495) rss_mb | MB | 1 | 4.906 | 4.906 | 4.906 | 4.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4495) vms_mb | MB | 1 | 11.383 | 11.383 | 11.383 | 11.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_counterfactual_modes.py (PID 4509) CPU | percent | 35 | 0.511 | 0.000 | 3.969 | 2.979 | 0.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_counterfactual_modes.py (PID 4509) rss_mb | MB | 36 | 22.268 | 18.645 | 22.371 | 22.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_counterfactual_modes.py (PID 4509) main thread run-queue wait | percent | 35 | 0.009 | 0.000 | 0.110 | 0.021 | 0.003246 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_counterfactual_modes.py (PID 4509) vms_mb | MB | 36 | 28.083 | 24.410 | 28.230 | 28.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpv9goso0w.py (PID 4526) rss_mb | MB | 1 | 7.121 | 7.121 | 7.121 | 7.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpv9goso0w.py (PID 4526) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp6xe_yl3p.py (PID 4562) rss_mb | MB | 1 | 7.242 | 7.242 | 7.242 | 7.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp6xe_yl3p.py (PID 4562) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpkxpu207m.py (PID 4623) rss_mb | MB | 1 | 8.793 | 8.793 | 8.793 | 8.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpkxpu207m.py (PID 4623) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp_x4nq7q3.py (PID 4661) rss_mb | MB | 1 | 7.207 | 7.207 | 7.207 | 7.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp_x4nq7q3.py (PID 4661) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp9ls1a377.py (PID 4715) rss_mb | MB | 1 | 4.750 | 4.750 | 4.750 | 4.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp9ls1a377.py (PID 4715) vms_mb | MB | 1 | 11.383 | 11.383 | 11.383 | 11.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpwz6kh0it.py (PID 4751) rss_mb | MB | 1 | 7.473 | 7.473 | 7.473 | 7.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpwz6kh0it.py (PID 4751) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — compare_modes.py (PID 4791) CPU | percent | 3 | 2.649 | 1.985 | 2.983 | 1.985 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — compare_modes.py (PID 4791) rss_mb | MB | 4 | 12.465 | 12.371 | 12.496 | 12.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — compare_modes.py (PID 4791) main thread run-queue wait | percent | 3 | 0.020 | 0.018 | 0.022 | 0.021 | 0.000613 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — compare_modes.py (PID 4791) vms_mb | MB | 4 | 15.965 | 15.965 | 15.965 | 15.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpvam3814e.py (PID 4808) rss_mb | MB | 1 | 6.211 | 6.211 | 6.211 | 6.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpvam3814e.py (PID 4808) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpm1fvc4o9.py (PID 4844) rss_mb | MB | 1 | 6.930 | 6.930 | 6.930 | 6.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpm1fvc4o9.py (PID 4844) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpxfmq09x7.py (PID 4880) rss_mb | MB | 1 | 7.711 | 7.711 | 7.711 | 7.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpxfmq09x7.py (PID 4880) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_clean_modes.py (PID 4932) CPU | percent | 23 | 1.122 | 0.000 | 8.936 | 8.936 | 0.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_clean_modes.py (PID 4932) rss_mb | MB | 24 | 22.053 | 22.012 | 22.633 | 22.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_clean_modes.py (PID 4932) main thread run-queue wait | percent | 23 | 0.014 | 0.000 | 0.143 | 0.143 | 0.003313 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_clean_modes.py (PID 4932) vms_mb | MB | 24 | 28.059 | 27.984 | 28.508 | 28.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzfstne31.py (PID 4971) rss_mb | MB | 1 | 8.219 | 8.219 | 8.219 | 8.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzfstne31.py (PID 4971) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpv2pmbl1_.py (PID 5008) rss_mb | MB | 1 | 8.480 | 8.480 | 8.480 | 8.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpv2pmbl1_.py (PID 5008) vms_mb | MB | 1 | 13.086 | 13.086 | 13.086 | 13.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp5jdyfxwn.py (PID 5059) rss_mb | MB | 1 | 7.305 | 7.305 | 7.305 | 7.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp5jdyfxwn.py (PID 5059) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp_rqn2gh9.py (PID 5071) rss_mb | MB | 1 | 9.371 | 9.371 | 9.371 | 9.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp_rqn2gh9.py (PID 5071) vms_mb | MB | 1 | 13.250 | 13.250 | 13.250 | 13.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpb4pqogg6.py (PID 5082) rss_mb | MB | 1 | 1.078 | 1.078 | 1.078 | 1.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpb4pqogg6.py (PID 5082) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5126) CPU | percent | 1 | 1.984 | 1.984 | 1.984 | 1.984 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5126) rss_mb | MB | 2 | 12.387 | 12.387 | 12.387 | 12.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5126) main thread run-queue wait | percent | 1 | 0.019 | 0.019 | 0.019 | 0.019 | 0.000190 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5126) vms_mb | MB | 2 | 15.859 | 15.859 | 15.859 | 15.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpfhvk3e0k.py (PID 5144) rss_mb | MB | 1 | 8.652 | 8.652 | 8.652 | 8.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpfhvk3e0k.py (PID 5144) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2h06i5l8.py (PID 5181) rss_mb | MB | 1 | 7.117 | 7.117 | 7.117 | 7.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2h06i5l8.py (PID 5181) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5232) CPU | percent | 2 | 3.453 | 2.978 | 3.928 | 3.928 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5232) rss_mb | MB | 3 | 13.242 | 13.117 | 13.367 | 13.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5232) main thread run-queue wait | percent | 2 | 0.017 | 0.016 | 0.019 | 0.019 | 0.000352 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5232) vms_mb | MB | 3 | 17.219 | 17.148 | 17.254 | 17.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp3vnl8l7o.py (PID 5242) rss_mb | MB | 1 | 7.672 | 7.672 | 7.672 | 7.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp3vnl8l7o.py (PID 5242) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsq6vy_23.py (PID 5279) rss_mb | MB | 1 | 7.492 | 7.492 | 7.492 | 7.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsq6vy_23.py (PID 5279) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpi5dnr8vz.py (PID 5317) rss_mb | MB | 1 | 7.039 | 7.039 | 7.039 | 7.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpi5dnr8vz.py (PID 5317) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5339) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5339) rss_mb | MB | 3 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5339) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5339) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5340) CPU | percent | 2 | 2.977 | 2.976 | 2.978 | 2.978 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5340) rss_mb | MB | 3 | 13.060 | 12.977 | 13.102 | 13.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5340) main thread run-queue wait | percent | 2 | 0.018 | 0.017 | 0.020 | 0.020 | 0.000372 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5340) vms_mb | MB | 3 | 17.125 | 17.102 | 17.137 | 17.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpe402g__e.py (PID 5356) rss_mb | MB | 1 | 8.152 | 8.152 | 8.152 | 8.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpe402g__e.py (PID 5356) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpwtlqku8o.py (PID 5392) rss_mb | MB | 1 | 8.680 | 8.680 | 8.680 | 8.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpwtlqku8o.py (PID 5392) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpbjvtyi1u.py (PID 5429) rss_mb | MB | 1 | 7.734 | 7.734 | 7.734 | 7.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpbjvtyi1u.py (PID 5429) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_ref_token_stats.py (PID 5446) rss_mb | MB | 1 | 9.582 | 9.582 | 9.582 | 9.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_ref_token_stats.py (PID 5446) vms_mb | MB | 1 | 13.590 | 13.590 | 13.590 | 13.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_ref_token_stats.py (PID 5513) rss_mb | MB | 1 | 10.188 | 10.188 | 10.188 | 10.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_ref_token_stats.py (PID 5513) vms_mb | MB | 1 | 14.730 | 14.730 | 14.730 | 14.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_ref_token_stats.py (PID 5593) CPU | percent | 24 | 0.207 | 0.000 | 2.978 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_ref_token_stats.py (PID 5593) rss_mb | MB | 25 | 22.035 | 22.035 | 22.035 | 22.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_ref_token_stats.py (PID 5593) main thread run-queue wait | percent | 24 | 0.015 | 0.000 | 0.329 | 0.000 | 0.003634 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_ref_token_stats.py (PID 5593) vms_mb | MB | 25 | 28.195 | 28.195 | 28.195 | 28.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python3 (PID 5635) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python3 (PID 5635) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2pavyeuy.py (PID 5669) CPU | percent | 2 | 99.970 | 99.508 | 100.433 | 99.508 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2pavyeuy.py (PID 5669) rss_mb | MB | 3 | 8.266 | 8.266 | 8.266 | 8.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2pavyeuy.py (PID 5669) main thread run-queue wait | percent | 2 | 0.004 | 0.003 | 0.005 | 0.005 | 0.000083 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2pavyeuy.py (PID 5669) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpd78sjqn7.py (PID 5671) CPU | percent | 2 | 99.943 | 99.438 | 100.449 | 99.438 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpd78sjqn7.py (PID 5671) rss_mb | MB | 3 | 8.301 | 8.301 | 8.301 | 8.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpd78sjqn7.py (PID 5671) main thread run-queue wait | percent | 2 | 0.004 | 0.004 | 0.004 | 0.004 | 0.000080 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpd78sjqn7.py (PID 5671) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_token_stats0.py (PID 5730) rss_mb | MB | 1 | 18.543 | 18.543 | 18.543 | 18.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_token_stats0.py (PID 5730) vms_mb | MB | 1 | 24.047 | 24.047 | 24.047 | 24.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5774) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5774) rss_mb | MB | 5 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5774) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5774) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5775) CPU | percent | 4 | 0.494 | 0.000 | 0.995 | 0.995 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5775) rss_mb | MB | 5 | 12.836 | 12.836 | 12.836 | 12.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5775) main thread run-queue wait | percent | 4 | 0.005 | 0.000 | 0.013 | 0.013 | 0.000206 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5775) vms_mb | MB | 5 | 16.930 | 16.930 | 16.930 | 16.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpupiv3toa.py (PID 5802) rss_mb | MB | 1 | 8.566 | 8.566 | 8.566 | 8.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpupiv3toa.py (PID 5802) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpyjwiwy9k.py (PID 5813) CPU | percent | 2 | 99.814 | 99.249 | 100.379 | 100.379 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpyjwiwy9k.py (PID 5813) rss_mb | MB | 3 | 8.230 | 8.230 | 8.230 | 8.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpyjwiwy9k.py (PID 5813) main thread run-queue wait | percent | 2 | 0.003 | 0.003 | 0.003 | 0.003 | 0.000068 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpyjwiwy9k.py (PID 5813) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_brief_think.py (PID 5852) CPU | percent | 32 | 0.062 | 0.000 | 1.980 | 1.980 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_brief_think.py (PID 5852) rss_mb | MB | 33 | 21.821 | 21.668 | 21.887 | 21.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_brief_think.py (PID 5852) main thread run-queue wait | percent | 32 | 0.002 | 0.000 | 0.051 | 0.010 | 0.000615 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_brief_think.py (PID 5852) vms_mb | MB | 33 | 26.922 | 26.918 | 27.051 | 27.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python3 (PID 5889) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python3 (PID 5889) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_mech_probes1.py (PID 5954) CPU | percent | 4 | 0.248 | 0.000 | 0.993 | 0.993 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_mech_probes1.py (PID 5954) rss_mb | MB | 5 | 22.375 | 22.375 | 22.375 | 22.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_mech_probes1.py (PID 5954) main thread run-queue wait | percent | 4 | 0.081 | 0.000 | 0.322 | 0.322 | 0.003243 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_mech_probes1.py (PID 5954) vms_mb | MB | 5 | 28.077 | 28.051 | 28.184 | 28.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5970) rss_mb | MB | 1 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5970) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5971) rss_mb | MB | 1 | 7.348 | 7.348 | 7.348 | 7.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5971) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6013) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6013) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_states_s1_s2.py (PID 6043) CPU | percent | 12 | 4.790 | 0.000 | 43.573 | 43.573 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_states_s1_s2.py (PID 6043) rss_mb | MB | 13 | 168.040 | 13.738 | 1782.984 | 1782.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_states_s1_s2.py (PID 6043) main thread run-queue wait | percent | 12 | 0.072 | 0.000 | 0.550 | 0.002 | 0.008724 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_states_s1_s2.py (PID 6043) vms_mb | MB | 13 | 510.280 | 207.539 | 3907.703 | 3907.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6090) rss_mb | MB | 1 | 2.559 | 2.559 | 2.559 | 2.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6090) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6092) rss_mb | MB | 1 | 7.355 | 7.355 | 7.355 | 7.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6092) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_s2_heads.py (PID 6105) CPU | percent | 5 | 164.716 | 140.009 | 173.543 | 165.017 | 8.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_s2_heads.py (PID 6105) rss_mb | MB | 6 | 1369.230 | 83.066 | 1785.176 | 1785.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_s2_heads.py (PID 6105) main thread run-queue wait | percent | 5 | 50.785 | 36.315 | 59.678 | 59.678 | 2.555858 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_s2_heads.py (PID 6105) vms_mb | MB | 6 | 2813.268 | 1945.629 | 3021.996 | 3021.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_s1_and_vh10.py (PID 6147) CPU | percent | 11 | 168.211 | 131.582 | 176.049 | 173.080 | 18.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_s1_and_vh10.py (PID 6147) rss_mb | MB | 12 | 2167.268 | 1166.582 | 3155.895 | 3155.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_s1_and_vh10.py (PID 6147) main thread run-queue wait | percent | 11 | 54.400 | 34.049 | 76.358 | 56.256 | 6.040378 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — analyze_s1_and_vh10.py (PID 6147) vms_mb | MB | 12 | 4082.190 | 2919.965 | 5678.398 | 5678.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — probe_trace_and_steered_s2.py (PID 6206) CPU | percent | 6 | 6.447 | 0.000 | 38.685 | 0.000 | 0.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — probe_trace_and_steered_s2.py (PID 6206) rss_mb | MB | 7 | 31.919 | 13.387 | 35.008 | 35.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — probe_trace_and_steered_s2.py (PID 6206) main thread run-queue wait | percent | 6 | 1.194 | 0.000 | 7.074 | 0.000 | 0.072220 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — probe_trace_and_steered_s2.py (PID 6206) vms_mb | MB | 7 | 198.781 | 18.613 | 228.809 | 228.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — compare_steered_s2.py (PID 6236) CPU | percent | 9 | 171.993 | 168.771 | 174.757 | 168.771 | 15.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — compare_steered_s2.py (PID 6236) rss_mb | MB | 10 | 1686.938 | 1588.402 | 2515.035 | 1647.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — compare_steered_s2.py (PID 6236) main thread run-queue wait | percent | 9 | 60.899 | 50.502 | 71.034 | 56.198 | 5.519450 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — compare_steered_s2.py (PID 6236) vms_mb | MB | 10 | 3071.641 | 2979.484 | 3889.160 | 2991.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6277) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6277) rss_mb | MB | 11 | 2.891 | 2.891 | 2.891 | 2.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6277) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6277) vms_mb | MB | 11 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6278) CPU | percent | 10 | 173.758 | 170.953 | 177.424 | 174.016 | 17.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6278) rss_mb | MB | 11 | 1713.594 | 1587.789 | 1807.516 | 1807.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6278) main thread run-queue wait | percent | 10 | 59.016 | 49.136 | 69.911 | 60.335 | 5.951519 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6278) vms_mb | MB | 11 | 3912.571 | 2978.926 | 4688.941 | 4688.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6310) rss_mb | MB | 1 | 2.719 | 2.719 | 2.719 | 2.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6310) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6311) rss_mb | MB | 1 | 20.629 | 20.629 | 20.629 | 20.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6311) vms_mb | MB | 1 | 212.207 | 212.207 | 212.207 | 212.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6361) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6361) rss_mb | MB | 2 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6361) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6361) vms_mb | MB | 2 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6362) CPU | percent | 1 | 175.963 | 175.963 | 175.963 | 175.963 | 1.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6362) rss_mb | MB | 2 | 76.900 | 60.609 | 93.191 | 93.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6362) main thread run-queue wait | percent | 1 | 60.454 | 60.454 | 60.454 | 60.454 | 0.614978 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6362) vms_mb | MB | 2 | 1948.711 | 1946.227 | 1951.195 | 1951.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6384) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6384) rss_mb | MB | 6 | 2.645 | 2.645 | 2.645 | 2.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6384) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6384) vms_mb | MB | 6 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6385) CPU | percent | 5 | 173.320 | 172.941 | 174.011 | 173.683 | 8.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6385) rss_mb | MB | 6 | 150.408 | 101.773 | 187.785 | 162.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6385) main thread run-queue wait | percent | 5 | 60.011 | 52.408 | 75.007 | 75.007 | 3.019505 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6385) vms_mb | MB | 6 | 2061.370 | 2050.703 | 2066.703 | 2066.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6522) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6522) rss_mb | MB | 6 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6522) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6522) vms_mb | MB | 6 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6523) CPU | percent | 5 | 1.390 | 0.000 | 2.979 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6523) rss_mb | MB | 6 | 12.466 | 12.258 | 12.508 | 12.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6523) main thread run-queue wait | percent | 5 | 0.008 | 0.000 | 0.019 | 0.000 | 0.000401 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6523) vms_mb | MB | 6 | 15.903 | 15.887 | 15.906 | 15.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpf9i103in.py (PID 6553) rss_mb | MB | 1 | 8.535 | 8.535 | 8.535 | 8.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpf9i103in.py (PID 6553) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpfokpq098.py (PID 6590) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpfokpq098.py (PID 6590) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpiv4z2msk.py (PID 6626) rss_mb | MB | 1 | 8.566 | 8.566 | 8.566 | 8.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpiv4z2msk.py (PID 6626) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpgyug2oia.py (PID 6637) CPU | percent | 2 | 99.921 | 99.442 | 100.399 | 100.399 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpgyug2oia.py (PID 6637) rss_mb | MB | 3 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpgyug2oia.py (PID 6637) main thread run-queue wait | percent | 2 | 0.004 | 0.003 | 0.006 | 0.003 | 0.000082 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpgyug2oia.py (PID 6637) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6701) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6701) rss_mb | MB | 8 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6701) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6701) vms_mb | MB | 8 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6702) CPU | percent | 7 | 1.703 | 0.000 | 2.984 | 2.984 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6702) rss_mb | MB | 8 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6702) main thread run-queue wait | percent | 7 | 0.008 | 0.000 | 0.020 | 0.009 | 0.000560 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6702) vms_mb | MB | 8 | 15.877 | 15.871 | 15.887 | 15.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpiywuspr5.py (PID 6742) rss_mb | MB | 1 | 8.016 | 8.016 | 8.016 | 8.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpiywuspr5.py (PID 6742) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcjk965_2.py (PID 6753) CPU | percent | 2 | 100.448 | 100.423 | 100.473 | 100.473 | 2.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcjk965_2.py (PID 6753) rss_mb | MB | 3 | 8.406 | 8.406 | 8.406 | 8.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcjk965_2.py (PID 6753) main thread run-queue wait | percent | 2 | 0.004 | 0.004 | 0.004 | 0.004 | 0.000075 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcjk965_2.py (PID 6753) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2vjii5mk.py (PID 6782) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2vjii5mk.py (PID 6782) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp9smq7tmq.py (PID 6818) rss_mb | MB | 1 | 5.789 | 5.789 | 5.789 | 5.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp9smq7tmq.py (PID 6818) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp5ppti26m.py (PID 6856) rss_mb | MB | 1 | 7.086 | 7.086 | 7.086 | 7.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp5ppti26m.py (PID 6856) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_nodoc_counterfactual.py (PID 6958) CPU | percent | 48 | 0.435 | 0.000 | 3.977 | 0.000 | 0.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_nodoc_counterfactual.py (PID 6958) rss_mb | MB | 49 | 22.363 | 22.363 | 22.363 | 22.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_nodoc_counterfactual.py (PID 6958) main thread run-queue wait | percent | 48 | 0.007 | 0.000 | 0.120 | 0.000 | 0.003336 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — exp_nodoc_counterfactual.py (PID 6958) vms_mb | MB | 49 | 28.182 | 28.066 | 28.238 | 28.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp8aw49g11.py (PID 6991) rss_mb | MB | 1 | 7.293 | 7.293 | 7.293 | 7.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp8aw49g11.py (PID 6991) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmppq_z0x6y.py (PID 7029) rss_mb | MB | 1 | 4.750 | 4.750 | 4.750 | 4.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmppq_z0x6y.py (PID 7029) vms_mb | MB | 1 | 11.383 | 11.383 | 11.383 | 11.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpfh72jmwl.py (PID 7065) rss_mb | MB | 1 | 7.047 | 7.047 | 7.047 | 7.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpfh72jmwl.py (PID 7065) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsevskgq9.py (PID 7139) rss_mb | MB | 1 | 4.395 | 4.395 | 4.395 | 4.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsevskgq9.py (PID 7139) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmtoqs6jb.py (PID 7154) CPU | percent | 2 | 99.857 | 99.347 | 100.367 | 100.367 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmtoqs6jb.py (PID 7154) rss_mb | MB | 3 | 8.316 | 8.316 | 8.316 | 8.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmtoqs6jb.py (PID 7154) main thread run-queue wait | percent | 2 | 0.001 | 0.000 | 0.002 | 0.002 | 0.000026 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmtoqs6jb.py (PID 7154) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmphj57poie.py (PID 7155) CPU | percent | 2 | 100.385 | 100.304 | 100.466 | 100.466 | 2.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmphj57poie.py (PID 7155) rss_mb | MB | 3 | 8.348 | 8.348 | 8.348 | 8.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmphj57poie.py (PID 7155) main thread run-queue wait | percent | 2 | 0.005 | 0.003 | 0.007 | 0.003 | 0.000102 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmphj57poie.py (PID 7155) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp589dwvn4.py (PID 7179) rss_mb | MB | 1 | 7.672 | 7.672 | 7.672 | 7.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp589dwvn4.py (PID 7179) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpjwjuc178.py (PID 7192) CPU | percent | 2 | 99.781 | 99.324 | 100.238 | 99.324 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpjwjuc178.py (PID 7192) rss_mb | MB | 3 | 86.108 | 39.316 | 132.566 | 132.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpjwjuc178.py (PID 7192) main thread run-queue wait | percent | 2 | 0.002 | 0.002 | 0.003 | 0.002 | 0.000044 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpjwjuc178.py (PID 7192) vms_mb | MB | 3 | 97.875 | 46.262 | 149.250 | 149.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpz3d013eq.py (PID 7193) CPU | percent | 2 | 99.950 | 99.452 | 100.448 | 100.448 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpz3d013eq.py (PID 7193) rss_mb | MB | 3 | 81.238 | 38.738 | 122.988 | 122.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpz3d013eq.py (PID 7193) main thread run-queue wait | percent | 2 | 0.003 | 0.002 | 0.004 | 0.004 | 0.000059 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpz3d013eq.py (PID 7193) vms_mb | MB | 3 | 89.686 | 46.262 | 134.125 | 134.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp3e3t4_hq.py (PID 7219) rss_mb | MB | 1 | 8.551 | 8.551 | 8.551 | 8.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp3e3t4_hq.py (PID 7219) vms_mb | MB | 1 | 13.133 | 13.133 | 13.133 | 13.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp6blr16q3.py (PID 7222) CPU | percent | 2 | 99.982 | 99.509 | 100.456 | 99.509 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp6blr16q3.py (PID 7222) rss_mb | MB | 3 | 8.141 | 8.141 | 8.141 | 8.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp6blr16q3.py (PID 7222) main thread run-queue wait | percent | 2 | 0.004 | 0.003 | 0.005 | 0.005 | 0.000088 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp6blr16q3.py (PID 7222) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpz2pm1hwy.py (PID 7223) CPU | percent | 2 | 99.852 | 99.308 | 100.395 | 100.395 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpz2pm1hwy.py (PID 7223) rss_mb | MB | 3 | 8.363 | 8.363 | 8.363 | 8.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpz2pm1hwy.py (PID 7223) main thread run-queue wait | percent | 2 | 0.004 | 0.002 | 0.006 | 0.006 | 0.000078 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpz2pm1hwy.py (PID 7223) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpf7lqssjk.py (PID 7224) CPU | percent | 2 | 99.898 | 99.473 | 100.323 | 99.473 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpf7lqssjk.py (PID 7224) rss_mb | MB | 3 | 160.488 | 82.488 | 238.738 | 238.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpf7lqssjk.py (PID 7224) main thread run-queue wait | percent | 2 | 0.004 | 0.004 | 0.005 | 0.005 | 0.000082 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpf7lqssjk.py (PID 7224) vms_mb | MB | 3 | 167.016 | 88.211 | 245.312 | 245.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpdcg5ntz3.py (PID 7225) CPU | percent | 2 | 99.907 | 99.457 | 100.356 | 99.457 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpdcg5ntz3.py (PID 7225) rss_mb | MB | 3 | 156.322 | 81.113 | 232.863 | 232.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpdcg5ntz3.py (PID 7225) main thread run-queue wait | percent | 2 | 0.004 | 0.003 | 0.005 | 0.003 | 0.000080 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpdcg5ntz3.py (PID 7225) vms_mb | MB | 3 | 162.332 | 86.203 | 240.312 | 240.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp66ydzei5.py (PID 7245) CPU | percent | 2 | 99.923 | 99.426 | 100.420 | 100.420 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp66ydzei5.py (PID 7245) rss_mb | MB | 3 | 8.227 | 8.227 | 8.227 | 8.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp66ydzei5.py (PID 7245) main thread run-queue wait | percent | 2 | 0.009 | 0.003 | 0.014 | 0.014 | 0.000173 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp66ydzei5.py (PID 7245) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 7265) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 7265) rss_mb | MB | 4 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 7265) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 7265) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7266) CPU | percent | 3 | 2.645 | 1.983 | 2.976 | 2.976 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7266) rss_mb | MB | 4 | 13.016 | 12.891 | 13.141 | 13.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7266) main thread run-queue wait | percent | 3 | 0.019 | 0.013 | 0.028 | 0.017 | 0.000580 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7266) vms_mb | MB | 4 | 17.129 | 17.105 | 17.152 | 17.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmppsflqc1y.py (PID 7273) rss_mb | MB | 1 | 7.340 | 7.340 | 7.340 | 7.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmppsflqc1y.py (PID 7273) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpm8uxr22q.py (PID 7306) rss_mb | MB | 1 | 7.547 | 7.547 | 7.547 | 7.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpm8uxr22q.py (PID 7306) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4xk7wqya.py (PID 7342) rss_mb | MB | 1 | 4.383 | 4.383 | 4.383 | 4.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4xk7wqya.py (PID 7342) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmprrg9g35b.py (PID 7380) rss_mb | MB | 1 | 5.922 | 5.922 | 5.922 | 5.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmprrg9g35b.py (PID 7380) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 7444) CPU | percent | 72 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 7444) rss_mb | MB | 73 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 7444) main thread run-queue wait | percent | 72 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 7444) vms_mb | MB | 73 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7445) CPU | percent | 72 | 2.067 | 0.000 | 12.909 | 0.000 | 1.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7445) rss_mb | MB | 73 | 13.218 | 11.031 | 13.633 | 13.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7445) main thread run-queue wait | percent | 72 | 0.017 | 0.000 | 0.125 | 0.000 | 0.012351 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7445) vms_mb | MB | 73 | 17.427 | 15.273 | 17.832 | 17.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmplup77owl.py (PID 7513) rss_mb | MB | 1 | 7.484 | 7.484 | 7.484 | 7.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmplup77owl.py (PID 7513) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpdxe38_wo.py (PID 7543) rss_mb | MB | 1 | 9.766 | 9.766 | 9.766 | 9.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpdxe38_wo.py (PID 7543) vms_mb | MB | 1 | 14.578 | 14.578 | 14.578 | 14.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpuak_b2zy.py (PID 7579) rss_mb | MB | 1 | 8.613 | 8.613 | 8.613 | 8.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpuak_b2zy.py (PID 7579) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpojztj4ct.py (PID 7617) rss_mb | MB | 1 | 6.836 | 6.836 | 6.836 | 6.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpojztj4ct.py (PID 7617) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzxnr0eai.py (PID 7654) rss_mb | MB | 1 | 8.875 | 8.875 | 8.875 | 8.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzxnr0eai.py (PID 7654) vms_mb | MB | 1 | 13.129 | 13.129 | 13.129 | 13.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2omhmhah.py (PID 7691) rss_mb | MB | 1 | 7.547 | 7.547 | 7.547 | 7.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp2omhmhah.py (PID 7691) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7730) rss_mb | MB | 1 | 13.062 | 13.062 | 13.062 | 13.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 7730) vms_mb | MB | 1 | 17.406 | 17.406 | 17.406 | 17.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp3uw_t2nu.py (PID 7767) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp3uw_t2nu.py (PID 7767) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp882xkshq.py (PID 7804) rss_mb | MB | 1 | 7.371 | 7.371 | 7.371 | 7.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp882xkshq.py (PID 7804) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpood85am2.py (PID 7840) rss_mb | MB | 1 | 7.035 | 7.035 | 7.035 | 7.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpood85am2.py (PID 7840) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4pdif0ld.py (PID 7878) rss_mb | MB | 1 | 7.285 | 7.285 | 7.285 | 7.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4pdif0ld.py (PID 7878) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsovnsne5.py (PID 7916) rss_mb | MB | 1 | 6.922 | 6.922 | 6.922 | 6.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsovnsne5.py (PID 7916) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpyvkhsj1a.py (PID 7953) rss_mb | MB | 1 | 8.441 | 8.441 | 8.441 | 8.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpyvkhsj1a.py (PID 7953) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpi5b4q2u7.py (PID 7991) rss_mb | MB | 1 | 7.480 | 7.480 | 7.480 | 7.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpi5b4q2u7.py (PID 7991) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4rm24efu.py (PID 8027) rss_mb | MB | 1 | 4.668 | 4.668 | 4.668 | 4.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4rm24efu.py (PID 8027) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpknp1w9xi.py (PID 8065) rss_mb | MB | 1 | 4.320 | 4.320 | 4.320 | 4.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpknp1w9xi.py (PID 8065) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpp_j1ox1y.py (PID 8102) rss_mb | MB | 1 | 7.047 | 7.047 | 7.047 | 7.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpp_j1ox1y.py (PID 8102) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmphtjzhhxo.py (PID 8176) rss_mb | MB | 1 | 7.730 | 7.730 | 7.730 | 7.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmphtjzhhxo.py (PID 8176) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp62lmetta.py (PID 8250) rss_mb | MB | 1 | 5.414 | 5.414 | 5.414 | 5.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp62lmetta.py (PID 8250) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsw0wxf8_.py (PID 8287) rss_mb | MB | 1 | 4.414 | 4.414 | 4.414 | 4.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsw0wxf8_.py (PID 8287) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcpiqo0sg.py (PID 8322) rss_mb | MB | 1 | 0.141 | 0.141 | 0.141 | 0.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcpiqo0sg.py (PID 8322) vms_mb | MB | 1 | 6.734 | 6.734 | 6.734 | 6.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 8360) rss_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 8360) vms_mb | MB | 1 | 17.410 | 17.410 | 17.410 | 17.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmporv528bm.py (PID 8397) rss_mb | MB | 1 | 7.602 | 7.602 | 7.602 | 7.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmporv528bm.py (PID 8397) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsejaylo_.py (PID 8435) rss_mb | MB | 1 | 7.609 | 7.609 | 7.609 | 7.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsejaylo_.py (PID 8435) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpce81avgh.py (PID 8472) rss_mb | MB | 1 | 8.602 | 8.602 | 8.602 | 8.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpce81avgh.py (PID 8472) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpuwfgcv7j.py (PID 8503) rss_mb | MB | 1 | 9.277 | 9.277 | 9.277 | 9.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpuwfgcv7j.py (PID 8503) vms_mb | MB | 1 | 13.250 | 13.250 | 13.250 | 13.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmz0mlscy.py (PID 8504) rss_mb | MB | 1 | 9.301 | 9.301 | 9.301 | 9.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmz0mlscy.py (PID 8504) vms_mb | MB | 1 | 13.250 | 13.250 | 13.250 | 13.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp71zoagwq.py (PID 8537) rss_mb | MB | 1 | 7.285 | 7.285 | 7.285 | 7.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp71zoagwq.py (PID 8537) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpm5l1q599.py (PID 8575) rss_mb | MB | 1 | 7.105 | 7.105 | 7.105 | 7.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpm5l1q599.py (PID 8575) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmprf7ekz3k.py (PID 8611) rss_mb | MB | 1 | 8.051 | 8.051 | 8.051 | 8.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmprf7ekz3k.py (PID 8611) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp00dn_lz8.py (PID 8650) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp00dn_lz8.py (PID 8650) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp24rsutfm.py (PID 8688) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp24rsutfm.py (PID 8688) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzr6bdgw9.py (PID 8697) CPU | percent | 2 | 99.971 | 99.503 | 100.439 | 99.503 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzr6bdgw9.py (PID 8697) rss_mb | MB | 3 | 8.238 | 8.238 | 8.238 | 8.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzr6bdgw9.py (PID 8697) main thread run-queue wait | percent | 2 | 0.005 | 0.002 | 0.007 | 0.002 | 0.000093 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpzr6bdgw9.py (PID 8697) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp93__7vc7.py (PID 8698) CPU | percent | 2 | 99.926 | 99.458 | 100.395 | 99.458 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp93__7vc7.py (PID 8698) rss_mb | MB | 3 | 8.301 | 8.301 | 8.301 | 8.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp93__7vc7.py (PID 8698) main thread run-queue wait | percent | 2 | 0.003 | 0.002 | 0.003 | 0.003 | 0.000051 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp93__7vc7.py (PID 8698) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpknp8k8wq.py (PID 8767) rss_mb | MB | 1 | 7.047 | 7.047 | 7.047 | 7.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpknp8k8wq.py (PID 8767) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpow0nbdu3.py (PID 8805) rss_mb | MB | 1 | 8.039 | 8.039 | 8.039 | 8.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpow0nbdu3.py (PID 8805) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpyjgt8swf.py (PID 8844) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpyjgt8swf.py (PID 8844) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpa3_wxe6e.py (PID 8882) rss_mb | MB | 1 | 7.391 | 7.391 | 7.391 | 7.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpa3_wxe6e.py (PID 8882) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp_2jg31s5.py (PID 8921) rss_mb | MB | 1 | 7.496 | 7.496 | 7.496 | 7.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp_2jg31s5.py (PID 8921) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmsn3dg7p.py (PID 8958) rss_mb | MB | 1 | 5.602 | 5.602 | 5.602 | 5.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmsn3dg7p.py (PID 8958) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpgyp1e2yd.py (PID 8996) rss_mb | MB | 1 | 7.094 | 7.094 | 7.094 | 7.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpgyp1e2yd.py (PID 8996) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpl7_ny4x5.py (PID 9033) rss_mb | MB | 1 | 7.684 | 7.684 | 7.684 | 7.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpl7_ny4x5.py (PID 9033) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnx1p_qis.py (PID 9055) CPU | percent | 2 | 99.866 | 99.304 | 100.429 | 100.429 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnx1p_qis.py (PID 9055) rss_mb | MB | 3 | 75.556 | 28.348 | 122.223 | 122.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnx1p_qis.py (PID 9055) main thread run-queue wait | percent | 2 | 0.002 | 0.001 | 0.004 | 0.004 | 0.000045 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnx1p_qis.py (PID 9055) vms_mb | MB | 3 | 85.539 | 33.820 | 134.125 | 134.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmvwvigwd.py (PID 9056) CPU | percent | 2 | 99.920 | 99.442 | 100.398 | 100.398 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmvwvigwd.py (PID 9056) rss_mb | MB | 3 | 75.697 | 28.363 | 122.488 | 122.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmvwvigwd.py (PID 9056) main thread run-queue wait | percent | 2 | 0.002 | 0.001 | 0.003 | 0.001 | 0.000034 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpmvwvigwd.py (PID 9056) vms_mb | MB | 3 | 85.539 | 33.820 | 134.125 | 134.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpgot1atsh.py (PID 9073) rss_mb | MB | 1 | 7.461 | 7.461 | 7.461 | 7.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpgot1atsh.py (PID 9073) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4v9tw8b6.py (PID 9083) CPU | percent | 2 | 99.836 | 99.294 | 100.378 | 100.378 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4v9tw8b6.py (PID 9083) rss_mb | MB | 3 | 8.230 | 8.230 | 8.230 | 8.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4v9tw8b6.py (PID 9083) main thread run-queue wait | percent | 2 | 0.002 | 0.002 | 0.003 | 0.002 | 0.000049 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp4v9tw8b6.py (PID 9083) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp31asbbcd.py (PID 9084) CPU | percent | 2 | 99.890 | 99.414 | 100.367 | 99.414 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp31asbbcd.py (PID 9084) rss_mb | MB | 3 | 8.340 | 8.340 | 8.340 | 8.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp31asbbcd.py (PID 9084) main thread run-queue wait | percent | 2 | 0.020 | 0.019 | 0.022 | 0.019 | 0.000408 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp31asbbcd.py (PID 9084) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsjd8w7df.py (PID 9085) CPU | percent | 2 | 99.892 | 99.442 | 100.342 | 99.442 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsjd8w7df.py (PID 9085) rss_mb | MB | 3 | 141.738 | 66.363 | 215.488 | 215.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsjd8w7df.py (PID 9085) main thread run-queue wait | percent | 2 | 0.003 | 0.003 | 0.004 | 0.004 | 0.000065 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpsjd8w7df.py (PID 9085) vms_mb | MB | 3 | 147.732 | 72.309 | 221.406 | 221.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp1pu0b4_s.py (PID 9087) CPU | percent | 2 | 99.827 | 99.322 | 100.332 | 100.332 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp1pu0b4_s.py (PID 9087) rss_mb | MB | 3 | 138.891 | 62.266 | 214.516 | 214.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp1pu0b4_s.py (PID 9087) main thread run-queue wait | percent | 2 | 0.003 | 0.002 | 0.004 | 0.004 | 0.000062 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmp1pu0b4_s.py (PID 9087) vms_mb | MB | 3 | 145.133 | 67.512 | 221.406 | 221.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcoc08qg9.py (PID 9105) CPU | percent | 2 | 99.922 | 99.494 | 100.350 | 99.494 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcoc08qg9.py (PID 9105) rss_mb | MB | 3 | 8.316 | 8.316 | 8.316 | 8.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcoc08qg9.py (PID 9105) main thread run-queue wait | percent | 2 | 0.027 | 0.013 | 0.041 | 0.041 | 0.000543 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpcoc08qg9.py (PID 9105) vms_mb | MB | 3 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9127) CPU | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9127) rss_mb | MB | 32 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9127) main thread run-queue wait | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9127) vms_mb | MB | 32 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9128) CPU | percent | 31 | 0.288 | 0.000 | 2.975 | 1.985 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9128) rss_mb | MB | 32 | 22.330 | 22.250 | 22.461 | 22.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9128) main thread run-queue wait | percent | 31 | 0.008 | 0.000 | 0.186 | 0.028 | 0.002541 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9128) vms_mb | MB | 32 | 28.070 | 28.020 | 28.191 | 28.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpvrto5rze.py (PID 9180) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpvrto5rze.py (PID 9180) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9218) rss_mb | MB | 1 | 22.375 | 22.375 | 22.375 | 22.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9218) vms_mb | MB | 1 | 28.098 | 28.098 | 28.098 | 28.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpw8ms3n0b.py (PID 9251) rss_mb | MB | 1 | 7.602 | 7.602 | 7.602 | 7.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpw8ms3n0b.py (PID 9251) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9289) rss_mb | MB | 1 | 22.461 | 22.461 | 22.461 | 22.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9289) vms_mb | MB | 1 | 28.191 | 28.191 | 28.191 | 28.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9330) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9330) rss_mb | MB | 2 | 2.676 | 2.676 | 2.676 | 2.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9330) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9330) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9331) CPU | percent | 1 | 2.975 | 2.975 | 2.975 | 2.975 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9331) rss_mb | MB | 2 | 12.945 | 12.945 | 12.945 | 12.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9331) main thread run-queue wait | percent | 1 | 0.020 | 0.020 | 0.020 | 0.020 | 0.000207 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9331) vms_mb | MB | 2 | 17.066 | 17.066 | 17.066 | 17.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnzu79cwj.py (PID 9389) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tmpnzu79cwj.py (PID 9389) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9434) rss_mb | MB | 1 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9434) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9435) rss_mb | MB | 1 | 13.582 | 13.582 | 13.582 | 13.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9435) vms_mb | MB | 1 | 207.277 | 207.277 | 207.277 | 207.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_full_atlas.py (PID 9535) CPU | percent | 6 | 2.485 | 0.000 | 14.910 | 0.000 | 0.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_full_atlas.py (PID 9535) rss_mb | MB | 7 | 95.590 | 65.312 | 100.637 | 100.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_full_atlas.py (PID 9535) main thread run-queue wait | percent | 6 | 0.075 | 0.000 | 0.333 | 0.000 | 0.004564 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — capture_full_atlas.py (PID 9535) vms_mb | MB | 7 | 289.948 | 259.305 | 295.055 | 295.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9549) CPU | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9549) rss_mb | MB | 18 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9549) main thread run-queue wait | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9549) vms_mb | MB | 18 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9550) CPU | percent | 17 | 1.637 | 0.000 | 25.842 | 0.000 | 0.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9550) rss_mb | MB | 18 | 98.328 | 56.152 | 100.809 | 100.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9550) main thread run-queue wait | percent | 17 | 0.334 | 0.000 | 4.275 | 0.000 | 0.057143 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9550) vms_mb | MB | 18 | 292.797 | 249.902 | 295.320 | 295.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — consolidate_and_analyze_atlas.py (PID 9595) CPU | percent | 119 | 166.597 | 76.436 | 183.864 | 180.329 | 199.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — consolidate_and_analyze_atlas.py (PID 9595) rss_mb | MB | 120 | 1996.653 | 24.375 | 2123.191 | 1976.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — consolidate_and_analyze_atlas.py (PID 9595) main thread run-queue wait | percent | 119 | 46.139 | 0.036 | 71.503 | 48.218 | 55.305960 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — consolidate_and_analyze_atlas.py (PID 9595) vms_mb | MB | 120 | 3365.758 | 216.207 | 3493.008 | 3345.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — consolidate_and_analyze_atlas.py (PID 9696) CPU | percent | 118 | 166.014 | 75.460 | 176.246 | 161.888 | 197.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — consolidate_and_analyze_atlas.py (PID 9696) rss_mb | MB | 119 | 1994.813 | 50.867 | 2123.438 | 2025.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — consolidate_and_analyze_atlas.py (PID 9696) main thread run-queue wait | percent | 118 | 46.282 | 0.121 | 62.247 | 44.111 | 55.016161 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — consolidate_and_analyze_atlas.py (PID 9696) vms_mb | MB | 119 | 3378.090 | 1909.125 | 3493.004 | 3395.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 9747) CPU | percent | 2 | 112.466 | 64.506 | 160.426 | 160.426 | 2.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 9747) rss_mb | MB | 3 | 1408.882 | 788.641 | 1742.930 | 1742.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 9747) main thread run-queue wait | percent | 2 | 34.226 | 0.962 | 67.489 | 67.489 | 0.691206 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 9747) vms_mb | MB | 3 | 3043.779 | 2923.613 | 3121.336 | 3121.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9765) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9765) rss_mb | MB | 4 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9765) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9765) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9766) CPU | percent | 3 | 111.940 | 64.466 | 156.047 | 115.308 | 3.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9766) rss_mb | MB | 4 | 1863.062 | 346.891 | 3718.250 | 3718.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9766) main thread run-queue wait | percent | 3 | 20.827 | 0.079 | 44.727 | 17.676 | 0.628618 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9766) vms_mb | MB | 4 | 3955.185 | 2923.816 | 6759.688 | 6759.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9822) rss_mb | MB | 1 | 2.684 | 2.684 | 2.684 | 2.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9822) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9823) rss_mb | MB | 1 | 22.129 | 22.129 | 22.129 | 22.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9823) vms_mb | MB | 1 | 28.047 | 28.047 | 28.047 | 28.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9852) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9852) rss_mb | MB | 2 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9852) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9852) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9853) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9853) rss_mb | MB | 2 | 22.289 | 22.289 | 22.289 | 22.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9853) main thread run-queue wait | percent | 1 | 0.501 | 0.501 | 0.501 | 0.501 | 0.005066 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9853) vms_mb | MB | 2 | 28.027 | 28.027 | 28.027 | 28.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9886) rss_mb | MB | 1 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9886) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9887) rss_mb | MB | 1 | 82.488 | 82.488 | 82.488 | 82.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9887) vms_mb | MB | 1 | 1933.312 | 1933.312 | 1933.312 | 1933.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gate_pulse_geometry.py (PID 9919) CPU | percent | 1 | 171.955 | 171.955 | 171.955 | 171.955 | 1.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gate_pulse_geometry.py (PID 9919) rss_mb | MB | 2 | 106.041 | 95.121 | 116.961 | 116.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gate_pulse_geometry.py (PID 9919) main thread run-queue wait | percent | 1 | 64.224 | 64.224 | 64.224 | 64.224 | 0.646141 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — check_gate_pulse_geometry.py (PID 9919) vms_mb | MB | 2 | 1989.648 | 1988.613 | 1990.684 | 1990.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9938) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9938) rss_mb | MB | 9 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9938) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9938) vms_mb | MB | 9 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9939) CPU | percent | 8 | 172.242 | 167.911 | 175.146 | 175.146 | 13.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9939) rss_mb | MB | 9 | 2562.643 | 2300.699 | 2664.387 | 2664.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9939) main thread run-queue wait | percent | 8 | 57.671 | 46.999 | 79.917 | 72.933 | 4.644742 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9939) vms_mb | MB | 9 | 3978.486 | 3895.207 | 4064.586 | 4064.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9979) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9979) rss_mb | MB | 12 | 2.641 | 2.641 | 2.641 | 2.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9979) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 9979) vms_mb | MB | 12 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9980) CPU | percent | 11 | 172.657 | 165.775 | 176.837 | 174.915 | 19.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9980) rss_mb | MB | 12 | 2574.484 | 2302.680 | 2738.105 | 2697.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9980) main thread run-queue wait | percent | 11 | 52.695 | 38.117 | 64.474 | 64.474 | 5.837446 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 9980) vms_mb | MB | 12 | 4005.055 | 3828.000 | 4167.395 | 4043.355 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 CPU | percent | 13574 | 41.876 | 0.000 | 211.491 | 0.000 | 5717.505946 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 13574 | 2.093 | 0.000 | 50.666 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 13574 | 2.769 | 0.000 | 73.214 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_full_pct | percent of wall time stalled | 13574 | 0.010 | 0.000 | 47.531 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_some_pct | percent of wall time stalled | 13574 | 0.010 | 0.000 | 47.535 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io read MB/s | MB/s | 13574 | 0.012 | 0.000 | 29.740 | 0.000 | 170.816406 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io write MB/s | MB/s | 13574 | 0.060 | 0.000 | 98.359 | 0.000 | 815.800781 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory | MB | 13575 | 1220.324 | 27.227 | 4001.336 | 426.453 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_full_pct | percent of wall time stalled | 13574 | 0.001 | 0.000 | 7.412 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_some_pct | percent of wall time stalled | 13574 | 0.001 | 0.000 | 7.412 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net rx MB/s | MB/s | 13574 | 0.002 | 0.000 | 12.775 | 0.000 | 26.256117 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net tx MB/s | MB/s | 13574 | 0.000 | 0.000 | 0.070 | 0.000 | 0.509228 MB | n/a |
| workload total CPU | percent | 13575 | 3.608 | 1.381 | 164.168 | 1.800 | 493.324439 CPU seconds | n/a |
| workload total memory | MB | 13576 | 8921.623 | 8224.027 | 9542.672 | 9505.715 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
