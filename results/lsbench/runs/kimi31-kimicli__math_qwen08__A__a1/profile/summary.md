# agprof summary

- Duration: **4711.339 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **456 calls**, 404 succeeded, 52 failed, 0 interrupted, n/a reported retries, 2900.044 s total wait
- Tools: **130/130 completed**, 16 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **469411** at 1.966 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 4702456.573 / 4702456.573 ms |
| LLM latency p50 / p95 | 6181.524 / 10650.100 ms |
| LLM TTFT p50 / p95 | 5299.901 / 10253.656 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 456 total, 404 succeeded, 52 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- kimi: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 96/96 | 81 | 15 | 0 | n/a | n/a |
| Glob | 1/1 | 1 | 0 | 0 | n/a | n/a |
| Grep | 7/7 | 6 | 1 | 0 | n/a | n/a |
| Read | 18/18 | 18 | 0 | 0 | n/a | n/a |
| TaskList | 1/1 | 1 | 0 | 0 | n/a | n/a |
| TodoList | 6/6 | 6 | 0 | 0 | n/a | n/a |
| Write | 1/1 | 1 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 9.243% | 173.261% | 436.350 s | 6409.037 MB | 7015.574 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bash | 15583 | sandbox_agent_lsb-kimi_0000_0000 | 4666 | 50.254% | 116.016% | 2363.210 s | 148.667 MB | 173.906 MB | 946.817 MB | 986.492 MB | n/a MB | n/a MB |
| python | 15197 |  | 4675 | 5.892% | 170.683% | 278.000 s | 3661.281 MB | 4324.965 MB | 18350.126 MB | 23906.797 MB | 8.644531 MB | 1852.140625 MB |
| kimi_seq.sh | 15185 |  | 4675 | 0.000% | 0.000% | 0.000 s | 3.344 MB | 3.344 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| lsb_grid_worker | 15189 |  | 4675 | 0.000% | 0.000% | 0.000 s | 3.328 MB | 3.328 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 15239 |  | 4675 | 3.068% | 50.419% | 144.820 s | 2337.347 MB | 2337.582 MB | 21236.570 MB | 21236.664 MB | 0.000000 MB | 0.027344 MB |
| vllm | 15202 |  | 4675 | 0.282% | 6.927% | 13.330 s | 1776.011 MB | 1776.105 MB | 11014.718 MB | 11016.797 MB | 0.000000 MB | 0.050781 MB |
| tail | 15490 | sandbox_agent_lsb-kimi_0000_0000 | 4666 | 0.002% | 0.995% | 0.110 s | 1.543 MB | 1.543 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 15238 |  | 4675 | 0.000% | 0.000% | 0.000 s | 12.336 MB | 12.336 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python3 | 15589 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 98.891% | 98.891% | 1.000 s | 52.229 MB | 78.980 MB | 64.104 MB | 94.188 MB | n/a MB | n/a MB |
| docker-init | 15458 | sandbox_agent_lsb-kimi_0000_0000 | 4666 | 0.002% | 0.995% | 0.110 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| MainThread | 15597 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 237.055 MB | 237.055 MB | 1644.375 MB | 1644.375 MB | n/a MB | n/a MB |
| MainThread | 15614 | sandbox_agent_lsb-kimi_0000_0000 | 347 | 3.641% | 67.568% | 12.690 s | 388.615 MB | 416.297 MB | 10146.010 MB | 10218.258 MB | n/a MB | n/a MB |
| MainThread | 15646 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 199.996 MB | 199.996 MB | 1617.457 MB | 1617.457 MB | n/a MB | n/a MB |
| bash | 15697 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.609 MB | 2.609 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp | 15698 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 75.558% | 75.558% | 0.760 s | 35.250 MB | 61.555 MB | 44.576 MB | 75.875 MB | n/a MB | n/a MB |
| python3 | 15717 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.777 MB | 18.777 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| sh | 15716 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 15725 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| bash | 15754 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.676 MB | 2.676 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 15755 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 78.537% | 78.537% | 0.790 s | 43.623 MB | 64.664 MB | 55.912 MB | 79.770 MB | n/a MB | n/a MB |
| bash | 15901 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.820 MB | 2.820 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 15902 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 24.121 MB | 24.121 MB | 30.242 MB | 30.242 MB | n/a MB | n/a MB |
| python3 | 15973 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.004 MB | 21.004 MB | 25.836 MB | 25.836 MB | n/a MB | n/a MB |
| sh | 15972 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 15979 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 15980 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.789 MB | 21.789 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| bash | 15981 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 15982 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.250 MB | 50.250 MB | 57.008 MB | 57.008 MB | n/a MB | n/a MB |
| sh | 15988 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 15989 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.613 MB | 9.613 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| bash | 16008 | sandbox_agent_lsb-kimi_0000_0000 | 24 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 16009 | sandbox_agent_lsb-kimi_0000_0000 | 24 | 2.676% | 61.544% | 0.620 s | 64.884 MB | 66.363 MB | 79.499 MB | 81.172 MB | n/a MB | n/a MB |
| sh | 16022 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16023 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.352 MB | 18.352 MB | 24.340 MB | 24.340 MB | n/a MB | n/a MB |
| bash | 16037 | sandbox_agent_lsb-kimi_0000_0000 | 71 | 0.000% | 0.000% | 0.000 s | 2.746 MB | 2.746 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 16038 | sandbox_agent_lsb-kimi_0000_0000 | 71 | 0.893% | 62.492% | 0.630 s | 66.032 MB | 66.531 MB | 80.589 MB | 81.152 MB | n/a MB | n/a MB |
| bash | 16080 | sandbox_agent_lsb-kimi_0000_0000 | 73 | 0.000% | 0.000% | 0.000 s | 2.672 MB | 2.672 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 16081 | sandbox_agent_lsb-kimi_0000_0000 | 73 | 0.992% | 57.526% | 0.720 s | 67.184 MB | 68.781 MB | 81.712 MB | 83.273 MB | n/a MB | n/a MB |
| python | 16137 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 11.929% | 23.858% | 0.240 s | 59.708 MB | 66.305 MB | 71.704 MB | 80.098 MB | n/a MB | n/a MB |
| bash | 16136 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 16147 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.395 MB | 7.395 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 16146 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 16156 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 6.522% | 32.799% | 0.460 s | 65.073 MB | 68.844 MB | 78.661 MB | 83.223 MB | n/a MB | n/a MB |
| bash | 16155 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.715 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 16175 | sandbox_agent_lsb-kimi_0000_0000 | 62 | 6.707% | 70.498% | 4.120 s | 387.025 MB | 397.344 MB | 9932.432 MB | 10210.938 MB | n/a MB | n/a MB |
| MainThread | 16217 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 253.355 MB | 253.355 MB | 1648.871 MB | 1648.871 MB | n/a MB | n/a MB |
| sh | 16318 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16319 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.297 MB | 19.297 MB | 24.805 MB | 24.805 MB | n/a MB | n/a MB |
| python | 16321 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 2.978% | 12.890% | 0.210 s | 65.558 MB | 67.789 MB | 79.706 MB | 82.543 MB | n/a MB | n/a MB |
| bash | 16320 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.594 MB | 2.594 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 16344 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.707 MB | 17.707 MB | 23.184 MB | 23.184 MB | n/a MB | n/a MB |
| sh | 16343 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 16358 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.758 MB | 2.758 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 16359 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 19.339% | 34.710% | 0.390 s | 59.435 MB | 67.332 MB | 72.255 MB | 82.590 MB | n/a MB | n/a MB |
| sh | 16367 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16368 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.586 MB | 14.586 MB | 20.082 MB | 20.082 MB | n/a MB | n/a MB |
| MainThread | 16385 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.712% | 91.471% | 2.980 s | 352.181 MB | 385.660 MB | 8956.496 MB | 10210.887 MB | n/a MB | n/a MB |
| sh | 16409 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16410 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.180 MB | 10.180 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 16414 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.434 MB | 229.434 MB | 1631.953 MB | 1631.953 MB | n/a MB | n/a MB |
| python | 16429 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 28.279% | 47.625% | 0.570 s | 58.422 MB | 68.051 MB | 70.997 MB | 82.547 MB | n/a MB | n/a MB |
| bash | 16428 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.730 MB | 2.730 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 16443 | sandbox_agent_lsb-kimi_0000_0000 | 25 | 14.067% | 87.384% | 3.400 s | 369.542 MB | 389.062 MB | 9510.173 MB | 10210.488 MB | n/a MB | n/a MB |
| python3 | 16467 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.594 MB | 8.594 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 16466 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi | 16469 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.423% | 66.423% | 0.670 s | 120.936 MB | 241.250 MB | 901.578 MB | 1639.855 MB | n/a MB | n/a MB |
| bash | 16487 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.766 MB | 2.766 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 16488 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 34.338% | 34.338% | 0.350 s | 55.539 MB | 66.879 MB | 67.543 MB | 82.094 MB | n/a MB | n/a MB |
| python | 16506 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 73.413% | 73.413% | 0.740 s | 36.010 MB | 64.176 MB | 45.902 MB | 78.754 MB | n/a MB | n/a MB |
| bash | 16505 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.719 MB | 2.719 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 16509 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.414 MB | 21.414 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| sh | 16508 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi-code | 16518 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 14.257% | 62.537% | 2.010 s | 376.337 MB | 393.586 MB | 9619.811 MB | 10194.379 MB | n/a MB | n/a MB |
| python3 | 16547 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.082 MB | 10.082 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 16546 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 16539 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.595% | 64.595% | 0.650 s | 204.275 MB | 262.859 MB | 1479.889 MB | 1658.043 MB | n/a MB | n/a MB |
| bash | 16567 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.754 MB | 2.754 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 16568 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.521% | 62.521% | 0.630 s | 49.746 MB | 66.285 MB | 61.379 MB | 80.121 MB | n/a MB | n/a MB |
| MainThread | 16581 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 14.869% | 64.642% | 2.720 s | 369.473 MB | 384.895 MB | 9747.422 MB | 10211.082 MB | n/a MB | n/a MB |
| MainThread | 16600 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.104% | 59.104% | 0.600 s | 216.400 MB | 263.398 MB | 1618.881 MB | 1658.789 MB | n/a MB | n/a MB |
| sh | 16612 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16613 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.504 MB | 9.504 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| python | 16624 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 19.846% | 44.672% | 0.600 s | 61.014 MB | 68.496 MB | 73.939 MB | 83.211 MB | n/a MB | n/a MB |
| bash | 16623 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.914 MB | 2.914 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 16639 | sandbox_agent_lsb-kimi_0000_0000 | 114 | 4.767% | 71.281% | 5.440 s | 380.877 MB | 388.852 MB | 10055.591 MB | 10211.762 MB | n/a MB | n/a MB |
| MainThread | 16668 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 234.953 MB | 234.953 MB | 1636.078 MB | 1636.078 MB | n/a MB | n/a MB |
| bash | 16682 | sandbox_agent_lsb-kimi_0000_0000 | 81 | 0.000% | 0.000% | 0.000 s | 2.699 MB | 2.699 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 16683 | sandbox_agent_lsb-kimi_0000_0000 | 81 | 1.068% | 62.608% | 0.860 s | 66.276 MB | 67.121 MB | 80.618 MB | 81.410 MB | n/a MB | n/a MB |
| python | 16699 | sandbox_agent_lsb-kimi_0000_0000 | 85 | 169.395% | 180.063% | 144.200 s | 433.253 MB | 560.781 MB | 824.421 MB | 872.035 MB | n/a MB | n/a MB |
| bash | 16698 | sandbox_agent_lsb-kimi_0000_0000 | 85 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 16712 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16713 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.566 MB | 4.566 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| MainThread | 16732 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 18.970% | 66.509% | 2.870 s | 370.543 MB | 393.406 MB | 9137.760 MB | 10207.664 MB | n/a MB | n/a MB |
| MainThread | 16758 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 73.549% | 73.549% | 0.740 s | 221.734 MB | 295.625 MB | 1497.174 MB | 1690.035 MB | n/a MB | n/a MB |
| python | 16778 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 7.193% | 28.772% | 0.290 s | 62.280 MB | 66.367 MB | 75.058 MB | 80.152 MB | n/a MB | n/a MB |
| bash | 16777 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.703 MB | 2.703 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 16789 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 17.887% | 89.501% | 2.700 s | 355.934 MB | 387.488 MB | 9085.873 MB | 10199.785 MB | n/a MB | n/a MB |
| sh | 16818 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16819 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.270 MB | 7.270 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 16808 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.514% | 58.514% | 0.590 s | 252.143 MB | 295.199 MB | 1655.148 MB | 1689.566 MB | n/a MB | n/a MB |
| MainThread | 16836 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 35.070% | 90.492% | 2.470 s | 324.717 MB | 387.562 MB | 8009.741 MB | 10197.621 MB | n/a MB | n/a MB |
| MainThread | 16855 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.550% | 62.550% | 0.630 s | 249.822 MB | 295.234 MB | 1654.365 MB | 1689.988 MB | n/a MB | n/a MB |
| python3 | 16866 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.008 MB | 7.008 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 16865 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 16883 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 40.461% | 87.394% | 2.850 s | 334.641 MB | 390.711 MB | 8022.264 MB | 10207.988 MB | n/a MB | n/a MB |
| MainThread | 16903 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.598% | 57.598% | 0.580 s | 251.623 MB | 295.223 MB | 1654.604 MB | 1689.977 MB | n/a MB | n/a MB |
| MainThread | 16931 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 38.522% | 67.652% | 2.370 s | 341.301 MB | 383.504 MB | 7761.634 MB | 10203.516 MB | n/a MB | n/a MB |
| sh | 16948 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16949 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.832 MB | 9.832 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 16952 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.379% | 61.379% | 0.680 s | 245.881 MB | 297.562 MB | 1653.355 MB | 1692.238 MB | n/a MB | n/a MB |
| sh | 16988 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 16989 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.164 MB | 10.164 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 16993 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 30.060% | 70.231% | 2.120 s | 352.614 MB | 386.629 MB | 8074.957 MB | 10207.277 MB | n/a MB | n/a MB |
| MainThread | 17017 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 198.480 MB | 198.480 MB | 1617.203 MB | 1617.203 MB | n/a MB | n/a MB |
| MainThread | 17042 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 35.953% | 64.595% | 1.810 s | 345.082 MB | 371.742 MB | 8760.956 MB | 10202.613 MB | n/a MB | n/a MB |
| python3 | 17064 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.551 MB | 9.551 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| sh | 17063 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 17067 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 195.195 MB | 195.195 MB | 1614.973 MB | 1614.973 MB | n/a MB | n/a MB |
| MainThread | 17087 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.331% | 89.073% | 2.630 s | 324.373 MB | 378.852 MB | 7702.249 MB | 10205.348 MB | n/a MB | n/a MB |
| MainThread | 17244 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.605% | 61.605% | 0.620 s | 233.033 MB | 278.551 MB | 1633.760 MB | 1673.547 MB | n/a MB | n/a MB |
| MainThread | 17270 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 33.531% | 85.412% | 2.700 s | 335.843 MB | 389.824 MB | 8266.629 MB | 10207.680 MB | n/a MB | n/a MB |
| MainThread | 17289 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.547% | 60.547% | 0.610 s | 255.346 MB | 296.816 MB | 1672.869 MB | 1723.250 MB | n/a MB | n/a MB |
| MainThread | 17317 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 35.085% | 70.554% | 2.120 s | 346.134 MB | 379.984 MB | 7772.130 MB | 10207.594 MB | n/a MB | n/a MB |
| MainThread | 17345 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 287.402 MB | 287.402 MB | 1682.531 MB | 1682.531 MB | n/a MB | n/a MB |
| MainThread | 17364 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 32.797% | 68.590% | 1.980 s | 350.713 MB | 384.980 MB | 8942.710 MB | 10203.426 MB | n/a MB | n/a MB |
| MainThread | 17393 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 208.703 MB | 208.703 MB | 1619.711 MB | 1619.711 MB | n/a MB | n/a MB |
| MainThread | 17410 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 38.433% | 69.581% | 2.320 s | 336.367 MB | 379.348 MB | 7762.429 MB | 10202.430 MB | n/a MB | n/a MB |
| sh | 17427 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 17429 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.585% | 64.585% | 0.650 s | 180.611 MB | 255.180 MB | 1467.264 MB | 1650.832 MB | n/a MB | n/a MB |
| python3 | 17451 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.367 MB | 7.367 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 17450 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 17455 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 17.740% | 68.518% | 2.700 s | 366.385 MB | 389.488 MB | 9134.844 MB | 10206.590 MB | n/a MB | n/a MB |
| MainThread | 17474 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.173% | 63.173% | 0.640 s | 206.303 MB | 259.527 MB | 1482.291 MB | 1655.344 MB | n/a MB | n/a MB |
| python | 17500 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 45.000 MB | 45.000 MB | 53.383 MB | 53.383 MB | n/a MB | n/a MB |
| bash | 17499 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 17512 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 17.610% | 60.552% | 2.130 s | 368.131 MB | 385.027 MB | 9537.778 MB | 10204.402 MB | n/a MB | n/a MB |
| MainThread | 17538 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 208.516 MB | 208.516 MB | 1619.469 MB | 1619.469 MB | n/a MB | n/a MB |
| python | 17555 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 31.705% | 31.705% | 0.320 s | 54.865 MB | 65.840 MB | 66.475 MB | 80.133 MB | n/a MB | n/a MB |
| bash | 17554 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 17557 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.469 MB | 21.469 MB | 26.980 MB | 26.980 MB | n/a MB | n/a MB |
| sh | 17556 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 17569 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.165% | 83.401% | 2.700 s | 359.591 MB | 390.117 MB | 9046.551 MB | 10208.004 MB | n/a MB | n/a MB |
| MainThread | 17588 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.156 MB | 229.156 MB | 1632.219 MB | 1632.219 MB | n/a MB | n/a MB |
| MainThread | 17616 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 26.520% | 72.443% | 3.470 s | 356.789 MB | 384.766 MB | 8983.362 MB | 10210.125 MB | n/a MB | n/a MB |
| python3 | 17634 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.617 MB | 8.617 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 17635 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.564% | 54.564% | 0.550 s | 130.146 MB | 228.898 MB | 1143.586 MB | 1631.359 MB | n/a MB | n/a MB |
| sh | 17633 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 17664 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 18.691% | 65.612% | 2.070 s | 361.348 MB | 391.023 MB | 8781.107 MB | 10205.137 MB | n/a MB | n/a MB |
| MainThread | 17692 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 294.965 MB | 294.965 MB | 1689.691 MB | 1689.691 MB | n/a MB | n/a MB |
| MainThread | 17711 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 28.200% | 71.632% | 2.270 s | 351.599 MB | 385.848 MB | 8309.882 MB | 10206.043 MB | n/a MB | n/a MB |
| MainThread | 17739 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 267.926 MB | 267.926 MB | 1663.398 MB | 1663.398 MB | n/a MB | n/a MB |
| MainThread | 17758 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 18.284% | 63.601% | 1.840 s | 367.663 MB | 385.902 MB | 9418.665 MB | 10203.469 MB | n/a MB | n/a MB |
| MainThread | 17786 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.520 MB | 229.520 MB | 1631.961 MB | 1631.961 MB | n/a MB | n/a MB |
| MainThread | 17803 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 18.622% | 62.786% | 2.070 s | 365.065 MB | 387.527 MB | 9481.350 MB | 10208.191 MB | n/a MB | n/a MB |
| MainThread | 17824 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.596% | 57.596% | 0.580 s | 228.773 MB | 271.176 MB | 1630.162 MB | 1666.602 MB | n/a MB | n/a MB |
| MainThread | 17852 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 19.573% | 62.596% | 1.970 s | 368.436 MB | 387.684 MB | 9419.487 MB | 10207.727 MB | n/a MB | n/a MB |
| MainThread | 17873 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.552% | 59.552% | 0.600 s | 231.336 MB | 273.074 MB | 1631.910 MB | 1668.848 MB | n/a MB | n/a MB |
| MainThread | 17901 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 24.211% | 88.477% | 2.680 s | 357.591 MB | 393.805 MB | 8772.049 MB | 10211.277 MB | n/a MB | n/a MB |
| python3 | 17937 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.832 MB | 6.832 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 17926 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.604% | 55.604% | 0.560 s | 216.055 MB | 262.762 MB | 1618.510 MB | 1658.297 MB | n/a MB | n/a MB |
| sh | 17936 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 17952 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.563% | 79.375% | 2.610 s | 354.869 MB | 388.898 MB | 8755.182 MB | 10208.461 MB | n/a MB | n/a MB |
| MainThread | 17975 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.429% | 66.429% | 0.670 s | 246.594 MB | 299.324 MB | 1669.387 MB | 1724.551 MB | n/a MB | n/a MB |
| python3 | 17986 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.391 MB | 7.391 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 17985 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 18002 | sandbox_agent_lsb-kimi_0000_0000 | 25 | 10.519% | 70.615% | 2.540 s | 382.877 MB | 396.660 MB | 9860.375 MB | 10211.000 MB | n/a MB | n/a MB |
| MainThread | 18030 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 179.883 MB | 179.883 MB | 1591.223 MB | 1591.223 MB | n/a MB | n/a MB |
| bash | 18047 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.898 MB | 2.898 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 18048 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.328 MB | 19.328 MB | 211.684 MB | 211.684 MB | n/a MB | n/a MB |
| kimi-code | 18065 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 17.367% | 55.618% | 1.930 s | 370.021 MB | 389.160 MB | 9487.199 MB | 10208.152 MB | n/a MB | n/a MB |
| python3 | 18097 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.934 MB | 6.934 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 18086 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.723% | 61.723% | 0.630 s | 244.701 MB | 294.383 MB | 1652.061 MB | 1689.148 MB | n/a MB | n/a MB |
| sh | 18096 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 18114 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.332% | 65.583% | 2.140 s | 369.523 MB | 391.617 MB | 9481.148 MB | 10209.211 MB | n/a MB | n/a MB |
| MainThread | 18133 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.552% | 64.552% | 0.650 s | 220.332 MB | 265.344 MB | 1625.027 MB | 1660.082 MB | n/a MB | n/a MB |
| MainThread | 18163 | sandbox_agent_lsb-kimi_0000_0000 | 40 | 9.814% | 90.007% | 3.860 s | 380.292 MB | 391.336 MB | 9784.401 MB | 10214.781 MB | n/a MB | n/a MB |
| MainThread | 18191 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 259.105 MB | 259.105 MB | 1655.316 MB | 1655.316 MB | n/a MB | n/a MB |
| sh | 18205 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18206 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.656 MB | 21.656 MB | 26.723 MB | 26.723 MB | n/a MB | n/a MB |
| sh | 18231 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18232 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.578 MB | 21.578 MB | 26.980 MB | 26.980 MB | n/a MB | n/a MB |
| MainThread | 18247 | sandbox_agent_lsb-kimi_0000_0000 | 21 | 11.211% | 72.494% | 2.260 s | 381.390 MB | 397.566 MB | 9787.957 MB | 10204.188 MB | n/a MB | n/a MB |
| MainThread | 18272 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 230.258 MB | 230.258 MB | 1632.699 MB | 1632.699 MB | n/a MB | n/a MB |
| python | 18313 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.486% | 67.486% | 0.680 s | 44.496 MB | 65.941 MB | 54.451 MB | 79.855 MB | n/a MB | n/a MB |
| bash | 18311 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.816 MB | 2.816 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 18325 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.531% | 91.392% | 2.480 s | 351.513 MB | 391.535 MB | 8827.294 MB | 10206.832 MB | n/a MB | n/a MB |
| sh | 18350 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18351 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| MainThread | 18356 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.715 MB | 228.715 MB | 1635.840 MB | 1635.840 MB | n/a MB | n/a MB |
| MainThread | 18375 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 17.130% | 72.620% | 1.900 s | 365.704 MB | 387.223 MB | 9469.039 MB | 10207.121 MB | n/a MB | n/a MB |
| MainThread | 18481 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 179.410 MB | 179.410 MB | 1590.973 MB | 1590.973 MB | n/a MB | n/a MB |
| MainThread | 18500 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.934% | 83.478% | 2.740 s | 357.579 MB | 385.191 MB | 8962.696 MB | 10209.484 MB | n/a MB | n/a MB |
| MainThread | 18527 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.411% | 67.411% | 0.680 s | 173.938 MB | 260.078 MB | 1469.553 MB | 1655.410 MB | n/a MB | n/a MB |
| sh | 18525 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18526 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.902 MB | 9.902 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 18552 | sandbox_agent_lsb-kimi_0000_0000 | 27 | 12.094% | 76.438% | 3.180 s | 368.841 MB | 385.797 MB | 9572.275 MB | 10210.598 MB | n/a MB | n/a MB |
| MainThread | 18575 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.081% | 61.081% | 0.630 s | 238.838 MB | 293.984 MB | 1640.916 MB | 1688.859 MB | n/a MB | n/a MB |
| python3 | 18586 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.250 MB | 9.250 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 18585 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.344 MB | 1.344 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 18602 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.820 MB | 2.820 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 18603 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 7.563% | 60.503% | 0.610 s | 62.808 MB | 66.527 MB | 75.960 MB | 80.133 MB | n/a MB | n/a MB |
| MainThread | 18615 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 24.125% | 84.271% | 2.430 s | 360.217 MB | 384.348 MB | 9416.522 MB | 10211.738 MB | n/a MB | n/a MB |
| kimi-code | 18634 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 46.527 MB | 46.527 MB | 847.070 MB | 847.070 MB | n/a MB | n/a MB |
| MainThread | 18643 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 254.730 MB | 254.730 MB | 1651.086 MB | 1651.086 MB | n/a MB | n/a MB |
| MainThread | 18662 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 19.207% | 88.468% | 2.900 s | 362.911 MB | 394.906 MB | 9113.622 MB | 10206.941 MB | n/a MB | n/a MB |
| MainThread | 18681 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.539% | 57.539% | 0.580 s | 251.074 MB | 295.246 MB | 1654.527 MB | 1689.820 MB | n/a MB | n/a MB |
| sh | 18691 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18692 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.125 MB | 10.125 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 18713 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.231% | 82.392% | 2.780 s | 363.227 MB | 392.305 MB | 8983.213 MB | 10209.141 MB | n/a MB | n/a MB |
| MainThread | 18734 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.398% | 59.398% | 0.600 s | 252.262 MB | 296.684 MB | 1655.342 MB | 1691.215 MB | n/a MB | n/a MB |
| MainThread | 18763 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 21.053% | 71.626% | 2.120 s | 361.042 MB | 382.477 MB | 8667.327 MB | 10204.469 MB | n/a MB | n/a MB |
| MainThread | 18790 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 174.980 MB | 174.980 MB | 1589.723 MB | 1589.723 MB | n/a MB | n/a MB |
| MainThread | 18810 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 19.068% | 65.479% | 1.920 s | 370.713 MB | 390.176 MB | 9419.450 MB | 10206.137 MB | n/a MB | n/a MB |
| MainThread | 18834 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.613% | 51.613% | 0.520 s | 187.945 MB | 229.570 MB | 1469.047 MB | 1635.859 MB | n/a MB | n/a MB |
| MainThread | 18860 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.325% | 70.494% | 2.140 s | 364.180 MB | 384.645 MB | 9481.198 MB | 10207.617 MB | n/a MB | n/a MB |
| MainThread | 18882 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 213.598 MB | 213.598 MB | 1622.711 MB | 1622.711 MB | n/a MB | n/a MB |
| MainThread | 18908 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 15.929% | 75.431% | 2.730 s | 366.883 MB | 388.844 MB | 9251.364 MB | 10205.523 MB | n/a MB | n/a MB |
| MainThread | 18928 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.535 MB | 229.535 MB | 1631.949 MB | 1631.949 MB | n/a MB | n/a MB |
| MainThread | 18957 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 21.778% | 74.512% | 2.630 s | 361.330 MB | 391.023 MB | 8886.745 MB | 10209.031 MB | n/a MB | n/a MB |
| MainThread | 18985 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 69.568% | 69.568% | 0.700 s | 210.066 MB | 271.844 MB | 1485.727 MB | 1667.336 MB | n/a MB | n/a MB |
| MainThread | 19007 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 21.357% | 72.608% | 2.150 s | 363.739 MB | 390.242 MB | 9413.181 MB | 10207.273 MB | n/a MB | n/a MB |
| MainThread | 19030 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 45.653% | 45.653% | 0.460 s | 131.072 MB | 221.520 MB | 1398.455 MB | 1624.461 MB | n/a MB | n/a MB |
| MainThread | 19056 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 24.915% | 90.408% | 2.760 s | 343.806 MB | 389.156 MB | 8734.457 MB | 10204.988 MB | n/a MB | n/a MB |
| MainThread | 19077 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.493% | 57.493% | 0.580 s | 248.775 MB | 294.484 MB | 1653.520 MB | 1689.062 MB | n/a MB | n/a MB |
| sh | 19087 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19088 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.629 MB | 7.629 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| MainThread | 19105 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 17.801% | 70.623% | 2.690 s | 366.983 MB | 389.801 MB | 9134.598 MB | 10205.914 MB | n/a MB | n/a MB |
| python3 | 19137 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.367 MB | 7.367 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 19136 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19124 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 219.969 MB | 219.969 MB | 1623.727 MB | 1623.727 MB | n/a MB | n/a MB |
| MainThread | 19155 | sandbox_agent_lsb-kimi_0000_0000 | 23 | 11.178% | 64.535% | 2.480 s | 385.536 MB | 397.438 MB | 9832.878 MB | 10211.031 MB | n/a MB | n/a MB |
| MainThread | 19175 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.544% | 57.544% | 0.580 s | 218.285 MB | 260.988 MB | 1623.268 MB | 1656.062 MB | n/a MB | n/a MB |
| python3 | 19206 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.277 MB | 18.277 MB | 24.234 MB | 24.234 MB | n/a MB | n/a MB |
| sh | 19205 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19221 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.724% | 82.354% | 2.450 s | 356.316 MB | 389.289 MB | 8951.991 MB | 10177.418 MB | n/a MB | n/a MB |
| MainThread | 19252 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 151.426 MB | 151.426 MB | 1315.969 MB | 1315.969 MB | n/a MB | n/a MB |
| MainThread | 19274 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.361% | 85.499% | 2.870 s | 363.310 MB | 394.242 MB | 9043.140 MB | 10206.809 MB | n/a MB | n/a MB |
| MainThread | 19295 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.459% | 59.459% | 0.600 s | 247.346 MB | 294.594 MB | 1653.672 MB | 1689.340 MB | n/a MB | n/a MB |
| sh | 19305 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19306 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.914 MB | 9.914 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 19326 | sandbox_agent_lsb-kimi_0000_0000 | 29 | 11.096% | 76.412% | 3.130 s | 374.346 MB | 390.000 MB | 9614.418 MB | 10207.617 MB | n/a MB | n/a MB |
| MainThread | 19345 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.503% | 59.503% | 0.600 s | 259.689 MB | 302.184 MB | 1675.082 MB | 1726.938 MB | n/a MB | n/a MB |
| bash | 19447 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 19448 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 30.744% | 61.489% | 0.620 s | 54.130 MB | 66.215 MB | 66.591 MB | 80.094 MB | n/a MB | n/a MB |
| python3 | 19470 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.816 MB | 15.816 MB | 20.711 MB | 20.711 MB | n/a MB | n/a MB |
| sh | 19469 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19479 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 24.050% | 71.604% | 2.460 s | 365.159 MB | 387.461 MB | 9418.493 MB | 10211.898 MB | n/a MB | n/a MB |
| kimi-code | 19500 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 47.934 MB | 47.934 MB | 843.387 MB | 843.387 MB | n/a MB | n/a MB |
| MainThread | 19504 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 181.574 MB | 181.574 MB | 1591.723 MB | 1591.723 MB | n/a MB | n/a MB |
| python3 | 19524 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.562 MB | 6.562 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 19523 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19528 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.089% | 72.549% | 2.500 s | 367.033 MB | 388.531 MB | 8988.381 MB | 10209.859 MB | n/a MB | n/a MB |
| MainThread | 19549 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 199.805 MB | 199.805 MB | 1617.977 MB | 1617.977 MB | n/a MB | n/a MB |
| MainThread | 19579 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.684% | 73.489% | 2.500 s | 364.289 MB | 387.660 MB | 8893.632 MB | 10209.363 MB | n/a MB | n/a MB |
| MainThread | 19601 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.476% | 62.476% | 0.630 s | 174.375 MB | 253.074 MB | 1466.516 MB | 1649.336 MB | n/a MB | n/a MB |
| python3 | 19600 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.867 MB | 9.867 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 19599 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 19613 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19614 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| MainThread | 19629 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 18.021% | 72.464% | 2.180 s | 367.703 MB | 385.230 MB | 9534.416 MB | 10205.301 MB | n/a MB | n/a MB |
| MainThread | 19648 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.097% | 63.097% | 0.640 s | 220.160 MB | 272.043 MB | 1622.562 MB | 1666.652 MB | n/a MB | n/a MB |
| MainThread | 19676 | sandbox_agent_lsb-kimi_0000_0000 | 26 | 10.050% | 67.581% | 2.530 s | 382.912 MB | 393.375 MB | 9875.738 MB | 10211.336 MB | n/a MB | n/a MB |
| MainThread | 19696 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.586% | 55.586% | 0.560 s | 214.076 MB | 259.887 MB | 1617.018 MB | 1655.562 MB | n/a MB | n/a MB |
| python | 19723 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 30.763% | 61.525% | 0.620 s | 66.621 MB | 77.270 MB | 267.496 MB | 279.871 MB | n/a MB | n/a MB |
| bash | 19722 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.809 MB | 2.809 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 19727 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19728 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.879 MB | 18.879 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| MainThread | 19741 | sandbox_agent_lsb-kimi_0000_0000 | 30 | 10.811% | 76.438% | 3.160 s | 383.359 MB | 398.145 MB | 9640.834 MB | 10214.074 MB | n/a MB | n/a MB |
| sh | 19761 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19762 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.215 MB | 9.215 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 19775 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19765 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.462% | 63.462% | 0.640 s | 244.527 MB | 294.980 MB | 1651.895 MB | 1689.316 MB | n/a MB | n/a MB |
| python3 | 19776 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.254 MB | 7.254 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 19810 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.105% | 74.556% | 2.670 s | 363.494 MB | 391.359 MB | 8890.782 MB | 10209.383 MB | n/a MB | n/a MB |
| MainThread | 19832 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.785 MB | 229.785 MB | 1636.090 MB | 1636.090 MB | n/a MB | n/a MB |
| MainThread | 19860 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.402% | 73.581% | 2.540 s | 365.514 MB | 390.070 MB | 8986.701 MB | 10209.734 MB | n/a MB | n/a MB |
| sh | 19877 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19878 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.246 MB | 9.246 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 19879 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.486% | 61.486% | 0.620 s | 144.867 MB | 235.383 MB | 1437.473 MB | 1636.336 MB | n/a MB | n/a MB |
| MainThread | 19907 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 16.273% | 66.522% | 2.130 s | 374.320 MB | 391.883 MB | 9589.347 MB | 10211.574 MB | n/a MB | n/a MB |
| MainThread | 19928 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.474% | 65.474% | 0.660 s | 238.795 MB | 289.023 MB | 1638.900 MB | 1683.578 MB | n/a MB | n/a MB |
| MainThread | 19959 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.832% | 87.499% | 2.760 s | 358.901 MB | 392.840 MB | 8882.463 MB | 10207.457 MB | n/a MB | n/a MB |
| sh | 19980 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19981 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.445 MB | 7.445 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 19987 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.160 MB | 229.160 MB | 1631.703 MB | 1631.703 MB | n/a MB | n/a MB |
| MainThread | 20007 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 17.666% | 69.515% | 2.140 s | 375.618 MB | 395.117 MB | 9540.791 MB | 10211.574 MB | n/a MB | n/a MB |
| MainThread | 20028 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.547% | 57.547% | 0.580 s | 216.535 MB | 260.688 MB | 1617.877 MB | 1656.031 MB | n/a MB | n/a MB |
| MainThread | 20059 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.709% | 77.543% | 2.840 s | 358.056 MB | 388.734 MB | 8982.388 MB | 10211.938 MB | n/a MB | n/a MB |
| sh | 20089 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 20090 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.691 MB | 10.691 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 20079 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.509% | 62.509% | 0.630 s | 252.381 MB | 297.855 MB | 1656.035 MB | 1692.328 MB | n/a MB | n/a MB |
| MainThread | 20110 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 13.284% | 68.475% | 2.140 s | 379.026 MB | 393.859 MB | 9699.015 MB | 10208.727 MB | n/a MB | n/a MB |
| MainThread | 20139 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 186.996 MB | 186.996 MB | 1593.973 MB | 1593.973 MB | n/a MB | n/a MB |
| kimi-code | 20163 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 17.333% | 64.612% | 1.920 s | 372.928 MB | 390.516 MB | 9490.978 MB | 10210.895 MB | n/a MB | n/a MB |
| python3 | 20195 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.742 MB | 10.742 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 20187 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 50.537% | 50.537% | 0.510 s | 187.705 MB | 228.855 MB | 1469.541 MB | 1635.848 MB | n/a MB | n/a MB |
| sh | 20193 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 20213 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.552% | 91.450% | 2.850 s | 356.598 MB | 396.859 MB | 8864.107 MB | 10211.941 MB | n/a MB | n/a MB |
| sh | 20243 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 20235 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.565% | 54.565% | 0.550 s | 213.242 MB | 259.168 MB | 1616.910 MB | 1655.598 MB | n/a MB | n/a MB |
| python3 | 20244 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.676 MB | 7.676 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| MainThread | 20268 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 16.161% | 75.588% | 2.770 s | 371.398 MB | 393.035 MB | 9257.461 MB | 10211.168 MB | n/a MB | n/a MB |
| MainThread | 20288 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.797 MB | 228.797 MB | 1635.355 MB | 1635.355 MB | n/a MB | n/a MB |
| MainThread | 20319 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 15.377% | 73.609% | 2.320 s | 376.950 MB | 395.406 MB | 9664.940 MB | 10211.055 MB | n/a MB | n/a MB |
| MainThread | 20343 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 204.691 MB | 204.691 MB | 1618.734 MB | 1618.734 MB | n/a MB | n/a MB |
| sh | 20364 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| MainThread | 20369 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 25.120% | 71.481% | 2.530 s | 364.027 MB | 395.422 MB | 8654.697 MB | 10209.500 MB | n/a MB | n/a MB |
| sh | 20388 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 20389 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.734 MB | 10.734 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 20390 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.446% | 61.446% | 0.620 s | 195.717 MB | 254.461 MB | 1473.090 MB | 1649.828 MB | n/a MB | n/a MB |
| python3 | 20404 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.680 MB | 5.680 MB | 11.645 MB | 11.645 MB | n/a MB | n/a MB |
| sh | 20403 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 20419 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.507% | 69.464% | 2.750 s | 370.351 MB | 396.234 MB | 9068.500 MB | 10210.707 MB | n/a MB | n/a MB |
| MainThread | 20520 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.545% | 58.545% | 0.590 s | 241.160 MB | 288.602 MB | 1649.008 MB | 1683.543 MB | n/a MB | n/a MB |
| MainThread | 20563 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.479% | 74.558% | 2.430 s | 368.372 MB | 393.473 MB | 8987.191 MB | 10206.480 MB | n/a MB | n/a MB |
| python3 | 20590 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.445 MB | 10.445 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 20589 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 20592 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 62.594 MB | 62.594 MB | 1238.609 MB | 1238.609 MB | n/a MB | n/a MB |
| MainThread | 20616 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.024% | 72.491% | 2.660 s | 361.239 MB | 391.664 MB | 8889.974 MB | 10209.973 MB | n/a MB | n/a MB |
| MainThread | 20636 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.643% | 56.643% | 0.570 s | 252.244 MB | 295.418 MB | 1655.104 MB | 1689.977 MB | n/a MB | n/a MB |
| python3 | 20658 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.285 MB | 8.285 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 20657 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 20662 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 17.822% | 76.611% | 2.690 s | 373.913 MB | 399.430 MB | 9138.719 MB | 10211.984 MB | n/a MB | n/a MB |
| MainThread | 20683 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.670% | 57.670% | 0.580 s | 261.635 MB | 301.961 MB | 1675.279 MB | 1726.332 MB | n/a MB | n/a MB |
| MainThread | 20715 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.790% | 74.452% | 2.650 s | 367.606 MB | 392.242 MB | 9069.233 MB | 10211.020 MB | n/a MB | n/a MB |
| MainThread | 20747 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 261.305 MB | 261.305 MB | 1656.551 MB | 1656.551 MB | n/a MB | n/a MB |
| MainThread | 20769 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.943% | 76.456% | 2.530 s | 362.399 MB | 387.910 MB | 8894.441 MB | 10211.125 MB | n/a MB | n/a MB |
| python3 | 20788 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.914 MB | 9.914 MB | 13.578 MB | 13.578 MB | n/a MB | n/a MB |
| sh | 20787 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 20798 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 268.738 MB | 268.738 MB | 1664.566 MB | 1664.566 MB | n/a MB | n/a MB |
| MainThread | 20820 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 14.424% | 85.447% | 2.620 s | 369.801 MB | 394.305 MB | 9291.489 MB | 10210.426 MB | n/a MB | n/a MB |
| MainThread | 20843 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 70.518% | 70.518% | 0.710 s | 221.291 MB | 275.211 MB | 1624.279 MB | 1669.836 MB | n/a MB | n/a MB |
| MainThread | 20872 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 16.986% | 75.423% | 2.060 s | 368.636 MB | 393.992 MB | 8891.014 MB | 10203.000 MB | n/a MB | n/a MB |
| MainThread | 20901 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 84.511% | 84.511% | 0.870 s | 200.527 MB | 296.855 MB | 1487.586 MB | 1691.477 MB | n/a MB | n/a MB |
| MainThread | 20922 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.451% | 73.433% | 2.470 s | 360.030 MB | 391.805 MB | 8887.924 MB | 10208.672 MB | n/a MB | n/a MB |
| MainThread | 20943 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 68.594% | 68.594% | 0.690 s | 218.357 MB | 278.633 MB | 1586.791 MB | 1673.613 MB | n/a MB | n/a MB |
| MainThread | 20969 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.040% | 76.438% | 2.330 s | 365.416 MB | 390.688 MB | 8786.533 MB | 10208.195 MB | n/a MB | n/a MB |
| MainThread | 20997 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 288.434 MB | 288.434 MB | 1683.059 MB | 1683.059 MB | n/a MB | n/a MB |
| MainThread | 21016 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.496% | 86.343% | 2.890 s | 364.741 MB | 395.887 MB | 9059.855 MB | 10211.406 MB | n/a MB | n/a MB |
| MainThread | 21040 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 50.647% | 50.647% | 0.510 s | 170.105 MB | 235.055 MB | 1459.771 MB | 1635.848 MB | n/a MB | n/a MB |
| MainThread | 21067 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.160% | 73.437% | 2.700 s | 367.628 MB | 395.672 MB | 9063.189 MB | 10208.941 MB | n/a MB | n/a MB |
| MainThread | 21088 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.582% | 57.582% | 0.580 s | 264.201 MB | 299.941 MB | 1678.119 MB | 1724.520 MB | n/a MB | n/a MB |
| MainThread | 21120 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.099% | 86.370% | 2.500 s | 371.952 MB | 389.578 MB | 9004.222 MB | 10212.734 MB | n/a MB | n/a MB |
| MainThread | 21158 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 12.587% | 74.494% | 2.280 s | 375.549 MB | 394.176 MB | 9302.791 MB | 10201.934 MB | n/a MB | n/a MB |
| MainThread | 21197 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 17.347% | 69.624% | 1.920 s | 367.003 MB | 381.551 MB | 9483.603 MB | 10203.340 MB | n/a MB | n/a MB |
| MainThread | 21232 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 13.690% | 75.456% | 1.930 s | 373.790 MB | 392.301 MB | 9062.927 MB | 10186.246 MB | n/a MB | n/a MB |
| MainThread | 21268 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 15.528% | 73.545% | 2.190 s | 370.668 MB | 392.184 MB | 9062.840 MB | 10200.125 MB | n/a MB | n/a MB |
| sh | 21287 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21288 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.797 MB | 9.797 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 21304 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.498% | 73.590% | 2.400 s | 360.139 MB | 384.055 MB | 8783.548 MB | 10206.949 MB | n/a MB | n/a MB |
| python3 | 21324 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.176 MB | 9.176 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 21323 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 21339 | sandbox_agent_lsb-kimi_0000_0000 | 31 | 9.688% | 79.228% | 2.940 s | 383.296 MB | 401.926 MB | 9641.242 MB | 10205.805 MB | n/a MB | n/a MB |
| python3 | 21373 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.727 MB | 11.727 MB | 19.910 MB | 19.910 MB | n/a MB | n/a MB |
| sh | 21372 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 21376 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 9.920% | 19.840% | 0.200 s | 60.747 MB | 66.090 MB | 73.031 MB | 80.109 MB | n/a MB | n/a MB |
| bash | 21375 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.879 MB | 2.879 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 21385 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21386 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.102 MB | 10.102 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 21390 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 13.745% | 77.594% | 2.650 s | 375.406 MB | 392.875 MB | 9355.750 MB | 10211.914 MB | n/a MB | n/a MB |
| python3 | 21410 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.973 MB | 9.973 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 21409 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 21523 | sandbox_agent_lsb-kimi_0000_0000 | 30 | 11.135% | 84.454% | 3.250 s | 375.580 MB | 392.699 MB | 9624.701 MB | 10206.230 MB | n/a MB | n/a MB |
| sh | 21546 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21547 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.566 MB | 10.566 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 21553 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21554 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.707 MB | 14.707 MB | 20.082 MB | 20.082 MB | n/a MB | n/a MB |
| MainThread | 21572 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 13.659% | 73.460% | 2.210 s | 381.107 MB | 395.637 MB | 9698.619 MB | 10209.758 MB | n/a MB | n/a MB |
| MainThread | 21607 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 19.720% | 75.615% | 2.380 s | 368.417 MB | 391.324 MB | 8899.288 MB | 10205.898 MB | n/a MB | n/a MB |
| MainThread | 21643 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 21.279% | 77.436% | 2.570 s | 361.591 MB | 385.164 MB | 8892.827 MB | 10207.867 MB | n/a MB | n/a MB |
| sh | 21662 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21663 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.922 MB | 9.922 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 21668 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21669 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.547 MB | 5.547 MB | 11.645 MB | 11.645 MB | n/a MB | n/a MB |
| MainThread | 21678 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 24.330% | 76.422% | 2.700 s | 354.096 MB | 386.973 MB | 8778.891 MB | 10210.672 MB | n/a MB | n/a MB |
| sh | 21704 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21705 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.945 MB | 8.945 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 21717 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 17.617% | 75.565% | 2.310 s | 368.876 MB | 390.262 MB | 8995.515 MB | 10209.926 MB | n/a MB | n/a MB |
| sh | 21742 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21743 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.914 MB | 9.914 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 21755 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 11.972% | 72.478% | 2.170 s | 376.872 MB | 389.484 MB | 9753.282 MB | 10211.797 MB | n/a MB | n/a MB |
| MainThread | 21794 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.587% | 81.364% | 2.730 s | 353.111 MB | 382.078 MB | 8879.614 MB | 10203.809 MB | n/a MB | n/a MB |
| python3 | 21819 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.047 MB | 10.047 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 21818 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 21830 | sandbox_agent_lsb-kimi_0000_0000 | 162 | 4.578% | 77.527% | 7.420 s | 384.053 MB | 398.742 MB | 10133.337 MB | 10216.277 MB | n/a MB | n/a MB |
| bash | 21868 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.881 MB | 2.508 MB | 2.918 MB | 3.848 MB | n/a MB | n/a MB |
| python | 21869 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 7.440% | 14.880% | 0.150 s | 61.609 MB | 66.367 MB | 73.708 MB | 80.109 MB | n/a MB | n/a MB |
| sh | 21908 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21909 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.754 MB | 20.754 MB | 25.836 MB | 25.836 MB | n/a MB | n/a MB |
| bash | 21915 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.586 MB | 2.586 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 21916 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 32.354% | 64.708% | 0.660 s | 51.009 MB | 65.766 MB | 62.440 MB | 80.102 MB | n/a MB | n/a MB |
| python3 | 21918 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.398 MB | 15.398 MB | 20.602 MB | 20.602 MB | n/a MB | n/a MB |
| sh | 21917 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21927 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.293 MB | 9.293 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 21926 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 21934 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.738 MB | 2.738 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 21935 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.414 MB | 10.414 MB | 13.867 MB | 13.867 MB | n/a MB | n/a MB |
| sh | 21949 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| python | 21952 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 49.703 MB | 49.703 MB | 57.672 MB | 57.672 MB | n/a MB | n/a MB |
| bash | 21951 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.648 MB | 2.648 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 21958 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21959 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.883 MB | 16.883 MB | 22.141 MB | 22.141 MB | n/a MB | n/a MB |
| python | 21961 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 30.753% | 30.753% | 0.310 s | 57.324 MB | 67.699 MB | 68.713 MB | 82.484 MB | n/a MB | n/a MB |
| bash | 21960 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.762 MB | 2.762 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 21979 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 21980 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 25.137% | 71.458% | 0.760 s | 55.492 MB | 66.777 MB | 67.711 MB | 81.820 MB | n/a MB | n/a MB |
| sh | 21983 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21984 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.680 MB | 14.680 MB | 20.082 MB | 20.082 MB | n/a MB | n/a MB |
| bash | 21997 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.867 MB | 2.867 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 21998 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 68.434% | 68.434% | 0.690 s | 36.428 MB | 62.797 MB | 46.010 MB | 77.508 MB | n/a MB | n/a MB |
| python3 | 22001 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.691 MB | 20.691 MB | 25.832 MB | 25.832 MB | n/a MB | n/a MB |
| sh | 22000 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 22005 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22006 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.051 MB | 15.051 MB | 20.398 MB | 20.398 MB | n/a MB | n/a MB |
| bash | 22032 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.840 MB | 2.840 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 22033 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 30.737% | 57.534% | 0.620 s | 56.221 MB | 67.113 MB | 68.630 MB | 81.812 MB | n/a MB | n/a MB |
| sh | 22048 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22049 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.316 MB | 21.316 MB | 27.070 MB | 27.070 MB | n/a MB | n/a MB |
| MainThread | 22058 | sandbox_agent_lsb-kimi_0000_0000 | 26 | 13.995% | 89.458% | 3.520 s | 370.328 MB | 392.387 MB | 9534.896 MB | 10211.734 MB | n/a MB | n/a MB |
| MainThread | 22079 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 207.938 MB | 207.938 MB | 1619.484 MB | 1619.484 MB | n/a MB | n/a MB |
| python | 22104 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 44.113 MB | 44.113 MB | 52.984 MB | 52.984 MB | n/a MB | n/a MB |
| bash | 22103 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 22116 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.645 MB | 2.645 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 22117 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 15.895% | 27.831% | 0.320 s | 59.741 MB | 66.605 MB | 72.315 MB | 81.844 MB | n/a MB | n/a MB |
| MainThread | 22128 | sandbox_agent_lsb-kimi_0000_0000 | 37 | 10.453% | 88.294% | 3.790 s | 375.248 MB | 388.871 MB | 9744.675 MB | 10213.992 MB | n/a MB | n/a MB |
| python3 | 22152 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.992 MB | 6.992 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 22151 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22160 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 166.582 MB | 166.582 MB | 1577.973 MB | 1577.973 MB | n/a MB | n/a MB |
| python | 22250 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 3.972% | 39.720% | 0.400 s | 63.469 MB | 65.719 MB | 77.405 MB | 80.188 MB | n/a MB | n/a MB |
| bash | 22249 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.844 MB | 2.844 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 22258 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.270 MB | 7.270 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 22257 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 22264 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.734 MB | 2.734 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 22265 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 37.805 MB | 37.805 MB | 46.059 MB | 46.059 MB | n/a MB | n/a MB |
| bash | 22275 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| MainThread | 22290 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 27.501% | 72.535% | 2.230 s | 360.964 MB | 388.258 MB | 9237.990 MB | 10210.945 MB | n/a MB | n/a MB |
| MainThread | 22310 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.293% | 57.293% | 0.580 s | 205.057 MB | 254.641 MB | 1480.875 MB | 1650.379 MB | n/a MB | n/a MB |
| python3 | 22324 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.234 MB | 8.234 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 22323 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22339 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 17.759% | 86.488% | 3.220 s | 367.377 MB | 393.277 MB | 9286.981 MB | 10211.734 MB | n/a MB | n/a MB |
| MainThread | 22358 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.596% | 52.596% | 0.530 s | 217.555 MB | 260.434 MB | 1622.639 MB | 1655.305 MB | n/a MB | n/a MB |
| bash | 22385 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.762 MB | 2.762 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 22386 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 33.708% | 67.417% | 0.680 s | 52.431 MB | 66.742 MB | 63.786 MB | 81.195 MB | n/a MB | n/a MB |
| MainThread | 22397 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.106% | 75.458% | 2.370 s | 375.320 MB | 391.070 MB | 9590.825 MB | 10211.832 MB | n/a MB | n/a MB |
| MainThread | 22422 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 79.522% | 79.522% | 0.800 s | 235.650 MB | 303.168 MB | 1653.029 MB | 1727.586 MB | n/a MB | n/a MB |
| bash | 22441 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.898 MB | 2.898 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 22442 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 51.441 MB | 51.441 MB | 248.070 MB | 248.070 MB | n/a MB | n/a MB |
| MainThread | 22456 | sandbox_agent_lsb-kimi_0000_0000 | 29 | 11.517% | 73.487% | 3.250 s | 381.457 MB | 400.871 MB | 9910.251 MB | 10214.781 MB | n/a MB | n/a MB |
| MainThread | 22477 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.560% | 52.560% | 0.530 s | 196.186 MB | 235.484 MB | 1475.121 MB | 1636.359 MB | n/a MB | n/a MB |
| python3 | 22490 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.797 MB | 7.797 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 22489 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 22502 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.730 MB | 2.730 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 22503 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 43.223 MB | 43.223 MB | 51.438 MB | 51.438 MB | n/a MB | n/a MB |
| sh | 22510 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22511 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.922 MB | 14.922 MB | 20.242 MB | 20.242 MB | n/a MB | n/a MB |
| python3 | 22525 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.531 MB | 20.531 MB | 25.707 MB | 25.707 MB | n/a MB | n/a MB |
| sh | 22524 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 22538 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22539 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.844 MB | 9.844 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 22543 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 16.063% | 70.509% | 2.750 s | 374.221 MB | 395.895 MB | 9226.368 MB | 10191.117 MB | n/a MB | n/a MB |
| MainThread | 22572 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 197.586 MB | 197.586 MB | 1616.949 MB | 1616.949 MB | n/a MB | n/a MB |
| bash | 22588 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.883 MB | 2.883 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 22589 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.454% | 66.454% | 0.670 s | 45.195 MB | 65.824 MB | 55.623 MB | 79.840 MB | n/a MB | n/a MB |
| python3 | 22603 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.059 MB | 10.059 MB | 13.844 MB | 13.844 MB | n/a MB | n/a MB |
| sh | 22602 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22612 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 39.911% | 78.458% | 2.410 s | 339.152 MB | 389.812 MB | 7749.610 MB | 10209.270 MB | n/a MB | n/a MB |
| python3 | 22634 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.621 MB | 9.621 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| sh | 22633 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22640 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.195 MB | 229.195 MB | 1631.988 MB | 1631.988 MB | n/a MB | n/a MB |
| MainThread | 22659 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 39.897% | 76.426% | 2.410 s | 334.515 MB | 380.086 MB | 7740.097 MB | 10177.070 MB | n/a MB | n/a MB |
| MainThread | 22676 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 47.626% | 47.626% | 0.480 s | 266.270 MB | 303.199 MB | 1681.107 MB | 1726.887 MB | n/a MB | n/a MB |
| sh | 22694 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22695 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.105 MB | 9.105 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 22707 | sandbox_agent_lsb-kimi_0000_0000 | 40 | 9.062% | 85.342% | 3.560 s | 389.336 MB | 405.348 MB | 9762.248 MB | 10200.973 MB | n/a MB | n/a MB |
| MainThread | 22726 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.601% | 52.601% | 0.530 s | 222.963 MB | 261.250 MB | 1624.879 MB | 1656.285 MB | n/a MB | n/a MB |
| python3 | 22739 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.973 MB | 9.973 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 22738 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 22752 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 0.000% | 0.000% | 0.000 s | 2.945 MB | 2.945 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 22753 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 4.099% | 47.586% | 0.620 s | 65.150 MB | 67.367 MB | 79.514 MB | 82.086 MB | n/a MB | n/a MB |
| MainThread | 22781 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.536% | 75.527% | 2.630 s | 335.775 MB | 385.898 MB | 7754.014 MB | 10203.703 MB | n/a MB | n/a MB |
| sh | 22811 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.395 MB | 1.395 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22812 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.512 MB | 7.512 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 22801 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 50.631% | 50.631% | 0.510 s | 227.867 MB | 264.367 MB | 1628.520 MB | 1660.566 MB | n/a MB | n/a MB |
| sh | 22822 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22823 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.707 MB | 4.707 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| MainThread | 22827 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.200% | 76.359% | 2.610 s | 332.873 MB | 383.715 MB | 7761.007 MB | 10210.484 MB | n/a MB | n/a MB |
| MainThread | 22855 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 194.980 MB | 194.980 MB | 1615.223 MB | 1615.223 MB | n/a MB | n/a MB |
| MainThread | 22874 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 42.369% | 67.472% | 2.560 s | 336.295 MB | 385.789 MB | 7757.441 MB | 10206.891 MB | n/a MB | n/a MB |
| sh | 22904 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22893 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.518% | 56.518% | 0.570 s | 236.539 MB | 278.961 MB | 1644.014 MB | 1673.555 MB | n/a MB | n/a MB |
| python3 | 22905 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.105 MB | 10.105 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| python3 | 22918 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.707 MB | 6.707 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 22917 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22922 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 38.308% | 73.520% | 2.700 s | 343.772 MB | 388.254 MB | 8060.701 MB | 10207.027 MB | n/a MB | n/a MB |
| MainThread | 22941 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.462% | 57.462% | 0.580 s | 249.836 MB | 294.395 MB | 1654.133 MB | 1689.301 MB | n/a MB | n/a MB |
| python3 | 22952 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.406 MB | 9.406 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 22951 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22969 | sandbox_agent_lsb-kimi_0000_0000 | 22 | 15.229% | 66.483% | 3.220 s | 380.926 MB | 399.852 MB | 9430.681 MB | 10212.316 MB | n/a MB | n/a MB |
| MainThread | 22986 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.641% | 54.641% | 0.550 s | 195.398 MB | 236.090 MB | 1473.871 MB | 1637.121 MB | n/a MB | n/a MB |
| gzip | 23012 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| tar | 23011 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.285 MB | 2.285 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| python | 23016 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 6.450% | 25.800% | 0.260 s | 62.566 MB | 66.684 MB | 75.075 MB | 80.176 MB | n/a MB | n/a MB |
| bash | 23015 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 23035 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 46.168% | 88.473% | 2.790 s | 319.924 MB | 385.145 MB | 7699.773 MB | 10204.863 MB | n/a MB | n/a MB |
| MainThread | 23054 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.585% | 60.585% | 0.610 s | 224.971 MB | 273.043 MB | 1629.270 MB | 1668.066 MB | n/a MB | n/a MB |
| kimi | 23082 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 36.752% | 86.334% | 2.960 s | 323.224 MB | 389.246 MB | 8124.068 MB | 10207.891 MB | n/a MB | n/a MB |
| MainThread | 23101 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.627% | 49.627% | 0.500 s | 210.088 MB | 253.434 MB | 1613.273 MB | 1648.824 MB | n/a MB | n/a MB |
| MainThread | 23127 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 25.338% | 78.585% | 2.550 s | 361.200 MB | 385.770 MB | 8659.194 MB | 10210.859 MB | n/a MB | n/a MB |
| sh | 23144 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 23145 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.988 MB | 9.988 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 23155 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 276.039 MB | 276.039 MB | 1671.301 MB | 1671.301 MB | n/a MB | n/a MB |
| bash | 23169 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 23170 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 70.559% | 70.559% | 0.710 s | 41.244 MB | 63.281 MB | 51.438 MB | 77.504 MB | n/a MB | n/a MB |
| MainThread | 23203 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 42.953% | 79.519% | 2.610 s | 330.328 MB | 378.340 MB | 7747.964 MB | 10202.363 MB | n/a MB | n/a MB |
| MainThread | 23220 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.484 MB | 228.484 MB | 1631.617 MB | 1631.617 MB | n/a MB | n/a MB |
| MainThread | 23248 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 33.828% | 69.616% | 2.050 s | 358.977 MB | 384.449 MB | 8965.090 MB | 10203.473 MB | n/a MB | n/a MB |
| MainThread | 23268 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.903% | 58.903% | 0.600 s | 213.377 MB | 259.945 MB | 1616.914 MB | 1655.855 MB | n/a MB | n/a MB |
| sh | 23280 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.293 MB | 1.293 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 23281 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.406 MB | 10.406 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 23296 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 17.617% | 78.457% | 2.860 s | 375.946 MB | 397.336 MB | 9200.704 MB | 10209.188 MB | n/a MB | n/a MB |
| MainThread | 23317 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.778% | 60.778% | 0.640 s | 237.217 MB | 293.840 MB | 1640.270 MB | 1689.066 MB | n/a MB | n/a MB |
| python3 | 23343 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.609 MB | 9.609 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sh | 23342 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 23349 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.668 MB | 2.668 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 23350 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 69.555% | 69.555% | 0.700 s | 39.750 MB | 61.762 MB | 49.826 MB | 75.918 MB | n/a MB | n/a MB |
| MainThread | 23361 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.534% | 86.360% | 2.630 s | 328.929 MB | 378.480 MB | 7735.898 MB | 10205.207 MB | n/a MB | n/a MB |
| MainThread | 23391 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 186.375 MB | 186.375 MB | 1593.723 MB | 1593.723 MB | n/a MB | n/a MB |
| kimi-code | 23410 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 32.119% | 71.474% | 1.940 s | 362.055 MB | 388.902 MB | 8968.681 MB | 10203.363 MB | n/a MB | n/a MB |
| MainThread | 23431 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 206.957 MB | 206.957 MB | 1618.988 MB | 1618.988 MB | n/a MB | n/a MB |
| kimi-code | 23450 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 59.395 MB | 59.395 MB | 899.762 MB | 899.762 MB | n/a MB | n/a MB |
| MainThread | 23457 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 22.843% | 87.372% | 3.220 s | 356.778 MB | 395.367 MB | 9031.167 MB | 10208.727 MB | n/a MB | n/a MB |
| MainThread | 23476 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.578% | 53.578% | 0.540 s | 215.518 MB | 259.477 MB | 1617.525 MB | 1655.328 MB | n/a MB | n/a MB |
| bash | 23501 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.789 MB | 2.789 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 23505 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.184 MB | 8.184 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| MainThread | 23520 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 32.279% | 76.520% | 1.950 s | 359.138 MB | 381.984 MB | 8969.408 MB | 10204.766 MB | n/a MB | n/a MB |
| MainThread | 23549 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 174.668 MB | 174.668 MB | 1582.223 MB | 1582.223 MB | n/a MB | n/a MB |
| MainThread | 23566 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 44.539% | 77.545% | 2.690 s | 339.586 MB | 390.988 MB | 7759.905 MB | 10211.512 MB | n/a MB | n/a MB |
| sh | 23587 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 23588 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.262 MB | 7.262 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| python3 | 23603 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.531 MB | 8.531 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 23602 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23594 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 260.492 MB | 260.492 MB | 1656.059 MB | 1656.059 MB | n/a MB | n/a MB |
| MainThread | 23610 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 38.874% | 76.488% | 2.740 s | 342.468 MB | 392.027 MB | 8058.574 MB | 10210.312 MB | n/a MB | n/a MB |
| MainThread | 23629 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.547% | 59.547% | 0.600 s | 226.773 MB | 267.898 MB | 1628.650 MB | 1663.828 MB | n/a MB | n/a MB |
| MainThread | 23657 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 17.697% | 71.448% | 3.040 s | 373.996 MB | 396.031 MB | 9259.904 MB | 10215.406 MB | n/a MB | n/a MB |
| MainThread | 23676 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.559% | 59.559% | 0.600 s | 242.836 MB | 287.023 MB | 1649.773 MB | 1682.066 MB | n/a MB | n/a MB |
| python3 | 23700 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.430 MB | 10.430 MB | 14.059 MB | 14.059 MB | n/a MB | n/a MB |
| sh | 23699 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 23701 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.766 MB | 2.766 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 23702 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 23.818% | 23.818% | 0.240 s | 57.309 MB | 66.152 MB | 68.721 MB | 80.105 MB | n/a MB | n/a MB |
| MainThread | 23714 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 25.662% | 83.491% | 2.840 s | 355.926 MB | 394.820 MB | 8761.955 MB | 10207.020 MB | n/a MB | n/a MB |
| MainThread | 23743 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 180.312 MB | 180.312 MB | 1591.473 MB | 1591.473 MB | n/a MB | n/a MB |
| MainThread | 23762 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 41.730% | 76.591% | 2.100 s | 349.540 MB | 383.676 MB | 8755.029 MB | 10207.582 MB | n/a MB | n/a MB |
| python3 | 23794 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.695 MB | 8.695 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 23793 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23783 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.431% | 67.431% | 0.680 s | 247.100 MB | 299.605 MB | 1654.617 MB | 1694.262 MB | n/a MB | n/a MB |
| MainThread | 23807 | sandbox_agent_lsb-kimi_0000_0000 | 25 | 11.220% | 76.584% | 2.710 s | 382.382 MB | 394.578 MB | 9862.066 MB | 10211.875 MB | n/a MB | n/a MB |
| MainThread | 23829 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 212.457 MB | 212.457 MB | 1622.238 MB | 1622.238 MB | n/a MB | n/a MB |
| bash | 23852 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.660 MB | 2.660 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 23853 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.023 MB | 14.023 MB | 207.629 MB | 207.629 MB | n/a MB | n/a MB |
| python3 | 23865 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.523 MB | 7.523 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 23864 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23869 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 37.770% | 74.540% | 2.680 s | 342.596 MB | 386.941 MB | 8057.905 MB | 10208.270 MB | n/a MB | n/a MB |
| MainThread | 23886 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.121 MB | 229.121 MB | 1631.723 MB | 1631.723 MB | n/a MB | n/a MB |
| MainThread | 23914 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 28.816% | 67.632% | 2.330 s | 363.179 MB | 395.051 MB | 9225.777 MB | 10218.621 MB | n/a MB | n/a MB |
| MainThread | 23931 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.519% | 60.519% | 0.610 s | 214.043 MB | 262.121 MB | 1617.639 MB | 1657.305 MB | n/a MB | n/a MB |
| MainThread | 23959 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 41.295% | 72.456% | 2.080 s | 349.979 MB | 384.852 MB | 8748.702 MB | 10204.070 MB | n/a MB | n/a MB |
| MainThread | 23977 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.565% | 57.565% | 0.580 s | 212.641 MB | 260.551 MB | 1614.154 MB | 1655.836 MB | n/a MB | n/a MB |
| sh | 23991 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.426 MB | 1.426 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 23992 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.492 MB | 7.492 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 24007 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 15.680% | 73.466% | 2.530 s | 377.775 MB | 394.512 MB | 9694.455 MB | 10209.637 MB | n/a MB | n/a MB |
| MainThread | 24026 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.299% | 49.299% | 0.500 s | 186.734 MB | 229.668 MB | 1467.830 MB | 1635.855 MB | n/a MB | n/a MB |
| sh | 24038 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24039 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.980 MB | 8.980 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 24049 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24050 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.457 MB | 20.457 MB | 25.320 MB | 25.320 MB | n/a MB | n/a MB |
| bash | 24051 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.820 MB | 2.820 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 24052 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1061.676 MB | 1061.676 MB | 1253.316 MB | 1253.316 MB | n/a MB | n/a MB |
| MainThread | 24066 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 15.887% | 78.423% | 1.920 s | 373.031 MB | 390.902 MB | 9507.821 MB | 10200.344 MB | n/a MB | n/a MB |
| MainThread | 24094 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 294.137 MB | 294.137 MB | 1689.332 MB | 1689.332 MB | n/a MB | n/a MB |
| MainThread | 24113 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 39.920% | 72.465% | 2.030 s | 354.900 MB | 386.152 MB | 8756.289 MB | 10207.422 MB | n/a MB | n/a MB |
| MainThread | 24133 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.279% | 56.279% | 0.570 s | 203.381 MB | 253.832 MB | 1574.275 MB | 1649.332 MB | n/a MB | n/a MB |
| sh | 24145 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24146 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.875 MB | 8.875 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 24159 | sandbox_agent_lsb-kimi_0000_0000 | 40 | 8.047% | 77.433% | 3.160 s | 383.233 MB | 391.480 MB | 9990.652 MB | 10210.938 MB | n/a MB | n/a MB |
| MainThread | 24178 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.568% | 59.568% | 0.600 s | 172.432 MB | 240.375 MB | 1461.387 MB | 1639.078 MB | n/a MB | n/a MB |
| sh | 24212 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24213 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.484 MB | 9.484 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| python | 24215 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1061.629 MB | 1061.629 MB | 1253.301 MB | 1253.301 MB | n/a MB | n/a MB |
| bash | 24214 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.824 MB | 2.824 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 24232 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 17.639% | 69.453% | 3.020 s | 366.898 MB | 390.977 MB | 9254.159 MB | 10209.523 MB | n/a MB | n/a MB |
| MainThread | 24256 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.483% | 49.483% | 0.500 s | 203.525 MB | 243.410 MB | 1605.859 MB | 1639.246 MB | n/a MB | n/a MB |
| python3 | 24264 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.988 MB | 7.988 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 24263 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24278 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.234 MB | 21.234 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| sh | 24277 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 24279 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 24280 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 33.714% | 33.714% | 0.340 s | 68.367 MB | 78.184 MB | 268.172 MB | 280.848 MB | n/a MB | n/a MB |
| python3 | 24292 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.945 MB | 6.945 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 24291 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24296 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 44.615% | 85.322% | 2.730 s | 331.136 MB | 386.828 MB | 7726.562 MB | 10204.246 MB | n/a MB | n/a MB |
| MainThread | 24315 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.172% | 64.172% | 0.650 s | 223.334 MB | 274.652 MB | 1624.768 MB | 1670.062 MB | n/a MB | n/a MB |
| MainThread | 24343 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 36.569% | 78.446% | 2.210 s | 352.059 MB | 383.934 MB | 8938.477 MB | 10205.555 MB | n/a MB | n/a MB |
| sh | 24360 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24361 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| MainThread | 24362 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.619% | 55.619% | 0.560 s | 263.529 MB | 297.387 MB | 1662.346 MB | 1692.219 MB | n/a MB | n/a MB |
| MainThread | 24390 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.629% | 82.505% | 2.980 s | 359.350 MB | 390.469 MB | 8971.306 MB | 10208.574 MB | n/a MB | n/a MB |
| MainThread | 24409 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.201% | 61.201% | 0.620 s | 223.564 MB | 271.906 MB | 1624.512 MB | 1667.301 MB | n/a MB | n/a MB |
| git | 24417 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.059 MB | 4.059 MB | n/a MB | n/a MB |
| MainThread | 24455 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.920% | 75.314% | 2.440 s | 368.150 MB | 395.273 MB | 8782.098 MB | 10207.387 MB | n/a MB | n/a MB |
| sh | 24474 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 24473 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 24488 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 24489 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24475 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 50.645% | 50.645% | 0.510 s | 265.697 MB | 302.125 MB | 1679.047 MB | 1726.363 MB | n/a MB | n/a MB |
| MainThread | 24504 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 36.888% | 78.562% | 2.230 s | 352.940 MB | 389.625 MB | 8946.852 MB | 10207.828 MB | n/a MB | n/a MB |
| sh | 24522 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24523 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.906 MB | 7.906 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 24536 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.398 MB | 1.398 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24537 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.371 MB | 7.371 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| MainThread | 24526 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.459% | 62.459% | 0.630 s | 244.664 MB | 295.621 MB | 1652.217 MB | 1690.211 MB | n/a MB | n/a MB |
| MainThread | 24552 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.411% | 75.423% | 2.150 s | 377.640 MB | 396.879 MB | 9489.362 MB | 10213.516 MB | n/a MB | n/a MB |
| MainThread | 24580 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 78.504% | 78.504% | 0.790 s | 227.496 MB | 295.742 MB | 1503.008 MB | 1690.207 MB | n/a MB | n/a MB |
| MainThread | 24599 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 17.907% | 72.474% | 2.180 s | 372.847 MB | 390.746 MB | 9538.153 MB | 10211.160 MB | n/a MB | n/a MB |
| MainThread | 24618 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.320% | 55.320% | 0.560 s | 200.930 MB | 243.645 MB | 1570.174 MB | 1640.379 MB | n/a MB | n/a MB |
| python3 | 24634 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.027 MB | 10.027 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 24633 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24725 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.519% | 71.442% | 2.640 s | 332.873 MB | 386.574 MB | 7748.312 MB | 10206.285 MB | n/a MB | n/a MB |
| MainThread | 24745 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.192% | 62.192% | 0.630 s | 110.938 MB | 221.875 MB | 812.359 MB | 1624.719 MB | n/a MB | n/a MB |
| python3 | 24764 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.859 MB | 7.859 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 24763 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24775 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.221% | 77.476% | 2.350 s | 373.049 MB | 398.023 MB | 9483.492 MB | 10210.543 MB | n/a MB | n/a MB |
| MainThread | 24804 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 259.289 MB | 259.289 MB | 1655.328 MB | 1655.328 MB | n/a MB | n/a MB |
| MainThread | 24823 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 16.415% | 77.508% | 2.320 s | 371.443 MB | 392.078 MB | 9060.063 MB | 10196.914 MB | n/a MB | n/a MB |
| sh | 24848 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24849 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.121 MB | 7.121 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 24855 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 206.352 MB | 206.352 MB | 1619.719 MB | 1619.719 MB | n/a MB | n/a MB |
| python3 | 24868 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.117 MB | 8.117 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 24867 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24872 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.359% | 79.384% | 2.620 s | 332.733 MB | 384.488 MB | 7754.355 MB | 10203.898 MB | n/a MB | n/a MB |
| MainThread | 24894 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 47.637% | 47.637% | 0.480 s | 194.227 MB | 228.980 MB | 1473.660 MB | 1631.262 MB | n/a MB | n/a MB |
| MainThread | 24920 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.073% | 77.257% | 2.500 s | 372.656 MB | 395.762 MB | 8986.616 MB | 10208.340 MB | n/a MB | n/a MB |
| MainThread | 24941 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.406% | 61.406% | 0.620 s | 262.600 MB | 302.980 MB | 1676.178 MB | 1727.645 MB | n/a MB | n/a MB |
| sh | 24953 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24954 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.730 MB | 6.730 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 24969 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 40.033% | 71.501% | 2.420 s | 346.064 MB | 389.051 MB | 7764.767 MB | 10208.148 MB | n/a MB | n/a MB |
| MainThread | 24992 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.587% | 51.587% | 0.520 s | 212.580 MB | 256.891 MB | 1615.268 MB | 1652.062 MB | n/a MB | n/a MB |
| MainThread | 25018 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.746% | 87.481% | 2.990 s | 351.878 MB | 395.770 MB | 8853.188 MB | 10210.648 MB | n/a MB | n/a MB |
| MainThread | 25037 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.398% | 60.398% | 0.610 s | 222.510 MB | 270.145 MB | 1627.494 MB | 1665.016 MB | n/a MB | n/a MB |
| kimi-code | 25045 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.711 MB | 50.711 MB | 847.578 MB | 847.578 MB | n/a MB | n/a MB |
| python3 | 25050 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.711 MB | 10.711 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 25049 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25061 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.172 MB | 10.172 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 25060 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25065 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.828% | 68.521% | 2.760 s | 366.086 MB | 395.070 MB | 8888.707 MB | 10208.301 MB | n/a MB | n/a MB |
| MainThread | 25084 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.548% | 49.548% | 0.500 s | 225.197 MB | 261.375 MB | 1625.260 MB | 1656.297 MB | n/a MB | n/a MB |
| python3 | 25098 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.191 MB | 7.191 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 25097 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25115 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 39.103% | 74.452% | 2.370 s | 348.040 MB | 387.914 MB | 7764.931 MB | 10207.043 MB | n/a MB | n/a MB |
| MainThread | 25137 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.561% | 51.561% | 0.520 s | 213.432 MB | 259.141 MB | 1616.898 MB | 1655.324 MB | n/a MB | n/a MB |
| kimi | 25164 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 27.149% | 87.314% | 3.030 s | 342.647 MB | 395.965 MB | 8645.019 MB | 10208.254 MB | n/a MB | n/a MB |
| MainThread | 25183 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.250% | 54.250% | 0.550 s | 209.592 MB | 255.621 MB | 1611.912 MB | 1651.352 MB | n/a MB | n/a MB |
| python3 | 25207 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.188 MB | 7.188 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 25206 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25211 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 24.655% | 67.570% | 2.730 s | 363.005 MB | 395.102 MB | 8781.491 MB | 10210.941 MB | n/a MB | n/a MB |
| python3 | 25241 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.695 MB | 8.695 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 25240 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25233 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 44.715% | 44.715% | 0.450 s | 201.773 MB | 236.844 MB | 1607.520 MB | 1637.316 MB | n/a MB | n/a MB |
| MainThread | 25259 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 23.313% | 86.430% | 3.050 s | 355.755 MB | 397.613 MB | 8948.178 MB | 10208.707 MB | n/a MB | n/a MB |
| MainThread | 25278 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.581% | 52.581% | 0.530 s | 209.930 MB | 253.309 MB | 1613.533 MB | 1649.344 MB | n/a MB | n/a MB |
| MainThread | 25306 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 24.104% | 67.563% | 2.670 s | 362.551 MB | 392.426 MB | 8781.504 MB | 10208.633 MB | n/a MB | n/a MB |
| MainThread | 25326 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.515% | 61.515% | 0.620 s | 240.686 MB | 287.910 MB | 1648.648 MB | 1683.074 MB | n/a MB | n/a MB |
| MainThread | 25354 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 40.439% | 85.384% | 2.850 s | 327.019 MB | 387.746 MB | 8005.607 MB | 10204.934 MB | n/a MB | n/a MB |
| MainThread | 25373 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.455% | 61.455% | 0.620 s | 250.816 MB | 295.637 MB | 1654.725 MB | 1690.223 MB | n/a MB | n/a MB |
| MainThread | 25403 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 20.216% | 75.439% | 2.240 s | 367.030 MB | 388.492 MB | 9479.049 MB | 10208.125 MB | n/a MB | n/a MB |
| MainThread | 25422 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.560% | 58.560% | 0.590 s | 200.873 MB | 253.875 MB | 1476.859 MB | 1649.602 MB | n/a MB | n/a MB |
| sh | 25434 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25435 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.602 MB | 4.602 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| tar | 25444 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.621 MB | 1.621 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| tar | 25443 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.047 MB | 2.047 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| MainThread | 25450 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.179% | 82.340% | 2.920 s | 360.986 MB | 394.785 MB | 8878.603 MB | 10210.621 MB | n/a MB | n/a MB |
| MainThread | 25474 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 197.266 MB | 197.266 MB | 1616.504 MB | 1616.504 MB | n/a MB | n/a MB |
| MainThread | 25500 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 24.915% | 75.412% | 2.760 s | 361.441 MB | 396.488 MB | 8779.994 MB | 10211.234 MB | n/a MB | n/a MB |
| MainThread | 25522 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 47.557% | 47.557% | 0.480 s | 202.373 MB | 237.906 MB | 1607.916 MB | 1637.609 MB | n/a MB | n/a MB |
| sh | 25529 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25530 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.012 MB | 9.012 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 25548 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.852% | 71.466% | 2.200 s | 370.366 MB | 391.953 MB | 9479.820 MB | 10207.527 MB | n/a MB | n/a MB |
| MainThread | 25565 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.525% | 58.525% | 0.590 s | 209.324 MB | 259.594 MB | 1578.023 MB | 1656.078 MB | n/a MB | n/a MB |
| sh | 25572 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25573 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.605 MB | 10.605 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| python3 | 25582 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.105 MB | 8.105 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 25581 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.344 MB | 1.344 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25597 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 34.610% | 74.582% | 2.090 s | 358.338 MB | 389.367 MB | 8962.274 MB | 10205.430 MB | n/a MB | n/a MB |
| MainThread | 25616 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.557% | 53.557% | 0.540 s | 172.318 MB | 235.664 MB | 1459.773 MB | 1635.852 MB | n/a MB | n/a MB |
| git | 25643 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.059 MB | 4.059 MB | n/a MB | n/a MB |
| MainThread | 25646 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.181% | 70.616% | 2.680 s | 368.261 MB | 397.715 MB | 8890.071 MB | 10209.637 MB | n/a MB | n/a MB |
| sh | 25675 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25676 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.875 MB | 9.875 MB | 13.578 MB | 13.578 MB | n/a MB | n/a MB |
| MainThread | 25665 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.475% | 57.475% | 0.580 s | 239.654 MB | 285.316 MB | 1647.902 MB | 1681.332 MB | n/a MB | n/a MB |
| MainThread | 25696 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.437% | 74.583% | 2.160 s | 372.229 MB | 392.297 MB | 9483.072 MB | 10205.449 MB | n/a MB | n/a MB |
| MainThread | 25727 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 76.199% | 76.199% | 0.820 s | 209.760 MB | 296.980 MB | 1509.959 MB | 1723.566 MB | n/a MB | n/a MB |
| MainThread | 25746 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.416% | 77.248% | 2.470 s | 370.381 MB | 393.480 MB | 8893.334 MB | 10207.922 MB | n/a MB | n/a MB |
| python3 | 25790 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.773 MB | 10.773 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 25789 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25794 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.090 MB | 229.090 MB | 1631.590 MB | 1631.590 MB | n/a MB | n/a MB |
| sh | 25809 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25810 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.367 MB | 7.367 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 25814 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 42.385% | 69.539% | 2.560 s | 341.011 MB | 387.395 MB | 7758.596 MB | 10208.262 MB | n/a MB | n/a MB |
| python3 | 25845 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.551 MB | 7.551 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 25834 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.604% | 56.604% | 0.570 s | 248.457 MB | 291.254 MB | 1652.523 MB | 1686.066 MB | n/a MB | n/a MB |
| sh | 25844 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25862 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.556% | 77.199% | 2.390 s | 365.949 MB | 391.898 MB | 8788.946 MB | 10211.895 MB | n/a MB | n/a MB |
| python3 | 25881 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sh | 25880 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25891 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 211.770 MB | 211.770 MB | 1622.727 MB | 1622.727 MB | n/a MB | n/a MB |
| MainThread | 25910 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.171% | 86.475% | 2.920 s | 355.283 MB | 395.117 MB | 8856.399 MB | 10208.156 MB | n/a MB | n/a MB |
| kimi-code | 25937 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 49.773 MB | 49.773 MB | 851.352 MB | 851.352 MB | n/a MB | n/a MB |
| MainThread | 25929 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 48.698% | 48.698% | 0.490 s | 203.303 MB | 240.074 MB | 1608.023 MB | 1638.324 MB | n/a MB | n/a MB |
| MainThread | 25957 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.425% | 80.436% | 2.830 s | 359.821 MB | 391.770 MB | 8865.897 MB | 10208.109 MB | n/a MB | n/a MB |
| python3 | 25987 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.930 MB | 6.930 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 25986 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25979 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 41.645% | 41.645% | 0.420 s | 141.453 MB | 211.098 MB | 1453.221 MB | 1622.746 MB | n/a MB | n/a MB |
| MainThread | 26003 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.034% | 78.545% | 2.910 s | 360.823 MB | 397.246 MB | 8885.415 MB | 10208.543 MB | n/a MB | n/a MB |
| MainThread | 26025 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.865% | 55.865% | 0.570 s | 214.795 MB | 259.863 MB | 1617.393 MB | 1656.062 MB | n/a MB | n/a MB |
| MainThread | 26053 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 22.753% | 72.479% | 2.520 s | 365.400 MB | 395.238 MB | 8784.459 MB | 10212.160 MB | n/a MB | n/a MB |
| MainThread | 26072 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.550% | 58.550% | 0.590 s | 241.631 MB | 289.020 MB | 1649.014 MB | 1683.555 MB | n/a MB | n/a MB |
| sh | 26095 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 26096 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.223 MB | 9.223 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| MainThread | 26100 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 25.094% | 74.399% | 2.780 s | 363.806 MB | 397.121 MB | 8781.810 MB | 10211.281 MB | n/a MB | n/a MB |
| python3 | 26129 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.609 MB | 8.609 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 26128 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 26122 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 38.638% | 38.638% | 0.390 s | 152.098 MB | 219.988 MB | 1453.836 MB | 1623.977 MB | n/a MB | n/a MB |
| MainThread | 26148 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.007% | 77.396% | 2.780 s | 359.776 MB | 391.707 MB | 8888.659 MB | 10209.965 MB | n/a MB | n/a MB |
| MainThread | 26173 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 197.113 MB | 197.113 MB | 1616.242 MB | 1616.242 MB | n/a MB | n/a MB |
| MainThread | 26197 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 32.484% | 77.512% | 2.290 s | 359.462 MB | 397.113 MB | 9115.014 MB | 10212.617 MB | n/a MB | n/a MB |
| MainThread | 26218 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.547% | 52.547% | 0.530 s | 153.463 MB | 235.184 MB | 1460.143 MB | 1636.590 MB | n/a MB | n/a MB |
| python3 | 26217 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.859 MB | 8.859 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 26216 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 26319 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.059 MB | 5.059 MB | 11.383 MB | 11.383 MB | n/a MB | n/a MB |
| sh | 26318 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 26323 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 24.747% | 72.516% | 2.740 s | 359.956 MB | 394.391 MB | 8778.660 MB | 10211.285 MB | n/a MB | n/a MB |
| MainThread | 26342 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.564% | 58.564% | 0.590 s | 234.244 MB | 279.309 MB | 1634.395 MB | 1674.316 MB | n/a MB | n/a MB |
| MainThread | 26373 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.825% | 84.410% | 3.000 s | 361.317 MB | 394.074 MB | 8957.319 MB | 10213.141 MB | n/a MB | n/a MB |
| MainThread | 26394 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.340% | 61.340% | 0.630 s | 220.346 MB | 272.340 MB | 1622.754 MB | 1667.035 MB | n/a MB | n/a MB |
| sh | 26406 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 26407 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.816 MB | 8.816 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 26422 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.993% | 82.472% | 3.020 s | 361.797 MB | 392.387 MB | 8894.175 MB | 10214.133 MB | n/a MB | n/a MB |
| MainThread | 26455 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 260.539 MB | 260.539 MB | 1656.590 MB | 1656.590 MB | n/a MB | n/a MB |
| MainThread | 26472 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 24.626% | 73.460% | 2.480 s | 359.080 MB | 388.766 MB | 8656.618 MB | 10209.676 MB | n/a MB | n/a MB |
| MainThread | 26502 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 235.457 MB | 235.457 MB | 1636.340 MB | 1636.340 MB | n/a MB | n/a MB |
| MainThread | 26521 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.511% | 86.471% | 2.960 s | 356.044 MB | 394.797 MB | 8863.227 MB | 10214.648 MB | n/a MB | n/a MB |
| MainThread | 26551 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 295.238 MB | 295.238 MB | 1689.727 MB | 1689.727 MB | n/a MB | n/a MB |
| MainThread | 26570 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 34.118% | 68.602% | 2.060 s | 357.209 MB | 383.531 MB | 8961.588 MB | 10209.059 MB | n/a MB | n/a MB |
| MainThread | 26587 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.607% | 60.607% | 0.610 s | 233.707 MB | 278.254 MB | 1633.777 MB | 1673.332 MB | n/a MB | n/a MB |
| sh | 26601 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 26602 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.520 MB | 7.520 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 26617 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.331% | 81.398% | 2.940 s | 360.858 MB | 398.020 MB | 8865.044 MB | 10212.055 MB | n/a MB | n/a MB |
| MainThread | 26636 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.572% | 55.572% | 0.560 s | 215.418 MB | 260.406 MB | 1618.176 MB | 1656.879 MB | n/a MB | n/a MB |
| MainThread | 26664 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.276% | 85.492% | 3.010 s | 357.547 MB | 395.367 MB | 9036.011 MB | 10212.797 MB | n/a MB | n/a MB |
| MainThread | 26694 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 84.303% | 84.303% | 0.850 s | 169.008 MB | 295.113 MB | 1431.939 MB | 1689.555 MB | n/a MB | n/a MB |
| MainThread | 26713 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 19.865% | 80.529% | 2.400 s | 374.734 MB | 397.973 MB | 9539.056 MB | 10214.078 MB | n/a MB | n/a MB |
| sh | 26731 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 26732 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.145 MB | 10.145 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| python3 | 26747 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.371 MB | 9.371 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| sh | 26746 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 26736 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.469% | 61.469% | 0.620 s | 244.725 MB | 295.605 MB | 1652.346 MB | 1689.969 MB | n/a MB | n/a MB |
| MainThread | 26762 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 36.739% | 63.605% | 2.590 s | 347.569 MB | 394.242 MB | 8068.666 MB | 10212.457 MB | n/a MB | n/a MB |
| MainThread | 26782 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.501% | 58.501% | 0.590 s | 231.211 MB | 273.184 MB | 1631.275 MB | 1667.828 MB | n/a MB | n/a MB |
| MainThread | 26810 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.826% | 85.411% | 3.000 s | 350.076 MB | 396.074 MB | 8852.862 MB | 10213.363 MB | n/a MB | n/a MB |
| MainThread | 26838 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 288.445 MB | 288.445 MB | 1683.785 MB | 1683.785 MB | n/a MB | n/a MB |
| MainThread | 26860 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 21.408% | 73.475% | 2.170 s | 372.347 MB | 394.410 MB | 9418.022 MB | 10212.750 MB | n/a MB | n/a MB |
| MainThread | 26879 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.241% | 53.241% | 0.540 s | 192.678 MB | 237.121 MB | 1470.922 MB | 1637.348 MB | n/a MB | n/a MB |
| python3 | 26892 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.820 MB | 8.820 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 26891 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 26907 | sandbox_agent_lsb-kimi_0000_0000 | 40 | 7.963% | 76.442% | 3.130 s | 386.814 MB | 396.852 MB | 9995.632 MB | 10215.496 MB | n/a MB | n/a MB |
| bash | 26940 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.922 MB | 2.922 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 26941 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 12.886% | 64.441% | 0.780 s | 61.010 MB | 68.609 MB | 74.333 MB | 83.254 MB | n/a MB | n/a MB |
| python3 | 26944 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.527 MB | 21.527 MB | 27.070 MB | 27.070 MB | n/a MB | n/a MB |
| sh | 26943 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 26952 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 24.133% | 62.468% | 0.730 s | 57.653 MB | 67.906 MB | 71.091 MB | 82.773 MB | n/a MB | n/a MB |
| bash | 26951 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 26971 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 26972 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.797 MB | 17.797 MB | 23.184 MB | 23.184 MB | n/a MB | n/a MB |
| MainThread | 26981 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 26.434% | 76.402% | 2.930 s | 360.419 MB | 395.758 MB | 8779.083 MB | 10212.848 MB | n/a MB | n/a MB |
| kimi | 27002 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 46.523% | 46.523% | 0.470 s | 108.285 MB | 216.570 MB | 811.684 MB | 1623.238 MB | n/a MB | n/a MB |
| MainThread | 27028 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 17.461% | 72.598% | 2.460 s | 374.746 MB | 401.484 MB | 9064.424 MB | 10203.293 MB | n/a MB | n/a MB |
| MainThread | 27055 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 237.051 MB | 237.051 MB | 1637.855 MB | 1637.855 MB | n/a MB | n/a MB |
| tar | 27069 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.129 MB | 2.129 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 27070 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| python3 | 27075 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.715 MB | 10.715 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 27074 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27079 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 38.684% | 66.444% | 2.350 s | 339.611 MB | 383.004 MB | 7750.049 MB | 10192.238 MB | n/a MB | n/a MB |
| MainThread | 27097 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.563% | 57.563% | 0.580 s | 171.344 MB | 236.641 MB | 1460.262 MB | 1636.828 MB | n/a MB | n/a MB |
| sh | 27115 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi | 27125 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 22.864% | 86.144% | 3.230 s | 352.296 MB | 396.852 MB | 8948.659 MB | 10213.027 MB | n/a MB | n/a MB |
| MainThread | 27142 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.507% | 64.507% | 0.650 s | 241.973 MB | 294.527 MB | 1641.883 MB | 1689.293 MB | n/a MB | n/a MB |
| tar | 27167 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.039 MB | 2.039 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| tar | 27168 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| MainThread | 27175 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.985% | 85.489% | 3.140 s | 354.392 MB | 396.488 MB | 8854.642 MB | 10213.223 MB | n/a MB | n/a MB |
| MainThread | 27194 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.549% | 57.549% | 0.580 s | 203.434 MB | 252.176 MB | 1479.596 MB | 1648.320 MB | n/a MB | n/a MB |
| python3 | 27208 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.008 MB | 8.008 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 27207 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.488 MB | 1.488 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27221 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.974% | 74.556% | 2.910 s | 366.353 MB | 389.129 MB | 8991.006 MB | 10215.152 MB | n/a MB | n/a MB |
| MainThread | 27243 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.285% | 55.285% | 0.560 s | 251.617 MB | 294.613 MB | 1654.664 MB | 1689.832 MB | n/a MB | n/a MB |
| MainThread | 27271 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 22.929% | 76.447% | 2.310 s | 370.609 MB | 395.637 MB | 9415.203 MB | 10212.711 MB | n/a MB | n/a MB |
| sh | 27289 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27290 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.297 MB | 9.297 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| MainThread | 27291 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.542% | 53.542% | 0.540 s | 155.189 MB | 234.324 MB | 1459.773 MB | 1635.852 MB | n/a MB | n/a MB |
| MainThread | 27319 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.198% | 75.530% | 2.440 s | 341.646 MB | 394.605 MB | 8123.711 MB | 10212.863 MB | n/a MB | n/a MB |
| python3 | 27337 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.734 MB | 8.734 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 27338 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 52.087% | 55.515% | 1.050 s | 189.984 MB | 297.953 MB | 1511.312 MB | 1724.254 MB | n/a MB | n/a MB |
| sh | 27336 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27368 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 25.319% | 77.334% | 2.550 s | 364.644 MB | 394.871 MB | 8655.741 MB | 10212.758 MB | n/a MB | n/a MB |
| MainThread | 27391 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 43.729% | 43.729% | 0.440 s | 197.488 MB | 234.223 MB | 1567.912 MB | 1635.355 MB | n/a MB | n/a MB |
| MainThread | 27415 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 22.326% | 77.583% | 2.270 s | 372.762 MB | 397.594 MB | 9422.219 MB | 10212.473 MB | n/a MB | n/a MB |
| MainThread | 27444 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 161.133 MB | 161.133 MB | 1500.469 MB | 1500.469 MB | n/a MB | n/a MB |
| MainThread | 27463 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.996% | 70.470% | 2.560 s | 368.736 MB | 394.660 MB | 8894.407 MB | 10209.801 MB | n/a MB | n/a MB |
| sh | 27486 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27487 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.066 MB | 9.066 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 27491 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 212.980 MB | 212.980 MB | 1623.250 MB | 1623.250 MB | n/a MB | n/a MB |
| MainThread | 27510 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.466% | 73.491% | 2.680 s | 367.887 MB | 394.770 MB | 8986.216 MB | 10210.020 MB | n/a MB | n/a MB |
| MainThread | 27530 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.558% | 49.558% | 0.500 s | 233.297 MB | 271.359 MB | 1641.129 MB | 1666.785 MB | n/a MB | n/a MB |
| python3 | 27558 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.895 MB | 10.895 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 27557 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27562 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.872% | 69.452% | 2.890 s | 368.293 MB | 395.855 MB | 8983.004 MB | 10211.910 MB | n/a MB | n/a MB |
| MainThread | 27579 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.600% | 58.600% | 0.590 s | 142.209 MB | 235.008 MB | 1437.102 MB | 1635.594 MB | n/a MB | n/a MB |
| python3 | 27599 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.422 MB | 7.422 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 27598 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| tar | 27603 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.234 MB | 2.234 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 27604 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| MainThread | 27610 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.273% | 66.652% | 2.690 s | 368.607 MB | 398.688 MB | 8890.198 MB | 10209.363 MB | n/a MB | n/a MB |
| MainThread | 27629 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.612% | 57.612% | 0.580 s | 201.410 MB | 254.262 MB | 1477.158 MB | 1649.570 MB | n/a MB | n/a MB |
| MainThread | 27659 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.695% | 79.449% | 2.870 s | 363.403 MB | 398.461 MB | 8886.593 MB | 10209.520 MB | n/a MB | n/a MB |
| MainThread | 27682 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 202.445 MB | 202.445 MB | 1618.227 MB | 1618.227 MB | n/a MB | n/a MB |
| MainThread | 27708 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.501% | 65.419% | 2.720 s | 373.002 MB | 400.109 MB | 8897.482 MB | 10214.465 MB | n/a MB | n/a MB |
| MainThread | 27741 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 197.883 MB | 197.883 MB | 1616.727 MB | 1616.727 MB | n/a MB | n/a MB |
| kimi-code | 27758 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.369% | 71.601% | 2.170 s | 379.106 MB | 399.812 MB | 9486.694 MB | 10209.203 MB | n/a MB | n/a MB |
| MainThread | 27777 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.514% | 57.514% | 0.580 s | 213.953 MB | 261.238 MB | 1617.270 MB | 1656.566 MB | n/a MB | n/a MB |
| python3 | 27790 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.816 MB | 8.816 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 27789 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27805 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 18.556% | 76.571% | 2.260 s | 376.558 MB | 395.801 MB | 9538.138 MB | 10209.383 MB | n/a MB | n/a MB |
| MainThread | 27824 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.029% | 53.029% | 0.540 s | 195.004 MB | 236.668 MB | 1473.422 MB | 1637.605 MB | n/a MB | n/a MB |
| python3 | 27837 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.059 MB | 9.059 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 27836 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27854 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 17.686% | 76.402% | 2.150 s | 369.739 MB | 392.379 MB | 8863.575 MB | 10204.992 MB | n/a MB | n/a MB |
| MainThread | 27883 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 259.941 MB | 259.941 MB | 1655.555 MB | 1655.555 MB | n/a MB | n/a MB |
| MainThread | 27902 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 32.023% | 81.436% | 2.260 s | 357.708 MB | 395.223 MB | 9103.268 MB | 10216.328 MB | n/a MB | n/a MB |
| MainThread | 27924 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.424% | 60.424% | 0.610 s | 243.850 MB | 294.250 MB | 1644.000 MB | 1689.277 MB | n/a MB | n/a MB |
| MainThread | 27948 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 18.838% | 77.437% | 2.320 s | 376.043 MB | 395.488 MB | 9542.425 MB | 10212.121 MB | n/a MB | n/a MB |
| MainThread | 27971 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 220.137 MB | 220.137 MB | 1624.238 MB | 1624.238 MB | n/a MB | n/a MB |
| MainThread | 27997 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 25.008% | 66.544% | 2.770 s | 363.715 MB | 395.121 MB | 8779.845 MB | 10209.156 MB | n/a MB | n/a MB |
| MainThread | 28016 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.588% | 53.588% | 0.540 s | 230.475 MB | 267.680 MB | 1630.758 MB | 1663.043 MB | n/a MB | n/a MB |
| python3 | 28028 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.617 MB | 6.617 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 28027 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28045 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.076% | 63.631% | 2.830 s | 373.210 MB | 399.926 MB | 9069.167 MB | 10214.609 MB | n/a MB | n/a MB |
| sh | 28073 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28066 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 37.661% | 37.661% | 0.380 s | 148.654 MB | 211.098 MB | 1453.082 MB | 1622.469 MB | n/a MB | n/a MB |
| python3 | 28074 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.320 MB | 7.320 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 28114 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 22.656% | 73.475% | 2.510 s | 368.181 MB | 395.598 MB | 8785.461 MB | 10212.020 MB | n/a MB | n/a MB |
| MainThread | 28144 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 206.918 MB | 206.918 MB | 1619.211 MB | 1619.211 MB | n/a MB | n/a MB |
| MainThread | 28163 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 21.275% | 76.437% | 2.570 s | 369.443 MB | 396.590 MB | 8892.667 MB | 10209.492 MB | n/a MB | n/a MB |
| MainThread | 28184 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.655% | 55.655% | 0.560 s | 246.531 MB | 287.395 MB | 1650.367 MB | 1681.785 MB | n/a MB | n/a MB |
| MainThread | 28212 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 23.888% | 85.446% | 3.130 s | 353.577 MB | 399.566 MB | 8946.671 MB | 10214.395 MB | n/a MB | n/a MB |
| python3 | 28236 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.836 MB | 10.836 MB | 14.730 MB | 14.730 MB | n/a MB | n/a MB |
| MainThread | 28229 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.641% | 61.641% | 0.630 s | 202.803 MB | 259.438 MB | 1478.652 MB | 1655.070 MB | n/a MB | n/a MB |
| sh | 28230 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28260 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.496% | 74.403% | 2.840 s | 365.562 MB | 398.488 MB | 8890.550 MB | 10213.137 MB | n/a MB | n/a MB |
| MainThread | 28282 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 31.727% | 31.727% | 0.320 s | 183.172 MB | 211.504 MB | 1466.799 MB | 1622.727 MB | n/a MB | n/a MB |
| MainThread | 28308 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.856% | 79.526% | 2.420 s | 372.099 MB | 397.578 MB | 9481.944 MB | 10212.609 MB | n/a MB | n/a MB |
| python3 | 28327 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.738 MB | 7.738 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 28326 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28328 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 51.130% | 59.559% | 1.030 s | 190.829 MB | 298.504 MB | 1510.633 MB | 1724.316 MB | n/a MB | n/a MB |
| MainThread | 28356 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.339% | 72.414% | 2.820 s | 368.214 MB | 399.621 MB | 8888.500 MB | 10209.895 MB | n/a MB | n/a MB |
| MainThread | 28378 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 206.012 MB | 206.012 MB | 1619.020 MB | 1619.020 MB | n/a MB | n/a MB |
| MainThread | 28404 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 19.344% | 77.428% | 2.340 s | 369.472 MB | 391.832 MB | 9538.947 MB | 10211.250 MB | n/a MB | n/a MB |
| python3 | 28424 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.215 MB | 9.215 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 28423 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.352 MB | 1.352 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 28430 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sh | 28429 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28434 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.684 MB | 228.684 MB | 1635.840 MB | 1635.840 MB | n/a MB | n/a MB |
| MainThread | 28453 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 17.481% | 73.470% | 2.320 s | 378.335 MB | 397.023 MB | 9589.849 MB | 10213.637 MB | n/a MB | n/a MB |
| MainThread | 28473 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.262% | 54.262% | 0.550 s | 164.336 MB | 234.645 MB | 1459.516 MB | 1635.336 MB | n/a MB | n/a MB |
| python3 | 28486 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.086 MB | 10.086 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 28485 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28501 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.608% | 68.530% | 2.740 s | 366.464 MB | 392.664 MB | 8987.501 MB | 10212.707 MB | n/a MB | n/a MB |
| MainThread | 28520 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.098% | 57.098% | 0.620 s | 248.043 MB | 294.762 MB | 1653.512 MB | 1689.305 MB | n/a MB | n/a MB |
| python3 | 28532 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.031 MB | 9.031 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 28531 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28549 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.074% | 85.419% | 3.030 s | 352.578 MB | 397.781 MB | 8855.845 MB | 10212.527 MB | n/a MB | n/a MB |
| MainThread | 28571 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 206.047 MB | 206.047 MB | 1619.215 MB | 1619.215 MB | n/a MB | n/a MB |
| MainThread | 28597 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 26.934% | 84.379% | 2.990 s | 349.395 MB | 394.254 MB | 8745.586 MB | 10212.871 MB | n/a MB | n/a MB |
| MainThread | 28626 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 71.287% | 71.287% | 0.720 s | 223.279 MB | 286.426 MB | 1498.635 MB | 1681.551 MB | n/a MB | n/a MB |
| MainThread | 28643 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 22.881% | 75.923% | 2.540 s | 372.481 MB | 400.836 MB | 8787.484 MB | 10214.766 MB | n/a MB | n/a MB |
| MainThread | 28665 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.662% | 55.662% | 0.560 s | 237.494 MB | 278.418 MB | 1644.666 MB | 1673.344 MB | n/a MB | n/a MB |
| MainThread | 28693 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 17.606% | 77.592% | 2.480 s | 377.670 MB | 398.715 MB | 9629.127 MB | 10215.387 MB | n/a MB | n/a MB |
| MainThread | 28714 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 49.628% | 52.509% | 1.000 s | 206.566 MB | 295.863 MB | 1535.546 MB | 1690.969 MB | n/a MB | n/a MB |
| python3 | 28713 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.117 MB | 10.117 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 28712 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28745 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.180% | 75.413% | 2.930 s | 361.145 MB | 393.891 MB | 8885.201 MB | 10213.484 MB | n/a MB | n/a MB |
| sh | 28772 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 28773 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.156 MB | 10.156 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 28764 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.078 MB | 229.078 MB | 1631.953 MB | 1631.953 MB | n/a MB | n/a MB |
| MainThread | 28794 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 21.684% | 75.473% | 2.620 s | 370.451 MB | 398.555 MB | 8895.446 MB | 10213.891 MB | n/a MB | n/a MB |
| MainThread | 28816 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 43.661% | 43.661% | 0.440 s | 197.189 MB | 234.789 MB | 1567.617 MB | 1635.266 MB | n/a MB | n/a MB |
| git | 28840 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.508 MB | 1.508 MB | 6.684 MB | 6.684 MB | n/a MB | n/a MB |
| MainThread | 28843 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.590% | 65.532% | 2.730 s | 368.820 MB | 401.719 MB | 8893.947 MB | 10214.977 MB | n/a MB | n/a MB |
| kimi-code | 28856 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.852 MB | 16.852 MB | 706.980 MB | 706.980 MB | n/a MB | n/a MB |
| sh | 28865 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 28866 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.207 MB | 9.207 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| MainThread | 28870 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 177.492 MB | 177.492 MB | 1590.973 MB | 1590.973 MB | n/a MB | n/a MB |
| MainThread | 28894 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.055% | 65.443% | 2.970 s | 367.396 MB | 394.082 MB | 9064.740 MB | 10213.074 MB | n/a MB | n/a MB |
| kimi | 28912 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.445% | 56.445% | 0.570 s | 114.631 MB | 229.262 MB | 898.002 MB | 1635.859 MB | n/a MB | n/a MB |
| sh | 28930 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 28931 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.367 MB | 7.367 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 28942 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 25.145% | 68.449% | 2.790 s | 362.142 MB | 397.281 MB | 8781.076 MB | 10214.117 MB | n/a MB | n/a MB |
| MainThread | 28970 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 167.996 MB | 167.996 MB | 1578.473 MB | 1578.473 MB | n/a MB | n/a MB |
| MainThread | 28992 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.706% | 70.615% | 2.500 s | 368.980 MB | 393.043 MB | 8896.505 MB | 10207.645 MB | n/a MB | n/a MB |
| MainThread | 29020 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 189.074 MB | 189.074 MB | 1594.223 MB | 1594.223 MB | n/a MB | n/a MB |
| MainThread | 29039 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.445% | 77.454% | 2.600 s | 376.716 MB | 401.125 MB | 9072.055 MB | 10215.367 MB | n/a MB | n/a MB |
| MainThread | 29062 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 42.675% | 42.675% | 0.430 s | 206.240 MB | 237.320 MB | 1614.158 MB | 1638.094 MB | n/a MB | n/a MB |
| MainThread | 29091 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 20.667% | 77.490% | 2.290 s | 376.487 MB | 399.398 MB | 9486.536 MB | 10213.918 MB | n/a MB | n/a MB |
| sh | 29110 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29111 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.117 MB | 10.117 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 29112 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 51.051% | 56.462% | 1.030 s | 206.618 MB | 304.113 MB | 1549.389 MB | 1728.152 MB | n/a MB | n/a MB |
| MainThread | 29140 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.315% | 63.533% | 2.680 s | 369.351 MB | 392.562 MB | 8988.905 MB | 10213.738 MB | n/a MB | n/a MB |
| MainThread | 29172 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.574% | 58.574% | 0.590 s | 205.719 MB | 259.855 MB | 1577.549 MB | 1655.879 MB | n/a MB | n/a MB |
| MainThread | 29203 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.496% | 69.502% | 2.720 s | 369.423 MB | 397.211 MB | 8894.276 MB | 10213.812 MB | n/a MB | n/a MB |
| MainThread | 29227 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 38.727% | 38.727% | 0.390 s | 180.549 MB | 219.820 MB | 1460.818 MB | 1624.211 MB | n/a MB | n/a MB |
| MainThread | 29254 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 17.170% | 69.445% | 2.940 s | 374.110 MB | 398.945 MB | 9255.132 MB | 10209.969 MB | n/a MB | n/a MB |
| MainThread | 29273 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.460% | 52.460% | 0.530 s | 211.938 MB | 254.676 MB | 1614.283 MB | 1649.844 MB | n/a MB | n/a MB |
| kimi-code | 29298 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 64.930 MB | 64.930 MB | 900.188 MB | 900.188 MB | n/a MB | n/a MB |
| MainThread | 29301 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.184% | 80.534% | 2.920 s | 361.389 MB | 395.949 MB | 8882.843 MB | 10212.625 MB | n/a MB | n/a MB |
| git | 29323 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| MainThread | 29329 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 71.573% | 71.573% | 0.720 s | 231.662 MB | 296.137 MB | 1634.344 MB | 1690.465 MB | n/a MB | n/a MB |
| MainThread | 29351 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 21.342% | 76.374% | 2.580 s | 370.556 MB | 395.391 MB | 8895.876 MB | 10213.387 MB | n/a MB | n/a MB |
| stty | 29369 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 29375 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 44.613% | 44.613% | 0.450 s | 194.529 MB | 234.750 MB | 1567.426 MB | 1635.383 MB | n/a MB | n/a MB |
| MainThread | 29401 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.480% | 77.448% | 2.380 s | 374.114 MB | 399.320 MB | 8800.842 MB | 10213.547 MB | n/a MB | n/a MB |
| MainThread | 29422 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.555% | 55.555% | 0.560 s | 225.986 MB | 272.168 MB | 1629.135 MB | 1667.297 MB | n/a MB | n/a MB |
| MainThread | 29448 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.950% | 73.601% | 2.530 s | 368.877 MB | 391.898 MB | 8894.707 MB | 10207.770 MB | n/a MB | n/a MB |
| python3 | 29479 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.746 MB | 9.746 MB | 13.734 MB | 13.734 MB | n/a MB | n/a MB |
| sh | 29478 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 29470 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 46.629% | 46.629% | 0.470 s | 211.580 MB | 253.586 MB | 1614.025 MB | 1649.328 MB | n/a MB | n/a MB |
| MainThread | 29496 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 23.777% | 84.479% | 3.110 s | 354.297 MB | 392.715 MB | 8952.607 MB | 10213.188 MB | n/a MB | n/a MB |
| MainThread | 29525 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 187.570 MB | 187.570 MB | 1593.973 MB | 1593.973 MB | n/a MB | n/a MB |
| MainThread | 29544 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.785% | 65.481% | 2.800 s | 370.148 MB | 394.715 MB | 9069.179 MB | 10213.875 MB | n/a MB | n/a MB |
| sh | 29572 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 29565 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 36.678% | 36.678% | 0.370 s | 140.719 MB | 205.215 MB | 1451.219 MB | 1618.742 MB | n/a MB | n/a MB |
| python3 | 29573 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.191 MB | 6.191 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 29591 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.424% | 79.465% | 3.020 s | 365.377 MB | 392.844 MB | 9065.464 MB | 10214.191 MB | n/a MB | n/a MB |
| MainThread | 29611 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.576% | 60.576% | 0.610 s | 220.471 MB | 271.965 MB | 1622.766 MB | 1666.809 MB | n/a MB | n/a MB |
| sh | 29623 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29624 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.898 MB | 6.898 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 29639 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.287% | 70.497% | 2.720 s | 370.572 MB | 396.125 MB | 9071.541 MB | 10214.246 MB | n/a MB | n/a MB |
| MainThread | 29659 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.523% | 58.523% | 0.590 s | 239.809 MB | 285.664 MB | 1647.812 MB | 1680.902 MB | n/a MB | n/a MB |
| MainThread | 29688 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.483% | 82.492% | 3.080 s | 356.278 MB | 396.477 MB | 8857.440 MB | 10210.379 MB | n/a MB | n/a MB |
| MainThread | 29718 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 235.324 MB | 235.324 MB | 1635.590 MB | 1635.590 MB | n/a MB | n/a MB |
| sh | 29732 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29733 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.914 MB | 7.914 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| MainThread | 29737 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.641% | 75.386% | 2.980 s | 362.436 MB | 397.625 MB | 8889.974 MB | 10217.473 MB | n/a MB | n/a MB |
| sh | 29763 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29764 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.367 MB | 7.367 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 29755 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.404% | 61.404% | 0.620 s | 257.443 MB | 303.090 MB | 1674.906 MB | 1727.332 MB | n/a MB | n/a MB |
| sh | 29767 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| tar | 29778 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.035 MB | 2.035 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 29779 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.242 MB | 1.242 MB | n/a MB | n/a MB |
| MainThread | 29785 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 22.259% | 82.420% | 3.140 s | 368.061 MB | 402.188 MB | 9045.218 MB | 10216.957 MB | n/a MB | n/a MB |
| MainThread | 29813 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 182.613 MB | 182.613 MB | 1592.723 MB | 1592.723 MB | n/a MB | n/a MB |
| MainThread | 29835 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 19.048% | 64.545% | 2.880 s | 375.305 MB | 400.102 MB | 9136.701 MB | 10212.176 MB | n/a MB | n/a MB |
| MainThread | 29854 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 53.975% | 58.475% | 1.090 s | 199.979 MB | 303.949 MB | 1533.243 MB | 1728.395 MB | n/a MB | n/a MB |
| python3 | 29869 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.840 MB | 9.840 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 29868 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 29883 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29884 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.270 MB | 9.270 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 29888 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.157% | 74.559% | 2.990 s | 366.861 MB | 394.863 MB | 9063.747 MB | 10207.730 MB | n/a MB | n/a MB |
| git | 29908 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.887 MB | 2.887 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| MainThread | 29919 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.918 MB | 229.918 MB | 1631.961 MB | 1631.961 MB | n/a MB | n/a MB |
| MainThread | 29938 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 23.903% | 68.465% | 3.180 s | 366.218 MB | 393.898 MB | 8988.124 MB | 10217.508 MB | n/a MB | n/a MB |
| MainThread | 29960 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 42.427% | 42.427% | 0.430 s | 136.314 MB | 211.074 MB | 1430.664 MB | 1622.719 MB | n/a MB | n/a MB |
| MainThread | 29989 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 22.217% | 76.481% | 2.460 s | 372.573 MB | 397.895 MB | 8785.351 MB | 10210.402 MB | n/a MB | n/a MB |
| MainThread | 30013 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 45.665% | 45.665% | 0.460 s | 203.135 MB | 239.984 MB | 1608.029 MB | 1638.336 MB | n/a MB | n/a MB |
| python3 | 30039 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 20.246% | 86.364% | 3.270 s | 370.462 MB | 401.305 MB | 9156.641 MB | 10216.340 MB | n/a MB | n/a MB |
| MainThread | 30056 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.528% | 62.528% | 0.630 s | 237.066 MB | 286.828 MB | 1637.893 MB | 1682.062 MB | n/a MB | n/a MB |
| MainThread | 30087 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.166% | 78.519% | 2.380 s | 373.302 MB | 397.539 MB | 8798.444 MB | 10212.285 MB | n/a MB | n/a MB |
| python3 | 30113 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.762 MB | 9.762 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 30112 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.352 MB | 1.352 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30115 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.948% | 49.948% | 0.550 s | 189.051 MB | 238.031 MB | 1467.223 MB | 1638.094 MB | n/a MB | n/a MB |
| sh | 30131 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 30132 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.020 MB | 11.020 MB | 14.730 MB | 14.730 MB | n/a MB | n/a MB |
| MainThread | 30136 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.678% | 83.344% | 2.990 s | 366.415 MB | 401.938 MB | 8886.307 MB | 10217.672 MB | n/a MB | n/a MB |
| MainThread | 30155 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.470% | 54.470% | 0.560 s | 213.400 MB | 260.387 MB | 1616.791 MB | 1655.609 MB | n/a MB | n/a MB |
| python3 | 30169 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.910 MB | 6.910 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 30168 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30202 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.947% | 80.548% | 2.480 s | 379.405 MB | 402.121 MB | 9587.754 MB | 10216.215 MB | n/a MB | n/a MB |
| sh | 30220 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 30221 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| MainThread | 30222 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.649% | 55.649% | 0.560 s | 259.045 MB | 296.285 MB | 1657.631 MB | 1691.004 MB | n/a MB | n/a MB |
| MainThread | 30253 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 20.062% | 77.401% | 3.030 s | 369.300 MB | 398.887 MB | 9133.879 MB | 10213.945 MB | n/a MB | n/a MB |
| MainThread | 30273 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.504% | 60.504% | 0.610 s | 251.645 MB | 294.789 MB | 1654.367 MB | 1689.035 MB | n/a MB | n/a MB |
| MainThread | 30304 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.300% | 80.551% | 2.400 s | 375.696 MB | 393.742 MB | 9588.225 MB | 10214.836 MB | n/a MB | n/a MB |
| MainThread | 30327 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.889% | 52.889% | 0.540 s | 217.389 MB | 259.574 MB | 1622.773 MB | 1655.324 MB | n/a MB | n/a MB |
| sh | 30337 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 30338 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30351 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.839% | 75.384% | 2.880 s | 363.042 MB | 396.402 MB | 8889.584 MB | 10213.258 MB | n/a MB | n/a MB |
| MainThread | 30379 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 80.354% | 80.354% | 0.810 s | 225.006 MB | 302.164 MB | 1579.582 MB | 1726.852 MB | n/a MB | n/a MB |
| MainThread | 30400 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 22.205% | 82.485% | 3.160 s | 363.282 MB | 399.285 MB | 9039.488 MB | 10213.727 MB | n/a MB | n/a MB |
| sh | 30433 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30423 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.907% | 56.907% | 0.620 s | 238.020 MB | 288.812 MB | 1638.900 MB | 1683.578 MB | n/a MB | n/a MB |
| python3 | 30434 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.980 MB | 7.980 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python3 | 30445 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.641 MB | 7.641 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 30444 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30449 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.762% | 79.482% | 2.980 s | 365.831 MB | 397.602 MB | 8981.928 MB | 10214.199 MB | n/a MB | n/a MB |
| MainThread | 30468 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.493% | 53.493% | 0.540 s | 215.590 MB | 260.871 MB | 1617.516 MB | 1655.809 MB | n/a MB | n/a MB |
| sh | 30482 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 30483 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.395 MB | 7.395 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 30498 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 21.257% | 74.518% | 2.570 s | 375.723 MB | 402.016 MB | 8898.852 MB | 10216.039 MB | n/a MB | n/a MB |
| MainThread | 30539 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.283% | 73.522% | 2.720 s | 376.898 MB | 400.719 MB | 9072.502 MB | 10215.855 MB | n/a MB | n/a MB |
| MainThread | 30559 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.513% | 56.513% | 0.570 s | 247.008 MB | 288.898 MB | 1651.121 MB | 1683.539 MB | n/a MB | n/a MB |
| MainThread | 30590 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.635% | 66.558% | 2.910 s | 371.920 MB | 402.453 MB | 9069.223 MB | 10215.715 MB | n/a MB | n/a MB |
| MainThread | 30611 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.492% | 59.492% | 0.600 s | 217.574 MB | 260.484 MB | 1619.641 MB | 1657.309 MB | n/a MB | n/a MB |
| MainThread | 30642 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 22.922% | 86.412% | 3.230 s | 354.714 MB | 397.551 MB | 9029.493 MB | 10216.375 MB | n/a MB | n/a MB |
| MainThread | 30661 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.572% | 62.572% | 0.630 s | 238.312 MB | 287.020 MB | 1638.148 MB | 1681.824 MB | n/a MB | n/a MB |
| MainThread | 30694 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 18.228% | 81.366% | 3.150 s | 371.258 MB | 398.004 MB | 9253.143 MB | 10215.598 MB | n/a MB | n/a MB |
| git | 30713 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 30716 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.117 MB | 229.117 MB | 1632.238 MB | 1632.238 MB | n/a MB | n/a MB |
| MainThread | 30746 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.140% | 69.517% | 2.770 s | 370.164 MB | 396.777 MB | 8989.035 MB | 10213.859 MB | n/a MB | n/a MB |
| MainThread | 30769 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 34.730% | 34.730% | 0.350 s | 187.471 MB | 217.277 MB | 1469.178 MB | 1623.469 MB | n/a MB | n/a MB |
| MainThread | 30795 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.264% | 79.496% | 2.660 s | 361.497 MB | 392.906 MB | 8958.443 MB | 10186.555 MB | n/a MB | n/a MB |
| MainThread | 30812 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.385% | 58.385% | 0.590 s | 217.592 MB | 262.215 MB | 1618.531 MB | 1657.340 MB | n/a MB | n/a MB |
| sh | 30827 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 30828 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.859 MB | 9.859 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| MainThread | 30841 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 22.630% | 86.405% | 3.190 s | 358.404 MB | 400.398 MB | 9034.770 MB | 10214.160 MB | n/a MB | n/a MB |
| MainThread | 30863 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 50.098% | 57.519% | 1.010 s | 223.016 MB | 300.086 MB | 1553.177 MB | 1725.336 MB | n/a MB | n/a MB |
| python3 | 30862 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.707 MB | 9.707 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| sh | 30861 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30892 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.001% | 68.501% | 2.880 s | 370.179 MB | 398.688 MB | 8989.783 MB | 10216.395 MB | n/a MB | n/a MB |
| MainThread | 30928 | sandbox_agent_lsb-kimi_0000_0000 | 187 | 4.677% | 72.409% | 8.820 s | 387.947 MB | 406.070 MB | 10113.963 MB | 10219.965 MB | n/a MB | n/a MB |
| MainThread | 30948 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.962% | 63.962% | 0.650 s | 217.881 MB | 270.707 MB | 1619.260 MB | 1665.547 MB | n/a MB | n/a MB |
| git | 30956 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.035 MB | 4.035 MB | n/a MB | n/a MB |
| python | 30991 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2339.531 MB | 2339.531 MB | 2657.141 MB | 2657.141 MB | n/a MB | n/a MB |
| bash | 30990 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.656 MB | 2.656 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 31025 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31026 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.680 MB | 14.680 MB | 20.082 MB | 20.082 MB | n/a MB | n/a MB |
| bash | 31037 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.551 MB | 2.551 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 31038 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 31.271% | 62.542% | 0.630 s | 54.626 MB | 66.363 MB | 67.022 MB | 80.102 MB | n/a MB | n/a MB |
| python3 | 31040 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.895 MB | 7.895 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 31039 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31045 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| sh | 31044 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31060 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.359 MB | 21.359 MB | 27.066 MB | 27.066 MB | n/a MB | n/a MB |
| sh | 31059 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 31066 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.738 MB | 2.738 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 31067 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2279.422 MB | 2279.422 MB | 2655.004 MB | 2655.004 MB | n/a MB | n/a MB |
| python | 31089 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.898 MB | 13.898 MB | 207.594 MB | 207.594 MB | n/a MB | n/a MB |
| bash | 31088 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 90.068% | 100.469% | 6.340 s | 1.500 MB | 2.844 MB | 2.634 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 31099 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.289 MB | 8.289 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 31098 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 31114 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.801 MB | 2.801 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 31115 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 79.328 MB | 79.328 MB | 303.590 MB | 303.590 MB | n/a MB | n/a MB |
| sh | 31132 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31133 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.859 MB | 20.859 MB | 25.707 MB | 25.707 MB | n/a MB | n/a MB |
| python | 31140 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 107.162% | 114.001% | 2.160 s | 990.182 MB | 1745.883 MB | 1317.513 MB | 1969.621 MB | n/a MB | n/a MB |
| bash | 31139 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.805 MB | 2.805 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 31158 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 31159 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 43.824 MB | 43.824 MB | 52.672 MB | 52.672 MB | n/a MB | n/a MB |
| python3 | 31162 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sh | 31161 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 31169 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 45.273 MB | 45.273 MB | 53.426 MB | 53.426 MB | n/a MB | n/a MB |
| bash | 31168 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.699 MB | 2.699 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 31171 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.848 MB | 9.848 MB | 13.844 MB | 13.844 MB | n/a MB | n/a MB |
| sh | 31170 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| docker | 31214 |  | 22 | 0.000% | 0.000% | 0.000 s | 29.578 MB | 29.578 MB | 1771.195 MB | 1771.195 MB | 0.000000 MB | 0.000000 MB |
| docker | 31331 |  | 1 | n/a% | n/a% | n/a s | 21.965 MB | 21.965 MB | 1625.848 MB | 1625.848 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6.484% | 100.000% | 13891.804 MB | 19048.000 MB | 31.703 W | 76.642 W | 149355.546 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-kimi_0000_0000 | 81.063% | 228.729% | 3813.970 s | 443.018 MB | 2395.117 MB | 219.500000 MB | 702.777344 MB | 421.597801 MB | 5.658074 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 15346 | 4711.276 | interrupted |
| harness:retire | -1 | 0.128 | interrupted |
| harness:retire | -1 | 0.123 | interrupted |
| harness:retire | -1 | 0.120 | interrupted |
| harness:retire | -1 | 0.119 | interrupted |
| harness:retire | -1 | 0.119 | interrupted |
| harness:retire | -1 | 0.118 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.116 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.113 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.112 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.111 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.110 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.109 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.108 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.105 | interrupted |
| harness:retire | -1 | 0.105 | interrupted |
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
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
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
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.098 | interrupted |
| harness:retire | -1 | 0.098 | interrupted |
| harness:retire | -1 | 0.098 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.097 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.093 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.092 | interrupted |
| harness:retire | -1 | 0.091 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
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
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.085 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
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
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.080 | interrupted |
| harness:retire | -1 | 0.080 | interrupted |
| harness:retire | -1 | 0.080 | interrupted |
| harness:retire | -1 | 0.080 | interrupted |
| harness:retire | -1 | 0.080 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.078 | interrupted |
| harness:retire | -1 | 0.078 | interrupted |
| harness:retire | -1 | 0.077 | interrupted |
| harness:retire | -1 | 0.077 | interrupted |
| harness:retire | -1 | 0.077 | interrupted |
| harness:retire | -1 | 0.077 | interrupted |
| harness:retire | -1 | 0.077 | interrupted |
| harness:retire | -1 | 0.076 | interrupted |
| harness:retire | -1 | 0.076 | interrupted |
| harness:retire | -1 | 0.076 | interrupted |
| harness:retire | -1 | 0.075 | interrupted |
| harness:retire | -1 | 0.074 | interrupted |
| harness:retire | -1 | 0.073 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 4702.457 | n/a | n/a | 219.500 | 4702456.573 | 4702456.573 | 4702456.573 |
| engine:execute | 1/1 | 0 | 0 | 4702.455 | 2.153 | 4700.276 | 219.500 | 4702454.728 | 4702454.728 | 4702454.728 |
| harness:attempt_rpc | 272/272 | 0 | 0 | 4673.800 | 10.378 | 4663.420 | 219.500 | 17183.088 | 13527.309 | 29575.938 |
| harness:await_cli | 272/272 | 0 | 0 | 3459.717 | n/a | n/a | 219.500 | 12719.547 | 9083.724 | 25239.446 |
| llm:attempt | 456/456 | 52 | 0 | 2900.044 | 69.279 | 2830.185 | 26.528 | 6359.745 | 6181.524 | 10650.100 |
| harness:startup_ready | 272/272 | 0 | 0 | 854.672 | n/a | n/a | 0.000 | 3142.177 | 3172.941 | 3676.099 |
| tool:Bash | 96/96 | 15 | 0 | 463.009 | n/a | n/a | 198.057 | 4823.014 | 1450.481 | 12950.005 |
| harness:submit | 272/272 | 0 | 0 | 237.006 | n/a | n/a | 0.000 | 871.347 | 834.294 | 1153.875 |
| syscall:connect | 9070/9070 | 0 | 0 | 24.307 | n/a | n/a | 0.115 | 2.680 | 2.080 | 4.934 |
| run:container_call | 13/13 | 0 | 0 | 23.081 | 0.002 | 23.079 | 0.000 | 1775.492 | 35.896 | 9080.638 |
| teardown:commit | 1/1 | 0 | 0 | 22.666 | 0.004 | 22.662 | 0.000 | 22665.861 | 22665.861 | 22665.861 |
| sandbox:commit | 1/1 | 0 | 0 | 22.473 | 0.002 | 22.470 | 0.000 | 22472.643 | 22472.643 | 22472.643 |
| checkpoint.total | 1/1 | 0 | 0 | 22.473 | 0.002 | 22.470 | 0.000 | 22472.511 | 22472.511 | 22472.511 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.472 | 0.002 | 22.470 | 0.000 | 22472.374 | 22472.374 | 22472.374 |
| syscall:sendto | 6235/6235 | 0 | 0 | 17.203 | n/a | n/a | 0.138 | 2.759 | 2.165 | 4.969 |
| syscall:execve | 6289/6289 | 0 | 0 | 14.549 | n/a | n/a | 0.164 | 2.313 | 1.804 | 3.896 |
| harness:snapshot | 272/272 | 0 | 0 | 12.289 | n/a | n/a | 0.000 | 45.181 | 43.621 | 62.054 |
| tool:Grep | 7/7 | 1 | 0 | 5.335 | n/a | n/a | 0.000 | 762.130 | 257.729 | 2225.457 |
| harness:launch | 272/272 | 0 | 0 | 5.139 | n/a | n/a | 0.000 | 18.894 | 18.896 | 22.793 |
| tool:Read | 18/18 | 0 | 0 | 4.263 | n/a | n/a | 0.000 | 236.827 | 242.886 | 261.991 |
| syscall:bind | 1523/1523 | 0 | 0 | 4.167 | n/a | n/a | 0.000 | 2.736 | 2.363 | 4.823 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.157 | 0.723 | 2.434 | 0.000 | 3156.639 | 3156.639 | 3156.639 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.156 | 0.723 | 2.434 | 0.000 | 3156.345 | 3156.345 | 3156.345 |
| agency:decode_harness_result | 272/272 | 0 | 0 | 1.816 | 1.815 | 0.001 | 0.000 | 6.676 | 7.209 | 11.099 |
| tool:TodoList | 6/6 | 0 | 0 | 1.730 | n/a | n/a | 0.000 | 288.302 | 255.768 | 422.521 |
| tool:Glob | 1/1 | 0 | 0 | 1.139 | n/a | n/a | 0.000 | 1138.861 | 1138.861 | 1138.861 |
| sandbox:create | 1/1 | 0 | 0 | 0.355 | 0.262 | 0.093 | 0.000 | 354.509 | 354.509 | 354.509 |
| sandbox:start | 1/1 | 0 | 0 | 0.348 | 0.002 | 0.345 | 0.000 | 347.801 | 347.801 | 347.801 |
| runtime.container_create | 1/1 | 0 | 0 | 0.348 | 0.002 | 0.345 | 0.000 | 347.661 | 347.661 | 347.661 |
| tool:Write | 1/1 | 0 | 0 | 0.286 | n/a | n/a | 0.000 | 286.303 | 286.303 | 286.303 |
| tool:TaskList | 1/1 | 0 | 0 | 0.266 | n/a | n/a | 0.000 | 266.127 | 266.127 | 266.127 |
| sandbox:stop | 1/1 | 0 | 0 | 0.193 | 0.002 | 0.191 | 0.000 | 192.928 | 192.928 | 192.928 |
| agency:services_close | 1/1 | 0 | 0 | 0.107 | 0.003 | 0.104 | 0.000 | 106.828 | 106.828 | 106.828 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.031 | 0.000 | 72.772 | 72.772 | 72.772 |
| run:detect | 1/1 | 0 | 0 | 0.055 | 0.001 | 0.055 | 0.000 | 55.384 | 55.384 | 55.384 |
| agent:create | 1/1 | 0 | 0 | 0.047 | 0.008 | 0.040 | 0.000 | 47.340 | 47.340 | 47.340 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.313 | 1.313 | 1.313 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.076 | 0.074 | 0.116 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.229 | 0.229 | 0.229 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.063 | 0.063 | 0.063 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/272 | 0 | 272 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 4674 | 0.254 | 0.035 | 58.512 | 0.104 | 11.964279 CPU seconds | n/a |
| GPU 0 memory | MB | 4675 | 13891.804 | 11670.000 | 19048.000 | 12060.000 | n/a | n/a |
| GPU 0 power | W | 4675 | 31.703 | 28.317 | 76.642 | 28.512 | n/a | 149355.546 J |
| GPU 0 proc / 15197-674109 / sandbox / ~ / device / GPU-017f59e4-7dcc-676d-23e3-35a1e7154a44 memory | MB | 4675 | 5120.687 | 3118.000 | 10268.000 | 3280.000 | n/a | n/a |
| GPU 0 proc / 15197-674109 / sandbox / ~ / device / GPU-017f59e4-7dcc-676d-23e3-35a1e7154a44 estimated power | W | 4219 | 1.206 | 0.000 | 75.876 | 0.000 | n/a | n/a |
| GPU 0 proc / 15197-674109 / sandbox / ~ / device / GPU-017f59e4-7dcc-676d-23e3-35a1e7154a44 utilization | percent | 4219 | 1.409 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 15239-675874 / sandbox / ~ / device / GPU-017f59e4-7dcc-676d-23e3-35a1e7154a44 memory | MB | 4675 | 8289.118 | 8070.000 | 8298.000 | 8298.000 | n/a | n/a |
| GPU 0 proc / 15239-675874 / sandbox / ~ / device / GPU-017f59e4-7dcc-676d-23e3-35a1e7154a44 estimated power | W | 368 | 47.009 | 0.000 | 72.838 | 0.000 | n/a | n/a |
| GPU 0 proc / 15239-675874 / sandbox / ~ / device / GPU-017f59e4-7dcc-676d-23e3-35a1e7154a44 utilization | percent | 368 | 64.649 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 4675 | 13409.804 | 11188.000 | 18566.000 | 11578.000 | n/a | n/a |
| GPU 0 utilization | percent | 4675 | 6.484 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 4675 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 4674 | 3.978 | 0.088 | 76.036 | 0.210 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 4674 | 22.542 | 0.000 | 65.099 | 0.251 | n/a | n/a |
| host disk_read_mb_s | MB/s | 4674 | 0.394 | 0.000 | 202.340 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 4674 | 0.724 | 0.000 | 14.683 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 4674 | 0.327 | 0.000 | 65.109 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 4674 | 0.369 | 0.000 | 65.161 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 4675 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 4675 | 8015.614 | 6740.641 | 10363.820 | 8073.164 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 4674 | 0.000 | 0.000 | 0.251 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 4674 | 0.000 | 0.000 | 0.251 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 4674 | 0.122 | 0.000 | 2.244 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 4674 | 0.038 | 0.000 | 0.523 | 0.000 | n/a | n/a |
| bash kimi_seq.sh (PID 15185) CPU | percent | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash kimi_seq.sh (PID 15185) io read MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash kimi_seq.sh (PID 15185) io write MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash kimi_seq.sh (PID 15185) rss_mb | MB | 4675 | 3.344 | 3.344 | 3.344 | 3.344 | n/a | n/a |
| bash kimi_seq.sh (PID 15185) main thread run-queue wait | percent | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash kimi_seq.sh (PID 15185) vms_mb | MB | 4675 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 15189) CPU | percent | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 15189) io read MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 15189) io write MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 15189) rss_mb | MB | 4675 | 3.328 | 3.328 | 3.328 | 3.328 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 15189) main thread run-queue wait | percent | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 15189) vms_mb | MB | 4675 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 15197) CPU | percent | 4674 | 5.892 | 0.000 | 170.683 | 1.991 | 278.000000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 15197) io read MB/s | MB/s | 4674 | 0.002 | 0.000 | 6.714 | 0.000 | 8.644531 MB | n/a |
| Agency harness — python -m lsbench (PID 15197) io write MB/s | MB/s | 4674 | 0.393 | 0.000 | 21.941 | 0.035 | 1852.140625 MB | n/a |
| Agency harness — python -m lsbench (PID 15197) rss_mb | MB | 4675 | 3661.281 | 2583.199 | 4324.965 | 4158.000 | n/a | n/a |
| Agency harness — python -m lsbench (PID 15197) main thread run-queue wait | percent | 4674 | 0.000 | 0.000 | 0.217 | 0.000 | 0.007184 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 15197) vms_mb | MB | 4675 | 18350.126 | 14115.996 | 23906.797 | 17043.082 | n/a | n/a |
| Python — vllm (PID 15202) CPU | percent | 4674 | 0.282 | 0.000 | 6.927 | 0.000 | 13.330000 CPU seconds | n/a |
| Python — vllm (PID 15202) io read MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 15202) io write MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.008 | 0.000 | 0.050781 MB | n/a |
| Python — vllm (PID 15202) rss_mb | MB | 4675 | 1776.011 | 1773.855 | 1776.105 | 1776.105 | n/a | n/a |
| Python — vllm (PID 15202) main thread run-queue wait | percent | 4674 | 0.021 | 0.000 | 2.830 | 0.000 | 0.972320 run-queue seconds | n/a |
| Python — vllm (PID 15202) vms_mb | MB | 4675 | 11014.718 | 10942.777 | 11016.797 | 11016.797 | n/a | n/a |
| Python — python -c (PID 15238) CPU | percent | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 15238) io read MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 15238) io write MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 15238) rss_mb | MB | 4675 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| Python — python -c (PID 15238) main thread run-queue wait | percent | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 15238) vms_mb | MB | 4675 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 15239) CPU | percent | 4674 | 3.068 | 0.000 | 50.419 | 0.996 | 144.820000 CPU seconds | n/a |
| VLLM::EngineCore (PID 15239) io read MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 15239) io write MB/s | MB/s | 4674 | 0.000 | 0.000 | 0.004 | 0.000 | 0.027344 MB | n/a |
| VLLM::EngineCore (PID 15239) rss_mb | MB | 4675 | 2337.347 | 2336.207 | 2337.582 | 2337.582 | n/a | n/a |
| VLLM::EngineCore (PID 15239) main thread run-queue wait | percent | 4674 | 0.138 | 0.000 | 18.578 | 0.000 | 6.551406 run-queue seconds | n/a |
| VLLM::EngineCore (PID 15239) vms_mb | MB | 4675 | 21236.570 | 21235.215 | 21236.664 | 21236.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 15458) CPU | percent | 4665 | 0.002 | 0.000 | 0.995 | 0.000 | 0.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 15458) rss_mb | MB | 4666 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 15458) main thread run-queue wait | percent | 4665 | 0.011 | 0.000 | 5.034 | 0.000 | 0.519585 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 15458) vms_mb | MB | 4666 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 15490) CPU | percent | 4665 | 0.002 | 0.000 | 0.995 | 0.000 | 0.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 15490) rss_mb | MB | 4666 | 1.543 | 1.543 | 1.543 | 1.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 15490) main thread run-queue wait | percent | 4665 | 0.007 | 0.000 | 4.682 | 0.000 | 0.346942 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 15490) vms_mb | MB | 4666 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15583) CPU | percent | 4665 | 50.254 | 0.000 | 116.016 | 0.000 | 2363.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15583) rss_mb | MB | 4666 | 148.667 | 3.172 | 173.906 | 147.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15583) main thread run-queue wait | percent | 4665 | 0.000 | 0.000 | 0.047 | 0.000 | 0.000548 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15583) vms_mb | MB | 4666 | 946.817 | 4.258 | 986.492 | 976.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 15589) CPU | percent | 1 | 98.891 | 98.891 | 98.891 | 98.891 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 15589) rss_mb | MB | 2 | 52.229 | 25.477 | 78.980 | 78.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 15589) main thread run-queue wait | percent | 1 | 0.004 | 0.004 | 0.004 | 0.004 | 0.000038 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 15589) vms_mb | MB | 2 | 64.104 | 34.020 | 94.188 | 94.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15597) rss_mb | MB | 1 | 237.055 | 237.055 | 237.055 | 237.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15597) vms_mb | MB | 1 | 1644.375 | 1644.375 | 1644.375 | 1644.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15614) CPU | percent | 346 | 3.641 | 0.979 | 67.568 | 7.959 | 12.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15614) rss_mb | MB | 347 | 388.615 | 212.352 | 416.297 | 399.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15614) main thread run-queue wait | percent | 346 | 0.186 | 0.001 | 9.968 | 0.028 | 0.647219 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15614) vms_mb | MB | 347 | 10146.010 | 1622.801 | 10218.258 | 10202.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15646) rss_mb | MB | 1 | 199.996 | 199.996 | 199.996 | 199.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 15646) vms_mb | MB | 1 | 1617.457 | 1617.457 | 1617.457 | 1617.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15697) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15697) rss_mb | MB | 2 | 2.609 | 2.609 | 2.609 | 2.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15697) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15697) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp (PID 15698) CPU | percent | 1 | 75.558 | 75.558 | 75.558 | 75.558 | 0.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp (PID 15698) rss_mb | MB | 2 | 35.250 | 8.945 | 61.555 | 61.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp (PID 15698) main thread run-queue wait | percent | 1 | 0.053 | 0.053 | 0.053 | 0.053 | 0.000536 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — mcp (PID 15698) vms_mb | MB | 2 | 44.576 | 13.277 | 75.875 | 75.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15716) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15716) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15717) rss_mb | MB | 1 | 18.777 | 18.777 | 18.777 | 18.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15717) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15725) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15725) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15754) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15754) rss_mb | MB | 2 | 2.676 | 2.676 | 2.676 | 2.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15754) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15754) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15755) CPU | percent | 1 | 78.537 | 78.537 | 78.537 | 78.537 | 0.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15755) rss_mb | MB | 2 | 43.623 | 22.582 | 64.664 | 64.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15755) main thread run-queue wait | percent | 1 | 0.148 | 0.148 | 0.148 | 0.148 | 0.001493 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15755) vms_mb | MB | 2 | 55.912 | 32.055 | 79.770 | 79.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15901) rss_mb | MB | 1 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15901) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15902) rss_mb | MB | 1 | 24.121 | 24.121 | 24.121 | 24.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15902) vms_mb | MB | 1 | 30.242 | 30.242 | 30.242 | 30.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15972) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15972) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15973) rss_mb | MB | 1 | 21.004 | 21.004 | 21.004 | 21.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15973) vms_mb | MB | 1 | 25.836 | 25.836 | 25.836 | 25.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15979) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15979) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15980) rss_mb | MB | 1 | 21.789 | 21.789 | 21.789 | 21.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15980) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15981) rss_mb | MB | 1 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 15981) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15982) rss_mb | MB | 1 | 50.250 | 50.250 | 50.250 | 50.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 15982) vms_mb | MB | 1 | 57.008 | 57.008 | 57.008 | 57.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15988) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 15988) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15989) rss_mb | MB | 1 | 9.613 | 9.613 | 9.613 | 9.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 15989) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16008) CPU | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16008) rss_mb | MB | 24 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16008) main thread run-queue wait | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16008) vms_mb | MB | 24 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16009) CPU | percent | 23 | 2.676 | 0.000 | 61.544 | 0.000 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16009) rss_mb | MB | 24 | 64.884 | 30.867 | 66.363 | 66.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16009) main thread run-queue wait | percent | 23 | 0.018 | 0.000 | 0.410 | 0.000 | 0.004135 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16009) vms_mb | MB | 24 | 79.499 | 41.027 | 81.172 | 81.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16022) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16022) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16023) rss_mb | MB | 1 | 18.352 | 18.352 | 18.352 | 18.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16023) vms_mb | MB | 1 | 24.340 | 24.340 | 24.340 | 24.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16037) CPU | percent | 70 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16037) rss_mb | MB | 71 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16037) main thread run-queue wait | percent | 70 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16037) vms_mb | MB | 71 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16038) CPU | percent | 70 | 0.893 | 0.000 | 62.492 | 0.000 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16038) rss_mb | MB | 71 | 66.032 | 31.117 | 66.531 | 66.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16038) main thread run-queue wait | percent | 70 | 0.003 | 0.000 | 0.185 | 0.000 | 0.001868 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16038) vms_mb | MB | 71 | 80.589 | 41.148 | 81.152 | 81.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16080) CPU | percent | 72 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16080) rss_mb | MB | 73 | 2.672 | 2.672 | 2.672 | 2.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16080) main thread run-queue wait | percent | 72 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16080) vms_mb | MB | 73 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16081) CPU | percent | 72 | 0.992 | 0.000 | 57.526 | 0.000 | 0.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16081) rss_mb | MB | 73 | 67.184 | 35.445 | 68.781 | 68.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16081) main thread run-queue wait | percent | 72 | 0.026 | 0.000 | 0.659 | 0.000 | 0.019176 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16081) vms_mb | MB | 73 | 81.712 | 44.031 | 83.273 | 83.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16136) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16136) rss_mb | MB | 3 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16136) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16136) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16137) CPU | percent | 2 | 11.929 | 0.000 | 23.858 | 0.000 | 0.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16137) rss_mb | MB | 3 | 59.708 | 46.516 | 66.305 | 66.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16137) main thread run-queue wait | percent | 2 | 0.100 | 0.000 | 0.201 | 0.000 | 0.002021 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16137) vms_mb | MB | 3 | 71.704 | 54.918 | 80.098 | 80.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16146) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16146) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16147) rss_mb | MB | 1 | 7.395 | 7.395 | 7.395 | 7.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16147) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16155) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16155) rss_mb | MB | 8 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16155) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16155) vms_mb | MB | 8 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16156) CPU | percent | 7 | 6.522 | 0.000 | 32.799 | 0.000 | 0.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16156) rss_mb | MB | 8 | 65.073 | 44.680 | 68.844 | 68.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16156) main thread run-queue wait | percent | 7 | 0.239 | 0.000 | 0.787 | 0.000 | 0.016904 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16156) vms_mb | MB | 8 | 78.661 | 52.926 | 83.223 | 83.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16175) CPU | percent | 61 | 6.707 | 0.994 | 70.498 | 2.985 | 4.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16175) rss_mb | MB | 62 | 387.025 | 217.559 | 397.344 | 397.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16175) main thread run-queue wait | percent | 61 | 0.629 | 0.003 | 8.446 | 0.017 | 0.386496 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16175) vms_mb | MB | 62 | 9932.432 | 1623.523 | 10210.938 | 10210.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16217) rss_mb | MB | 1 | 253.355 | 253.355 | 253.355 | 253.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16217) vms_mb | MB | 1 | 1648.871 | 1648.871 | 1648.871 | 1648.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16318) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16318) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16319) rss_mb | MB | 1 | 19.297 | 19.297 | 19.297 | 19.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16319) vms_mb | MB | 1 | 24.805 | 24.805 | 24.805 | 24.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16320) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16320) rss_mb | MB | 8 | 2.594 | 2.594 | 2.594 | 2.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16320) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16320) vms_mb | MB | 8 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16321) CPU | percent | 7 | 2.978 | 0.000 | 12.890 | 7.954 | 0.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16321) rss_mb | MB | 8 | 65.558 | 59.691 | 67.789 | 67.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16321) main thread run-queue wait | percent | 7 | 0.144 | 0.000 | 0.841 | 0.841 | 0.010168 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16321) vms_mb | MB | 8 | 79.706 | 74.258 | 82.543 | 82.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16343) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16343) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16344) rss_mb | MB | 1 | 17.707 | 17.707 | 17.707 | 17.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16344) vms_mb | MB | 1 | 23.184 | 23.184 | 23.184 | 23.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16358) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16358) rss_mb | MB | 3 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16358) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16358) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16359) CPU | percent | 2 | 19.339 | 3.968 | 34.710 | 3.968 | 0.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16359) rss_mb | MB | 3 | 59.435 | 44.516 | 67.332 | 67.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16359) main thread run-queue wait | percent | 2 | 0.505 | 0.277 | 0.733 | 0.277 | 0.010184 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16359) vms_mb | MB | 3 | 72.255 | 53.297 | 82.590 | 82.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16367) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16367) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16368) rss_mb | MB | 1 | 14.586 | 14.586 | 14.586 | 14.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16368) vms_mb | MB | 1 | 20.082 | 20.082 | 20.082 | 20.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16385) CPU | percent | 13 | 22.712 | 1.988 | 91.471 | 2.983 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16385) rss_mb | MB | 14 | 352.181 | 99.145 | 385.660 | 385.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16385) main thread run-queue wait | percent | 13 | 1.585 | 0.006 | 13.614 | 0.006 | 0.209814 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16385) vms_mb | MB | 14 | 8956.496 | 1283.598 | 10210.887 | 10210.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16409) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16409) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16410) rss_mb | MB | 1 | 10.180 | 10.180 | 10.180 | 10.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16410) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16414) rss_mb | MB | 1 | 229.434 | 229.434 | 229.434 | 229.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16414) vms_mb | MB | 1 | 1631.953 | 1631.953 | 1631.953 | 1631.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16428) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16428) rss_mb | MB | 3 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16428) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16428) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16429) CPU | percent | 2 | 28.279 | 8.934 | 47.625 | 8.934 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16429) rss_mb | MB | 3 | 58.422 | 40.664 | 68.051 | 68.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16429) main thread run-queue wait | percent | 2 | 0.730 | 0.527 | 0.933 | 0.933 | 0.014703 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16429) vms_mb | MB | 3 | 70.997 | 49.285 | 82.547 | 82.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16443) CPU | percent | 24 | 14.067 | 0.994 | 87.384 | 1.989 | 3.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16443) rss_mb | MB | 25 | 369.542 | 133.383 | 389.062 | 389.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16443) main thread run-queue wait | percent | 24 | 1.067 | 0.005 | 17.725 | 0.010 | 0.258317 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16443) vms_mb | MB | 25 | 9510.173 | 1296.254 | 10210.488 | 10210.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16466) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16466) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16467) rss_mb | MB | 1 | 8.594 | 8.594 | 8.594 | 8.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16467) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16469) CPU | percent | 1 | 66.423 | 66.423 | 66.423 | 66.423 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16469) rss_mb | MB | 2 | 120.936 | 0.621 | 241.250 | 241.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16469) main thread run-queue wait | percent | 1 | 19.702 | 19.702 | 19.702 | 19.702 | 0.198735 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16469) vms_mb | MB | 2 | 901.578 | 163.301 | 1639.855 | 1639.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16487) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16487) rss_mb | MB | 2 | 2.766 | 2.766 | 2.766 | 2.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16487) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16487) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16488) CPU | percent | 1 | 34.338 | 34.338 | 34.338 | 34.338 | 0.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16488) rss_mb | MB | 2 | 55.539 | 44.199 | 66.879 | 66.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16488) main thread run-queue wait | percent | 1 | 0.798 | 0.798 | 0.798 | 0.798 | 0.008138 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16488) vms_mb | MB | 2 | 67.543 | 52.992 | 82.094 | 82.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16505) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16505) rss_mb | MB | 2 | 2.719 | 2.719 | 2.719 | 2.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16505) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16505) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16506) CPU | percent | 1 | 73.413 | 73.413 | 73.413 | 73.413 | 0.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16506) rss_mb | MB | 2 | 36.010 | 7.844 | 64.176 | 64.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16506) main thread run-queue wait | percent | 1 | 0.068 | 0.068 | 0.068 | 0.068 | 0.000687 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16506) vms_mb | MB | 2 | 45.902 | 13.051 | 78.754 | 78.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16508) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16508) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16509) rss_mb | MB | 1 | 21.414 | 21.414 | 21.414 | 21.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16509) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 16518) CPU | percent | 14 | 14.257 | 0.992 | 62.537 | 4.971 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 16518) rss_mb | MB | 15 | 376.337 | 300.340 | 393.586 | 393.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 16518) main thread run-queue wait | percent | 14 | 1.139 | 0.002 | 12.762 | 0.009 | 0.160485 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 16518) vms_mb | MB | 15 | 9619.811 | 1724.785 | 10194.379 | 10193.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16539) CPU | percent | 1 | 64.595 | 64.595 | 64.595 | 64.595 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16539) rss_mb | MB | 2 | 204.275 | 145.691 | 262.859 | 262.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16539) main thread run-queue wait | percent | 1 | 16.462 | 16.462 | 16.462 | 16.462 | 0.165651 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16539) vms_mb | MB | 2 | 1479.889 | 1301.734 | 1658.043 | 1658.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16546) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16546) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16547) rss_mb | MB | 1 | 10.082 | 10.082 | 10.082 | 10.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16547) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16567) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16567) rss_mb | MB | 2 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16567) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16567) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16568) CPU | percent | 1 | 62.521 | 62.521 | 62.521 | 62.521 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16568) rss_mb | MB | 2 | 49.746 | 33.207 | 66.285 | 66.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16568) main thread run-queue wait | percent | 1 | 0.256 | 0.256 | 0.256 | 0.256 | 0.002581 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16568) vms_mb | MB | 2 | 61.379 | 42.637 | 80.121 | 80.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16581) CPU | percent | 18 | 14.869 | 0.994 | 64.642 | 3.977 | 2.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16581) rss_mb | MB | 19 | 369.473 | 236.945 | 384.895 | 384.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16581) main thread run-queue wait | percent | 18 | 2.284 | 0.006 | 19.877 | 0.013 | 0.423146 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16581) vms_mb | MB | 19 | 9747.422 | 1637.281 | 10211.082 | 10211.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16600) CPU | percent | 1 | 59.104 | 59.104 | 59.104 | 59.104 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16600) rss_mb | MB | 2 | 216.400 | 169.402 | 263.398 | 263.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16600) main thread run-queue wait | percent | 1 | 18.094 | 18.094 | 18.094 | 18.094 | 0.183678 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16600) vms_mb | MB | 2 | 1618.881 | 1578.973 | 1658.789 | 1658.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16612) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16612) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16613) rss_mb | MB | 1 | 9.504 | 9.504 | 9.504 | 9.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16613) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16623) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16623) rss_mb | MB | 4 | 2.914 | 2.914 | 2.914 | 2.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16623) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16623) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16624) CPU | percent | 3 | 19.846 | 1.988 | 44.672 | 1.988 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16624) rss_mb | MB | 4 | 61.014 | 41.066 | 68.496 | 68.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16624) main thread run-queue wait | percent | 3 | 0.501 | 0.227 | 0.951 | 0.326 | 0.015165 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16624) vms_mb | MB | 4 | 73.939 | 49.656 | 83.211 | 83.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16639) CPU | percent | 113 | 4.767 | 0.982 | 71.281 | 5.955 | 5.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16639) rss_mb | MB | 114 | 380.877 | 215.891 | 388.852 | 363.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16639) main thread run-queue wait | percent | 113 | 29.006 | 0.002 | 58.501 | 0.013 | 33.210245 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16639) vms_mb | MB | 114 | 10055.591 | 1623.258 | 10211.762 | 10147.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16668) rss_mb | MB | 1 | 234.953 | 234.953 | 234.953 | 234.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16668) vms_mb | MB | 1 | 1636.078 | 1636.078 | 1636.078 | 1636.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16682) CPU | percent | 80 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16682) rss_mb | MB | 81 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16682) main thread run-queue wait | percent | 80 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16682) vms_mb | MB | 81 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16683) CPU | percent | 80 | 1.068 | 0.000 | 62.608 | 15.839 | 0.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16683) rss_mb | MB | 81 | 66.276 | 29.656 | 67.121 | 67.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16683) main thread run-queue wait | percent | 80 | 1.531 | 0.000 | 78.083 | 78.083 | 1.236519 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16683) vms_mb | MB | 81 | 80.618 | 38.609 | 81.410 | 81.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16698) CPU | percent | 84 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16698) rss_mb | MB | 85 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16698) main thread run-queue wait | percent | 84 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16698) vms_mb | MB | 85 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16699) CPU | percent | 84 | 169.395 | 140.416 | 180.063 | 171.968 | 144.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16699) rss_mb | MB | 85 | 433.253 | 8.426 | 560.781 | 560.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16699) main thread run-queue wait | percent | 84 | 55.328 | 25.177 | 76.305 | 63.756 | 47.086909 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16699) vms_mb | MB | 85 | 824.421 | 13.207 | 872.035 | 872.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16712) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16712) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16713) rss_mb | MB | 1 | 4.566 | 4.566 | 4.566 | 4.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 16713) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16732) CPU | percent | 15 | 18.970 | 0.989 | 66.509 | 1.989 | 2.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16732) rss_mb | MB | 16 | 370.543 | 220.473 | 393.406 | 393.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16732) main thread run-queue wait | percent | 15 | 2.032 | 0.003 | 15.449 | 0.006 | 0.307413 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16732) vms_mb | MB | 16 | 9137.760 | 1623.781 | 10207.664 | 10207.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16758) CPU | percent | 1 | 73.549 | 73.549 | 73.549 | 73.549 | 0.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16758) rss_mb | MB | 2 | 221.734 | 147.844 | 295.625 | 295.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16758) main thread run-queue wait | percent | 1 | 14.985 | 14.985 | 14.985 | 14.985 | 0.150765 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16758) vms_mb | MB | 2 | 1497.174 | 1304.312 | 1690.035 | 1690.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16777) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16777) rss_mb | MB | 5 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16777) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 16777) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16778) CPU | percent | 4 | 7.193 | 0.000 | 28.772 | 0.000 | 0.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16778) rss_mb | MB | 5 | 62.280 | 45.934 | 66.367 | 66.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16778) main thread run-queue wait | percent | 4 | 0.063 | 0.000 | 0.251 | 0.000 | 0.002533 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 16778) vms_mb | MB | 5 | 75.058 | 54.680 | 80.152 | 80.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16789) CPU | percent | 15 | 17.887 | 1.987 | 89.501 | 2.984 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16789) rss_mb | MB | 16 | 355.934 | 60.195 | 387.488 | 387.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16789) main thread run-queue wait | percent | 15 | 2.244 | 0.000 | 21.627 | 0.008 | 0.339234 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16789) vms_mb | MB | 16 | 9085.873 | 1238.512 | 10199.785 | 10169.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16808) CPU | percent | 1 | 58.514 | 58.514 | 58.514 | 58.514 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16808) rss_mb | MB | 2 | 252.143 | 209.086 | 295.199 | 295.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16808) main thread run-queue wait | percent | 1 | 25.163 | 25.163 | 25.163 | 25.163 | 0.253716 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16808) vms_mb | MB | 2 | 1655.148 | 1620.730 | 1689.566 | 1689.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16818) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16818) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16819) rss_mb | MB | 1 | 7.270 | 7.270 | 7.270 | 7.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16819) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16836) CPU | percent | 7 | 35.070 | 3.970 | 90.492 | 5.966 | 2.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16836) rss_mb | MB | 8 | 324.717 | 60.324 | 387.562 | 387.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16836) main thread run-queue wait | percent | 7 | 5.982 | 0.012 | 25.923 | 0.012 | 0.421644 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16836) vms_mb | MB | 8 | 8009.741 | 1238.512 | 10197.621 | 10197.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16855) CPU | percent | 1 | 62.550 | 62.550 | 62.550 | 62.550 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16855) rss_mb | MB | 2 | 249.822 | 204.410 | 295.234 | 295.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16855) main thread run-queue wait | percent | 1 | 18.918 | 18.918 | 18.918 | 18.918 | 0.190538 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16855) vms_mb | MB | 2 | 1654.365 | 1618.742 | 1689.988 | 1689.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16865) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16865) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16866) rss_mb | MB | 1 | 7.008 | 7.008 | 7.008 | 7.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16866) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16883) CPU | percent | 7 | 40.461 | 7.960 | 87.394 | 9.949 | 2.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16883) rss_mb | MB | 8 | 334.641 | 134.621 | 390.711 | 390.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16883) main thread run-queue wait | percent | 7 | 5.864 | 0.024 | 23.462 | 0.025 | 0.413172 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16883) vms_mb | MB | 8 | 8022.264 | 1296.254 | 10207.988 | 10207.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16903) CPU | percent | 1 | 57.598 | 57.598 | 57.598 | 57.598 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16903) rss_mb | MB | 2 | 251.623 | 208.023 | 295.223 | 295.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16903) main thread run-queue wait | percent | 1 | 23.424 | 23.424 | 23.424 | 23.424 | 0.235876 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16903) vms_mb | MB | 2 | 1654.604 | 1619.230 | 1689.977 | 1689.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16931) CPU | percent | 6 | 38.522 | 2.984 | 67.652 | 8.954 | 2.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16931) rss_mb | MB | 7 | 341.301 | 209.121 | 383.504 | 383.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16931) main thread run-queue wait | percent | 6 | 6.619 | 0.019 | 21.582 | 0.100 | 0.422212 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16931) vms_mb | MB | 7 | 7761.634 | 1619.789 | 10203.516 | 10203.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16948) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16948) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16949) rss_mb | MB | 1 | 9.832 | 9.832 | 9.832 | 9.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16949) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16952) CPU | percent | 1 | 61.379 | 61.379 | 61.379 | 61.379 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16952) rss_mb | MB | 2 | 245.881 | 194.199 | 297.562 | 297.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16952) main thread run-queue wait | percent | 1 | 20.808 | 20.808 | 20.808 | 20.808 | 0.230526 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16952) vms_mb | MB | 2 | 1653.355 | 1614.473 | 1692.238 | 1692.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16988) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 16988) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16989) rss_mb | MB | 1 | 10.164 | 10.164 | 10.164 | 10.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 16989) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16993) CPU | percent | 7 | 30.060 | 1.989 | 70.231 | 5.964 | 2.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16993) rss_mb | MB | 8 | 352.614 | 235.617 | 386.629 | 386.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16993) main thread run-queue wait | percent | 7 | 3.791 | 0.004 | 15.861 | 0.010 | 0.266978 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 16993) vms_mb | MB | 8 | 8074.957 | 1636.035 | 10207.277 | 10207.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17017) rss_mb | MB | 1 | 198.480 | 198.480 | 198.480 | 198.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17017) vms_mb | MB | 1 | 1617.203 | 1617.203 | 1617.203 | 1617.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17042) CPU | percent | 5 | 35.953 | 2.983 | 64.595 | 3.979 | 1.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17042) rss_mb | MB | 6 | 345.082 | 271.711 | 371.742 | 371.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17042) main thread run-queue wait | percent | 5 | 3.623 | 0.012 | 16.273 | 0.012 | 0.182539 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17042) vms_mb | MB | 6 | 8760.956 | 1666.996 | 10202.613 | 10202.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17063) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17063) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17064) rss_mb | MB | 1 | 9.551 | 9.551 | 9.551 | 9.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17064) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17067) rss_mb | MB | 1 | 195.195 | 195.195 | 195.195 | 195.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17067) vms_mb | MB | 1 | 1614.973 | 1614.973 | 1614.973 | 1614.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17087) CPU | percent | 6 | 43.331 | 3.980 | 89.073 | 3.980 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17087) rss_mb | MB | 7 | 324.373 | 147.828 | 378.852 | 378.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17087) main thread run-queue wait | percent | 6 | 6.709 | 0.022 | 21.431 | 0.022 | 0.405942 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17087) vms_mb | MB | 7 | 7702.249 | 1304.098 | 10205.348 | 10205.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17244) CPU | percent | 1 | 61.605 | 61.605 | 61.605 | 61.605 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17244) rss_mb | MB | 2 | 233.033 | 187.516 | 278.551 | 278.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17244) main thread run-queue wait | percent | 1 | 18.877 | 18.877 | 18.877 | 18.877 | 0.189978 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17244) vms_mb | MB | 2 | 1633.760 | 1593.973 | 1673.547 | 1673.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17270) CPU | percent | 8 | 33.531 | 4.963 | 85.412 | 6.959 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17270) rss_mb | MB | 9 | 335.843 | 104.082 | 389.824 | 389.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17270) main thread run-queue wait | percent | 8 | 4.548 | 0.019 | 24.314 | 0.055 | 0.366425 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17270) vms_mb | MB | 9 | 8266.629 | 1283.598 | 10207.680 | 10207.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17289) CPU | percent | 1 | 60.547 | 60.547 | 60.547 | 60.547 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17289) rss_mb | MB | 2 | 255.346 | 213.875 | 296.816 | 296.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17289) main thread run-queue wait | percent | 1 | 17.704 | 17.704 | 17.704 | 17.704 | 0.178365 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17289) vms_mb | MB | 2 | 1672.869 | 1622.488 | 1723.250 | 1723.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17317) CPU | percent | 6 | 35.085 | 3.978 | 70.554 | 3.978 | 2.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17317) rss_mb | MB | 7 | 346.134 | 229.781 | 379.984 | 379.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17317) main thread run-queue wait | percent | 6 | 2.347 | 0.025 | 8.269 | 0.074 | 0.141789 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17317) vms_mb | MB | 7 | 7772.130 | 1632.004 | 10207.594 | 10207.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17345) rss_mb | MB | 1 | 287.402 | 287.402 | 287.402 | 287.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17345) vms_mb | MB | 1 | 1682.531 | 1682.531 | 1682.531 | 1682.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17364) CPU | percent | 6 | 32.797 | 3.978 | 68.590 | 5.960 | 1.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17364) rss_mb | MB | 7 | 350.713 | 252.801 | 384.980 | 384.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17364) main thread run-queue wait | percent | 6 | 2.108 | 0.034 | 11.122 | 0.242 | 0.127199 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17364) vms_mb | MB | 7 | 8942.710 | 1649.293 | 10203.426 | 10203.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17393) rss_mb | MB | 1 | 208.703 | 208.703 | 208.703 | 208.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17393) vms_mb | MB | 1 | 1619.711 | 1619.711 | 1619.711 | 1619.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17410) CPU | percent | 6 | 38.433 | 4.972 | 69.581 | 5.967 | 2.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17410) rss_mb | MB | 7 | 336.367 | 193.879 | 379.348 | 379.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17410) main thread run-queue wait | percent | 6 | 6.446 | 0.011 | 17.798 | 0.011 | 0.389113 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17410) vms_mb | MB | 7 | 7762.429 | 1614.469 | 10202.430 | 10202.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17427) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17427) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17429) CPU | percent | 1 | 64.585 | 64.585 | 64.585 | 64.585 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17429) rss_mb | MB | 2 | 180.611 | 106.043 | 255.180 | 255.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17429) main thread run-queue wait | percent | 1 | 18.648 | 18.648 | 18.648 | 18.648 | 0.187681 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17429) vms_mb | MB | 2 | 1467.264 | 1283.695 | 1650.832 | 1650.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17450) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17450) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17451) rss_mb | MB | 1 | 7.367 | 7.367 | 7.367 | 7.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17451) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17455) CPU | percent | 15 | 17.740 | 0.995 | 68.518 | 1.990 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17455) rss_mb | MB | 16 | 366.385 | 207.164 | 389.488 | 388.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17455) main thread run-queue wait | percent | 15 | 3.053 | 0.002 | 22.106 | 0.008 | 0.470433 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17455) vms_mb | MB | 16 | 9134.844 | 1619.293 | 10206.590 | 10205.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17474) CPU | percent | 1 | 63.173 | 63.173 | 63.173 | 63.173 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17474) rss_mb | MB | 2 | 206.303 | 153.078 | 259.527 | 259.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17474) main thread run-queue wait | percent | 1 | 12.740 | 12.740 | 12.740 | 12.740 | 0.129066 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17474) vms_mb | MB | 2 | 1482.291 | 1309.238 | 1655.344 | 1655.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17499) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17499) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17500) rss_mb | MB | 1 | 45.000 | 45.000 | 45.000 | 45.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17500) vms_mb | MB | 1 | 53.383 | 53.383 | 53.383 | 53.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17512) CPU | percent | 12 | 17.610 | 1.988 | 60.552 | 1.988 | 2.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17512) rss_mb | MB | 13 | 368.131 | 289.426 | 385.027 | 385.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17512) main thread run-queue wait | percent | 12 | 2.212 | 0.006 | 20.068 | 0.006 | 0.267484 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17512) vms_mb | MB | 13 | 9537.778 | 1684.348 | 10204.402 | 10204.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17538) rss_mb | MB | 1 | 208.516 | 208.516 | 208.516 | 208.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17538) vms_mb | MB | 1 | 1619.469 | 1619.469 | 1619.469 | 1619.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17554) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17554) rss_mb | MB | 2 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17554) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17554) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17555) CPU | percent | 1 | 31.705 | 31.705 | 31.705 | 31.705 | 0.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17555) rss_mb | MB | 2 | 54.865 | 43.891 | 65.840 | 65.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17555) main thread run-queue wait | percent | 1 | 0.556 | 0.556 | 0.556 | 0.556 | 0.005608 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17555) vms_mb | MB | 2 | 66.475 | 52.816 | 80.133 | 80.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17556) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17556) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17557) rss_mb | MB | 1 | 21.469 | 21.469 | 21.469 | 21.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17557) vms_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17569) CPU | percent | 14 | 19.165 | 1.989 | 83.401 | 1.989 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17569) rss_mb | MB | 15 | 359.591 | 157.332 | 390.117 | 390.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17569) main thread run-queue wait | percent | 14 | 2.174 | 0.005 | 17.802 | 0.007 | 0.306244 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17569) vms_mb | MB | 15 | 9046.551 | 1314.121 | 10208.004 | 10208.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17588) rss_mb | MB | 1 | 229.156 | 229.156 | 229.156 | 229.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17588) vms_mb | MB | 1 | 1632.219 | 1632.219 | 1632.219 | 1632.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17616) CPU | percent | 13 | 26.520 | 0.995 | 72.443 | 40.765 | 3.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17616) rss_mb | MB | 14 | 356.789 | 185.102 | 384.766 | 353.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17616) main thread run-queue wait | percent | 13 | 5.903 | 0.007 | 35.026 | 10.809 | 0.772359 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17616) vms_mb | MB | 14 | 8983.362 | 1592.969 | 10210.125 | 10178.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17633) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17633) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17634) rss_mb | MB | 1 | 8.617 | 8.617 | 8.617 | 8.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17634) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17635) CPU | percent | 1 | 54.564 | 54.564 | 54.564 | 54.564 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17635) rss_mb | MB | 2 | 130.146 | 31.395 | 228.898 | 228.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17635) main thread run-queue wait | percent | 1 | 15.297 | 15.297 | 15.297 | 15.297 | 0.154197 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17635) vms_mb | MB | 2 | 1143.586 | 655.812 | 1631.359 | 1631.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17664) CPU | percent | 11 | 18.691 | 1.988 | 65.612 | 4.970 | 2.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17664) rss_mb | MB | 12 | 361.348 | 220.055 | 391.023 | 391.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17664) main thread run-queue wait | percent | 11 | 1.220 | 0.009 | 4.915 | 0.018 | 0.135060 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17664) vms_mb | MB | 12 | 8781.107 | 1624.027 | 10205.137 | 10205.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17692) rss_mb | MB | 1 | 294.965 | 294.965 | 294.965 | 294.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17692) vms_mb | MB | 1 | 1689.691 | 1689.691 | 1689.691 | 1689.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17711) CPU | percent | 8 | 28.200 | 3.966 | 71.632 | 3.979 | 2.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17711) rss_mb | MB | 9 | 351.599 | 210.797 | 385.848 | 385.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17711) main thread run-queue wait | percent | 8 | 1.814 | 0.009 | 9.361 | 0.023 | 0.146093 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17711) vms_mb | MB | 9 | 8309.882 | 1622.023 | 10206.043 | 10206.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17739) rss_mb | MB | 1 | 267.926 | 267.926 | 267.926 | 267.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17739) vms_mb | MB | 1 | 1663.398 | 1663.398 | 1663.398 | 1663.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17758) CPU | percent | 10 | 18.284 | 1.990 | 63.601 | 2.983 | 1.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17758) rss_mb | MB | 11 | 367.663 | 295.211 | 385.902 | 385.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17758) main thread run-queue wait | percent | 10 | 0.894 | 0.009 | 5.225 | 0.020 | 0.090010 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17758) vms_mb | MB | 11 | 9418.665 | 1690.004 | 10203.469 | 10203.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17786) rss_mb | MB | 1 | 229.520 | 229.520 | 229.520 | 229.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17786) vms_mb | MB | 1 | 1631.961 | 1631.961 | 1631.961 | 1631.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17803) CPU | percent | 11 | 18.622 | 1.987 | 62.786 | 1.987 | 2.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17803) rss_mb | MB | 12 | 365.065 | 262.641 | 387.527 | 387.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17803) main thread run-queue wait | percent | 11 | 2.863 | 0.008 | 20.582 | 0.008 | 0.317957 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17803) vms_mb | MB | 12 | 9481.350 | 1658.254 | 10208.191 | 10208.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17824) CPU | percent | 1 | 57.596 | 57.596 | 57.596 | 57.596 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17824) rss_mb | MB | 2 | 228.773 | 186.371 | 271.176 | 271.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17824) main thread run-queue wait | percent | 1 | 17.874 | 17.874 | 17.874 | 17.874 | 0.179987 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17824) vms_mb | MB | 2 | 1630.162 | 1593.723 | 1666.602 | 1666.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17852) CPU | percent | 10 | 19.573 | 0.994 | 62.596 | 2.985 | 1.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17852) rss_mb | MB | 11 | 368.436 | 294.031 | 387.684 | 387.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17852) main thread run-queue wait | percent | 10 | 3.036 | 0.004 | 19.106 | 0.024 | 0.305788 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17852) vms_mb | MB | 11 | 9419.487 | 1688.996 | 10207.727 | 10207.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17873) CPU | percent | 1 | 59.552 | 59.552 | 59.552 | 59.552 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17873) rss_mb | MB | 2 | 231.336 | 189.598 | 273.074 | 273.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17873) main thread run-queue wait | percent | 1 | 14.343 | 14.343 | 14.343 | 14.343 | 0.144504 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17873) vms_mb | MB | 2 | 1631.910 | 1594.973 | 1668.848 | 1668.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17901) CPU | percent | 11 | 24.211 | 0.995 | 88.477 | 0.995 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17901) rss_mb | MB | 12 | 357.591 | 151.164 | 393.805 | 393.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17901) main thread run-queue wait | percent | 11 | 3.356 | 0.003 | 25.785 | 0.003 | 0.371765 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17901) vms_mb | MB | 12 | 8772.049 | 1499.215 | 10211.277 | 10211.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17926) CPU | percent | 1 | 55.604 | 55.604 | 55.604 | 55.604 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17926) rss_mb | MB | 2 | 216.055 | 169.348 | 262.762 | 262.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17926) main thread run-queue wait | percent | 1 | 23.339 | 23.339 | 23.339 | 23.339 | 0.235052 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17926) vms_mb | MB | 2 | 1618.510 | 1578.723 | 1658.297 | 1658.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17936) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17936) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17937) rss_mb | MB | 1 | 6.832 | 6.832 | 6.832 | 6.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17937) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17952) CPU | percent | 11 | 23.563 | 1.990 | 79.375 | 1.990 | 2.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17952) rss_mb | MB | 12 | 354.869 | 147.848 | 388.898 | 388.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17952) main thread run-queue wait | percent | 11 | 2.714 | 0.009 | 18.282 | 0.009 | 0.300812 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17952) vms_mb | MB | 12 | 8755.182 | 1304.309 | 10208.461 | 10208.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17975) CPU | percent | 1 | 66.429 | 66.429 | 66.429 | 66.429 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17975) rss_mb | MB | 2 | 246.594 | 193.863 | 299.324 | 299.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17975) main thread run-queue wait | percent | 1 | 20.122 | 20.122 | 20.122 | 20.122 | 0.202949 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17975) vms_mb | MB | 2 | 1669.387 | 1614.223 | 1724.551 | 1724.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17985) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17985) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17986) rss_mb | MB | 1 | 7.391 | 7.391 | 7.391 | 7.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17986) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18002) CPU | percent | 24 | 10.519 | 0.993 | 70.615 | 0.994 | 2.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18002) rss_mb | MB | 25 | 382.877 | 271.566 | 396.660 | 395.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18002) main thread run-queue wait | percent | 24 | 0.611 | 0.004 | 8.361 | 0.010 | 0.147464 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18002) vms_mb | MB | 25 | 9860.375 | 1666.766 | 10211.000 | 10210.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18030) rss_mb | MB | 1 | 179.883 | 179.883 | 179.883 | 179.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18030) vms_mb | MB | 1 | 1591.223 | 1591.223 | 1591.223 | 1591.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18047) rss_mb | MB | 1 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18047) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18048) rss_mb | MB | 1 | 19.328 | 19.328 | 19.328 | 19.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18048) vms_mb | MB | 1 | 211.684 | 211.684 | 211.684 | 211.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18065) CPU | percent | 11 | 17.367 | 1.989 | 55.618 | 1.989 | 1.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18065) rss_mb | MB | 12 | 370.021 | 298.629 | 389.160 | 389.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18065) main thread run-queue wait | percent | 11 | 3.517 | 0.006 | 28.170 | 0.006 | 0.393433 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18065) vms_mb | MB | 12 | 9487.199 | 1723.672 | 10208.152 | 10208.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18086) CPU | percent | 1 | 61.723 | 61.723 | 61.723 | 61.723 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18086) rss_mb | MB | 2 | 244.701 | 195.020 | 294.383 | 294.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18086) main thread run-queue wait | percent | 1 | 22.059 | 22.059 | 22.059 | 22.059 | 0.225154 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18086) vms_mb | MB | 2 | 1652.061 | 1614.973 | 1689.148 | 1689.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18096) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18096) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18097) rss_mb | MB | 1 | 6.934 | 6.934 | 6.934 | 6.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18097) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18114) CPU | percent | 11 | 19.332 | 0.995 | 65.583 | 6.957 | 2.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18114) rss_mb | MB | 12 | 369.523 | 262.449 | 391.617 | 391.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18114) main thread run-queue wait | percent | 11 | 3.450 | 0.005 | 17.010 | 0.030 | 0.382143 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18114) vms_mb | MB | 12 | 9481.148 | 1657.762 | 10209.211 | 10209.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18133) CPU | percent | 1 | 64.552 | 64.552 | 64.552 | 64.552 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18133) rss_mb | MB | 2 | 220.332 | 175.320 | 265.344 | 265.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18133) main thread run-queue wait | percent | 1 | 12.353 | 12.353 | 12.353 | 12.353 | 0.124385 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18133) vms_mb | MB | 2 | 1625.027 | 1589.973 | 1660.082 | 1660.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18163) CPU | percent | 39 | 9.814 | 0.993 | 90.007 | 6.961 | 3.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18163) rss_mb | MB | 40 | 380.292 | 229.520 | 391.336 | 389.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18163) main thread run-queue wait | percent | 39 | 1.038 | 0.002 | 14.490 | 0.022 | 0.408276 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18163) vms_mb | MB | 40 | 9784.401 | 1632.027 | 10214.781 | 10211.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18191) rss_mb | MB | 1 | 259.105 | 259.105 | 259.105 | 259.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18191) vms_mb | MB | 1 | 1655.316 | 1655.316 | 1655.316 | 1655.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18205) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18205) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18206) rss_mb | MB | 1 | 21.656 | 21.656 | 21.656 | 21.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18206) vms_mb | MB | 1 | 26.723 | 26.723 | 26.723 | 26.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18231) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18231) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18232) rss_mb | MB | 1 | 21.578 | 21.578 | 21.578 | 21.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18232) vms_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18247) CPU | percent | 20 | 11.211 | 0.992 | 72.494 | 1.986 | 2.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18247) rss_mb | MB | 21 | 381.390 | 248.090 | 397.566 | 397.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18247) main thread run-queue wait | percent | 20 | 0.578 | 0.004 | 8.254 | 0.014 | 0.116704 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18247) vms_mb | MB | 21 | 9787.957 | 1644.254 | 10204.188 | 10204.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18272) rss_mb | MB | 1 | 230.258 | 230.258 | 230.258 | 230.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18272) vms_mb | MB | 1 | 1632.699 | 1632.699 | 1632.699 | 1632.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18311) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18311) rss_mb | MB | 2 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18311) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18311) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18313) CPU | percent | 1 | 67.486 | 67.486 | 67.486 | 67.486 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18313) rss_mb | MB | 2 | 44.496 | 23.051 | 65.941 | 65.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18313) main thread run-queue wait | percent | 1 | 0.373 | 0.373 | 0.373 | 0.373 | 0.003760 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18313) vms_mb | MB | 2 | 54.451 | 29.047 | 79.855 | 79.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -m agency.harness.daemon (PID 18325) CPU | percent | 12 | 20.531 | 1.989 | 91.392 | 3.975 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -m agency.harness.daemon (PID 18325) rss_mb | MB | 13 | 351.513 | 115.453 | 391.535 | 391.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -m agency.harness.daemon (PID 18325) main thread run-queue wait | percent | 12 | 0.704 | 0.003 | 3.561 | 0.026 | 0.085113 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -m agency.harness.daemon (PID 18325) vms_mb | MB | 13 | 8827.294 | 904.512 | 10206.832 | 10206.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18350) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18350) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18351) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18351) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18356) rss_mb | MB | 1 | 228.715 | 228.715 | 228.715 | 228.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18356) vms_mb | MB | 1 | 1635.840 | 1635.840 | 1635.840 | 1635.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18375) CPU | percent | 11 | 17.130 | 0.995 | 72.620 | 0.995 | 1.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18375) rss_mb | MB | 12 | 365.704 | 259.832 | 387.223 | 387.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18375) main thread run-queue wait | percent | 11 | 0.637 | 0.003 | 3.707 | 0.014 | 0.070636 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18375) vms_mb | MB | 12 | 9469.039 | 1655.785 | 10207.121 | 10207.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18481) rss_mb | MB | 1 | 179.410 | 179.410 | 179.410 | 179.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18481) vms_mb | MB | 1 | 1590.973 | 1590.973 | 1590.973 | 1590.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18500) CPU | percent | 13 | 20.934 | 1.989 | 83.478 | 1.989 | 2.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18500) rss_mb | MB | 14 | 357.579 | 160.137 | 385.191 | 384.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18500) main thread run-queue wait | percent | 13 | 1.923 | 0.008 | 15.146 | 0.015 | 0.252030 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18500) vms_mb | MB | 14 | 8962.696 | 1315.715 | 10209.484 | 10208.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18525) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18525) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18526) rss_mb | MB | 1 | 9.902 | 9.902 | 9.902 | 9.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18526) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18527) CPU | percent | 1 | 67.411 | 67.411 | 67.411 | 67.411 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18527) rss_mb | MB | 2 | 173.938 | 87.797 | 260.078 | 260.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18527) main thread run-queue wait | percent | 1 | 15.766 | 15.766 | 15.766 | 15.766 | 0.159040 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18527) vms_mb | MB | 2 | 1469.553 | 1283.695 | 1655.410 | 1655.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18552) CPU | percent | 26 | 12.094 | 0.985 | 76.438 | 6.961 | 3.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18552) rss_mb | MB | 27 | 368.841 | 166.777 | 385.797 | 385.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18552) main thread run-queue wait | percent | 26 | 1.106 | 0.003 | 17.419 | 0.040 | 0.294238 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18552) vms_mb | MB | 27 | 9572.275 | 1577.719 | 10210.598 | 10209.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18575) CPU | percent | 1 | 61.081 | 61.081 | 61.081 | 61.081 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18575) rss_mb | MB | 2 | 238.838 | 183.691 | 293.984 | 293.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18575) main thread run-queue wait | percent | 1 | 17.534 | 17.534 | 17.534 | 17.534 | 0.180849 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18575) vms_mb | MB | 2 | 1640.916 | 1592.973 | 1688.859 | 1688.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18585) rss_mb | MB | 1 | 1.344 | 1.344 | 1.344 | 1.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18585) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18586) rss_mb | MB | 1 | 9.250 | 9.250 | 9.250 | 9.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18586) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18602) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18602) rss_mb | MB | 9 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18602) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18602) vms_mb | MB | 9 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18603) CPU | percent | 8 | 7.563 | 0.000 | 60.503 | 0.000 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18603) rss_mb | MB | 9 | 62.808 | 33.051 | 66.527 | 66.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18603) main thread run-queue wait | percent | 8 | 0.043 | 0.000 | 0.348 | 0.000 | 0.003507 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18603) vms_mb | MB | 9 | 75.960 | 42.574 | 80.133 | 80.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18615) CPU | percent | 10 | 24.125 | 1.988 | 84.271 | 1.988 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18615) rss_mb | MB | 11 | 360.217 | 241.992 | 384.348 | 384.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18615) main thread run-queue wait | percent | 10 | 2.787 | 0.006 | 19.410 | 0.006 | 0.280993 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18615) vms_mb | MB | 11 | 9416.522 | 1639.059 | 10211.738 | 10211.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18634) rss_mb | MB | 1 | 46.527 | 46.527 | 46.527 | 46.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18634) vms_mb | MB | 1 | 847.070 | 847.070 | 847.070 | 847.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18643) rss_mb | MB | 1 | 254.730 | 254.730 | 254.730 | 254.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18643) vms_mb | MB | 1 | 1651.086 | 1651.086 | 1651.086 | 1651.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18662) CPU | percent | 15 | 19.207 | 0.995 | 88.468 | 1.986 | 2.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18662) rss_mb | MB | 16 | 362.911 | 106.023 | 394.906 | 394.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18662) main thread run-queue wait | percent | 15 | 2.790 | 0.005 | 30.086 | 0.005 | 0.421661 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18662) vms_mb | MB | 16 | 9113.622 | 1283.598 | 10206.941 | 10206.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18681) CPU | percent | 1 | 57.539 | 57.539 | 57.539 | 57.539 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18681) rss_mb | MB | 2 | 251.074 | 206.902 | 295.246 | 295.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18681) main thread run-queue wait | percent | 1 | 23.979 | 23.979 | 23.979 | 23.979 | 0.241710 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18681) vms_mb | MB | 2 | 1654.527 | 1619.234 | 1689.820 | 1689.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18691) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18691) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18692) rss_mb | MB | 1 | 10.125 | 10.125 | 10.125 | 10.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18692) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18713) CPU | percent | 13 | 21.231 | 1.989 | 82.392 | 7.958 | 2.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18713) rss_mb | MB | 14 | 363.227 | 180.977 | 392.305 | 392.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18713) main thread run-queue wait | percent | 13 | 2.580 | 0.005 | 21.016 | 0.029 | 0.338471 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18713) vms_mb | MB | 14 | 8983.213 | 1591.719 | 10209.141 | 10209.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18734) CPU | percent | 1 | 59.398 | 59.398 | 59.398 | 59.398 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18734) rss_mb | MB | 2 | 252.262 | 207.840 | 296.684 | 296.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18734) main thread run-queue wait | percent | 1 | 21.501 | 21.501 | 21.501 | 21.501 | 0.217188 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18734) vms_mb | MB | 2 | 1655.342 | 1619.469 | 1691.215 | 1691.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18763) CPU | percent | 10 | 21.053 | 0.994 | 71.626 | 3.979 | 2.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18763) rss_mb | MB | 11 | 361.042 | 255.762 | 382.477 | 382.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18763) main thread run-queue wait | percent | 10 | 2.869 | 0.007 | 22.217 | 0.010 | 0.289570 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18763) vms_mb | MB | 11 | 8667.327 | 1651.504 | 10204.469 | 10204.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18790) rss_mb | MB | 1 | 174.980 | 174.980 | 174.980 | 174.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18790) vms_mb | MB | 1 | 1589.723 | 1589.723 | 1589.723 | 1589.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18810) CPU | percent | 10 | 19.068 | 1.988 | 65.479 | 1.990 | 1.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18810) rss_mb | MB | 11 | 370.713 | 294.668 | 390.176 | 390.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18810) main thread run-queue wait | percent | 10 | 2.940 | 0.006 | 22.462 | 0.007 | 0.296215 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18810) vms_mb | MB | 11 | 9419.450 | 1689.758 | 10206.137 | 10206.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18834) CPU | percent | 1 | 51.613 | 51.613 | 51.613 | 51.613 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18834) rss_mb | MB | 2 | 187.945 | 146.320 | 229.570 | 229.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18834) main thread run-queue wait | percent | 1 | 23.063 | 23.063 | 23.063 | 23.063 | 0.232361 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18834) vms_mb | MB | 2 | 1469.047 | 1302.234 | 1635.859 | 1635.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18860) CPU | percent | 11 | 19.325 | 0.994 | 70.494 | 1.990 | 2.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18860) rss_mb | MB | 12 | 364.180 | 259.629 | 384.645 | 384.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18860) main thread run-queue wait | percent | 11 | 3.036 | 0.002 | 23.644 | 0.011 | 0.336424 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18860) vms_mb | MB | 12 | 9481.198 | 1656.031 | 10207.617 | 10207.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18882) rss_mb | MB | 1 | 213.598 | 213.598 | 213.598 | 213.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18882) vms_mb | MB | 1 | 1622.711 | 1622.711 | 1622.711 | 1622.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18908) CPU | percent | 17 | 15.929 | 0.994 | 75.431 | 1.989 | 2.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18908) rss_mb | MB | 18 | 366.883 | 172.984 | 388.844 | 388.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18908) main thread run-queue wait | percent | 17 | 2.350 | 0.006 | 22.685 | 0.008 | 0.404301 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18908) vms_mb | MB | 18 | 9251.364 | 1579.969 | 10205.523 | 10205.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18928) rss_mb | MB | 1 | 229.535 | 229.535 | 229.535 | 229.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18928) vms_mb | MB | 1 | 1631.949 | 1631.949 | 1631.949 | 1631.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18957) CPU | percent | 12 | 21.778 | 0.994 | 74.512 | 7.953 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18957) rss_mb | MB | 13 | 361.330 | 170.398 | 391.023 | 391.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18957) main thread run-queue wait | percent | 12 | 2.429 | 0.004 | 16.830 | 0.024 | 0.293325 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18957) vms_mb | MB | 13 | 8886.745 | 1579.219 | 10209.031 | 10209.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18985) CPU | percent | 1 | 69.568 | 69.568 | 69.568 | 69.568 | 0.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18985) rss_mb | MB | 2 | 210.066 | 148.289 | 271.844 | 271.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18985) main thread run-queue wait | percent | 1 | 18.084 | 18.084 | 18.084 | 18.084 | 0.181964 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18985) vms_mb | MB | 2 | 1485.727 | 1304.117 | 1667.336 | 1667.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19007) CPU | percent | 10 | 21.357 | 0.994 | 72.608 | 2.984 | 2.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19007) rss_mb | MB | 11 | 363.739 | 237.188 | 390.242 | 390.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19007) main thread run-queue wait | percent | 10 | 3.145 | 0.005 | 22.612 | 0.018 | 0.316902 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19007) vms_mb | MB | 11 | 9413.181 | 1638.020 | 10207.273 | 10207.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19030) CPU | percent | 1 | 45.653 | 45.653 | 45.653 | 45.653 | 0.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19030) rss_mb | MB | 2 | 131.072 | 40.625 | 221.520 | 221.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19030) main thread run-queue wait | percent | 1 | 20.396 | 20.396 | 20.396 | 20.396 | 0.205507 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19030) vms_mb | MB | 2 | 1398.455 | 1172.449 | 1624.461 | 1624.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19056) CPU | percent | 11 | 24.915 | 0.995 | 90.408 | 2.982 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19056) rss_mb | MB | 12 | 343.806 | 45.453 | 389.156 | 389.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19056) main thread run-queue wait | percent | 11 | 3.040 | 0.004 | 21.422 | 0.028 | 0.337144 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19056) vms_mb | MB | 12 | 8734.457 | 1174.262 | 10204.988 | 10204.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19077) CPU | percent | 1 | 57.493 | 57.493 | 57.493 | 57.493 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19077) rss_mb | MB | 2 | 248.775 | 203.066 | 294.484 | 294.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19077) main thread run-queue wait | percent | 1 | 22.837 | 22.837 | 22.837 | 22.837 | 0.230380 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19077) vms_mb | MB | 2 | 1653.520 | 1617.977 | 1689.062 | 1689.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19087) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19087) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19088) rss_mb | MB | 1 | 7.629 | 7.629 | 7.629 | 7.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19088) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19105) CPU | percent | 15 | 17.801 | 0.995 | 70.623 | 1.988 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19105) rss_mb | MB | 16 | 366.983 | 196.879 | 389.801 | 389.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19105) main thread run-queue wait | percent | 15 | 2.195 | 0.010 | 16.660 | 0.010 | 0.332545 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19105) vms_mb | MB | 16 | 9134.598 | 1616.547 | 10205.914 | 10205.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19124) rss_mb | MB | 1 | 219.969 | 219.969 | 219.969 | 219.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19124) vms_mb | MB | 1 | 1623.727 | 1623.727 | 1623.727 | 1623.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19136) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19136) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19137) rss_mb | MB | 1 | 7.367 | 7.367 | 7.367 | 7.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19137) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19155) CPU | percent | 22 | 11.178 | 0.994 | 64.535 | 0.995 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19155) rss_mb | MB | 23 | 385.536 | 291.246 | 397.438 | 397.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19155) main thread run-queue wait | percent | 22 | 1.625 | 0.001 | 19.189 | 0.007 | 0.360528 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19155) vms_mb | MB | 23 | 9832.878 | 1686.523 | 10211.031 | 10211.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19175) CPU | percent | 1 | 57.544 | 57.544 | 57.544 | 57.544 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19175) rss_mb | MB | 2 | 218.285 | 175.582 | 260.988 | 260.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19175) main thread run-queue wait | percent | 1 | 22.923 | 22.923 | 22.923 | 22.923 | 0.231051 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19175) vms_mb | MB | 2 | 1623.268 | 1590.473 | 1656.062 | 1656.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19205) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19205) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 19206) rss_mb | MB | 1 | 18.277 | 18.277 | 18.277 | 18.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 19206) vms_mb | MB | 1 | 24.234 | 24.234 | 24.234 | 24.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19221) CPU | percent | 13 | 18.724 | 0.994 | 82.354 | 1.987 | 2.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19221) rss_mb | MB | 14 | 356.316 | 155.297 | 389.289 | 388.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19221) main thread run-queue wait | percent | 13 | 0.768 | 0.006 | 4.851 | 0.006 | 0.100559 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19221) vms_mb | MB | 14 | 8951.991 | 1499.465 | 10177.418 | 10176.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19252) rss_mb | MB | 1 | 151.426 | 151.426 | 151.426 | 151.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19252) vms_mb | MB | 1 | 1315.969 | 1315.969 | 1315.969 | 1315.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19274) CPU | percent | 14 | 20.361 | 0.995 | 85.499 | 1.990 | 2.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19274) rss_mb | MB | 15 | 363.310 | 160.996 | 394.242 | 393.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19274) main thread run-queue wait | percent | 14 | 2.632 | 0.006 | 24.056 | 0.020 | 0.371376 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19274) vms_mb | MB | 15 | 9043.140 | 1317.719 | 10206.809 | 10205.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19295) CPU | percent | 1 | 59.459 | 59.459 | 59.459 | 59.459 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19295) rss_mb | MB | 2 | 247.346 | 200.098 | 294.594 | 294.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19295) main thread run-queue wait | percent | 1 | 23.271 | 23.271 | 23.271 | 23.271 | 0.234829 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19295) vms_mb | MB | 2 | 1653.672 | 1618.004 | 1689.340 | 1689.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19305) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19305) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19306) rss_mb | MB | 1 | 9.914 | 9.914 | 9.914 | 9.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19306) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19326) CPU | percent | 28 | 11.096 | 0.994 | 76.412 | 1.986 | 3.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19326) rss_mb | MB | 29 | 374.346 | 166.707 | 390.000 | 389.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19326) main thread run-queue wait | percent | 28 | 1.365 | 0.004 | 23.421 | 0.004 | 0.385440 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19326) vms_mb | MB | 29 | 9614.418 | 1577.719 | 10207.617 | 10206.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19345) CPU | percent | 1 | 59.503 | 59.503 | 59.503 | 59.503 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19345) rss_mb | MB | 2 | 259.689 | 217.195 | 302.184 | 302.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19345) main thread run-queue wait | percent | 1 | 23.342 | 23.342 | 23.342 | 23.342 | 0.235367 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19345) vms_mb | MB | 2 | 1675.082 | 1623.227 | 1726.938 | 1726.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19447) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19447) rss_mb | MB | 3 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19447) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19447) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19448) CPU | percent | 2 | 30.744 | 0.000 | 61.489 | 0.000 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19448) rss_mb | MB | 3 | 54.130 | 29.961 | 66.215 | 66.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19448) main thread run-queue wait | percent | 2 | 0.129 | 0.000 | 0.257 | 0.000 | 0.002594 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19448) vms_mb | MB | 3 | 66.591 | 39.586 | 80.094 | 80.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19469) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19469) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 19470) rss_mb | MB | 1 | 15.816 | 15.816 | 15.816 | 15.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 19470) vms_mb | MB | 1 | 20.711 | 20.711 | 20.711 | 20.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19479) CPU | percent | 10 | 24.050 | 0.995 | 71.604 | 4.971 | 2.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19479) rss_mb | MB | 11 | 365.159 | 260.648 | 387.461 | 387.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19479) main thread run-queue wait | percent | 10 | 2.904 | 0.008 | 14.155 | 0.027 | 0.308009 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19479) vms_mb | MB | 11 | 9418.493 | 1656.254 | 10211.898 | 10211.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 19500) rss_mb | MB | 1 | 47.934 | 47.934 | 47.934 | 47.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 19500) vms_mb | MB | 1 | 843.387 | 843.387 | 843.387 | 843.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19504) rss_mb | MB | 1 | 181.574 | 181.574 | 181.574 | 181.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19504) vms_mb | MB | 1 | 1591.723 | 1591.723 | 1591.723 | 1591.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19523) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19523) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19524) rss_mb | MB | 1 | 6.562 | 6.562 | 6.562 | 6.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19524) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19528) CPU | percent | 13 | 19.089 | 0.994 | 72.549 | 5.969 | 2.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19528) rss_mb | MB | 14 | 367.033 | 229.117 | 388.531 | 388.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19528) main thread run-queue wait | percent | 13 | 2.128 | 0.009 | 17.325 | 0.085 | 0.278953 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19528) vms_mb | MB | 14 | 8988.381 | 1632.285 | 10209.859 | 10209.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19549) rss_mb | MB | 1 | 199.805 | 199.805 | 199.805 | 199.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19549) vms_mb | MB | 1 | 1617.977 | 1617.977 | 1617.977 | 1617.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19579) CPU | percent | 12 | 20.684 | 0.994 | 73.489 | 1.990 | 2.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19579) rss_mb | MB | 13 | 364.289 | 228.086 | 387.660 | 387.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19579) main thread run-queue wait | percent | 12 | 3.102 | 0.012 | 16.815 | 0.012 | 0.375134 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19579) vms_mb | MB | 13 | 8893.632 | 1631.055 | 10209.363 | 10209.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19599) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19599) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19600) rss_mb | MB | 1 | 9.867 | 9.867 | 9.867 | 9.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19600) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19601) CPU | percent | 1 | 62.476 | 62.476 | 62.476 | 62.476 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19601) rss_mb | MB | 2 | 174.375 | 95.676 | 253.074 | 253.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19601) main thread run-queue wait | percent | 1 | 12.028 | 12.028 | 12.028 | 12.028 | 0.121288 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19601) vms_mb | MB | 2 | 1466.516 | 1283.695 | 1649.336 | 1649.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19613) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19613) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19614) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19614) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19629) CPU | percent | 12 | 18.021 | 0.995 | 72.464 | 1.989 | 2.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19629) rss_mb | MB | 13 | 367.703 | 272.926 | 385.230 | 385.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19629) main thread run-queue wait | percent | 12 | 2.939 | 0.007 | 20.561 | 0.020 | 0.356701 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19629) vms_mb | MB | 13 | 9534.416 | 1667.770 | 10205.301 | 10205.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19648) CPU | percent | 1 | 63.097 | 63.097 | 63.097 | 63.097 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19648) rss_mb | MB | 2 | 220.160 | 168.277 | 272.043 | 272.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19648) main thread run-queue wait | percent | 1 | 19.888 | 19.888 | 19.888 | 19.888 | 0.201722 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19648) vms_mb | MB | 2 | 1622.562 | 1578.473 | 1666.652 | 1666.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19676) CPU | percent | 25 | 10.050 | 0.986 | 67.581 | 0.990 | 2.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19676) rss_mb | MB | 26 | 382.912 | 294.707 | 393.375 | 393.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19676) main thread run-queue wait | percent | 25 | 1.364 | 0.004 | 15.678 | 0.024 | 0.343515 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19676) vms_mb | MB | 26 | 9875.738 | 1689.461 | 10211.336 | 10211.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19696) CPU | percent | 1 | 55.586 | 55.586 | 55.586 | 55.586 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19696) rss_mb | MB | 2 | 214.076 | 168.266 | 259.887 | 259.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19696) main thread run-queue wait | percent | 1 | 13.116 | 13.116 | 13.116 | 13.116 | 0.132137 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19696) vms_mb | MB | 2 | 1617.018 | 1578.473 | 1655.562 | 1655.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19722) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19722) rss_mb | MB | 3 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19722) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19722) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19723) CPU | percent | 2 | 30.763 | 0.000 | 61.525 | 0.000 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19723) rss_mb | MB | 3 | 66.621 | 45.324 | 77.270 | 77.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19723) main thread run-queue wait | percent | 2 | 0.164 | 0.000 | 0.328 | 0.000 | 0.003307 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19723) vms_mb | MB | 3 | 267.496 | 242.746 | 279.871 | 279.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19727) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19727) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 19728) rss_mb | MB | 1 | 18.879 | 18.879 | 18.879 | 18.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 19728) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19741) CPU | percent | 29 | 10.811 | 0.993 | 76.438 | 2.972 | 3.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19741) rss_mb | MB | 30 | 383.359 | 204.754 | 398.145 | 397.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19741) main thread run-queue wait | percent | 29 | 1.335 | 0.002 | 24.402 | 0.033 | 0.390298 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19741) vms_mb | MB | 30 | 9640.834 | 1619.027 | 10214.074 | 10213.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19761) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19761) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19762) rss_mb | MB | 1 | 9.215 | 9.215 | 9.215 | 9.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19762) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19765) CPU | percent | 1 | 63.462 | 63.462 | 63.462 | 63.462 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19765) rss_mb | MB | 2 | 244.527 | 194.074 | 294.980 | 294.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19765) main thread run-queue wait | percent | 1 | 22.657 | 22.657 | 22.657 | 22.657 | 0.228491 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19765) vms_mb | MB | 2 | 1651.895 | 1614.473 | 1689.316 | 1689.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19775) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19775) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19776) rss_mb | MB | 1 | 7.254 | 7.254 | 7.254 | 7.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19776) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19810) CPU | percent | 12 | 22.105 | 0.995 | 74.556 | 6.961 | 2.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19810) rss_mb | MB | 13 | 363.494 | 197.625 | 391.359 | 391.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19810) main thread run-queue wait | percent | 12 | 3.626 | 0.004 | 26.543 | 0.040 | 0.437801 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19810) vms_mb | MB | 13 | 8890.782 | 1617.047 | 10209.383 | 10209.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19832) rss_mb | MB | 1 | 229.785 | 229.785 | 229.785 | 229.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19832) vms_mb | MB | 1 | 1636.090 | 1636.090 | 1636.090 | 1636.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19860) CPU | percent | 13 | 19.402 | 0.995 | 73.581 | 0.995 | 2.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19860) rss_mb | MB | 14 | 365.514 | 208.395 | 390.070 | 390.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19860) main thread run-queue wait | percent | 13 | 3.142 | 0.008 | 20.544 | 0.008 | 0.411684 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19860) vms_mb | MB | 14 | 8986.701 | 1619.531 | 10209.734 | 10209.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19877) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19877) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19878) rss_mb | MB | 1 | 9.246 | 9.246 | 9.246 | 9.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19878) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19879) CPU | percent | 1 | 61.486 | 61.486 | 61.486 | 61.486 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19879) rss_mb | MB | 2 | 144.867 | 54.352 | 235.383 | 235.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19879) main thread run-queue wait | percent | 1 | 6.524 | 6.524 | 6.524 | 6.524 | 0.065790 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19879) vms_mb | MB | 2 | 1437.473 | 1238.609 | 1636.336 | 1636.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19907) CPU | percent | 13 | 16.273 | 1.989 | 66.522 | 1.989 | 2.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19907) rss_mb | MB | 14 | 374.320 | 295.461 | 391.883 | 391.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19907) main thread run-queue wait | percent | 13 | 2.912 | 0.004 | 19.387 | 0.004 | 0.381320 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19907) vms_mb | MB | 14 | 9589.347 | 1690.164 | 10211.574 | 10210.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19928) CPU | percent | 1 | 65.474 | 65.474 | 65.474 | 65.474 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19928) rss_mb | MB | 2 | 238.795 | 188.566 | 289.023 | 289.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19928) main thread run-queue wait | percent | 1 | 16.869 | 16.869 | 16.869 | 16.869 | 0.170047 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19928) vms_mb | MB | 2 | 1638.900 | 1594.223 | 1683.578 | 1683.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19959) CPU | percent | 12 | 22.832 | 1.989 | 87.499 | 1.989 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19959) rss_mb | MB | 13 | 358.901 | 153.188 | 392.840 | 392.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19959) main thread run-queue wait | percent | 12 | 1.846 | 0.005 | 10.825 | 0.005 | 0.223130 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19959) vms_mb | MB | 13 | 8882.463 | 1499.215 | 10207.457 | 10207.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19980) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19980) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19981) rss_mb | MB | 1 | 7.445 | 7.445 | 7.445 | 7.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19981) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19987) rss_mb | MB | 1 | 229.160 | 229.160 | 229.160 | 229.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19987) vms_mb | MB | 1 | 1631.703 | 1631.703 | 1631.703 | 1631.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20007) CPU | percent | 12 | 17.666 | 1.988 | 69.515 | 1.989 | 2.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20007) rss_mb | MB | 13 | 375.618 | 285.918 | 395.117 | 394.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20007) main thread run-queue wait | percent | 12 | 2.993 | 0.004 | 14.653 | 0.013 | 0.361835 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20007) vms_mb | MB | 13 | 9540.791 | 1681.340 | 10211.574 | 10210.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20028) CPU | percent | 1 | 57.547 | 57.547 | 57.547 | 57.547 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20028) rss_mb | MB | 2 | 216.535 | 172.383 | 260.688 | 260.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20028) main thread run-queue wait | percent | 1 | 12.720 | 12.720 | 12.720 | 12.720 | 0.128201 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20028) vms_mb | MB | 2 | 1617.877 | 1579.723 | 1656.031 | 1656.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20059) CPU | percent | 13 | 21.709 | 0.995 | 77.543 | 2.983 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20059) rss_mb | MB | 14 | 358.056 | 167.184 | 388.734 | 387.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20059) main thread run-queue wait | percent | 13 | 3.241 | 0.010 | 26.547 | 0.016 | 0.424388 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20059) vms_mb | MB | 14 | 8982.388 | 1578.219 | 10211.938 | 10211.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20079) CPU | percent | 1 | 62.509 | 62.509 | 62.509 | 62.509 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20079) rss_mb | MB | 2 | 252.381 | 206.906 | 297.855 | 297.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20079) main thread run-queue wait | percent | 1 | 25.507 | 25.507 | 25.507 | 25.507 | 0.257073 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20079) vms_mb | MB | 2 | 1656.035 | 1619.742 | 1692.328 | 1692.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20089) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20089) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20090) rss_mb | MB | 1 | 10.691 | 10.691 | 10.691 | 10.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20090) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20110) CPU | percent | 16 | 13.284 | 0.993 | 68.475 | 0.995 | 2.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20110) rss_mb | MB | 17 | 379.026 | 294.465 | 393.859 | 393.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20110) main thread run-queue wait | percent | 16 | 1.104 | 0.003 | 12.762 | 0.004 | 0.177881 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20110) vms_mb | MB | 17 | 9699.015 | 1689.109 | 10208.727 | 10208.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20139) rss_mb | MB | 1 | 186.996 | 186.996 | 186.996 | 186.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20139) vms_mb | MB | 1 | 1593.973 | 1593.973 | 1593.973 | 1593.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 20163) CPU | percent | 11 | 17.333 | 0.995 | 64.612 | 1.986 | 1.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 20163) rss_mb | MB | 12 | 372.928 | 300.492 | 390.516 | 390.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 20163) main thread run-queue wait | percent | 11 | 2.567 | 0.009 | 25.708 | 0.011 | 0.284855 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 20163) vms_mb | MB | 12 | 9490.978 | 1725.156 | 10210.895 | 10210.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20187) CPU | percent | 1 | 50.537 | 50.537 | 50.537 | 50.537 | 0.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20187) rss_mb | MB | 2 | 187.705 | 146.555 | 228.855 | 228.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20187) main thread run-queue wait | percent | 1 | 21.193 | 21.193 | 21.193 | 21.193 | 0.213867 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20187) vms_mb | MB | 2 | 1469.541 | 1303.234 | 1635.848 | 1635.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20193) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20193) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20195) rss_mb | MB | 1 | 10.742 | 10.742 | 10.742 | 10.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20195) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20213) CPU | percent | 12 | 23.552 | 0.995 | 91.450 | 4.972 | 2.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20213) rss_mb | MB | 13 | 356.598 | 83.324 | 396.859 | 396.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20213) main thread run-queue wait | percent | 12 | 2.014 | 0.003 | 17.034 | 0.021 | 0.243663 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20213) vms_mb | MB | 13 | 8864.107 | 1283.598 | 10211.941 | 10211.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20235) CPU | percent | 1 | 54.565 | 54.565 | 54.565 | 54.565 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20235) rss_mb | MB | 2 | 213.242 | 167.316 | 259.168 | 259.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20235) main thread run-queue wait | percent | 1 | 14.637 | 14.637 | 14.637 | 14.637 | 0.147533 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20235) vms_mb | MB | 2 | 1616.910 | 1578.223 | 1655.598 | 1655.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20243) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20243) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20244) rss_mb | MB | 1 | 7.676 | 7.676 | 7.676 | 7.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20244) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20268) CPU | percent | 17 | 16.161 | 0.993 | 75.588 | 6.964 | 2.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20268) rss_mb | MB | 18 | 371.398 | 194.250 | 393.035 | 392.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20268) main thread run-queue wait | percent | 17 | 2.014 | 0.007 | 20.145 | 0.044 | 0.345938 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20268) vms_mb | MB | 18 | 9257.461 | 1614.719 | 10211.168 | 10210.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20288) rss_mb | MB | 1 | 228.797 | 228.797 | 228.797 | 228.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20288) vms_mb | MB | 1 | 1635.355 | 1635.355 | 1635.355 | 1635.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20319) CPU | percent | 15 | 15.377 | 0.995 | 73.609 | 4.970 | 2.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20319) rss_mb | MB | 16 | 376.950 | 256.754 | 395.406 | 395.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20319) main thread run-queue wait | percent | 15 | 1.924 | 0.007 | 15.744 | 0.018 | 0.290289 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20319) vms_mb | MB | 16 | 9664.940 | 1652.305 | 10211.055 | 10211.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20343) rss_mb | MB | 1 | 204.691 | 204.691 | 204.691 | 204.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20343) vms_mb | MB | 1 | 1618.734 | 1618.734 | 1618.734 | 1618.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20364) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20364) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20369) CPU | percent | 10 | 25.120 | 1.988 | 71.481 | 7.958 | 2.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20369) rss_mb | MB | 11 | 364.027 | 211.305 | 395.422 | 395.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20369) main thread run-queue wait | percent | 10 | 4.428 | 0.006 | 20.061 | 0.038 | 0.446184 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20369) vms_mb | MB | 11 | 8654.697 | 1622.535 | 10209.500 | 10209.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20388) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20388) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20389) rss_mb | MB | 1 | 10.734 | 10.734 | 10.734 | 10.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20389) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20390) CPU | percent | 1 | 61.446 | 61.446 | 61.446 | 61.446 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20390) rss_mb | MB | 2 | 195.717 | 136.973 | 254.461 | 254.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20390) main thread run-queue wait | percent | 1 | 19.534 | 19.534 | 19.534 | 19.534 | 0.197103 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20390) vms_mb | MB | 2 | 1473.090 | 1296.352 | 1649.828 | 1649.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20403) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20403) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20404) rss_mb | MB | 1 | 5.680 | 5.680 | 5.680 | 5.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20404) vms_mb | MB | 1 | 11.645 | 11.645 | 11.645 | 11.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20419) CPU | percent | 14 | 19.507 | 0.990 | 69.464 | 6.956 | 2.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20419) rss_mb | MB | 15 | 370.351 | 194.402 | 396.234 | 396.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20419) main thread run-queue wait | percent | 14 | 2.417 | 0.010 | 21.325 | 0.040 | 0.340970 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20419) vms_mb | MB | 15 | 9068.500 | 1614.719 | 10210.707 | 10210.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20520) CPU | percent | 1 | 58.545 | 58.545 | 58.545 | 58.545 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20520) rss_mb | MB | 2 | 241.160 | 193.719 | 288.602 | 288.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20520) main thread run-queue wait | percent | 1 | 14.573 | 14.573 | 14.573 | 14.573 | 0.146864 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20520) vms_mb | MB | 2 | 1649.008 | 1614.473 | 1683.543 | 1683.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20563) CPU | percent | 13 | 18.479 | 0.956 | 74.558 | 1.990 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20563) rss_mb | MB | 14 | 368.372 | 229.746 | 393.473 | 392.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20563) main thread run-queue wait | percent | 13 | 1.318 | 0.006 | 13.469 | 0.013 | 0.176254 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20563) vms_mb | MB | 14 | 8987.191 | 1632.039 | 10206.480 | 10205.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20589) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20589) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20590) rss_mb | MB | 1 | 10.445 | 10.445 | 10.445 | 10.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20590) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20592) rss_mb | MB | 1 | 62.594 | 62.594 | 62.594 | 62.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20592) vms_mb | MB | 1 | 1238.609 | 1238.609 | 1238.609 | 1238.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20616) CPU | percent | 12 | 22.024 | 0.995 | 72.491 | 4.972 | 2.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20616) rss_mb | MB | 13 | 361.239 | 182.820 | 391.664 | 391.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20616) main thread run-queue wait | percent | 12 | 2.766 | 0.013 | 18.974 | 0.026 | 0.334111 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20616) vms_mb | MB | 13 | 8889.974 | 1593.219 | 10209.973 | 10209.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20636) CPU | percent | 1 | 56.643 | 56.643 | 56.643 | 56.643 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20636) rss_mb | MB | 2 | 252.244 | 209.070 | 295.418 | 295.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20636) main thread run-queue wait | percent | 1 | 16.397 | 16.397 | 16.397 | 16.397 | 0.165004 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20636) vms_mb | MB | 2 | 1655.104 | 1620.230 | 1689.977 | 1689.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20657) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20657) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20658) rss_mb | MB | 1 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20658) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20662) CPU | percent | 15 | 17.822 | 0.995 | 76.611 | 0.995 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20662) rss_mb | MB | 16 | 373.913 | 202.793 | 399.430 | 398.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20662) main thread run-queue wait | percent | 15 | 2.393 | 0.001 | 22.858 | 0.018 | 0.361172 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20662) vms_mb | MB | 16 | 9138.719 | 1618.281 | 10211.984 | 10211.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20683) CPU | percent | 1 | 57.670 | 57.670 | 57.670 | 57.670 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20683) rss_mb | MB | 2 | 261.635 | 221.309 | 301.961 | 301.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20683) main thread run-queue wait | percent | 1 | 16.753 | 16.753 | 16.753 | 16.753 | 0.168487 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20683) vms_mb | MB | 2 | 1675.279 | 1624.227 | 1726.332 | 1726.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20715) CPU | percent | 14 | 18.790 | 1.986 | 74.452 | 2.984 | 2.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20715) rss_mb | MB | 15 | 367.606 | 195.121 | 392.242 | 392.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20715) main thread run-queue wait | percent | 14 | 1.119 | 0.007 | 8.440 | 0.068 | 0.158130 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20715) vms_mb | MB | 15 | 9069.233 | 1614.469 | 10211.020 | 10210.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20747) rss_mb | MB | 1 | 261.305 | 261.305 | 261.305 | 261.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20747) vms_mb | MB | 1 | 1656.551 | 1656.551 | 1656.551 | 1656.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20769) CPU | percent | 12 | 20.943 | 0.994 | 76.456 | 2.984 | 2.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20769) rss_mb | MB | 13 | 362.399 | 208.898 | 387.910 | 387.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20769) main thread run-queue wait | percent | 12 | 1.429 | 0.004 | 9.659 | 0.018 | 0.172597 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20769) vms_mb | MB | 13 | 8894.441 | 1619.777 | 10211.125 | 10210.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20787) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20787) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20788) rss_mb | MB | 1 | 9.914 | 9.914 | 9.914 | 9.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20788) vms_mb | MB | 1 | 13.578 | 13.578 | 13.578 | 13.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20798) rss_mb | MB | 1 | 268.738 | 268.738 | 268.738 | 268.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20798) vms_mb | MB | 1 | 1664.566 | 1664.566 | 1664.566 | 1664.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20820) CPU | percent | 18 | 14.424 | 0.000 | 85.447 | 0.995 | 2.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20820) rss_mb | MB | 19 | 369.801 | 161.168 | 394.305 | 393.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20820) main thread run-queue wait | percent | 18 | 1.152 | 0.007 | 8.151 | 0.008 | 0.208766 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20820) vms_mb | MB | 19 | 9291.489 | 1317.719 | 10210.426 | 10210.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20843) CPU | percent | 1 | 70.518 | 70.518 | 70.518 | 70.518 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20843) rss_mb | MB | 2 | 221.291 | 167.371 | 275.211 | 275.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20843) main thread run-queue wait | percent | 1 | 13.988 | 13.988 | 13.988 | 13.988 | 0.140842 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20843) vms_mb | MB | 2 | 1624.279 | 1578.723 | 1669.836 | 1669.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20872) CPU | percent | 12 | 16.986 | 0.994 | 75.423 | 1.989 | 2.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20872) rss_mb | MB | 13 | 368.636 | 229.027 | 393.992 | 393.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20872) main thread run-queue wait | percent | 12 | 0.816 | 0.006 | 3.860 | 0.013 | 0.099653 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20872) vms_mb | MB | 13 | 8891.014 | 1636.031 | 10203.000 | 10203.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20901) CPU | percent | 1 | 84.511 | 84.511 | 84.511 | 84.511 | 0.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20901) rss_mb | MB | 2 | 200.527 | 104.199 | 296.855 | 296.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20901) main thread run-queue wait | percent | 1 | 8.160 | 8.160 | 8.160 | 8.160 | 0.084005 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20901) vms_mb | MB | 2 | 1487.586 | 1283.695 | 1691.477 | 1691.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20922) CPU | percent | 12 | 20.451 | 0.994 | 73.433 | 8.950 | 2.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20922) rss_mb | MB | 13 | 360.030 | 184.215 | 391.805 | 391.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20922) main thread run-queue wait | percent | 12 | 1.159 | 0.001 | 5.981 | 0.040 | 0.140027 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20922) vms_mb | MB | 13 | 8887.924 | 1592.969 | 10208.672 | 10208.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20943) CPU | percent | 1 | 68.594 | 68.594 | 68.594 | 68.594 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20943) rss_mb | MB | 2 | 218.357 | 158.082 | 278.633 | 278.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20943) main thread run-queue wait | percent | 1 | 8.587 | 8.587 | 8.587 | 8.587 | 0.086376 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20943) vms_mb | MB | 2 | 1586.791 | 1499.969 | 1673.613 | 1673.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20969) CPU | percent | 11 | 21.040 | 0.995 | 76.438 | 0.995 | 2.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20969) rss_mb | MB | 12 | 365.416 | 237.055 | 390.688 | 390.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20969) main thread run-queue wait | percent | 11 | 1.150 | 0.005 | 6.505 | 0.018 | 0.127294 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20969) vms_mb | MB | 12 | 8786.533 | 1637.309 | 10208.195 | 10208.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20997) rss_mb | MB | 1 | 288.434 | 288.434 | 288.434 | 288.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20997) vms_mb | MB | 1 | 1683.059 | 1683.059 | 1683.059 | 1683.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21016) CPU | percent | 14 | 20.496 | 0.993 | 86.343 | 0.993 | 2.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21016) rss_mb | MB | 15 | 364.741 | 158.629 | 395.887 | 395.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21016) main thread run-queue wait | percent | 14 | 1.340 | 0.007 | 8.785 | 0.007 | 0.188900 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21016) vms_mb | MB | 15 | 9059.855 | 1499.965 | 10211.406 | 10210.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21040) CPU | percent | 1 | 50.647 | 50.647 | 50.647 | 50.647 | 0.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21040) rss_mb | MB | 2 | 170.105 | 105.156 | 235.055 | 235.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21040) main thread run-queue wait | percent | 1 | 11.887 | 11.887 | 11.887 | 11.887 | 0.119694 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21040) vms_mb | MB | 2 | 1459.771 | 1283.695 | 1635.848 | 1635.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21067) CPU | percent | 14 | 19.160 | 0.993 | 73.437 | 0.995 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21067) rss_mb | MB | 15 | 367.628 | 186.887 | 395.672 | 394.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21067) main thread run-queue wait | percent | 14 | 2.174 | 0.007 | 16.795 | 0.016 | 0.306298 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21067) vms_mb | MB | 15 | 9063.189 | 1593.969 | 10208.941 | 10207.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21088) CPU | percent | 1 | 57.582 | 57.582 | 57.582 | 57.582 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21088) rss_mb | MB | 2 | 264.201 | 228.461 | 299.941 | 299.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21088) main thread run-queue wait | percent | 1 | 24.492 | 24.492 | 24.492 | 24.492 | 0.246700 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21088) vms_mb | MB | 2 | 1678.119 | 1631.719 | 1724.520 | 1724.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21120) CPU | percent | 13 | 19.099 | 1.971 | 86.370 | 7.950 | 2.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21120) rss_mb | MB | 14 | 371.952 | 273.152 | 389.578 | 389.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21120) main thread run-queue wait | percent | 13 | 2.101 | 0.008 | 23.561 | 0.091 | 0.275107 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21120) vms_mb | MB | 14 | 9004.222 | 1668.520 | 10212.734 | 10212.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21158) CPU | percent | 18 | 12.587 | 0.994 | 74.494 | 2.983 | 2.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21158) rss_mb | MB | 19 | 375.549 | 221.145 | 394.176 | 393.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21158) main thread run-queue wait | percent | 18 | 0.325 | 0.004 | 2.500 | 0.011 | 0.058930 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21158) vms_mb | MB | 19 | 9302.791 | 1624.039 | 10201.934 | 10201.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21197) CPU | percent | 11 | 17.347 | 0.995 | 69.624 | 1.989 | 1.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21197) rss_mb | MB | 12 | 367.003 | 295.465 | 381.551 | 381.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21197) main thread run-queue wait | percent | 11 | 0.977 | 0.004 | 9.935 | 0.011 | 0.108174 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21197) vms_mb | MB | 12 | 9483.603 | 1689.859 | 10203.340 | 10203.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21232) CPU | percent | 14 | 13.690 | 0.995 | 75.456 | 6.952 | 1.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21232) rss_mb | MB | 15 | 373.790 | 259.508 | 392.301 | 392.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21232) main thread run-queue wait | percent | 14 | 0.273 | 0.007 | 1.567 | 0.013 | 0.038453 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21232) vms_mb | MB | 15 | 9062.927 | 1655.770 | 10186.246 | 10186.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21268) CPU | percent | 14 | 15.528 | 0.995 | 73.545 | 7.958 | 2.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21268) rss_mb | MB | 15 | 370.668 | 229.273 | 392.184 | 392.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21268) main thread run-queue wait | percent | 14 | 0.284 | 0.004 | 1.346 | 0.265 | 0.040057 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21268) vms_mb | MB | 15 | 9062.840 | 1631.801 | 10200.125 | 10200.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21287) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21287) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21288) rss_mb | MB | 1 | 9.797 | 9.797 | 9.797 | 9.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21288) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21304) CPU | percent | 11 | 21.498 | 0.994 | 73.590 | 2.983 | 2.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21304) rss_mb | MB | 12 | 360.139 | 229.309 | 384.055 | 384.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21304) main thread run-queue wait | percent | 11 | 1.285 | 0.002 | 8.556 | 0.022 | 0.144940 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21304) vms_mb | MB | 12 | 8783.548 | 1631.793 | 10206.949 | 10206.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21323) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21323) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21324) rss_mb | MB | 1 | 9.176 | 9.176 | 9.176 | 9.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21324) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21339) CPU | percent | 30 | 9.688 | 0.994 | 79.228 | 5.966 | 2.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21339) rss_mb | MB | 31 | 383.296 | 160.031 | 401.926 | 401.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21339) main thread run-queue wait | percent | 30 | 0.235 | 0.004 | 2.801 | 0.014 | 0.071615 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21339) vms_mb | MB | 31 | 9641.242 | 1315.715 | 10205.805 | 10205.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21372) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21372) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21373) rss_mb | MB | 1 | 11.727 | 11.727 | 11.727 | 11.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21373) vms_mb | MB | 1 | 19.910 | 19.910 | 19.910 | 19.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21375) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21375) rss_mb | MB | 3 | 2.879 | 2.879 | 2.879 | 2.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21375) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21375) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21376) CPU | percent | 2 | 9.920 | 0.000 | 19.840 | 0.000 | 0.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21376) rss_mb | MB | 3 | 60.747 | 50.062 | 66.090 | 66.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21376) main thread run-queue wait | percent | 2 | 0.086 | 0.000 | 0.173 | 0.000 | 0.001740 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21376) vms_mb | MB | 3 | 73.031 | 58.875 | 80.109 | 80.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21385) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21385) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21386) rss_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21386) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21390) CPU | percent | 19 | 13.745 | 0.994 | 77.594 | 0.995 | 2.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21390) rss_mb | MB | 20 | 375.406 | 221.418 | 392.875 | 391.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21390) main thread run-queue wait | percent | 19 | 0.870 | 0.002 | 6.030 | 0.012 | 0.170138 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21390) vms_mb | MB | 20 | 9355.750 | 1624.523 | 10211.914 | 10210.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21409) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21409) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21410) rss_mb | MB | 1 | 9.973 | 9.973 | 9.973 | 9.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21410) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21523) CPU | percent | 29 | 11.135 | 0.994 | 84.454 | 1.989 | 3.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21523) rss_mb | MB | 30 | 375.580 | 152.910 | 392.699 | 392.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21523) main thread run-queue wait | percent | 29 | 0.803 | 0.003 | 13.722 | 0.007 | 0.234644 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21523) vms_mb | MB | 30 | 9624.701 | 1308.969 | 10206.230 | 10206.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21546) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21546) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21547) rss_mb | MB | 1 | 10.566 | 10.566 | 10.566 | 10.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21547) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21553) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21553) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21554) rss_mb | MB | 1 | 14.707 | 14.707 | 14.707 | 14.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21554) vms_mb | MB | 1 | 20.082 | 20.082 | 20.082 | 20.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21572) CPU | percent | 16 | 13.659 | 0.994 | 73.460 | 6.964 | 2.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21572) rss_mb | MB | 17 | 381.107 | 282.078 | 395.637 | 395.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21572) main thread run-queue wait | percent | 16 | 0.951 | 0.004 | 13.072 | 0.028 | 0.155514 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21572) vms_mb | MB | 17 | 9698.619 | 1677.012 | 10209.758 | 10209.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21607) CPU | percent | 12 | 19.720 | 0.995 | 75.615 | 7.956 | 2.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21607) rss_mb | MB | 13 | 368.417 | 236.375 | 391.324 | 391.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21607) main thread run-queue wait | percent | 12 | 1.060 | 0.007 | 11.429 | 0.031 | 0.127937 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21607) vms_mb | MB | 13 | 8899.288 | 1636.543 | 10205.898 | 10205.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21643) CPU | percent | 12 | 21.279 | 1.988 | 77.436 | 7.958 | 2.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21643) rss_mb | MB | 13 | 361.591 | 214.535 | 385.164 | 385.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21643) main thread run-queue wait | percent | 12 | 1.026 | 0.009 | 7.661 | 0.039 | 0.123843 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21643) vms_mb | MB | 13 | 8892.827 | 1622.793 | 10207.867 | 10207.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21662) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21662) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21663) rss_mb | MB | 1 | 9.922 | 9.922 | 9.922 | 9.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21663) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21668) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21668) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21669) rss_mb | MB | 1 | 5.547 | 5.547 | 5.547 | 5.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21669) vms_mb | MB | 1 | 11.645 | 11.645 | 11.645 | 11.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21678) CPU | percent | 11 | 24.330 | 1.927 | 76.422 | 1.988 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21678) rss_mb | MB | 12 | 354.096 | 168.723 | 386.973 | 386.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21678) main thread run-queue wait | percent | 11 | 1.254 | 0.005 | 8.111 | 0.025 | 0.139106 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21678) vms_mb | MB | 12 | 8778.891 | 1578.469 | 10210.672 | 10210.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21704) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21704) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21705) rss_mb | MB | 1 | 8.945 | 8.945 | 8.945 | 8.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21705) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21717) CPU | percent | 13 | 17.617 | 0.994 | 75.565 | 1.990 | 2.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21717) rss_mb | MB | 14 | 368.876 | 252.645 | 390.262 | 389.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21717) main thread run-queue wait | percent | 13 | 1.434 | 0.003 | 15.098 | 0.012 | 0.188442 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21717) vms_mb | MB | 14 | 8995.515 | 1648.562 | 10209.926 | 10209.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21742) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21742) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21743) rss_mb | MB | 1 | 9.914 | 9.914 | 9.914 | 9.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21743) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21755) CPU | percent | 18 | 11.972 | 0.993 | 72.478 | 1.990 | 2.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21755) rss_mb | MB | 19 | 376.872 | 294.559 | 389.484 | 388.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21755) main thread run-queue wait | percent | 18 | 0.660 | 0.004 | 10.175 | 0.014 | 0.119536 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21755) vms_mb | MB | 19 | 9753.282 | 1689.234 | 10211.797 | 10210.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21794) CPU | percent | 12 | 22.587 | 0.994 | 81.364 | 1.986 | 2.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21794) rss_mb | MB | 13 | 353.111 | 161.465 | 382.078 | 382.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21794) main thread run-queue wait | percent | 12 | 1.105 | 0.006 | 5.715 | 0.007 | 0.133670 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21794) vms_mb | MB | 13 | 8879.614 | 1500.215 | 10203.809 | 10203.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21818) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21818) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21819) rss_mb | MB | 1 | 10.047 | 10.047 | 10.047 | 10.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21819) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21830) CPU | percent | 161 | 4.578 | 0.985 | 77.527 | 2.985 | 7.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21830) rss_mb | MB | 162 | 384.053 | 294.125 | 398.742 | 386.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21830) main thread run-queue wait | percent | 161 | 0.291 | 0.002 | 14.995 | 0.011 | 0.471739 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21830) vms_mb | MB | 162 | 10133.337 | 1689.227 | 10216.277 | 10161.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21868) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21868) rss_mb | MB | 4 | 1.881 | 0.000 | 2.508 | 2.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21868) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21868) vms_mb | MB | 4 | 2.918 | 0.129 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21869) CPU | percent | 2 | 7.440 | 0.000 | 14.880 | 0.000 | 0.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21869) rss_mb | MB | 3 | 61.609 | 52.094 | 66.367 | 66.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21869) main thread run-queue wait | percent | 2 | 0.051 | 0.000 | 0.102 | 0.000 | 0.001030 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21869) vms_mb | MB | 3 | 73.708 | 60.906 | 80.109 | 80.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21908) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21908) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21909) rss_mb | MB | 1 | 20.754 | 20.754 | 20.754 | 20.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21909) vms_mb | MB | 1 | 25.836 | 25.836 | 25.836 | 25.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21915) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21915) rss_mb | MB | 3 | 2.586 | 2.586 | 2.586 | 2.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21915) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21915) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21916) CPU | percent | 2 | 32.354 | 0.000 | 64.708 | 0.000 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21916) rss_mb | MB | 3 | 51.009 | 21.496 | 65.766 | 65.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21916) main thread run-queue wait | percent | 2 | 0.107 | 0.000 | 0.214 | 0.000 | 0.002179 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21916) vms_mb | MB | 3 | 62.440 | 27.117 | 80.102 | 80.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21917) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21917) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21918) rss_mb | MB | 1 | 15.398 | 15.398 | 15.398 | 15.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21918) vms_mb | MB | 1 | 20.602 | 20.602 | 20.602 | 20.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21926) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21926) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21927) rss_mb | MB | 1 | 9.293 | 9.293 | 9.293 | 9.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21927) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21934) rss_mb | MB | 1 | 2.738 | 2.738 | 2.738 | 2.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21934) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21935) rss_mb | MB | 1 | 10.414 | 10.414 | 10.414 | 10.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21935) vms_mb | MB | 1 | 13.867 | 13.867 | 13.867 | 13.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21949) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21949) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21951) rss_mb | MB | 1 | 2.648 | 2.648 | 2.648 | 2.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21951) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21952) rss_mb | MB | 1 | 49.703 | 49.703 | 49.703 | 49.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21952) vms_mb | MB | 1 | 57.672 | 57.672 | 57.672 | 57.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21958) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21958) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21959) rss_mb | MB | 1 | 16.883 | 16.883 | 16.883 | 16.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21959) vms_mb | MB | 1 | 22.141 | 22.141 | 22.141 | 22.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21960) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21960) rss_mb | MB | 2 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21960) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21960) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21961) CPU | percent | 1 | 30.753 | 30.753 | 30.753 | 30.753 | 0.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21961) rss_mb | MB | 2 | 57.324 | 46.949 | 67.699 | 67.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21961) main thread run-queue wait | percent | 1 | 1.983 | 1.983 | 1.983 | 1.983 | 0.019990 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21961) vms_mb | MB | 2 | 68.713 | 54.941 | 82.484 | 82.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21979) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21979) rss_mb | MB | 4 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21979) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21979) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21980) CPU | percent | 3 | 25.137 | 0.988 | 71.458 | 2.964 | 0.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21980) rss_mb | MB | 4 | 55.492 | 23.137 | 66.777 | 66.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21980) main thread run-queue wait | percent | 3 | 0.190 | 0.084 | 0.319 | 0.319 | 0.005757 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21980) vms_mb | MB | 4 | 67.711 | 29.055 | 81.820 | 81.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21983) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21983) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21984) rss_mb | MB | 1 | 14.680 | 14.680 | 14.680 | 14.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21984) vms_mb | MB | 1 | 20.082 | 20.082 | 20.082 | 20.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21997) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21997) rss_mb | MB | 2 | 2.867 | 2.867 | 2.867 | 2.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21997) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 21997) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21998) CPU | percent | 1 | 68.434 | 68.434 | 68.434 | 68.434 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21998) rss_mb | MB | 2 | 36.428 | 10.059 | 62.797 | 62.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21998) main thread run-queue wait | percent | 1 | 0.069 | 0.069 | 0.069 | 0.069 | 0.000694 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 21998) vms_mb | MB | 2 | 46.010 | 14.512 | 77.508 | 77.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22000) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22000) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22001) rss_mb | MB | 1 | 20.691 | 20.691 | 20.691 | 20.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22001) vms_mb | MB | 1 | 25.832 | 25.832 | 25.832 | 25.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22005) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22005) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22006) rss_mb | MB | 1 | 15.051 | 15.051 | 15.051 | 15.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22006) vms_mb | MB | 1 | 20.398 | 20.398 | 20.398 | 20.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22032) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22032) rss_mb | MB | 3 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22032) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22032) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22033) CPU | percent | 2 | 30.737 | 3.939 | 57.534 | 3.939 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22033) rss_mb | MB | 3 | 56.221 | 35.312 | 67.113 | 67.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22033) main thread run-queue wait | percent | 2 | 0.352 | 0.116 | 0.587 | 0.587 | 0.007137 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22033) vms_mb | MB | 3 | 68.630 | 43.965 | 81.812 | 81.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22048) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22048) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22049) rss_mb | MB | 1 | 21.316 | 21.316 | 21.316 | 21.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22049) vms_mb | MB | 1 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22058) CPU | percent | 25 | 13.995 | 0.993 | 89.458 | 0.993 | 3.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22058) rss_mb | MB | 26 | 370.328 | 71.359 | 392.387 | 392.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22058) main thread run-queue wait | percent | 25 | 1.022 | 0.003 | 14.728 | 0.003 | 0.257262 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22058) vms_mb | MB | 26 | 9534.896 | 1283.598 | 10211.734 | 10211.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22079) rss_mb | MB | 1 | 207.938 | 207.938 | 207.938 | 207.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22079) vms_mb | MB | 1 | 1619.484 | 1619.484 | 1619.484 | 1619.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22103) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22103) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22104) rss_mb | MB | 1 | 44.113 | 44.113 | 44.113 | 44.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22104) vms_mb | MB | 1 | 52.984 | 52.984 | 52.984 | 52.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22116) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22116) rss_mb | MB | 3 | 2.645 | 2.645 | 2.645 | 2.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22116) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22116) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22117) CPU | percent | 2 | 15.895 | 3.958 | 27.831 | 3.958 | 0.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22117) rss_mb | MB | 3 | 59.741 | 46.887 | 66.605 | 66.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22117) main thread run-queue wait | percent | 2 | 0.423 | 0.304 | 0.542 | 0.542 | 0.008540 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22117) vms_mb | MB | 3 | 72.315 | 54.957 | 81.844 | 81.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22128) CPU | percent | 36 | 10.453 | 0.000 | 88.294 | 1.989 | 3.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22128) rss_mb | MB | 37 | 375.248 | 153.945 | 388.871 | 388.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22128) main thread run-queue wait | percent | 36 | 0.661 | 0.004 | 9.165 | 0.004 | 0.239551 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22128) vms_mb | MB | 37 | 9744.675 | 1499.215 | 10213.992 | 10213.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22151) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22151) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22152) rss_mb | MB | 1 | 6.992 | 6.992 | 6.992 | 6.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22152) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22160) rss_mb | MB | 1 | 166.582 | 166.582 | 166.582 | 166.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22160) vms_mb | MB | 1 | 1577.973 | 1577.973 | 1577.973 | 1577.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22249) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22249) rss_mb | MB | 11 | 2.844 | 2.844 | 2.844 | 2.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22249) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22249) vms_mb | MB | 11 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22250) CPU | percent | 10 | 3.972 | 0.000 | 39.720 | 0.000 | 0.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22250) rss_mb | MB | 11 | 63.469 | 40.977 | 65.719 | 65.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22250) main thread run-queue wait | percent | 10 | 0.038 | 0.000 | 0.381 | 0.000 | 0.003839 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22250) vms_mb | MB | 11 | 77.405 | 49.578 | 80.188 | 80.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22257) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22257) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22258) rss_mb | MB | 1 | 7.270 | 7.270 | 7.270 | 7.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22258) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22264) rss_mb | MB | 1 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22264) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22265) rss_mb | MB | 1 | 37.805 | 37.805 | 37.805 | 37.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22265) vms_mb | MB | 1 | 46.059 | 46.059 | 46.059 | 46.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22275) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22275) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22290) CPU | percent | 8 | 27.501 | 1.989 | 72.535 | 1.989 | 2.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22290) rss_mb | MB | 9 | 360.964 | 271.090 | 388.258 | 388.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22290) main thread run-queue wait | percent | 8 | 4.683 | 0.010 | 16.697 | 0.012 | 0.382296 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22290) vms_mb | MB | 9 | 9237.990 | 1666.262 | 10210.945 | 10210.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22310) CPU | percent | 1 | 57.293 | 57.293 | 57.293 | 57.293 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22310) rss_mb | MB | 2 | 205.057 | 155.473 | 254.641 | 254.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22310) main thread run-queue wait | percent | 1 | 17.458 | 17.458 | 17.458 | 17.458 | 0.176729 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22310) vms_mb | MB | 2 | 1480.875 | 1311.371 | 1650.379 | 1650.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22323) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22323) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22324) rss_mb | MB | 1 | 8.234 | 8.234 | 8.234 | 8.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22324) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22339) CPU | percent | 18 | 17.759 | 1.988 | 86.488 | 1.989 | 3.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22339) rss_mb | MB | 19 | 367.377 | 128.020 | 393.277 | 393.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22339) main thread run-queue wait | percent | 18 | 1.738 | 0.006 | 14.644 | 0.009 | 0.315413 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22339) vms_mb | MB | 19 | 9286.981 | 1296.254 | 10211.734 | 10211.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22358) CPU | percent | 1 | 52.596 | 52.596 | 52.596 | 52.596 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22358) rss_mb | MB | 2 | 217.555 | 174.676 | 260.434 | 260.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22358) main thread run-queue wait | percent | 1 | 12.348 | 12.348 | 12.348 | 12.348 | 0.124424 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22358) vms_mb | MB | 2 | 1622.639 | 1589.973 | 1655.305 | 1655.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22385) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22385) rss_mb | MB | 3 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22385) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22385) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22386) CPU | percent | 2 | 33.708 | 0.000 | 67.417 | 0.000 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22386) rss_mb | MB | 3 | 52.431 | 23.934 | 66.742 | 66.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22386) main thread run-queue wait | percent | 2 | 0.130 | 0.005 | 0.254 | 0.005 | 0.002615 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22386) vms_mb | MB | 3 | 63.786 | 29.227 | 81.195 | 81.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22397) CPU | percent | 13 | 18.106 | 1.986 | 75.458 | 1.989 | 2.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22397) rss_mb | MB | 14 | 375.320 | 293.930 | 391.070 | 391.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22397) main thread run-queue wait | percent | 13 | 2.136 | 0.009 | 17.117 | 0.012 | 0.279570 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22397) vms_mb | MB | 14 | 9590.825 | 1689.000 | 10211.832 | 10211.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22422) CPU | percent | 1 | 79.522 | 79.522 | 79.522 | 79.522 | 0.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22422) rss_mb | MB | 2 | 235.650 | 168.133 | 303.168 | 303.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22422) main thread run-queue wait | percent | 1 | 8.874 | 8.874 | 8.874 | 8.874 | 0.089268 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22422) vms_mb | MB | 2 | 1653.029 | 1578.473 | 1727.586 | 1727.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22441) rss_mb | MB | 1 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22441) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22442) rss_mb | MB | 1 | 51.441 | 51.441 | 51.441 | 51.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22442) vms_mb | MB | 1 | 248.070 | 248.070 | 248.070 | 248.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22456) CPU | percent | 28 | 11.517 | 0.994 | 73.487 | 3.979 | 3.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22456) rss_mb | MB | 29 | 381.457 | 259.625 | 400.871 | 400.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22456) main thread run-queue wait | percent | 28 | 1.353 | 0.005 | 15.231 | 0.007 | 0.382494 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22456) vms_mb | MB | 29 | 9910.251 | 1655.766 | 10214.781 | 10214.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22477) CPU | percent | 1 | 52.560 | 52.560 | 52.560 | 52.560 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22477) rss_mb | MB | 2 | 196.186 | 156.887 | 235.484 | 235.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22477) main thread run-queue wait | percent | 1 | 10.232 | 10.232 | 10.232 | 10.232 | 0.103176 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22477) vms_mb | MB | 2 | 1475.121 | 1313.883 | 1636.359 | 1636.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22489) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22489) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22490) rss_mb | MB | 1 | 7.797 | 7.797 | 7.797 | 7.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22490) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22502) rss_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22502) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22503) rss_mb | MB | 1 | 43.223 | 43.223 | 43.223 | 43.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22503) vms_mb | MB | 1 | 51.438 | 51.438 | 51.438 | 51.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22510) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22510) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22511) rss_mb | MB | 1 | 14.922 | 14.922 | 14.922 | 14.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22511) vms_mb | MB | 1 | 20.242 | 20.242 | 20.242 | 20.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22524) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22524) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22525) rss_mb | MB | 1 | 20.531 | 20.531 | 20.531 | 20.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22525) vms_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22538) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22538) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22539) rss_mb | MB | 1 | 9.844 | 9.844 | 9.844 | 9.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22539) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22543) CPU | percent | 17 | 16.063 | 0.993 | 70.509 | 2.984 | 2.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22543) rss_mb | MB | 18 | 374.221 | 206.414 | 395.895 | 395.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22543) main thread run-queue wait | percent | 17 | 1.043 | 0.003 | 5.884 | 0.025 | 0.178536 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22543) vms_mb | MB | 18 | 9226.368 | 1619.305 | 10191.117 | 10170.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22572) rss_mb | MB | 1 | 197.586 | 197.586 | 197.586 | 197.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22572) vms_mb | MB | 1 | 1616.949 | 1616.949 | 1616.949 | 1616.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22588) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22588) rss_mb | MB | 2 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22588) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22588) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22589) CPU | percent | 1 | 66.454 | 66.454 | 66.454 | 66.454 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22589) rss_mb | MB | 2 | 45.195 | 24.566 | 65.824 | 65.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22589) main thread run-queue wait | percent | 1 | 0.195 | 0.195 | 0.195 | 0.195 | 0.001968 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22589) vms_mb | MB | 2 | 55.623 | 31.406 | 79.840 | 79.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22602) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22602) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22603) rss_mb | MB | 1 | 10.059 | 10.059 | 10.059 | 10.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 22603) vms_mb | MB | 1 | 13.844 | 13.844 | 13.844 | 13.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22612) CPU | percent | 6 | 39.911 | 4.970 | 78.458 | 6.954 | 2.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22612) rss_mb | MB | 7 | 339.152 | 166.270 | 389.812 | 389.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22612) main thread run-queue wait | percent | 6 | 1.773 | 0.153 | 5.720 | 0.703 | 0.107124 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22612) vms_mb | MB | 7 | 7749.610 | 1573.469 | 10209.270 | 10178.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22633) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22633) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22634) rss_mb | MB | 1 | 9.621 | 9.621 | 9.621 | 9.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22634) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22640) rss_mb | MB | 1 | 229.195 | 229.195 | 229.195 | 229.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22640) vms_mb | MB | 1 | 1631.988 | 1631.988 | 1631.988 | 1631.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22659) CPU | percent | 6 | 39.897 | 5.966 | 76.426 | 5.966 | 2.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22659) rss_mb | MB | 7 | 334.515 | 171.059 | 380.086 | 380.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22659) main thread run-queue wait | percent | 6 | 5.306 | 0.027 | 14.358 | 0.027 | 0.320700 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22659) vms_mb | MB | 7 | 7740.097 | 1579.219 | 10177.070 | 10177.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22676) CPU | percent | 1 | 47.626 | 47.626 | 47.626 | 47.626 | 0.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22676) rss_mb | MB | 2 | 266.270 | 229.340 | 303.199 | 303.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22676) main thread run-queue wait | percent | 1 | 16.104 | 16.104 | 16.104 | 16.104 | 0.162302 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22676) vms_mb | MB | 2 | 1681.107 | 1635.328 | 1726.887 | 1726.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22694) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22694) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22695) rss_mb | MB | 1 | 9.105 | 9.105 | 9.105 | 9.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22695) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22707) CPU | percent | 39 | 9.062 | 0.987 | 85.342 | 2.983 | 3.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22707) rss_mb | MB | 40 | 389.336 | 160.145 | 405.348 | 405.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22707) main thread run-queue wait | percent | 39 | 0.876 | 0.004 | 13.292 | 0.023 | 0.344141 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22707) vms_mb | MB | 40 | 9762.248 | 1315.715 | 10200.973 | 10200.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22726) CPU | percent | 1 | 52.601 | 52.601 | 52.601 | 52.601 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22726) rss_mb | MB | 2 | 222.963 | 184.676 | 261.250 | 261.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22726) main thread run-queue wait | percent | 1 | 13.952 | 13.952 | 13.952 | 13.952 | 0.140580 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22726) vms_mb | MB | 2 | 1624.879 | 1593.473 | 1656.285 | 1656.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22738) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22738) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22739) rss_mb | MB | 1 | 9.973 | 9.973 | 9.973 | 9.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22739) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22752) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22752) rss_mb | MB | 16 | 2.945 | 2.945 | 2.945 | 2.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22752) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22752) vms_mb | MB | 16 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22753) CPU | percent | 15 | 4.099 | 0.000 | 47.586 | 9.931 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22753) rss_mb | MB | 16 | 65.150 | 39.145 | 67.367 | 67.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22753) main thread run-queue wait | percent | 15 | 0.048 | 0.000 | 0.375 | 0.112 | 0.007341 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22753) vms_mb | MB | 16 | 79.514 | 47.855 | 82.086 | 82.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22781) CPU | percent | 6 | 43.536 | 6.952 | 75.527 | 6.952 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22781) rss_mb | MB | 7 | 335.775 | 175.180 | 385.898 | 385.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22781) main thread run-queue wait | percent | 6 | 5.560 | 0.059 | 16.410 | 0.059 | 0.336024 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22781) vms_mb | MB | 7 | 7754.014 | 1589.969 | 10203.703 | 10203.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22801) CPU | percent | 1 | 50.631 | 50.631 | 50.631 | 50.631 | 0.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22801) rss_mb | MB | 2 | 227.867 | 191.367 | 264.367 | 264.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22801) main thread run-queue wait | percent | 1 | 13.751 | 13.751 | 13.751 | 13.751 | 0.138513 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22801) vms_mb | MB | 2 | 1628.520 | 1596.473 | 1660.566 | 1660.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22811) rss_mb | MB | 1 | 1.395 | 1.395 | 1.395 | 1.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22811) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22812) rss_mb | MB | 1 | 7.512 | 7.512 | 7.512 | 7.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22812) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22822) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22822) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22823) rss_mb | MB | 1 | 4.707 | 4.707 | 4.707 | 4.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22823) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22827) CPU | percent | 6 | 43.200 | 3.974 | 76.359 | 6.962 | 2.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22827) rss_mb | MB | 7 | 332.873 | 175.234 | 383.715 | 383.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22827) main thread run-queue wait | percent | 6 | 3.686 | 0.020 | 15.872 | 0.020 | 0.222856 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22827) vms_mb | MB | 7 | 7761.007 | 1589.969 | 10210.484 | 10210.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22855) rss_mb | MB | 1 | 194.980 | 194.980 | 194.980 | 194.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22855) vms_mb | MB | 1 | 1615.223 | 1615.223 | 1615.223 | 1615.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22874) CPU | percent | 6 | 42.369 | 6.956 | 67.472 | 6.956 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22874) rss_mb | MB | 7 | 336.295 | 186.746 | 385.789 | 385.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22874) main thread run-queue wait | percent | 6 | 4.682 | 0.018 | 13.829 | 0.018 | 0.283087 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22874) vms_mb | MB | 7 | 7757.441 | 1593.469 | 10206.891 | 10206.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22893) CPU | percent | 1 | 56.518 | 56.518 | 56.518 | 56.518 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22893) rss_mb | MB | 2 | 236.539 | 194.117 | 278.961 | 278.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22893) main thread run-queue wait | percent | 1 | 21.959 | 21.959 | 21.959 | 21.959 | 0.221464 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22893) vms_mb | MB | 2 | 1644.014 | 1614.473 | 1673.555 | 1673.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22904) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22904) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22905) rss_mb | MB | 1 | 10.105 | 10.105 | 10.105 | 10.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22905) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22917) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22917) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22918) rss_mb | MB | 1 | 6.707 | 6.707 | 6.707 | 6.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22918) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22922) CPU | percent | 7 | 38.308 | 4.971 | 73.520 | 13.923 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22922) rss_mb | MB | 8 | 343.772 | 181.430 | 388.254 | 388.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22922) main thread run-queue wait | percent | 7 | 5.418 | 0.015 | 24.813 | 0.045 | 0.382469 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22922) vms_mb | MB | 8 | 8060.701 | 1591.469 | 10207.027 | 10207.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22941) CPU | percent | 1 | 57.462 | 57.462 | 57.462 | 57.462 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22941) rss_mb | MB | 2 | 249.836 | 205.277 | 294.395 | 294.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22941) main thread run-queue wait | percent | 1 | 23.647 | 23.647 | 23.647 | 23.647 | 0.238689 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22941) vms_mb | MB | 2 | 1654.133 | 1618.965 | 1689.301 | 1689.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22951) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22951) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22952) rss_mb | MB | 1 | 9.406 | 9.406 | 9.406 | 9.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22952) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22969) CPU | percent | 21 | 15.229 | 0.994 | 66.483 | 2.983 | 3.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22969) rss_mb | MB | 22 | 380.926 | 206.230 | 399.852 | 399.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22969) main thread run-queue wait | percent | 21 | 2.336 | 0.004 | 16.686 | 0.017 | 0.493890 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22969) vms_mb | MB | 22 | 9430.681 | 1619.586 | 10212.316 | 10211.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22986) CPU | percent | 1 | 54.641 | 54.641 | 54.641 | 54.641 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22986) rss_mb | MB | 2 | 195.398 | 154.707 | 236.090 | 236.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22986) main thread run-queue wait | percent | 1 | 19.391 | 19.391 | 19.391 | 19.391 | 0.195184 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22986) vms_mb | MB | 2 | 1473.871 | 1310.621 | 1637.121 | 1637.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 23011) rss_mb | MB | 1 | 2.285 | 2.285 | 2.285 | 2.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 23011) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 23012) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 23012) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23015) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23015) rss_mb | MB | 5 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23015) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23015) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23016) CPU | percent | 4 | 6.450 | 0.000 | 25.800 | 0.000 | 0.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23016) rss_mb | MB | 5 | 62.566 | 46.098 | 66.684 | 66.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23016) main thread run-queue wait | percent | 4 | 0.035 | 0.000 | 0.139 | 0.000 | 0.001399 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23016) vms_mb | MB | 5 | 75.075 | 54.672 | 80.176 | 80.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23035) CPU | percent | 6 | 46.168 | 5.966 | 88.473 | 5.966 | 2.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23035) rss_mb | MB | 7 | 319.924 | 90.504 | 385.145 | 385.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23035) main thread run-queue wait | percent | 6 | 6.152 | 0.015 | 19.132 | 0.015 | 0.371854 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23035) vms_mb | MB | 7 | 7699.773 | 1283.598 | 10204.863 | 10204.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23054) CPU | percent | 1 | 60.585 | 60.585 | 60.585 | 60.585 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23054) rss_mb | MB | 2 | 224.971 | 176.898 | 273.043 | 273.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23054) main thread run-queue wait | percent | 1 | 18.528 | 18.528 | 18.528 | 18.528 | 0.186545 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23054) vms_mb | MB | 2 | 1629.270 | 1590.473 | 1668.066 | 1668.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23082) CPU | percent | 8 | 36.752 | 2.983 | 86.334 | 13.928 | 2.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23082) rss_mb | MB | 9 | 323.224 | 0.000 | 389.246 | 389.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23082) main thread run-queue wait | percent | 8 | 3.671 | 0.009 | 13.103 | 0.031 | 0.295791 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23082) vms_mb | MB | 9 | 8124.068 | 160.145 | 10207.891 | 10207.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23101) CPU | percent | 1 | 49.627 | 49.627 | 49.627 | 49.627 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23101) rss_mb | MB | 2 | 210.088 | 166.742 | 253.434 | 253.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23101) main thread run-queue wait | percent | 1 | 15.359 | 15.359 | 15.359 | 15.359 | 0.154744 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23101) vms_mb | MB | 2 | 1613.273 | 1577.723 | 1648.824 | 1648.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23127) CPU | percent | 10 | 25.338 | 0.994 | 78.585 | 1.988 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23127) rss_mb | MB | 11 | 361.200 | 234.824 | 385.770 | 385.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23127) main thread run-queue wait | percent | 10 | 1.870 | 0.012 | 14.304 | 0.017 | 0.188231 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23127) vms_mb | MB | 11 | 8659.194 | 1635.773 | 10210.859 | 10210.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23144) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23144) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23145) rss_mb | MB | 1 | 9.988 | 9.988 | 9.988 | 9.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23145) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23155) rss_mb | MB | 1 | 276.039 | 276.039 | 276.039 | 276.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23155) vms_mb | MB | 1 | 1671.301 | 1671.301 | 1671.301 | 1671.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23169) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23169) rss_mb | MB | 2 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23169) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23169) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23170) CPU | percent | 1 | 70.559 | 70.559 | 70.559 | 70.559 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23170) rss_mb | MB | 2 | 41.244 | 19.207 | 63.281 | 63.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23170) main thread run-queue wait | percent | 1 | 0.305 | 0.305 | 0.305 | 0.305 | 0.003066 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23170) vms_mb | MB | 2 | 51.438 | 25.371 | 77.504 | 77.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23203) CPU | percent | 6 | 42.953 | 2.984 | 79.519 | 2.984 | 2.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23203) rss_mb | MB | 7 | 330.328 | 167.082 | 378.340 | 378.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23203) main thread run-queue wait | percent | 6 | 5.253 | 0.022 | 10.924 | 0.022 | 0.320145 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23203) vms_mb | MB | 7 | 7747.964 | 1578.219 | 10202.363 | 10202.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23220) rss_mb | MB | 1 | 228.484 | 228.484 | 228.484 | 228.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23220) vms_mb | MB | 1 | 1631.617 | 1631.617 | 1631.617 | 1631.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23248) CPU | percent | 6 | 33.828 | 6.958 | 69.616 | 8.950 | 2.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23248) rss_mb | MB | 7 | 358.977 | 289.871 | 384.449 | 384.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23248) main thread run-queue wait | percent | 6 | 6.061 | 0.014 | 18.310 | 0.026 | 0.369187 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23248) vms_mb | MB | 7 | 8965.090 | 1684.734 | 10203.473 | 10203.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23268) CPU | percent | 1 | 58.903 | 58.903 | 58.903 | 58.903 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23268) rss_mb | MB | 2 | 213.377 | 166.809 | 259.945 | 259.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23268) main thread run-queue wait | percent | 1 | 13.020 | 13.020 | 13.020 | 13.020 | 0.132629 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23268) vms_mb | MB | 2 | 1616.914 | 1577.973 | 1655.855 | 1655.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23280) rss_mb | MB | 1 | 1.293 | 1.293 | 1.293 | 1.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23280) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23281) rss_mb | MB | 1 | 10.406 | 10.406 | 10.406 | 10.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23281) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23296) CPU | percent | 16 | 17.617 | 0.995 | 78.457 | 0.995 | 2.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23296) rss_mb | MB | 17 | 375.946 | 221.586 | 397.336 | 396.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23296) main thread run-queue wait | percent | 16 | 1.731 | 0.006 | 12.405 | 0.026 | 0.285199 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23296) vms_mb | MB | 17 | 9200.704 | 1624.270 | 10209.188 | 10208.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23317) CPU | percent | 1 | 60.778 | 60.778 | 60.778 | 60.778 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23317) rss_mb | MB | 2 | 237.217 | 180.594 | 293.840 | 293.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23317) main thread run-queue wait | percent | 1 | 18.480 | 18.480 | 18.480 | 18.480 | 0.194601 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23317) vms_mb | MB | 2 | 1640.270 | 1591.473 | 1689.066 | 1689.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23342) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23342) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 23343) rss_mb | MB | 1 | 9.609 | 9.609 | 9.609 | 9.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 23343) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23349) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23349) rss_mb | MB | 2 | 2.668 | 2.668 | 2.668 | 2.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23349) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23349) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23350) CPU | percent | 1 | 69.555 | 69.555 | 69.555 | 69.555 | 0.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23350) rss_mb | MB | 2 | 39.750 | 17.738 | 61.762 | 61.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23350) main thread run-queue wait | percent | 1 | 0.058 | 0.058 | 0.058 | 0.058 | 0.000586 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23350) vms_mb | MB | 2 | 49.826 | 23.734 | 75.918 | 75.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23361) CPU | percent | 6 | 43.534 | 2.977 | 86.360 | 3.974 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23361) rss_mb | MB | 7 | 328.929 | 155.773 | 378.480 | 378.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23361) main thread run-queue wait | percent | 6 | 3.394 | 0.018 | 12.603 | 0.018 | 0.204925 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23361) vms_mb | MB | 7 | 7735.898 | 1499.465 | 10205.207 | 10205.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23391) rss_mb | MB | 1 | 186.375 | 186.375 | 186.375 | 186.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23391) vms_mb | MB | 1 | 1593.723 | 1593.723 | 1593.723 | 1593.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23410) CPU | percent | 6 | 32.119 | 3.968 | 71.474 | 3.968 | 1.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23410) rss_mb | MB | 7 | 362.055 | 296.789 | 388.902 | 388.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23410) main thread run-queue wait | percent | 6 | 4.339 | 0.015 | 15.996 | 0.015 | 0.262043 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23410) vms_mb | MB | 7 | 8968.681 | 1691.641 | 10203.363 | 10202.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23431) rss_mb | MB | 1 | 206.957 | 206.957 | 206.957 | 206.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23431) vms_mb | MB | 1 | 1618.988 | 1618.988 | 1618.988 | 1618.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23450) rss_mb | MB | 1 | 59.395 | 59.395 | 59.395 | 59.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23450) vms_mb | MB | 1 | 899.762 | 899.762 | 899.762 | 899.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23457) CPU | percent | 14 | 22.843 | 0.994 | 87.372 | 1.989 | 3.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23457) rss_mb | MB | 15 | 356.778 | 63.664 | 395.367 | 395.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23457) main thread run-queue wait | percent | 14 | 3.659 | 0.005 | 18.336 | 0.006 | 0.515987 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23457) vms_mb | MB | 15 | 9031.167 | 1238.512 | 10208.727 | 10208.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23476) CPU | percent | 1 | 53.578 | 53.578 | 53.578 | 53.578 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23476) rss_mb | MB | 2 | 215.518 | 171.559 | 259.477 | 259.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23476) main thread run-queue wait | percent | 1 | 14.303 | 14.303 | 14.303 | 14.303 | 0.144159 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23476) vms_mb | MB | 2 | 1617.525 | 1579.723 | 1655.328 | 1655.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23501) rss_mb | MB | 1 | 2.789 | 2.789 | 2.789 | 2.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23501) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23505) rss_mb | MB | 1 | 8.184 | 8.184 | 8.184 | 8.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23505) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23520) CPU | percent | 6 | 32.279 | 1.989 | 76.520 | 1.989 | 1.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23520) rss_mb | MB | 7 | 359.138 | 294.547 | 381.984 | 381.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23520) main thread run-queue wait | percent | 6 | 2.448 | 0.017 | 10.403 | 0.017 | 0.147887 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23520) vms_mb | MB | 7 | 8969.408 | 1689.508 | 10204.766 | 10204.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23549) rss_mb | MB | 1 | 174.668 | 174.668 | 174.668 | 174.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23549) vms_mb | MB | 1 | 1582.223 | 1582.223 | 1582.223 | 1582.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23566) CPU | percent | 6 | 44.539 | 4.974 | 77.545 | 9.947 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23566) rss_mb | MB | 7 | 339.586 | 175.109 | 390.988 | 390.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23566) main thread run-queue wait | percent | 6 | 2.468 | 0.014 | 5.849 | 3.865 | 0.149039 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23566) vms_mb | MB | 7 | 7759.905 | 1589.969 | 10211.512 | 10211.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23587) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23587) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23588) rss_mb | MB | 1 | 7.262 | 7.262 | 7.262 | 7.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23588) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23594) rss_mb | MB | 1 | 260.492 | 260.492 | 260.492 | 260.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23594) vms_mb | MB | 1 | 1656.059 | 1656.059 | 1656.059 | 1656.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23602) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23602) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23603) rss_mb | MB | 1 | 8.531 | 8.531 | 8.531 | 8.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23603) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23610) CPU | percent | 7 | 38.874 | 3.978 | 76.488 | 12.933 | 2.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23610) rss_mb | MB | 8 | 342.468 | 174.762 | 392.027 | 392.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23610) main thread run-queue wait | percent | 7 | 6.070 | 0.014 | 15.564 | 0.043 | 0.428037 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23610) vms_mb | MB | 8 | 8058.574 | 1581.969 | 10210.312 | 10210.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23629) CPU | percent | 1 | 59.547 | 59.547 | 59.547 | 59.547 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23629) rss_mb | MB | 2 | 226.773 | 185.648 | 267.898 | 267.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23629) main thread run-queue wait | percent | 1 | 16.817 | 16.817 | 16.817 | 16.817 | 0.169453 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23629) vms_mb | MB | 2 | 1628.650 | 1593.473 | 1663.828 | 1663.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23657) CPU | percent | 17 | 17.697 | 0.994 | 71.448 | 0.994 | 3.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23657) rss_mb | MB | 18 | 373.996 | 188.918 | 396.031 | 395.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23657) main thread run-queue wait | percent | 17 | 2.427 | 0.003 | 27.457 | 0.005 | 0.415874 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23657) vms_mb | MB | 18 | 9259.904 | 1594.469 | 10215.406 | 10214.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23676) CPU | percent | 1 | 59.559 | 59.559 | 59.559 | 59.559 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23676) rss_mb | MB | 2 | 242.836 | 198.648 | 287.023 | 287.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23676) main thread run-queue wait | percent | 1 | 23.705 | 23.705 | 23.705 | 23.705 | 0.238800 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23676) vms_mb | MB | 2 | 1649.773 | 1617.480 | 1682.066 | 1682.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23699) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23699) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 23700) rss_mb | MB | 1 | 10.430 | 10.430 | 10.430 | 10.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 23700) vms_mb | MB | 1 | 14.059 | 14.059 | 14.059 | 14.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23701) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23701) rss_mb | MB | 2 | 2.766 | 2.766 | 2.766 | 2.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23701) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23701) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23702) CPU | percent | 1 | 23.818 | 23.818 | 23.818 | 23.818 | 0.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23702) rss_mb | MB | 2 | 57.309 | 48.465 | 66.152 | 66.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23702) main thread run-queue wait | percent | 1 | 0.230 | 0.230 | 0.230 | 0.230 | 0.002321 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23702) vms_mb | MB | 2 | 68.721 | 57.336 | 80.105 | 80.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23714) CPU | percent | 11 | 25.662 | 1.990 | 83.491 | 2.984 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23714) rss_mb | MB | 12 | 355.926 | 158.531 | 394.820 | 394.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23714) main thread run-queue wait | percent | 11 | 2.096 | 0.011 | 14.656 | 0.011 | 0.232175 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23714) vms_mb | MB | 12 | 8761.955 | 1500.465 | 10207.020 | 10207.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23743) rss_mb | MB | 1 | 180.312 | 180.312 | 180.312 | 180.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23743) vms_mb | MB | 1 | 1591.473 | 1591.473 | 1591.473 | 1591.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23762) CPU | percent | 5 | 41.730 | 2.979 | 76.591 | 2.979 | 2.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23762) rss_mb | MB | 6 | 349.540 | 262.219 | 383.676 | 383.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23762) main thread run-queue wait | percent | 5 | 3.563 | 0.026 | 13.515 | 0.026 | 0.179559 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23762) vms_mb | MB | 6 | 8755.029 | 1657.262 | 10207.582 | 10207.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23783) CPU | percent | 1 | 67.431 | 67.431 | 67.431 | 67.431 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23783) rss_mb | MB | 2 | 247.100 | 194.594 | 299.605 | 299.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23783) main thread run-queue wait | percent | 1 | 15.733 | 15.733 | 15.733 | 15.733 | 0.158659 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23783) vms_mb | MB | 2 | 1654.617 | 1614.973 | 1694.262 | 1694.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23793) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23793) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23794) rss_mb | MB | 1 | 8.695 | 8.695 | 8.695 | 8.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23794) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23807) CPU | percent | 24 | 11.220 | 0.994 | 76.584 | 3.978 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23807) rss_mb | MB | 25 | 382.382 | 272.035 | 394.578 | 394.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23807) main thread run-queue wait | percent | 24 | 1.023 | 0.006 | 15.714 | 0.027 | 0.247269 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23807) vms_mb | MB | 25 | 9862.066 | 1667.020 | 10211.875 | 10211.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23829) rss_mb | MB | 1 | 212.457 | 212.457 | 212.457 | 212.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23829) vms_mb | MB | 1 | 1622.238 | 1622.238 | 1622.238 | 1622.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23852) rss_mb | MB | 1 | 2.660 | 2.660 | 2.660 | 2.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23852) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23853) rss_mb | MB | 1 | 14.023 | 14.023 | 14.023 | 14.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23853) vms_mb | MB | 1 | 207.629 | 207.629 | 207.629 | 207.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23864) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23864) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23865) rss_mb | MB | 1 | 7.523 | 7.523 | 7.523 | 7.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23865) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23869) CPU | percent | 7 | 37.770 | 3.972 | 74.540 | 5.970 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23869) rss_mb | MB | 8 | 342.596 | 176.344 | 386.941 | 386.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23869) main thread run-queue wait | percent | 7 | 5.247 | 0.012 | 12.809 | 0.016 | 0.376550 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23869) vms_mb | MB | 8 | 8057.905 | 1590.719 | 10208.270 | 10208.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23886) rss_mb | MB | 1 | 229.121 | 229.121 | 229.121 | 229.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23886) vms_mb | MB | 1 | 1631.723 | 1631.723 | 1631.723 | 1631.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23914) CPU | percent | 8 | 28.816 | 2.983 | 67.632 | 2.985 | 2.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23914) rss_mb | MB | 9 | 363.179 | 256.688 | 395.051 | 395.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23914) main thread run-queue wait | percent | 8 | 3.748 | 0.015 | 16.637 | 0.017 | 0.302493 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23914) vms_mb | MB | 9 | 9225.777 | 1652.531 | 10218.621 | 10218.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23931) CPU | percent | 1 | 60.519 | 60.519 | 60.519 | 60.519 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23931) rss_mb | MB | 2 | 214.043 | 165.965 | 262.121 | 262.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23931) main thread run-queue wait | percent | 1 | 14.150 | 14.150 | 14.150 | 14.150 | 0.142623 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23931) vms_mb | MB | 2 | 1617.639 | 1577.973 | 1657.305 | 1657.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23959) CPU | percent | 5 | 41.295 | 4.973 | 72.456 | 4.973 | 2.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23959) rss_mb | MB | 6 | 349.979 | 271.066 | 384.852 | 384.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23959) main thread run-queue wait | percent | 5 | 7.958 | 0.017 | 15.707 | 0.017 | 0.401088 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23959) vms_mb | MB | 6 | 8748.702 | 1665.996 | 10204.070 | 10204.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23977) CPU | percent | 1 | 57.565 | 57.565 | 57.565 | 57.565 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23977) rss_mb | MB | 2 | 212.641 | 164.730 | 260.551 | 260.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23977) main thread run-queue wait | percent | 1 | 17.690 | 17.690 | 17.690 | 17.690 | 0.178231 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23977) vms_mb | MB | 2 | 1614.154 | 1572.473 | 1655.836 | 1655.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23991) rss_mb | MB | 1 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23991) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23992) rss_mb | MB | 1 | 7.492 | 7.492 | 7.492 | 7.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23992) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24007) CPU | percent | 16 | 15.680 | 0.994 | 73.466 | 1.988 | 2.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24007) rss_mb | MB | 17 | 377.775 | 270.844 | 394.512 | 394.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24007) main thread run-queue wait | percent | 16 | 1.916 | 0.007 | 14.522 | 0.012 | 0.309655 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24007) vms_mb | MB | 17 | 9694.455 | 1666.355 | 10209.637 | 10209.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24026) CPU | percent | 1 | 49.299 | 49.299 | 49.299 | 49.299 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24026) rss_mb | MB | 2 | 186.734 | 143.801 | 229.668 | 229.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24026) main thread run-queue wait | percent | 1 | 12.390 | 12.390 | 12.390 | 12.390 | 0.125666 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24026) vms_mb | MB | 2 | 1467.830 | 1299.805 | 1635.855 | 1635.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24038) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24038) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24039) rss_mb | MB | 1 | 8.980 | 8.980 | 8.980 | 8.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24039) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24049) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24049) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 24050) rss_mb | MB | 1 | 20.457 | 20.457 | 20.457 | 20.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 24050) vms_mb | MB | 1 | 25.320 | 25.320 | 25.320 | 25.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 24051) rss_mb | MB | 1 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 24051) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 24052) rss_mb | MB | 1 | 1061.676 | 1061.676 | 1061.676 | 1061.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 24052) vms_mb | MB | 1 | 1253.316 | 1253.316 | 1253.316 | 1253.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24066) CPU | percent | 12 | 15.887 | 1.989 | 78.423 | 2.982 | 1.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24066) rss_mb | MB | 13 | 373.031 | 278.789 | 390.902 | 390.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24066) main thread run-queue wait | percent | 12 | 0.341 | 0.010 | 1.389 | 0.013 | 0.041136 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24066) vms_mb | MB | 13 | 9507.821 | 1674.738 | 10200.344 | 10158.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24094) rss_mb | MB | 1 | 294.137 | 294.137 | 294.137 | 294.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24094) vms_mb | MB | 1 | 1689.332 | 1689.332 | 1689.332 | 1689.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24113) CPU | percent | 5 | 39.920 | 4.973 | 72.465 | 4.973 | 2.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24113) rss_mb | MB | 6 | 354.900 | 281.668 | 386.152 | 386.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24113) main thread run-queue wait | percent | 5 | 5.338 | 0.014 | 14.573 | 0.014 | 0.274581 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24113) vms_mb | MB | 6 | 8756.289 | 1676.750 | 10207.422 | 10207.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24133) CPU | percent | 1 | 56.279 | 56.279 | 56.279 | 56.279 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24133) rss_mb | MB | 2 | 203.381 | 152.930 | 253.832 | 253.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24133) main thread run-queue wait | percent | 1 | 15.308 | 15.308 | 15.308 | 15.308 | 0.155046 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24133) vms_mb | MB | 2 | 1574.275 | 1499.219 | 1649.332 | 1649.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24145) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24145) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24146) rss_mb | MB | 1 | 8.875 | 8.875 | 8.875 | 8.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24146) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24159) CPU | percent | 39 | 8.047 | 0.993 | 77.433 | 2.983 | 3.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24159) rss_mb | MB | 40 | 383.233 | 273.531 | 391.480 | 391.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24159) main thread run-queue wait | percent | 39 | 1.277 | 0.000 | 21.852 | 0.005 | 0.501561 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24159) vms_mb | MB | 40 | 9990.652 | 1669.000 | 10210.938 | 10210.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24178) CPU | percent | 1 | 59.568 | 59.568 | 59.568 | 59.568 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24178) rss_mb | MB | 2 | 172.432 | 104.488 | 240.375 | 240.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24178) main thread run-queue wait | percent | 1 | 13.047 | 13.047 | 13.047 | 13.047 | 0.131412 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24178) vms_mb | MB | 2 | 1461.387 | 1283.695 | 1639.078 | 1639.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24212) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24212) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 24213) rss_mb | MB | 1 | 9.484 | 9.484 | 9.484 | 9.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 24213) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 24214) rss_mb | MB | 1 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 24214) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 24215) rss_mb | MB | 1 | 1061.629 | 1061.629 | 1061.629 | 1061.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 24215) vms_mb | MB | 1 | 1253.301 | 1253.301 | 1253.301 | 1253.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24232) CPU | percent | 17 | 17.639 | 0.995 | 69.453 | 2.984 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24232) rss_mb | MB | 18 | 366.898 | 188.711 | 390.977 | 390.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24232) main thread run-queue wait | percent | 17 | 1.322 | 0.005 | 12.602 | 0.044 | 0.226872 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24232) vms_mb | MB | 18 | 9254.159 | 1594.219 | 10209.523 | 10209.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24256) CPU | percent | 1 | 49.483 | 49.483 | 49.483 | 49.483 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24256) rss_mb | MB | 2 | 203.525 | 163.641 | 243.410 | 243.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24256) main thread run-queue wait | percent | 1 | 11.758 | 11.758 | 11.758 | 11.758 | 0.118808 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24256) vms_mb | MB | 2 | 1605.859 | 1572.473 | 1639.246 | 1639.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24263) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24263) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24264) rss_mb | MB | 1 | 7.988 | 7.988 | 7.988 | 7.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24264) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24277) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24277) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 24278) rss_mb | MB | 1 | 21.234 | 21.234 | 21.234 | 21.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 24278) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 24279) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 24279) rss_mb | MB | 2 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 24279) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 24279) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 24280) CPU | percent | 1 | 33.714 | 33.714 | 33.714 | 33.714 | 0.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 24280) rss_mb | MB | 2 | 68.367 | 58.551 | 78.184 | 78.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 24280) main thread run-queue wait | percent | 1 | 1.053 | 1.053 | 1.053 | 1.053 | 0.010620 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 24280) vms_mb | MB | 2 | 268.172 | 255.496 | 280.848 | 280.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24291) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24291) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24292) rss_mb | MB | 1 | 6.945 | 6.945 | 6.945 | 6.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24292) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24296) CPU | percent | 6 | 44.615 | 5.966 | 85.322 | 5.966 | 2.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24296) rss_mb | MB | 7 | 331.136 | 159.312 | 386.828 | 386.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24296) main thread run-queue wait | percent | 6 | 5.758 | 0.003 | 17.745 | 0.003 | 0.356307 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24296) vms_mb | MB | 7 | 7726.562 | 1499.965 | 10204.246 | 10204.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24315) CPU | percent | 1 | 64.172 | 64.172 | 64.172 | 64.172 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24315) rss_mb | MB | 2 | 223.334 | 172.016 | 274.652 | 274.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24315) main thread run-queue wait | percent | 1 | 14.540 | 14.540 | 14.540 | 14.540 | 0.147272 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24315) vms_mb | MB | 2 | 1624.768 | 1579.473 | 1670.062 | 1670.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24343) CPU | percent | 6 | 36.569 | 2.984 | 78.446 | 2.984 | 2.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24343) rss_mb | MB | 7 | 352.059 | 255.918 | 383.934 | 383.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24343) main thread run-queue wait | percent | 6 | 5.265 | 0.011 | 21.291 | 0.011 | 0.318200 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24343) vms_mb | MB | 7 | 8938.477 | 1651.527 | 10205.555 | 10205.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24360) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24360) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24361) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24361) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24362) CPU | percent | 1 | 55.619 | 55.619 | 55.619 | 55.619 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24362) rss_mb | MB | 2 | 263.529 | 229.672 | 297.387 | 297.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24362) main thread run-queue wait | percent | 1 | 17.750 | 17.750 | 17.750 | 17.750 | 0.178719 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24362) vms_mb | MB | 2 | 1662.346 | 1632.473 | 1692.219 | 1692.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24390) CPU | percent | 13 | 22.629 | 0.994 | 82.505 | 6.962 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24390) rss_mb | MB | 14 | 359.350 | 158.328 | 390.469 | 390.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24390) main thread run-queue wait | percent | 13 | 2.271 | 0.008 | 10.430 | 0.033 | 0.301571 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24390) vms_mb | MB | 14 | 8971.306 | 1499.965 | 10208.574 | 10208.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24409) CPU | percent | 1 | 61.201 | 61.201 | 61.201 | 61.201 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24409) rss_mb | MB | 2 | 223.564 | 175.223 | 271.906 | 271.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24409) main thread run-queue wait | percent | 1 | 12.893 | 12.893 | 12.893 | 12.893 | 0.130616 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24409) vms_mb | MB | 2 | 1624.512 | 1581.723 | 1667.301 | 1667.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 24417) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 24417) vms_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24455) CPU | percent | 11 | 21.920 | 1.989 | 75.314 | 1.989 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24455) rss_mb | MB | 12 | 368.150 | 229.742 | 395.273 | 395.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24455) main thread run-queue wait | percent | 11 | 2.330 | 0.003 | 17.480 | 0.003 | 0.258173 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24455) vms_mb | MB | 12 | 8782.098 | 1635.520 | 10207.387 | 10207.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24473) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24473) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24474) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24474) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24475) CPU | percent | 1 | 50.645 | 50.645 | 50.645 | 50.645 | 0.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24475) rss_mb | MB | 2 | 265.697 | 229.270 | 302.125 | 302.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24475) main thread run-queue wait | percent | 1 | 16.626 | 16.626 | 16.626 | 16.626 | 0.167421 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24475) vms_mb | MB | 2 | 1679.047 | 1631.730 | 1726.363 | 1726.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24488) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24488) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24489) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24489) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24504) CPU | percent | 6 | 36.888 | 1.989 | 78.562 | 1.989 | 2.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24504) rss_mb | MB | 7 | 352.940 | 244.293 | 389.625 | 389.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24504) main thread run-queue wait | percent | 6 | 3.860 | 0.028 | 18.584 | 0.028 | 0.233648 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24504) vms_mb | MB | 7 | 8946.852 | 1640.316 | 10207.828 | 10207.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24522) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24522) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24523) rss_mb | MB | 1 | 7.906 | 7.906 | 7.906 | 7.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24523) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24526) CPU | percent | 1 | 62.459 | 62.459 | 62.459 | 62.459 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24526) rss_mb | MB | 2 | 244.664 | 193.707 | 295.621 | 295.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24526) main thread run-queue wait | percent | 1 | 19.547 | 19.547 | 19.547 | 19.547 | 0.197164 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24526) vms_mb | MB | 2 | 1652.217 | 1614.223 | 1690.211 | 1690.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24536) rss_mb | MB | 1 | 1.398 | 1.398 | 1.398 | 1.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24536) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24537) rss_mb | MB | 1 | 7.371 | 7.371 | 7.371 | 7.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24537) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24552) CPU | percent | 11 | 19.411 | 0.994 | 75.423 | 1.988 | 2.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24552) rss_mb | MB | 12 | 377.640 | 292.035 | 396.879 | 396.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24552) main thread run-queue wait | percent | 11 | 1.653 | 0.006 | 8.315 | 0.006 | 0.183023 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24552) vms_mb | MB | 12 | 9489.362 | 1687.227 | 10213.516 | 10213.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24580) CPU | percent | 1 | 78.504 | 78.504 | 78.504 | 78.504 | 0.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24580) rss_mb | MB | 2 | 227.496 | 159.250 | 295.742 | 295.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24580) main thread run-queue wait | percent | 1 | 8.649 | 8.649 | 8.649 | 8.649 | 0.087037 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24580) vms_mb | MB | 2 | 1503.008 | 1315.809 | 1690.207 | 1690.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24599) CPU | percent | 12 | 17.907 | 0.994 | 72.474 | 0.994 | 2.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24599) rss_mb | MB | 13 | 372.847 | 295.719 | 390.746 | 390.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24599) main thread run-queue wait | percent | 12 | 2.124 | 0.007 | 14.458 | 0.016 | 0.258867 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24599) vms_mb | MB | 13 | 9538.153 | 1690.398 | 10211.160 | 10211.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24618) CPU | percent | 1 | 55.320 | 55.320 | 55.320 | 55.320 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24618) rss_mb | MB | 2 | 200.930 | 158.215 | 243.645 | 243.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24618) main thread run-queue wait | percent | 1 | 15.041 | 15.041 | 15.041 | 15.041 | 0.152258 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24618) vms_mb | MB | 2 | 1570.174 | 1499.969 | 1640.379 | 1640.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24633) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24633) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24634) rss_mb | MB | 1 | 10.027 | 10.027 | 10.027 | 10.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24634) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24725) CPU | percent | 6 | 43.519 | 5.967 | 71.442 | 5.967 | 2.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24725) rss_mb | MB | 7 | 332.873 | 175.090 | 386.574 | 386.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24725) main thread run-queue wait | percent | 6 | 5.858 | 0.018 | 14.827 | 0.018 | 0.356012 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24725) vms_mb | MB | 7 | 7748.312 | 1589.969 | 10206.285 | 10206.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24745) CPU | percent | 1 | 62.192 | 62.192 | 62.192 | 62.192 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24745) rss_mb | MB | 2 | 110.938 | 0.000 | 221.875 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24745) main thread run-queue wait | percent | 1 | 11.255 | 11.255 | 11.255 | 11.255 | 0.114010 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24745) vms_mb | MB | 2 | 812.359 | 0.000 | 1624.719 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24763) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24763) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24764) rss_mb | MB | 1 | 7.859 | 7.859 | 7.859 | 7.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24764) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24775) CPU | percent | 11 | 21.221 | 1.989 | 77.476 | 6.957 | 2.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24775) rss_mb | MB | 12 | 373.049 | 261.047 | 398.023 | 398.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24775) main thread run-queue wait | percent | 11 | 1.124 | 0.009 | 6.177 | 0.033 | 0.124545 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24775) vms_mb | MB | 12 | 9483.492 | 1656.254 | 10210.543 | 10210.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24804) rss_mb | MB | 1 | 259.289 | 259.289 | 259.289 | 259.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24804) vms_mb | MB | 1 | 1655.328 | 1655.328 | 1655.328 | 1655.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24823) CPU | percent | 14 | 16.415 | 0.994 | 77.508 | 5.968 | 2.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24823) rss_mb | MB | 15 | 371.443 | 234.465 | 392.078 | 392.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24823) main thread run-queue wait | percent | 14 | 0.567 | 0.007 | 2.912 | 0.008 | 0.080130 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24823) vms_mb | MB | 15 | 9060.063 | 1636.023 | 10196.914 | 10196.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24848) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24848) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24849) rss_mb | MB | 1 | 7.121 | 7.121 | 7.121 | 7.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24849) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24855) rss_mb | MB | 1 | 206.352 | 206.352 | 206.352 | 206.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24855) vms_mb | MB | 1 | 1619.719 | 1619.719 | 1619.719 | 1619.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24867) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24867) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24868) rss_mb | MB | 1 | 8.117 | 8.117 | 8.117 | 8.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24868) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24872) CPU | percent | 6 | 43.359 | 3.975 | 79.384 | 3.975 | 2.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24872) rss_mb | MB | 7 | 332.733 | 164.531 | 384.488 | 384.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24872) main thread run-queue wait | percent | 6 | 4.640 | 0.011 | 19.501 | 0.011 | 0.280526 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24872) vms_mb | MB | 7 | 7754.355 | 1572.469 | 10203.898 | 10203.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24894) CPU | percent | 1 | 47.637 | 47.637 | 47.637 | 47.637 | 0.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24894) rss_mb | MB | 2 | 194.227 | 159.473 | 228.980 | 228.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24894) main thread run-queue wait | percent | 1 | 14.864 | 14.864 | 14.864 | 14.864 | 0.149777 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24894) vms_mb | MB | 2 | 1473.660 | 1316.059 | 1631.262 | 1631.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24920) CPU | percent | 13 | 19.073 | 0.993 | 77.257 | 5.965 | 2.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24920) rss_mb | MB | 14 | 372.656 | 237.305 | 395.762 | 395.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24920) main thread run-queue wait | percent | 13 | 2.823 | 0.005 | 24.666 | 0.024 | 0.370261 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24920) vms_mb | MB | 14 | 8986.616 | 1637.516 | 10208.340 | 10208.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24941) CPU | percent | 1 | 61.406 | 61.406 | 61.406 | 61.406 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24941) rss_mb | MB | 2 | 262.600 | 222.219 | 302.980 | 302.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24941) main thread run-queue wait | percent | 1 | 24.461 | 24.461 | 24.461 | 24.461 | 0.246980 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24941) vms_mb | MB | 2 | 1676.178 | 1624.711 | 1727.645 | 1727.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24953) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24953) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24954) rss_mb | MB | 1 | 6.730 | 6.730 | 6.730 | 6.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24954) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24969) CPU | percent | 6 | 40.033 | 1.988 | 71.501 | 1.988 | 2.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24969) rss_mb | MB | 7 | 346.064 | 229.555 | 389.051 | 389.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24969) main thread run-queue wait | percent | 6 | 4.083 | 0.017 | 14.003 | 0.017 | 0.246915 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24969) vms_mb | MB | 7 | 7764.767 | 1632.539 | 10208.148 | 10208.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24992) CPU | percent | 1 | 51.587 | 51.587 | 51.587 | 51.587 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24992) rss_mb | MB | 2 | 212.580 | 168.270 | 256.891 | 256.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24992) main thread run-queue wait | percent | 1 | 9.184 | 9.184 | 9.184 | 9.184 | 0.092575 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24992) vms_mb | MB | 2 | 1615.268 | 1578.473 | 1652.062 | 1652.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25018) CPU | percent | 12 | 24.746 | 0.994 | 87.481 | 4.972 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25018) rss_mb | MB | 13 | 351.878 | 52.418 | 395.770 | 395.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25018) main thread run-queue wait | percent | 12 | 2.822 | 0.010 | 15.768 | 0.021 | 0.341779 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25018) vms_mb | MB | 13 | 8853.188 | 1238.512 | 10210.648 | 10210.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25037) CPU | percent | 1 | 60.398 | 60.398 | 60.398 | 60.398 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25037) rss_mb | MB | 2 | 222.510 | 174.875 | 270.145 | 270.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25037) main thread run-queue wait | percent | 1 | 15.712 | 15.712 | 15.712 | 15.712 | 0.158683 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25037) vms_mb | MB | 2 | 1627.494 | 1589.973 | 1665.016 | 1665.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 25045) rss_mb | MB | 1 | 50.711 | 50.711 | 50.711 | 50.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 25045) vms_mb | MB | 1 | 847.578 | 847.578 | 847.578 | 847.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25049) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25049) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25050) rss_mb | MB | 1 | 10.711 | 10.711 | 10.711 | 10.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25050) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25060) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25060) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25061) rss_mb | MB | 1 | 10.172 | 10.172 | 10.172 | 10.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25061) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25065) CPU | percent | 12 | 22.828 | 0.994 | 68.521 | 6.959 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25065) rss_mb | MB | 13 | 366.086 | 205.277 | 395.070 | 395.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25065) main thread run-queue wait | percent | 12 | 2.166 | 0.006 | 17.152 | 0.042 | 0.262145 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25065) vms_mb | MB | 13 | 8888.707 | 1618.797 | 10208.301 | 10208.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25084) CPU | percent | 1 | 49.548 | 49.548 | 49.548 | 49.548 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25084) rss_mb | MB | 2 | 225.197 | 189.020 | 261.375 | 261.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25084) main thread run-queue wait | percent | 1 | 16.190 | 16.190 | 16.190 | 16.190 | 0.163371 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25084) vms_mb | MB | 2 | 1625.260 | 1594.223 | 1656.297 | 1656.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25097) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25097) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25098) rss_mb | MB | 1 | 7.191 | 7.191 | 7.191 | 7.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25098) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25115) CPU | percent | 6 | 39.103 | 4.963 | 74.452 | 5.966 | 2.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25115) rss_mb | MB | 7 | 348.040 | 229.180 | 387.914 | 387.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25115) main thread run-queue wait | percent | 6 | 3.995 | 0.023 | 16.090 | 0.023 | 0.242117 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25115) vms_mb | MB | 7 | 7764.931 | 1635.543 | 10207.043 | 10207.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25137) CPU | percent | 1 | 51.561 | 51.561 | 51.561 | 51.561 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25137) rss_mb | MB | 2 | 213.432 | 167.723 | 259.141 | 259.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25137) main thread run-queue wait | percent | 1 | 17.868 | 17.868 | 17.868 | 17.868 | 0.180201 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25137) vms_mb | MB | 2 | 1616.898 | 1578.473 | 1655.324 | 1655.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25164) CPU | percent | 11 | 27.149 | 1.986 | 87.314 | 4.971 | 3.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25164) rss_mb | MB | 12 | 342.647 | 0.000 | 395.965 | 395.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25164) main thread run-queue wait | percent | 11 | 3.451 | 0.010 | 17.740 | 0.028 | 0.389771 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25164) vms_mb | MB | 12 | 8645.019 | 160.145 | 10208.254 | 10208.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25183) CPU | percent | 1 | 54.250 | 54.250 | 54.250 | 54.250 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25183) rss_mb | MB | 2 | 209.592 | 163.562 | 255.621 | 255.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25183) main thread run-queue wait | percent | 1 | 19.170 | 19.170 | 19.170 | 19.170 | 0.194351 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25183) vms_mb | MB | 2 | 1611.912 | 1572.473 | 1651.352 | 1651.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25206) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25206) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25207) rss_mb | MB | 1 | 7.188 | 7.188 | 7.188 | 7.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25207) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25211) CPU | percent | 11 | 24.655 | 0.000 | 67.570 | 3.977 | 2.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25211) rss_mb | MB | 12 | 363.005 | 194.309 | 395.102 | 395.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25211) main thread run-queue wait | percent | 11 | 2.118 | 0.011 | 16.679 | 0.016 | 0.234448 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25211) vms_mb | MB | 12 | 8781.491 | 1614.969 | 10210.941 | 10210.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25233) CPU | percent | 1 | 44.715 | 44.715 | 44.715 | 44.715 | 0.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25233) rss_mb | MB | 2 | 201.773 | 166.703 | 236.844 | 236.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25233) main thread run-queue wait | percent | 1 | 15.095 | 15.095 | 15.095 | 15.095 | 0.151913 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25233) vms_mb | MB | 2 | 1607.520 | 1577.723 | 1637.316 | 1637.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25240) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25240) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25241) rss_mb | MB | 1 | 8.695 | 8.695 | 8.695 | 8.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25241) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25259) CPU | percent | 13 | 23.313 | 1.989 | 86.430 | 3.976 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25259) rss_mb | MB | 14 | 355.755 | 58.781 | 397.613 | 397.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25259) main thread run-queue wait | percent | 13 | 3.633 | 0.007 | 20.532 | 0.028 | 0.475650 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25259) vms_mb | MB | 14 | 8948.178 | 1238.512 | 10208.707 | 10208.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25278) CPU | percent | 1 | 52.581 | 52.581 | 52.581 | 52.581 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25278) rss_mb | MB | 2 | 209.930 | 166.551 | 253.309 | 253.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25278) main thread run-queue wait | percent | 1 | 12.324 | 12.324 | 12.324 | 12.324 | 0.124227 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25278) vms_mb | MB | 2 | 1613.533 | 1577.723 | 1649.344 | 1649.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25306) CPU | percent | 11 | 24.104 | 1.987 | 67.563 | 1.989 | 2.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25306) rss_mb | MB | 12 | 362.551 | 206.172 | 392.426 | 392.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25306) main thread run-queue wait | percent | 11 | 3.742 | 0.008 | 21.219 | 0.011 | 0.414675 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25306) vms_mb | MB | 12 | 8781.504 | 1619.027 | 10208.633 | 10208.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25326) CPU | percent | 1 | 61.515 | 61.515 | 61.515 | 61.515 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25326) rss_mb | MB | 2 | 240.686 | 193.461 | 287.910 | 287.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25326) main thread run-queue wait | percent | 1 | 16.559 | 16.559 | 16.559 | 16.559 | 0.166893 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25326) vms_mb | MB | 2 | 1648.648 | 1614.223 | 1683.074 | 1683.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25354) CPU | percent | 7 | 40.439 | 2.985 | 85.384 | 2.985 | 2.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25354) rss_mb | MB | 8 | 327.019 | 91.156 | 387.746 | 387.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25354) main thread run-queue wait | percent | 7 | 5.486 | 0.008 | 15.797 | 0.008 | 0.386939 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25354) vms_mb | MB | 8 | 8005.607 | 1283.598 | 10204.934 | 10204.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25373) CPU | percent | 1 | 61.455 | 61.455 | 61.455 | 61.455 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25373) rss_mb | MB | 2 | 250.816 | 205.996 | 295.637 | 295.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25373) main thread run-queue wait | percent | 1 | 20.582 | 20.582 | 20.582 | 20.582 | 0.207650 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25373) vms_mb | MB | 2 | 1654.725 | 1619.227 | 1690.223 | 1690.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25403) CPU | percent | 11 | 20.216 | 0.994 | 75.439 | 2.984 | 2.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25403) rss_mb | MB | 12 | 367.030 | 271.574 | 388.492 | 388.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25403) main thread run-queue wait | percent | 11 | 3.006 | 0.008 | 18.565 | 0.013 | 0.333230 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25403) vms_mb | MB | 12 | 9479.049 | 1666.738 | 10208.125 | 10208.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25422) CPU | percent | 1 | 58.560 | 58.560 | 58.560 | 58.560 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25422) rss_mb | MB | 2 | 200.873 | 147.871 | 253.875 | 253.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25422) main thread run-queue wait | percent | 1 | 14.467 | 14.467 | 14.467 | 14.467 | 0.145760 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25422) vms_mb | MB | 2 | 1476.859 | 1304.117 | 1649.602 | 1649.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25434) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25434) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25435) rss_mb | MB | 1 | 4.602 | 4.602 | 4.602 | 4.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25435) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 25443) rss_mb | MB | 1 | 2.047 | 2.047 | 2.047 | 2.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 25443) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 25444) rss_mb | MB | 1 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 25444) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25450) CPU | percent | 12 | 24.179 | 0.994 | 82.340 | 6.960 | 2.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25450) rss_mb | MB | 13 | 360.986 | 160.586 | 394.785 | 394.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25450) main thread run-queue wait | percent | 12 | 2.463 | 0.010 | 15.430 | 0.026 | 0.297453 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25450) vms_mb | MB | 13 | 8878.603 | 1500.215 | 10210.621 | 10210.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25474) rss_mb | MB | 1 | 197.266 | 197.266 | 197.266 | 197.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25474) vms_mb | MB | 1 | 1616.504 | 1616.504 | 1616.504 | 1616.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25500) CPU | percent | 11 | 24.915 | 0.995 | 75.412 | 1.989 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25500) rss_mb | MB | 12 | 361.441 | 188.023 | 396.488 | 396.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25500) main thread run-queue wait | percent | 11 | 3.114 | 0.007 | 23.086 | 0.013 | 0.345503 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25500) vms_mb | MB | 12 | 8779.994 | 1594.469 | 10211.234 | 10211.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25522) CPU | percent | 1 | 47.557 | 47.557 | 47.557 | 47.557 | 0.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25522) rss_mb | MB | 2 | 202.373 | 166.840 | 237.906 | 237.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25522) main thread run-queue wait | percent | 1 | 14.963 | 14.963 | 14.963 | 14.963 | 0.151023 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25522) vms_mb | MB | 2 | 1607.916 | 1578.223 | 1637.609 | 1637.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25529) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25529) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25530) rss_mb | MB | 1 | 9.012 | 9.012 | 9.012 | 9.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25530) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25548) CPU | percent | 11 | 19.852 | 0.994 | 71.466 | 1.986 | 2.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25548) rss_mb | MB | 12 | 370.366 | 276.020 | 391.953 | 391.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25548) main thread run-queue wait | percent | 11 | 2.694 | 0.002 | 14.645 | 0.008 | 0.298706 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25548) vms_mb | MB | 12 | 9479.820 | 1671.758 | 10207.527 | 10207.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25565) CPU | percent | 1 | 58.525 | 58.525 | 58.525 | 58.525 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25565) rss_mb | MB | 2 | 209.324 | 159.055 | 259.594 | 259.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25565) main thread run-queue wait | percent | 1 | 10.336 | 10.336 | 10.336 | 10.336 | 0.104201 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25565) vms_mb | MB | 2 | 1578.023 | 1499.969 | 1656.078 | 1656.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25572) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25572) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25573) rss_mb | MB | 1 | 10.605 | 10.605 | 10.605 | 10.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25573) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25581) rss_mb | MB | 1 | 1.344 | 1.344 | 1.344 | 1.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25581) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25582) rss_mb | MB | 1 | 8.105 | 8.105 | 8.105 | 8.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25582) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25597) CPU | percent | 6 | 34.610 | 5.968 | 74.582 | 6.962 | 2.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25597) rss_mb | MB | 7 | 358.338 | 286.758 | 389.367 | 389.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25597) main thread run-queue wait | percent | 6 | 4.986 | 0.046 | 14.123 | 0.046 | 0.301205 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25597) vms_mb | MB | 7 | 8962.274 | 1682.262 | 10205.430 | 10205.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25616) CPU | percent | 1 | 53.557 | 53.557 | 53.557 | 53.557 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25616) rss_mb | MB | 2 | 172.318 | 108.973 | 235.664 | 235.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25616) main thread run-queue wait | percent | 1 | 14.403 | 14.403 | 14.403 | 14.403 | 0.145217 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25616) vms_mb | MB | 2 | 1459.773 | 1283.695 | 1635.852 | 1635.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 25643) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 25643) vms_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25646) CPU | percent | 12 | 22.181 | 1.986 | 70.616 | 1.989 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25646) rss_mb | MB | 13 | 368.261 | 214.422 | 397.715 | 397.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25646) main thread run-queue wait | percent | 12 | 3.265 | 0.002 | 26.149 | 0.012 | 0.395126 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25646) vms_mb | MB | 13 | 8890.071 | 1622.797 | 10209.637 | 10209.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25665) CPU | percent | 1 | 57.475 | 57.475 | 57.475 | 57.475 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25665) rss_mb | MB | 2 | 239.654 | 193.992 | 285.316 | 285.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25665) main thread run-queue wait | percent | 1 | 24.113 | 24.113 | 24.113 | 24.113 | 0.243337 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25665) vms_mb | MB | 2 | 1647.902 | 1614.473 | 1681.332 | 1681.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25675) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25675) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25676) rss_mb | MB | 1 | 9.875 | 9.875 | 9.875 | 9.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25676) vms_mb | MB | 1 | 13.578 | 13.578 | 13.578 | 13.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25696) CPU | percent | 11 | 19.437 | 1.984 | 74.583 | 2.983 | 2.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25696) rss_mb | MB | 12 | 372.229 | 294.098 | 392.297 | 392.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25696) main thread run-queue wait | percent | 11 | 1.603 | 0.010 | 13.467 | 0.020 | 0.180097 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25696) vms_mb | MB | 12 | 9483.072 | 1689.078 | 10205.449 | 10205.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25727) CPU | percent | 1 | 76.199 | 76.199 | 76.199 | 76.199 | 0.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25727) rss_mb | MB | 2 | 209.760 | 122.539 | 296.980 | 296.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25727) main thread run-queue wait | percent | 1 | 5.097 | 5.097 | 5.097 | 5.097 | 0.054845 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25727) vms_mb | MB | 2 | 1509.959 | 1296.352 | 1723.566 | 1723.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25746) CPU | percent | 12 | 20.416 | 0.995 | 77.248 | 3.975 | 2.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25746) rss_mb | MB | 13 | 370.381 | 243.336 | 393.480 | 393.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25746) main thread run-queue wait | percent | 12 | 1.861 | 0.006 | 17.007 | 0.020 | 0.225135 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25746) vms_mb | MB | 13 | 8893.334 | 1639.793 | 10207.922 | 10207.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25789) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25789) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25790) rss_mb | MB | 1 | 10.773 | 10.773 | 10.773 | 10.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25790) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25794) rss_mb | MB | 1 | 229.090 | 229.090 | 229.090 | 229.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25794) vms_mb | MB | 1 | 1631.590 | 1631.590 | 1631.590 | 1631.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25809) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25809) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25810) rss_mb | MB | 1 | 7.367 | 7.367 | 7.367 | 7.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25810) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25814) CPU | percent | 6 | 42.385 | 4.974 | 69.539 | 4.974 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25814) rss_mb | MB | 7 | 341.011 | 192.793 | 387.395 | 387.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25814) main thread run-queue wait | percent | 6 | 5.221 | 0.017 | 22.119 | 0.017 | 0.315444 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25814) vms_mb | MB | 7 | 7758.596 | 1598.465 | 10208.262 | 10207.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25834) CPU | percent | 1 | 56.604 | 56.604 | 56.604 | 56.604 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25834) rss_mb | MB | 2 | 248.457 | 205.660 | 291.254 | 291.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25834) main thread run-queue wait | percent | 1 | 20.077 | 20.077 | 20.077 | 20.077 | 0.202179 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25834) vms_mb | MB | 2 | 1652.523 | 1618.980 | 1686.066 | 1686.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25844) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25844) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25845) rss_mb | MB | 1 | 7.551 | 7.551 | 7.551 | 7.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25845) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25862) CPU | percent | 11 | 21.556 | 0.993 | 77.199 | 0.995 | 2.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25862) rss_mb | MB | 12 | 365.949 | 236.285 | 391.898 | 391.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25862) main thread run-queue wait | percent | 11 | 0.534 | 0.003 | 2.407 | 0.003 | 0.059106 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25862) vms_mb | MB | 12 | 8788.946 | 1636.312 | 10211.895 | 10211.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25880) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25880) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25881) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25881) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25891) rss_mb | MB | 1 | 211.770 | 211.770 | 211.770 | 211.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25891) vms_mb | MB | 1 | 1622.727 | 1622.727 | 1622.727 | 1622.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25910) CPU | percent | 12 | 24.171 | 0.995 | 86.475 | 0.995 | 2.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25910) rss_mb | MB | 13 | 355.283 | 109.324 | 395.117 | 395.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25910) main thread run-queue wait | percent | 12 | 2.605 | 0.006 | 13.416 | 0.009 | 0.314753 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25910) vms_mb | MB | 13 | 8856.399 | 1283.598 | 10208.156 | 10208.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25929) CPU | percent | 1 | 48.698 | 48.698 | 48.698 | 48.698 | 0.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25929) rss_mb | MB | 2 | 203.303 | 166.531 | 240.074 | 240.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25929) main thread run-queue wait | percent | 1 | 12.999 | 12.999 | 12.999 | 12.999 | 0.130795 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25929) vms_mb | MB | 2 | 1608.023 | 1577.723 | 1638.324 | 1638.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 25937) rss_mb | MB | 1 | 49.773 | 49.773 | 49.773 | 49.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 25937) vms_mb | MB | 1 | 851.352 | 851.352 | 851.352 | 851.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25957) CPU | percent | 12 | 23.425 | 1.987 | 80.436 | 5.968 | 2.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25957) rss_mb | MB | 13 | 359.821 | 161.043 | 391.770 | 391.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25957) main thread run-queue wait | percent | 12 | 2.196 | 0.007 | 14.794 | 0.021 | 0.265620 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25957) vms_mb | MB | 13 | 8865.897 | 1317.719 | 10208.109 | 10208.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25979) CPU | percent | 1 | 41.645 | 41.645 | 41.645 | 41.645 | 0.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25979) rss_mb | MB | 2 | 141.453 | 71.809 | 211.098 | 211.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25979) main thread run-queue wait | percent | 1 | 7.121 | 7.121 | 7.121 | 7.121 | 0.071814 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25979) vms_mb | MB | 2 | 1453.221 | 1283.695 | 1622.746 | 1622.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25986) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25986) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25987) rss_mb | MB | 1 | 6.930 | 6.930 | 6.930 | 6.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25987) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26003) CPU | percent | 12 | 24.034 | 1.987 | 78.545 | 7.946 | 2.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26003) rss_mb | MB | 13 | 360.823 | 167.484 | 397.246 | 397.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26003) main thread run-queue wait | percent | 12 | 2.297 | 0.005 | 13.461 | 0.042 | 0.279498 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26003) vms_mb | MB | 13 | 8885.415 | 1577.969 | 10208.543 | 10208.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26025) CPU | percent | 1 | 55.865 | 55.865 | 55.865 | 55.865 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26025) rss_mb | MB | 2 | 214.795 | 169.727 | 259.863 | 259.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26025) main thread run-queue wait | percent | 1 | 13.717 | 13.717 | 13.717 | 13.717 | 0.139959 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26025) vms_mb | MB | 2 | 1617.393 | 1578.723 | 1656.062 | 1656.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26053) CPU | percent | 11 | 22.753 | 0.995 | 72.479 | 6.960 | 2.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26053) rss_mb | MB | 12 | 365.400 | 229.719 | 395.238 | 395.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26053) main thread run-queue wait | percent | 11 | 3.049 | 0.005 | 20.681 | 0.023 | 0.337794 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26053) vms_mb | MB | 12 | 8784.459 | 1632.020 | 10212.160 | 10212.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26072) CPU | percent | 1 | 58.550 | 58.550 | 58.550 | 58.550 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26072) rss_mb | MB | 2 | 241.631 | 194.242 | 289.020 | 289.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26072) main thread run-queue wait | percent | 1 | 16.613 | 16.613 | 16.613 | 16.613 | 0.167411 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26072) vms_mb | MB | 2 | 1649.014 | 1614.473 | 1683.555 | 1683.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26095) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26095) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26096) rss_mb | MB | 1 | 9.223 | 9.223 | 9.223 | 9.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26096) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26100) CPU | percent | 11 | 25.094 | 1.989 | 74.399 | 1.990 | 2.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26100) rss_mb | MB | 12 | 363.806 | 194.902 | 397.121 | 397.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26100) main thread run-queue wait | percent | 11 | 3.443 | 0.005 | 23.401 | 0.006 | 0.382005 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26100) vms_mb | MB | 12 | 8781.810 | 1614.969 | 10211.281 | 10211.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26122) CPU | percent | 1 | 38.638 | 38.638 | 38.638 | 38.638 | 0.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26122) rss_mb | MB | 2 | 152.098 | 84.207 | 219.988 | 219.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26122) main thread run-queue wait | percent | 1 | 21.550 | 21.550 | 21.550 | 21.550 | 0.217522 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26122) vms_mb | MB | 2 | 1453.836 | 1283.695 | 1623.977 | 1623.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26128) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26128) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26129) rss_mb | MB | 1 | 8.609 | 8.609 | 8.609 | 8.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26129) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26148) CPU | percent | 12 | 23.007 | 0.994 | 77.396 | 2.985 | 2.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26148) rss_mb | MB | 13 | 359.776 | 166.375 | 391.707 | 391.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26148) main thread run-queue wait | percent | 12 | 2.496 | 0.006 | 18.775 | 0.010 | 0.301782 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26148) vms_mb | MB | 13 | 8888.659 | 1577.969 | 10209.965 | 10209.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26173) rss_mb | MB | 1 | 197.113 | 197.113 | 197.113 | 197.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26173) vms_mb | MB | 1 | 1616.242 | 1616.242 | 1616.242 | 1616.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26197) CPU | percent | 7 | 32.484 | 2.979 | 77.512 | 9.942 | 2.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26197) rss_mb | MB | 8 | 359.462 | 260.668 | 397.113 | 397.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26197) main thread run-queue wait | percent | 7 | 3.854 | 0.013 | 12.947 | 0.013 | 0.271776 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26197) vms_mb | MB | 8 | 9115.014 | 1656.230 | 10212.617 | 10212.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26216) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26216) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26217) rss_mb | MB | 1 | 8.859 | 8.859 | 8.859 | 8.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26217) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26218) CPU | percent | 1 | 52.547 | 52.547 | 52.547 | 52.547 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26218) rss_mb | MB | 2 | 153.463 | 71.742 | 235.184 | 235.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26218) main thread run-queue wait | percent | 1 | 8.539 | 8.539 | 8.539 | 8.539 | 0.086128 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26218) vms_mb | MB | 2 | 1460.143 | 1283.695 | 1636.590 | 1636.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26318) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26318) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26319) rss_mb | MB | 1 | 5.059 | 5.059 | 5.059 | 5.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26319) vms_mb | MB | 1 | 11.383 | 11.383 | 11.383 | 11.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26323) CPU | percent | 11 | 24.747 | 0.994 | 72.516 | 1.989 | 2.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26323) rss_mb | MB | 12 | 359.956 | 185.977 | 394.391 | 394.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26323) main thread run-queue wait | percent | 11 | 3.458 | 0.006 | 24.280 | 0.007 | 0.383137 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26323) vms_mb | MB | 12 | 8778.660 | 1593.469 | 10211.285 | 10211.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26342) CPU | percent | 1 | 58.564 | 58.564 | 58.564 | 58.564 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26342) rss_mb | MB | 2 | 234.244 | 189.180 | 279.309 | 279.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26342) main thread run-queue wait | percent | 1 | 18.014 | 18.014 | 18.014 | 18.014 | 0.181478 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26342) vms_mb | MB | 2 | 1634.395 | 1594.473 | 1674.316 | 1674.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26373) CPU | percent | 13 | 22.825 | 1.989 | 84.410 | 3.973 | 3.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26373) rss_mb | MB | 14 | 361.317 | 152.219 | 394.074 | 394.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26373) main thread run-queue wait | percent | 13 | 2.791 | 0.006 | 18.452 | 0.092 | 0.370232 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26373) vms_mb | MB | 14 | 8957.319 | 1308.969 | 10213.141 | 10213.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26394) CPU | percent | 1 | 61.340 | 61.340 | 61.340 | 61.340 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26394) rss_mb | MB | 2 | 220.346 | 168.352 | 272.340 | 272.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26394) main thread run-queue wait | percent | 1 | 12.017 | 12.017 | 12.017 | 12.017 | 0.123419 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26394) vms_mb | MB | 2 | 1622.754 | 1578.473 | 1667.035 | 1667.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26406) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26406) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26407) rss_mb | MB | 1 | 8.816 | 8.816 | 8.816 | 8.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26407) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26422) CPU | percent | 12 | 24.993 | 0.994 | 82.472 | 1.989 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26422) rss_mb | MB | 13 | 361.797 | 175.430 | 392.387 | 392.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26422) main thread run-queue wait | percent | 12 | 1.607 | 0.004 | 12.387 | 0.004 | 0.194169 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26422) vms_mb | MB | 13 | 8894.175 | 1589.969 | 10214.133 | 10214.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26455) rss_mb | MB | 1 | 260.539 | 260.539 | 260.539 | 260.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26455) vms_mb | MB | 1 | 1656.590 | 1656.590 | 1656.590 | 1656.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26472) CPU | percent | 10 | 24.626 | 1.989 | 73.460 | 1.989 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26472) rss_mb | MB | 11 | 359.080 | 229.645 | 388.766 | 388.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26472) main thread run-queue wait | percent | 10 | 2.033 | 0.011 | 11.488 | 0.012 | 0.204693 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26472) vms_mb | MB | 11 | 8656.618 | 1632.035 | 10209.676 | 10209.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26502) rss_mb | MB | 1 | 235.457 | 235.457 | 235.457 | 235.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26502) vms_mb | MB | 1 | 1636.340 | 1636.340 | 1636.340 | 1636.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26521) CPU | percent | 12 | 24.511 | 1.984 | 86.471 | 2.983 | 2.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26521) rss_mb | MB | 13 | 356.044 | 118.246 | 394.797 | 394.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26521) main thread run-queue wait | percent | 12 | 1.387 | 0.005 | 9.069 | 0.006 | 0.167502 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26521) vms_mb | MB | 13 | 8863.227 | 1296.254 | 10214.648 | 10214.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26551) rss_mb | MB | 1 | 295.238 | 295.238 | 295.238 | 295.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26551) vms_mb | MB | 1 | 1689.727 | 1689.727 | 1689.727 | 1689.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26570) CPU | percent | 6 | 34.118 | 1.990 | 68.602 | 3.960 | 2.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26570) rss_mb | MB | 7 | 357.209 | 295.273 | 383.531 | 383.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26570) main thread run-queue wait | percent | 6 | 5.642 | 0.014 | 13.204 | 0.085 | 0.340694 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26570) vms_mb | MB | 7 | 8961.588 | 1690.281 | 10209.059 | 10209.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26587) CPU | percent | 1 | 60.607 | 60.607 | 60.607 | 60.607 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26587) rss_mb | MB | 2 | 233.707 | 189.160 | 278.254 | 278.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26587) main thread run-queue wait | percent | 1 | 10.687 | 10.687 | 10.687 | 10.687 | 0.107565 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26587) vms_mb | MB | 2 | 1633.777 | 1594.223 | 1673.332 | 1673.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26601) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26601) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26602) rss_mb | MB | 1 | 7.520 | 7.520 | 7.520 | 7.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26602) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26617) CPU | percent | 12 | 24.331 | 0.995 | 81.398 | 1.989 | 2.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26617) rss_mb | MB | 13 | 360.858 | 158.215 | 398.020 | 398.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26617) main thread run-queue wait | percent | 12 | 2.653 | 0.008 | 10.613 | 0.012 | 0.320767 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26617) vms_mb | MB | 13 | 8865.044 | 1315.172 | 10212.055 | 10212.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26636) CPU | percent | 1 | 55.572 | 55.572 | 55.572 | 55.572 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26636) rss_mb | MB | 2 | 215.418 | 170.430 | 260.406 | 260.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26636) main thread run-queue wait | percent | 1 | 9.373 | 9.373 | 9.373 | 9.373 | 0.094455 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26636) vms_mb | MB | 2 | 1618.176 | 1579.473 | 1656.879 | 1656.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26664) CPU | percent | 14 | 21.276 | 0.994 | 85.492 | 2.984 | 3.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26664) rss_mb | MB | 15 | 357.547 | 57.512 | 395.367 | 395.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26664) main thread run-queue wait | percent | 14 | 1.428 | 0.004 | 10.910 | 0.012 | 0.202158 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26664) vms_mb | MB | 15 | 9036.011 | 1238.512 | 10212.797 | 10212.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26694) CPU | percent | 1 | 84.303 | 84.303 | 84.303 | 84.303 | 0.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26694) rss_mb | MB | 2 | 169.008 | 42.902 | 295.113 | 295.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26694) main thread run-queue wait | percent | 1 | 7.768 | 7.768 | 7.768 | 7.768 | 0.078319 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26694) vms_mb | MB | 2 | 1431.939 | 1174.324 | 1689.555 | 1689.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26713) CPU | percent | 12 | 19.865 | 1.989 | 80.529 | 6.960 | 2.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26713) rss_mb | MB | 13 | 374.734 | 262.504 | 397.973 | 397.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26713) main thread run-queue wait | percent | 12 | 2.495 | 0.006 | 25.963 | 0.017 | 0.301906 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26713) vms_mb | MB | 13 | 9539.056 | 1657.746 | 10214.078 | 10214.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26731) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26731) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26732) rss_mb | MB | 1 | 10.145 | 10.145 | 10.145 | 10.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26732) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26736) CPU | percent | 1 | 61.469 | 61.469 | 61.469 | 61.469 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26736) rss_mb | MB | 2 | 244.725 | 193.844 | 295.605 | 295.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26736) main thread run-queue wait | percent | 1 | 21.205 | 21.205 | 21.205 | 21.205 | 0.213883 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26736) vms_mb | MB | 2 | 1652.346 | 1614.723 | 1689.969 | 1689.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26746) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26746) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26747) rss_mb | MB | 1 | 9.371 | 9.371 | 9.371 | 9.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26747) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26762) CPU | percent | 7 | 36.739 | 2.983 | 63.605 | 7.957 | 2.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26762) rss_mb | MB | 8 | 347.569 | 211.398 | 394.242 | 394.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26762) main thread run-queue wait | percent | 7 | 4.450 | 0.011 | 19.275 | 0.013 | 0.313924 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26762) vms_mb | MB | 8 | 8068.666 | 1622.039 | 10212.457 | 10212.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26782) CPU | percent | 1 | 58.501 | 58.501 | 58.501 | 58.501 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26782) rss_mb | MB | 2 | 231.211 | 189.238 | 273.184 | 273.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26782) main thread run-queue wait | percent | 1 | 18.619 | 18.619 | 18.619 | 18.619 | 0.187781 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26782) vms_mb | MB | 2 | 1631.275 | 1594.723 | 1667.828 | 1667.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26810) CPU | percent | 12 | 24.826 | 0.995 | 85.411 | 1.990 | 3.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26810) rss_mb | MB | 13 | 350.076 | 43.938 | 396.074 | 396.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26810) main thread run-queue wait | percent | 12 | 1.398 | 0.005 | 6.219 | 0.005 | 0.168885 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26810) vms_mb | MB | 13 | 8852.862 | 1174.227 | 10213.363 | 10213.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26838) rss_mb | MB | 1 | 288.445 | 288.445 | 288.445 | 288.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26838) vms_mb | MB | 1 | 1683.785 | 1683.785 | 1683.785 | 1683.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26860) CPU | percent | 10 | 21.408 | 1.989 | 73.475 | 2.980 | 2.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26860) rss_mb | MB | 11 | 372.347 | 288.934 | 394.410 | 394.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26860) main thread run-queue wait | percent | 10 | 1.944 | 0.006 | 9.803 | 0.015 | 0.198625 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26860) vms_mb | MB | 11 | 9418.022 | 1683.605 | 10212.750 | 10212.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26879) CPU | percent | 1 | 53.241 | 53.241 | 53.241 | 53.241 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26879) rss_mb | MB | 2 | 192.678 | 148.234 | 237.121 | 237.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26879) main thread run-queue wait | percent | 1 | 5.412 | 5.412 | 5.412 | 5.412 | 0.054892 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26879) vms_mb | MB | 2 | 1470.922 | 1304.496 | 1637.348 | 1637.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26891) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26891) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26892) rss_mb | MB | 1 | 8.820 | 8.820 | 8.820 | 8.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26892) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26907) CPU | percent | 39 | 7.963 | 0.992 | 76.442 | 4.974 | 3.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26907) rss_mb | MB | 40 | 386.814 | 277.824 | 396.852 | 396.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26907) main thread run-queue wait | percent | 39 | 0.423 | 0.003 | 11.207 | 0.018 | 0.166697 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26907) vms_mb | MB | 40 | 9995.632 | 1672.949 | 10215.496 | 10215.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26940) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26940) rss_mb | MB | 7 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26940) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26940) vms_mb | MB | 7 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26941) CPU | percent | 6 | 12.886 | 0.000 | 64.441 | 0.000 | 0.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26941) rss_mb | MB | 7 | 61.010 | 20.789 | 68.609 | 68.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26941) main thread run-queue wait | percent | 6 | 0.264 | 0.000 | 0.514 | 0.000 | 0.016001 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26941) vms_mb | MB | 7 | 74.333 | 26.930 | 83.254 | 83.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26943) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26943) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 26944) rss_mb | MB | 1 | 21.527 | 21.527 | 21.527 | 21.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 26944) vms_mb | MB | 1 | 27.070 | 27.070 | 27.070 | 27.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26951) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26951) rss_mb | MB | 4 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26951) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26951) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26952) CPU | percent | 3 | 24.133 | 3.973 | 62.468 | 5.958 | 0.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26952) rss_mb | MB | 4 | 57.653 | 30.395 | 67.906 | 67.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26952) main thread run-queue wait | percent | 3 | 0.511 | 0.172 | 0.856 | 0.856 | 0.015446 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26952) vms_mb | MB | 4 | 71.091 | 39.863 | 82.773 | 82.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26971) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26971) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 26972) rss_mb | MB | 1 | 17.797 | 17.797 | 17.797 | 17.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 26972) vms_mb | MB | 1 | 23.184 | 23.184 | 23.184 | 23.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26981) CPU | percent | 11 | 26.434 | 1.988 | 76.402 | 7.953 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26981) rss_mb | MB | 12 | 360.419 | 172.371 | 395.758 | 395.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26981) main thread run-queue wait | percent | 11 | 2.229 | 0.013 | 9.071 | 0.028 | 0.247380 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26981) vms_mb | MB | 12 | 8779.083 | 1579.469 | 10212.848 | 10212.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27002) CPU | percent | 1 | 46.523 | 46.523 | 46.523 | 46.523 | 0.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27002) rss_mb | MB | 2 | 108.285 | 0.000 | 216.570 | 216.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27002) main thread run-queue wait | percent | 1 | 7.641 | 7.641 | 7.641 | 7.641 | 0.077195 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27002) vms_mb | MB | 2 | 811.684 | 0.129 | 1623.238 | 1623.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27028) CPU | percent | 14 | 17.461 | 0.995 | 72.598 | 5.969 | 2.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27028) rss_mb | MB | 15 | 374.746 | 219.234 | 401.484 | 401.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27028) main thread run-queue wait | percent | 14 | 0.595 | 0.011 | 3.410 | 0.023 | 0.083850 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27028) vms_mb | MB | 15 | 9064.424 | 1624.266 | 10203.293 | 10203.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27055) rss_mb | MB | 1 | 237.051 | 237.051 | 237.051 | 237.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27055) vms_mb | MB | 1 | 1637.855 | 1637.855 | 1637.855 | 1637.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 27069) rss_mb | MB | 1 | 2.129 | 2.129 | 2.129 | 2.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 27069) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 27070) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 27070) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27074) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27074) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27075) rss_mb | MB | 1 | 10.715 | 10.715 | 10.715 | 10.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27075) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27079) CPU | percent | 6 | 38.684 | 2.980 | 66.444 | 2.980 | 2.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27079) rss_mb | MB | 7 | 339.611 | 198.992 | 383.004 | 383.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27079) main thread run-queue wait | percent | 6 | 3.894 | 0.018 | 11.100 | 0.018 | 0.235783 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27079) vms_mb | MB | 7 | 7750.049 | 1617.535 | 10192.238 | 10192.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27097) CPU | percent | 1 | 57.563 | 57.563 | 57.563 | 57.563 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27097) rss_mb | MB | 2 | 171.344 | 106.047 | 236.641 | 236.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27097) main thread run-queue wait | percent | 1 | 18.173 | 18.173 | 18.173 | 18.173 | 0.183104 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27097) vms_mb | MB | 2 | 1460.262 | 1283.695 | 1636.828 | 1636.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27115) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27115) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27125) CPU | percent | 14 | 22.864 | 1.987 | 86.144 | 1.990 | 3.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27125) rss_mb | MB | 15 | 352.296 | 0.000 | 396.852 | 396.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27125) main thread run-queue wait | percent | 14 | 3.482 | 0.007 | 19.182 | 0.013 | 0.491157 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27125) vms_mb | MB | 15 | 8948.659 | 3.312 | 10213.027 | 10213.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27142) CPU | percent | 1 | 64.507 | 64.507 | 64.507 | 64.507 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27142) rss_mb | MB | 2 | 241.973 | 189.418 | 294.527 | 294.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27142) main thread run-queue wait | percent | 1 | 19.619 | 19.619 | 19.619 | 19.619 | 0.197688 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27142) vms_mb | MB | 2 | 1641.883 | 1594.473 | 1689.293 | 1689.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 27167) rss_mb | MB | 1 | 2.039 | 2.039 | 2.039 | 2.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 27167) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 27168) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 27168) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27175) CPU | percent | 12 | 25.985 | 1.986 | 85.489 | 7.959 | 3.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27175) rss_mb | MB | 13 | 354.392 | 96.121 | 396.488 | 396.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27175) main thread run-queue wait | percent | 12 | 3.210 | 0.005 | 17.995 | 0.026 | 0.388239 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27175) vms_mb | MB | 13 | 8854.642 | 1283.598 | 10213.223 | 10213.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27194) CPU | percent | 1 | 57.549 | 57.549 | 57.549 | 57.549 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27194) rss_mb | MB | 2 | 203.434 | 154.691 | 252.176 | 252.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27194) main thread run-queue wait | percent | 1 | 14.791 | 14.791 | 14.791 | 14.791 | 0.149067 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27194) vms_mb | MB | 2 | 1479.596 | 1310.871 | 1648.320 | 1648.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27207) rss_mb | MB | 1 | 1.488 | 1.488 | 1.488 | 1.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27207) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27208) rss_mb | MB | 1 | 8.008 | 8.008 | 8.008 | 8.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27208) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27221) CPU | percent | 13 | 21.974 | 0.995 | 74.556 | 0.995 | 2.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27221) rss_mb | MB | 14 | 366.353 | 228.883 | 389.129 | 389.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27221) main thread run-queue wait | percent | 13 | 4.248 | 0.005 | 37.167 | 0.014 | 0.566440 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27221) vms_mb | MB | 14 | 8991.006 | 1631.793 | 10215.152 | 10215.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27243) CPU | percent | 1 | 55.285 | 55.285 | 55.285 | 55.285 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27243) rss_mb | MB | 2 | 251.617 | 208.621 | 294.613 | 294.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27243) main thread run-queue wait | percent | 1 | 32.459 | 32.459 | 32.459 | 32.459 | 0.328792 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27243) vms_mb | MB | 2 | 1654.664 | 1619.496 | 1689.832 | 1689.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27271) CPU | percent | 10 | 22.929 | 0.994 | 76.447 | 2.984 | 2.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27271) rss_mb | MB | 11 | 370.609 | 271.312 | 395.637 | 395.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27271) main thread run-queue wait | percent | 10 | 3.071 | 0.007 | 17.559 | 0.011 | 0.309520 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27271) vms_mb | MB | 11 | 9415.203 | 1666.496 | 10212.711 | 10212.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27289) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27289) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27290) rss_mb | MB | 1 | 9.297 | 9.297 | 9.297 | 9.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27290) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27291) CPU | percent | 1 | 53.542 | 53.542 | 53.542 | 53.542 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27291) rss_mb | MB | 2 | 155.189 | 76.055 | 234.324 | 234.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27291) main thread run-queue wait | percent | 1 | 12.659 | 12.659 | 12.659 | 12.659 | 0.127675 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27291) vms_mb | MB | 2 | 1459.773 | 1283.695 | 1635.852 | 1635.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27319) CPU | percent | 12 | 20.198 | 0.994 | 75.530 | 6.962 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27319) rss_mb | MB | 13 | 341.646 | 0.000 | 394.605 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27319) main thread run-queue wait | percent | 12 | 3.015 | 0.010 | 24.800 | 0.039 | 0.364515 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27319) vms_mb | MB | 13 | 8123.711 | 0.000 | 10212.863 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27336) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27336) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27337) rss_mb | MB | 1 | 8.734 | 8.734 | 8.734 | 8.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27337) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27338) CPU | percent | 2 | 52.087 | 48.659 | 55.515 | 48.659 | 1.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27338) rss_mb | MB | 3 | 189.984 | 42.324 | 297.953 | 297.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27338) main thread run-queue wait | percent | 2 | 15.740 | 9.958 | 21.521 | 21.521 | 0.317174 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27338) vms_mb | MB | 3 | 1511.312 | 1173.824 | 1724.254 | 1724.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27368) CPU | percent | 10 | 25.319 | 0.993 | 77.334 | 3.975 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27368) rss_mb | MB | 11 | 364.644 | 228.762 | 394.871 | 394.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27368) main thread run-queue wait | percent | 10 | 3.076 | 0.014 | 21.260 | 0.030 | 0.309533 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27368) vms_mb | MB | 11 | 8655.741 | 1631.262 | 10212.758 | 10212.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27391) CPU | percent | 1 | 43.729 | 43.729 | 43.729 | 43.729 | 0.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27391) rss_mb | MB | 2 | 197.488 | 160.754 | 234.223 | 234.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27391) main thread run-queue wait | percent | 1 | 19.366 | 19.366 | 19.366 | 19.366 | 0.194862 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27391) vms_mb | MB | 2 | 1567.912 | 1500.469 | 1635.355 | 1635.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27415) CPU | percent | 10 | 22.326 | 1.988 | 77.583 | 2.984 | 2.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27415) rss_mb | MB | 11 | 372.762 | 278.754 | 397.594 | 397.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27415) main thread run-queue wait | percent | 10 | 1.015 | 0.006 | 5.380 | 0.013 | 0.104452 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27415) vms_mb | MB | 11 | 9422.219 | 1673.496 | 10212.473 | 10212.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27444) rss_mb | MB | 1 | 161.133 | 161.133 | 161.133 | 161.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27444) vms_mb | MB | 1 | 1500.469 | 1500.469 | 1500.469 | 1500.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27463) CPU | percent | 12 | 20.996 | 0.993 | 70.470 | 6.965 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27463) rss_mb | MB | 13 | 368.736 | 235.488 | 394.660 | 394.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27463) main thread run-queue wait | percent | 12 | 1.452 | 0.014 | 12.544 | 0.037 | 0.182137 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27463) vms_mb | MB | 13 | 8894.407 | 1636.023 | 10209.801 | 10209.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27486) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27486) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27487) rss_mb | MB | 1 | 9.066 | 9.066 | 9.066 | 9.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27487) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27491) rss_mb | MB | 1 | 212.980 | 212.980 | 212.980 | 212.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27491) vms_mb | MB | 1 | 1623.250 | 1623.250 | 1623.250 | 1623.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27510) CPU | percent | 13 | 20.466 | 1.988 | 73.491 | 5.964 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27510) rss_mb | MB | 14 | 367.887 | 229.398 | 394.770 | 394.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27510) main thread run-queue wait | percent | 13 | 2.327 | 0.006 | 15.999 | 0.131 | 0.304915 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27510) vms_mb | MB | 14 | 8986.216 | 1631.520 | 10210.020 | 10210.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27530) CPU | percent | 1 | 49.558 | 49.558 | 49.558 | 49.558 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27530) rss_mb | MB | 2 | 233.297 | 195.234 | 271.359 | 271.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27530) main thread run-queue wait | percent | 1 | 15.004 | 15.004 | 15.004 | 15.004 | 0.151383 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27530) vms_mb | MB | 2 | 1641.129 | 1615.473 | 1666.785 | 1666.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27557) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27557) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27558) rss_mb | MB | 1 | 10.895 | 10.895 | 10.895 | 10.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27558) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27562) CPU | percent | 13 | 21.872 | 0.994 | 69.452 | 6.961 | 2.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27562) rss_mb | MB | 14 | 368.293 | 193.906 | 395.855 | 395.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27562) main thread run-queue wait | percent | 13 | 3.111 | 0.011 | 18.577 | 0.022 | 0.411321 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27562) vms_mb | MB | 14 | 8983.004 | 1605.469 | 10211.910 | 10211.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27579) CPU | percent | 1 | 58.600 | 58.600 | 58.600 | 58.600 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27579) rss_mb | MB | 2 | 142.209 | 49.410 | 235.008 | 235.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27579) main thread run-queue wait | percent | 1 | 19.944 | 19.944 | 19.944 | 19.944 | 0.200798 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27579) vms_mb | MB | 2 | 1437.102 | 1238.609 | 1635.594 | 1635.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27598) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27598) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27599) rss_mb | MB | 1 | 7.422 | 7.422 | 7.422 | 7.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27599) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 27603) rss_mb | MB | 1 | 2.234 | 2.234 | 2.234 | 2.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 27603) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 27604) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 27604) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27610) CPU | percent | 12 | 22.273 | 0.995 | 66.652 | 2.979 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27610) rss_mb | MB | 13 | 368.607 | 208.426 | 398.688 | 398.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27610) main thread run-queue wait | percent | 12 | 3.658 | 0.004 | 15.491 | 0.018 | 0.441781 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27610) vms_mb | MB | 13 | 8890.198 | 1619.555 | 10209.363 | 10209.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27629) CPU | percent | 1 | 57.612 | 57.612 | 57.612 | 57.612 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27629) rss_mb | MB | 2 | 201.410 | 148.559 | 254.262 | 254.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27629) main thread run-queue wait | percent | 1 | 9.615 | 9.615 | 9.615 | 9.615 | 0.096793 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27629) vms_mb | MB | 2 | 1477.158 | 1304.746 | 1649.570 | 1649.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27659) CPU | percent | 12 | 23.695 | 1.987 | 79.449 | 1.990 | 2.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27659) rss_mb | MB | 13 | 363.403 | 167.805 | 398.461 | 398.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27659) main thread run-queue wait | percent | 12 | 2.494 | 0.014 | 14.354 | 0.017 | 0.301878 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27659) vms_mb | MB | 13 | 8886.593 | 1578.469 | 10209.520 | 10209.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27682) rss_mb | MB | 1 | 202.445 | 202.445 | 202.445 | 202.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27682) vms_mb | MB | 1 | 1618.227 | 1618.227 | 1618.227 | 1618.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27708) CPU | percent | 12 | 22.501 | 1.986 | 65.419 | 2.985 | 2.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27708) rss_mb | MB | 13 | 373.002 | 227.707 | 400.109 | 400.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27708) main thread run-queue wait | percent | 12 | 2.092 | 0.004 | 13.846 | 0.025 | 0.252765 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27708) vms_mb | MB | 13 | 8897.482 | 1630.805 | 10214.465 | 10214.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27741) rss_mb | MB | 1 | 197.883 | 197.883 | 197.883 | 197.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27741) vms_mb | MB | 1 | 1616.727 | 1616.727 | 1616.727 | 1616.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 27758) CPU | percent | 11 | 19.369 | 0.995 | 71.601 | 2.984 | 2.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 27758) rss_mb | MB | 12 | 379.106 | 298.242 | 399.812 | 399.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 27758) main thread run-queue wait | percent | 11 | 2.058 | 0.008 | 10.697 | 0.010 | 0.234657 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 27758) vms_mb | MB | 12 | 9486.694 | 1723.664 | 10209.203 | 10209.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27777) CPU | percent | 1 | 57.514 | 57.514 | 57.514 | 57.514 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27777) rss_mb | MB | 2 | 213.953 | 166.668 | 261.238 | 261.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27777) main thread run-queue wait | percent | 1 | 13.860 | 13.860 | 13.860 | 13.860 | 0.139771 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27777) vms_mb | MB | 2 | 1617.270 | 1577.973 | 1656.566 | 1656.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27789) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27789) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27790) rss_mb | MB | 1 | 8.816 | 8.816 | 8.816 | 8.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27790) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27805) CPU | percent | 12 | 18.556 | 1.989 | 76.571 | 2.982 | 2.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27805) rss_mb | MB | 13 | 376.558 | 294.797 | 395.801 | 395.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27805) main thread run-queue wait | percent | 12 | 2.247 | 0.012 | 13.079 | 0.024 | 0.276502 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27805) vms_mb | MB | 13 | 9538.138 | 1689.547 | 10209.383 | 10209.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27824) CPU | percent | 1 | 53.029 | 53.029 | 53.029 | 53.029 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27824) rss_mb | MB | 2 | 195.004 | 153.340 | 236.668 | 236.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27824) main thread run-queue wait | percent | 1 | 12.861 | 12.861 | 12.861 | 12.861 | 0.130966 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27824) vms_mb | MB | 2 | 1473.422 | 1309.238 | 1637.605 | 1637.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27836) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27836) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27837) rss_mb | MB | 1 | 9.059 | 9.059 | 9.059 | 9.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27837) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27854) CPU | percent | 12 | 17.686 | 0.995 | 76.402 | 1.989 | 2.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27854) rss_mb | MB | 13 | 369.739 | 259.840 | 392.379 | 392.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27854) main thread run-queue wait | percent | 12 | 0.592 | 0.010 | 2.753 | 0.018 | 0.073340 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27854) vms_mb | MB | 13 | 8863.575 | 1655.547 | 10204.992 | 10158.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27883) rss_mb | MB | 1 | 259.941 | 259.941 | 259.941 | 259.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27883) vms_mb | MB | 1 | 1655.555 | 1655.555 | 1655.555 | 1655.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27902) CPU | percent | 7 | 32.023 | 2.980 | 81.436 | 7.832 | 2.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27902) rss_mb | MB | 8 | 357.708 | 252.816 | 395.223 | 395.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27902) main thread run-queue wait | percent | 7 | 3.191 | 0.014 | 14.837 | 0.014 | 0.225352 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27902) vms_mb | MB | 8 | 9103.268 | 1648.492 | 10216.328 | 10216.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27924) CPU | percent | 1 | 60.424 | 60.424 | 60.424 | 60.424 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27924) rss_mb | MB | 2 | 243.850 | 193.449 | 294.250 | 294.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27924) main thread run-queue wait | percent | 1 | 16.435 | 16.435 | 16.435 | 16.435 | 0.165920 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27924) vms_mb | MB | 2 | 1644.000 | 1598.723 | 1689.277 | 1689.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27948) CPU | percent | 12 | 18.838 | 1.988 | 77.437 | 8.895 | 2.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27948) rss_mb | MB | 13 | 376.043 | 295.039 | 395.488 | 395.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27948) main thread run-queue wait | percent | 12 | 2.302 | 0.011 | 16.763 | 0.027 | 0.299794 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27948) vms_mb | MB | 13 | 9542.425 | 1689.895 | 10212.121 | 10212.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27971) rss_mb | MB | 1 | 220.137 | 220.137 | 220.137 | 220.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27971) vms_mb | MB | 1 | 1624.238 | 1624.238 | 1624.238 | 1624.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27997) CPU | percent | 11 | 25.008 | 1.988 | 66.544 | 9.946 | 2.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27997) rss_mb | MB | 12 | 363.715 | 211.074 | 395.121 | 395.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27997) main thread run-queue wait | percent | 11 | 2.817 | 0.005 | 18.288 | 0.050 | 0.312218 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27997) vms_mb | MB | 12 | 8779.845 | 1622.297 | 10209.156 | 10209.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28016) CPU | percent | 1 | 53.588 | 53.588 | 53.588 | 53.588 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28016) rss_mb | MB | 2 | 230.475 | 193.270 | 267.680 | 267.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28016) main thread run-queue wait | percent | 1 | 18.532 | 18.532 | 18.532 | 18.532 | 0.186748 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28016) vms_mb | MB | 2 | 1630.758 | 1598.473 | 1663.043 | 1663.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28027) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28027) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28028) rss_mb | MB | 1 | 6.617 | 6.617 | 6.617 | 6.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28028) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28045) CPU | percent | 14 | 20.076 | 1.988 | 63.631 | 1.989 | 2.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28045) rss_mb | MB | 15 | 373.210 | 205.855 | 399.926 | 399.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28045) main thread run-queue wait | percent | 14 | 1.699 | 0.006 | 11.223 | 0.020 | 0.239740 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28045) vms_mb | MB | 15 | 9069.167 | 1619.035 | 10214.609 | 10213.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28066) CPU | percent | 1 | 37.661 | 37.661 | 37.661 | 37.661 | 0.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28066) rss_mb | MB | 2 | 148.654 | 86.211 | 211.098 | 211.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28066) main thread run-queue wait | percent | 1 | 11.199 | 11.199 | 11.199 | 11.199 | 0.112994 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28066) vms_mb | MB | 2 | 1453.082 | 1283.695 | 1622.469 | 1622.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28073) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28073) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28074) rss_mb | MB | 1 | 7.320 | 7.320 | 7.320 | 7.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28074) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28114) CPU | percent | 11 | 22.656 | 0.994 | 73.475 | 3.978 | 2.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28114) rss_mb | MB | 12 | 368.181 | 236.066 | 395.598 | 395.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28114) main thread run-queue wait | percent | 11 | 1.128 | 0.011 | 8.011 | 0.021 | 0.125067 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28114) vms_mb | MB | 12 | 8785.461 | 1636.301 | 10212.020 | 10212.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28144) rss_mb | MB | 1 | 206.918 | 206.918 | 206.918 | 206.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28144) vms_mb | MB | 1 | 1619.211 | 1619.211 | 1619.211 | 1619.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28163) CPU | percent | 12 | 21.275 | 1.986 | 76.437 | 1.987 | 2.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28163) rss_mb | MB | 13 | 369.443 | 235.578 | 396.590 | 396.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28163) main thread run-queue wait | percent | 12 | 2.654 | 0.009 | 22.617 | 0.009 | 0.320550 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28163) vms_mb | MB | 13 | 8892.667 | 1636.047 | 10209.492 | 10209.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28184) CPU | percent | 1 | 55.655 | 55.655 | 55.655 | 55.655 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28184) rss_mb | MB | 2 | 246.531 | 205.668 | 287.395 | 287.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28184) main thread run-queue wait | percent | 1 | 24.311 | 24.311 | 24.311 | 24.311 | 0.244614 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28184) vms_mb | MB | 2 | 1650.367 | 1618.949 | 1681.785 | 1681.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28212) CPU | percent | 13 | 23.888 | 1.988 | 85.446 | 5.965 | 3.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28212) rss_mb | MB | 14 | 353.577 | 40.418 | 399.566 | 399.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28212) main thread run-queue wait | percent | 13 | 2.820 | 0.006 | 19.942 | 0.029 | 0.370093 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28212) vms_mb | MB | 14 | 8946.671 | 1172.289 | 10214.395 | 10214.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28229) CPU | percent | 1 | 61.641 | 61.641 | 61.641 | 61.641 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28229) rss_mb | MB | 2 | 202.803 | 146.168 | 259.438 | 259.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28229) main thread run-queue wait | percent | 1 | 10.225 | 10.225 | 10.225 | 10.225 | 0.104507 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28229) vms_mb | MB | 2 | 1478.652 | 1302.234 | 1655.070 | 1655.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28230) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28230) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28236) rss_mb | MB | 1 | 10.836 | 10.836 | 10.836 | 10.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28236) vms_mb | MB | 1 | 14.730 | 14.730 | 14.730 | 14.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28260) CPU | percent | 12 | 23.496 | 0.994 | 74.403 | 2.983 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28260) rss_mb | MB | 13 | 365.562 | 187.344 | 398.488 | 398.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28260) main thread run-queue wait | percent | 12 | 2.258 | 0.007 | 11.941 | 0.031 | 0.272997 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28260) vms_mb | MB | 13 | 8890.550 | 1593.969 | 10213.137 | 10213.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28282) CPU | percent | 1 | 31.727 | 31.727 | 31.727 | 31.727 | 0.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28282) rss_mb | MB | 2 | 183.172 | 154.840 | 211.504 | 211.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28282) main thread run-queue wait | percent | 1 | 8.894 | 8.894 | 8.894 | 8.894 | 0.089703 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28282) vms_mb | MB | 2 | 1466.799 | 1310.871 | 1622.727 | 1622.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28308) CPU | percent | 11 | 21.856 | 0.995 | 79.526 | 6.953 | 2.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28308) rss_mb | MB | 12 | 372.099 | 262.680 | 397.578 | 397.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28308) main thread run-queue wait | percent | 11 | 3.178 | 0.010 | 24.337 | 0.018 | 0.352034 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28308) vms_mb | MB | 12 | 9481.944 | 1657.746 | 10212.609 | 10212.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28326) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28326) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28327) rss_mb | MB | 1 | 7.738 | 7.738 | 7.738 | 7.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28327) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28328) CPU | percent | 2 | 51.130 | 42.702 | 59.559 | 42.702 | 1.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28328) rss_mb | MB | 3 | 190.829 | 38.617 | 298.504 | 298.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28328) main thread run-queue wait | percent | 2 | 15.545 | 8.584 | 22.506 | 22.506 | 0.313109 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28328) vms_mb | MB | 3 | 1510.633 | 1171.504 | 1724.316 | 1724.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28356) CPU | percent | 12 | 23.339 | 1.988 | 72.414 | 1.988 | 2.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28356) rss_mb | MB | 13 | 368.214 | 189.133 | 399.621 | 399.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28356) main thread run-queue wait | percent | 12 | 1.933 | 0.003 | 12.392 | 0.003 | 0.233566 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28356) vms_mb | MB | 13 | 8888.500 | 1594.719 | 10209.895 | 10209.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28378) rss_mb | MB | 1 | 206.012 | 206.012 | 206.012 | 206.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28378) vms_mb | MB | 1 | 1619.020 | 1619.020 | 1619.020 | 1619.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28404) CPU | percent | 12 | 19.344 | 1.989 | 77.428 | 1.989 | 2.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28404) rss_mb | MB | 13 | 369.472 | 260.539 | 391.832 | 391.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28404) main thread run-queue wait | percent | 12 | 1.660 | 0.011 | 13.118 | 0.016 | 0.200969 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28404) vms_mb | MB | 13 | 9538.947 | 1656.016 | 10211.250 | 10211.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28423) rss_mb | MB | 1 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28423) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28424) rss_mb | MB | 1 | 9.215 | 9.215 | 9.215 | 9.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28424) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28429) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28429) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28430) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28430) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28434) rss_mb | MB | 1 | 228.684 | 228.684 | 228.684 | 228.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28434) vms_mb | MB | 1 | 1635.840 | 1635.840 | 1635.840 | 1635.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28453) CPU | percent | 13 | 17.481 | 0.982 | 73.470 | 7.950 | 2.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28453) rss_mb | MB | 14 | 378.335 | 291.281 | 397.023 | 397.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28453) main thread run-queue wait | percent | 13 | 2.212 | 0.009 | 16.176 | 0.024 | 0.301880 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28453) vms_mb | MB | 14 | 9589.849 | 1685.762 | 10213.637 | 10213.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28473) CPU | percent | 1 | 54.262 | 54.262 | 54.262 | 54.262 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28473) rss_mb | MB | 2 | 164.336 | 94.027 | 234.645 | 234.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28473) main thread run-queue wait | percent | 1 | 11.447 | 11.447 | 11.447 | 11.447 | 0.116031 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28473) vms_mb | MB | 2 | 1459.516 | 1283.695 | 1635.336 | 1635.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28485) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28485) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28486) rss_mb | MB | 1 | 10.086 | 10.086 | 10.086 | 10.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28486) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28501) CPU | percent | 13 | 20.608 | 0.000 | 68.530 | 1.988 | 2.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28501) rss_mb | MB | 14 | 366.464 | 211.332 | 392.664 | 392.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28501) main thread run-queue wait | percent | 13 | 2.694 | 0.007 | 26.914 | 0.030 | 0.373991 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28501) vms_mb | MB | 14 | 8987.501 | 1622.324 | 10212.707 | 10212.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28520) CPU | percent | 1 | 57.098 | 57.098 | 57.098 | 57.098 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28520) rss_mb | MB | 2 | 248.043 | 201.324 | 294.762 | 294.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28520) main thread run-queue wait | percent | 1 | 28.674 | 28.674 | 28.674 | 28.674 | 0.311355 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28520) vms_mb | MB | 2 | 1653.512 | 1617.719 | 1689.305 | 1689.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28531) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28531) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28532) rss_mb | MB | 1 | 9.031 | 9.031 | 9.031 | 9.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28532) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28549) CPU | percent | 12 | 25.074 | 0.995 | 85.419 | 0.995 | 3.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28549) rss_mb | MB | 13 | 352.578 | 62.570 | 397.781 | 397.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28549) main thread run-queue wait | percent | 12 | 2.416 | 0.007 | 15.806 | 0.009 | 0.292160 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28549) vms_mb | MB | 13 | 8855.845 | 1238.512 | 10212.527 | 10212.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28571) rss_mb | MB | 1 | 206.047 | 206.047 | 206.047 | 206.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28571) vms_mb | MB | 1 | 1619.215 | 1619.215 | 1619.215 | 1619.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28597) CPU | percent | 11 | 26.934 | 1.989 | 84.379 | 2.984 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28597) rss_mb | MB | 12 | 349.395 | 88.504 | 394.254 | 394.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28597) main thread run-queue wait | percent | 11 | 1.494 | 0.012 | 5.561 | 0.013 | 0.166357 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28597) vms_mb | MB | 12 | 8745.586 | 1283.598 | 10212.871 | 10212.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28626) CPU | percent | 1 | 71.287 | 71.287 | 71.287 | 71.287 | 0.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28626) rss_mb | MB | 2 | 223.279 | 160.133 | 286.426 | 286.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28626) main thread run-queue wait | percent | 1 | 10.616 | 10.616 | 10.616 | 10.616 | 0.107227 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28626) vms_mb | MB | 2 | 1498.635 | 1315.719 | 1681.551 | 1681.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28643) CPU | percent | 11 | 22.881 | 0.994 | 75.923 | 2.984 | 2.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28643) rss_mb | MB | 12 | 372.481 | 238.582 | 400.836 | 400.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28643) main thread run-queue wait | percent | 11 | 2.729 | 0.009 | 18.287 | 0.031 | 0.302310 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28643) vms_mb | MB | 12 | 8787.484 | 1638.289 | 10214.766 | 10214.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28665) CPU | percent | 1 | 55.662 | 55.662 | 55.662 | 55.662 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28665) rss_mb | MB | 2 | 237.494 | 196.570 | 278.418 | 278.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28665) main thread run-queue wait | percent | 1 | 14.477 | 14.477 | 14.477 | 14.477 | 0.145650 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28665) vms_mb | MB | 2 | 1644.666 | 1615.988 | 1673.344 | 1673.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28693) CPU | percent | 14 | 17.606 | 0.995 | 77.592 | 6.965 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28693) rss_mb | MB | 15 | 377.670 | 273.168 | 398.715 | 398.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28693) main thread run-queue wait | percent | 14 | 3.372 | 0.009 | 31.737 | 0.027 | 0.475057 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28693) vms_mb | MB | 15 | 9629.127 | 1667.996 | 10215.387 | 10214.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28712) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28712) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28713) rss_mb | MB | 1 | 10.117 | 10.117 | 10.117 | 10.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28713) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28714) CPU | percent | 2 | 49.628 | 46.746 | 52.509 | 46.746 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28714) rss_mb | MB | 3 | 206.566 | 94.707 | 295.863 | 295.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28714) main thread run-queue wait | percent | 2 | 19.636 | 9.295 | 29.978 | 29.978 | 0.395223 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28714) vms_mb | MB | 3 | 1535.546 | 1283.695 | 1690.969 | 1690.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28745) CPU | percent | 12 | 24.180 | 1.987 | 75.413 | 1.987 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28745) rss_mb | MB | 13 | 361.145 | 169.812 | 393.891 | 393.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28745) main thread run-queue wait | percent | 12 | 3.893 | 0.006 | 16.448 | 0.016 | 0.473045 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28745) vms_mb | MB | 13 | 8885.201 | 1578.719 | 10213.484 | 10213.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28764) rss_mb | MB | 1 | 229.078 | 229.078 | 229.078 | 229.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28764) vms_mb | MB | 1 | 1631.953 | 1631.953 | 1631.953 | 1631.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28772) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28772) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28773) rss_mb | MB | 1 | 10.156 | 10.156 | 10.156 | 10.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28773) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28794) CPU | percent | 12 | 21.684 | 0.994 | 75.473 | 6.963 | 2.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28794) rss_mb | MB | 13 | 370.451 | 235.906 | 398.555 | 398.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28794) main thread run-queue wait | percent | 12 | 2.505 | 0.005 | 24.978 | 0.035 | 0.302876 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28794) vms_mb | MB | 13 | 8895.446 | 1636.539 | 10213.891 | 10213.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28816) CPU | percent | 1 | 43.661 | 43.661 | 43.661 | 43.661 | 0.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28816) rss_mb | MB | 2 | 197.189 | 159.590 | 234.789 | 234.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28816) main thread run-queue wait | percent | 1 | 17.912 | 17.912 | 17.912 | 17.912 | 0.180507 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28816) vms_mb | MB | 2 | 1567.617 | 1499.969 | 1635.266 | 1635.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 28840) rss_mb | MB | 1 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 28840) vms_mb | MB | 1 | 6.684 | 6.684 | 6.684 | 6.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28843) CPU | percent | 12 | 22.590 | 0.995 | 65.532 | 1.989 | 2.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28843) rss_mb | MB | 13 | 368.820 | 207.754 | 401.719 | 401.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28843) main thread run-queue wait | percent | 12 | 2.026 | 0.007 | 14.592 | 0.011 | 0.245014 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28843) vms_mb | MB | 13 | 8893.947 | 1619.551 | 10214.977 | 10214.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 28856) rss_mb | MB | 1 | 16.852 | 16.852 | 16.852 | 16.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 28856) vms_mb | MB | 1 | 706.980 | 706.980 | 706.980 | 706.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28865) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28865) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28866) rss_mb | MB | 1 | 9.207 | 9.207 | 9.207 | 9.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28866) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28870) rss_mb | MB | 1 | 177.492 | 177.492 | 177.492 | 177.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28870) vms_mb | MB | 1 | 1590.973 | 1590.973 | 1590.973 | 1590.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28894) CPU | percent | 14 | 21.055 | 0.993 | 65.443 | 7.954 | 2.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28894) rss_mb | MB | 15 | 367.396 | 193.766 | 394.082 | 394.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28894) main thread run-queue wait | percent | 14 | 2.543 | 0.007 | 13.869 | 0.015 | 0.359116 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28894) vms_mb | MB | 15 | 9064.740 | 1614.219 | 10213.074 | 10213.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28912) CPU | percent | 1 | 56.445 | 56.445 | 56.445 | 56.445 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28912) rss_mb | MB | 2 | 114.631 | 0.000 | 229.262 | 229.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28912) main thread run-queue wait | percent | 1 | 16.425 | 16.425 | 16.425 | 16.425 | 0.165864 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28912) vms_mb | MB | 2 | 898.002 | 160.145 | 1635.859 | 1635.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28930) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28930) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28931) rss_mb | MB | 1 | 7.367 | 7.367 | 7.367 | 7.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28931) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28942) CPU | percent | 11 | 25.145 | 0.994 | 68.449 | 3.978 | 2.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28942) rss_mb | MB | 12 | 362.142 | 188.801 | 397.281 | 397.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28942) main thread run-queue wait | percent | 11 | 2.061 | 0.013 | 11.372 | 0.025 | 0.229277 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28942) vms_mb | MB | 12 | 8781.076 | 1593.969 | 10214.117 | 10214.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28970) rss_mb | MB | 1 | 167.996 | 167.996 | 167.996 | 167.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28970) vms_mb | MB | 1 | 1578.473 | 1578.473 | 1578.473 | 1578.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28992) CPU | percent | 12 | 20.706 | 0.994 | 70.615 | 1.990 | 2.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28992) rss_mb | MB | 13 | 368.980 | 254.156 | 393.043 | 393.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28992) main thread run-queue wait | percent | 12 | 1.139 | 0.012 | 8.023 | 0.012 | 0.138008 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28992) vms_mb | MB | 13 | 8896.505 | 1650.273 | 10207.645 | 10207.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29020) rss_mb | MB | 1 | 189.074 | 189.074 | 189.074 | 189.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29020) vms_mb | MB | 1 | 1594.223 | 1594.223 | 1594.223 | 1594.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29039) CPU | percent | 14 | 18.445 | 0.995 | 77.454 | 1.990 | 2.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29039) rss_mb | MB | 15 | 376.716 | 235.512 | 401.125 | 400.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29039) main thread run-queue wait | percent | 14 | 1.912 | 0.007 | 21.566 | 0.017 | 0.269720 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29039) vms_mb | MB | 15 | 9072.055 | 1636.281 | 10215.367 | 10214.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29062) CPU | percent | 1 | 42.675 | 42.675 | 42.675 | 42.675 | 0.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29062) rss_mb | MB | 2 | 206.240 | 175.160 | 237.320 | 237.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29062) main thread run-queue wait | percent | 1 | 17.269 | 17.269 | 17.269 | 17.269 | 0.174000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29062) vms_mb | MB | 2 | 1614.158 | 1590.223 | 1638.094 | 1638.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29091) CPU | percent | 11 | 20.667 | 0.995 | 77.490 | 1.988 | 2.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29091) rss_mb | MB | 12 | 376.487 | 289.641 | 399.398 | 399.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29091) main thread run-queue wait | percent | 11 | 2.922 | 0.013 | 17.582 | 0.015 | 0.324114 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29091) vms_mb | MB | 12 | 9486.536 | 1684.492 | 10213.918 | 10213.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29110) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29110) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29111) rss_mb | MB | 1 | 10.117 | 10.117 | 10.117 | 10.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29111) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29112) CPU | percent | 2 | 51.051 | 45.640 | 56.462 | 45.640 | 1.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29112) rss_mb | MB | 3 | 206.618 | 79.660 | 304.113 | 304.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29112) main thread run-queue wait | percent | 2 | 12.081 | 11.298 | 12.864 | 12.864 | 0.243703 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29112) vms_mb | MB | 3 | 1549.389 | 1283.695 | 1728.152 | 1728.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29140) CPU | percent | 13 | 20.315 | 0.993 | 63.533 | 7.945 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29140) rss_mb | MB | 14 | 369.351 | 236.488 | 392.562 | 392.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29140) main thread run-queue wait | percent | 13 | 3.289 | 0.009 | 18.308 | 0.024 | 0.438224 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29140) vms_mb | MB | 14 | 8988.905 | 1637.305 | 10213.738 | 10213.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29172) CPU | percent | 1 | 58.574 | 58.574 | 58.574 | 58.574 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29172) rss_mb | MB | 2 | 205.719 | 151.582 | 259.855 | 259.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29172) main thread run-queue wait | percent | 1 | 16.644 | 16.644 | 16.644 | 16.644 | 0.167645 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29172) vms_mb | MB | 2 | 1577.549 | 1499.219 | 1655.879 | 1655.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29203) CPU | percent | 12 | 22.496 | 1.990 | 69.502 | 7.951 | 2.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29203) rss_mb | MB | 13 | 369.423 | 229.156 | 397.211 | 397.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29203) main thread run-queue wait | percent | 12 | 2.216 | 0.006 | 18.668 | 0.072 | 0.267787 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29203) vms_mb | MB | 13 | 8894.276 | 1632.031 | 10213.812 | 10213.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29227) CPU | percent | 1 | 38.727 | 38.727 | 38.727 | 38.727 | 0.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29227) rss_mb | MB | 2 | 180.549 | 141.277 | 219.820 | 219.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29227) main thread run-queue wait | percent | 1 | 21.872 | 21.872 | 21.872 | 21.872 | 0.220265 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29227) vms_mb | MB | 2 | 1460.818 | 1297.426 | 1624.211 | 1624.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29254) CPU | percent | 17 | 17.170 | 0.994 | 69.445 | 5.965 | 2.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29254) rss_mb | MB | 18 | 374.110 | 188.344 | 398.945 | 398.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29254) main thread run-queue wait | percent | 17 | 1.423 | 0.008 | 10.260 | 0.026 | 0.244016 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29254) vms_mb | MB | 18 | 9255.132 | 1594.219 | 10209.969 | 10209.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29273) CPU | percent | 1 | 52.460 | 52.460 | 52.460 | 52.460 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29273) rss_mb | MB | 2 | 211.938 | 169.199 | 254.676 | 254.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29273) main thread run-queue wait | percent | 1 | 10.645 | 10.645 | 10.645 | 10.645 | 0.107547 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29273) vms_mb | MB | 2 | 1614.283 | 1578.723 | 1649.844 | 1649.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 29298) rss_mb | MB | 1 | 64.930 | 64.930 | 64.930 | 64.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 29298) vms_mb | MB | 1 | 900.188 | 900.188 | 900.188 | 900.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29301) CPU | percent | 12 | 24.184 | 0.994 | 80.534 | 0.995 | 2.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29301) rss_mb | MB | 13 | 361.389 | 160.441 | 395.949 | 395.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29301) main thread run-queue wait | percent | 12 | 2.141 | 0.008 | 12.330 | 0.011 | 0.258598 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29301) vms_mb | MB | 13 | 8882.843 | 1500.465 | 10212.625 | 10212.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git (PID 29323) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git (PID 29323) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29329) CPU | percent | 1 | 71.573 | 71.573 | 71.573 | 71.573 | 0.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29329) rss_mb | MB | 2 | 231.662 | 167.188 | 296.137 | 296.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29329) main thread run-queue wait | percent | 1 | 17.068 | 17.068 | 17.068 | 17.068 | 0.171695 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29329) vms_mb | MB | 2 | 1634.344 | 1578.223 | 1690.465 | 1690.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29351) CPU | percent | 12 | 21.342 | 0.995 | 76.374 | 1.988 | 2.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29351) rss_mb | MB | 13 | 370.556 | 237.082 | 395.391 | 395.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29351) main thread run-queue wait | percent | 12 | 2.479 | 0.012 | 26.194 | 0.026 | 0.299996 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29351) vms_mb | MB | 13 | 8895.876 | 1637.508 | 10213.387 | 10213.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — stty (PID 29369) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — stty (PID 29369) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29375) CPU | percent | 1 | 44.613 | 44.613 | 44.613 | 44.613 | 0.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29375) rss_mb | MB | 2 | 194.529 | 154.309 | 234.750 | 234.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29375) main thread run-queue wait | percent | 1 | 21.315 | 21.315 | 21.315 | 21.315 | 0.214999 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29375) vms_mb | MB | 2 | 1567.426 | 1499.469 | 1635.383 | 1635.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29401) CPU | percent | 11 | 21.480 | 1.988 | 77.448 | 2.982 | 2.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29401) rss_mb | MB | 12 | 374.114 | 268.223 | 399.320 | 399.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29401) main thread run-queue wait | percent | 11 | 1.636 | 0.010 | 14.298 | 0.014 | 0.181355 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29401) vms_mb | MB | 12 | 8800.842 | 1664.012 | 10213.547 | 10213.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29422) CPU | percent | 1 | 55.555 | 55.555 | 55.555 | 55.555 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29422) rss_mb | MB | 2 | 225.986 | 179.805 | 272.168 | 272.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29422) main thread run-queue wait | percent | 1 | 14.739 | 14.739 | 14.739 | 14.739 | 0.148574 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29422) vms_mb | MB | 2 | 1629.135 | 1590.973 | 1667.297 | 1667.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29448) CPU | percent | 12 | 20.950 | 0.994 | 73.601 | 0.994 | 2.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29448) rss_mb | MB | 13 | 368.877 | 236.066 | 391.898 | 391.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29448) main thread run-queue wait | percent | 12 | 1.634 | 0.005 | 13.020 | 0.015 | 0.197553 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29448) vms_mb | MB | 13 | 8894.707 | 1637.531 | 10207.770 | 10207.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29470) CPU | percent | 1 | 46.629 | 46.629 | 46.629 | 46.629 | 0.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29470) rss_mb | MB | 2 | 211.580 | 169.574 | 253.586 | 253.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29470) main thread run-queue wait | percent | 1 | 14.256 | 14.256 | 14.256 | 14.256 | 0.143694 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29470) vms_mb | MB | 2 | 1614.025 | 1578.723 | 1649.328 | 1649.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29478) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29478) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29479) rss_mb | MB | 1 | 9.746 | 9.746 | 9.746 | 9.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29479) vms_mb | MB | 1 | 13.734 | 13.734 | 13.734 | 13.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29496) CPU | percent | 13 | 23.777 | 0.994 | 84.479 | 5.968 | 3.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29496) rss_mb | MB | 14 | 354.297 | 69.211 | 392.715 | 392.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29496) main thread run-queue wait | percent | 13 | 1.072 | 0.012 | 9.037 | 0.029 | 0.140130 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29496) vms_mb | MB | 14 | 8952.607 | 1238.512 | 10213.188 | 10213.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29525) rss_mb | MB | 1 | 187.570 | 187.570 | 187.570 | 187.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29525) vms_mb | MB | 1 | 1593.973 | 1593.973 | 1593.973 | 1593.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29544) CPU | percent | 14 | 19.785 | 0.994 | 65.481 | 3.976 | 2.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29544) rss_mb | MB | 15 | 370.148 | 197.383 | 394.715 | 394.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29544) main thread run-queue wait | percent | 14 | 2.352 | 0.004 | 19.788 | 0.165 | 0.332167 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29544) vms_mb | MB | 15 | 9069.179 | 1616.789 | 10213.875 | 10213.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29565) CPU | percent | 1 | 36.678 | 36.678 | 36.678 | 36.678 | 0.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29565) rss_mb | MB | 2 | 140.719 | 76.223 | 205.215 | 205.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29565) main thread run-queue wait | percent | 1 | 17.971 | 17.971 | 17.971 | 17.971 | 0.181291 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29565) vms_mb | MB | 2 | 1451.219 | 1283.695 | 1618.742 | 1618.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29572) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29572) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29573) rss_mb | MB | 1 | 6.191 | 6.191 | 6.191 | 6.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29573) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29591) CPU | percent | 14 | 21.424 | 0.993 | 79.465 | 7.928 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29591) rss_mb | MB | 15 | 365.377 | 172.727 | 392.844 | 392.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29591) main thread run-queue wait | percent | 14 | 2.059 | 0.004 | 13.370 | 0.024 | 0.290536 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29591) vms_mb | MB | 15 | 9065.464 | 1579.719 | 10214.191 | 10214.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29611) CPU | percent | 1 | 60.576 | 60.576 | 60.576 | 60.576 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29611) rss_mb | MB | 2 | 220.471 | 168.977 | 271.965 | 271.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29611) main thread run-queue wait | percent | 1 | 11.217 | 11.217 | 11.217 | 11.217 | 0.112953 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29611) vms_mb | MB | 2 | 1622.766 | 1578.723 | 1666.809 | 1666.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29623) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29623) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29624) rss_mb | MB | 1 | 6.898 | 6.898 | 6.898 | 6.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29624) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29639) CPU | percent | 14 | 19.287 | 0.995 | 70.497 | 1.989 | 2.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29639) rss_mb | MB | 15 | 370.572 | 222.805 | 396.125 | 396.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29639) main thread run-queue wait | percent | 14 | 2.621 | 0.004 | 20.418 | 0.010 | 0.369815 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29639) vms_mb | MB | 15 | 9071.541 | 1625.535 | 10214.246 | 10214.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29659) CPU | percent | 1 | 58.523 | 58.523 | 58.523 | 58.523 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29659) rss_mb | MB | 2 | 239.809 | 193.953 | 285.664 | 285.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29659) main thread run-queue wait | percent | 1 | 21.625 | 21.625 | 21.625 | 21.625 | 0.218008 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29659) vms_mb | MB | 2 | 1647.812 | 1614.723 | 1680.902 | 1680.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29688) CPU | percent | 12 | 25.483 | 1.986 | 82.492 | 4.974 | 3.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29688) rss_mb | MB | 13 | 356.278 | 90.453 | 396.477 | 396.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29688) main thread run-queue wait | percent | 12 | 1.345 | 0.007 | 6.786 | 0.017 | 0.162553 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29688) vms_mb | MB | 13 | 8857.440 | 1283.598 | 10210.379 | 10210.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29718) rss_mb | MB | 1 | 235.324 | 235.324 | 235.324 | 235.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29718) vms_mb | MB | 1 | 1635.590 | 1635.590 | 1635.590 | 1635.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29732) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29732) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29733) rss_mb | MB | 1 | 7.914 | 7.914 | 7.914 | 7.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29733) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29737) CPU | percent | 12 | 24.641 | 0.994 | 75.386 | 2.982 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29737) rss_mb | MB | 13 | 362.436 | 183.199 | 397.625 | 397.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29737) main thread run-queue wait | percent | 12 | 3.381 | 0.002 | 15.403 | 0.021 | 0.409237 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29737) vms_mb | MB | 13 | 8889.974 | 1593.219 | 10217.473 | 10217.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29755) CPU | percent | 1 | 61.404 | 61.404 | 61.404 | 61.404 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29755) rss_mb | MB | 2 | 257.443 | 211.797 | 303.090 | 303.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29755) main thread run-queue wait | percent | 1 | 15.793 | 15.793 | 15.793 | 15.793 | 0.159469 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29755) vms_mb | MB | 2 | 1674.906 | 1622.480 | 1727.332 | 1727.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29763) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29763) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29764) rss_mb | MB | 1 | 7.367 | 7.367 | 7.367 | 7.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29764) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29767) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29767) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 29778) rss_mb | MB | 1 | 2.035 | 2.035 | 2.035 | 2.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 29778) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 29779) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 29779) vms_mb | MB | 1 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29785) CPU | percent | 14 | 22.259 | 1.988 | 82.420 | 6.960 | 3.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29785) rss_mb | MB | 15 | 368.061 | 137.906 | 402.188 | 401.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29785) main thread run-queue wait | percent | 14 | 1.853 | 0.008 | 17.011 | 0.039 | 0.261464 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29785) vms_mb | MB | 15 | 9045.218 | 1296.254 | 10216.957 | 10215.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29813) rss_mb | MB | 1 | 182.613 | 182.613 | 182.613 | 182.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29813) vms_mb | MB | 1 | 1592.723 | 1592.723 | 1592.723 | 1592.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29835) CPU | percent | 15 | 19.048 | 0.995 | 64.545 | 4.972 | 2.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29835) rss_mb | MB | 16 | 375.305 | 228.758 | 400.102 | 399.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29835) main thread run-queue wait | percent | 15 | 2.478 | 0.009 | 14.738 | 0.015 | 0.375102 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29835) vms_mb | MB | 16 | 9136.701 | 1632.020 | 10212.176 | 10211.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29854) CPU | percent | 2 | 53.975 | 49.475 | 58.475 | 49.475 | 1.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29854) rss_mb | MB | 3 | 199.979 | 66.230 | 303.949 | 303.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29854) main thread run-queue wait | percent | 2 | 12.972 | 10.542 | 15.401 | 10.542 | 0.261938 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29854) vms_mb | MB | 3 | 1533.243 | 1238.609 | 1728.395 | 1728.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29868) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29868) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29869) rss_mb | MB | 1 | 9.840 | 9.840 | 9.840 | 9.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29869) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29883) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29883) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29884) rss_mb | MB | 1 | 9.270 | 9.270 | 9.270 | 9.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29884) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29888) CPU | percent | 14 | 21.157 | 1.989 | 74.559 | 6.961 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29888) rss_mb | MB | 15 | 366.861 | 184.594 | 394.863 | 394.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29888) main thread run-queue wait | percent | 14 | 1.392 | 0.006 | 9.198 | 0.031 | 0.199705 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29888) vms_mb | MB | 15 | 9063.747 | 1592.969 | 10207.730 | 10207.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git (PID 29908) rss_mb | MB | 1 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git (PID 29908) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29919) rss_mb | MB | 1 | 229.918 | 229.918 | 229.918 | 229.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29919) vms_mb | MB | 1 | 1631.961 | 1631.961 | 1631.961 | 1631.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29938) CPU | percent | 13 | 23.903 | 0.995 | 68.465 | 0.995 | 3.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29938) rss_mb | MB | 14 | 366.218 | 193.027 | 393.898 | 393.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29938) main thread run-queue wait | percent | 13 | 2.417 | 0.006 | 12.564 | 0.015 | 0.334830 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29938) vms_mb | MB | 14 | 8988.124 | 1598.219 | 10217.508 | 10217.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29960) CPU | percent | 1 | 42.427 | 42.427 | 42.427 | 42.427 | 0.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29960) rss_mb | MB | 2 | 136.314 | 61.555 | 211.074 | 211.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29960) main thread run-queue wait | percent | 1 | 9.369 | 9.369 | 9.369 | 9.369 | 0.094951 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29960) vms_mb | MB | 2 | 1430.664 | 1238.609 | 1622.719 | 1622.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29989) CPU | percent | 11 | 22.217 | 0.994 | 76.481 | 2.983 | 2.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29989) rss_mb | MB | 12 | 372.573 | 255.395 | 397.895 | 397.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29989) main thread run-queue wait | percent | 11 | 2.153 | 0.007 | 16.774 | 0.009 | 0.238462 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29989) vms_mb | MB | 12 | 8785.351 | 1651.543 | 10210.402 | 10210.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30013) CPU | percent | 1 | 45.665 | 45.665 | 45.665 | 45.665 | 0.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30013) rss_mb | MB | 2 | 203.135 | 166.285 | 239.984 | 239.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30013) main thread run-queue wait | percent | 1 | 12.928 | 12.928 | 12.928 | 12.928 | 0.130223 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30013) vms_mb | MB | 2 | 1608.029 | 1577.723 | 1638.336 | 1638.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -m agency.harness.daemon (PID 30039) CPU | percent | 16 | 20.246 | 0.994 | 86.364 | 1.986 | 3.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -m agency.harness.daemon (PID 30039) rss_mb | MB | 17 | 370.462 | 157.680 | 401.305 | 401.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -m agency.harness.daemon (PID 30039) main thread run-queue wait | percent | 16 | 2.396 | 0.004 | 13.339 | 0.006 | 0.387719 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -m agency.harness.daemon (PID 30039) vms_mb | MB | 17 | 9156.641 | 976.695 | 10216.340 | 10216.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30056) CPU | percent | 1 | 62.528 | 62.528 | 62.528 | 62.528 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30056) rss_mb | MB | 2 | 237.066 | 187.305 | 286.828 | 286.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30056) main thread run-queue wait | percent | 1 | 15.328 | 15.328 | 15.328 | 15.328 | 0.154433 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30056) vms_mb | MB | 2 | 1637.893 | 1593.723 | 1682.062 | 1682.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30087) CPU | percent | 11 | 21.166 | 1.988 | 78.519 | 4.974 | 2.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30087) rss_mb | MB | 12 | 373.302 | 262.855 | 397.539 | 397.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30087) main thread run-queue wait | percent | 11 | 1.460 | 0.007 | 11.419 | 0.016 | 0.172484 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30087) vms_mb | MB | 12 | 8798.444 | 1657.836 | 10212.285 | 10212.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30112) rss_mb | MB | 1 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30112) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30113) rss_mb | MB | 1 | 9.762 | 9.762 | 9.762 | 9.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30113) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30115) CPU | percent | 1 | 49.948 | 49.948 | 49.948 | 49.948 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30115) rss_mb | MB | 2 | 189.051 | 140.070 | 238.031 | 238.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30115) main thread run-queue wait | percent | 1 | 12.747 | 12.747 | 12.747 | 12.747 | 0.140367 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30115) vms_mb | MB | 2 | 1467.223 | 1296.352 | 1638.094 | 1638.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30131) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30131) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30132) rss_mb | MB | 1 | 11.020 | 11.020 | 11.020 | 11.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30132) vms_mb | MB | 1 | 14.730 | 14.730 | 14.730 | 14.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30136) CPU | percent | 12 | 24.678 | 0.994 | 83.344 | 2.985 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30136) rss_mb | MB | 13 | 366.415 | 167.879 | 401.938 | 401.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30136) main thread run-queue wait | percent | 12 | 2.136 | 0.005 | 9.525 | 0.024 | 0.259928 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30136) vms_mb | MB | 13 | 8886.307 | 1578.469 | 10217.672 | 10217.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30155) CPU | percent | 1 | 54.470 | 54.470 | 54.470 | 54.470 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30155) rss_mb | MB | 2 | 213.400 | 166.414 | 260.387 | 260.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30155) main thread run-queue wait | percent | 1 | 11.579 | 11.579 | 11.579 | 11.579 | 0.119037 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30155) vms_mb | MB | 2 | 1616.791 | 1577.973 | 1655.609 | 1655.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30168) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30168) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30169) rss_mb | MB | 1 | 6.910 | 6.910 | 6.910 | 6.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30169) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30202) CPU | percent | 13 | 18.947 | 0.995 | 80.548 | 1.990 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30202) rss_mb | MB | 14 | 379.405 | 274.035 | 402.121 | 401.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30202) main thread run-queue wait | percent | 13 | 2.538 | 0.004 | 18.026 | 0.016 | 0.332265 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30202) vms_mb | MB | 14 | 9587.754 | 1669.004 | 10216.215 | 10215.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30220) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30220) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30221) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30221) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30222) CPU | percent | 1 | 55.649 | 55.649 | 55.649 | 55.649 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30222) rss_mb | MB | 2 | 259.045 | 221.805 | 296.285 | 296.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30222) main thread run-queue wait | percent | 1 | 12.631 | 12.631 | 12.631 | 12.631 | 0.127104 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30222) vms_mb | MB | 2 | 1657.631 | 1624.258 | 1691.004 | 1691.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30253) CPU | percent | 15 | 20.062 | 0.994 | 77.401 | 0.995 | 3.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30253) rss_mb | MB | 16 | 369.300 | 167.352 | 398.887 | 398.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30253) main thread run-queue wait | percent | 15 | 2.664 | 0.002 | 14.122 | 0.002 | 0.402328 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30253) vms_mb | MB | 16 | 9133.879 | 1577.969 | 10213.945 | 10213.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30273) CPU | percent | 1 | 60.504 | 60.504 | 60.504 | 60.504 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30273) rss_mb | MB | 2 | 251.645 | 208.500 | 294.789 | 294.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30273) main thread run-queue wait | percent | 1 | 9.898 | 9.898 | 9.898 | 9.898 | 0.099790 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30273) vms_mb | MB | 2 | 1654.367 | 1619.699 | 1689.035 | 1689.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30304) CPU | percent | 13 | 18.300 | 1.985 | 80.551 | 6.964 | 2.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30304) rss_mb | MB | 14 | 375.696 | 279.098 | 393.742 | 393.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30304) main thread run-queue wait | percent | 13 | 1.547 | 0.006 | 16.779 | 0.022 | 0.204848 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30304) vms_mb | MB | 14 | 9588.225 | 1673.836 | 10214.836 | 10214.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30327) CPU | percent | 1 | 52.889 | 52.889 | 52.889 | 52.889 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30327) rss_mb | MB | 2 | 217.389 | 175.203 | 259.574 | 259.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30327) main thread run-queue wait | percent | 1 | 15.133 | 15.133 | 15.133 | 15.133 | 0.154509 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30327) vms_mb | MB | 2 | 1622.773 | 1590.223 | 1655.324 | 1655.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30337) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30337) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30338) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30338) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30351) CPU | percent | 12 | 23.839 | 0.995 | 75.384 | 1.989 | 2.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30351) rss_mb | MB | 13 | 363.042 | 169.730 | 396.402 | 396.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30351) main thread run-queue wait | percent | 12 | 1.282 | 0.006 | 5.960 | 0.020 | 0.155030 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30351) vms_mb | MB | 13 | 8889.584 | 1578.719 | 10213.258 | 10213.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30379) CPU | percent | 1 | 80.354 | 80.354 | 80.354 | 80.354 | 0.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30379) rss_mb | MB | 2 | 225.006 | 147.848 | 302.164 | 302.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30379) main thread run-queue wait | percent | 1 | 6.023 | 6.023 | 6.023 | 6.023 | 0.060713 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30379) vms_mb | MB | 2 | 1579.582 | 1432.312 | 1726.852 | 1726.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30400) CPU | percent | 14 | 22.205 | 0.994 | 82.485 | 4.974 | 3.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30400) rss_mb | MB | 15 | 363.282 | 121.801 | 399.285 | 399.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30400) main thread run-queue wait | percent | 14 | 1.808 | 0.007 | 14.144 | 0.011 | 0.266401 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30400) vms_mb | MB | 15 | 9039.488 | 1296.254 | 10213.727 | 10213.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30423) CPU | percent | 1 | 56.907 | 56.907 | 56.907 | 56.907 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30423) rss_mb | MB | 2 | 238.020 | 187.227 | 288.812 | 288.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30423) main thread run-queue wait | percent | 1 | 14.987 | 14.987 | 14.987 | 14.987 | 0.163279 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30423) vms_mb | MB | 2 | 1638.900 | 1594.223 | 1683.578 | 1683.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30433) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30433) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30434) rss_mb | MB | 1 | 7.980 | 7.980 | 7.980 | 7.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30434) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30444) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30444) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30445) rss_mb | MB | 1 | 7.641 | 7.641 | 7.641 | 7.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30445) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30449) CPU | percent | 13 | 22.762 | 0.994 | 79.482 | 1.988 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30449) rss_mb | MB | 14 | 365.831 | 172.727 | 397.602 | 397.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30449) main thread run-queue wait | percent | 13 | 2.551 | 0.009 | 12.913 | 0.014 | 0.334494 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30449) vms_mb | MB | 14 | 8981.928 | 1579.969 | 10214.199 | 10214.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30468) CPU | percent | 1 | 53.493 | 53.493 | 53.493 | 53.493 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30468) rss_mb | MB | 2 | 215.590 | 170.309 | 260.871 | 260.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30468) main thread run-queue wait | percent | 1 | 13.257 | 13.257 | 13.257 | 13.257 | 0.133822 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30468) vms_mb | MB | 2 | 1617.516 | 1579.223 | 1655.809 | 1655.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30482) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30482) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30483) rss_mb | MB | 1 | 7.395 | 7.395 | 7.395 | 7.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30483) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30498) CPU | percent | 12 | 21.257 | 0.994 | 74.518 | 0.994 | 2.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30498) rss_mb | MB | 13 | 375.723 | 237.254 | 402.016 | 402.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30498) main thread run-queue wait | percent | 12 | 1.702 | 0.004 | 16.590 | 0.004 | 0.205780 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30498) vms_mb | MB | 13 | 8898.852 | 1637.520 | 10216.039 | 10216.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30539) CPU | percent | 14 | 19.283 | 0.994 | 73.522 | 6.963 | 2.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30539) rss_mb | MB | 15 | 376.898 | 235.871 | 400.719 | 400.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30539) main thread run-queue wait | percent | 14 | 1.839 | 0.007 | 18.610 | 0.045 | 0.259586 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30539) vms_mb | MB | 15 | 9072.502 | 1637.039 | 10215.855 | 10215.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30559) CPU | percent | 1 | 56.513 | 56.513 | 56.513 | 56.513 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30559) rss_mb | MB | 2 | 247.008 | 205.117 | 288.898 | 288.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30559) main thread run-queue wait | percent | 1 | 15.188 | 15.188 | 15.188 | 15.188 | 0.153190 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30559) vms_mb | MB | 2 | 1651.121 | 1618.703 | 1683.539 | 1683.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30590) CPU | percent | 14 | 20.635 | 0.995 | 66.558 | 2.984 | 2.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30590) rss_mb | MB | 15 | 371.920 | 193.371 | 402.453 | 402.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30590) main thread run-queue wait | percent | 14 | 2.102 | 0.008 | 18.277 | 0.025 | 0.296721 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30590) vms_mb | MB | 15 | 9069.223 | 1614.719 | 10215.715 | 10215.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30611) CPU | percent | 1 | 59.492 | 59.492 | 59.492 | 59.492 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30611) rss_mb | MB | 2 | 217.574 | 174.664 | 260.484 | 260.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30611) main thread run-queue wait | percent | 1 | 14.912 | 14.912 | 14.912 | 14.912 | 0.150395 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30611) vms_mb | MB | 2 | 1619.641 | 1581.973 | 1657.309 | 1657.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30642) CPU | percent | 14 | 22.922 | 0.995 | 86.412 | 2.967 | 3.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30642) rss_mb | MB | 15 | 354.714 | 35.742 | 397.551 | 397.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30642) main thread run-queue wait | percent | 14 | 2.129 | 0.006 | 9.629 | 0.026 | 0.299999 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30642) vms_mb | MB | 15 | 9029.493 | 1169.414 | 10216.375 | 10216.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30661) CPU | percent | 1 | 62.572 | 62.572 | 62.572 | 62.572 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30661) rss_mb | MB | 2 | 238.312 | 189.605 | 287.020 | 287.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30661) main thread run-queue wait | percent | 1 | 10.679 | 10.679 | 10.679 | 10.679 | 0.107517 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30661) vms_mb | MB | 2 | 1638.148 | 1594.473 | 1681.824 | 1681.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30694) CPU | percent | 17 | 18.228 | 0.993 | 81.366 | 6.953 | 3.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30694) rss_mb | MB | 18 | 371.258 | 158.520 | 398.004 | 397.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30694) main thread run-queue wait | percent | 17 | 1.474 | 0.003 | 9.860 | 0.028 | 0.261294 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30694) vms_mb | MB | 18 | 9253.143 | 1499.965 | 10215.598 | 10214.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 30713) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 30713) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30716) rss_mb | MB | 1 | 229.117 | 229.117 | 229.117 | 229.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30716) vms_mb | MB | 1 | 1632.238 | 1632.238 | 1632.238 | 1632.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30746) CPU | percent | 13 | 21.140 | 0.994 | 69.517 | 5.969 | 2.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30746) rss_mb | MB | 14 | 370.164 | 227.621 | 396.777 | 396.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30746) main thread run-queue wait | percent | 13 | 2.341 | 0.005 | 15.431 | 0.022 | 0.306610 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30746) vms_mb | MB | 14 | 8989.035 | 1630.270 | 10213.859 | 10213.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30769) CPU | percent | 1 | 34.730 | 34.730 | 34.730 | 34.730 | 0.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30769) rss_mb | MB | 2 | 187.471 | 157.664 | 217.277 | 217.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30769) main thread run-queue wait | percent | 1 | 14.175 | 14.175 | 14.175 | 14.175 | 0.142850 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30769) vms_mb | MB | 2 | 1469.178 | 1314.887 | 1623.469 | 1623.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30795) CPU | percent | 13 | 20.264 | 0.993 | 79.496 | 0.993 | 2.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30795) rss_mb | MB | 14 | 361.497 | 170.371 | 392.906 | 392.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30795) main thread run-queue wait | percent | 13 | 2.319 | 0.002 | 13.666 | 0.016 | 0.309331 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30795) vms_mb | MB | 14 | 8958.443 | 1579.219 | 10186.555 | 10186.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30812) CPU | percent | 1 | 58.385 | 58.385 | 58.385 | 58.385 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30812) rss_mb | MB | 2 | 217.592 | 172.969 | 262.215 | 262.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30812) main thread run-queue wait | percent | 1 | 14.496 | 14.496 | 14.496 | 14.496 | 0.146486 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30812) vms_mb | MB | 2 | 1618.531 | 1579.723 | 1657.340 | 1657.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30827) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30827) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30828) rss_mb | MB | 1 | 9.859 | 9.859 | 9.859 | 9.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30828) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30841) CPU | percent | 14 | 22.630 | 0.993 | 86.405 | 5.967 | 3.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30841) rss_mb | MB | 15 | 358.404 | 48.797 | 400.398 | 400.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30841) main thread run-queue wait | percent | 14 | 1.835 | 0.001 | 12.936 | 0.029 | 0.258826 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30841) vms_mb | MB | 15 | 9034.770 | 1238.512 | 10214.160 | 10214.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30861) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30861) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30862) rss_mb | MB | 1 | 9.707 | 9.707 | 9.707 | 9.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30862) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30863) CPU | percent | 2 | 50.098 | 42.677 | 57.519 | 42.677 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30863) rss_mb | MB | 3 | 223.016 | 131.742 | 300.086 | 300.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30863) main thread run-queue wait | percent | 2 | 11.517 | 6.970 | 16.063 | 16.063 | 0.232131 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30863) vms_mb | MB | 3 | 1553.177 | 1296.352 | 1725.336 | 1725.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30892) CPU | percent | 13 | 22.001 | 0.994 | 68.501 | 5.971 | 2.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30892) rss_mb | MB | 14 | 370.179 | 194.113 | 398.688 | 398.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30892) main thread run-queue wait | percent | 13 | 1.565 | 0.010 | 14.065 | 0.043 | 0.204934 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30892) vms_mb | MB | 14 | 8989.783 | 1614.469 | 10216.395 | 10216.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30928) CPU | percent | 186 | 4.677 | 0.000 | 72.409 | 8.953 | 8.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30928) rss_mb | MB | 187 | 387.947 | 189.176 | 406.070 | 389.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30928) main thread run-queue wait | percent | 186 | 0.589 | 0.002 | 17.111 | 0.020 | 1.116935 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30928) vms_mb | MB | 187 | 10113.963 | 1594.469 | 10219.965 | 10211.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30948) CPU | percent | 1 | 63.962 | 63.962 | 63.962 | 63.962 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30948) rss_mb | MB | 2 | 217.881 | 165.055 | 270.707 | 270.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30948) main thread run-queue wait | percent | 1 | 14.680 | 14.680 | 14.680 | 14.680 | 0.149184 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30948) vms_mb | MB | 2 | 1619.260 | 1572.973 | 1665.547 | 1665.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 30956) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 30956) vms_mb | MB | 1 | 4.035 | 4.035 | 4.035 | 4.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30990) rss_mb | MB | 1 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30990) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 30991) rss_mb | MB | 1 | 2339.531 | 2339.531 | 2339.531 | 2339.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 30991) vms_mb | MB | 1 | 2657.141 | 2657.141 | 2657.141 | 2657.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31025) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31025) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31026) rss_mb | MB | 1 | 14.680 | 14.680 | 14.680 | 14.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31026) vms_mb | MB | 1 | 20.082 | 20.082 | 20.082 | 20.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31037) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31037) rss_mb | MB | 3 | 2.551 | 2.551 | 2.551 | 2.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31037) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31037) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31038) CPU | percent | 2 | 31.271 | 0.000 | 62.542 | 0.000 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31038) rss_mb | MB | 3 | 54.626 | 31.277 | 66.363 | 66.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31038) main thread run-queue wait | percent | 2 | 0.110 | 0.030 | 0.191 | 0.030 | 0.002226 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31038) vms_mb | MB | 3 | 67.022 | 41.125 | 80.102 | 80.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31039) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31039) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31040) rss_mb | MB | 1 | 7.895 | 7.895 | 7.895 | 7.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31040) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31044) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31044) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python3 (PID 31045) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python3 (PID 31045) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31059) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31059) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31060) rss_mb | MB | 1 | 21.359 | 21.359 | 21.359 | 21.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31060) vms_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31066) rss_mb | MB | 1 | 2.738 | 2.738 | 2.738 | 2.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31066) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31067) rss_mb | MB | 1 | 2279.422 | 2279.422 | 2279.422 | 2279.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31067) vms_mb | MB | 1 | 2655.004 | 2655.004 | 2655.004 | 2655.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31088) CPU | percent | 7 | 90.068 | 51.534 | 100.469 | 80.580 | 6.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31088) rss_mb | MB | 8 | 1.500 | 1.309 | 2.844 | 1.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31088) main thread run-queue wait | percent | 7 | 0.004 | 0.003 | 0.006 | 0.006 | 0.000276 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31088) vms_mb | MB | 8 | 2.634 | 2.461 | 3.848 | 2.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31089) rss_mb | MB | 1 | 13.898 | 13.898 | 13.898 | 13.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31089) vms_mb | MB | 1 | 207.594 | 207.594 | 207.594 | 207.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31098) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31098) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31099) rss_mb | MB | 1 | 8.289 | 8.289 | 8.289 | 8.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31099) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31114) rss_mb | MB | 1 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31114) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31115) rss_mb | MB | 1 | 79.328 | 79.328 | 79.328 | 79.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31115) vms_mb | MB | 1 | 303.590 | 303.590 | 303.590 | 303.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31132) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31132) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31133) rss_mb | MB | 1 | 20.859 | 20.859 | 20.859 | 20.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31133) vms_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31139) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31139) rss_mb | MB | 3 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31139) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31139) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31140) CPU | percent | 2 | 107.162 | 100.324 | 114.001 | 100.324 | 2.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31140) rss_mb | MB | 3 | 990.182 | 8.781 | 1745.883 | 1745.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31140) main thread run-queue wait | percent | 2 | 5.289 | 0.004 | 10.573 | 0.004 | 0.106697 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31140) vms_mb | MB | 3 | 1317.513 | 13.297 | 1969.621 | 1969.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31158) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31158) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31159) rss_mb | MB | 1 | 43.824 | 43.824 | 43.824 | 43.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31159) vms_mb | MB | 1 | 52.672 | 52.672 | 52.672 | 52.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31161) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31161) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31162) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31162) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31168) rss_mb | MB | 1 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31168) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31169) rss_mb | MB | 1 | 45.273 | 45.273 | 45.273 | 45.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31169) vms_mb | MB | 1 | 53.426 | 53.426 | 53.426 | 53.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31170) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31170) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31171) rss_mb | MB | 1 | 9.848 | 9.848 | 9.848 | 9.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 31171) vms_mb | MB | 1 | 13.844 | 13.844 | 13.844 | 13.844 | n/a | n/a |
| docker commit (PID 31214) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 31214) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 31214) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 31214) rss_mb | MB | 22 | 29.578 | 29.578 | 29.578 | 29.578 | n/a | n/a |
| docker commit (PID 31214) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 31214) vms_mb | MB | 22 | 1771.195 | 1771.195 | 1771.195 | 1771.195 | n/a | n/a |
| docker inspect (PID 31331) rss_mb | MB | 1 | 21.965 | 21.965 | 21.965 | 21.965 | n/a | n/a |
| docker inspect (PID 31331) vms_mb | MB | 1 | 1625.848 | 1625.848 | 1625.848 | 1625.848 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 CPU | percent | 4665 | 81.063 | 0.000 | 228.729 | 0.000 | 3813.970138 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 4665 | 2.326 | 0.000 | 50.786 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 4665 | 3.612 | 0.000 | 73.719 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io_psi_full_pct | percent of wall time stalled | 4665 | 0.043 | 0.000 | 12.655 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io_psi_some_pct | percent of wall time stalled | 4665 | 0.055 | 0.000 | 12.683 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io read MB/s | MB/s | 4665 | 0.047 | 0.000 | 164.143 | 0.000 | 219.500000 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io write MB/s | MB/s | 4665 | 0.149 | 0.000 | 5.891 | 0.000 | 702.777344 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory | MB | 4666 | 443.018 | 17.434 | 2395.117 | 356.176 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory_psi_full_pct | percent of wall time stalled | 4665 | 0.000 | 0.000 | 0.264 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory_psi_some_pct | percent of wall time stalled | 4665 | 0.000 | 0.000 | 0.264 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 net rx MB/s | MB/s | 4665 | 0.090 | 0.000 | 2.165 | 0.000 | 421.597801 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 net tx MB/s | MB/s | 4665 | 0.001 | 0.000 | 0.014 | 0.000 | 5.658074 MB | n/a |
| workload total CPU | percent | 4674 | 9.243 | 1.430 | 173.261 | 1.993 | 436.350115 CPU seconds | n/a |
| workload total memory | MB | 4675 | 6409.037 | 5265.246 | 7015.574 | 7011.234 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
