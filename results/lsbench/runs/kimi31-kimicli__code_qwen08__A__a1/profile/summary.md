# agprof summary

- Duration: **4891.809 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **493 calls**, 426 succeeded, 67 failed, 0 interrupted, n/a reported retries, 3183.029 s total wait
- Tools: **154/154 completed**, 31 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **484001** at 1.965 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 4885372.815 / 4885372.815 ms |
| LLM latency p50 / p95 | 6195.762 / 11457.526 ms |
| LLM TTFT p50 / p95 | 5396.510 / 10875.092 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 493 total, 426 succeeded, 67 failed, 0 interrupted |
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
| Bash | 79/79 | 51 | 28 | 0 | n/a | n/a |
| Edit | 20/20 | 19 | 1 | 0 | n/a | n/a |
| Glob | 3/3 | 3 | 0 | 0 | n/a | n/a |
| Grep | 6/6 | 4 | 2 | 0 | n/a | n/a |
| Read | 31/31 | 31 | 0 | 0 | n/a | n/a |
| TodoList | 7/7 | 7 | 0 | 0 | n/a | n/a |
| Write | 8/8 | 8 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 6.315% | 150.156% | 309.837 s | 9577.354 MB | 10023.738 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 16894 |  | 4854 | 5.132% | 149.555% | 251.740 s | 3714.260 MB | 4157.602 MB | 16773.401 MB | 17228.809 MB | 9.859375 MB | 1781.933594 MB |
| vllm | 16899 |  | 4854 | 0.120% | 8.899% | 5.880 s | 1782.698 MB | 1783.715 MB | 11022.047 MB | 11024.168 MB | 0.007812 MB | 0.027344 MB |
| lsb_grid_worker | 16886 |  | 4854 | 0.000% | 0.000% | 0.000 s | 3.336 MB | 3.336 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 16934 |  | 4854 | 1.059% | 65.300% | 51.820 s | 2320.816 MB | 2322.055 MB | 21204.086 MB | 21204.102 MB | 0.003906 MB | 0.031250 MB |
| python | 16933 |  | 4854 | 0.000% | 0.000% | 0.000 s | 12.180 MB | 12.180 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| kimi_seq.sh | 1928 |  | 4854 | 0.000% | 0.000% | 0.000 s | 3.270 MB | 3.270 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python3 | 17282 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 59.454% | 65.514% | 1.200 s | 49.279 MB | 77.809 MB | 59.458 MB | 93.059 MB | n/a MB | n/a MB |
| bash | 17276 | sandbox_agent_lsb-kimi_0000_0000 | 4846 | 49.836% | 111.507% | 2434.810 s | 146.073 MB | 178.648 MB | 942.470 MB | 986.137 MB | n/a MB | n/a MB |
| docker-init | 17151 | sandbox_agent_lsb-kimi_0000_0000 | 4846 | 0.002% | 0.995% | 0.090 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 17173 | sandbox_agent_lsb-kimi_0000_0000 | 4846 | 0.002% | 1.986% | 0.110 s | 1.418 MB | 1.418 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| MainThread | 17290 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 186.148 MB | 186.148 MB | 1594.348 MB | 1594.348 MB | n/a MB | n/a MB |
| MainThread | 17307 | sandbox_agent_lsb-kimi_0000_0000 | 143 | 6.265% | 96.439% | 8.960 s | 386.969 MB | 407.660 MB | 10079.049 MB | 10214.766 MB | n/a MB | n/a MB |
| MainThread | 17339 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.360% | 54.360% | 0.550 s | 127.969 MB | 226.633 MB | 951.131 MB | 1630.449 MB | n/a MB | n/a MB |
| python3 | 17338 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.363 MB | 7.363 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 17337 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.344 MB | 1.344 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 17381 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.105 MB | 17.105 MB | 21.000 MB | 21.000 MB | n/a MB | n/a MB |
| bash | 17379 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.684 MB | 2.684 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 17460 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.070 MB | 229.070 MB | 1631.344 MB | 1631.344 MB | n/a MB | n/a MB |
| bash | 17458 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.715 MB | 2.715 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 17488 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17489 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.277 MB | 21.277 MB | 26.980 MB | 26.980 MB | n/a MB | n/a MB |
| rg | 17511 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 5.648 MB | 5.648 MB | n/a MB | n/a MB |
| sh | 17526 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.609 MB | 1.609 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17527 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.785 MB | 8.785 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 17543 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| sh | 17585 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17586 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.441 MB | 21.441 MB | 26.727 MB | 26.727 MB | n/a MB | n/a MB |
| python | 17588 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 61.223 MB | 61.223 MB | 75.887 MB | 75.887 MB | n/a MB | n/a MB |
| bash | 17587 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.820 MB | 2.820 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 17596 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.625 MB | 2.625 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 17597 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 45.207 MB | 45.207 MB | 52.262 MB | 52.262 MB | n/a MB | n/a MB |
| sh | 17603 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17604 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.555 MB | 7.555 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 17606 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 51.852 MB | 51.852 MB | 60.992 MB | 60.992 MB | n/a MB | n/a MB |
| bash | 17605 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.762 MB | 2.762 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 17612 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17613 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.562 MB | 17.562 MB | 23.184 MB | 23.184 MB | n/a MB | n/a MB |
| python | 17616 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 62.094 MB | 62.094 MB | 76.984 MB | 76.984 MB | n/a MB | n/a MB |
| bash | 17615 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.875 MB | 2.875 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 17622 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17623 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.852 MB | 6.852 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python3 | 17630 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.461 MB | 14.461 MB | 19.953 MB | 19.953 MB | n/a MB | n/a MB |
| sh | 17629 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 17664 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 15.663% | 76.330% | 0.790 s | 55.972 MB | 65.137 MB | 69.122 MB | 80.133 MB | n/a MB | n/a MB |
| MainThread | 17693 | sandbox_agent_lsb-kimi_0000_0000 | 39 | 11.311% | 90.193% | 4.340 s | 378.730 MB | 394.676 MB | 9767.685 MB | 10213.371 MB | n/a MB | n/a MB |
| MainThread | 17717 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 45.515% | 45.515% | 0.460 s | 157.191 MB | 224.375 MB | 1455.713 MB | 1627.730 MB | n/a MB | n/a MB |
| sh | 17737 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17738 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.855 MB | 6.855 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 17749 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17750 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.730 MB | 20.730 MB | 25.320 MB | 25.320 MB | n/a MB | n/a MB |
| sh | 17754 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 17786 | sandbox_agent_lsb-kimi_0000_0000 | 73 | 7.445% | 77.383% | 5.400 s | 387.951 MB | 401.113 MB | 10094.174 MB | 10221.137 MB | n/a MB | n/a MB |
| sh | 17809 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi | 17814 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 71.209% | 71.209% | 0.720 s | 119.094 MB | 237.566 MB | 900.688 MB | 1638.094 MB | n/a MB | n/a MB |
| python3 | 17810 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.641 MB | 10.641 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| python3 | 17834 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.047 MB | 9.047 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 17833 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 17840 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17841 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.824 MB | 18.824 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| python | 17884 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.719 MB | 7.719 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| python | 17860 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.895 MB | 11.895 MB | 15.207 MB | 15.207 MB | n/a MB | n/a MB |
| bash | 17893 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 42.704% | 78.465% | 0.860 s | 28.462 MB | 61.984 MB | 35.564 MB | 76.082 MB | n/a MB | n/a MB |
| python | 17896 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 30.734 MB | 30.734 MB | 39.750 MB | 39.750 MB | n/a MB | n/a MB |
| sh | 17984 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 17985 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 17992 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.285 MB | 15.285 MB | 20.500 MB | 20.500 MB | n/a MB | n/a MB |
| sh | 17991 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 18121 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 25.798% | 50.606% | 0.520 s | 56.125 MB | 66.152 MB | 68.273 MB | 80.312 MB | n/a MB | n/a MB |
| bash | 18119 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 21.178% | 63.534% | 0.640 s | 17.281 MB | 60.980 MB | 21.824 MB | 75.754 MB | n/a MB | n/a MB |
| sh | 18142 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| python | 18144 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 6.961% | 6.961% | 0.070 s | 63.518 MB | 65.184 MB | 78.648 MB | 80.102 MB | n/a MB | n/a MB |
| git | 18148 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| python3 | 18150 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.855 MB | 8.855 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 18149 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 18167 | sandbox_agent_lsb-kimi_0000_0000 | 30 | 12.846% | 92.360% | 3.750 s | 368.572 MB | 386.656 MB | 9625.270 MB | 10209.465 MB | n/a MB | n/a MB |
| MainThread | 18195 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 186.219 MB | 186.219 MB | 1593.723 MB | 1593.723 MB | n/a MB | n/a MB |
| sh | 18207 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18208 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.738 MB | 21.738 MB | 26.953 MB | 26.953 MB | n/a MB | n/a MB |
| sh | 18218 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18219 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.535 MB | 7.535 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 18225 | sandbox_agent_lsb-kimi_0000_0000 | 6 | 12.902% | 64.511% | 0.650 s | 58.002 MB | 65.184 MB | 71.520 MB | 80.109 MB | n/a MB | n/a MB |
| MainThread | 18256 | sandbox_agent_lsb-kimi_0000_0000 | 35 | 10.666% | 76.897% | 3.660 s | 377.803 MB | 387.086 MB | 9722.479 MB | 10207.684 MB | n/a MB | n/a MB |
| MainThread | 18284 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.156 MB | 229.156 MB | 1632.016 MB | 1632.016 MB | n/a MB | n/a MB |
| sh | 18298 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18299 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.418 MB | 9.418 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| python | 18303 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 16.369% | 32.738% | 0.330 s | 58.906 MB | 65.777 MB | 71.233 MB | 80.090 MB | n/a MB | n/a MB |
| bash | 18300 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 14.384% | 48.685% | 0.870 s | 34.586 MB | 65.090 MB | 42.884 MB | 80.207 MB | n/a MB | n/a MB |
| python3 | 18322 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.098 MB | 10.098 MB | 13.844 MB | 13.844 MB | n/a MB | n/a MB |
| sh | 18321 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18329 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.652 MB | 9.652 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| sh | 18328 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 18333 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 42.339% | 70.507% | 2.560 s | 340.283 MB | 380.191 MB | 7759.041 MB | 10202.891 MB | n/a MB | n/a MB |
| sh | 18350 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18351 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.195 MB | 10.195 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 18364 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.352 MB | 1.352 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 18354 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 46.602% | 46.602% | 0.470 s | 213.912 MB | 252.852 MB | 1619.525 MB | 1648.828 MB | n/a MB | n/a MB |
| python3 | 18365 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.121 MB | 6.121 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 18378 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 40.172% | 75.411% | 2.430 s | 333.473 MB | 383.324 MB | 7741.732 MB | 10183.984 MB | n/a MB | n/a MB |
| kimi | 18397 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 56.891% | 57.476% | 1.150 s | 177.659 MB | 303.500 MB | 1120.237 MB | 1727.961 MB | n/a MB | n/a MB |
| python3 | 18396 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.441 MB | 8.441 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 18395 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 18425 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 34.574% | 75.497% | 2.790 s | 347.999 MB | 385.117 MB | 8302.436 MB | 10211.148 MB | n/a MB | n/a MB |
| sh | 18442 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18443 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.336 MB | 10.336 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 18449 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18450 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.750 MB | 9.750 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| MainThread | 18454 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 261.504 MB | 261.504 MB | 1656.289 MB | 1656.289 MB | n/a MB | n/a MB |
| sh | 18466 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 18471 | sandbox_agent_lsb-kimi_0000_0000 | 26 | 14.296% | 70.631% | 3.600 s | 375.924 MB | 391.785 MB | 9549.354 MB | 10211.363 MB | n/a MB | n/a MB |
| python3 | 18489 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.660 MB | 8.660 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| kimi | 18490 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 55.032% | 58.513% | 1.110 s | 177.410 MB | 302.629 MB | 1173.298 MB | 1727.539 MB | n/a MB | n/a MB |
| sh | 18488 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18514 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.582 MB | 16.582 MB | 22.180 MB | 22.180 MB | n/a MB | n/a MB |
| sh | 18513 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 18515 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 7.758% | 75.421% | 0.860 s | 29.337 MB | 65.785 MB | 36.243 MB | 80.191 MB | n/a MB | n/a MB |
| python | 18518 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 10.437% | 20.875% | 0.210 s | 59.607 MB | 65.332 MB | 72.212 MB | 80.141 MB | n/a MB | n/a MB |
| python | 18520 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 24.349% | 48.698% | 0.490 s | 56.531 MB | 65.438 MB | 69.470 MB | 80.270 MB | n/a MB | n/a MB |
| MainThread | 18534 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 18.811% | 66.622% | 2.840 s | 370.419 MB | 389.340 MB | 9660.180 MB | 10210.691 MB | n/a MB | n/a MB |
| MainThread | 18553 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.518% | 61.518% | 0.620 s | 213.553 MB | 260.211 MB | 1616.893 MB | 1655.812 MB | n/a MB | n/a MB |
| python | 18579 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.582 MB | 21.582 MB | 213.828 MB | 213.828 MB | n/a MB | n/a MB |
| bash | 18578 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.777 MB | 2.777 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 18594 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.736% | 75.403% | 2.630 s | 365.429 MB | 388.207 MB | 8785.408 MB | 10209.160 MB | n/a MB | n/a MB |
| kimi-code | 18610 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.543 MB | 17.543 MB | 706.863 MB | 706.863 MB | n/a MB | n/a MB |
| MainThread | 18622 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 92.394% | 92.394% | 0.930 s | 174.881 MB | 298.238 MB | 1481.348 MB | 1724.086 MB | n/a MB | n/a MB |
| MainThread | 18641 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 29.512% | 68.566% | 2.080 s | 363.550 MB | 387.629 MB | 9127.920 MB | 10210.062 MB | n/a MB | n/a MB |
| sh | 18665 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18666 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.969 MB | 8.969 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| MainThread | 18672 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.137 MB | 229.137 MB | 1631.359 MB | 1631.359 MB | n/a MB | n/a MB |
| MainThread | 18691 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 33.063% | 70.034% | 2.670 s | 351.906 MB | 386.625 MB | 8305.328 MB | 10209.402 MB | n/a MB | n/a MB |
| id | 18705 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.418 MB | 0.418 MB | n/a MB | n/a MB |
| bash | 18704 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.562 MB | 2.562 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 18709 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.398 MB | 8.398 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 18708 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi-code | 18710 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 54.045% | 54.639% | 1.090 s | 188.816 MB | 295.188 MB | 1385.561 MB | 1689.953 MB | n/a MB | n/a MB |
| sh | 18720 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18721 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.195 MB | 10.195 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 18738 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 16.878% | 66.508% | 2.890 s | 373.168 MB | 392.906 MB | 9255.686 MB | 10208.734 MB | n/a MB | n/a MB |
| MainThread | 18757 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.493% | 62.493% | 0.630 s | 202.957 MB | 258.992 MB | 1479.562 MB | 1655.891 MB | n/a MB | n/a MB |
| sh | 18769 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 18770 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.031 MB | 7.031 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 18815 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.140% | 66.543% | 2.120 s | 365.727 MB | 387.484 MB | 9481.236 MB | 10204.719 MB | n/a MB | n/a MB |
| MainThread | 18839 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 205.586 MB | 205.586 MB | 1618.715 MB | 1618.715 MB | n/a MB | n/a MB |
| MainThread | 18865 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 17.805% | 66.543% | 2.150 s | 370.159 MB | 392.785 MB | 8909.231 MB | 10210.836 MB | n/a MB | n/a MB |
| MainThread | 18894 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 174.516 MB | 174.516 MB | 1582.223 MB | 1582.223 MB | n/a MB | n/a MB |
| MainThread | 18913 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 34.925% | 73.500% | 2.460 s | 342.695 MB | 383.805 MB | 8069.781 MB | 10207.730 MB | n/a MB | n/a MB |
| MainThread | 18943 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 234.820 MB | 234.820 MB | 1635.090 MB | 1635.090 MB | n/a MB | n/a MB |
| MainThread | 18962 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 22.654% | 74.831% | 2.430 s | 363.847 MB | 385.855 MB | 9418.891 MB | 10211.297 MB | n/a MB | n/a MB |
| MainThread | 18985 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 193.934 MB | 193.934 MB | 1614.473 MB | 1614.473 MB | n/a MB | n/a MB |
| MainThread | 19009 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.495% | 64.495% | 2.160 s | 367.128 MB | 389.016 MB | 9482.027 MB | 10208.262 MB | n/a MB | n/a MB |
| MainThread | 19029 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.544% | 54.544% | 0.550 s | 212.812 MB | 259.012 MB | 1616.535 MB | 1655.098 MB | n/a MB | n/a MB |
| MainThread | 19057 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 40.677% | 95.260% | 2.870 s | 331.714 MB | 382.949 MB | 8015.969 MB | 10208.539 MB | n/a MB | n/a MB |
| MainThread | 19078 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.533% | 61.533% | 0.620 s | 236.053 MB | 278.152 MB | 1644.105 MB | 1673.738 MB | n/a MB | n/a MB |
| MainThread | 19106 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 20.490% | 61.555% | 2.070 s | 367.018 MB | 387.668 MB | 9418.572 MB | 10207.270 MB | n/a MB | n/a MB |
| MainThread | 19125 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.691% | 64.691% | 0.660 s | 244.889 MB | 294.746 MB | 1651.900 MB | 1689.078 MB | n/a MB | n/a MB |
| MainThread | 19153 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 26.611% | 70.562% | 2.710 s | 353.593 MB | 385.270 MB | 8648.754 MB | 10203.816 MB | n/a MB | n/a MB |
| MainThread | 19260 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 159.141 MB | 159.141 MB | 1315.809 MB | 1315.809 MB | n/a MB | n/a MB |
| sh | 19272 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19273 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.207 MB | 7.207 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 19277 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.783% | 75.417% | 2.590 s | 364.961 MB | 388.609 MB | 8986.377 MB | 10207.141 MB | n/a MB | n/a MB |
| MainThread | 19306 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.270 MB | 229.270 MB | 1631.730 MB | 1631.730 MB | n/a MB | n/a MB |
| MainThread | 19325 | sandbox_agent_lsb-kimi_0000_0000 | 10 | 23.944% | 65.505% | 2.170 s | 362.045 MB | 388.578 MB | 9332.189 MB | 10207.945 MB | n/a MB | n/a MB |
| MainThread | 19346 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.617% | 56.617% | 0.570 s | 206.658 MB | 252.281 MB | 1483.291 MB | 1648.859 MB | n/a MB | n/a MB |
| tar | 19367 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.539 MB | 0.539 MB | 3.609 MB | 3.609 MB | n/a MB | n/a MB |
| MainThread | 19374 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 20.157% | 64.529% | 2.030 s | 369.779 MB | 391.855 MB | 9419.385 MB | 10208.879 MB | n/a MB | n/a MB |
| MainThread | 19393 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.502% | 62.502% | 0.630 s | 229.244 MB | 272.844 MB | 1630.910 MB | 1668.348 MB | n/a MB | n/a MB |
| MainThread | 19422 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 22.577% | 68.489% | 2.500 s | 358.562 MB | 388.297 MB | 8779.534 MB | 10207.062 MB | n/a MB | n/a MB |
| sh | 19441 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19443 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.458% | 65.458% | 0.660 s | 136.729 MB | 236.027 MB | 1403.500 MB | 1636.125 MB | n/a MB | n/a MB |
| python3 | 19442 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.047 MB | 9.047 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| kimi-code | 19455 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 48.289 MB | 48.289 MB | 876.301 MB | 876.301 MB | n/a MB | n/a MB |
| MainThread | 19471 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 25.494% | 92.300% | 2.830 s | 342.311 MB | 389.332 MB | 8733.926 MB | 10204.109 MB | n/a MB | n/a MB |
| MainThread | 19492 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.870% | 56.870% | 0.580 s | 211.381 MB | 259.266 MB | 1613.672 MB | 1654.871 MB | n/a MB | n/a MB |
| python3 | 19514 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.762 MB | 9.762 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| sh | 19513 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19518 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.298% | 71.471% | 2.360 s | 361.720 MB | 385.602 MB | 8785.818 MB | 10208.121 MB | n/a MB | n/a MB |
| MainThread | 19541 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 203.973 MB | 203.973 MB | 1618.953 MB | 1618.953 MB | n/a MB | n/a MB |
| MainThread | 19568 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.367% | 76.557% | 2.370 s | 365.957 MB | 389.590 MB | 9467.655 MB | 10204.871 MB | n/a MB | n/a MB |
| MainThread | 19596 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 166.254 MB | 166.254 MB | 1577.723 MB | 1577.723 MB | n/a MB | n/a MB |
| sh | 19613 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19614 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.707 MB | 8.707 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 19618 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.968% | 73.456% | 2.630 s | 364.687 MB | 385.270 MB | 8987.908 MB | 10206.797 MB | n/a MB | n/a MB |
| MainThread | 19645 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 140.223 MB | 140.223 MB | 1296.918 MB | 1296.918 MB | n/a MB | n/a MB |
| MainThread | 19667 | sandbox_agent_lsb-kimi_0000_0000 | 21 | 15.239% | 73.564% | 3.070 s | 372.216 MB | 388.824 MB | 9392.748 MB | 10209.867 MB | n/a MB | n/a MB |
| bash | 19683 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.605 MB | 1.605 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 19682 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.785 MB | 2.785 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 19687 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.828 MB | 8.828 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 19686 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19688 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 57.528% | 60.465% | 1.160 s | 187.152 MB | 301.520 MB | 1338.318 MB | 1726.410 MB | n/a MB | n/a MB |
| sh | 19700 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19701 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.574 MB | 7.574 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 19712 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.121 MB | 13.121 MB | 207.254 MB | 207.254 MB | n/a MB | n/a MB |
| bash | 19711 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.750 MB | 2.750 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 19729 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 40.707% | 95.414% | 2.870 s | 322.928 MB | 387.676 MB | 8012.529 MB | 10208.727 MB | n/a MB | n/a MB |
| MainThread | 19750 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.470% | 63.470% | 0.640 s | 241.760 MB | 289.031 MB | 1649.398 MB | 1684.074 MB | n/a MB | n/a MB |
| python3 | 19761 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.227 MB | 7.227 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 19760 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19778 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 25.551% | 79.435% | 2.840 s | 358.008 MB | 390.934 MB | 8778.268 MB | 10209.656 MB | n/a MB | n/a MB |
| MainThread | 19801 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.568% | 59.568% | 0.600 s | 212.082 MB | 259.832 MB | 1613.660 MB | 1654.848 MB | n/a MB | n/a MB |
| MainThread | 19825 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 22.111% | 74.579% | 2.460 s | 361.474 MB | 383.828 MB | 8784.700 MB | 10207.957 MB | n/a MB | n/a MB |
| MainThread | 19848 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.849% | 66.849% | 0.690 s | 253.998 MB | 302.379 MB | 1672.885 MB | 1726.566 MB | n/a MB | n/a MB |
| python3 | 19859 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.828 MB | 8.828 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 19858 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 19874 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 27.405% | 86.292% | 2.760 s | 352.105 MB | 390.609 MB | 8648.748 MB | 10208.258 MB | n/a MB | n/a MB |
| sh | 19899 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19900 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| MainThread | 19904 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 221.703 MB | 221.703 MB | 1624.723 MB | 1624.723 MB | n/a MB | n/a MB |
| kimi | 19923 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 26.450% | 93.397% | 2.930 s | 340.136 MB | 388.555 MB | 8653.758 MB | 10207.969 MB | n/a MB | n/a MB |
| sh | 19947 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 19948 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.605 MB | 9.605 MB | 13.578 MB | 13.578 MB | n/a MB | n/a MB |
| MainThread | 19954 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 172.254 MB | 172.254 MB | 1579.723 MB | 1579.723 MB | n/a MB | n/a MB |
| MainThread | 19973 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.154% | 71.563% | 2.120 s | 364.553 MB | 390.164 MB | 8776.610 MB | 10197.688 MB | n/a MB | n/a MB |
| MainThread | 20004 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 290.172 MB | 290.172 MB | 1685.809 MB | 1685.809 MB | n/a MB | n/a MB |
| MainThread | 20024 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 19.910% | 69.256% | 2.210 s | 362.521 MB | 384.699 MB | 8798.002 MB | 10209.250 MB | n/a MB | n/a MB |
| MainThread | 20053 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 242.465 MB | 242.465 MB | 1640.105 MB | 1640.105 MB | n/a MB | n/a MB |
| MainThread | 20091 | sandbox_agent_lsb-kimi_0000_0000 | 24 | 12.397% | 88.375% | 2.880 s | 371.069 MB | 394.883 MB | 9480.487 MB | 10211.367 MB | n/a MB | n/a MB |
| sh | 20117 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.418 MB | 1.418 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 20118 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.719 MB | 7.719 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| MainThread | 20122 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 293.875 MB | 293.875 MB | 1688.418 MB | 1688.418 MB | n/a MB | n/a MB |
| sh | 20143 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 20144 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.590 MB | 21.590 MB | 26.980 MB | 26.980 MB | n/a MB | n/a MB |
| MainThread | 20159 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.186% | 81.374% | 2.510 s | 357.959 MB | 388.227 MB | 8972.707 MB | 10199.410 MB | n/a MB | n/a MB |
| MainThread | 20180 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 212.082 MB | 212.082 MB | 1621.711 MB | 1621.711 MB | n/a MB | n/a MB |
| MainThread | 20208 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.112% | 73.441% | 2.340 s | 360.277 MB | 385.125 MB | 8779.740 MB | 10207.527 MB | n/a MB | n/a MB |
| sh | 20227 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 20229 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.493% | 62.493% | 0.630 s | 135.965 MB | 234.473 MB | 1403.359 MB | 1635.844 MB | n/a MB | n/a MB |
| python3 | 20228 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.957 MB | 8.957 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 20257 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 19.710% | 76.507% | 2.390 s | 367.333 MB | 390.090 MB | 8899.912 MB | 10208.211 MB | n/a MB | n/a MB |
| MainThread | 20278 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.875 MB | 228.875 MB | 1632.426 MB | 1632.426 MB | n/a MB | n/a MB |
| MainThread | 20304 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.950% | 77.527% | 2.440 s | 360.594 MB | 393.836 MB | 8777.225 MB | 10204.879 MB | n/a MB | n/a MB |
| sh | 20321 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 20322 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.020 MB | 7.020 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 20334 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 197.727 MB | 197.727 MB | 1617.250 MB | 1617.250 MB | n/a MB | n/a MB |
| sh | 20348 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| MainThread | 20353 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 43.088% | 89.114% | 3.040 s | 340.299 MB | 390.262 MB | 8056.806 MB | 10207.582 MB | n/a MB | n/a MB |
| MainThread | 20372 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.460% | 66.460% | 0.670 s | 232.455 MB | 277.266 MB | 1633.650 MB | 1673.328 MB | n/a MB | n/a MB |
| MainThread | 20400 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.823% | 78.480% | 2.880 s | 366.332 MB | 392.484 MB | 8888.615 MB | 10205.168 MB | n/a MB | n/a MB |
| MainThread | 20419 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.428% | 60.428% | 0.610 s | 257.400 MB | 294.082 MB | 1656.523 MB | 1688.816 MB | n/a MB | n/a MB |
| MainThread | 20524 | sandbox_agent_lsb-kimi_0000_0000 | 51 | 7.588% | 87.221% | 3.820 s | 385.619 MB | 397.492 MB | 9870.027 MB | 10209.184 MB | n/a MB | n/a MB |
| MainThread | 20544 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.566% | 58.566% | 0.590 s | 250.168 MB | 294.707 MB | 1654.277 MB | 1689.820 MB | n/a MB | n/a MB |
| bash | 20572 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 9.550% | 60.533% | 0.770 s | 19.756 MB | 64.938 MB | 24.925 MB | 80.078 MB | n/a MB | n/a MB |
| python | 20578 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 31.243% | 62.485% | 0.630 s | 51.626 MB | 65.133 MB | 63.570 MB | 80.133 MB | n/a MB | n/a MB |
| python | 20580 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 22.309% | 44.617% | 0.450 s | 56.516 MB | 65.266 MB | 69.385 MB | 80.160 MB | n/a MB | n/a MB |
| sh | 20604 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 20605 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.953 MB | 7.953 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| MainThread | 20609 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 38.786% | 73.489% | 2.350 s | 342.682 MB | 390.066 MB | 7764.675 MB | 10205.285 MB | n/a MB | n/a MB |
| MainThread | 20639 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 172.117 MB | 172.117 MB | 1579.723 MB | 1579.723 MB | n/a MB | n/a MB |
| MainThread | 20652 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 23.704% | 62.542% | 1.910 s | 365.056 MB | 390.773 MB | 9246.522 MB | 10208.918 MB | n/a MB | n/a MB |
| MainThread | 20671 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.551% | 60.551% | 0.610 s | 240.049 MB | 286.250 MB | 1647.766 MB | 1681.309 MB | n/a MB | n/a MB |
| MainThread | 20699 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 38.024% | 84.356% | 2.680 s | 340.786 MB | 392.590 MB | 8062.862 MB | 10209.184 MB | n/a MB | n/a MB |
| MainThread | 20726 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.348 MB | 229.348 MB | 1631.734 MB | 1631.734 MB | n/a MB | n/a MB |
| python3 | 20744 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.910 MB | 6.910 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 20743 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 20748 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.233% | 83.321% | 3.050 s | 366.496 MB | 395.559 MB | 8896.095 MB | 10215.121 MB | n/a MB | n/a MB |
| MainThread | 20776 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 160.809 MB | 160.809 MB | 1500.469 MB | 1500.469 MB | n/a MB | n/a MB |
| MainThread | 20795 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 26.954% | 96.167% | 3.270 s | 345.227 MB | 388.977 MB | 8844.322 MB | 10209.383 MB | n/a MB | n/a MB |
| MainThread | 20815 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.101% | 65.101% | 0.660 s | 212.822 MB | 259.582 MB | 1616.777 MB | 1655.582 MB | n/a MB | n/a MB |
| git | 20825 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.414 MB | 1.414 MB | 6.684 MB | 6.684 MB | n/a MB | n/a MB |
| MainThread | 20844 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 20.955% | 68.518% | 2.340 s | 368.443 MB | 392.203 MB | 9476.185 MB | 10205.004 MB | n/a MB | n/a MB |
| MainThread | 20864 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.443% | 64.443% | 0.650 s | 210.789 MB | 260.934 MB | 1578.258 MB | 1656.297 MB | n/a MB | n/a MB |
| sh | 20877 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 20878 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.895 MB | 7.895 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| MainThread | 20893 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 28.343% | 80.512% | 3.710 s | 355.514 MB | 386.320 MB | 8984.515 MB | 10213.219 MB | n/a MB | n/a MB |
| MainThread | 20914 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.648% | 49.648% | 0.500 s | 211.211 MB | 253.934 MB | 1614.162 MB | 1649.602 MB | n/a MB | n/a MB |
| kimi | 20940 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 26.458% | 93.383% | 2.930 s | 334.869 MB | 381.738 MB | 8648.261 MB | 10202.074 MB | n/a MB | n/a MB |
| MainThread | 20971 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 187.641 MB | 187.641 MB | 1593.973 MB | 1593.973 MB | n/a MB | n/a MB |
| MainThread | 20988 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.738% | 92.367% | 2.990 s | 355.192 MB | 388.879 MB | 8861.732 MB | 10209.531 MB | n/a MB | n/a MB |
| sh | 21009 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21010 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.367 MB | 10.367 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 21016 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 193.633 MB | 193.633 MB | 1614.723 MB | 1614.723 MB | n/a MB | n/a MB |
| sh | 21030 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21031 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.758 MB | 8.758 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 21035 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.501% | 74.472% | 2.720 s | 364.069 MB | 391.902 MB | 8892.105 MB | 10209.020 MB | n/a MB | n/a MB |
| MainThread | 21055 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.437% | 57.437% | 0.580 s | 265.750 MB | 302.309 MB | 1679.340 MB | 1726.719 MB | n/a MB | n/a MB |
| MainThread | 21083 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.932% | 72.436% | 2.690 s | 366.093 MB | 396.566 MB | 8784.641 MB | 10212.363 MB | n/a MB | n/a MB |
| python3 | 21108 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.457 MB | 9.457 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| sh | 21107 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 21112 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 255.879 MB | 255.879 MB | 1651.863 MB | 1651.863 MB | n/a MB | n/a MB |
| MainThread | 21131 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.174% | 87.401% | 2.770 s | 355.748 MB | 385.676 MB | 8961.490 MB | 10207.695 MB | n/a MB | n/a MB |
| MainThread | 21162 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 149.586 MB | 149.586 MB | 1308.988 MB | 1308.988 MB | n/a MB | n/a MB |
| kimi | 21181 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.299% | 90.467% | 2.580 s | 339.549 MB | 388.781 MB | 8632.434 MB | 10199.516 MB | n/a MB | n/a MB |
| MainThread | 21212 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.887 MB | 228.887 MB | 1635.832 MB | 1635.832 MB | n/a MB | n/a MB |
| MainThread | 21251 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 17.035% | 69.480% | 2.230 s | 375.208 MB | 393.320 MB | 9582.990 MB | 10206.121 MB | n/a MB | n/a MB |
| MainThread | 21271 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.627% | 55.627% | 0.560 s | 212.729 MB | 258.637 MB | 1616.793 MB | 1655.363 MB | n/a MB | n/a MB |
| MainThread | 21299 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.042% | 89.471% | 2.600 s | 328.797 MB | 379.016 MB | 7716.244 MB | 10205.750 MB | n/a MB | n/a MB |
| sh | 21330 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21331 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.871 MB | 9.871 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 21318 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.514% | 52.514% | 0.530 s | 236.816 MB | 272.590 MB | 1643.012 MB | 1667.758 MB | n/a MB | n/a MB |
| MainThread | 21346 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 14.766% | 72.508% | 2.230 s | 375.128 MB | 392.527 MB | 9664.121 MB | 10209.500 MB | n/a MB | n/a MB |
| MainThread | 21367 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 207.996 MB | 207.996 MB | 1620.477 MB | 1620.477 MB | n/a MB | n/a MB |
| kimi | 21393 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 41.580% | 91.331% | 2.930 s | 313.170 MB | 385.027 MB | 7867.745 MB | 10205.027 MB | n/a MB | n/a MB |
| MainThread | 21417 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 207.684 MB | 207.684 MB | 1619.258 MB | 1619.258 MB | n/a MB | n/a MB |
| MainThread | 21443 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.831% | 78.552% | 2.640 s | 360.381 MB | 386.602 MB | 8781.367 MB | 10209.695 MB | n/a MB | n/a MB |
| sh | 21460 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21461 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.492 MB | 7.492 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 21462 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 48.636% | 48.636% | 0.490 s | 263.490 MB | 297.270 MB | 1678.123 MB | 1724.254 MB | n/a MB | n/a MB |
| MainThread | 21490 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.747% | 93.396% | 2.990 s | 347.552 MB | 389.395 MB | 8850.969 MB | 10209.027 MB | n/a MB | n/a MB |
| MainThread | 21512 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 47.569% | 47.569% | 0.480 s | 194.373 MB | 229.121 MB | 1473.838 MB | 1631.957 MB | n/a MB | n/a MB |
| MainThread | 21538 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.089% | 80.359% | 2.910 s | 358.553 MB | 394.797 MB | 8888.467 MB | 10209.344 MB | n/a MB | n/a MB |
| MainThread | 21561 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.628% | 55.628% | 0.560 s | 211.262 MB | 254.098 MB | 1614.309 MB | 1650.145 MB | n/a MB | n/a MB |
| MainThread | 21590 | sandbox_agent_lsb-kimi_0000_0000 | 29 | 12.249% | 74.571% | 3.470 s | 379.610 MB | 395.016 MB | 9621.618 MB | 10214.957 MB | n/a MB | n/a MB |
| python3 | 21615 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.996 MB | 8.996 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 21614 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 21621 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 212.488 MB | 212.488 MB | 1622.461 MB | 1622.461 MB | n/a MB | n/a MB |
| sh | 21721 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 21722 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 21733 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 21.770% | 76.561% | 2.410 s | 367.301 MB | 392.125 MB | 8794.071 MB | 10210.172 MB | n/a MB | n/a MB |
| MainThread | 21761 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 279.363 MB | 279.363 MB | 1674.059 MB | 1674.059 MB | n/a MB | n/a MB |
| MainThread | 21780 | sandbox_agent_lsb-kimi_0000_0000 | 32 | 10.992% | 83.501% | 3.430 s | 380.555 MB | 395.523 MB | 9674.646 MB | 10213.426 MB | n/a MB | n/a MB |
| MainThread | 21810 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 221.445 MB | 221.445 MB | 1624.234 MB | 1624.234 MB | n/a MB | n/a MB |
| sh | 21831 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21832 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.957 MB | 19.957 MB | 25.062 MB | 25.062 MB | n/a MB | n/a MB |
| MainThread | 21847 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 31.490% | 76.417% | 2.220 s | 361.344 MB | 391.938 MB | 9125.098 MB | 10213.410 MB | n/a MB | n/a MB |
| MainThread | 21877 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 195.211 MB | 195.211 MB | 1615.473 MB | 1615.473 MB | n/a MB | n/a MB |
| MainThread | 21896 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.650% | 76.519% | 2.630 s | 369.376 MB | 390.148 MB | 9068.078 MB | 10209.066 MB | n/a MB | n/a MB |
| MainThread | 21916 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.505% | 60.505% | 0.610 s | 178.137 MB | 237.504 MB | 1466.979 MB | 1637.605 MB | n/a MB | n/a MB |
| sh | 21928 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 21929 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| MainThread | 21944 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 23.054% | 90.402% | 3.270 s | 353.034 MB | 391.680 MB | 9028.193 MB | 10209.352 MB | n/a MB | n/a MB |
| MainThread | 21964 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.113% | 64.113% | 0.650 s | 223.570 MB | 274.129 MB | 1625.012 MB | 1670.051 MB | n/a MB | n/a MB |
| kimi-code | 21972 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 48.859 MB | 48.859 MB | 843.254 MB | 843.254 MB | n/a MB | n/a MB |
| MainThread | 21994 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.842% | 79.530% | 2.640 s | 364.848 MB | 392.645 MB | 8786.002 MB | 10213.078 MB | n/a MB | n/a MB |
| MainThread | 22024 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 237.883 MB | 237.883 MB | 1638.371 MB | 1638.371 MB | n/a MB | n/a MB |
| MainThread | 22043 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 23.968% | 88.447% | 3.140 s | 360.179 MB | 391.465 MB | 8977.436 MB | 10211.812 MB | n/a MB | n/a MB |
| MainThread | 22063 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.173% | 61.173% | 0.620 s | 216.021 MB | 260.359 MB | 1617.775 MB | 1656.078 MB | n/a MB | n/a MB |
| MainThread | 22092 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.925% | 82.387% | 2.660 s | 360.050 MB | 394.785 MB | 8761.551 MB | 10195.078 MB | n/a MB | n/a MB |
| python3 | 22123 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.957 MB | 9.957 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 22122 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22115 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.575% | 59.575% | 0.600 s | 213.643 MB | 260.285 MB | 1617.262 MB | 1656.301 MB | n/a MB | n/a MB |
| MainThread | 22141 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 24.150% | 72.602% | 2.430 s | 357.101 MB | 389.738 MB | 8640.684 MB | 10194.883 MB | n/a MB | n/a MB |
| MainThread | 22162 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 74.427% | 74.427% | 0.750 s | 240.926 MB | 297.672 MB | 1642.855 MB | 1692.488 MB | n/a MB | n/a MB |
| MainThread | 22188 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 14.007% | 76.538% | 2.410 s | 373.988 MB | 394.238 MB | 9254.602 MB | 10203.180 MB | n/a MB | n/a MB |
| python3 | 22207 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.793 MB | 8.793 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 22206 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi-code | 22217 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 301.609 MB | 301.609 MB | 1726.293 MB | 1726.293 MB | n/a MB | n/a MB |
| MainThread | 22236 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.239% | 92.316% | 2.930 s | 346.210 MB | 387.797 MB | 8849.780 MB | 10207.270 MB | n/a MB | n/a MB |
| sh | 22260 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22261 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| MainThread | 22269 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 278.809 MB | 278.809 MB | 1673.812 MB | 1673.812 MB | n/a MB | n/a MB |
| MainThread | 22286 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 36.326% | 72.585% | 2.560 s | 347.841 MB | 396.176 MB | 8066.915 MB | 10209.781 MB | n/a MB | n/a MB |
| MainThread | 22305 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.587% | 57.587% | 0.580 s | 265.824 MB | 302.441 MB | 1679.436 MB | 1726.609 MB | n/a MB | n/a MB |
| MainThread | 22333 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.697% | 81.385% | 2.840 s | 362.136 MB | 394.094 MB | 8983.131 MB | 10211.570 MB | n/a MB | n/a MB |
| MainThread | 22354 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.527% | 56.527% | 0.570 s | 213.742 MB | 259.672 MB | 1616.906 MB | 1655.590 MB | n/a MB | n/a MB |
| kimi | 22399 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.411% | 93.275% | 2.950 s | 346.533 MB | 391.152 MB | 8774.040 MB | 10209.688 MB | n/a MB | n/a MB |
| MainThread | 22430 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 158.148 MB | 158.148 MB | 1314.930 MB | 1314.930 MB | n/a MB | n/a MB |
| MainThread | 22450 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 18.684% | 92.346% | 3.200 s | 362.859 MB | 397.191 MB | 9228.207 MB | 10211.562 MB | n/a MB | n/a MB |
| MainThread | 22472 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 46.562% | 46.562% | 0.470 s | 194.818 MB | 228.766 MB | 1474.547 MB | 1631.371 MB | n/a MB | n/a MB |
| MainThread | 22504 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 29.498% | 91.319% | 2.970 s | 349.266 MB | 387.387 MB | 8620.580 MB | 10208.582 MB | n/a MB | n/a MB |
| python3 | 22530 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.246 MB | 7.246 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 22529 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22535 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 205.516 MB | 205.516 MB | 1618.750 MB | 1618.750 MB | n/a MB | n/a MB |
| MainThread | 22555 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.573% | 75.599% | 2.430 s | 366.343 MB | 387.047 MB | 9569.837 MB | 10206.469 MB | n/a MB | n/a MB |
| MainThread | 22574 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.562% | 58.562% | 0.590 s | 160.279 MB | 236.500 MB | 1459.898 MB | 1636.102 MB | n/a MB | n/a MB |
| MainThread | 22603 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 26.575% | 82.374% | 2.710 s | 365.319 MB | 391.723 MB | 8651.857 MB | 10206.180 MB | n/a MB | n/a MB |
| python3 | 22624 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.094 MB | 8.094 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 22623 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22638 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.340 MB | 9.340 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 22637 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22629 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.406% | 60.406% | 0.650 s | 222.537 MB | 270.078 MB | 1623.771 MB | 1665.570 MB | n/a MB | n/a MB |
| python3 | 22649 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.980 MB | 9.980 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 22648 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22653 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 27.462% | 80.404% | 3.320 s | 359.697 MB | 392.121 MB | 8884.250 MB | 10209.180 MB | n/a MB | n/a MB |
| MainThread | 22670 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 69.515% | 69.515% | 0.700 s | 249.590 MB | 293.754 MB | 1653.887 MB | 1689.055 MB | n/a MB | n/a MB |
| sh | 22685 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| kimi | 22701 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 20.166% | 91.058% | 3.250 s | 351.692 MB | 390.645 MB | 9098.326 MB | 10213.297 MB | n/a MB | n/a MB |
| MainThread | 22722 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 202.398 MB | 202.398 MB | 1618.281 MB | 1618.281 MB | n/a MB | n/a MB |
| MainThread | 22827 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 22.136% | 75.434% | 2.230 s | 356.884 MB | 390.234 MB | 8652.369 MB | 10208.477 MB | n/a MB | n/a MB |
| sh | 22845 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 22846 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.961 MB | 8.961 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 22858 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 89.317% | 89.317% | 0.900 s | 163.779 MB | 289.527 MB | 1427.781 MB | 1684.059 MB | n/a MB | n/a MB |
| MainThread | 22877 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.792% | 73.518% | 2.650 s | 369.158 MB | 393.137 MB | 9065.344 MB | 10207.688 MB | n/a MB | n/a MB |
| python3 | 22895 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.801 MB | 5.801 MB | 11.645 MB | 11.645 MB | n/a MB | n/a MB |
| sh | 22894 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22896 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.926 MB | 228.926 MB | 1636.332 MB | 1636.332 MB | n/a MB | n/a MB |
| python3 | 22923 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.809 MB | 8.809 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 22922 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 22927 | sandbox_agent_lsb-kimi_0000_0000 | 27 | 11.501% | 77.503% | 3.010 s | 379.410 MB | 394.777 MB | 9577.876 MB | 10213.379 MB | n/a MB | n/a MB |
| MainThread | 22953 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 74.507% | 74.507% | 0.750 s | 230.650 MB | 294.996 MB | 1633.760 MB | 1689.797 MB | n/a MB | n/a MB |
| python | 22977 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 27.676 MB | 27.676 MB | 250.352 MB | 250.352 MB | n/a MB | n/a MB |
| bash | 22976 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 22996 | sandbox_agent_lsb-kimi_0000_0000 | 43 | 9.925% | 79.393% | 4.210 s | 385.472 MB | 397.707 MB | 9812.120 MB | 10213.566 MB | n/a MB | n/a MB |
| MainThread | 23027 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 194.324 MB | 194.324 MB | 1614.973 MB | 1614.973 MB | n/a MB | n/a MB |
| python | 23047 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.129 MB | 13.129 MB | 207.277 MB | 207.277 MB | n/a MB | n/a MB |
| bash | 23046 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.551 MB | 2.551 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 23066 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.719 MB | 2.719 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 23072 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.688 MB | 21.688 MB | 27.363 MB | 27.363 MB | n/a MB | n/a MB |
| sh | 23073 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 23085 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 23.741% | 78.343% | 2.870 s | 360.496 MB | 394.605 MB | 8889.606 MB | 10210.023 MB | n/a MB | n/a MB |
| MainThread | 23106 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.514% | 53.514% | 0.540 s | 209.992 MB | 253.414 MB | 1613.547 MB | 1649.121 MB | n/a MB | n/a MB |
| python3 | 23114 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.586 MB | 10.586 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 23113 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23132 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.880% | 79.515% | 2.600 s | 372.769 MB | 392.844 MB | 9587.508 MB | 10211.207 MB | n/a MB | n/a MB |
| MainThread | 23162 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 88.295% | 88.295% | 0.890 s | 223.107 MB | 302.453 MB | 1513.039 MB | 1726.273 MB | n/a MB | n/a MB |
| MainThread | 23184 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.752% | 77.321% | 2.730 s | 368.474 MB | 391.512 MB | 8989.259 MB | 10210.418 MB | n/a MB | n/a MB |
| python3 | 23203 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.281 MB | 8.281 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 23202 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi-code | 23204 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.426% | 60.426% | 0.610 s | 139.379 MB | 234.570 MB | 1235.500 MB | 1635.621 MB | n/a MB | n/a MB |
| MainThread | 23232 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.558% | 75.377% | 2.900 s | 369.179 MB | 393.133 MB | 9068.920 MB | 10211.203 MB | n/a MB | n/a MB |
| MainThread | 23252 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.561% | 60.561% | 0.610 s | 252.707 MB | 294.152 MB | 1655.570 MB | 1689.113 MB | n/a MB | n/a MB |
| python3 | 23265 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.008 MB | 10.008 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 23264 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23285 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.757% | 83.499% | 2.990 s | 361.770 MB | 396.816 MB | 8885.773 MB | 10209.062 MB | n/a MB | n/a MB |
| MainThread | 23309 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 49.611% | 49.611% | 0.500 s | 194.283 MB | 228.770 MB | 1476.154 MB | 1635.848 MB | n/a MB | n/a MB |
| MainThread | 23338 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 19.191% | 72.561% | 2.540 s | 372.858 MB | 396.789 MB | 9584.288 MB | 10212.656 MB | n/a MB | n/a MB |
| MainThread | 23358 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.606% | 57.606% | 0.580 s | 206.572 MB | 252.113 MB | 1483.160 MB | 1648.598 MB | n/a MB | n/a MB |
| python3 | 23373 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.160 MB | 8.160 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 23372 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23391 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.789% | 76.359% | 2.650 s | 371.425 MB | 393.812 MB | 9069.564 MB | 10211.676 MB | n/a MB | n/a MB |
| stty | 23409 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.453 MB | 0.453 MB | n/a MB | n/a MB |
| sh | 23410 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 23411 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.258 MB | 9.258 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| python3 | 23427 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.113 MB | 8.113 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| MainThread | 23416 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.606% | 56.606% | 0.570 s | 228.242 MB | 270.629 MB | 1629.537 MB | 1665.852 MB | n/a MB | n/a MB |
| sh | 23426 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23465 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.187% | 84.415% | 2.930 s | 362.451 MB | 395.258 MB | 8889.356 MB | 10210.609 MB | n/a MB | n/a MB |
| MainThread | 23495 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.316 MB | 229.316 MB | 1631.699 MB | 1631.699 MB | n/a MB | n/a MB |
| sh | 23509 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 23510 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.137 MB | 7.137 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 23514 | sandbox_agent_lsb-kimi_0000_0000 | 28 | 12.058% | 78.436% | 3.280 s | 376.694 MB | 391.586 MB | 9594.261 MB | 10206.590 MB | n/a MB | n/a MB |
| python3 | 23532 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.020 MB | 8.020 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 23531 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23541 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 235.035 MB | 235.035 MB | 1635.352 MB | 1635.352 MB | n/a MB | n/a MB |
| bash | 23560 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 10.289% | 72.409% | 0.830 s | 25.607 MB | 65.719 MB | 31.749 MB | 80.414 MB | n/a MB | n/a MB |
| python | 23563 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 13.414% | 53.657% | 0.540 s | 60.051 MB | 65.871 MB | 73.098 MB | 80.211 MB | n/a MB | n/a MB |
| MainThread | 23576 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 17.387% | 76.410% | 2.680 s | 374.448 MB | 393.520 MB | 9142.082 MB | 10211.211 MB | n/a MB | n/a MB |
| MainThread | 23599 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.814% | 61.814% | 0.710 s | 242.914 MB | 297.109 MB | 1642.854 MB | 1691.484 MB | n/a MB | n/a MB |
| MainThread | 23626 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.386% | 74.398% | 2.950 s | 365.529 MB | 394.348 MB | 8891.357 MB | 10210.559 MB | n/a MB | n/a MB |
| MainThread | 23648 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.526% | 62.526% | 0.630 s | 236.398 MB | 279.133 MB | 1644.400 MB | 1673.828 MB | n/a MB | n/a MB |
| MainThread | 23676 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.932% | 77.439% | 2.810 s | 362.709 MB | 389.656 MB | 9065.793 MB | 10210.043 MB | n/a MB | n/a MB |
| sh | 23705 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.512 MB | 1.512 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 23698 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 45.671% | 45.671% | 0.460 s | 199.875 MB | 236.223 MB | 1604.277 MB | 1636.332 MB | n/a MB | n/a MB |
| python3 | 23706 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.359 MB | 10.359 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 23724 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 19.371% | 75.451% | 2.340 s | 374.536 MB | 396.988 MB | 8911.600 MB | 10211.934 MB | n/a MB | n/a MB |
| MainThread | 23754 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 278.934 MB | 278.934 MB | 1673.812 MB | 1673.812 MB | n/a MB | n/a MB |
| MainThread | 23852 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.892% | 75.410% | 2.960 s | 365.637 MB | 396.496 MB | 9063.736 MB | 10210.062 MB | n/a MB | n/a MB |
| MainThread | 23871 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.581% | 54.581% | 0.550 s | 235.031 MB | 275.836 MB | 1643.402 MB | 1672.082 MB | n/a MB | n/a MB |
| MainThread | 23903 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 22.109% | 91.218% | 3.180 s | 367.317 MB | 401.711 MB | 9039.668 MB | 10211.254 MB | n/a MB | n/a MB |
| MainThread | 23921 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 74.253% | 74.253% | 0.750 s | 225.439 MB | 281.098 MB | 1627.145 MB | 1675.566 MB | n/a MB | n/a MB |
| MainThread | 23951 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 19.743% | 78.389% | 2.440 s | 373.415 MB | 390.844 MB | 9542.862 MB | 10211.484 MB | n/a MB | n/a MB |
| MainThread | 23974 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 215.535 MB | 215.535 MB | 1623.918 MB | 1623.918 MB | n/a MB | n/a MB |
| MainThread | 24003 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 25.502% | 94.422% | 3.340 s | 352.862 MB | 391.449 MB | 8952.802 MB | 10211.340 MB | n/a MB | n/a MB |
| kimi-code | 24023 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 48.566 MB | 48.566 MB | 847.234 MB | 847.234 MB | n/a MB | n/a MB |
| MainThread | 24034 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 194.562 MB | 194.562 MB | 1614.723 MB | 1614.723 MB | n/a MB | n/a MB |
| tar | 24042 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.879 MB | 0.879 MB | n/a MB | n/a MB |
| python3 | 24052 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.086 MB | 9.086 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 24051 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24056 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 21.251% | 81.271% | 3.210 s | 368.275 MB | 395.871 MB | 9136.492 MB | 10212.988 MB | n/a MB | n/a MB |
| MainThread | 24075 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.436% | 62.436% | 0.630 s | 217.977 MB | 260.691 MB | 1623.029 MB | 1656.336 MB | n/a MB | n/a MB |
| MainThread | 24108 | sandbox_agent_lsb-kimi_0000_0000 | 22 | 14.037% | 78.396% | 2.970 s | 378.736 MB | 394.621 MB | 9431.946 MB | 10210.797 MB | n/a MB | n/a MB |
| python3 | 24136 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.113 MB | 8.113 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 24135 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24137 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.664 MB | 228.664 MB | 1631.469 MB | 1631.469 MB | n/a MB | n/a MB |
| MainThread | 24159 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 28.321% | 78.516% | 2.280 s | 361.432 MB | 391.074 MB | 9239.612 MB | 10210.266 MB | n/a MB | n/a MB |
| MainThread | 24184 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 205.641 MB | 205.641 MB | 1619.488 MB | 1619.488 MB | n/a MB | n/a MB |
| MainThread | 24208 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.182% | 76.451% | 2.440 s | 369.781 MB | 393.828 MB | 8895.424 MB | 10211.875 MB | n/a MB | n/a MB |
| MainThread | 24227 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.502% | 60.502% | 0.610 s | 175.158 MB | 254.496 MB | 1466.635 MB | 1649.574 MB | n/a MB | n/a MB |
| sh | 24239 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24240 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.020 MB | 7.020 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 24256 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 17.940% | 66.528% | 2.170 s | 375.581 MB | 394.383 MB | 9540.534 MB | 10212.098 MB | n/a MB | n/a MB |
| MainThread | 24275 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.595% | 61.595% | 0.620 s | 221.963 MB | 269.156 MB | 1623.482 MB | 1664.992 MB | n/a MB | n/a MB |
| MainThread | 24307 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 19.368% | 86.453% | 3.120 s | 363.890 MB | 401.020 MB | 9173.032 MB | 10218.355 MB | n/a MB | n/a MB |
| MainThread | 24334 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 170.207 MB | 170.207 MB | 1579.723 MB | 1579.723 MB | n/a MB | n/a MB |
| MainThread | 24358 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.019% | 78.505% | 2.880 s | 359.759 MB | 388.020 MB | 8978.853 MB | 10207.012 MB | n/a MB | n/a MB |
| python3 | 24390 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.797 MB | 8.797 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 24389 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24379 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.538% | 67.538% | 0.680 s | 244.875 MB | 295.660 MB | 1652.465 MB | 1690.457 MB | n/a MB | n/a MB |
| MainThread | 24408 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.997% | 86.368% | 2.750 s | 363.704 MB | 400.188 MB | 8952.914 MB | 10202.344 MB | n/a MB | n/a MB |
| python3 | 24432 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.289 MB | 7.289 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 24431 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24438 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 213.289 MB | 213.289 MB | 1622.980 MB | 1622.980 MB | n/a MB | n/a MB |
| MainThread | 24460 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 17.946% | 68.528% | 2.170 s | 374.266 MB | 396.688 MB | 9535.750 MB | 10212.543 MB | n/a MB | n/a MB |
| MainThread | 24478 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.484% | 65.484% | 0.660 s | 234.852 MB | 280.488 MB | 1634.756 MB | 1675.289 MB | n/a MB | n/a MB |
| sh | 24490 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24491 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.551 MB | 10.551 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 24528 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.070% | 77.417% | 2.590 s | 371.500 MB | 392.738 MB | 9066.918 MB | 10207.188 MB | n/a MB | n/a MB |
| python3 | 24547 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.625 MB | 8.625 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 24546 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24557 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.287% | 63.287% | 0.700 s | 209.240 MB | 271.082 MB | 1485.088 MB | 1666.309 MB | n/a MB | n/a MB |
| MainThread | 24578 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.708% | 76.463% | 2.930 s | 368.788 MB | 393.871 MB | 9065.270 MB | 10208.367 MB | n/a MB | n/a MB |
| sh | 24603 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24604 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.059 MB | 7.059 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 24608 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 213.160 MB | 213.160 MB | 1623.469 MB | 1623.469 MB | n/a MB | n/a MB |
| gzip | 24621 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| tar | 24620 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.211 MB | 2.211 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| MainThread | 24630 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 23.312% | 90.255% | 3.760 s | 365.036 MB | 393.598 MB | 9191.574 MB | 10211.270 MB | n/a MB | n/a MB |
| MainThread | 24651 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 53.009% | 57.483% | 1.070 s | 220.676 MB | 288.715 MB | 1538.783 MB | 1683.812 MB | n/a MB | n/a MB |
| sh | 24678 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 24679 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.797 MB | 8.797 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 24683 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 27.061% | 88.362% | 3.550 s | 359.303 MB | 388.320 MB | 8978.899 MB | 10209.164 MB | n/a MB | n/a MB |
| sh | 24709 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi | 24712 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.976% | 53.976% | 0.550 s | 106.705 MB | 212.824 MB | 893.121 MB | 1622.961 MB | n/a MB | n/a MB |
| python3 | 24710 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.375 MB | 9.375 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| MainThread | 24733 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 21.164% | 74.545% | 2.190 s | 369.611 MB | 395.703 MB | 9414.774 MB | 10206.453 MB | n/a MB | n/a MB |
| MainThread | 24752 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.103% | 67.103% | 0.680 s | 216.465 MB | 269.512 MB | 1618.766 MB | 1665.059 MB | n/a MB | n/a MB |
| MainThread | 24780 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 15.691% | 73.580% | 2.400 s | 378.035 MB | 398.363 MB | 9661.165 MB | 10210.855 MB | n/a MB | n/a MB |
| MainThread | 24800 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.371% | 60.371% | 0.610 s | 209.654 MB | 258.703 MB | 1486.088 MB | 1655.086 MB | n/a MB | n/a MB |
| python3 | 24813 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.133 MB | 8.133 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 24812 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 24832 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.655% | 81.365% | 2.910 s | 359.021 MB | 388.641 MB | 9052.833 MB | 10209.941 MB | n/a MB | n/a MB |
| MainThread | 25001 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 166.793 MB | 166.793 MB | 1577.973 MB | 1577.973 MB | n/a MB | n/a MB |
| MainThread | 25023 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 33.290% | 77.478% | 2.360 s | 356.686 MB | 391.387 MB | 8078.975 MB | 10212.082 MB | n/a MB | n/a MB |
| python3 | 25042 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.742 MB | 9.742 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 25041 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25053 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 295.652 MB | 295.652 MB | 1690.730 MB | 1690.730 MB | n/a MB | n/a MB |
| MainThread | 25073 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.246% | 66.641% | 2.780 s | 367.073 MB | 395.562 MB | 8980.897 MB | 10206.730 MB | n/a MB | n/a MB |
| MainThread | 25098 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 197.797 MB | 197.797 MB | 1616.711 MB | 1616.711 MB | n/a MB | n/a MB |
| MainThread | 25120 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 18.717% | 69.338% | 2.830 s | 366.525 MB | 391.984 MB | 9139.789 MB | 10213.121 MB | n/a MB | n/a MB |
| sh | 25150 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.352 MB | 1.352 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25139 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.508% | 55.508% | 0.560 s | 254.756 MB | 294.934 MB | 1656.012 MB | 1689.305 MB | n/a MB | n/a MB |
| python3 | 25151 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.148 MB | 9.148 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 25171 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.987% | 78.168% | 2.680 s | 371.035 MB | 396.871 MB | 9069.553 MB | 10211.547 MB | n/a MB | n/a MB |
| bash | 25185 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.480 MB | 1.480 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 25184 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.781 MB | 2.781 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 25188 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25189 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.207 MB | 7.207 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 25190 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 228.531 MB | 228.531 MB | 1635.594 MB | 1635.594 MB | n/a MB | n/a MB |
| python3 | 25218 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.594 MB | 9.594 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 25217 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25222 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.943% | 71.630% | 2.810 s | 368.752 MB | 398.391 MB | 9064.407 MB | 10208.750 MB | n/a MB | n/a MB |
| MainThread | 25242 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.466% | 61.466% | 0.620 s | 251.070 MB | 295.969 MB | 1654.914 MB | 1690.332 MB | n/a MB | n/a MB |
| MainThread | 25274 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.439% | 84.364% | 2.810 s | 376.217 MB | 399.086 MB | 8993.799 MB | 10211.223 MB | n/a MB | n/a MB |
| sh | 25292 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25293 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 25307 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.664 MB | 4.664 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| MainThread | 25296 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.444% | 53.444% | 0.540 s | 213.746 MB | 251.289 MB | 1619.148 MB | 1647.574 MB | n/a MB | n/a MB |
| sh | 25306 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 25325 | sandbox_agent_lsb-kimi_0000_0000 | 31 | 13.667% | 93.387% | 4.130 s | 378.343 MB | 398.395 MB | 9639.009 MB | 10210.566 MB | n/a MB | n/a MB |
| MainThread | 25343 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.413% | 64.413% | 0.650 s | 233.715 MB | 277.934 MB | 1633.893 MB | 1673.312 MB | n/a MB | n/a MB |
| python3 | 25356 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.992 MB | 6.992 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 25355 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 25374 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 9.785% | 59.539% | 0.790 s | 26.804 MB | 65.836 MB | 33.326 MB | 80.434 MB | n/a MB | n/a MB |
| python | 25377 | sandbox_agent_lsb-kimi_0000_0000 | 5 | 16.136% | 64.544% | 0.650 s | 58.052 MB | 65.941 MB | 70.762 MB | 80.172 MB | n/a MB | n/a MB |
| MainThread | 25391 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.129% | 69.595% | 2.980 s | 371.327 MB | 400.047 MB | 9069.409 MB | 10214.316 MB | n/a MB | n/a MB |
| sh | 25420 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| MainThread | 25410 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.325% | 61.325% | 0.620 s | 248.285 MB | 293.957 MB | 1653.631 MB | 1689.035 MB | n/a MB | n/a MB |
| MainThread | 25441 | sandbox_agent_lsb-kimi_0000_0000 | 17 | 18.945% | 83.460% | 3.050 s | 367.753 MB | 393.387 MB | 9200.867 MB | 10212.641 MB | n/a MB | n/a MB |
| MainThread | 25467 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 194.406 MB | 194.406 MB | 1614.473 MB | 1614.473 MB | n/a MB | n/a MB |
| MainThread | 25494 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.372% | 77.416% | 2.590 s | 376.405 MB | 396.879 MB | 9624.979 MB | 10213.785 MB | n/a MB | n/a MB |
| MainThread | 25514 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.605% | 60.605% | 0.610 s | 155.268 MB | 235.695 MB | 1459.895 MB | 1636.094 MB | n/a MB | n/a MB |
| kimi-code | 25538 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 58.180 MB | 58.180 MB | 903.160 MB | 903.160 MB | n/a MB | n/a MB |
| sh | 25540 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25541 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.008 MB | 9.008 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 25545 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 21.385% | 71.482% | 2.800 s | 367.882 MB | 394.219 MB | 8985.942 MB | 10210.457 MB | n/a MB | n/a MB |
| MainThread | 25569 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.578% | 52.578% | 0.530 s | 210.900 MB | 254.098 MB | 1614.176 MB | 1649.879 MB | n/a MB | n/a MB |
| MainThread | 25593 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.524% | 78.557% | 2.750 s | 373.680 MB | 397.770 MB | 9068.598 MB | 10210.016 MB | n/a MB | n/a MB |
| MainThread | 25631 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.670% | 51.670% | 0.520 s | 244.727 MB | 278.379 MB | 1647.848 MB | 1673.016 MB | n/a MB | n/a MB |
| MainThread | 25662 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 16.624% | 76.511% | 2.530 s | 377.113 MB | 398.594 MB | 9144.129 MB | 10211.723 MB | n/a MB | n/a MB |
| sh | 25679 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25680 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.922 MB | 8.922 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 25690 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 238.035 MB | 238.035 MB | 1638.570 MB | 1638.570 MB | n/a MB | n/a MB |
| MainThread | 25709 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.620% | 76.415% | 2.460 s | 380.390 MB | 399.746 MB | 9589.021 MB | 10213.484 MB | n/a MB | n/a MB |
| MainThread | 25735 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 70.384% | 70.384% | 0.710 s | 245.645 MB | 297.469 MB | 1669.062 MB | 1723.652 MB | n/a MB | n/a MB |
| MainThread | 25762 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 16.309% | 82.310% | 3.120 s | 369.357 MB | 391.812 MB | 9348.546 MB | 10213.102 MB | n/a MB | n/a MB |
| sh | 25785 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 25786 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.664 MB | 5.664 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| MainThread | 25793 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 175.879 MB | 175.879 MB | 1590.223 MB | 1590.223 MB | n/a MB | n/a MB |
| MainThread | 25815 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.087% | 77.317% | 2.550 s | 371.323 MB | 391.043 MB | 9068.758 MB | 10204.664 MB | n/a MB | n/a MB |
| stty | 25833 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.422 MB | 0.422 MB | n/a MB | n/a MB |
| MainThread | 25847 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 89.351% | 89.351% | 0.900 s | 171.148 MB | 296.129 MB | 1432.535 MB | 1690.711 MB | n/a MB | n/a MB |
| MainThread | 25866 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.865% | 75.590% | 2.540 s | 368.885 MB | 388.504 MB | 8911.908 MB | 10213.320 MB | n/a MB | n/a MB |
| MainThread | 25895 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 291.012 MB | 291.012 MB | 1686.070 MB | 1686.070 MB | n/a MB | n/a MB |
| MainThread | 25914 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 24.761% | 89.417% | 3.250 s | 353.371 MB | 397.203 MB | 8942.575 MB | 10212.086 MB | n/a MB | n/a MB |
| MainThread | 25997 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.528% | 59.528% | 0.600 s | 203.250 MB | 252.305 MB | 1573.785 MB | 1648.102 MB | n/a MB | n/a MB |
| python3 | 26024 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.145 MB | 8.145 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 26023 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 26039 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 16.881% | 79.431% | 2.380 s | 378.430 MB | 398.359 MB | 9084.782 MB | 10212.254 MB | n/a MB | n/a MB |
| MainThread | 26069 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 166.965 MB | 166.965 MB | 1577.973 MB | 1577.973 MB | n/a MB | n/a MB |
| MainThread | 26091 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.254% | 72.597% | 2.390 s | 375.865 MB | 394.512 MB | 9588.197 MB | 10211.738 MB | n/a MB | n/a MB |
| MainThread | 26112 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.545% | 61.545% | 0.620 s | 207.416 MB | 255.645 MB | 1575.656 MB | 1651.344 MB | n/a MB | n/a MB |
| python3 | 26125 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.047 MB | 6.047 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 26124 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| tar | 26133 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.191 MB | 2.191 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 26134 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.336 MB | 1.336 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| MainThread | 26143 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 18.994% | 89.454% | 3.440 s | 368.081 MB | 399.113 MB | 9287.282 MB | 10215.160 MB | n/a MB | n/a MB |
| MainThread | 26174 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 175.195 MB | 175.195 MB | 1589.973 MB | 1589.973 MB | n/a MB | n/a MB |
| MainThread | 26196 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 20.388% | 74.495% | 3.080 s | 365.948 MB | 391.992 MB | 9138.499 MB | 10212.578 MB | n/a MB | n/a MB |
| sh | 26225 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 26215 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.316% | 64.316% | 0.650 s | 232.029 MB | 277.527 MB | 1633.029 MB | 1672.336 MB | n/a MB | n/a MB |
| tar | 26236 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.039 MB | 2.039 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| tar | 26237 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| MainThread | 26246 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.184% | 74.469% | 2.450 s | 371.218 MB | 392.953 MB | 9539.116 MB | 10211.930 MB | n/a MB | n/a MB |
| MainThread | 26274 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 70.444% | 70.444% | 0.710 s | 215.607 MB | 278.258 MB | 1586.498 MB | 1673.777 MB | n/a MB | n/a MB |
| tar | 26289 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.012 MB | 2.012 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 26290 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.242 MB | 1.242 MB | n/a MB | n/a MB |
| MainThread | 26296 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 20.791% | 86.362% | 3.140 s | 367.825 MB | 399.160 MB | 9118.954 MB | 10213.934 MB | n/a MB | n/a MB |
| MainThread | 26316 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.604% | 59.604% | 0.600 s | 217.402 MB | 260.781 MB | 1618.902 MB | 1656.582 MB | n/a MB | n/a MB |
| MainThread | 26347 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 19.873% | 73.591% | 2.800 s | 367.031 MB | 391.867 MB | 9070.545 MB | 10213.355 MB | n/a MB | n/a MB |
| sh | 26373 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 26374 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 26378 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 205.516 MB | 205.516 MB | 1618.691 MB | 1618.691 MB | n/a MB | n/a MB |
| kimi | 26400 | sandbox_agent_lsb-kimi_0000_0000 | 21 | 16.256% | 89.349% | 3.280 s | 365.494 MB | 398.367 MB | 9316.352 MB | 10208.125 MB | n/a MB | n/a MB |
| MainThread | 26429 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 83.298% | 83.298% | 0.840 s | 230.062 MB | 301.523 MB | 1613.146 MB | 1726.324 MB | n/a MB | n/a MB |
| MainThread | 26453 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 20.320% | 73.559% | 2.250 s | 373.993 MB | 395.789 MB | 9486.028 MB | 10212.090 MB | n/a MB | n/a MB |
| MainThread | 26475 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.619% | 58.619% | 0.590 s | 200.805 MB | 253.016 MB | 1541.783 MB | 1649.098 MB | n/a MB | n/a MB |
| python3 | 26488 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.477 MB | 5.477 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| sh | 26487 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 26503 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.984% | 87.362% | 3.060 s | 357.576 MB | 392.484 MB | 8865.795 MB | 10210.695 MB | n/a MB | n/a MB |
| MainThread | 26522 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.182% | 65.182% | 0.660 s | 226.861 MB | 279.000 MB | 1631.760 MB | 1673.547 MB | n/a MB | n/a MB |
| kimi-code | 26548 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 60.723 MB | 60.723 MB | 903.531 MB | 903.531 MB | n/a MB | n/a MB |
| MainThread | 26551 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 20.586% | 83.378% | 3.110 s | 371.696 MB | 394.430 MB | 9145.223 MB | 10216.316 MB | n/a MB | n/a MB |
| MainThread | 26581 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 272.277 MB | 272.277 MB | 1667.309 MB | 1667.309 MB | n/a MB | n/a MB |
| MainThread | 26603 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 18.503% | 89.458% | 3.170 s | 363.649 MB | 399.957 MB | 9226.905 MB | 10214.000 MB | n/a MB | n/a MB |
| MainThread | 26622 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.519% | 65.519% | 0.660 s | 240.926 MB | 288.148 MB | 1648.766 MB | 1683.059 MB | n/a MB | n/a MB |
| python3 | 26631 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.676 MB | 7.676 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 26630 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 26671 | sandbox_agent_lsb-kimi_0000_0000 | 21 | 16.244% | 70.490% | 3.310 s | 377.084 MB | 396.449 MB | 9393.178 MB | 10211.723 MB | n/a MB | n/a MB |
| MainThread | 26691 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.996% | 67.996% | 0.690 s | 237.566 MB | 286.566 MB | 1637.625 MB | 1681.277 MB | n/a MB | n/a MB |
| MainThread | 26724 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 17.641% | 75.424% | 3.020 s | 374.015 MB | 394.992 MB | 9256.937 MB | 10208.852 MB | n/a MB | n/a MB |
| MainThread | 26755 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 166.711 MB | 166.711 MB | 1577.723 MB | 1577.723 MB | n/a MB | n/a MB |
| MainThread | 26775 | sandbox_agent_lsb-kimi_0000_0000 | 143 | 5.813% | 86.325% | 8.310 s | 395.870 MB | 419.277 MB | 10085.577 MB | 10219.336 MB | n/a MB | n/a MB |
| MainThread | 26798 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 208.402 MB | 208.402 MB | 1619.977 MB | 1619.977 MB | n/a MB | n/a MB |
| bash | 26826 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.863 MB | 2.863 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 26827 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 34.012 MB | 34.012 MB | 226.105 MB | 226.105 MB | n/a MB | n/a MB |
| python | 26855 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 46.215 MB | 46.215 MB | 267.531 MB | 267.531 MB | n/a MB | n/a MB |
| bash | 26854 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.727 MB | 2.727 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 26956 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.707 MB | 2.707 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 26957 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.336 MB | 13.336 MB | 207.258 MB | 207.258 MB | n/a MB | n/a MB |
| bash | 26969 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.875 MB | 2.875 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 26970 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.289 MB | 13.289 MB | 207.137 MB | 207.137 MB | n/a MB | n/a MB |
| sh | 26980 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 26981 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.688 MB | 15.688 MB | 20.711 MB | 20.711 MB | n/a MB | n/a MB |
| python3 | 26993 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.160 MB | 9.160 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 26992 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27026 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.785 MB | 6.785 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 27025 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.398 MB | 1.398 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27043 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.254 MB | 10.254 MB | 15.270 MB | 15.270 MB | n/a MB | n/a MB |
| sh | 27042 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 27047 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27048 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.480 MB | 16.480 MB | 21.844 MB | 21.844 MB | n/a MB | n/a MB |
| python3 | 27057 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.551 MB | 14.551 MB | 20.082 MB | 20.082 MB | n/a MB | n/a MB |
| sh | 27056 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 27064 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27065 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.422 MB | 9.422 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| bash | 27073 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.641 MB | 2.641 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 27074 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 10.898 MB | 10.898 MB | 14.891 MB | 14.891 MB | n/a MB | n/a MB |
| python | 27075 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 35.168% | 69.343% | 0.710 s | 53.947 MB | 65.746 MB | 66.609 MB | 80.191 MB | n/a MB | n/a MB |
| python3 | 27077 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.676 MB | 7.676 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 27076 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27087 | sandbox_agent_lsb-kimi_0000_0000 | 37 | 9.903% | 74.495% | 3.590 s | 385.599 MB | 397.895 MB | 9749.580 MB | 10215.387 MB | n/a MB | n/a MB |
| bash | 27103 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 27102 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.609 MB | 2.609 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 27110 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 48.604% | 48.604% | 0.490 s | 204.137 MB | 241.703 MB | 1608.789 MB | 1639.855 MB | n/a MB | n/a MB |
| bash | 27133 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.922 MB | 2.922 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 27134 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 29.802% | 59.605% | 0.600 s | 36.874 MB | 50.164 MB | 185.737 MB | 271.246 MB | n/a MB | n/a MB |
| python | 27138 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 41.736% | 41.736% | 0.420 s | 53.047 MB | 65.891 MB | 64.072 MB | 80.098 MB | n/a MB | n/a MB |
| bash | 27147 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 27148 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.661% | 1.984% | 0.020 s | 10.207 MB | 10.906 MB | 14.452 MB | 14.930 MB | n/a MB | n/a MB |
| python | 27149 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 6.447% | 12.894% | 0.130 s | 63.767 MB | 65.805 MB | 78.217 MB | 80.168 MB | n/a MB | n/a MB |
| python3 | 27157 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.297 MB | 9.297 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 27156 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 27159 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 11.191 MB | 11.191 MB | 14.926 MB | 14.926 MB | n/a MB | n/a MB |
| bash | 27158 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.727 MB | 2.727 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 27160 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 21.806% | 21.806% | 0.220 s | 56.191 MB | 65.059 MB | 68.061 MB | 80.102 MB | n/a MB | n/a MB |
| sh | 27162 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27163 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.465 MB | 21.465 MB | 26.984 MB | 26.984 MB | n/a MB | n/a MB |
| MainThread | 27174 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 15.252% | 74.593% | 2.610 s | 380.801 MB | 395.969 MB | 9724.527 MB | 10210.137 MB | n/a MB | n/a MB |
| MainThread | 27202 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 67.444% | 67.444% | 0.680 s | 220.838 MB | 288.031 MB | 1591.146 MB | 1683.074 MB | n/a MB | n/a MB |
| bash | 27218 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.770 MB | 2.770 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 27219 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.180 MB | 23.180 MB | 215.605 MB | 215.605 MB | n/a MB | n/a MB |
| MainThread | 27233 | sandbox_agent_lsb-kimi_0000_0000 | 32 | 12.908% | 84.514% | 4.030 s | 376.768 MB | 403.812 MB | 9659.527 MB | 10213.449 MB | n/a MB | n/a MB |
| git | 27253 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 27262 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 278.012 MB | 278.012 MB | 1672.809 MB | 1672.809 MB | n/a MB | n/a MB |
| python | 27283 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.441 MB | 14.441 MB | 1874.160 MB | 1874.160 MB | n/a MB | n/a MB |
| bash | 27278 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 25.766% | 25.766% | 0.260 s | 19.371 MB | 36.031 MB | 24.160 MB | 44.473 MB | n/a MB | n/a MB |
| python3 | 27288 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sh | 27287 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.285 MB | 1.285 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27293 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.898 MB | 20.898 MB | 25.449 MB | 25.449 MB | n/a MB | n/a MB |
| sh | 27292 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27310 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 39.881% | 69.590% | 2.820 s | 347.722 MB | 386.855 MB | 8055.031 MB | 10195.707 MB | n/a MB | n/a MB |
| MainThread | 27336 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 203.816 MB | 203.816 MB | 1618.480 MB | 1618.480 MB | n/a MB | n/a MB |
| MainThread | 27360 | sandbox_agent_lsb-kimi_0000_0000 | 54 | 8.711% | 68.618% | 4.650 s | 390.921 MB | 402.188 MB | 9895.130 MB | 10215.602 MB | n/a MB | n/a MB |
| sh | 27381 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27382 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.367 MB | 7.367 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 27388 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 160.727 MB | 160.727 MB | 1500.469 MB | 1500.469 MB | n/a MB | n/a MB |
| sh | 27414 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27415 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.070 MB | 7.070 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 27446 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27447 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.035 MB | 18.035 MB | 24.184 MB | 24.184 MB | n/a MB | n/a MB |
| sh | 27465 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27466 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.625 MB | 10.625 MB | 15.297 MB | 15.297 MB | n/a MB | n/a MB |
| sh | 27481 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27482 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.535 MB | 21.535 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| MainThread | 27505 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 16.397% | 81.494% | 3.140 s | 369.869 MB | 395.668 MB | 9310.035 MB | 10186.246 MB | n/a MB | n/a MB |
| python3 | 27523 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.777 MB | 10.777 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 27522 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 27536 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27526 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 68.798% | 68.798% | 0.710 s | 238.516 MB | 296.676 MB | 1641.350 MB | 1691.227 MB | n/a MB | n/a MB |
| python3 | 27537 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.695 MB | 8.695 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| python3 | 27550 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.555 MB | 10.555 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 27549 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27554 | sandbox_agent_lsb-kimi_0000_0000 | 22 | 16.844% | 75.380% | 3.570 s | 373.938 MB | 393.832 MB | 9432.317 MB | 10213.816 MB | n/a MB | n/a MB |
| MainThread | 27583 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 84.384% | 84.384% | 0.850 s | 224.385 MB | 292.055 MB | 1499.672 MB | 1686.711 MB | n/a MB | n/a MB |
| MainThread | 27610 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 41.383% | 71.485% | 2.500 s | 355.387 MB | 385.332 MB | 8952.373 MB | 10214.270 MB | n/a MB | n/a MB |
| MainThread | 27628 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.459% | 64.459% | 0.650 s | 221.711 MB | 271.824 MB | 1623.262 MB | 1666.801 MB | n/a MB | n/a MB |
| MainThread | 27657 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 19.098% | 85.354% | 3.670 s | 370.818 MB | 395.227 MB | 9333.569 MB | 10214.906 MB | n/a MB | n/a MB |
| MainThread | 27679 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.760% | 56.760% | 0.590 s | 232.367 MB | 277.570 MB | 1634.023 MB | 1673.574 MB | n/a MB | n/a MB |
| python3 | 27690 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.867 MB | 9.867 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 27689 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 27700 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 127.109% | 149.894% | 2.560 s | 1614.303 MB | 2785.039 MB | 1877.051 MB | 3160.988 MB | n/a MB | n/a MB |
| sh | 27706 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27708 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.254 MB | 7.254 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 27793 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 36.304% | 87.476% | 2.930 s | 340.978 MB | 396.844 MB | 8250.877 MB | 10207.188 MB | n/a MB | n/a MB |
| python3 | 27828 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.863 MB | 9.863 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 27817 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 66.309% | 66.309% | 0.670 s | 248.348 MB | 302.793 MB | 1670.289 MB | 1726.355 MB | n/a MB | n/a MB |
| sh | 27827 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 27841 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 25.795% | 76.477% | 3.380 s | 366.327 MB | 396.234 MB | 8981.846 MB | 10214.438 MB | n/a MB | n/a MB |
| MainThread | 27865 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 208.273 MB | 208.273 MB | 1619.488 MB | 1619.488 MB | n/a MB | n/a MB |
| python | 27887 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 10.930 MB | 10.930 MB | 14.895 MB | 14.895 MB | n/a MB | n/a MB |
| python | 27888 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.479% | 61.479% | 0.620 s | 49.250 MB | 65.035 MB | 61.426 MB | 80.105 MB | n/a MB | n/a MB |
| bash | 27886 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.805 MB | 2.805 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 27891 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27892 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.070 MB | 7.070 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 27902 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 27.966% | 91.417% | 3.390 s | 353.127 MB | 390.809 MB | 8858.251 MB | 10212.164 MB | n/a MB | n/a MB |
| MainThread | 27931 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 188.758 MB | 188.758 MB | 1594.223 MB | 1594.223 MB | n/a MB | n/a MB |
| sh | 27945 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 27946 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.668 MB | 10.668 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 27950 | sandbox_agent_lsb-kimi_0000_0000 | 10 | 32.343% | 79.462% | 2.930 s | 352.190 MB | 394.949 MB | 8493.094 MB | 10213.867 MB | n/a MB | n/a MB |
| MainThread | 27985 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 23.838% | 70.484% | 2.640 s | 363.088 MB | 388.727 MB | 8783.841 MB | 10212.223 MB | n/a MB | n/a MB |
| MainThread | 28018 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 20.197% | 91.224% | 3.050 s | 366.865 MB | 395.746 MB | 9081.695 MB | 10196.875 MB | n/a MB | n/a MB |
| MainThread | 28055 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 39.386% | 83.534% | 2.380 s | 351.507 MB | 380.754 MB | 8954.438 MB | 10207.875 MB | n/a MB | n/a MB |
| python3 | 28074 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.621 MB | 7.621 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 28073 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28084 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 207.320 MB | 207.320 MB | 1619.215 MB | 1619.215 MB | n/a MB | n/a MB |
| MainThread | 28101 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 25.688% | 76.470% | 3.370 s | 360.467 MB | 396.957 MB | 8973.362 MB | 10215.008 MB | n/a MB | n/a MB |
| MainThread | 28118 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.472% | 64.472% | 0.650 s | 243.988 MB | 290.133 MB | 1651.273 MB | 1685.066 MB | n/a MB | n/a MB |
| MainThread | 28157 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 19.498% | 85.458% | 3.730 s | 368.053 MB | 397.273 MB | 9326.457 MB | 10210.789 MB | n/a MB | n/a MB |
| MainThread | 28174 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.621% | 59.621% | 0.600 s | 208.842 MB | 259.598 MB | 1577.658 MB | 1655.348 MB | n/a MB | n/a MB |
| python3 | 28200 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.523 MB | 21.523 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| sh | 28199 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 28207 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.672 MB | 8.672 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 28206 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28218 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 45.682% | 74.382% | 2.760 s | 339.196 MB | 389.398 MB | 7759.444 MB | 10207.949 MB | n/a MB | n/a MB |
| MainThread | 28240 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 40.744% | 40.744% | 0.410 s | 187.795 MB | 228.875 MB | 1467.604 MB | 1632.223 MB | n/a MB | n/a MB |
| MainThread | 28266 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 50.146% | 86.441% | 3.030 s | 325.636 MB | 380.387 MB | 7694.243 MB | 10203.969 MB | n/a MB | n/a MB |
| MainThread | 28284 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 65.405% | 65.405% | 0.660 s | 234.113 MB | 279.289 MB | 1634.271 MB | 1674.320 MB | n/a MB | n/a MB |
| python3 | 28297 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.383 MB | 7.383 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 28296 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28314 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 38.966% | 65.434% | 2.750 s | 350.937 MB | 387.527 MB | 8063.107 MB | 10207.598 MB | n/a MB | n/a MB |
| MainThread | 28332 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 57.514% | 58.497% | 1.160 s | 204.676 MB | 303.801 MB | 1547.725 MB | 1727.867 MB | n/a MB | n/a MB |
| python3 | 28351 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.145 MB | 7.145 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 28350 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 28356 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.824 MB | 9.824 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 28355 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28360 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 35.678% | 63.670% | 2.520 s | 347.529 MB | 382.039 MB | 8062.255 MB | 10208.422 MB | n/a MB | n/a MB |
| MainThread | 28377 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.499% | 56.499% | 0.570 s | 199.955 MB | 241.301 MB | 1477.324 MB | 1638.840 MB | n/a MB | n/a MB |
| MainThread | 28405 | sandbox_agent_lsb-kimi_0000_0000 | 10 | 33.757% | 87.345% | 3.060 s | 338.684 MB | 392.496 MB | 8444.482 MB | 10208.016 MB | n/a MB | n/a MB |
| MainThread | 28433 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 81.324% | 81.324% | 0.820 s | 164.250 MB | 277.852 MB | 1455.705 MB | 1672.801 MB | n/a MB | n/a MB |
| MainThread | 28471 | sandbox_agent_lsb-kimi_0000_0000 | 44 | 10.072% | 90.304% | 4.360 s | 385.841 MB | 402.156 MB | 9811.845 MB | 10215.590 MB | n/a MB | n/a MB |
| MainThread | 28500 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 77.513% | 77.513% | 0.780 s | 217.383 MB | 294.750 MB | 1492.770 MB | 1689.188 MB | n/a MB | n/a MB |
| python | 28543 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 135.767% | 172.706% | 4.100 s | 2063.058 MB | 3752.871 MB | 2365.196 MB | 4198.840 MB | n/a MB | n/a MB |
| MainThread | 28560 | sandbox_agent_lsb-kimi_0000_0000 | 10 | 34.165% | 84.374% | 3.100 s | 345.886 MB | 392.586 MB | 8456.445 MB | 10213.621 MB | n/a MB | n/a MB |
| MainThread | 28591 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 287.375 MB | 287.375 MB | 1682.098 MB | 1682.098 MB | n/a MB | n/a MB |
| MainThread | 28616 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.531% | 73.501% | 2.950 s | 371.770 MB | 396.266 MB | 8992.718 MB | 10214.996 MB | n/a MB | n/a MB |
| MainThread | 28647 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 277.605 MB | 277.605 MB | 1672.805 MB | 1672.805 MB | n/a MB | n/a MB |
| sh | 28663 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 28664 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.520 MB | 7.520 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 28757 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 32.480% | 69.500% | 3.270 s | 356.825 MB | 394.969 MB | 8645.368 MB | 10212.945 MB | n/a MB | n/a MB |
| python3 | 28785 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.750 MB | 9.750 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 28784 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28776 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.609% | 59.609% | 0.600 s | 256.422 MB | 296.711 MB | 1673.119 MB | 1723.250 MB | n/a MB | n/a MB |
| MainThread | 28814 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 18.155% | 77.570% | 2.560 s | 377.803 MB | 402.844 MB | 9065.206 MB | 10206.395 MB | n/a MB | n/a MB |
| MainThread | 28833 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.389% | 61.389% | 0.620 s | 254.039 MB | 296.621 MB | 1656.846 MB | 1690.969 MB | n/a MB | n/a MB |
| sh | 28843 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 28844 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.289 MB | 9.289 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| python | 28858 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 152.097% | 174.234% | 3.070 s | 70.704 MB | 99.777 MB | 282.214 MB | 318.863 MB | n/a MB | n/a MB |
| MainThread | 28872 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 27.700% | 77.380% | 2.800 s | 350.691 MB | 388.328 MB | 8644.735 MB | 10208.172 MB | n/a MB | n/a MB |
| MainThread | 28900 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 86.481% | 86.481% | 0.870 s | 191.293 MB | 295.648 MB | 1487.137 MB | 1690.578 MB | n/a MB | n/a MB |
| MainThread | 28917 | sandbox_agent_lsb-kimi_0000_0000 | 22 | 13.527% | 80.441% | 2.860 s | 378.792 MB | 393.664 MB | 9433.983 MB | 10213.480 MB | n/a MB | n/a MB |
| MainThread | 28937 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.560% | 54.560% | 0.550 s | 256.113 MB | 294.738 MB | 1656.729 MB | 1689.727 MB | n/a MB | n/a MB |
| python3 | 28963 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.492 MB | 14.492 MB | 19.902 MB | 19.902 MB | n/a MB | n/a MB |
| sh | 28962 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 28974 | sandbox_agent_lsb-kimi_0000_0000 | 21 | 13.212% | 77.574% | 2.660 s | 384.333 MB | 398.648 MB | 9796.425 MB | 10214.047 MB | n/a MB | n/a MB |
| MainThread | 29004 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.539% | 53.539% | 0.540 s | 190.564 MB | 236.172 MB | 1468.695 MB | 1636.332 MB | n/a MB | n/a MB |
| python | 29020 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 160.406% | 171.040% | 3.230 s | 78.967 MB | 113.359 MB | 239.944 MB | 331.594 MB | n/a MB | n/a MB |
| MainThread | 29036 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 21.354% | 71.580% | 2.580 s | 368.644 MB | 390.910 MB | 9525.228 MB | 10211.621 MB | n/a MB | n/a MB |
| MainThread | 29056 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.466% | 62.466% | 0.630 s | 219.900 MB | 270.660 MB | 1622.143 MB | 1665.562 MB | n/a MB | n/a MB |
| MainThread | 29086 | sandbox_agent_lsb-kimi_0000_0000 | 35 | 12.267% | 87.259% | 4.240 s | 380.387 MB | 400.512 MB | 9468.685 MB | 10212.508 MB | n/a MB | n/a MB |
| python3 | 29105 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.500 MB | 8.500 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 29104 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 29110 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29111 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.391 MB | 8.391 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| MainThread | 29115 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.648 MB | 229.648 MB | 1632.328 MB | 1632.328 MB | n/a MB | n/a MB |
| python | 29141 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 156.057% | 156.057% | 1.570 s | 73.650 MB | 111.691 MB | 295.449 MB | 331.598 MB | n/a MB | n/a MB |
| sh | 29146 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 29145 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 29153 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 29158 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 20.518% | 86.408% | 3.720 s | 367.592 MB | 393.457 MB | 9296.112 MB | 10208.945 MB | n/a MB | n/a MB |
| MainThread | 29176 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.513% | 63.513% | 0.640 s | 229.855 MB | 271.871 MB | 1630.529 MB | 1667.086 MB | n/a MB | n/a MB |
| git | 29187 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.059 MB | 4.059 MB | n/a MB | n/a MB |
| MainThread | 29206 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 34.467% | 82.486% | 2.430 s | 360.638 MB | 394.051 MB | 8094.661 MB | 10212.855 MB | n/a MB | n/a MB |
| sh | 29230 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29231 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.117 MB | 7.117 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 29235 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 217.848 MB | 217.848 MB | 1624.008 MB | 1624.008 MB | n/a MB | n/a MB |
| MainThread | 29252 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 35.988% | 82.340% | 2.900 s | 346.875 MB | 390.363 MB | 8292.879 MB | 10209.332 MB | n/a MB | n/a MB |
| MainThread | 29286 | sandbox_agent_lsb-kimi_0000_0000 | 49 | 7.222% | 71.503% | 3.490 s | 394.147 MB | 406.387 MB | 9867.377 MB | 10221.453 MB | n/a MB | n/a MB |
| MainThread | 29322 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.514% | 60.514% | 0.610 s | 250.162 MB | 294.703 MB | 1654.225 MB | 1689.723 MB | n/a MB | n/a MB |
| MainThread | 29387 | sandbox_agent_lsb-kimi_0000_0000 | 23 | 13.050% | 75.510% | 2.890 s | 380.329 MB | 392.797 MB | 9472.852 MB | 10210.258 MB | n/a MB | n/a MB |
| python3 | 29420 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.461 MB | 10.461 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 29419 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 29409 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.622% | 52.622% | 0.530 s | 252.857 MB | 293.535 MB | 1655.629 MB | 1689.047 MB | n/a MB | n/a MB |
| python | 29434 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 131.398 MB | 131.398 MB | 352.160 MB | 352.160 MB | n/a MB | n/a MB |
| python3 | 29444 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.098 MB | 10.098 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 29443 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi | 29448 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 43.795% | 86.260% | 3.530 s | 318.464 MB | 391.746 MB | 7188.840 MB | 10208.820 MB | n/a MB | n/a MB |
| MainThread | 29470 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.457% | 60.457% | 0.610 s | 232.562 MB | 271.426 MB | 1640.623 MB | 1666.773 MB | n/a MB | n/a MB |
| MainThread | 29496 | sandbox_agent_lsb-kimi_0000_0000 | 25 | 14.822% | 68.307% | 3.590 s | 382.126 MB | 399.695 MB | 9525.417 MB | 10216.062 MB | n/a MB | n/a MB |
| bash | 29509 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| MainThread | 29513 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 58.418% | 60.529% | 1.180 s | 186.964 MB | 295.438 MB | 1497.367 MB | 1689.988 MB | n/a MB | n/a MB |
| python3 | 29526 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.559 MB | 10.559 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 29525 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 29540 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.668 MB | 2.668 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 29541 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 85.398 MB | 85.398 MB | 89.211 MB | 89.211 MB | n/a MB | n/a MB |
| MainThread | 29633 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.939% | 79.532% | 2.480 s | 376.198 MB | 395.621 MB | 9586.504 MB | 10212.281 MB | n/a MB | n/a MB |
| sh | 29654 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 29653 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 29655 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.527% | 55.527% | 0.560 s | 251.588 MB | 289.730 MB | 1654.551 MB | 1685.344 MB | n/a MB | n/a MB |
| MainThread | 29683 | sandbox_agent_lsb-kimi_0000_0000 | 23 | 14.536% | 75.569% | 3.220 s | 379.532 MB | 394.734 MB | 9466.164 MB | 10212.742 MB | n/a MB | n/a MB |
| MainThread | 29706 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 34.680% | 34.680% | 0.350 s | 178.672 MB | 211.555 MB | 1462.365 MB | 1622.996 MB | n/a MB | n/a MB |
| python3 | 29714 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.840 MB | 5.840 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sh | 29713 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 29727 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29728 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.168 MB | 21.168 MB | 26.938 MB | 26.938 MB | n/a MB | n/a MB |
| MainThread | 29742 | sandbox_agent_lsb-kimi_0000_0000 | 9 | 39.993% | 87.413% | 3.220 s | 326.783 MB | 390.254 MB | 8233.614 MB | 10209.918 MB | n/a MB | n/a MB |
| MainThread | 29760 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.524% | 59.524% | 0.600 s | 223.104 MB | 270.188 MB | 1628.252 MB | 1665.781 MB | n/a MB | n/a MB |
| kimi-code | 29783 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 56.828 MB | 56.828 MB | 900.508 MB | 900.508 MB | n/a MB | n/a MB |
| MainThread | 29788 | sandbox_agent_lsb-kimi_0000_0000 | 27 | 13.915% | 83.320% | 3.660 s | 378.148 MB | 395.906 MB | 9571.382 MB | 10208.996 MB | n/a MB | n/a MB |
| sh | 29813 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29814 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.258 MB | 9.258 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| python | 29822 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 158.149% | 170.351% | 3.190 s | 106.828 MB | 128.758 MB | 326.598 MB | 346.105 MB | n/a MB | n/a MB |
| MainThread | 29838 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 24.820% | 75.459% | 2.750 s | 369.076 MB | 397.562 MB | 8784.840 MB | 10212.691 MB | n/a MB | n/a MB |
| MainThread | 29859 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 44.640% | 44.640% | 0.450 s | 194.721 MB | 228.547 MB | 1474.533 MB | 1631.344 MB | n/a MB | n/a MB |
| sh | 29887 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29889 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.938 MB | 4.938 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| MainThread | 29908 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 27.282% | 80.121% | 3.300 s | 348.635 MB | 394.340 MB | 8222.260 MB | 10213.340 MB | n/a MB | n/a MB |
| MainThread | 29928 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.520% | 51.520% | 0.520 s | 242.514 MB | 278.766 MB | 1646.746 MB | 1674.039 MB | n/a MB | n/a MB |
| sh | 29938 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29939 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.086 MB | 10.086 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 29956 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 20.772% | 78.448% | 2.330 s | 370.799 MB | 391.535 MB | 8800.450 MB | 10212.117 MB | n/a MB | n/a MB |
| python3 | 29974 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.980 MB | 7.980 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 29973 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| kimi | 29984 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 63.056% | 63.056% | 0.680 s | 133.445 MB | 259.324 MB | 910.455 MB | 1655.320 MB | n/a MB | n/a MB |
| sh | 29979 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 29980 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.988 MB | 9.988 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| tar | 29992 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.270 MB | 2.270 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 29993 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.555 MB | 1.555 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| MainThread | 30003 | sandbox_agent_lsb-kimi_0000_0000 | 25 | 11.776% | 75.426% | 2.850 s | 385.412 MB | 397.340 MB | 9859.672 MB | 10210.691 MB | n/a MB | n/a MB |
| MainThread | 30024 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.552% | 52.552% | 0.530 s | 188.652 MB | 235.078 MB | 1467.129 MB | 1635.828 MB | n/a MB | n/a MB |
| python3 | 30037 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.184 MB | 7.184 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 30036 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 30051 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.867 MB | 22.867 MB | 215.410 MB | 215.410 MB | n/a MB | n/a MB |
| bash | 30050 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 40.193% | 67.502% | 0.810 s | 31.087 MB | 64.875 MB | 38.483 MB | 79.801 MB | n/a MB | n/a MB |
| MainThread | 30067 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.713% | 71.416% | 3.010 s | 364.087 MB | 390.562 MB | 8889.496 MB | 10212.676 MB | n/a MB | n/a MB |
| MainThread | 30086 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.950% | 57.950% | 0.590 s | 213.305 MB | 259.699 MB | 1616.408 MB | 1655.094 MB | n/a MB | n/a MB |
| MainThread | 30114 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 26.798% | 84.224% | 3.240 s | 358.840 MB | 395.227 MB | 8874.140 MB | 10213.758 MB | n/a MB | n/a MB |
| MainThread | 30134 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 50.650% | 54.663% | 1.020 s | 227.410 MB | 302.152 MB | 1554.574 MB | 1726.836 MB | n/a MB | n/a MB |
| MainThread | 30162 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 25.818% | 74.591% | 2.600 s | 371.638 MB | 401.441 MB | 8657.389 MB | 10212.906 MB | n/a MB | n/a MB |
| MainThread | 30186 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 37.691% | 37.691% | 0.380 s | 177.072 MB | 212.977 MB | 1459.824 MB | 1622.473 MB | n/a MB | n/a MB |
| MainThread | 30210 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.486% | 80.338% | 2.490 s | 373.948 MB | 396.195 MB | 8908.877 MB | 10212.297 MB | n/a MB | n/a MB |
| sh | 30234 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 30235 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.734 MB | 8.734 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 30239 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 296.281 MB | 296.281 MB | 1691.336 MB | 1691.336 MB | n/a MB | n/a MB |
| MainThread | 30274 | sandbox_agent_lsb-kimi_0000_0000 | 27 | 11.148% | 80.403% | 2.920 s | 387.601 MB | 400.422 MB | 9889.941 MB | 10216.145 MB | n/a MB | n/a MB |
| python3 | 30294 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.215 MB | 7.215 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 30293 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30295 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.618% | 53.618% | 0.540 s | 262.051 MB | 294.918 MB | 1661.020 MB | 1689.562 MB | n/a MB | n/a MB |
| python | 30321 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 4.936% | 14.808% | 0.150 s | 22.827 MB | 24.543 MB | 215.258 MB | 217.055 MB | n/a MB | n/a MB |
| bash | 30320 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.578 MB | 2.578 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 30325 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 15.402% | 30.803% | 0.310 s | 58.887 MB | 65.734 MB | 71.307 MB | 80.164 MB | n/a MB | n/a MB |
| python3 | 30327 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.316 MB | 20.316 MB | 25.320 MB | 25.320 MB | n/a MB | n/a MB |
| sh | 30326 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30343 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.497% | 79.381% | 2.490 s | 376.241 MB | 396.184 MB | 9540.251 MB | 10212.828 MB | n/a MB | n/a MB |
| python3 | 30363 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.855 MB | 9.855 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 30362 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 30377 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30367 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 50.555% | 50.555% | 0.510 s | 217.680 MB | 255.250 MB | 1621.289 MB | 1651.105 MB | n/a MB | n/a MB |
| MainThread | 30394 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.093% | 69.552% | 3.030 s | 366.086 MB | 399.609 MB | 8888.977 MB | 10209.066 MB | n/a MB | n/a MB |
| MainThread | 30421 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 80.495% | 80.495% | 0.810 s | 234.133 MB | 301.984 MB | 1652.131 MB | 1726.289 MB | n/a MB | n/a MB |
| MainThread | 30442 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.261% | 71.530% | 2.690 s | 376.498 MB | 402.008 MB | 9534.131 MB | 10213.426 MB | n/a MB | n/a MB |
| MainThread | 30459 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.482% | 58.482% | 0.590 s | 214.855 MB | 262.020 MB | 1618.029 MB | 1657.586 MB | n/a MB | n/a MB |
| MainThread | 30489 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.785% | 67.619% | 2.740 s | 374.229 MB | 396.320 MB | 9571.995 MB | 10212.539 MB | n/a MB | n/a MB |
| MainThread | 30508 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.486% | 57.486% | 0.580 s | 211.193 MB | 255.770 MB | 1614.531 MB | 1651.340 MB | n/a MB | n/a MB |
| MainThread | 30538 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 26.400% | 84.308% | 3.480 s | 351.500 MB | 397.805 MB | 8355.898 MB | 10212.883 MB | n/a MB | n/a MB |
| python3 | 30565 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.031 MB | 9.031 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| kimi | 30566 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.507% | 57.507% | 0.610 s | 127.783 MB | 229.164 MB | 898.904 MB | 1631.961 MB | n/a MB | n/a MB |
| sh | 30564 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| tar | 30582 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.426 MB | 1.426 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| tar | 30581 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.039 MB | 2.039 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| MainThread | 30607 | sandbox_agent_lsb-kimi_0000_0000 | 12 | 27.271% | 75.449% | 3.080 s | 363.378 MB | 399.398 MB | 8778.524 MB | 10213.562 MB | n/a MB | n/a MB |
| MainThread | 30684 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.270% | 53.270% | 0.540 s | 210.295 MB | 253.480 MB | 1613.928 MB | 1649.633 MB | n/a MB | n/a MB |
| sh | 30696 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30712 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.550% | 80.549% | 2.950 s | 371.562 MB | 392.367 MB | 8994.281 MB | 10214.379 MB | n/a MB | n/a MB |
| python3 | 30734 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.062 MB | 9.062 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| sh | 30733 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30740 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 74.549% | 74.549% | 0.750 s | 222.482 MB | 286.141 MB | 1590.766 MB | 1681.562 MB | n/a MB | n/a MB |
| MainThread | 30759 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 20.288% | 75.370% | 3.120 s | 369.604 MB | 396.082 MB | 9135.470 MB | 10213.391 MB | n/a MB | n/a MB |
| MainThread | 30780 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.260% | 56.260% | 0.570 s | 211.246 MB | 255.645 MB | 1614.771 MB | 1651.570 MB | n/a MB | n/a MB |
| MainThread | 30808 | sandbox_agent_lsb-kimi_0000_0000 | 7 | 43.370% | 70.423% | 2.620 s | 339.841 MB | 383.711 MB | 7757.589 MB | 10210.484 MB | n/a MB | n/a MB |
| MainThread | 30832 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 199.230 MB | 199.230 MB | 1617.488 MB | 1617.488 MB | n/a MB | n/a MB |
| MainThread | 30858 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.480% | 80.546% | 2.420 s | 372.909 MB | 391.973 MB | 9586.364 MB | 10213.426 MB | n/a MB | n/a MB |
| kimi-code | 30875 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 44.844 MB | 44.844 MB | 836.945 MB | 836.945 MB | n/a MB | n/a MB |
| MainThread | 30877 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.460% | 54.460% | 0.550 s | 262.826 MB | 296.559 MB | 1677.869 MB | 1723.500 MB | n/a MB | n/a MB |
| MainThread | 30905 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 17.594% | 77.536% | 2.480 s | 378.386 MB | 397.457 MB | 9628.616 MB | 10212.609 MB | n/a MB | n/a MB |
| python3 | 30924 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.992 MB | 6.992 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 30923 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 30925 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 50.633% | 50.633% | 0.510 s | 263.588 MB | 298.164 MB | 1677.889 MB | 1724.066 MB | n/a MB | n/a MB |
| MainThread | 30954 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.096% | 72.546% | 2.920 s | 365.004 MB | 397.477 MB | 8892.549 MB | 10213.824 MB | n/a MB | n/a MB |
| MainThread | 30981 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 78.420% | 78.420% | 0.790 s | 231.863 MB | 297.109 MB | 1634.969 MB | 1691.715 MB | n/a MB | n/a MB |
| MainThread | 31004 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.462% | 62.653% | 2.480 s | 372.457 MB | 401.461 MB | 8887.680 MB | 10209.480 MB | n/a MB | n/a MB |
| MainThread | 31021 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.574% | 54.574% | 0.550 s | 196.055 MB | 237.238 MB | 1474.250 MB | 1637.629 MB | n/a MB | n/a MB |
| kimi-code | 31044 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 59.375 MB | 59.375 MB | 893.219 MB | 893.219 MB | n/a MB | n/a MB |
| MainThread | 31051 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.752% | 81.319% | 3.140 s | 362.416 MB | 396.055 MB | 8882.011 MB | 10212.637 MB | n/a MB | n/a MB |
| MainThread | 31076 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.887% | 62.887% | 0.670 s | 238.391 MB | 294.035 MB | 1640.768 MB | 1688.812 MB | n/a MB | n/a MB |
| MainThread | 31100 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 21.272% | 70.453% | 2.580 s | 374.147 MB | 394.973 MB | 9537.271 MB | 10213.488 MB | n/a MB | n/a MB |
| MainThread | 31119 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.555% | 57.555% | 0.580 s | 208.879 MB | 253.453 MB | 1611.145 MB | 1649.816 MB | n/a MB | n/a MB |
| MainThread | 31149 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 18.537% | 78.550% | 2.440 s | 378.250 MB | 395.582 MB | 9589.702 MB | 10213.645 MB | n/a MB | n/a MB |
| sh | 31166 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31167 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.871 MB | 9.871 MB | 13.520 MB | 13.520 MB | n/a MB | n/a MB |
| MainThread | 31179 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 158.012 MB | 158.012 MB | 1499.969 MB | 1499.969 MB | n/a MB | n/a MB |
| MainThread | 31198 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 27.142% | 86.326% | 3.570 s | 362.597 MB | 396.832 MB | 8970.442 MB | 10213.496 MB | n/a MB | n/a MB |
| sh | 31216 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31217 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.359 MB | 5.359 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| MainThread | 31228 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 91.365% | 91.365% | 0.920 s | 172.523 MB | 286.832 MB | 1459.828 MB | 1681.047 MB | n/a MB | n/a MB |
| python3 | 31243 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.109 MB | 10.109 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| sh | 31242 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 31247 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 25.149% | 88.217% | 3.810 s | 364.590 MB | 398.562 MB | 9116.527 MB | 10210.363 MB | n/a MB | n/a MB |
| MainThread | 31264 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.484% | 59.484% | 0.600 s | 220.219 MB | 259.645 MB | 1623.533 MB | 1655.844 MB | n/a MB | n/a MB |
| sh | 31283 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31284 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.000 MB | 9.000 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| MainThread | 31295 | sandbox_agent_lsb-kimi_0000_0000 | 11 | 25.609% | 69.498% | 2.580 s | 367.842 MB | 400.168 MB | 8652.708 MB | 10210.363 MB | n/a MB | n/a MB |
| MainThread | 31314 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.379% | 57.379% | 0.580 s | 227.822 MB | 271.137 MB | 1630.016 MB | 1667.059 MB | n/a MB | n/a MB |
| MainThread | 31342 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.775% | 63.401% | 2.760 s | 370.375 MB | 395.043 MB | 8983.261 MB | 10210.441 MB | n/a MB | n/a MB |
| bash | 31355 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.762 MB | 2.762 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 31361 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 58.496% | 58.496% | 0.590 s | 170.598 MB | 235.148 MB | 1459.768 MB | 1635.840 MB | n/a MB | n/a MB |
| MainThread | 31410 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.351% | 65.566% | 2.700 s | 364.755 MB | 392.875 MB | 8893.061 MB | 10212.469 MB | n/a MB | n/a MB |
| sh | 31433 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31434 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.902 MB | 9.902 MB | 14.676 MB | 14.676 MB | n/a MB | n/a MB |
| MainThread | 31435 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 205.629 MB | 205.629 MB | 1618.965 MB | 1618.965 MB | n/a MB | n/a MB |
| MainThread | 31459 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 18.797% | 78.563% | 2.270 s | 369.670 MB | 389.332 MB | 9539.222 MB | 10210.402 MB | n/a MB | n/a MB |
| MainThread | 31482 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.578% | 61.578% | 0.620 s | 242.193 MB | 290.125 MB | 1649.770 MB | 1684.816 MB | n/a MB | n/a MB |
| sh | 31492 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31493 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.219 MB | 8.219 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| python3 | 31504 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.027 MB | 8.027 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 31503 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.590 MB | 1.590 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 31508 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 20.191% | 82.373% | 3.050 s | 367.921 MB | 397.637 MB | 9122.538 MB | 10210.043 MB | n/a MB | n/a MB |
| MainThread | 31527 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.624% | 56.624% | 0.570 s | 205.986 MB | 256.633 MB | 1575.893 MB | 1652.316 MB | n/a MB | n/a MB |
| MainThread | 31556 | sandbox_agent_lsb-kimi_0000_0000 | 27 | 11.722% | 75.521% | 3.070 s | 387.656 MB | 400.824 MB | 9577.887 MB | 10212.164 MB | n/a MB | n/a MB |
| sh | 31588 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 31577 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.477% | 53.477% | 0.540 s | 244.756 MB | 285.922 MB | 1649.631 MB | 1680.785 MB | n/a MB | n/a MB |
| python3 | 31589 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.527 MB | 10.527 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| python | 31604 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.645 MB | 20.645 MB | 212.328 MB | 212.328 MB | n/a MB | n/a MB |
| bash | 31603 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.707 MB | 2.707 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| MainThread | 31621 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 39.805% | 76.428% | 2.810 s | 355.261 MB | 394.906 MB | 8071.546 MB | 10213.789 MB | n/a MB | n/a MB |
| MainThread | 31647 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.318% | 62.318% | 0.630 s | 236.375 MB | 283.793 MB | 1636.252 MB | 1678.531 MB | n/a MB | n/a MB |
| MainThread | 31671 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 21.176% | 70.481% | 3.200 s | 373.840 MB | 397.215 MB | 9140.670 MB | 10212.523 MB | n/a MB | n/a MB |
| MainThread | 31699 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 224.488 MB | 224.488 MB | 1627.473 MB | 1627.473 MB | n/a MB | n/a MB |
| MainThread | 31798 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.624% | 71.464% | 3.050 s | 369.763 MB | 397.949 MB | 9062.552 MB | 10210.609 MB | n/a MB | n/a MB |
| MainThread | 31818 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.400% | 57.400% | 0.580 s | 215.766 MB | 260.258 MB | 1617.896 MB | 1656.070 MB | n/a MB | n/a MB |
| python3 | 31833 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.832 MB | 7.832 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 31832 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.398 MB | 1.398 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 31849 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.141% | 70.490% | 2.980 s | 371.277 MB | 397.883 MB | 9070.854 MB | 10213.570 MB | n/a MB | n/a MB |
| MainThread | 31880 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 83.312% | 83.312% | 0.840 s | 159.119 MB | 288.977 MB | 973.555 MB | 1683.801 MB | n/a MB | n/a MB |
| tar | 31892 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.254 MB | 2.254 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| gzip | 31893 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| MainThread | 31899 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 25.132% | 84.480% | 3.290 s | 359.960 MB | 399.672 MB | 8948.335 MB | 10210.547 MB | n/a MB | n/a MB |
| sh | 31918 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 31919 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.262 MB | 7.262 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| MainThread | 31920 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 43.709% | 43.709% | 0.440 s | 262.182 MB | 294.863 MB | 1660.543 MB | 1689.086 MB | n/a MB | n/a MB |
| MainThread | 31948 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 25.594% | 81.478% | 3.100 s | 361.824 MB | 396.812 MB | 8879.551 MB | 10214.414 MB | n/a MB | n/a MB |
| MainThread | 31978 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 229.398 MB | 229.398 MB | 1632.477 MB | 1632.477 MB | n/a MB | n/a MB |
| MainThread | 31997 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.699% | 68.560% | 2.710 s | 374.942 MB | 398.164 MB | 8985.164 MB | 10210.008 MB | n/a MB | n/a MB |
| MainThread | 32014 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.516% | 57.516% | 0.580 s | 212.984 MB | 259.074 MB | 1616.525 MB | 1655.328 MB | n/a MB | n/a MB |
| MainThread | 32045 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 23.733% | 87.371% | 3.360 s | 355.801 MB | 399.734 MB | 9023.623 MB | 10210.492 MB | n/a MB | n/a MB |
| MainThread | 32062 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 62.512% | 62.512% | 0.630 s | 223.119 MB | 270.938 MB | 1628.268 MB | 1666.312 MB | n/a MB | n/a MB |
| kimi-code | 32073 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 50.621 MB | 50.621 MB | 851.293 MB | 851.293 MB | n/a MB | n/a MB |
| MainThread | 32092 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 27.969% | 82.393% | 3.380 s | 350.950 MB | 399.488 MB | 8844.159 MB | 10212.922 MB | n/a MB | n/a MB |
| sh | 32117 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 32118 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.969 MB | 7.969 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| MainThread | 32122 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 261.012 MB | 261.012 MB | 1656.570 MB | 1656.570 MB | n/a MB | n/a MB |
| MainThread | 32141 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 24.131% | 75.490% | 3.160 s | 363.334 MB | 393.969 MB | 8980.132 MB | 10213.066 MB | n/a MB | n/a MB |
| MainThread | 32158 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 59.393% | 59.393% | 0.600 s | 250.242 MB | 294.793 MB | 1654.096 MB | 1689.219 MB | n/a MB | n/a MB |
| sh | 32166 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 32167 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.324 MB | 7.324 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 32172 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 32173 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.617 MB | 6.617 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| tar | 32183 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.004 MB | 0.004 MB | n/a MB | n/a MB |
| MainThread | 32190 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 24.604% | 88.257% | 3.470 s | 356.597 MB | 399.289 MB | 9032.780 MB | 10216.762 MB | n/a MB | n/a MB |
| MainThread | 32209 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 54.488% | 54.488% | 0.550 s | 242.961 MB | 280.387 MB | 1647.145 MB | 1675.312 MB | n/a MB | n/a MB |
| sh | 32220 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| MainThread | 32239 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.636% | 80.328% | 2.980 s | 360.706 MB | 396.066 MB | 8883.761 MB | 10206.379 MB | n/a MB | n/a MB |
| MainThread | 32260 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 70.514% | 70.514% | 0.710 s | 235.082 MB | 295.438 MB | 1635.971 MB | 1689.969 MB | n/a MB | n/a MB |
| MainThread | 32286 | sandbox_agent_lsb-kimi_0000_0000 | 16 | 16.339% | 69.495% | 2.470 s | 381.480 MB | 399.465 MB | 9664.357 MB | 10212.855 MB | n/a MB | n/a MB |
| MainThread | 32304 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.552% | 57.552% | 0.580 s | 229.652 MB | 274.438 MB | 1631.389 MB | 1669.805 MB | n/a MB | n/a MB |
| kimi | 32334 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 25.055% | 90.430% | 3.280 s | 350.596 MB | 400.172 MB | 8867.376 MB | 10210.715 MB | n/a MB | n/a MB |
| MainThread | 32353 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.518% | 56.518% | 0.570 s | 227.838 MB | 269.348 MB | 1629.258 MB | 1664.793 MB | n/a MB | n/a MB |
| MainThread | 32383 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.826% | 70.586% | 2.760 s | 372.053 MB | 398.535 MB | 8897.673 MB | 10216.309 MB | n/a MB | n/a MB |
| MainThread | 32402 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.288% | 55.288% | 0.560 s | 230.482 MB | 271.973 MB | 1630.600 MB | 1666.727 MB | n/a MB | n/a MB |
| sh | 32412 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.129 MB | 0.129 MB | n/a MB | n/a MB |
| MainThread | 32431 | sandbox_agent_lsb-kimi_0000_0000 | 18 | 18.047% | 74.547% | 3.090 s | 374.549 MB | 402.051 MB | 9257.537 MB | 10214.652 MB | n/a MB | n/a MB |
| MainThread | 32473 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 70.256% | 70.256% | 0.710 s | 222.457 MB | 289.203 MB | 1591.508 MB | 1683.547 MB | n/a MB | n/a MB |
| MainThread | 32497 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.188% | 62.540% | 2.990 s | 374.928 MB | 401.750 MB | 9066.764 MB | 10214.039 MB | n/a MB | n/a MB |
| MainThread | 32516 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.531% | 55.531% | 0.560 s | 165.291 MB | 229.285 MB | 1457.785 MB | 1631.875 MB | n/a MB | n/a MB |
| python3 | 32525 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.891 MB | 9.891 MB | 13.734 MB | 13.734 MB | n/a MB | n/a MB |
| sh | 32524 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 32549 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 20.699% | 67.571% | 2.760 s | 370.783 MB | 392.531 MB | 9583.968 MB | 10212.594 MB | n/a MB | n/a MB |
| MainThread | 32568 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.389% | 57.389% | 0.580 s | 212.318 MB | 255.379 MB | 1615.045 MB | 1651.117 MB | n/a MB | n/a MB |
| MainThread | 32599 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 22.508% | 74.437% | 2.720 s | 372.317 MB | 399.613 MB | 8897.386 MB | 10216.840 MB | n/a MB | n/a MB |
| MainThread | 32620 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.545% | 57.545% | 0.580 s | 236.479 MB | 278.031 MB | 1643.887 MB | 1672.801 MB | n/a MB | n/a MB |
| MainThread | 32648 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 22.702% | 76.374% | 2.980 s | 376.345 MB | 399.887 MB | 8987.858 MB | 10214.293 MB | n/a MB | n/a MB |
| MainThread | 32670 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.062% | 57.062% | 0.580 s | 209.381 MB | 247.035 MB | 1611.271 MB | 1642.570 MB | n/a MB | n/a MB |
| MainThread | 32698 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 24.540% | 73.345% | 3.280 s | 371.336 MB | 396.293 MB | 8986.741 MB | 10213.230 MB | n/a MB | n/a MB |
| env | 32711 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.418 MB | 0.418 MB | n/a MB | n/a MB |
| git | 32720 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| MainThread | 32724 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.231% | 55.231% | 0.640 s | 238.807 MB | 280.602 MB | 1646.508 MB | 1676.051 MB | n/a MB | n/a MB |
| git | 32743 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.059 MB | 4.059 MB | n/a MB | n/a MB |
| MainThread | 32746 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 28.705% | 89.217% | 3.760 s | 361.448 MB | 397.988 MB | 8362.751 MB | 10213.684 MB | n/a MB | n/a MB |
| MainThread | 32777 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 167.016 MB | 167.016 MB | 1577.973 MB | 1577.973 MB | n/a MB | n/a MB |
| MainThread | 32873 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 24.715% | 74.373% | 3.000 s | 368.163 MB | 399.094 MB | 8887.918 MB | 10214.473 MB | n/a MB | n/a MB |
| MainThread | 32892 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 53.429% | 53.429% | 0.540 s | 214.600 MB | 259.320 MB | 1616.914 MB | 1655.105 MB | n/a MB | n/a MB |
| python3 | 32905 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.676 MB | 8.676 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 32904 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| gzip | 32914 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 3.273 MB | 3.273 MB | n/a MB | n/a MB |
| tar | 32913 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.270 MB | 2.270 MB | 3.730 MB | 3.730 MB | n/a MB | n/a MB |
| MainThread | 32920 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 21.637% | 84.431% | 3.060 s | 358.084 MB | 398.145 MB | 9030.936 MB | 10213.387 MB | n/a MB | n/a MB |
| sh | 32953 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 32954 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.344 MB | 10.344 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| MainThread | 32945 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.500% | 61.500% | 0.630 s | 241.592 MB | 295.113 MB | 1641.846 MB | 1689.719 MB | n/a MB | n/a MB |
| MainThread | 32969 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 20.855% | 69.618% | 2.520 s | 373.481 MB | 397.156 MB | 9529.600 MB | 10213.613 MB | n/a MB | n/a MB |
| python3 | 33000 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.645 MB | 7.645 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 32992 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 41.615% | 41.615% | 0.420 s | 148.680 MB | 212.758 MB | 1453.092 MB | 1622.488 MB | n/a MB | n/a MB |
| sh | 32999 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33014 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.797 MB | 7.797 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 33013 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 33018 | sandbox_agent_lsb-kimi_0000_0000 | 20 | 16.981% | 81.454% | 3.250 s | 377.130 MB | 401.805 MB | 9349.594 MB | 10215.637 MB | n/a MB | n/a MB |
| python3 | 33051 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.320 MB | 7.320 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| MainThread | 33040 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 57.231% | 57.231% | 0.580 s | 244.789 MB | 294.621 MB | 1652.135 MB | 1689.297 MB | n/a MB | n/a MB |
| sh | 33050 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 33069 | sandbox_agent_lsb-kimi_0000_0000 | 15 | 20.789% | 69.564% | 2.930 s | 372.279 MB | 401.578 MB | 9066.033 MB | 10213.680 MB | n/a MB | n/a MB |
| MainThread | 33090 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 60.515% | 60.515% | 0.610 s | 222.861 MB | 270.281 MB | 1627.895 MB | 1665.566 MB | n/a MB | n/a MB |
| sh | 33102 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33103 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.676 MB | 7.676 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| MainThread | 33119 | sandbox_agent_lsb-kimi_0000_0000 | 8 | 33.119% | 75.584% | 2.340 s | 364.607 MB | 395.586 MB | 9120.733 MB | 10214.953 MB | n/a MB | n/a MB |
| python3 | 33145 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.562 MB | 10.562 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 33144 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 33150 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 168.383 MB | 168.383 MB | 1578.473 MB | 1578.473 MB | n/a MB | n/a MB |
| MainThread | 33169 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 16.542% | 69.463% | 3.000 s | 376.172 MB | 394.703 MB | 9312.389 MB | 10215.512 MB | n/a MB | n/a MB |
| bash | 33182 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.914 MB | 2.914 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 33183 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.508 MB | 1.508 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sh | 33190 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33191 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.262 MB | 10.262 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| sh | 33202 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33203 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.602 MB | 7.602 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| kimi | 33207 | sandbox_agent_lsb-kimi_0000_0000 | 13 | 29.538% | 86.327% | 3.570 s | 346.688 MB | 399.969 MB | 8137.092 MB | 10215.309 MB | n/a MB | n/a MB |
| MainThread | 33236 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 80.502% | 80.502% | 0.810 s | 234.209 MB | 295.953 MB | 1635.092 MB | 1690.211 MB | n/a MB | n/a MB |
| MainThread | 33255 | sandbox_agent_lsb-kimi_0000_0000 | 14 | 25.721% | 87.222% | 3.380 s | 354.165 MB | 404.105 MB | 8923.227 MB | 10181.730 MB | n/a MB | n/a MB |
| MainThread | 33274 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.404% | 61.404% | 0.620 s | 218.330 MB | 260.996 MB | 1623.016 MB | 1656.059 MB | n/a MB | n/a MB |
| python3 | 33293 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.297 MB | 9.297 MB | 13.359 MB | 13.359 MB | n/a MB | n/a MB |
| sh | 33292 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| MainThread | 33304 | sandbox_agent_lsb-kimi_0000_0000 | 149 | 5.495% | 80.357% | 8.190 s | 397.485 MB | 416.668 MB | 10098.797 MB | 10228.473 MB | n/a MB | n/a MB |
| MainThread | 33321 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 61.489% | 61.489% | 0.620 s | 250.568 MB | 295.062 MB | 1654.369 MB | 1689.742 MB | n/a MB | n/a MB |
| bash | 33353 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.656 MB | 2.656 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 33354 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 131.865% | 131.865% | 1.330 s | 1102.213 MB | 1971.074 MB | 1447.199 MB | 2193.543 MB | n/a MB | n/a MB |
| python3 | 33377 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.668 MB | 9.668 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sh | 33376 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33406 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.922 MB | 7.922 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 33405 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 33412 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.770 MB | 15.770 MB | 208.867 MB | 208.867 MB | n/a MB | n/a MB |
| python3 | 33422 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.129 MB | 10.129 MB | 14.059 MB | 14.059 MB | n/a MB | n/a MB |
| sh | 33421 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 33431 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33432 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.859 MB | 6.859 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python | 33439 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 166.511% | 166.511% | 1.680 s | 53.504 MB | 82.152 MB | 258.607 MB | 300.105 MB | n/a MB | n/a MB |
| python3 | 33451 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.629 MB | 10.629 MB | 15.270 MB | 15.270 MB | n/a MB | n/a MB |
| sh | 33450 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33465 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.195 MB | 7.195 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 33464 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 33471 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33472 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.449 MB | 7.449 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 33479 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 155.350% | 171.939% | 3.130 s | 44.431 MB | 89.379 MB | 190.590 MB | 307.590 MB | n/a MB | n/a MB |
| python | 33494 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.297 MB | 9.297 MB | 13.410 MB | 13.410 MB | n/a MB | n/a MB |
| bash | 33493 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.699 MB | 2.699 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 33506 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 174.432% | 174.432% | 1.760 s | 89.211 MB | 90.023 MB | 307.586 MB | 307.586 MB | n/a MB | n/a MB |
| MainThread | 33521 | sandbox_agent_lsb-kimi_0000_0000 | 39 | 10.703% | 67.541% | 4.100 s | 389.710 MB | 401.574 MB | 9773.976 MB | 10216.941 MB | n/a MB | n/a MB |
| env | 33535 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.418 MB | 0.418 MB | n/a MB | n/a MB |
| MainThread | 33541 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 52.372% | 52.372% | 0.530 s | 217.146 MB | 259.457 MB | 1618.777 MB | 1655.582 MB | n/a MB | n/a MB |
| python3 | 33554 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.609 MB | 8.609 MB | 13.184 MB | 13.184 MB | n/a MB | n/a MB |
| sh | 33553 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33650 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.609 MB | 21.609 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 33649 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 33668 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 172.962% | 173.583% | 3.510 s | 90.077 MB | 90.590 MB | 307.404 MB | 307.406 MB | n/a MB | n/a MB |
| MainThread | 33683 | sandbox_agent_lsb-kimi_0000_0000 | 25 | 15.550% | 80.560% | 3.760 s | 375.558 MB | 392.379 MB | 9524.662 MB | 10213.707 MB | n/a MB | n/a MB |
| MainThread | 33713 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 187.250 MB | 187.250 MB | 1593.973 MB | 1593.973 MB | n/a MB | n/a MB |
| python | 33727 | sandbox_agent_lsb-kimi_0000_0000 | 3 | 171.884% | 176.325% | 3.470 s | 89.467 MB | 90.172 MB | 307.401 MB | 307.402 MB | n/a MB | n/a MB |
| sh | 33734 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33735 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.543 MB | 9.543 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| bash | 33742 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 157.060% | 172.016% | 4.740 s | 68.017 MB | 90.258 MB | 231.513 MB | 307.402 MB | n/a MB | n/a MB |
| python | 33743 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.801 MB | 8.801 MB | 13.164 MB | 13.164 MB | n/a MB | n/a MB |
| MainThread | 33757 | sandbox_agent_lsb-kimi_0000_0000 | 19 | 19.450% | 71.392% | 3.530 s | 374.082 MB | 395.672 MB | 9306.995 MB | 10213.488 MB | n/a MB | n/a MB |
| MainThread | 33777 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 55.489% | 55.489% | 0.560 s | 217.912 MB | 260.855 MB | 1623.389 MB | 1657.055 MB | n/a MB | n/a MB |
| python | 33804 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.352 MB | 5.352 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| bash | 33803 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 157.220% | 176.205% | 4.760 s | 68.186 MB | 90.383 MB | 231.518 MB | 307.410 MB | n/a MB | n/a MB |
| MainThread | 33825 | sandbox_agent_lsb-kimi_0000_0000 | 48 | 9.865% | 61.669% | 4.670 s | 387.576 MB | 399.148 MB | 9857.814 MB | 10219.363 MB | n/a MB | n/a MB |
| MainThread | 33842 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 56.462% | 56.462% | 0.570 s | 146.686 MB | 229.043 MB | 1437.355 MB | 1636.102 MB | n/a MB | n/a MB |
| sh | 33850 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33851 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.078 MB | 7.078 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 33867 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 33868 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.805 MB | 8.805 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| python | 33877 | sandbox_agent_lsb-kimi_0000_0000 | 4 | 167.528% | 171.521% | 5.060 s | 85.154 MB | 106.348 MB | 296.391 MB | 323.438 MB | n/a MB | n/a MB |
| python3 | 33890 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.883 MB | 18.883 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| sh | 33889 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python | 33897 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 64.536% | 64.536% | 0.650 s | 44.348 MB | 63.660 MB | 54.158 MB | 77.957 MB | n/a MB | n/a MB |
| python | 33906 | sandbox_agent_lsb-kimi_0000_0000 | 2 | 51.604% | 51.604% | 0.520 s | 52.676 MB | 66.008 MB | 64.051 MB | 80.309 MB | n/a MB | n/a MB |
| python3 | 33916 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.453 MB | 21.453 MB | 26.977 MB | 26.977 MB | n/a MB | n/a MB |
| sh | 33915 | sandbox_agent_lsb-kimi_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| docker | 33951 |  | 22 | 0.000% | 0.000% | 0.000 s | 29.309 MB | 29.309 MB | 1835.016 MB | 1835.016 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.556% | 100.000% | 11913.964 MB | 12352.000 MB | 28.709 W | 73.562 W | 140410.660 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-kimi_0000_0000 | 79.563% | 232.584% | 3888.789 s | 607.689 MB | 4385.340 MB | 169.703125 MB | 702.023438 MB | 447.722233 MB | 5.963037 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 17041 | 4891.743 | interrupted |
| harness:retire | -1 | 11.591 | interrupted |
| harness:retire | -1 | 6.588 | interrupted |
| harness:retire | -1 | 0.450 | interrupted |
| harness:retire | -1 | 0.142 | interrupted |
| harness:retire | -1 | 0.137 | interrupted |
| harness:retire | -1 | 0.137 | interrupted |
| harness:retire | -1 | 0.135 | interrupted |
| harness:retire | -1 | 0.133 | interrupted |
| harness:retire | -1 | 0.133 | interrupted |
| harness:retire | -1 | 0.133 | interrupted |
| harness:retire | -1 | 0.132 | interrupted |
| harness:retire | -1 | 0.131 | interrupted |
| harness:retire | -1 | 0.131 | interrupted |
| harness:retire | -1 | 0.131 | interrupted |
| harness:retire | -1 | 0.130 | interrupted |
| harness:retire | -1 | 0.130 | interrupted |
| harness:retire | -1 | 0.129 | interrupted |
| harness:retire | -1 | 0.129 | interrupted |
| harness:retire | -1 | 0.128 | interrupted |
| harness:retire | -1 | 0.128 | interrupted |
| harness:retire | -1 | 0.127 | interrupted |
| harness:retire | -1 | 0.127 | interrupted |
| harness:retire | -1 | 0.127 | interrupted |
| harness:retire | -1 | 0.127 | interrupted |
| harness:retire | -1 | 0.125 | interrupted |
| harness:retire | -1 | 0.125 | interrupted |
| harness:retire | -1 | 0.125 | interrupted |
| harness:retire | -1 | 0.125 | interrupted |
| harness:retire | -1 | 0.124 | interrupted |
| harness:retire | -1 | 0.124 | interrupted |
| harness:retire | -1 | 0.124 | interrupted |
| harness:retire | -1 | 0.123 | interrupted |
| harness:retire | -1 | 0.122 | interrupted |
| harness:retire | -1 | 0.122 | interrupted |
| harness:retire | -1 | 0.122 | interrupted |
| harness:retire | -1 | 0.121 | interrupted |
| harness:retire | -1 | 0.121 | interrupted |
| harness:retire | -1 | 0.121 | interrupted |
| harness:retire | -1 | 0.121 | interrupted |
| harness:retire | -1 | 0.121 | interrupted |
| harness:retire | -1 | 0.121 | interrupted |
| harness:retire | -1 | 0.120 | interrupted |
| harness:retire | -1 | 0.120 | interrupted |
| harness:retire | -1 | 0.120 | interrupted |
| harness:retire | -1 | 0.120 | interrupted |
| harness:retire | -1 | 0.120 | interrupted |
| harness:retire | -1 | 0.120 | interrupted |
| harness:retire | -1 | 0.120 | interrupted |
| harness:retire | -1 | 0.119 | interrupted |
| harness:retire | -1 | 0.119 | interrupted |
| harness:retire | -1 | 0.119 | interrupted |
| harness:retire | -1 | 0.119 | interrupted |
| harness:retire | -1 | 0.119 | interrupted |
| harness:retire | -1 | 0.118 | interrupted |
| harness:retire | -1 | 0.118 | interrupted |
| harness:retire | -1 | 0.118 | interrupted |
| harness:retire | -1 | 0.118 | interrupted |
| harness:retire | -1 | 0.118 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.117 | interrupted |
| harness:retire | -1 | 0.116 | interrupted |
| harness:retire | -1 | 0.116 | interrupted |
| harness:retire | -1 | 0.116 | interrupted |
| harness:retire | -1 | 0.116 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.115 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
| harness:retire | -1 | 0.114 | interrupted |
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
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.107 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.106 | interrupted |
| harness:retire | -1 | 0.105 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.104 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.103 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.102 | interrupted |
| harness:retire | -1 | 0.101 | interrupted |
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
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.099 | interrupted |
| harness:retire | -1 | 0.098 | interrupted |
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
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.096 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.095 | interrupted |
| harness:retire | -1 | 0.094 | interrupted |
| harness:retire | -1 | 0.094 | interrupted |
| harness:retire | -1 | 0.093 | interrupted |
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
| harness:retire | -1 | 0.090 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
| harness:retire | -1 | 0.089 | interrupted |
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
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
| harness:retire | -1 | 0.087 | interrupted |
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
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.084 | interrupted |
| harness:retire | -1 | 0.083 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.082 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.081 | interrupted |
| harness:retire | -1 | 0.079 | interrupted |
| harness:retire | -1 | 0.078 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 4885.373 | n/a | n/a | 169.703 | 4885372.815 | 4885372.815 | 4885372.815 |
| engine:execute | 1/1 | 0 | 0 | 4885.371 | 2.533 | 4882.837 | 169.703 | 4885370.931 | 4885370.931 | 4885370.931 |
| harness:attempt_rpc | 270/270 | 0 | 0 | 4836.286 | 9.809 | 4826.475 | 137.795 | 17912.169 | 14222.064 | 35508.886 |
| harness:await_cli | 270/270 | 0 | 0 | 3497.013 | n/a | n/a | 26.053 | 12951.901 | 9486.415 | 30920.017 |
| llm:attempt | 493/493 | 67 | 0 | 3183.029 | 76.230 | 3106.177 | 11.468 | 6456.449 | 6195.762 | 11457.526 |
| harness:startup_ready | 270/270 | 0 | 0 | 888.118 | n/a | n/a | 10.553 | 3289.326 | 3241.346 | 4099.006 |
| harness:submit | 270/270 | 0 | 0 | 242.532 | n/a | n/a | 2.605 | 898.266 | 906.153 | 1166.551 |
| tool:Bash | 79/79 | 28 | 0 | 183.595 | n/a | n/a | 9.478 | 2323.984 | 1292.629 | 8172.610 |
| syscall:connect | 9061/9061 | 0 | 0 | 25.786 | n/a | n/a | 0.921 | 2.846 | 2.308 | 5.422 |
| run:container_call | 13/13 | 0 | 0 | 22.977 | 0.003 | 22.973 | 0.000 | 1767.430 | 44.084 | 9040.364 |
| teardown:commit | 1/1 | 0 | 0 | 22.312 | 0.005 | 22.307 | 0.000 | 22312.419 | 22312.419 | 22312.419 |
| sandbox:commit | 1/1 | 0 | 0 | 22.102 | 0.003 | 22.099 | 0.000 | 22101.879 | 22101.879 | 22101.879 |
| checkpoint.total | 1/1 | 0 | 0 | 22.102 | 0.003 | 22.099 | 0.000 | 22101.729 | 22101.729 | 22101.729 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.102 | 0.003 | 22.099 | 0.000 | 22101.557 | 22101.557 | 22101.557 |
| syscall:execve | 6491/6491 | 0 | 0 | 19.740 | n/a | n/a | 0.490 | 3.041 | 2.373 | 6.759 |
| harness:snapshot | 270/270 | 0 | 0 | 12.577 | n/a | n/a | 0.003 | 46.582 | 46.891 | 66.982 |
| syscall:sendto | 4410/4410 | 0 | 0 | 12.460 | n/a | n/a | 0.399 | 2.825 | 2.305 | 5.223 |
| tool:Read | 31/31 | 0 | 0 | 8.849 | n/a | n/a | 0.001 | 285.465 | 262.887 | 360.857 |
| tool:Edit | 20/20 | 1 | 0 | 5.953 | n/a | n/a | 0.000 | 297.628 | 294.685 | 365.460 |
| harness:launch | 270/270 | 0 | 0 | 5.529 | n/a | n/a | 0.011 | 20.476 | 19.610 | 25.502 |
| syscall:bind | 1587/1587 | 0 | 0 | 5.071 | n/a | n/a | 0.135 | 3.195 | 2.618 | 5.586 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 5.007 | 1.196 | 3.811 | 28.859 | 5006.751 | 5006.751 | 5006.751 |
| runtime.harness_start | 1/1 | 0 | 0 | 5.007 | 1.195 | 3.811 | 28.858 | 5006.505 | 5006.505 | 5006.505 |
| tool:Grep | 6/6 | 2 | 0 | 4.095 | n/a | n/a | 1.944 | 682.574 | 251.414 | 2154.760 |
| tool:Glob | 3/3 | 0 | 0 | 2.734 | n/a | n/a | 0.105 | 911.203 | 1167.737 | 1324.334 |
| tool:Write | 8/8 | 0 | 0 | 2.449 | n/a | n/a | 0.000 | 306.139 | 310.840 | 326.351 |
| tool:TodoList | 7/7 | 0 | 0 | 2.032 | n/a | n/a | 0.095 | 290.298 | 285.736 | 323.196 |
| agency:decode_harness_result | 270/270 | 0 | 0 | 1.805 | 1.804 | 0.001 | 0.000 | 6.684 | 5.509 | 11.175 |
| sandbox:create | 1/1 | 0 | 0 | 0.925 | 0.317 | 0.608 | 0.000 | 924.880 | 924.880 | 924.880 |
| sandbox:start | 1/1 | 0 | 0 | 0.592 | 0.003 | 0.589 | 0.000 | 592.459 | 592.459 | 592.459 |
| runtime.container_create | 1/1 | 0 | 0 | 0.592 | 0.003 | 0.589 | 0.000 | 592.298 | 592.298 | 592.298 |
| run:detect | 1/1 | 0 | 0 | 0.539 | 0.001 | 0.538 | 0.000 | 539.417 | 539.417 | 539.417 |
| sandbox:stop | 1/1 | 0 | 0 | 0.210 | 0.002 | 0.208 | 0.000 | 210.240 | 210.240 | 210.240 |
| agency:services_close | 1/1 | 0 | 0 | 0.157 | 0.003 | 0.153 | 0.000 | 156.582 | 156.582 | 156.582 |
| agency:services_start | 1/1 | 0 | 0 | 0.093 | 0.049 | 0.044 | 0.000 | 93.442 | 93.442 | 93.442 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.008 | 0.041 | 0.000 | 49.458 | 49.458 | 49.458 |
| sync:submission | 1/1 | 0 | 0 | 0.002 | 0.000 | 0.001 | 0.000 | 1.628 | 1.628 | 1.628 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.088 | 0.094 | 0.125 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.261 | 0.261 | 0.261 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.116 | 0.116 | 0.116 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/270 | 0 | 270 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 4852 | 0.166 | 0.014 | 43.046 | 0.029 | 8.116185 CPU seconds | n/a |
| GPU 0 memory | MB | 4854 | 11913.964 | 11670.000 | 12352.000 | 11892.000 | n/a | n/a |
| GPU 0 power | W | 4854 | 28.709 | 27.338 | 73.562 | 28.137 | n/a | 140410.660 J |
| GPU 0 proc / 16894-516560 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 memory | MB | 4854 | 3239.685 | 3118.000 | 3674.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 16894-516560 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 estimated power | W | 3839 | 0.525 | 0.000 | 70.376 | 0.000 | n/a | n/a |
| GPU 0 proc / 16894-516560 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 utilization | percent | 3839 | 0.416 | 0.000 | 97.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 16934-519090 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 memory | MB | 4854 | 8192.279 | 8070.000 | 8196.000 | 8196.000 | n/a | n/a |
| GPU 0 proc / 16934-519090 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 estimated power | W | 920 | 1.011 | 0.000 | 71.432 | 0.000 | n/a | n/a |
| GPU 0 proc / 16934-519090 / sandbox / ~ / device / GPU-563de78f-4de7-14f8-07bc-30680ae2eb99 utilization | percent | 920 | 1.246 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 4854 | 11431.964 | 11188.000 | 11870.000 | 11410.000 | n/a | n/a |
| GPU 0 utilization | percent | 4854 | 0.556 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 4854 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 4853 | 3.149 | 0.108 | 70.342 | 0.126 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 4853 | 21.505 | 0.000 | 60.553 | 0.250 | n/a | n/a |
| host disk_read_mb_s | MB/s | 4853 | 0.394 | 0.000 | 207.507 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 4853 | 0.668 | 0.000 | 11.459 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 4853 | 0.359 | 0.000 | 51.282 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 4853 | 0.402 | 0.000 | 51.453 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 4854 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 4854 | 8049.939 | 6701.668 | 11933.051 | 8202.121 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 4853 | 0.009 | 0.000 | 23.413 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 4853 | 0.009 | 0.000 | 23.451 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 4853 | 0.124 | 0.000 | 2.245 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 4853 | 0.041 | 0.000 | 0.559 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 16886) CPU | percent | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 16886) io read MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 16886) io write MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 16886) rss_mb | MB | 4854 | 3.336 | 3.336 | 3.336 | 3.336 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 16886) main thread run-queue wait | percent | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 16886) vms_mb | MB | 4854 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 16894) CPU | percent | 4853 | 5.132 | 0.000 | 149.555 | 0.996 | 251.740000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 16894) io read MB/s | MB/s | 4853 | 0.002 | 0.000 | 5.520 | 0.000 | 9.859375 MB | n/a |
| Agency harness — python -m lsbench (PID 16894) io write MB/s | MB/s | 4853 | 0.364 | 0.000 | 9.999 | 0.023 | 1781.933594 MB | n/a |
| Agency harness — python -m lsbench (PID 16894) rss_mb | MB | 4854 | 3714.260 | 2548.441 | 4157.602 | 4135.832 | n/a | n/a |
| Agency harness — python -m lsbench (PID 16894) main thread run-queue wait | percent | 4853 | 0.001 | 0.000 | 2.212 | 0.000 | 0.044760 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 16894) vms_mb | MB | 4854 | 16773.401 | 14095.801 | 17228.809 | 17108.207 | n/a | n/a |
| Python — vllm (PID 16899) CPU | percent | 4853 | 0.120 | 0.000 | 8.899 | 0.000 | 5.880000 CPU seconds | n/a |
| Python — vllm (PID 16899) io read MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 16899) io write MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.008 | 0.000 | 0.027344 MB | n/a |
| Python — vllm (PID 16899) rss_mb | MB | 4854 | 1782.698 | 1781.027 | 1783.715 | 1781.027 | n/a | n/a |
| Python — vllm (PID 16899) main thread run-queue wait | percent | 4853 | 0.009 | 0.000 | 0.661 | 0.000 | 0.445033 run-queue seconds | n/a |
| Python — vllm (PID 16899) vms_mb | MB | 4854 | 11022.047 | 10951.148 | 11024.168 | 11024.168 | n/a | n/a |
| Python — python -c (PID 16933) CPU | percent | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 16933) io read MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 16933) io write MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 16933) rss_mb | MB | 4854 | 12.180 | 12.180 | 12.180 | 12.180 | n/a | n/a |
| Python — python -c (PID 16933) main thread run-queue wait | percent | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 16933) vms_mb | MB | 4854 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 16934) CPU | percent | 4853 | 1.059 | 0.000 | 65.300 | 0.996 | 51.820000 CPU seconds | n/a |
| VLLM::EngineCore (PID 16934) io read MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 16934) io write MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.004 | 0.000 | 0.031250 MB | n/a |
| VLLM::EngineCore (PID 16934) rss_mb | MB | 4854 | 2320.816 | 2318.758 | 2322.055 | 2318.758 | n/a | n/a |
| VLLM::EngineCore (PID 16934) main thread run-queue wait | percent | 4853 | 0.000 | 0.000 | 0.197 | 0.000 | 0.010411 run-queue seconds | n/a |
| VLLM::EngineCore (PID 16934) vms_mb | MB | 4854 | 21204.086 | 21204.086 | 21204.102 | 21204.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 17151) CPU | percent | 4845 | 0.002 | 0.000 | 0.995 | 0.000 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 17151) rss_mb | MB | 4846 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 17151) main thread run-queue wait | percent | 4845 | 0.009 | 0.000 | 4.964 | 0.000 | 0.427804 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — docker-init (PID 17151) vms_mb | MB | 4846 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 17173) CPU | percent | 4845 | 0.002 | 0.000 | 1.986 | 0.000 | 0.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 17173) rss_mb | MB | 4846 | 1.418 | 1.418 | 1.418 | 1.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 17173) main thread run-queue wait | percent | 4845 | 0.010 | 0.000 | 5.129 | 0.000 | 0.478950 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tail (PID 17173) vms_mb | MB | 4846 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17276) CPU | percent | 4845 | 49.836 | 0.000 | 111.507 | 0.000 | 2434.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17276) rss_mb | MB | 4846 | 146.073 | 2.902 | 178.648 | 148.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17276) main thread run-queue wait | percent | 4845 | 0.000 | 0.000 | 0.009 | 0.000 | 0.000158 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17276) vms_mb | MB | 4846 | 942.470 | 4.258 | 986.137 | 976.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 17282) CPU | percent | 2 | 59.454 | 53.394 | 65.514 | 65.514 | 1.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 17282) rss_mb | MB | 3 | 49.279 | 20.688 | 77.809 | 77.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 17282) main thread run-queue wait | percent | 2 | 0.027 | 0.017 | 0.038 | 0.038 | 0.000551 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 17282) vms_mb | MB | 3 | 59.458 | 27.012 | 93.059 | 93.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17290) rss_mb | MB | 1 | 186.148 | 186.148 | 186.148 | 186.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17290) vms_mb | MB | 1 | 1594.348 | 1594.348 | 1594.348 | 1594.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17307) CPU | percent | 142 | 6.265 | 0.989 | 96.439 | 1.989 | 8.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17307) rss_mb | MB | 143 | 386.969 | 96.340 | 407.660 | 386.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17307) main thread run-queue wait | percent | 142 | 0.358 | 0.000 | 18.759 | 0.010 | 0.512701 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17307) vms_mb | MB | 143 | 10079.049 | 1283.695 | 10214.766 | 10193.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17337) rss_mb | MB | 1 | 1.344 | 1.344 | 1.344 | 1.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17337) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17338) rss_mb | MB | 1 | 7.363 | 7.363 | 7.363 | 7.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17338) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17339) CPU | percent | 1 | 54.360 | 54.360 | 54.360 | 54.360 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17339) rss_mb | MB | 2 | 127.969 | 29.305 | 226.633 | 226.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17339) main thread run-queue wait | percent | 1 | 18.537 | 18.537 | 18.537 | 18.537 | 0.187557 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17339) vms_mb | MB | 2 | 951.131 | 271.812 | 1630.449 | 1630.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17379) rss_mb | MB | 1 | 2.684 | 2.684 | 2.684 | 2.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17379) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17381) rss_mb | MB | 1 | 17.105 | 17.105 | 17.105 | 17.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17381) vms_mb | MB | 1 | 21.000 | 21.000 | 21.000 | 21.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17458) rss_mb | MB | 1 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17458) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17460) rss_mb | MB | 1 | 229.070 | 229.070 | 229.070 | 229.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17460) vms_mb | MB | 1 | 1631.344 | 1631.344 | 1631.344 | 1631.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17488) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17488) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17489) rss_mb | MB | 1 | 21.277 | 21.277 | 21.277 | 21.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17489) vms_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — rg (PID 17511) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — rg (PID 17511) vms_mb | MB | 1 | 5.648 | 5.648 | 5.648 | 5.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17526) rss_mb | MB | 1 | 1.609 | 1.609 | 1.609 | 1.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17526) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17527) rss_mb | MB | 1 | 8.785 | 8.785 | 8.785 | 8.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17527) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17543) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17543) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17585) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17585) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17586) rss_mb | MB | 1 | 21.441 | 21.441 | 21.441 | 21.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17586) vms_mb | MB | 1 | 26.727 | 26.727 | 26.727 | 26.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17587) rss_mb | MB | 1 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17587) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17588) rss_mb | MB | 1 | 61.223 | 61.223 | 61.223 | 61.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17588) vms_mb | MB | 1 | 75.887 | 75.887 | 75.887 | 75.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17596) rss_mb | MB | 1 | 2.625 | 2.625 | 2.625 | 2.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17596) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17597) rss_mb | MB | 1 | 45.207 | 45.207 | 45.207 | 45.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17597) vms_mb | MB | 1 | 52.262 | 52.262 | 52.262 | 52.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17603) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17603) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17604) rss_mb | MB | 1 | 7.555 | 7.555 | 7.555 | 7.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17604) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17605) rss_mb | MB | 1 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17605) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17606) rss_mb | MB | 1 | 51.852 | 51.852 | 51.852 | 51.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17606) vms_mb | MB | 1 | 60.992 | 60.992 | 60.992 | 60.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17612) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17612) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17613) rss_mb | MB | 1 | 17.562 | 17.562 | 17.562 | 17.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17613) vms_mb | MB | 1 | 23.184 | 23.184 | 23.184 | 23.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17615) rss_mb | MB | 1 | 2.875 | 2.875 | 2.875 | 2.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17615) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17616) rss_mb | MB | 1 | 62.094 | 62.094 | 62.094 | 62.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 17616) vms_mb | MB | 1 | 76.984 | 76.984 | 76.984 | 76.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17622) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17622) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17623) rss_mb | MB | 1 | 6.852 | 6.852 | 6.852 | 6.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17623) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17629) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17629) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17630) rss_mb | MB | 1 | 14.461 | 14.461 | 14.461 | 14.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17630) vms_mb | MB | 1 | 19.953 | 19.953 | 19.953 | 19.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 17664) CPU | percent | 5 | 15.663 | 0.000 | 76.330 | 0.000 | 0.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 17664) rss_mb | MB | 6 | 55.972 | 10.398 | 65.137 | 65.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 17664) main thread run-queue wait | percent | 5 | 0.056 | 0.000 | 0.209 | 0.000 | 0.002821 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 17664) vms_mb | MB | 6 | 69.122 | 14.629 | 80.133 | 80.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17693) CPU | percent | 38 | 11.311 | 0.973 | 90.193 | 2.978 | 4.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17693) rss_mb | MB | 39 | 378.730 | 156.113 | 394.676 | 394.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17693) main thread run-queue wait | percent | 38 | 1.060 | 0.000 | 23.000 | 0.007 | 0.406942 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17693) vms_mb | MB | 39 | 9767.685 | 1499.465 | 10213.371 | 10212.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17717) CPU | percent | 1 | 45.515 | 45.515 | 45.515 | 45.515 | 0.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17717) rss_mb | MB | 2 | 157.191 | 90.008 | 224.375 | 224.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17717) main thread run-queue wait | percent | 1 | 29.317 | 29.317 | 29.317 | 29.317 | 0.296300 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17717) vms_mb | MB | 2 | 1455.713 | 1283.695 | 1627.730 | 1627.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17737) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17737) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17738) rss_mb | MB | 1 | 6.855 | 6.855 | 6.855 | 6.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17738) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17749) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17749) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17750) rss_mb | MB | 1 | 20.730 | 20.730 | 20.730 | 20.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17750) vms_mb | MB | 1 | 25.320 | 25.320 | 25.320 | 25.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17754) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17754) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17786) CPU | percent | 72 | 7.445 | 0.994 | 77.383 | 1.989 | 5.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17786) rss_mb | MB | 73 | 387.951 | 272.605 | 401.113 | 401.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17786) main thread run-queue wait | percent | 72 | 0.376 | 0.000 | 12.786 | 0.008 | 0.273428 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17786) vms_mb | MB | 73 | 10094.174 | 1668.223 | 10221.137 | 10221.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17809) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17809) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17810) rss_mb | MB | 1 | 10.641 | 10.641 | 10.641 | 10.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 17810) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17814) CPU | percent | 1 | 71.209 | 71.209 | 71.209 | 71.209 | 0.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17814) rss_mb | MB | 2 | 119.094 | 0.621 | 237.566 | 237.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17814) main thread run-queue wait | percent | 1 | 16.318 | 16.318 | 16.318 | 16.318 | 0.164997 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 17814) vms_mb | MB | 2 | 900.688 | 163.281 | 1638.094 | 1638.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17833) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17833) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17834) rss_mb | MB | 1 | 9.047 | 9.047 | 9.047 | 9.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17834) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17840) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17840) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17841) rss_mb | MB | 1 | 18.824 | 18.824 | 18.824 | 18.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17841) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — apply_grader.py (PID 17860) rss_mb | MB | 1 | 11.895 | 11.895 | 11.895 | 11.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — apply_grader.py (PID 17860) vms_mb | MB | 1 | 15.207 | 15.207 | 15.207 | 15.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 17884) rss_mb | MB | 1 | 7.719 | 7.719 | 7.719 | 7.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python -c (PID 17884) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17893) CPU | percent | 2 | 42.704 | 6.944 | 78.465 | 78.465 | 0.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17893) rss_mb | MB | 3 | 28.462 | 2.754 | 61.984 | 61.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17893) main thread run-queue wait | percent | 2 | 0.295 | 0.030 | 0.560 | 0.560 | 0.005938 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 17893) vms_mb | MB | 3 | 35.564 | 3.852 | 76.082 | 76.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 17896) rss_mb | MB | 1 | 30.734 | 30.734 | 30.734 | 30.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 17896) vms_mb | MB | 1 | 39.750 | 39.750 | 39.750 | 39.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17984) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17984) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17985) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17985) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17991) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 17991) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17992) rss_mb | MB | 1 | 15.285 | 15.285 | 15.285 | 15.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 17992) vms_mb | MB | 1 | 20.500 | 20.500 | 20.500 | 20.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18119) CPU | percent | 3 | 21.178 | 0.000 | 63.534 | 63.534 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18119) rss_mb | MB | 4 | 17.281 | 2.715 | 60.980 | 60.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18119) main thread run-queue wait | percent | 3 | 0.021 | 0.000 | 0.062 | 0.062 | 0.000626 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18119) vms_mb | MB | 4 | 21.824 | 3.848 | 75.754 | 75.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18121) CPU | percent | 2 | 25.798 | 0.990 | 50.606 | 0.990 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18121) rss_mb | MB | 3 | 56.125 | 36.570 | 66.152 | 66.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18121) main thread run-queue wait | percent | 2 | 0.114 | 0.068 | 0.160 | 0.068 | 0.002299 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18121) vms_mb | MB | 3 | 68.273 | 44.438 | 80.312 | 80.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18142) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18142) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18144) CPU | percent | 1 | 6.961 | 6.961 | 6.961 | 6.961 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18144) rss_mb | MB | 2 | 63.518 | 61.852 | 65.184 | 65.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18144) main thread run-queue wait | percent | 1 | 0.173 | 0.173 | 0.173 | 0.173 | 0.001741 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18144) vms_mb | MB | 2 | 78.648 | 77.195 | 80.102 | 80.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 18148) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 18148) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18149) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18149) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18150) rss_mb | MB | 1 | 8.855 | 8.855 | 8.855 | 8.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18150) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18167) CPU | percent | 29 | 12.846 | 1.988 | 92.360 | 2.981 | 3.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18167) rss_mb | MB | 30 | 368.572 | 92.547 | 386.656 | 386.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18167) main thread run-queue wait | percent | 29 | 0.652 | 0.000 | 13.026 | 0.001 | 0.190249 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18167) vms_mb | MB | 30 | 9625.270 | 1283.598 | 10209.465 | 10208.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18195) rss_mb | MB | 1 | 186.219 | 186.219 | 186.219 | 186.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18195) vms_mb | MB | 1 | 1593.723 | 1593.723 | 1593.723 | 1593.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18207) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18207) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18208) rss_mb | MB | 1 | 21.738 | 21.738 | 21.738 | 21.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18208) vms_mb | MB | 1 | 26.953 | 26.953 | 26.953 | 26.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18218) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18218) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18219) rss_mb | MB | 1 | 7.535 | 7.535 | 7.535 | 7.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18219) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18225) CPU | percent | 5 | 12.902 | 0.000 | 64.511 | 0.000 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18225) rss_mb | MB | 6 | 58.002 | 22.094 | 65.184 | 65.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18225) main thread run-queue wait | percent | 5 | 0.032 | 0.000 | 0.158 | 0.000 | 0.001589 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18225) vms_mb | MB | 6 | 71.520 | 28.574 | 80.109 | 80.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18256) CPU | percent | 34 | 10.666 | 1.987 | 76.897 | 4.972 | 3.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18256) rss_mb | MB | 35 | 377.803 | 259.152 | 387.086 | 387.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18256) main thread run-queue wait | percent | 34 | 0.646 | 0.004 | 11.880 | 0.019 | 0.221679 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18256) vms_mb | MB | 35 | 9722.479 | 1655.285 | 10207.684 | 10207.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18284) rss_mb | MB | 1 | 229.156 | 229.156 | 229.156 | 229.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18284) vms_mb | MB | 1 | 1632.016 | 1632.016 | 1632.016 | 1632.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18298) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18298) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18299) rss_mb | MB | 1 | 9.418 | 9.418 | 9.418 | 9.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18299) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18300) CPU | percent | 6 | 14.384 | 0.000 | 48.685 | 0.000 | 0.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18300) rss_mb | MB | 7 | 34.586 | 2.633 | 65.090 | 65.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18300) main thread run-queue wait | percent | 6 | 0.018 | 0.000 | 0.081 | 0.000 | 0.001104 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18300) vms_mb | MB | 7 | 42.884 | 3.852 | 80.207 | 80.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18303) CPU | percent | 2 | 16.369 | 0.000 | 32.738 | 0.000 | 0.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18303) rss_mb | MB | 3 | 58.906 | 45.164 | 65.777 | 65.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18303) main thread run-queue wait | percent | 2 | 0.109 | 0.000 | 0.218 | 0.000 | 0.002201 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18303) vms_mb | MB | 3 | 71.233 | 53.520 | 80.090 | 80.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18321) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18321) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18322) rss_mb | MB | 1 | 10.098 | 10.098 | 10.098 | 10.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18322) vms_mb | MB | 1 | 13.844 | 13.844 | 13.844 | 13.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18328) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18328) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18329) rss_mb | MB | 1 | 9.652 | 9.652 | 9.652 | 9.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18329) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18333) CPU | percent | 6 | 42.339 | 4.970 | 70.507 | 4.974 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18333) rss_mb | MB | 7 | 340.283 | 207.887 | 380.191 | 380.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18333) main thread run-queue wait | percent | 6 | 5.667 | 0.008 | 23.702 | 0.008 | 0.342873 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18333) vms_mb | MB | 7 | 7759.041 | 1619.797 | 10202.891 | 10202.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18350) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18350) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18351) rss_mb | MB | 1 | 10.195 | 10.195 | 10.195 | 10.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18351) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18354) CPU | percent | 1 | 46.602 | 46.602 | 46.602 | 46.602 | 0.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18354) rss_mb | MB | 2 | 213.912 | 174.973 | 252.852 | 252.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18354) main thread run-queue wait | percent | 1 | 16.742 | 16.742 | 16.742 | 16.742 | 0.168854 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18354) vms_mb | MB | 2 | 1619.525 | 1590.223 | 1648.828 | 1648.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18364) rss_mb | MB | 1 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18364) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18365) rss_mb | MB | 1 | 6.121 | 6.121 | 6.121 | 6.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18365) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18378) CPU | percent | 6 | 40.172 | 6.949 | 75.411 | 6.963 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18378) rss_mb | MB | 7 | 333.473 | 166.293 | 383.324 | 383.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18378) main thread run-queue wait | percent | 6 | 5.496 | 0.009 | 18.184 | 0.009 | 0.333064 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18378) vms_mb | MB | 7 | 7741.732 | 1577.719 | 10183.984 | 10183.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18395) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18395) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18396) rss_mb | MB | 1 | 8.441 | 8.441 | 8.441 | 8.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18396) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18397) CPU | percent | 2 | 56.891 | 56.307 | 57.476 | 57.476 | 1.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18397) rss_mb | MB | 3 | 177.659 | 0.000 | 303.500 | 303.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18397) main thread run-queue wait | percent | 2 | 15.804 | 11.535 | 20.073 | 20.073 | 0.319327 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18397) vms_mb | MB | 3 | 1120.237 | 0.004 | 1727.961 | 1727.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18425) CPU | percent | 8 | 34.574 | 1.985 | 75.497 | 7.958 | 2.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18425) rss_mb | MB | 9 | 347.999 | 174.695 | 385.117 | 385.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18425) main thread run-queue wait | percent | 8 | 2.829 | 0.019 | 11.377 | 0.021 | 0.228803 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18425) vms_mb | MB | 9 | 8302.436 | 1581.719 | 10211.148 | 10211.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18442) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18442) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18443) rss_mb | MB | 1 | 10.336 | 10.336 | 10.336 | 10.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18443) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18449) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18449) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18450) rss_mb | MB | 1 | 9.750 | 9.750 | 9.750 | 9.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18450) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18454) rss_mb | MB | 1 | 261.504 | 261.504 | 261.504 | 261.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18454) vms_mb | MB | 1 | 1656.289 | 1656.289 | 1656.289 | 1656.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18466) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18466) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18471) CPU | percent | 25 | 14.296 | 1.978 | 70.631 | 8.941 | 3.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18471) rss_mb | MB | 26 | 375.924 | 195.105 | 391.785 | 391.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18471) main thread run-queue wait | percent | 25 | 2.089 | 0.005 | 24.072 | 0.015 | 0.526831 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18471) vms_mb | MB | 26 | 9549.354 | 1614.719 | 10211.363 | 10210.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18488) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18488) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18489) rss_mb | MB | 1 | 8.660 | 8.660 | 8.660 | 8.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18489) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18490) CPU | percent | 2 | 55.032 | 51.552 | 58.513 | 51.552 | 1.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18490) rss_mb | MB | 3 | 177.410 | 0.000 | 302.629 | 302.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18490) main thread run-queue wait | percent | 2 | 16.492 | 8.982 | 24.002 | 24.002 | 0.332682 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18490) vms_mb | MB | 3 | 1173.298 | 160.145 | 1727.539 | 1727.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18513) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18513) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18514) rss_mb | MB | 1 | 16.582 | 16.582 | 16.582 | 16.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 18514) vms_mb | MB | 1 | 22.180 | 22.180 | 22.180 | 22.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18515) CPU | percent | 11 | 7.758 | 0.000 | 75.421 | 0.000 | 0.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18515) rss_mb | MB | 12 | 29.337 | 2.863 | 65.785 | 65.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18515) main thread run-queue wait | percent | 11 | 0.025 | 0.000 | 0.212 | 0.000 | 0.002799 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18515) vms_mb | MB | 12 | 36.243 | 3.848 | 80.191 | 80.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18518) CPU | percent | 2 | 10.437 | 0.000 | 20.875 | 0.000 | 0.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18518) rss_mb | MB | 3 | 59.607 | 48.156 | 65.332 | 65.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18518) main thread run-queue wait | percent | 2 | 0.085 | 0.000 | 0.170 | 0.000 | 0.001710 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18518) vms_mb | MB | 3 | 72.212 | 56.355 | 80.141 | 80.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18520) CPU | percent | 2 | 24.349 | 0.000 | 48.698 | 0.000 | 0.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18520) rss_mb | MB | 3 | 56.531 | 38.719 | 65.438 | 65.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18520) main thread run-queue wait | percent | 2 | 0.080 | 0.000 | 0.161 | 0.000 | 0.001618 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 18520) vms_mb | MB | 3 | 69.470 | 47.871 | 80.270 | 80.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18534) CPU | percent | 15 | 18.811 | 2.982 | 66.622 | 4.966 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18534) rss_mb | MB | 16 | 370.419 | 252.215 | 389.340 | 389.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18534) main thread run-queue wait | percent | 15 | 2.424 | 0.002 | 21.967 | 0.020 | 0.366352 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18534) vms_mb | MB | 16 | 9660.180 | 1649.031 | 10210.691 | 10210.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18553) CPU | percent | 1 | 61.518 | 61.518 | 61.518 | 61.518 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18553) rss_mb | MB | 2 | 213.553 | 166.895 | 260.211 | 260.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18553) main thread run-queue wait | percent | 1 | 14.971 | 14.971 | 14.971 | 14.971 | 0.150879 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18553) vms_mb | MB | 2 | 1616.893 | 1577.973 | 1655.812 | 1655.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18578) rss_mb | MB | 1 | 2.777 | 2.777 | 2.777 | 2.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 18578) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18579) rss_mb | MB | 1 | 21.582 | 21.582 | 21.582 | 21.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 18579) vms_mb | MB | 1 | 213.828 | 213.828 | 213.828 | 213.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18594) CPU | percent | 11 | 23.736 | 1.989 | 75.403 | 1.989 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18594) rss_mb | MB | 12 | 365.429 | 229.230 | 388.207 | 388.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18594) main thread run-queue wait | percent | 11 | 1.924 | 0.001 | 16.301 | 0.007 | 0.212964 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18594) vms_mb | MB | 12 | 8785.408 | 1632.590 | 10209.160 | 10209.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18610) rss_mb | MB | 1 | 17.543 | 17.543 | 17.543 | 17.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18610) vms_mb | MB | 1 | 706.863 | 706.863 | 706.863 | 706.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18622) CPU | percent | 1 | 92.394 | 92.394 | 92.394 | 92.394 | 0.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18622) rss_mb | MB | 2 | 174.881 | 51.523 | 298.238 | 298.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18622) main thread run-queue wait | percent | 1 | 8.416 | 8.416 | 8.416 | 8.416 | 0.084709 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18622) vms_mb | MB | 2 | 1481.348 | 1238.609 | 1724.086 | 1724.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18641) CPU | percent | 7 | 29.512 | 3.971 | 68.566 | 11.934 | 2.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18641) rss_mb | MB | 8 | 363.550 | 295.371 | 387.629 | 387.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18641) main thread run-queue wait | percent | 7 | 2.830 | 0.033 | 13.328 | 0.162 | 0.199696 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18641) vms_mb | MB | 8 | 9127.920 | 1690.938 | 10210.062 | 10210.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18665) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18665) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18666) rss_mb | MB | 1 | 8.969 | 8.969 | 8.969 | 8.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18666) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18672) rss_mb | MB | 1 | 229.137 | 229.137 | 229.137 | 229.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18672) vms_mb | MB | 1 | 1631.359 | 1631.359 | 1631.359 | 1631.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18691) CPU | percent | 8 | 33.063 | 5.960 | 70.034 | 8.954 | 2.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18691) rss_mb | MB | 9 | 351.906 | 229.148 | 386.625 | 386.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18691) main thread run-queue wait | percent | 8 | 5.375 | 0.008 | 21.588 | 0.017 | 0.433450 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18691) vms_mb | MB | 9 | 8305.328 | 1632.305 | 10209.402 | 10209.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 18704) rss_mb | MB | 1 | 2.562 | 2.562 | 2.562 | 2.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 18704) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — id (PID 18705) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — id (PID 18705) vms_mb | MB | 1 | 0.418 | 0.418 | 0.418 | 0.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18708) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18708) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18709) rss_mb | MB | 1 | 8.398 | 8.398 | 8.398 | 8.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18709) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18710) CPU | percent | 2 | 54.045 | 53.452 | 54.639 | 54.639 | 1.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18710) rss_mb | MB | 3 | 188.816 | 42.375 | 295.188 | 295.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18710) main thread run-queue wait | percent | 2 | 16.920 | 13.071 | 20.769 | 20.769 | 0.341110 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 18710) vms_mb | MB | 3 | 1385.561 | 835.023 | 1689.953 | 1689.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18720) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18720) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18721) rss_mb | MB | 1 | 10.195 | 10.195 | 10.195 | 10.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18721) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18738) CPU | percent | 17 | 16.878 | 0.993 | 66.508 | 1.986 | 2.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18738) rss_mb | MB | 18 | 373.168 | 229.234 | 392.906 | 392.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18738) main thread run-queue wait | percent | 17 | 2.248 | 0.002 | 18.605 | 0.002 | 0.385333 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18738) vms_mb | MB | 18 | 9255.686 | 1632.246 | 10208.734 | 10208.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18757) CPU | percent | 1 | 62.493 | 62.493 | 62.493 | 62.493 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18757) rss_mb | MB | 2 | 202.957 | 146.922 | 258.992 | 258.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18757) main thread run-queue wait | percent | 1 | 16.073 | 16.073 | 16.073 | 16.073 | 0.162036 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18757) vms_mb | MB | 2 | 1479.562 | 1303.234 | 1655.891 | 1655.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18769) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 18769) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18770) rss_mb | MB | 1 | 7.031 | 7.031 | 7.031 | 7.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 18770) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18815) CPU | percent | 11 | 19.140 | 0.995 | 66.543 | 0.995 | 2.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18815) rss_mb | MB | 12 | 365.727 | 288.891 | 387.484 | 387.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18815) main thread run-queue wait | percent | 11 | 1.897 | 0.002 | 15.938 | 0.003 | 0.210037 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18815) vms_mb | MB | 12 | 9481.236 | 1683.727 | 10204.719 | 10204.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18839) rss_mb | MB | 1 | 205.586 | 205.586 | 205.586 | 205.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18839) vms_mb | MB | 1 | 1618.715 | 1618.715 | 1618.715 | 1618.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18865) CPU | percent | 12 | 17.805 | 1.990 | 66.543 | 1.990 | 2.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18865) rss_mb | MB | 13 | 370.159 | 261.508 | 392.785 | 392.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18865) main thread run-queue wait | percent | 12 | 0.727 | 0.004 | 5.112 | 0.004 | 0.087863 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18865) vms_mb | MB | 13 | 8909.231 | 1657.551 | 10210.836 | 10210.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18894) rss_mb | MB | 1 | 174.516 | 174.516 | 174.516 | 174.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18894) vms_mb | MB | 1 | 1582.223 | 1582.223 | 1582.223 | 1582.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18913) CPU | percent | 7 | 34.925 | 2.985 | 73.500 | 8.951 | 2.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18913) rss_mb | MB | 8 | 342.695 | 194.352 | 383.805 | 383.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18913) main thread run-queue wait | percent | 7 | 2.772 | 0.007 | 13.437 | 0.008 | 0.195488 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18913) vms_mb | MB | 8 | 8069.781 | 1614.469 | 10207.730 | 10207.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18943) rss_mb | MB | 1 | 234.820 | 234.820 | 234.820 | 234.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18943) vms_mb | MB | 1 | 1635.090 | 1635.090 | 1635.090 | 1635.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18962) CPU | percent | 10 | 22.654 | 1.989 | 74.831 | 2.984 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18962) rss_mb | MB | 11 | 363.847 | 269.055 | 385.855 | 385.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18962) main thread run-queue wait | percent | 10 | 3.195 | 0.004 | 26.592 | 0.009 | 0.376610 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18962) vms_mb | MB | 11 | 9418.891 | 1665.512 | 10211.297 | 10211.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18985) rss_mb | MB | 1 | 193.934 | 193.934 | 193.934 | 193.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 18985) vms_mb | MB | 1 | 1614.473 | 1614.473 | 1614.473 | 1614.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19009) CPU | percent | 11 | 19.495 | 1.989 | 64.495 | 2.983 | 2.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19009) rss_mb | MB | 12 | 367.128 | 273.348 | 389.016 | 389.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19009) main thread run-queue wait | percent | 11 | 3.630 | 0.003 | 18.537 | 0.003 | 0.402314 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19009) vms_mb | MB | 12 | 9482.027 | 1668.227 | 10208.262 | 10208.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19029) CPU | percent | 1 | 54.544 | 54.544 | 54.544 | 54.544 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19029) rss_mb | MB | 2 | 212.812 | 166.613 | 259.012 | 259.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19029) main thread run-queue wait | percent | 1 | 15.394 | 15.394 | 15.394 | 15.394 | 0.155223 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19029) vms_mb | MB | 2 | 1616.535 | 1577.973 | 1655.098 | 1655.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19057) CPU | percent | 7 | 40.677 | 6.962 | 95.260 | 7.956 | 2.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19057) rss_mb | MB | 8 | 331.714 | 142.105 | 382.949 | 382.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19057) main thread run-queue wait | percent | 7 | 4.802 | 0.006 | 19.915 | 0.008 | 0.338524 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19057) vms_mb | MB | 8 | 8015.969 | 1298.402 | 10208.539 | 10208.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19078) CPU | percent | 1 | 61.533 | 61.533 | 61.533 | 61.533 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19078) rss_mb | MB | 2 | 236.053 | 193.953 | 278.152 | 278.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19078) main thread run-queue wait | percent | 1 | 16.832 | 16.832 | 16.832 | 16.832 | 0.169600 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19078) vms_mb | MB | 2 | 1644.105 | 1614.473 | 1673.738 | 1673.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19106) CPU | percent | 10 | 20.490 | 1.989 | 61.555 | 6.959 | 2.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19106) rss_mb | MB | 11 | 367.018 | 295.422 | 387.668 | 387.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19106) main thread run-queue wait | percent | 10 | 3.797 | 0.002 | 26.667 | 0.019 | 0.385909 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19106) vms_mb | MB | 11 | 9418.572 | 1690.168 | 10207.270 | 10207.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19125) CPU | percent | 1 | 64.691 | 64.691 | 64.691 | 64.691 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19125) rss_mb | MB | 2 | 244.889 | 195.031 | 294.746 | 294.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19125) main thread run-queue wait | percent | 1 | 23.328 | 23.328 | 23.328 | 23.328 | 0.238003 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19125) vms_mb | MB | 2 | 1651.900 | 1614.723 | 1689.078 | 1689.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19153) CPU | percent | 10 | 26.611 | 1.989 | 70.562 | 7.953 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19153) rss_mb | MB | 11 | 353.593 | 205.590 | 385.270 | 385.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19153) main thread run-queue wait | percent | 10 | 2.481 | 0.007 | 8.322 | 0.023 | 0.255787 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19153) vms_mb | MB | 11 | 8648.754 | 1618.750 | 10203.816 | 10203.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19260) rss_mb | MB | 1 | 159.141 | 159.141 | 159.141 | 159.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19260) vms_mb | MB | 1 | 1315.809 | 1315.809 | 1315.809 | 1315.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19272) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19272) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19273) rss_mb | MB | 1 | 7.207 | 7.207 | 7.207 | 7.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19273) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19277) CPU | percent | 13 | 19.783 | 0.994 | 75.417 | 8.953 | 2.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19277) rss_mb | MB | 14 | 364.961 | 205.738 | 388.609 | 388.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19277) main thread run-queue wait | percent | 13 | 1.004 | 0.002 | 4.900 | 0.019 | 0.131464 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19277) vms_mb | MB | 14 | 8986.377 | 1619.031 | 10207.141 | 10207.141 | n/a | n/a |
| bash kimi_seq.sh (PID 1928) CPU | percent | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash kimi_seq.sh (PID 1928) io read MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash kimi_seq.sh (PID 1928) io write MB/s | MB/s | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash kimi_seq.sh (PID 1928) rss_mb | MB | 4854 | 3.270 | 3.270 | 3.270 | 3.270 | n/a | n/a |
| bash kimi_seq.sh (PID 1928) main thread run-queue wait | percent | 4853 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash kimi_seq.sh (PID 1928) vms_mb | MB | 4854 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19306) rss_mb | MB | 1 | 229.270 | 229.270 | 229.270 | 229.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19306) vms_mb | MB | 1 | 1631.730 | 1631.730 | 1631.730 | 1631.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19325) CPU | percent | 9 | 23.944 | 0.995 | 65.505 | 0.995 | 2.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19325) rss_mb | MB | 10 | 362.045 | 253.656 | 388.578 | 388.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19325) main thread run-queue wait | percent | 9 | 3.627 | 0.004 | 15.519 | 0.004 | 0.328788 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19325) vms_mb | MB | 10 | 9332.189 | 1649.832 | 10207.945 | 10207.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19346) CPU | percent | 1 | 56.617 | 56.617 | 56.617 | 56.617 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19346) rss_mb | MB | 2 | 206.658 | 161.035 | 252.281 | 252.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19346) main thread run-queue wait | percent | 1 | 11.354 | 11.354 | 11.354 | 11.354 | 0.114310 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19346) vms_mb | MB | 2 | 1483.291 | 1317.723 | 1648.859 | 1648.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 19367) rss_mb | MB | 1 | 0.539 | 0.539 | 0.539 | 0.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 19367) vms_mb | MB | 1 | 3.609 | 3.609 | 3.609 | 3.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19374) CPU | percent | 10 | 20.157 | 1.989 | 64.529 | 3.977 | 2.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19374) rss_mb | MB | 11 | 369.779 | 289.449 | 391.855 | 391.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19374) main thread run-queue wait | percent | 10 | 3.412 | 0.004 | 19.803 | 0.034 | 0.343966 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19374) vms_mb | MB | 11 | 9419.385 | 1684.520 | 10208.879 | 10208.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19393) CPU | percent | 1 | 62.502 | 62.502 | 62.502 | 62.502 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19393) rss_mb | MB | 2 | 229.244 | 185.645 | 272.844 | 272.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19393) main thread run-queue wait | percent | 1 | 14.969 | 14.969 | 14.969 | 14.969 | 0.150883 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19393) vms_mb | MB | 2 | 1630.910 | 1593.473 | 1668.348 | 1668.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19422) CPU | percent | 11 | 22.577 | 1.989 | 68.489 | 1.989 | 2.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19422) rss_mb | MB | 12 | 358.562 | 194.934 | 388.297 | 388.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19422) main thread run-queue wait | percent | 11 | 3.606 | 0.003 | 18.700 | 0.007 | 0.399421 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19422) vms_mb | MB | 12 | 8779.534 | 1614.719 | 10207.062 | 10207.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19441) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19441) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19442) rss_mb | MB | 1 | 9.047 | 9.047 | 9.047 | 9.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19442) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19443) CPU | percent | 1 | 65.458 | 65.458 | 65.458 | 65.458 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19443) rss_mb | MB | 2 | 136.729 | 37.430 | 236.027 | 236.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19443) main thread run-queue wait | percent | 1 | 15.747 | 15.747 | 15.747 | 15.747 | 0.158779 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19443) vms_mb | MB | 2 | 1403.500 | 1170.875 | 1636.125 | 1636.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 19455) rss_mb | MB | 1 | 48.289 | 48.289 | 48.289 | 48.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 19455) vms_mb | MB | 1 | 876.301 | 876.301 | 876.301 | 876.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19471) CPU | percent | 11 | 25.494 | 2.981 | 92.300 | 4.973 | 2.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19471) rss_mb | MB | 12 | 342.311 | 39.906 | 389.332 | 389.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19471) main thread run-queue wait | percent | 11 | 3.148 | 0.005 | 24.894 | 0.017 | 0.351883 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19471) vms_mb | MB | 12 | 8733.926 | 1172.453 | 10204.109 | 10204.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19492) CPU | percent | 1 | 56.870 | 56.870 | 56.870 | 56.870 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19492) rss_mb | MB | 2 | 211.381 | 163.496 | 259.266 | 259.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19492) main thread run-queue wait | percent | 1 | 24.211 | 24.211 | 24.211 | 24.211 | 0.246916 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19492) vms_mb | MB | 2 | 1613.672 | 1572.473 | 1654.871 | 1654.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19513) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19513) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19514) rss_mb | MB | 1 | 9.762 | 9.762 | 9.762 | 9.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19514) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19518) CPU | percent | 11 | 21.298 | 1.989 | 71.471 | 7.951 | 2.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19518) rss_mb | MB | 12 | 361.720 | 229.488 | 385.602 | 385.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19518) main thread run-queue wait | percent | 11 | 1.859 | 0.003 | 10.166 | 0.027 | 0.206114 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19518) vms_mb | MB | 12 | 8785.818 | 1635.781 | 10208.121 | 10208.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19541) rss_mb | MB | 1 | 203.973 | 203.973 | 203.973 | 203.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19541) vms_mb | MB | 1 | 1618.953 | 1618.953 | 1618.953 | 1618.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19568) CPU | percent | 11 | 21.367 | 1.990 | 76.557 | 3.978 | 2.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19568) rss_mb | MB | 12 | 365.957 | 253.270 | 389.590 | 389.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19568) main thread run-queue wait | percent | 11 | 2.214 | 0.002 | 19.209 | 0.013 | 0.246719 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19568) vms_mb | MB | 12 | 9467.655 | 1649.785 | 10204.871 | 10204.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19596) rss_mb | MB | 1 | 166.254 | 166.254 | 166.254 | 166.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19596) vms_mb | MB | 1 | 1577.723 | 1577.723 | 1577.723 | 1577.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19613) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19613) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19614) rss_mb | MB | 1 | 8.707 | 8.707 | 8.707 | 8.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19614) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19618) CPU | percent | 13 | 19.968 | 0.995 | 73.456 | 13.925 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19618) rss_mb | MB | 14 | 364.687 | 229.375 | 385.270 | 385.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19618) main thread run-queue wait | percent | 13 | 1.816 | 0.003 | 15.059 | 1.216 | 0.242566 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19618) vms_mb | MB | 14 | 8987.908 | 1632.785 | 10206.797 | 10206.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19645) rss_mb | MB | 1 | 140.223 | 140.223 | 140.223 | 140.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19645) vms_mb | MB | 1 | 1296.918 | 1296.918 | 1296.918 | 1296.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19667) CPU | percent | 20 | 15.239 | 0.994 | 73.564 | 1.989 | 3.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19667) rss_mb | MB | 21 | 372.216 | 217.574 | 388.824 | 388.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19667) main thread run-queue wait | percent | 20 | 2.139 | 0.002 | 23.131 | 0.009 | 0.431427 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19667) vms_mb | MB | 21 | 9392.748 | 1623.832 | 10209.867 | 10209.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 19682) rss_mb | MB | 1 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 19682) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 19683) rss_mb | MB | 1 | 1.605 | 1.605 | 1.605 | 1.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 19683) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19686) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19686) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19687) rss_mb | MB | 1 | 8.828 | 8.828 | 8.828 | 8.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19687) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19688) CPU | percent | 2 | 57.528 | 54.591 | 60.465 | 60.465 | 1.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19688) rss_mb | MB | 3 | 187.152 | 31.301 | 301.520 | 301.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19688) main thread run-queue wait | percent | 2 | 17.359 | 15.476 | 19.241 | 19.241 | 0.350034 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19688) vms_mb | MB | 3 | 1338.318 | 655.812 | 1726.410 | 1726.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19700) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19700) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19701) rss_mb | MB | 1 | 7.574 | 7.574 | 7.574 | 7.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19701) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19711) rss_mb | MB | 1 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 19711) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19712) rss_mb | MB | 1 | 13.121 | 13.121 | 13.121 | 13.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 19712) vms_mb | MB | 1 | 207.254 | 207.254 | 207.254 | 207.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19729) CPU | percent | 7 | 40.707 | 3.977 | 95.414 | 6.963 | 2.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19729) rss_mb | MB | 8 | 322.928 | 73.730 | 387.676 | 387.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19729) main thread run-queue wait | percent | 7 | 7.308 | 0.003 | 30.780 | 0.008 | 0.515518 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19729) vms_mb | MB | 8 | 8012.529 | 1283.598 | 10208.727 | 10208.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19750) CPU | percent | 1 | 63.470 | 63.470 | 63.470 | 63.470 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19750) rss_mb | MB | 2 | 241.760 | 194.488 | 289.031 | 289.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19750) main thread run-queue wait | percent | 1 | 21.307 | 21.307 | 21.307 | 21.307 | 0.214851 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19750) vms_mb | MB | 2 | 1649.398 | 1614.723 | 1684.074 | 1684.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19760) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19760) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19761) rss_mb | MB | 1 | 7.227 | 7.227 | 7.227 | 7.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19761) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19778) CPU | percent | 11 | 25.551 | 1.988 | 79.435 | 4.970 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19778) rss_mb | MB | 12 | 358.008 | 189.293 | 390.934 | 390.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19778) main thread run-queue wait | percent | 11 | 3.017 | 0.001 | 21.207 | 0.015 | 0.334926 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19778) vms_mb | MB | 12 | 8778.268 | 1594.469 | 10209.656 | 10209.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19801) CPU | percent | 1 | 59.568 | 59.568 | 59.568 | 59.568 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19801) rss_mb | MB | 2 | 212.082 | 164.332 | 259.832 | 259.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19801) main thread run-queue wait | percent | 1 | 17.019 | 17.019 | 17.019 | 17.019 | 0.171425 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19801) vms_mb | MB | 2 | 1613.660 | 1572.473 | 1654.848 | 1654.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19825) CPU | percent | 11 | 22.111 | 0.995 | 74.579 | 1.989 | 2.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19825) rss_mb | MB | 12 | 361.474 | 236.383 | 383.828 | 383.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19825) main thread run-queue wait | percent | 11 | 1.967 | 0.002 | 12.858 | 0.007 | 0.221306 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19825) vms_mb | MB | 12 | 8784.700 | 1636.531 | 10207.957 | 10207.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19848) CPU | percent | 1 | 66.849 | 66.849 | 66.849 | 66.849 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19848) rss_mb | MB | 2 | 253.998 | 205.617 | 302.379 | 302.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19848) main thread run-queue wait | percent | 1 | 15.544 | 15.544 | 15.544 | 15.544 | 0.160445 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19848) vms_mb | MB | 2 | 1672.885 | 1619.203 | 1726.566 | 1726.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19858) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19858) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19859) rss_mb | MB | 1 | 8.828 | 8.828 | 8.828 | 8.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19859) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19874) CPU | percent | 10 | 27.405 | 2.978 | 86.292 | 2.983 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19874) rss_mb | MB | 11 | 352.105 | 162.980 | 390.609 | 390.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19874) main thread run-queue wait | percent | 10 | 1.801 | 0.005 | 8.030 | 0.005 | 0.181496 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19874) vms_mb | MB | 11 | 8648.748 | 1572.469 | 10208.258 | 10208.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19899) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19899) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19900) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19900) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19904) rss_mb | MB | 1 | 221.703 | 221.703 | 221.703 | 221.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19904) vms_mb | MB | 1 | 1624.723 | 1624.723 | 1624.723 | 1624.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19923) CPU | percent | 11 | 26.450 | 1.989 | 93.397 | 5.967 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19923) rss_mb | MB | 12 | 340.136 | 23.617 | 388.555 | 388.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19923) main thread run-queue wait | percent | 11 | 2.456 | 0.009 | 13.748 | 0.013 | 0.272224 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19923) vms_mb | MB | 12 | 8653.758 | 165.848 | 10207.969 | 10207.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19947) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 19947) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19948) rss_mb | MB | 1 | 9.605 | 9.605 | 9.605 | 9.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 19948) vms_mb | MB | 1 | 13.578 | 13.578 | 13.578 | 13.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19954) rss_mb | MB | 1 | 172.254 | 172.254 | 172.254 | 172.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19954) vms_mb | MB | 1 | 1579.723 | 1579.723 | 1579.723 | 1579.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19973) CPU | percent | 11 | 19.154 | 1.990 | 71.563 | 1.990 | 2.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19973) rss_mb | MB | 12 | 364.553 | 228.449 | 390.164 | 390.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19973) main thread run-queue wait | percent | 11 | 0.635 | 0.007 | 3.475 | 0.008 | 0.070279 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 19973) vms_mb | MB | 12 | 8776.610 | 1631.559 | 10197.688 | 10197.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20004) rss_mb | MB | 1 | 290.172 | 290.172 | 290.172 | 290.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20004) vms_mb | MB | 1 | 1685.809 | 1685.809 | 1685.809 | 1685.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20024) CPU | percent | 11 | 19.910 | 0.994 | 69.256 | 2.984 | 2.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20024) rss_mb | MB | 12 | 362.521 | 255.320 | 384.699 | 384.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20024) main thread run-queue wait | percent | 11 | 0.867 | 0.005 | 5.734 | 0.019 | 0.095970 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20024) vms_mb | MB | 12 | 8798.002 | 1651.277 | 10209.250 | 10208.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20053) rss_mb | MB | 1 | 242.465 | 242.465 | 242.465 | 242.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20053) vms_mb | MB | 1 | 1640.105 | 1640.105 | 1640.105 | 1640.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20091) CPU | percent | 23 | 12.397 | 0.994 | 88.375 | 1.990 | 2.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20091) rss_mb | MB | 24 | 371.069 | 91.738 | 394.883 | 394.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20091) main thread run-queue wait | percent | 23 | 0.702 | 0.002 | 5.210 | 0.005 | 0.165377 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20091) vms_mb | MB | 24 | 9480.487 | 1283.598 | 10211.367 | 10211.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20117) rss_mb | MB | 1 | 1.418 | 1.418 | 1.418 | 1.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20117) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20118) rss_mb | MB | 1 | 7.719 | 7.719 | 7.719 | 7.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20118) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20122) rss_mb | MB | 1 | 293.875 | 293.875 | 293.875 | 293.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20122) vms_mb | MB | 1 | 1688.418 | 1688.418 | 1688.418 | 1688.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20143) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20143) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 20144) rss_mb | MB | 1 | 21.590 | 21.590 | 21.590 | 21.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 20144) vms_mb | MB | 1 | 26.980 | 26.980 | 26.980 | 26.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20159) CPU | percent | 13 | 19.186 | 1.989 | 81.374 | 7.958 | 2.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20159) rss_mb | MB | 14 | 357.959 | 166.855 | 388.227 | 388.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20159) main thread run-queue wait | percent | 13 | 2.492 | 0.003 | 17.602 | 0.012 | 0.325916 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20159) vms_mb | MB | 14 | 8972.707 | 1577.719 | 10199.410 | 10199.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20180) rss_mb | MB | 1 | 212.082 | 212.082 | 212.082 | 212.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20180) vms_mb | MB | 1 | 1621.711 | 1621.711 | 1621.711 | 1621.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20208) CPU | percent | 11 | 21.112 | 2.981 | 73.441 | 8.951 | 2.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20208) rss_mb | MB | 12 | 360.277 | 229.059 | 385.125 | 385.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20208) main thread run-queue wait | percent | 11 | 2.917 | 0.005 | 16.230 | 0.019 | 0.323218 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20208) vms_mb | MB | 12 | 8779.740 | 1632.281 | 10207.527 | 10207.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20227) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20227) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20228) rss_mb | MB | 1 | 8.957 | 8.957 | 8.957 | 8.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20228) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20229) CPU | percent | 1 | 62.493 | 62.493 | 62.493 | 62.493 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20229) rss_mb | MB | 2 | 135.965 | 37.457 | 234.473 | 234.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20229) main thread run-queue wait | percent | 1 | 19.879 | 19.879 | 19.879 | 19.879 | 0.200406 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20229) vms_mb | MB | 2 | 1403.359 | 1170.875 | 1635.844 | 1635.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20257) CPU | percent | 12 | 19.710 | 0.995 | 76.507 | 1.989 | 2.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20257) rss_mb | MB | 13 | 367.333 | 236.074 | 390.090 | 390.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20257) main thread run-queue wait | percent | 12 | 1.916 | 0.001 | 10.961 | 0.002 | 0.235255 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20257) vms_mb | MB | 13 | 8899.912 | 1636.805 | 10208.211 | 10208.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20278) rss_mb | MB | 1 | 228.875 | 228.875 | 228.875 | 228.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20278) vms_mb | MB | 1 | 1632.426 | 1632.426 | 1632.426 | 1632.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20304) CPU | percent | 11 | 21.950 | 1.964 | 77.527 | 5.955 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20304) rss_mb | MB | 12 | 360.594 | 174.477 | 393.836 | 393.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20304) main thread run-queue wait | percent | 11 | 1.040 | 0.003 | 5.715 | 0.017 | 0.115357 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20304) vms_mb | MB | 12 | 8777.225 | 1581.969 | 10204.879 | 10204.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20321) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20321) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20322) rss_mb | MB | 1 | 7.020 | 7.020 | 7.020 | 7.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20322) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20334) rss_mb | MB | 1 | 197.727 | 197.727 | 197.727 | 197.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20334) vms_mb | MB | 1 | 1617.250 | 1617.250 | 1617.250 | 1617.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20348) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20348) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20353) CPU | percent | 7 | 43.088 | 3.977 | 89.114 | 5.964 | 3.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20353) rss_mb | MB | 8 | 340.299 | 181.715 | 390.262 | 390.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20353) main thread run-queue wait | percent | 7 | 7.598 | 0.007 | 21.381 | 0.007 | 0.536065 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20353) vms_mb | MB | 8 | 8056.806 | 1591.719 | 10207.582 | 10207.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20372) CPU | percent | 1 | 66.460 | 66.460 | 66.460 | 66.460 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20372) rss_mb | MB | 2 | 232.455 | 187.645 | 277.266 | 277.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20372) main thread run-queue wait | percent | 1 | 15.083 | 15.083 | 15.083 | 15.083 | 0.152058 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20372) vms_mb | MB | 2 | 1633.650 | 1593.973 | 1673.328 | 1673.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20400) CPU | percent | 12 | 23.823 | 1.986 | 78.480 | 3.975 | 2.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20400) rss_mb | MB | 13 | 366.332 | 235.355 | 392.484 | 392.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20400) main thread run-queue wait | percent | 12 | 3.104 | 0.004 | 23.782 | 0.018 | 0.375734 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20400) vms_mb | MB | 13 | 8888.615 | 1636.789 | 10205.168 | 10205.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20419) CPU | percent | 1 | 60.428 | 60.428 | 60.428 | 60.428 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20419) rss_mb | MB | 2 | 257.400 | 220.719 | 294.082 | 294.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20419) main thread run-queue wait | percent | 1 | 28.065 | 28.065 | 28.065 | 28.065 | 0.283310 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20419) vms_mb | MB | 2 | 1656.523 | 1624.230 | 1688.816 | 1688.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20524) CPU | percent | 50 | 7.588 | 0.990 | 87.221 | 3.979 | 3.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20524) rss_mb | MB | 51 | 385.619 | 188.980 | 397.492 | 397.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20524) main thread run-queue wait | percent | 50 | 0.778 | 0.001 | 15.693 | 0.042 | 0.391573 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20524) vms_mb | MB | 51 | 9870.027 | 1594.469 | 10209.184 | 10208.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20544) CPU | percent | 1 | 58.566 | 58.566 | 58.566 | 58.566 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20544) rss_mb | MB | 2 | 250.168 | 205.629 | 294.707 | 294.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20544) main thread run-queue wait | percent | 1 | 18.321 | 18.321 | 18.321 | 18.321 | 0.184569 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20544) vms_mb | MB | 2 | 1654.277 | 1618.734 | 1689.820 | 1689.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 20572) CPU | percent | 8 | 9.550 | 0.000 | 60.533 | 0.000 | 0.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 20572) rss_mb | MB | 9 | 19.756 | 2.719 | 64.938 | 64.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 20572) main thread run-queue wait | percent | 8 | 0.031 | 0.000 | 0.213 | 0.000 | 0.002463 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 20572) vms_mb | MB | 9 | 24.925 | 3.848 | 80.078 | 80.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 20578) CPU | percent | 2 | 31.243 | 0.000 | 62.485 | 0.000 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 20578) rss_mb | MB | 3 | 51.626 | 24.613 | 65.133 | 65.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 20578) main thread run-queue wait | percent | 2 | 0.030 | 0.000 | 0.060 | 0.000 | 0.000606 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 20578) vms_mb | MB | 3 | 63.570 | 30.445 | 80.133 | 80.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 20580) CPU | percent | 2 | 22.309 | 0.000 | 44.617 | 0.000 | 0.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 20580) rss_mb | MB | 3 | 56.516 | 39.016 | 65.266 | 65.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 20580) main thread run-queue wait | percent | 2 | 0.109 | 0.000 | 0.218 | 0.000 | 0.002198 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 20580) vms_mb | MB | 3 | 69.385 | 47.836 | 80.160 | 80.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20604) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20604) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20605) rss_mb | MB | 1 | 7.953 | 7.953 | 7.953 | 7.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20605) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20609) CPU | percent | 6 | 38.786 | 3.974 | 73.489 | 8.951 | 2.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20609) rss_mb | MB | 7 | 342.682 | 207.590 | 390.066 | 390.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20609) main thread run-queue wait | percent | 6 | 2.823 | 0.010 | 6.849 | 0.011 | 0.171885 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20609) vms_mb | MB | 7 | 7764.675 | 1619.547 | 10205.285 | 10205.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20639) rss_mb | MB | 1 | 172.117 | 172.117 | 172.117 | 172.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20639) vms_mb | MB | 1 | 1579.723 | 1579.723 | 1579.723 | 1579.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20652) CPU | percent | 8 | 23.704 | 1.990 | 62.542 | 1.990 | 1.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20652) rss_mb | MB | 9 | 365.056 | 295.566 | 390.773 | 390.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20652) main thread run-queue wait | percent | 8 | 3.538 | 0.005 | 18.087 | 0.006 | 0.285057 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20652) vms_mb | MB | 9 | 9246.522 | 1690.031 | 10208.918 | 10208.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20671) CPU | percent | 1 | 60.551 | 60.551 | 60.551 | 60.551 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20671) rss_mb | MB | 2 | 240.049 | 193.848 | 286.250 | 286.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20671) main thread run-queue wait | percent | 1 | 15.638 | 15.638 | 15.638 | 15.638 | 0.157544 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20671) vms_mb | MB | 2 | 1647.766 | 1614.223 | 1681.309 | 1681.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20699) CPU | percent | 7 | 38.024 | 2.983 | 84.356 | 16.822 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20699) rss_mb | MB | 8 | 340.786 | 164.824 | 392.590 | 392.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20699) main thread run-queue wait | percent | 7 | 2.895 | 0.006 | 14.650 | 0.054 | 0.204057 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20699) vms_mb | MB | 8 | 8062.862 | 1572.719 | 10209.184 | 10209.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20726) rss_mb | MB | 1 | 229.348 | 229.348 | 229.348 | 229.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20726) vms_mb | MB | 1 | 1631.734 | 1631.734 | 1631.734 | 1631.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20743) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20743) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20744) rss_mb | MB | 1 | 6.910 | 6.910 | 6.910 | 6.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20744) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20748) CPU | percent | 12 | 25.233 | 0.995 | 83.321 | 1.989 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20748) rss_mb | MB | 13 | 366.496 | 194.879 | 395.559 | 395.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20748) main thread run-queue wait | percent | 12 | 1.655 | 0.001 | 7.686 | 0.004 | 0.200149 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20748) vms_mb | MB | 13 | 8896.095 | 1614.969 | 10215.121 | 10215.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20776) rss_mb | MB | 1 | 160.809 | 160.809 | 160.809 | 160.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20776) vms_mb | MB | 1 | 1500.469 | 1500.469 | 1500.469 | 1500.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20795) CPU | percent | 12 | 26.954 | 0.994 | 96.167 | 0.994 | 3.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20795) rss_mb | MB | 13 | 345.227 | 37.113 | 388.977 | 388.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20795) main thread run-queue wait | percent | 12 | 2.974 | 0.003 | 14.907 | 0.006 | 0.362519 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20795) vms_mb | MB | 13 | 8844.322 | 1170.816 | 10209.383 | 10209.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20815) CPU | percent | 1 | 65.101 | 65.101 | 65.101 | 65.101 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20815) rss_mb | MB | 2 | 212.822 | 166.062 | 259.582 | 259.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20815) main thread run-queue wait | percent | 1 | 18.380 | 18.380 | 18.380 | 18.380 | 0.186343 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20815) vms_mb | MB | 2 | 1616.777 | 1577.973 | 1655.582 | 1655.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 20825) rss_mb | MB | 1 | 1.414 | 1.414 | 1.414 | 1.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 20825) vms_mb | MB | 1 | 6.684 | 6.684 | 6.684 | 6.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20844) CPU | percent | 11 | 20.955 | 0.993 | 68.518 | 0.993 | 2.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20844) rss_mb | MB | 12 | 368.443 | 261.023 | 392.203 | 392.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20844) main thread run-queue wait | percent | 11 | 3.845 | 0.004 | 21.181 | 0.007 | 0.433332 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20844) vms_mb | MB | 12 | 9476.185 | 1656.242 | 10205.004 | 10205.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20864) CPU | percent | 1 | 64.443 | 64.443 | 64.443 | 64.443 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20864) rss_mb | MB | 2 | 210.789 | 160.645 | 260.934 | 260.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20864) main thread run-queue wait | percent | 1 | 18.705 | 18.705 | 18.705 | 18.705 | 0.188667 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20864) vms_mb | MB | 2 | 1578.258 | 1500.219 | 1656.297 | 1656.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20877) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 20877) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20878) rss_mb | MB | 1 | 7.895 | 7.895 | 7.895 | 7.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 20878) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20893) CPU | percent | 13 | 28.343 | 0.985 | 80.512 | 52.509 | 3.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20893) rss_mb | MB | 14 | 355.514 | 168.336 | 386.320 | 352.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20893) main thread run-queue wait | percent | 13 | 4.971 | 0.002 | 30.395 | 16.692 | 0.651117 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20893) vms_mb | MB | 14 | 8984.515 | 1578.469 | 10213.219 | 10177.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20914) CPU | percent | 1 | 49.648 | 49.648 | 49.648 | 49.648 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20914) rss_mb | MB | 2 | 211.211 | 168.488 | 253.934 | 253.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20914) main thread run-queue wait | percent | 1 | 19.987 | 19.987 | 19.987 | 19.987 | 0.201287 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20914) vms_mb | MB | 2 | 1614.162 | 1578.723 | 1649.602 | 1649.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20940) CPU | percent | 11 | 26.458 | 1.989 | 93.383 | 1.989 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20940) rss_mb | MB | 12 | 334.869 | 0.000 | 381.738 | 381.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20940) main thread run-queue wait | percent | 11 | 1.369 | 0.001 | 8.509 | 0.007 | 0.151614 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20940) vms_mb | MB | 12 | 8648.261 | 160.145 | 10202.074 | 10202.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20971) rss_mb | MB | 1 | 187.641 | 187.641 | 187.641 | 187.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20971) vms_mb | MB | 1 | 1593.973 | 1593.973 | 1593.973 | 1593.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20988) CPU | percent | 12 | 24.738 | 1.987 | 92.367 | 4.973 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20988) rss_mb | MB | 13 | 355.192 | 141.875 | 388.879 | 388.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20988) main thread run-queue wait | percent | 12 | 1.624 | 0.001 | 7.230 | 0.017 | 0.196382 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 20988) vms_mb | MB | 13 | 8861.732 | 1298.402 | 10209.531 | 10209.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21009) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21009) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21010) rss_mb | MB | 1 | 10.367 | 10.367 | 10.367 | 10.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21010) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21016) rss_mb | MB | 1 | 193.633 | 193.633 | 193.633 | 193.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21016) vms_mb | MB | 1 | 1614.723 | 1614.723 | 1614.723 | 1614.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21030) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21030) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21031) rss_mb | MB | 1 | 8.758 | 8.758 | 8.758 | 8.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21031) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21035) CPU | percent | 12 | 22.501 | 1.988 | 74.472 | 3.976 | 2.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21035) rss_mb | MB | 13 | 364.069 | 205.281 | 391.902 | 391.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21035) main thread run-queue wait | percent | 12 | 3.381 | 0.004 | 23.041 | 0.009 | 0.409038 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21035) vms_mb | MB | 13 | 8892.105 | 1618.762 | 10209.020 | 10209.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21055) CPU | percent | 1 | 57.437 | 57.437 | 57.437 | 57.437 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21055) rss_mb | MB | 2 | 265.750 | 229.191 | 302.309 | 302.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21055) main thread run-queue wait | percent | 1 | 17.680 | 17.680 | 17.680 | 17.680 | 0.178534 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21055) vms_mb | MB | 2 | 1679.340 | 1631.961 | 1726.719 | 1726.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21083) CPU | percent | 11 | 23.932 | 0.995 | 72.436 | 2.984 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21083) rss_mb | MB | 12 | 366.093 | 206.395 | 396.566 | 396.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21083) main thread run-queue wait | percent | 11 | 1.834 | 0.001 | 12.156 | 0.006 | 0.215458 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21083) vms_mb | MB | 12 | 8784.641 | 1619.582 | 10212.363 | 10212.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21107) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21107) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21108) rss_mb | MB | 1 | 9.457 | 9.457 | 9.457 | 9.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21108) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21112) rss_mb | MB | 1 | 255.879 | 255.879 | 255.879 | 255.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21112) vms_mb | MB | 1 | 1651.863 | 1651.863 | 1651.863 | 1651.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21131) CPU | percent | 13 | 21.174 | 0.995 | 87.401 | 2.984 | 2.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21131) rss_mb | MB | 14 | 355.748 | 151.734 | 385.676 | 385.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21131) main thread run-queue wait | percent | 13 | 1.510 | 0.004 | 11.506 | 0.011 | 0.197474 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21131) vms_mb | MB | 14 | 8961.490 | 1308.969 | 10207.695 | 10207.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21162) rss_mb | MB | 1 | 149.586 | 149.586 | 149.586 | 149.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21162) vms_mb | MB | 1 | 1308.988 | 1308.988 | 1308.988 | 1308.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21181) CPU | percent | 11 | 23.299 | 1.989 | 90.467 | 2.982 | 2.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21181) rss_mb | MB | 12 | 339.549 | 0.000 | 388.781 | 388.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21181) main thread run-queue wait | percent | 11 | 0.735 | 0.002 | 3.371 | 0.004 | 0.081546 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21181) vms_mb | MB | 12 | 8632.434 | 0.004 | 10199.516 | 10199.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21212) rss_mb | MB | 1 | 228.887 | 228.887 | 228.887 | 228.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21212) vms_mb | MB | 1 | 1635.832 | 1635.832 | 1635.832 | 1635.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21251) CPU | percent | 13 | 17.035 | 1.988 | 69.480 | 1.989 | 2.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21251) rss_mb | MB | 14 | 375.208 | 280.445 | 393.320 | 393.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21251) main thread run-queue wait | percent | 13 | 2.929 | 0.003 | 18.372 | 0.005 | 0.383314 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21251) vms_mb | MB | 14 | 9582.990 | 1675.488 | 10206.121 | 10206.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21271) CPU | percent | 1 | 55.627 | 55.627 | 55.627 | 55.627 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21271) rss_mb | MB | 2 | 212.729 | 166.820 | 258.637 | 258.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21271) main thread run-queue wait | percent | 1 | 16.849 | 16.849 | 16.849 | 16.849 | 0.169616 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21271) vms_mb | MB | 2 | 1616.793 | 1578.223 | 1655.363 | 1655.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21299) CPU | percent | 6 | 43.042 | 2.983 | 89.471 | 2.983 | 2.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21299) rss_mb | MB | 7 | 328.797 | 154.516 | 379.016 | 379.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21299) main thread run-queue wait | percent | 6 | 5.373 | 0.009 | 20.610 | 0.009 | 0.325039 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21299) vms_mb | MB | 7 | 7716.244 | 1310.613 | 10205.750 | 10205.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21318) CPU | percent | 1 | 52.514 | 52.514 | 52.514 | 52.514 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21318) rss_mb | MB | 2 | 236.816 | 201.043 | 272.590 | 272.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21318) main thread run-queue wait | percent | 1 | 21.227 | 21.227 | 21.227 | 21.227 | 0.214235 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21318) vms_mb | MB | 2 | 1643.012 | 1618.266 | 1667.758 | 1667.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21330) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21330) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21331) rss_mb | MB | 1 | 9.871 | 9.871 | 9.871 | 9.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21331) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21346) CPU | percent | 15 | 14.766 | 0.994 | 72.508 | 0.995 | 2.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21346) rss_mb | MB | 16 | 375.128 | 262.699 | 392.527 | 392.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21346) main thread run-queue wait | percent | 15 | 1.439 | 0.001 | 12.887 | 0.001 | 0.217356 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21346) vms_mb | MB | 16 | 9664.121 | 1658.336 | 10209.500 | 10209.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21367) rss_mb | MB | 1 | 207.996 | 207.996 | 207.996 | 207.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21367) vms_mb | MB | 1 | 1620.477 | 1620.477 | 1620.477 | 1620.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21393) CPU | percent | 7 | 41.580 | 4.974 | 91.331 | 4.974 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21393) rss_mb | MB | 8 | 313.170 | 0.000 | 385.027 | 385.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21393) main thread run-queue wait | percent | 7 | 3.596 | 0.004 | 12.273 | 0.004 | 0.253418 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21393) vms_mb | MB | 8 | 7867.745 | 160.145 | 10205.027 | 10205.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21417) rss_mb | MB | 1 | 207.684 | 207.684 | 207.684 | 207.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21417) vms_mb | MB | 1 | 1619.258 | 1619.258 | 1619.258 | 1619.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21443) CPU | percent | 11 | 23.831 | 1.989 | 78.552 | 1.989 | 2.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21443) rss_mb | MB | 12 | 360.381 | 217.504 | 386.602 | 386.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21443) main thread run-queue wait | percent | 11 | 3.805 | 0.002 | 23.444 | 0.006 | 0.421848 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21443) vms_mb | MB | 12 | 8781.367 | 1623.262 | 10209.695 | 10209.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21460) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21460) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21461) rss_mb | MB | 1 | 7.492 | 7.492 | 7.492 | 7.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21461) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21462) CPU | percent | 1 | 48.636 | 48.636 | 48.636 | 48.636 | 0.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21462) rss_mb | MB | 2 | 263.490 | 229.711 | 297.270 | 297.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21462) main thread run-queue wait | percent | 1 | 21.097 | 21.097 | 21.097 | 21.097 | 0.212546 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21462) vms_mb | MB | 2 | 1678.123 | 1631.992 | 1724.254 | 1724.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21490) CPU | percent | 12 | 24.747 | 1.986 | 93.396 | 1.988 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21490) rss_mb | MB | 13 | 347.552 | 40.602 | 389.395 | 389.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21490) main thread run-queue wait | percent | 12 | 2.611 | 0.004 | 25.116 | 0.004 | 0.316021 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21490) vms_mb | MB | 13 | 8850.969 | 1172.289 | 10209.027 | 10209.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21512) CPU | percent | 1 | 47.569 | 47.569 | 47.569 | 47.569 | 0.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21512) rss_mb | MB | 2 | 194.373 | 159.625 | 229.121 | 229.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21512) main thread run-queue wait | percent | 1 | 23.479 | 23.479 | 23.479 | 23.479 | 0.236922 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21512) vms_mb | MB | 2 | 1473.838 | 1315.719 | 1631.957 | 1631.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21538) CPU | percent | 12 | 24.089 | 1.989 | 80.359 | 1.989 | 2.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21538) rss_mb | MB | 13 | 358.553 | 166.562 | 394.797 | 394.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21538) main thread run-queue wait | percent | 12 | 2.941 | 0.002 | 24.377 | 0.005 | 0.355398 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21538) vms_mb | MB | 13 | 8888.467 | 1577.969 | 10209.344 | 10209.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21561) CPU | percent | 1 | 55.628 | 55.628 | 55.628 | 55.628 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21561) rss_mb | MB | 2 | 211.262 | 168.426 | 254.098 | 254.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21561) main thread run-queue wait | percent | 1 | 19.321 | 19.321 | 19.321 | 19.321 | 0.194499 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21561) vms_mb | MB | 2 | 1614.309 | 1578.473 | 1650.145 | 1650.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21590) CPU | percent | 28 | 12.249 | 0.993 | 74.571 | 7.955 | 3.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21590) rss_mb | MB | 29 | 379.610 | 188.594 | 395.016 | 395.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21590) main thread run-queue wait | percent | 28 | 0.918 | 0.001 | 11.691 | 0.026 | 0.262796 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21590) vms_mb | MB | 29 | 9621.618 | 1593.969 | 10214.957 | 10214.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21614) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21614) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21615) rss_mb | MB | 1 | 8.996 | 8.996 | 8.996 | 8.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21615) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21621) rss_mb | MB | 1 | 212.488 | 212.488 | 212.488 | 212.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21621) vms_mb | MB | 1 | 1622.461 | 1622.461 | 1622.461 | 1622.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21721) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21721) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21722) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21722) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21733) CPU | percent | 11 | 21.770 | 1.978 | 76.561 | 1.978 | 2.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21733) rss_mb | MB | 12 | 367.301 | 238.016 | 392.125 | 392.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21733) main thread run-queue wait | percent | 11 | 1.199 | 0.005 | 9.586 | 0.005 | 0.132736 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21733) vms_mb | MB | 12 | 8794.071 | 1638.246 | 10210.172 | 10210.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21761) rss_mb | MB | 1 | 279.363 | 279.363 | 279.363 | 279.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21761) vms_mb | MB | 1 | 1674.059 | 1674.059 | 1674.059 | 1674.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21780) CPU | percent | 31 | 10.992 | 0.993 | 83.501 | 2.983 | 3.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21780) rss_mb | MB | 32 | 380.555 | 170.336 | 395.523 | 394.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21780) main thread run-queue wait | percent | 31 | 0.482 | 0.001 | 6.956 | 0.010 | 0.150583 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21780) vms_mb | MB | 32 | 9674.646 | 1579.469 | 10213.426 | 10212.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21810) rss_mb | MB | 1 | 221.445 | 221.445 | 221.445 | 221.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21810) vms_mb | MB | 1 | 1624.234 | 1624.234 | 1624.234 | 1624.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21831) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21831) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21832) rss_mb | MB | 1 | 19.957 | 19.957 | 19.957 | 19.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 21832) vms_mb | MB | 1 | 25.062 | 25.062 | 25.062 | 25.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21847) CPU | percent | 7 | 31.490 | 4.973 | 76.417 | 10.941 | 2.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21847) rss_mb | MB | 8 | 361.344 | 272.625 | 391.938 | 391.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21847) main thread run-queue wait | percent | 7 | 1.973 | 0.010 | 10.373 | 0.027 | 0.139038 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21847) vms_mb | MB | 8 | 9125.098 | 1667.977 | 10213.410 | 10213.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21877) rss_mb | MB | 1 | 195.211 | 195.211 | 195.211 | 195.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21877) vms_mb | MB | 1 | 1615.473 | 1615.473 | 1615.473 | 1615.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21896) CPU | percent | 14 | 18.650 | 0.993 | 76.519 | 2.983 | 2.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21896) rss_mb | MB | 15 | 369.376 | 229.395 | 390.148 | 390.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21896) main thread run-queue wait | percent | 14 | 2.601 | 0.001 | 21.072 | 0.006 | 0.367196 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21896) vms_mb | MB | 15 | 9068.078 | 1635.535 | 10209.066 | 10209.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21916) CPU | percent | 1 | 60.505 | 60.505 | 60.505 | 60.505 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21916) rss_mb | MB | 2 | 178.137 | 118.770 | 237.504 | 237.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21916) main thread run-queue wait | percent | 1 | 12.061 | 12.061 | 12.061 | 12.061 | 0.121599 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21916) vms_mb | MB | 2 | 1466.979 | 1296.352 | 1637.605 | 1637.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21928) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 21928) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21929) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 21929) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21944) CPU | percent | 14 | 23.054 | 0.993 | 90.402 | 9.940 | 3.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21944) rss_mb | MB | 15 | 353.034 | 36.004 | 391.680 | 391.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21944) main thread run-queue wait | percent | 14 | 2.815 | 0.001 | 17.794 | 0.013 | 0.403178 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21944) vms_mb | MB | 15 | 9028.193 | 1169.793 | 10209.352 | 10209.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21964) CPU | percent | 1 | 64.113 | 64.113 | 64.113 | 64.113 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21964) rss_mb | MB | 2 | 223.570 | 173.012 | 274.129 | 274.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21964) main thread run-queue wait | percent | 1 | 17.174 | 17.174 | 17.174 | 17.174 | 0.174114 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21964) vms_mb | MB | 2 | 1625.012 | 1579.973 | 1670.051 | 1670.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 21972) rss_mb | MB | 1 | 48.859 | 48.859 | 48.859 | 48.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 21972) vms_mb | MB | 1 | 843.254 | 843.254 | 843.254 | 843.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21994) CPU | percent | 11 | 23.842 | 1.989 | 79.530 | 1.989 | 2.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21994) rss_mb | MB | 12 | 364.848 | 234.930 | 392.645 | 392.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21994) main thread run-queue wait | percent | 11 | 1.821 | 0.003 | 14.048 | 0.003 | 0.201788 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 21994) vms_mb | MB | 12 | 8786.002 | 1636.039 | 10213.078 | 10213.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22024) rss_mb | MB | 1 | 237.883 | 237.883 | 237.883 | 237.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22024) vms_mb | MB | 1 | 1638.371 | 1638.371 | 1638.371 | 1638.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22043) CPU | percent | 13 | 23.968 | 2.983 | 88.447 | 2.983 | 3.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22043) rss_mb | MB | 14 | 360.179 | 166.801 | 391.465 | 391.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22043) main thread run-queue wait | percent | 13 | 3.242 | 0.003 | 16.153 | 0.004 | 0.425227 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22043) vms_mb | MB | 14 | 8977.436 | 1577.719 | 10211.812 | 10211.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22063) CPU | percent | 1 | 61.173 | 61.173 | 61.173 | 61.173 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22063) rss_mb | MB | 2 | 216.021 | 171.684 | 260.359 | 260.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22063) main thread run-queue wait | percent | 1 | 14.666 | 14.666 | 14.666 | 14.666 | 0.148639 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22063) vms_mb | MB | 2 | 1617.775 | 1579.473 | 1656.078 | 1656.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22092) CPU | percent | 11 | 23.925 | 1.989 | 82.387 | 2.983 | 2.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22092) rss_mb | MB | 12 | 360.050 | 161.598 | 394.785 | 394.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22092) main thread run-queue wait | percent | 11 | 1.832 | 0.003 | 14.139 | 0.012 | 0.203238 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22092) vms_mb | MB | 12 | 8761.551 | 1500.215 | 10195.078 | 10195.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22115) CPU | percent | 1 | 59.575 | 59.575 | 59.575 | 59.575 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22115) rss_mb | MB | 2 | 213.643 | 167.000 | 260.285 | 260.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22115) main thread run-queue wait | percent | 1 | 12.250 | 12.250 | 12.250 | 12.250 | 0.123378 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22115) vms_mb | MB | 2 | 1617.262 | 1578.223 | 1656.301 | 1656.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22122) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22122) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22123) rss_mb | MB | 1 | 9.957 | 9.957 | 9.957 | 9.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22123) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22141) CPU | percent | 10 | 24.150 | 1.986 | 72.602 | 2.984 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22141) rss_mb | MB | 11 | 357.101 | 184.340 | 389.738 | 389.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22141) main thread run-queue wait | percent | 10 | 2.311 | 0.002 | 11.870 | 0.004 | 0.232775 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22141) vms_mb | MB | 11 | 8640.684 | 1593.219 | 10194.883 | 10194.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22162) CPU | percent | 1 | 74.427 | 74.427 | 74.427 | 74.427 | 0.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22162) rss_mb | MB | 2 | 240.926 | 184.180 | 297.672 | 297.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22162) main thread run-queue wait | percent | 1 | 14.194 | 14.194 | 14.194 | 14.194 | 0.143032 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22162) vms_mb | MB | 2 | 1642.855 | 1593.223 | 1692.488 | 1692.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22188) CPU | percent | 17 | 14.007 | 0.995 | 76.538 | 2.985 | 2.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22188) rss_mb | MB | 18 | 373.988 | 211.012 | 394.238 | 394.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22188) main thread run-queue wait | percent | 17 | 0.497 | 0.004 | 3.213 | 0.041 | 0.085121 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22188) vms_mb | MB | 18 | 9254.602 | 1622.547 | 10203.180 | 10203.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22206) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22206) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22207) rss_mb | MB | 1 | 8.793 | 8.793 | 8.793 | 8.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22207) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 22217) rss_mb | MB | 1 | 301.609 | 301.609 | 301.609 | 301.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 22217) vms_mb | MB | 1 | 1726.293 | 1726.293 | 1726.293 | 1726.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22236) CPU | percent | 12 | 24.239 | 0.995 | 92.316 | 2.984 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22236) rss_mb | MB | 13 | 346.210 | 35.113 | 387.797 | 387.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22236) main thread run-queue wait | percent | 12 | 1.685 | 0.004 | 11.816 | 0.018 | 0.203760 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22236) vms_mb | MB | 13 | 8849.780 | 1168.414 | 10207.270 | 10207.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22260) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22260) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22261) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22261) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22269) rss_mb | MB | 1 | 278.809 | 278.809 | 278.809 | 278.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22269) vms_mb | MB | 1 | 1673.812 | 1673.812 | 1673.812 | 1673.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22286) CPU | percent | 7 | 36.326 | 3.977 | 72.585 | 7.957 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22286) rss_mb | MB | 8 | 347.841 | 194.184 | 396.176 | 396.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22286) main thread run-queue wait | percent | 7 | 4.351 | 0.006 | 15.490 | 0.009 | 0.306763 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22286) vms_mb | MB | 8 | 8066.915 | 1614.469 | 10209.781 | 10209.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22305) CPU | percent | 1 | 57.587 | 57.587 | 57.587 | 57.587 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22305) rss_mb | MB | 2 | 265.824 | 229.207 | 302.441 | 302.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22305) main thread run-queue wait | percent | 1 | 13.838 | 13.838 | 13.838 | 13.838 | 0.139368 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22305) vms_mb | MB | 2 | 1679.436 | 1632.262 | 1726.609 | 1726.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22333) CPU | percent | 13 | 21.697 | 1.966 | 81.385 | 1.988 | 2.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22333) rss_mb | MB | 14 | 362.136 | 166.402 | 394.094 | 393.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22333) main thread run-queue wait | percent | 13 | 2.123 | 0.000 | 16.609 | 0.005 | 0.278157 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22333) vms_mb | MB | 14 | 8983.131 | 1577.719 | 10211.570 | 10210.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22354) CPU | percent | 1 | 56.527 | 56.527 | 56.527 | 56.527 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22354) rss_mb | MB | 2 | 213.742 | 167.812 | 259.672 | 259.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22354) main thread run-queue wait | percent | 1 | 21.907 | 21.907 | 21.907 | 21.907 | 0.220900 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22354) vms_mb | MB | 2 | 1616.906 | 1578.223 | 1655.590 | 1655.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22399) CPU | percent | 12 | 24.411 | 1.989 | 93.275 | 3.978 | 2.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22399) rss_mb | MB | 13 | 346.533 | 8.953 | 391.152 | 391.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22399) main thread run-queue wait | percent | 12 | 1.865 | 0.004 | 12.788 | 0.006 | 0.225515 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22399) vms_mb | MB | 13 | 8774.040 | 165.590 | 10209.688 | 10209.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22430) rss_mb | MB | 1 | 158.148 | 158.148 | 158.148 | 158.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22430) vms_mb | MB | 1 | 1314.930 | 1314.930 | 1314.930 | 1314.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22450) CPU | percent | 17 | 18.684 | 0.994 | 92.346 | 1.989 | 3.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22450) rss_mb | MB | 18 | 362.859 | 37.160 | 397.191 | 396.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22450) main thread run-queue wait | percent | 17 | 2.124 | 0.001 | 19.408 | 0.003 | 0.364197 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22450) vms_mb | MB | 18 | 9228.207 | 1170.816 | 10211.562 | 10210.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22472) CPU | percent | 1 | 46.562 | 46.562 | 46.562 | 46.562 | 0.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22472) rss_mb | MB | 2 | 194.818 | 160.871 | 228.766 | 228.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22472) main thread run-queue wait | percent | 1 | 9.960 | 9.960 | 9.960 | 9.960 | 0.100538 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22472) vms_mb | MB | 2 | 1474.547 | 1317.723 | 1631.371 | 1631.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22504) CPU | percent | 10 | 29.498 | 1.989 | 91.319 | 1.990 | 2.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22504) rss_mb | MB | 11 | 349.266 | 158.129 | 387.387 | 387.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22504) main thread run-queue wait | percent | 10 | 2.550 | 0.005 | 12.331 | 0.005 | 0.256747 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22504) vms_mb | MB | 11 | 8620.580 | 1314.922 | 10208.582 | 10208.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22529) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22529) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22530) rss_mb | MB | 1 | 7.246 | 7.246 | 7.246 | 7.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22530) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22535) rss_mb | MB | 1 | 205.516 | 205.516 | 205.516 | 205.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22535) vms_mb | MB | 1 | 1618.750 | 1618.750 | 1618.750 | 1618.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22555) CPU | percent | 13 | 18.573 | 1.986 | 75.599 | 2.982 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22555) rss_mb | MB | 14 | 366.343 | 243.766 | 387.047 | 387.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22555) main thread run-queue wait | percent | 13 | 2.732 | 0.003 | 17.917 | 0.004 | 0.357968 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22555) vms_mb | MB | 14 | 9569.837 | 1640.047 | 10206.469 | 10206.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22574) CPU | percent | 1 | 58.562 | 58.562 | 58.562 | 58.562 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22574) rss_mb | MB | 2 | 160.279 | 84.059 | 236.500 | 236.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22574) main thread run-queue wait | percent | 1 | 14.489 | 14.489 | 14.489 | 14.489 | 0.145974 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22574) vms_mb | MB | 2 | 1459.898 | 1283.695 | 1636.102 | 1636.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22603) CPU | percent | 10 | 26.575 | 1.988 | 82.374 | 6.961 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22603) rss_mb | MB | 11 | 365.319 | 259.980 | 391.723 | 391.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22603) main thread run-queue wait | percent | 10 | 3.729 | 0.002 | 26.118 | 0.073 | 0.393711 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22603) vms_mb | MB | 11 | 8651.857 | 1655.566 | 10206.180 | 10206.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22623) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22623) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22624) rss_mb | MB | 1 | 8.094 | 8.094 | 8.094 | 8.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22624) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22629) CPU | percent | 1 | 60.406 | 60.406 | 60.406 | 60.406 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22629) rss_mb | MB | 2 | 222.537 | 174.996 | 270.078 | 270.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22629) main thread run-queue wait | percent | 1 | 18.684 | 18.684 | 18.684 | 18.684 | 0.201055 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22629) vms_mb | MB | 2 | 1623.771 | 1581.973 | 1665.570 | 1665.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22637) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22637) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22638) rss_mb | MB | 1 | 9.340 | 9.340 | 9.340 | 9.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22638) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22648) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22648) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22649) rss_mb | MB | 1 | 9.980 | 9.980 | 9.980 | 9.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22649) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22653) CPU | percent | 12 | 27.462 | 1.988 | 80.404 | 1.988 | 3.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22653) rss_mb | MB | 13 | 359.697 | 193.855 | 392.121 | 392.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22653) main thread run-queue wait | percent | 12 | 4.281 | 0.002 | 19.734 | 0.003 | 0.517653 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22653) vms_mb | MB | 13 | 8884.250 | 1614.219 | 10209.180 | 10209.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22670) CPU | percent | 1 | 69.515 | 69.515 | 69.515 | 69.515 | 0.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22670) rss_mb | MB | 2 | 249.590 | 205.426 | 293.754 | 293.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22670) main thread run-queue wait | percent | 1 | 21.851 | 21.851 | 21.851 | 21.851 | 0.220039 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22670) vms_mb | MB | 2 | 1653.887 | 1618.719 | 1689.055 | 1689.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22685) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22685) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22701) CPU | percent | 16 | 20.166 | 0.000 | 91.058 | 0.000 | 3.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22701) rss_mb | MB | 17 | 351.692 | 0.000 | 390.645 | 389.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22701) main thread run-queue wait | percent | 16 | 1.867 | 0.001 | 14.937 | 0.004 | 0.300713 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22701) vms_mb | MB | 17 | 9098.326 | 0.004 | 10213.297 | 10212.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22722) rss_mb | MB | 1 | 202.398 | 202.398 | 202.398 | 202.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22722) vms_mb | MB | 1 | 1618.281 | 1618.281 | 1618.281 | 1618.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22827) CPU | percent | 10 | 22.136 | 0.995 | 75.434 | 4.974 | 2.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22827) rss_mb | MB | 11 | 356.884 | 203.648 | 390.234 | 390.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22827) main thread run-queue wait | percent | 10 | 0.914 | 0.004 | 3.891 | 0.024 | 0.092111 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22827) vms_mb | MB | 11 | 8652.369 | 1618.809 | 10208.477 | 10208.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22845) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22845) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22846) rss_mb | MB | 1 | 8.961 | 8.961 | 8.961 | 8.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22846) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22858) CPU | percent | 1 | 89.317 | 89.317 | 89.317 | 89.317 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22858) rss_mb | MB | 2 | 163.779 | 38.031 | 289.527 | 289.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22858) main thread run-queue wait | percent | 1 | 9.409 | 9.409 | 9.409 | 9.409 | 0.094810 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22858) vms_mb | MB | 2 | 1427.781 | 1171.504 | 1684.059 | 1684.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22877) CPU | percent | 14 | 18.792 | 0.995 | 73.518 | 3.978 | 2.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22877) rss_mb | MB | 15 | 369.158 | 220.840 | 393.137 | 393.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22877) main thread run-queue wait | percent | 14 | 3.102 | 0.002 | 21.548 | 0.010 | 0.437706 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22877) vms_mb | MB | 15 | 9065.344 | 1624.035 | 10207.688 | 10207.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22894) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22894) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22895) rss_mb | MB | 1 | 5.801 | 5.801 | 5.801 | 5.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22895) vms_mb | MB | 1 | 11.645 | 11.645 | 11.645 | 11.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22896) rss_mb | MB | 1 | 228.926 | 228.926 | 228.926 | 228.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22896) vms_mb | MB | 1 | 1636.332 | 1636.332 | 1636.332 | 1636.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22922) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 22922) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22923) rss_mb | MB | 1 | 8.809 | 8.809 | 8.809 | 8.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 22923) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22927) CPU | percent | 26 | 11.501 | 0.928 | 77.503 | 0.995 | 3.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22927) rss_mb | MB | 27 | 379.410 | 212.887 | 394.777 | 394.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22927) main thread run-queue wait | percent | 26 | 0.864 | 0.002 | 5.641 | 0.008 | 0.226133 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22927) vms_mb | MB | 27 | 9577.876 | 1622.777 | 10213.379 | 10213.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22953) CPU | percent | 1 | 74.507 | 74.507 | 74.507 | 74.507 | 0.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22953) rss_mb | MB | 2 | 230.650 | 166.305 | 294.996 | 294.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22953) main thread run-queue wait | percent | 1 | 11.408 | 11.408 | 11.408 | 11.408 | 0.114835 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22953) vms_mb | MB | 2 | 1633.760 | 1577.723 | 1689.797 | 1689.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22976) rss_mb | MB | 1 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 22976) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22977) rss_mb | MB | 1 | 27.676 | 27.676 | 27.676 | 27.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 22977) vms_mb | MB | 1 | 250.352 | 250.352 | 250.352 | 250.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22996) CPU | percent | 42 | 9.925 | 0.994 | 79.393 | 2.983 | 4.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22996) rss_mb | MB | 43 | 385.472 | 168.242 | 397.707 | 395.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22996) main thread run-queue wait | percent | 42 | 0.923 | 0.001 | 11.476 | 0.009 | 0.394018 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 22996) vms_mb | MB | 43 | 9812.120 | 1578.469 | 10213.566 | 10210.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23027) rss_mb | MB | 1 | 194.324 | 194.324 | 194.324 | 194.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23027) vms_mb | MB | 1 | 1614.973 | 1614.973 | 1614.973 | 1614.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23046) rss_mb | MB | 1 | 2.551 | 2.551 | 2.551 | 2.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23046) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23047) rss_mb | MB | 1 | 13.129 | 13.129 | 13.129 | 13.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 23047) vms_mb | MB | 1 | 207.277 | 207.277 | 207.277 | 207.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23066) rss_mb | MB | 1 | 2.719 | 2.719 | 2.719 | 2.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23066) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 23072) rss_mb | MB | 1 | 21.688 | 21.688 | 21.688 | 21.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 23072) vms_mb | MB | 1 | 27.363 | 27.363 | 27.363 | 27.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23073) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23073) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23085) CPU | percent | 12 | 23.741 | 1.989 | 78.343 | 1.989 | 2.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23085) rss_mb | MB | 13 | 360.496 | 166.852 | 394.605 | 394.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23085) main thread run-queue wait | percent | 12 | 2.705 | 0.003 | 22.799 | 0.007 | 0.327449 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23085) vms_mb | MB | 13 | 8889.606 | 1577.969 | 10210.023 | 10210.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23106) CPU | percent | 1 | 53.514 | 53.514 | 53.514 | 53.514 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23106) rss_mb | MB | 2 | 209.992 | 166.570 | 253.414 | 253.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23106) main thread run-queue wait | percent | 1 | 14.216 | 14.216 | 14.216 | 14.216 | 0.143454 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23106) vms_mb | MB | 2 | 1613.547 | 1577.973 | 1649.121 | 1649.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23113) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23113) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23114) rss_mb | MB | 1 | 10.586 | 10.586 | 10.586 | 10.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23114) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23132) CPU | percent | 13 | 19.880 | 0.995 | 79.515 | 9.945 | 2.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23132) rss_mb | MB | 14 | 372.769 | 259.750 | 392.844 | 392.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23132) main thread run-queue wait | percent | 13 | 0.921 | 0.001 | 7.658 | 0.017 | 0.120399 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23132) vms_mb | MB | 14 | 9587.508 | 1655.547 | 10211.207 | 10211.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23162) CPU | percent | 1 | 88.295 | 88.295 | 88.295 | 88.295 | 0.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23162) rss_mb | MB | 2 | 223.107 | 143.762 | 302.453 | 302.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23162) main thread run-queue wait | percent | 1 | 7.177 | 7.177 | 7.177 | 7.177 | 0.072343 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23162) vms_mb | MB | 2 | 1513.039 | 1299.805 | 1726.273 | 1726.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23184) CPU | percent | 13 | 20.752 | 0.993 | 77.321 | 6.962 | 2.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23184) rss_mb | MB | 14 | 368.474 | 228.902 | 391.512 | 391.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23184) main thread run-queue wait | percent | 13 | 3.496 | 0.002 | 30.532 | 0.024 | 0.458173 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23184) vms_mb | MB | 14 | 8989.259 | 1632.043 | 10210.418 | 10210.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23202) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23202) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23203) rss_mb | MB | 1 | 8.281 | 8.281 | 8.281 | 8.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23203) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23204) CPU | percent | 1 | 60.426 | 60.426 | 60.426 | 60.426 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23204) rss_mb | MB | 2 | 139.379 | 44.188 | 234.570 | 234.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23204) main thread run-queue wait | percent | 1 | 12.197 | 12.197 | 12.197 | 12.197 | 0.123134 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 23204) vms_mb | MB | 2 | 1235.500 | 835.379 | 1635.621 | 1635.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23232) CPU | percent | 14 | 20.558 | 0.995 | 75.377 | 4.974 | 2.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23232) rss_mb | MB | 15 | 369.179 | 211.773 | 393.133 | 393.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23232) main thread run-queue wait | percent | 14 | 3.570 | 0.004 | 30.727 | 0.016 | 0.503573 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23232) vms_mb | MB | 15 | 9068.920 | 1622.285 | 10211.203 | 10211.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23252) CPU | percent | 1 | 60.561 | 60.561 | 60.561 | 60.561 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23252) rss_mb | MB | 2 | 252.707 | 211.262 | 294.152 | 294.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23252) main thread run-queue wait | percent | 1 | 31.031 | 31.031 | 31.031 | 31.031 | 0.312565 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23252) vms_mb | MB | 2 | 1655.570 | 1622.027 | 1689.113 | 1689.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23264) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23264) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23265) rss_mb | MB | 1 | 10.008 | 10.008 | 10.008 | 10.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23265) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23285) CPU | percent | 12 | 24.757 | 1.988 | 83.499 | 1.989 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23285) rss_mb | MB | 13 | 361.770 | 168.324 | 396.816 | 395.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23285) main thread run-queue wait | percent | 12 | 2.809 | 0.001 | 21.883 | 0.001 | 0.339578 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23285) vms_mb | MB | 13 | 8885.773 | 1578.469 | 10209.062 | 10208.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23309) CPU | percent | 1 | 49.611 | 49.611 | 49.611 | 49.611 | 0.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23309) rss_mb | MB | 2 | 194.283 | 159.797 | 228.770 | 228.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23309) main thread run-queue wait | percent | 1 | 18.070 | 18.070 | 18.070 | 18.070 | 0.182117 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23309) vms_mb | MB | 2 | 1476.154 | 1316.461 | 1635.848 | 1635.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23338) CPU | percent | 13 | 19.191 | 0.995 | 72.561 | 2.984 | 2.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23338) rss_mb | MB | 14 | 372.858 | 254.125 | 396.789 | 395.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23338) main thread run-queue wait | percent | 13 | 2.396 | 0.001 | 15.525 | 0.004 | 0.323998 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23338) vms_mb | MB | 14 | 9584.288 | 1650.266 | 10212.656 | 10211.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23358) CPU | percent | 1 | 57.606 | 57.606 | 57.606 | 57.606 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23358) rss_mb | MB | 2 | 206.572 | 161.031 | 252.113 | 252.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23358) main thread run-queue wait | percent | 1 | 17.975 | 17.975 | 17.975 | 17.975 | 0.180981 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23358) vms_mb | MB | 2 | 1483.160 | 1317.723 | 1648.598 | 1648.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23372) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23372) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23373) rss_mb | MB | 1 | 8.160 | 8.160 | 8.160 | 8.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23373) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23391) CPU | percent | 14 | 18.789 | 1.987 | 76.359 | 2.984 | 2.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23391) rss_mb | MB | 15 | 371.425 | 235.328 | 393.812 | 393.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23391) main thread run-queue wait | percent | 14 | 1.808 | 0.003 | 18.971 | 0.006 | 0.254955 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23391) vms_mb | MB | 15 | 9069.564 | 1635.984 | 10211.676 | 10211.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — stty (PID 23409) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — stty (PID 23409) vms_mb | MB | 1 | 0.453 | 0.453 | 0.453 | 0.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23410) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23410) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23411) rss_mb | MB | 1 | 9.258 | 9.258 | 9.258 | 9.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23411) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23416) CPU | percent | 1 | 56.606 | 56.606 | 56.606 | 56.606 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23416) rss_mb | MB | 2 | 228.242 | 185.855 | 270.629 | 270.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23416) main thread run-queue wait | percent | 1 | 16.768 | 16.768 | 16.768 | 16.768 | 0.168850 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23416) vms_mb | MB | 2 | 1629.537 | 1593.223 | 1665.852 | 1665.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23426) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23426) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23427) rss_mb | MB | 1 | 8.113 | 8.113 | 8.113 | 8.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23427) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23465) CPU | percent | 12 | 24.187 | 1.990 | 84.415 | 4.975 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23465) rss_mb | MB | 13 | 362.451 | 172.773 | 395.258 | 395.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23465) main thread run-queue wait | percent | 12 | 1.568 | 0.005 | 8.123 | 0.016 | 0.189507 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23465) vms_mb | MB | 13 | 8889.356 | 1579.969 | 10210.609 | 10210.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23495) rss_mb | MB | 1 | 229.316 | 229.316 | 229.316 | 229.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23495) vms_mb | MB | 1 | 1631.699 | 1631.699 | 1631.699 | 1631.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23509) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23509) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23510) rss_mb | MB | 1 | 7.137 | 7.137 | 7.137 | 7.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23510) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23514) CPU | percent | 27 | 12.058 | 0.995 | 78.436 | 8.944 | 3.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23514) rss_mb | MB | 28 | 376.694 | 212.238 | 391.586 | 391.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23514) main thread run-queue wait | percent | 27 | 0.825 | 0.000 | 8.788 | 0.070 | 0.224522 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23514) vms_mb | MB | 28 | 9594.261 | 1622.781 | 10206.590 | 10205.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23531) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23531) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23532) rss_mb | MB | 1 | 8.020 | 8.020 | 8.020 | 8.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23532) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23541) rss_mb | MB | 1 | 235.035 | 235.035 | 235.035 | 235.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23541) vms_mb | MB | 1 | 1635.352 | 1635.352 | 1635.352 | 1635.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23560) CPU | percent | 8 | 10.289 | 0.000 | 72.409 | 0.000 | 0.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23560) rss_mb | MB | 9 | 25.607 | 2.703 | 65.719 | 65.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23560) main thread run-queue wait | percent | 8 | 0.015 | 0.000 | 0.067 | 0.000 | 0.001244 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 23560) vms_mb | MB | 9 | 31.749 | 3.848 | 80.414 | 80.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 23563) CPU | percent | 4 | 13.414 | 0.000 | 53.657 | 0.000 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 23563) rss_mb | MB | 5 | 60.051 | 36.770 | 65.871 | 65.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 23563) main thread run-queue wait | percent | 4 | 0.059 | 0.000 | 0.235 | 0.000 | 0.002364 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 23563) vms_mb | MB | 5 | 73.098 | 44.645 | 80.211 | 80.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23576) CPU | percent | 15 | 17.387 | 1.987 | 76.410 | 4.974 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23576) rss_mb | MB | 16 | 374.448 | 247.473 | 393.520 | 393.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23576) main thread run-queue wait | percent | 15 | 1.821 | 0.004 | 16.400 | 0.014 | 0.298747 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23576) vms_mb | MB | 16 | 9142.082 | 1643.031 | 10211.211 | 10211.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23599) CPU | percent | 1 | 61.814 | 61.814 | 61.814 | 61.814 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23599) rss_mb | MB | 2 | 242.914 | 188.719 | 297.109 | 297.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23599) main thread run-queue wait | percent | 1 | 15.622 | 15.622 | 15.622 | 15.622 | 0.179437 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23599) vms_mb | MB | 2 | 1642.854 | 1594.223 | 1691.484 | 1691.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23626) CPU | percent | 12 | 24.386 | 0.994 | 74.398 | 0.994 | 2.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23626) rss_mb | MB | 13 | 365.529 | 205.539 | 394.348 | 394.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23626) main thread run-queue wait | percent | 12 | 2.742 | 0.004 | 18.992 | 0.004 | 0.332104 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23626) vms_mb | MB | 13 | 8891.357 | 1619.035 | 10210.559 | 10210.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23648) CPU | percent | 1 | 62.526 | 62.526 | 62.526 | 62.526 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23648) rss_mb | MB | 2 | 236.398 | 193.664 | 279.133 | 279.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23648) main thread run-queue wait | percent | 1 | 18.934 | 18.934 | 18.934 | 18.934 | 0.190773 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23648) vms_mb | MB | 2 | 1644.400 | 1614.973 | 1673.828 | 1673.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23676) CPU | percent | 14 | 19.932 | 0.993 | 77.439 | 1.989 | 2.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23676) rss_mb | MB | 15 | 362.709 | 172.762 | 389.656 | 389.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23676) main thread run-queue wait | percent | 14 | 1.747 | 0.001 | 14.546 | 0.018 | 0.246249 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23676) vms_mb | MB | 15 | 9065.793 | 1579.719 | 10210.043 | 10210.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23698) CPU | percent | 1 | 45.671 | 45.671 | 45.671 | 45.671 | 0.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23698) rss_mb | MB | 2 | 199.875 | 163.527 | 236.223 | 236.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23698) main thread run-queue wait | percent | 1 | 18.914 | 18.914 | 18.914 | 18.914 | 0.190509 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23698) vms_mb | MB | 2 | 1604.277 | 1572.223 | 1636.332 | 1636.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23705) rss_mb | MB | 1 | 1.512 | 1.512 | 1.512 | 1.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 23705) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23706) rss_mb | MB | 1 | 10.359 | 10.359 | 10.359 | 10.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 23706) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23724) CPU | percent | 12 | 19.371 | 1.982 | 75.451 | 1.982 | 2.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23724) rss_mb | MB | 13 | 374.536 | 277.395 | 396.988 | 396.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23724) main thread run-queue wait | percent | 12 | 1.249 | 0.007 | 11.278 | 0.016 | 0.150719 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23724) vms_mb | MB | 13 | 8911.600 | 1673.035 | 10211.934 | 10210.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23754) rss_mb | MB | 1 | 278.934 | 278.934 | 278.934 | 278.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23754) vms_mb | MB | 1 | 1673.812 | 1673.812 | 1673.812 | 1673.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23852) CPU | percent | 14 | 20.892 | 0.994 | 75.410 | 1.989 | 2.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23852) rss_mb | MB | 15 | 365.637 | 177.121 | 396.496 | 395.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23852) main thread run-queue wait | percent | 14 | 2.922 | 0.001 | 25.686 | 0.001 | 0.412091 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23852) vms_mb | MB | 15 | 9063.736 | 1590.719 | 10210.062 | 10209.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23871) CPU | percent | 1 | 54.581 | 54.581 | 54.581 | 54.581 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23871) rss_mb | MB | 2 | 235.031 | 194.227 | 275.836 | 275.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23871) main thread run-queue wait | percent | 1 | 22.616 | 22.616 | 22.616 | 22.616 | 0.227896 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23871) vms_mb | MB | 2 | 1643.402 | 1614.723 | 1672.082 | 1672.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23903) CPU | percent | 14 | 22.109 | 0.994 | 91.218 | 1.989 | 3.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23903) rss_mb | MB | 15 | 367.317 | 144.117 | 401.711 | 401.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23903) main thread run-queue wait | percent | 14 | 2.847 | 0.002 | 18.107 | 0.007 | 0.420024 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23903) vms_mb | MB | 15 | 9039.668 | 1300.289 | 10211.254 | 10211.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23921) CPU | percent | 1 | 74.253 | 74.253 | 74.253 | 74.253 | 0.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23921) rss_mb | MB | 2 | 225.439 | 169.781 | 281.098 | 281.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23921) main thread run-queue wait | percent | 1 | 17.268 | 17.268 | 17.268 | 17.268 | 0.174417 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23921) vms_mb | MB | 2 | 1627.145 | 1578.723 | 1675.566 | 1675.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23951) CPU | percent | 12 | 19.743 | 0.994 | 78.389 | 2.984 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23951) rss_mb | MB | 13 | 373.415 | 295.262 | 390.844 | 390.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23951) main thread run-queue wait | percent | 12 | 1.843 | 0.002 | 9.575 | 0.002 | 0.238574 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23951) vms_mb | MB | 13 | 9542.862 | 1689.750 | 10211.484 | 10211.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23974) rss_mb | MB | 1 | 215.535 | 215.535 | 215.535 | 215.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 23974) vms_mb | MB | 1 | 1623.918 | 1623.918 | 1623.918 | 1623.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24003) CPU | percent | 13 | 25.502 | 0.993 | 94.422 | 5.967 | 3.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24003) rss_mb | MB | 14 | 352.862 | 62.551 | 391.449 | 391.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24003) main thread run-queue wait | percent | 13 | 1.217 | 0.005 | 8.133 | 0.012 | 0.159473 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24003) vms_mb | MB | 14 | 8952.802 | 1238.512 | 10211.340 | 10211.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 24023) rss_mb | MB | 1 | 48.566 | 48.566 | 48.566 | 48.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 24023) vms_mb | MB | 1 | 847.234 | 847.234 | 847.234 | 847.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24034) rss_mb | MB | 1 | 194.562 | 194.562 | 194.562 | 194.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24034) vms_mb | MB | 1 | 1614.723 | 1614.723 | 1614.723 | 1614.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 24042) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 24042) vms_mb | MB | 1 | 0.879 | 0.879 | 0.879 | 0.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24051) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24051) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24052) rss_mb | MB | 1 | 9.086 | 9.086 | 9.086 | 9.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24052) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24056) CPU | percent | 15 | 21.251 | 1.989 | 81.271 | 7.953 | 3.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24056) rss_mb | MB | 16 | 368.275 | 187.652 | 395.871 | 394.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24056) main thread run-queue wait | percent | 15 | 3.394 | 0.003 | 21.039 | 0.016 | 0.512915 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24056) vms_mb | MB | 16 | 9136.492 | 1593.969 | 10212.988 | 10212.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24075) CPU | percent | 1 | 62.436 | 62.436 | 62.436 | 62.436 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24075) rss_mb | MB | 2 | 217.977 | 175.262 | 260.691 | 260.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24075) main thread run-queue wait | percent | 1 | 17.425 | 17.425 | 17.425 | 17.425 | 0.175824 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24075) vms_mb | MB | 2 | 1623.029 | 1589.723 | 1656.336 | 1656.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24108) CPU | percent | 21 | 14.037 | 0.995 | 78.396 | 0.995 | 2.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24108) rss_mb | MB | 22 | 378.736 | 217.391 | 394.621 | 394.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24108) main thread run-queue wait | percent | 21 | 1.416 | 0.003 | 16.883 | 0.008 | 0.300083 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24108) vms_mb | MB | 22 | 9431.946 | 1623.266 | 10210.797 | 10210.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24135) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24135) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24136) rss_mb | MB | 1 | 8.113 | 8.113 | 8.113 | 8.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24136) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24137) rss_mb | MB | 1 | 228.664 | 228.664 | 228.664 | 228.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24137) vms_mb | MB | 1 | 1631.469 | 1631.469 | 1631.469 | 1631.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24159) CPU | percent | 8 | 28.321 | 1.990 | 78.516 | 8.954 | 2.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24159) rss_mb | MB | 9 | 361.432 | 256.574 | 391.074 | 391.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24159) main thread run-queue wait | percent | 8 | 4.120 | 0.006 | 18.721 | 0.031 | 0.331829 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24159) vms_mb | MB | 9 | 9239.612 | 1652.516 | 10210.266 | 10210.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24184) rss_mb | MB | 1 | 205.641 | 205.641 | 205.641 | 205.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24184) vms_mb | MB | 1 | 1619.488 | 1619.488 | 1619.488 | 1619.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24208) CPU | percent | 12 | 20.182 | 1.989 | 76.451 | 1.989 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24208) rss_mb | MB | 13 | 369.781 | 236.977 | 393.828 | 393.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24208) main thread run-queue wait | percent | 12 | 3.116 | 0.005 | 19.530 | 0.013 | 0.376963 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24208) vms_mb | MB | 13 | 8895.424 | 1638.277 | 10211.875 | 10211.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24227) CPU | percent | 1 | 60.502 | 60.502 | 60.502 | 60.502 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24227) rss_mb | MB | 2 | 175.158 | 95.820 | 254.496 | 254.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24227) main thread run-queue wait | percent | 1 | 11.316 | 11.316 | 11.316 | 11.316 | 0.114089 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24227) vms_mb | MB | 2 | 1466.635 | 1283.695 | 1649.574 | 1649.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24239) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24239) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24240) rss_mb | MB | 1 | 7.020 | 7.020 | 7.020 | 7.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24240) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24256) CPU | percent | 12 | 17.940 | 0.994 | 66.528 | 0.994 | 2.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24256) rss_mb | MB | 13 | 375.581 | 295.965 | 394.383 | 394.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24256) main thread run-queue wait | percent | 12 | 2.710 | 0.003 | 15.091 | 0.004 | 0.327478 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24256) vms_mb | MB | 13 | 9540.534 | 1690.926 | 10212.098 | 10212.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24275) CPU | percent | 1 | 61.595 | 61.595 | 61.595 | 61.595 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24275) rss_mb | MB | 2 | 221.963 | 174.770 | 269.156 | 269.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24275) main thread run-queue wait | percent | 1 | 16.416 | 16.416 | 16.416 | 16.416 | 0.165241 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24275) vms_mb | MB | 2 | 1623.482 | 1581.973 | 1664.992 | 1664.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24307) CPU | percent | 16 | 19.368 | 0.993 | 86.453 | 0.993 | 3.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24307) rss_mb | MB | 17 | 363.890 | 40.293 | 401.020 | 400.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24307) main thread run-queue wait | percent | 16 | 1.024 | 0.003 | 9.187 | 0.005 | 0.164964 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24307) vms_mb | MB | 17 | 9173.032 | 1172.289 | 10218.355 | 10217.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24334) rss_mb | MB | 1 | 170.207 | 170.207 | 170.207 | 170.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24334) vms_mb | MB | 1 | 1579.723 | 1579.723 | 1579.723 | 1579.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24358) CPU | percent | 13 | 22.019 | 0.995 | 78.505 | 1.990 | 2.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24358) rss_mb | MB | 14 | 359.759 | 167.262 | 388.020 | 388.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24358) main thread run-queue wait | percent | 13 | 2.540 | 0.003 | 15.041 | 0.004 | 0.332404 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24358) vms_mb | MB | 14 | 8978.853 | 1578.219 | 10207.012 | 10207.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24379) CPU | percent | 1 | 67.538 | 67.538 | 67.538 | 67.538 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24379) rss_mb | MB | 2 | 244.875 | 194.090 | 295.660 | 295.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24379) main thread run-queue wait | percent | 1 | 16.823 | 16.823 | 16.823 | 16.823 | 0.169378 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24379) vms_mb | MB | 2 | 1652.465 | 1614.473 | 1690.457 | 1690.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24389) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24389) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24390) rss_mb | MB | 1 | 8.797 | 8.797 | 8.797 | 8.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24390) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24408) CPU | percent | 13 | 20.997 | 1.817 | 86.368 | 1.989 | 2.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24408) rss_mb | MB | 14 | 363.704 | 148.047 | 400.188 | 399.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24408) main thread run-queue wait | percent | 13 | 0.883 | 0.004 | 6.719 | 0.011 | 0.115566 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24408) vms_mb | MB | 14 | 8952.914 | 1304.227 | 10202.344 | 10201.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24431) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24431) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24432) rss_mb | MB | 1 | 7.289 | 7.289 | 7.289 | 7.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24432) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24438) rss_mb | MB | 1 | 213.289 | 213.289 | 213.289 | 213.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24438) vms_mb | MB | 1 | 1622.980 | 1622.980 | 1622.980 | 1622.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24460) CPU | percent | 12 | 17.946 | 0.994 | 68.528 | 2.985 | 2.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24460) rss_mb | MB | 13 | 374.266 | 288.309 | 396.688 | 395.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24460) main thread run-queue wait | percent | 12 | 2.657 | 0.005 | 18.792 | 0.007 | 0.321354 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24460) vms_mb | MB | 13 | 9535.750 | 1683.250 | 10212.543 | 10211.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24478) CPU | percent | 1 | 65.484 | 65.484 | 65.484 | 65.484 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24478) rss_mb | MB | 2 | 234.852 | 189.215 | 280.488 | 280.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24478) main thread run-queue wait | percent | 1 | 14.965 | 14.965 | 14.965 | 14.965 | 0.150833 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24478) vms_mb | MB | 2 | 1634.756 | 1594.223 | 1675.289 | 1675.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24490) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24490) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24491) rss_mb | MB | 1 | 10.551 | 10.551 | 10.551 | 10.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24491) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24528) CPU | percent | 14 | 18.070 | 0.995 | 77.417 | 1.990 | 2.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24528) rss_mb | MB | 15 | 371.500 | 238.969 | 392.738 | 392.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24528) main thread run-queue wait | percent | 14 | 1.575 | 0.001 | 15.850 | 0.008 | 0.238161 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24528) vms_mb | MB | 15 | 9066.918 | 1639.051 | 10207.188 | 10207.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24546) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24546) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24547) rss_mb | MB | 1 | 8.625 | 8.625 | 8.625 | 8.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24547) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24557) CPU | percent | 1 | 63.287 | 63.287 | 63.287 | 63.287 | 0.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24557) rss_mb | MB | 2 | 209.240 | 147.398 | 271.082 | 271.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24557) main thread run-queue wait | percent | 1 | 14.022 | 14.022 | 14.022 | 14.022 | 0.155098 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24557) vms_mb | MB | 2 | 1485.088 | 1303.867 | 1666.309 | 1666.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24578) CPU | percent | 14 | 20.708 | 1.986 | 76.463 | 3.976 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24578) rss_mb | MB | 15 | 368.788 | 198.367 | 393.871 | 393.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24578) main thread run-queue wait | percent | 14 | 1.799 | 0.001 | 15.552 | 0.007 | 0.254762 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24578) vms_mb | MB | 15 | 9065.270 | 1617.035 | 10208.367 | 10208.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24603) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24603) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24604) rss_mb | MB | 1 | 7.059 | 7.059 | 7.059 | 7.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24604) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24608) rss_mb | MB | 1 | 213.160 | 213.160 | 213.160 | 213.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24608) vms_mb | MB | 1 | 1623.469 | 1623.469 | 1623.469 | 1623.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 24620) rss_mb | MB | 1 | 2.211 | 2.211 | 2.211 | 2.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 24620) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 24621) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 24621) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24630) CPU | percent | 16 | 23.312 | 1.984 | 90.255 | 4.968 | 3.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24630) rss_mb | MB | 17 | 365.036 | 166.867 | 393.598 | 393.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24630) main thread run-queue wait | percent | 16 | 3.199 | 0.003 | 25.480 | 0.046 | 0.516405 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24630) vms_mb | MB | 17 | 9191.574 | 1577.969 | 10211.270 | 10211.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24651) CPU | percent | 2 | 53.009 | 48.535 | 57.483 | 48.535 | 1.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24651) rss_mb | MB | 3 | 220.676 | 144.074 | 288.715 | 288.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24651) main thread run-queue wait | percent | 2 | 19.608 | 16.430 | 22.786 | 22.786 | 0.395821 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24651) vms_mb | MB | 3 | 1538.783 | 1300.309 | 1683.812 | 1683.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24678) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24678) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24679) rss_mb | MB | 1 | 8.797 | 8.797 | 8.797 | 8.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24679) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24683) CPU | percent | 13 | 27.061 | 1.987 | 88.362 | 1.987 | 3.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24683) rss_mb | MB | 14 | 359.303 | 183.738 | 388.320 | 388.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24683) main thread run-queue wait | percent | 13 | 2.701 | 0.003 | 23.819 | 0.006 | 0.356526 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24683) vms_mb | MB | 14 | 8978.899 | 1592.969 | 10209.164 | 10209.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24709) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24709) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24710) rss_mb | MB | 1 | 9.375 | 9.375 | 9.375 | 9.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24710) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24712) CPU | percent | 1 | 53.976 | 53.976 | 53.976 | 53.976 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24712) rss_mb | MB | 2 | 106.705 | 0.586 | 212.824 | 212.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24712) main thread run-queue wait | percent | 1 | 17.628 | 17.628 | 17.628 | 17.628 | 0.179622 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24712) vms_mb | MB | 2 | 893.121 | 163.281 | 1622.961 | 1622.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24733) CPU | percent | 10 | 21.164 | 1.989 | 74.545 | 4.974 | 2.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24733) rss_mb | MB | 11 | 369.611 | 279.922 | 395.703 | 395.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24733) main thread run-queue wait | percent | 10 | 4.301 | 0.004 | 22.938 | 0.008 | 0.459595 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24733) vms_mb | MB | 11 | 9414.774 | 1674.688 | 10206.453 | 10206.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24752) CPU | percent | 1 | 67.103 | 67.103 | 67.103 | 67.103 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24752) rss_mb | MB | 2 | 216.465 | 163.418 | 269.512 | 269.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24752) main thread run-queue wait | percent | 1 | 21.926 | 21.926 | 21.926 | 21.926 | 0.222195 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24752) vms_mb | MB | 2 | 1618.766 | 1572.473 | 1665.059 | 1665.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24780) CPU | percent | 15 | 15.691 | 0.994 | 73.580 | 0.995 | 2.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24780) rss_mb | MB | 16 | 378.035 | 252.992 | 398.363 | 397.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24780) main thread run-queue wait | percent | 15 | 2.432 | 0.003 | 18.861 | 0.007 | 0.377733 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24780) vms_mb | MB | 16 | 9661.165 | 1649.035 | 10210.855 | 10209.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24800) CPU | percent | 1 | 60.371 | 60.371 | 60.371 | 60.371 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24800) rss_mb | MB | 2 | 209.654 | 160.605 | 258.703 | 258.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24800) main thread run-queue wait | percent | 1 | 14.160 | 14.160 | 14.160 | 14.160 | 0.143078 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24800) vms_mb | MB | 2 | 1486.088 | 1317.090 | 1655.086 | 1655.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24812) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 24812) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24813) rss_mb | MB | 1 | 8.133 | 8.133 | 8.133 | 8.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 24813) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24832) CPU | percent | 14 | 20.655 | 0.995 | 81.365 | 5.969 | 2.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24832) rss_mb | MB | 15 | 359.021 | 154.980 | 388.641 | 388.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24832) main thread run-queue wait | percent | 14 | 1.738 | 0.003 | 12.191 | 0.026 | 0.244855 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 24832) vms_mb | MB | 15 | 9052.833 | 1499.465 | 10209.941 | 10209.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25001) rss_mb | MB | 1 | 166.793 | 166.793 | 166.793 | 166.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25001) vms_mb | MB | 1 | 1577.973 | 1577.973 | 1577.973 | 1577.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25023) CPU | percent | 7 | 33.290 | 3.970 | 77.478 | 7.959 | 2.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25023) rss_mb | MB | 8 | 356.686 | 239.262 | 391.387 | 391.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25023) main thread run-queue wait | percent | 7 | 1.707 | 0.038 | 3.906 | 0.038 | 0.121705 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25023) vms_mb | MB | 8 | 8078.975 | 1639.297 | 10212.082 | 10212.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25041) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25041) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25042) rss_mb | MB | 1 | 9.742 | 9.742 | 9.742 | 9.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25042) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25053) rss_mb | MB | 1 | 295.652 | 295.652 | 295.652 | 295.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25053) vms_mb | MB | 1 | 1690.730 | 1690.730 | 1690.730 | 1690.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25073) CPU | percent | 13 | 21.246 | 0.994 | 66.641 | 5.970 | 2.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25073) rss_mb | MB | 14 | 367.073 | 187.434 | 395.562 | 395.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25073) main thread run-queue wait | percent | 13 | 1.812 | 0.001 | 15.139 | 0.020 | 0.237255 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25073) vms_mb | MB | 14 | 8980.897 | 1593.969 | 10206.730 | 10206.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25098) rss_mb | MB | 1 | 197.797 | 197.797 | 197.797 | 197.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25098) vms_mb | MB | 1 | 1616.711 | 1616.711 | 1616.711 | 1616.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25120) CPU | percent | 15 | 18.717 | 0.988 | 69.338 | 4.970 | 2.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25120) rss_mb | MB | 16 | 366.525 | 200.930 | 391.984 | 391.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25120) main thread run-queue wait | percent | 15 | 2.302 | 0.002 | 21.036 | 0.010 | 0.348151 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25120) vms_mb | MB | 16 | 9139.789 | 1618.277 | 10213.121 | 10212.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25139) CPU | percent | 1 | 55.508 | 55.508 | 55.508 | 55.508 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25139) rss_mb | MB | 2 | 254.756 | 214.578 | 294.934 | 294.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25139) main thread run-queue wait | percent | 1 | 20.330 | 20.330 | 20.330 | 20.330 | 0.205103 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25139) vms_mb | MB | 2 | 1656.012 | 1622.719 | 1689.305 | 1689.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25150) rss_mb | MB | 1 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25150) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25151) rss_mb | MB | 1 | 9.148 | 9.148 | 9.148 | 9.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25151) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25171) CPU | percent | 14 | 18.987 | 0.984 | 78.168 | 4.968 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25171) rss_mb | MB | 15 | 371.035 | 208.422 | 396.871 | 396.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25171) main thread run-queue wait | percent | 14 | 2.890 | 0.004 | 17.805 | 0.013 | 0.408006 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25171) vms_mb | MB | 15 | 9069.553 | 1619.285 | 10211.547 | 10211.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 25184) rss_mb | MB | 1 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 25184) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 25185) rss_mb | MB | 1 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 25185) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25188) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25188) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25189) rss_mb | MB | 1 | 7.207 | 7.207 | 7.207 | 7.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25189) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25190) rss_mb | MB | 1 | 228.531 | 228.531 | 228.531 | 228.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25190) vms_mb | MB | 1 | 1635.594 | 1635.594 | 1635.594 | 1635.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25217) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25217) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25218) rss_mb | MB | 1 | 9.594 | 9.594 | 9.594 | 9.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25218) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25222) CPU | percent | 14 | 19.943 | 0.995 | 71.630 | 6.963 | 2.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25222) rss_mb | MB | 15 | 368.752 | 193.465 | 398.391 | 397.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25222) main thread run-queue wait | percent | 14 | 2.571 | 0.005 | 26.919 | 0.036 | 0.362834 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25222) vms_mb | MB | 15 | 9064.407 | 1613.969 | 10208.750 | 10207.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25242) CPU | percent | 1 | 61.466 | 61.466 | 61.466 | 61.466 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25242) rss_mb | MB | 2 | 251.070 | 206.172 | 295.969 | 295.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25242) main thread run-queue wait | percent | 1 | 19.719 | 19.719 | 19.719 | 19.719 | 0.198897 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25242) vms_mb | MB | 2 | 1654.914 | 1619.496 | 1690.332 | 1690.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25274) CPU | percent | 13 | 21.439 | 0.993 | 84.364 | 2.984 | 2.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25274) rss_mb | MB | 14 | 376.217 | 272.043 | 399.086 | 398.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25274) main thread run-queue wait | percent | 13 | 2.009 | 0.003 | 17.588 | 0.007 | 0.263793 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25274) vms_mb | MB | 14 | 8993.799 | 1667.113 | 10211.223 | 10210.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25292) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25292) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25293) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25293) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25296) CPU | percent | 1 | 53.444 | 53.444 | 53.444 | 53.444 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25296) rss_mb | MB | 2 | 213.746 | 176.203 | 251.289 | 251.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25296) main thread run-queue wait | percent | 1 | 21.861 | 21.861 | 21.861 | 21.861 | 0.220881 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25296) vms_mb | MB | 2 | 1619.148 | 1590.723 | 1647.574 | 1647.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25306) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25306) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25307) rss_mb | MB | 1 | 4.664 | 4.664 | 4.664 | 4.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25307) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25325) CPU | percent | 30 | 13.667 | 0.988 | 93.387 | 6.962 | 4.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25325) rss_mb | MB | 31 | 378.343 | 111.199 | 398.395 | 398.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25325) main thread run-queue wait | percent | 30 | 1.613 | 0.003 | 14.309 | 0.009 | 0.487932 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25325) vms_mb | MB | 31 | 9639.009 | 1283.598 | 10210.566 | 10210.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25343) CPU | percent | 1 | 64.413 | 64.413 | 64.413 | 64.413 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25343) rss_mb | MB | 2 | 233.715 | 189.496 | 277.934 | 277.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25343) main thread run-queue wait | percent | 1 | 13.560 | 13.560 | 13.560 | 13.560 | 0.136833 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25343) vms_mb | MB | 2 | 1633.893 | 1594.473 | 1673.312 | 1673.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25355) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25355) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25356) rss_mb | MB | 1 | 6.992 | 6.992 | 6.992 | 6.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25356) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 25374) CPU | percent | 8 | 9.785 | 0.000 | 59.539 | 3.963 | 0.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 25374) rss_mb | MB | 9 | 26.804 | 2.766 | 65.836 | 65.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 25374) main thread run-queue wait | percent | 8 | 0.021 | 0.000 | 0.129 | 0.022 | 0.001694 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 25374) vms_mb | MB | 9 | 33.326 | 3.848 | 80.434 | 80.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 25377) CPU | percent | 4 | 16.136 | 0.000 | 64.544 | 0.000 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 25377) rss_mb | MB | 5 | 58.052 | 26.496 | 65.941 | 65.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 25377) main thread run-queue wait | percent | 4 | 0.023 | 0.000 | 0.092 | 0.000 | 0.000928 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 25377) vms_mb | MB | 5 | 70.762 | 33.121 | 80.172 | 80.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25391) CPU | percent | 14 | 21.129 | 1.986 | 69.595 | 6.963 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25391) rss_mb | MB | 15 | 371.327 | 202.945 | 400.047 | 399.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25391) main thread run-queue wait | percent | 14 | 2.704 | 0.003 | 23.017 | 0.011 | 0.382072 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25391) vms_mb | MB | 15 | 9069.409 | 1618.570 | 10214.316 | 10213.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25410) CPU | percent | 1 | 61.325 | 61.325 | 61.325 | 61.325 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25410) rss_mb | MB | 2 | 248.285 | 202.613 | 293.957 | 293.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25410) main thread run-queue wait | percent | 1 | 21.133 | 21.133 | 21.133 | 21.133 | 0.213659 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25410) vms_mb | MB | 2 | 1653.631 | 1618.227 | 1689.035 | 1689.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25420) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25420) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25441) CPU | percent | 16 | 18.945 | 0.995 | 83.460 | 2.979 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25441) rss_mb | MB | 17 | 367.753 | 175.199 | 393.387 | 392.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25441) main thread run-queue wait | percent | 16 | 1.061 | 0.002 | 10.935 | 0.009 | 0.170789 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25441) vms_mb | MB | 17 | 9200.867 | 1589.969 | 10212.641 | 10211.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25467) rss_mb | MB | 1 | 194.406 | 194.406 | 194.406 | 194.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25467) vms_mb | MB | 1 | 1614.473 | 1614.473 | 1614.473 | 1614.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25494) CPU | percent | 14 | 18.372 | 0.995 | 77.416 | 6.958 | 2.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25494) rss_mb | MB | 15 | 376.405 | 256.715 | 396.879 | 396.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25494) main thread run-queue wait | percent | 14 | 2.615 | 0.005 | 18.195 | 0.020 | 0.368505 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25494) vms_mb | MB | 15 | 9624.979 | 1652.559 | 10213.785 | 10213.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25514) CPU | percent | 1 | 60.605 | 60.605 | 60.605 | 60.605 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25514) rss_mb | MB | 2 | 155.268 | 74.840 | 235.695 | 235.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25514) main thread run-queue wait | percent | 1 | 15.601 | 15.601 | 15.601 | 15.601 | 0.157025 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25514) vms_mb | MB | 2 | 1459.895 | 1283.695 | 1636.094 | 1636.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 25538) rss_mb | MB | 1 | 58.180 | 58.180 | 58.180 | 58.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 25538) vms_mb | MB | 1 | 903.160 | 903.160 | 903.160 | 903.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25540) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25540) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25541) rss_mb | MB | 1 | 9.008 | 9.008 | 9.008 | 9.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25541) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25545) CPU | percent | 13 | 21.385 | 1.988 | 71.482 | 1.988 | 2.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25545) rss_mb | MB | 14 | 367.882 | 217.613 | 394.219 | 394.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25545) main thread run-queue wait | percent | 13 | 1.989 | 0.004 | 13.999 | 0.009 | 0.260566 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25545) vms_mb | MB | 14 | 8985.942 | 1623.293 | 10210.457 | 10210.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25569) CPU | percent | 1 | 52.578 | 52.578 | 52.578 | 52.578 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25569) rss_mb | MB | 2 | 210.900 | 167.703 | 254.098 | 254.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25569) main thread run-queue wait | percent | 1 | 16.281 | 16.281 | 16.281 | 16.281 | 0.164113 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25569) vms_mb | MB | 2 | 1614.176 | 1578.473 | 1649.879 | 1649.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25593) CPU | percent | 14 | 19.524 | 0.994 | 78.557 | 9.936 | 2.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25593) rss_mb | MB | 15 | 373.680 | 240.445 | 397.770 | 396.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25593) main thread run-queue wait | percent | 14 | 3.132 | 0.002 | 29.573 | 0.020 | 0.441279 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25593) vms_mb | MB | 15 | 9068.598 | 1639.047 | 10210.016 | 10208.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25631) CPU | percent | 1 | 51.670 | 51.670 | 51.670 | 51.670 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25631) rss_mb | MB | 2 | 244.727 | 211.074 | 278.379 | 278.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25631) main thread run-queue wait | percent | 1 | 20.904 | 20.904 | 20.904 | 20.904 | 0.210371 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25631) vms_mb | MB | 2 | 1647.848 | 1622.680 | 1673.016 | 1673.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25662) CPU | percent | 15 | 16.624 | 0.994 | 76.511 | 1.988 | 2.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25662) rss_mb | MB | 16 | 377.113 | 235.418 | 398.594 | 398.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25662) main thread run-queue wait | percent | 15 | 0.949 | 0.002 | 7.159 | 0.002 | 0.146306 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25662) vms_mb | MB | 16 | 9144.129 | 1636.297 | 10211.723 | 10211.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25679) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25679) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25680) rss_mb | MB | 1 | 8.922 | 8.922 | 8.922 | 8.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25680) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25690) rss_mb | MB | 1 | 238.035 | 238.035 | 238.035 | 238.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25690) vms_mb | MB | 1 | 1638.570 | 1638.570 | 1638.570 | 1638.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25709) CPU | percent | 13 | 18.620 | 1.977 | 76.415 | 2.983 | 2.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25709) rss_mb | MB | 14 | 380.390 | 294.449 | 399.746 | 398.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25709) main thread run-queue wait | percent | 13 | 2.051 | 0.002 | 15.306 | 0.004 | 0.269179 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25709) vms_mb | MB | 14 | 9589.021 | 1689.359 | 10213.484 | 10212.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25735) CPU | percent | 1 | 70.384 | 70.384 | 70.384 | 70.384 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25735) rss_mb | MB | 2 | 245.645 | 193.820 | 297.469 | 297.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25735) main thread run-queue wait | percent | 1 | 21.462 | 21.462 | 21.462 | 21.462 | 0.216500 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25735) vms_mb | MB | 2 | 1669.062 | 1614.473 | 1723.652 | 1723.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25762) CPU | percent | 19 | 16.309 | 0.994 | 82.310 | 0.994 | 3.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25762) rss_mb | MB | 20 | 369.357 | 155.156 | 391.812 | 391.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25762) main thread run-queue wait | percent | 19 | 0.991 | 0.002 | 7.833 | 0.009 | 0.189769 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25762) vms_mb | MB | 20 | 9348.546 | 1499.465 | 10213.102 | 10212.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25785) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 25785) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25786) rss_mb | MB | 1 | 5.664 | 5.664 | 5.664 | 5.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 25786) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25793) rss_mb | MB | 1 | 175.879 | 175.879 | 175.879 | 175.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25793) vms_mb | MB | 1 | 1590.223 | 1590.223 | 1590.223 | 1590.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25815) CPU | percent | 14 | 18.087 | 0.995 | 77.317 | 2.985 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25815) rss_mb | MB | 15 | 371.323 | 254.000 | 391.043 | 391.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25815) main thread run-queue wait | percent | 14 | 1.132 | 0.001 | 9.614 | 0.008 | 0.159372 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25815) vms_mb | MB | 15 | 9068.758 | 1650.309 | 10204.664 | 10204.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — stty (PID 25833) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — stty (PID 25833) vms_mb | MB | 1 | 0.422 | 0.422 | 0.422 | 0.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25847) CPU | percent | 1 | 89.351 | 89.351 | 89.351 | 89.351 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25847) rss_mb | MB | 2 | 171.148 | 46.168 | 296.129 | 296.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25847) main thread run-queue wait | percent | 1 | 8.294 | 8.294 | 8.294 | 8.294 | 0.083544 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25847) vms_mb | MB | 2 | 1432.535 | 1174.359 | 1690.711 | 1690.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25866) CPU | percent | 12 | 20.865 | 0.995 | 75.590 | 0.995 | 2.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25866) rss_mb | MB | 13 | 368.885 | 260.316 | 388.504 | 388.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25866) main thread run-queue wait | percent | 12 | 1.878 | 0.005 | 13.081 | 0.011 | 0.230170 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25866) vms_mb | MB | 13 | 8911.908 | 1656.270 | 10213.320 | 10213.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25895) rss_mb | MB | 1 | 291.012 | 291.012 | 291.012 | 291.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25895) vms_mb | MB | 1 | 1686.070 | 1686.070 | 1686.070 | 1686.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25914) CPU | percent | 13 | 24.761 | 0.995 | 89.417 | 1.990 | 3.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25914) rss_mb | MB | 14 | 353.371 | 40.199 | 397.203 | 397.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25914) main thread run-queue wait | percent | 13 | 3.498 | 0.003 | 24.283 | 0.003 | 0.461816 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25914) vms_mb | MB | 14 | 8942.575 | 1172.289 | 10212.086 | 10212.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25997) CPU | percent | 1 | 59.528 | 59.528 | 59.528 | 59.528 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25997) rss_mb | MB | 2 | 203.250 | 154.195 | 252.305 | 252.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25997) main thread run-queue wait | percent | 1 | 8.336 | 8.336 | 8.336 | 8.336 | 0.084026 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 25997) vms_mb | MB | 2 | 1573.785 | 1499.469 | 1648.102 | 1648.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26023) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26023) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26024) rss_mb | MB | 1 | 8.145 | 8.145 | 8.145 | 8.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26024) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26039) CPU | percent | 14 | 16.881 | 0.995 | 79.431 | 0.995 | 2.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26039) rss_mb | MB | 15 | 378.430 | 285.305 | 398.359 | 397.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26039) main thread run-queue wait | percent | 14 | 0.675 | 0.005 | 5.004 | 0.005 | 0.095137 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26039) vms_mb | MB | 15 | 9084.782 | 1680.484 | 10212.254 | 10211.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26069) rss_mb | MB | 1 | 166.965 | 166.965 | 166.965 | 166.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26069) vms_mb | MB | 1 | 1577.973 | 1577.973 | 1577.973 | 1577.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26091) CPU | percent | 13 | 18.254 | 0.993 | 72.597 | 1.989 | 2.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26091) rss_mb | MB | 14 | 375.865 | 286.449 | 394.512 | 394.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26091) main thread run-queue wait | percent | 13 | 2.831 | 0.003 | 16.205 | 0.004 | 0.371039 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26091) vms_mb | MB | 14 | 9588.197 | 1681.461 | 10211.738 | 10211.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26112) CPU | percent | 1 | 61.545 | 61.545 | 61.545 | 61.545 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26112) rss_mb | MB | 2 | 207.416 | 159.188 | 255.645 | 255.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26112) main thread run-queue wait | percent | 1 | 12.779 | 12.779 | 12.779 | 12.779 | 0.128736 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26112) vms_mb | MB | 2 | 1575.656 | 1499.969 | 1651.344 | 1651.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26124) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26124) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26125) rss_mb | MB | 1 | 6.047 | 6.047 | 6.047 | 6.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26125) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 26133) rss_mb | MB | 1 | 2.191 | 2.191 | 2.191 | 2.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 26133) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 26134) rss_mb | MB | 1 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 26134) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26143) CPU | percent | 18 | 18.994 | 0.994 | 89.454 | 7.957 | 3.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26143) rss_mb | MB | 19 | 368.081 | 73.422 | 399.113 | 398.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26143) main thread run-queue wait | percent | 18 | 1.039 | 0.002 | 7.269 | 0.031 | 0.188133 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26143) vms_mb | MB | 19 | 9287.282 | 1283.598 | 10215.160 | 10214.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26174) rss_mb | MB | 1 | 175.195 | 175.195 | 175.195 | 175.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26174) vms_mb | MB | 1 | 1589.973 | 1589.973 | 1589.973 | 1589.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26196) CPU | percent | 15 | 20.388 | 1.989 | 74.495 | 1.989 | 3.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26196) rss_mb | MB | 16 | 365.948 | 199.562 | 391.992 | 391.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26196) main thread run-queue wait | percent | 15 | 2.266 | 0.001 | 11.286 | 0.013 | 0.342815 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26196) vms_mb | MB | 16 | 9138.499 | 1617.789 | 10212.578 | 10212.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26215) CPU | percent | 1 | 64.316 | 64.316 | 64.316 | 64.316 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26215) rss_mb | MB | 2 | 232.029 | 186.531 | 277.527 | 277.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26215) main thread run-queue wait | percent | 1 | 14.755 | 14.755 | 14.755 | 14.755 | 0.149117 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26215) vms_mb | MB | 2 | 1633.029 | 1593.723 | 1672.336 | 1672.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26225) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26225) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 26236) rss_mb | MB | 1 | 2.039 | 2.039 | 2.039 | 2.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 26236) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 26237) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 26237) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26246) CPU | percent | 12 | 20.184 | 1.978 | 74.469 | 1.989 | 2.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26246) rss_mb | MB | 13 | 371.218 | 271.832 | 392.953 | 392.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26246) main thread run-queue wait | percent | 12 | 1.459 | 0.003 | 9.040 | 0.005 | 0.176542 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26246) vms_mb | MB | 13 | 9539.116 | 1667.512 | 10211.930 | 10211.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26274) CPU | percent | 1 | 70.444 | 70.444 | 70.444 | 70.444 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26274) rss_mb | MB | 2 | 215.607 | 152.957 | 278.258 | 278.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26274) main thread run-queue wait | percent | 1 | 11.094 | 11.094 | 11.094 | 11.094 | 0.111814 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26274) vms_mb | MB | 2 | 1586.498 | 1499.219 | 1673.777 | 1673.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 26289) rss_mb | MB | 1 | 2.012 | 2.012 | 2.012 | 2.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 26289) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 26290) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 26290) vms_mb | MB | 1 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26296) CPU | percent | 15 | 20.791 | 0.994 | 86.362 | 6.964 | 3.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26296) rss_mb | MB | 16 | 367.825 | 155.855 | 399.160 | 398.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26296) main thread run-queue wait | percent | 15 | 2.663 | 0.002 | 16.075 | 0.016 | 0.402313 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26296) vms_mb | MB | 16 | 9118.954 | 1311.992 | 10213.934 | 10212.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26316) CPU | percent | 1 | 59.604 | 59.604 | 59.604 | 59.604 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26316) rss_mb | MB | 2 | 217.402 | 174.023 | 260.781 | 260.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26316) main thread run-queue wait | percent | 1 | 15.099 | 15.099 | 15.099 | 15.099 | 0.151998 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26316) vms_mb | MB | 2 | 1618.902 | 1581.223 | 1656.582 | 1656.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26347) CPU | percent | 14 | 19.873 | 0.995 | 73.591 | 2.984 | 2.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26347) rss_mb | MB | 15 | 367.031 | 208.980 | 391.867 | 390.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26347) main thread run-queue wait | percent | 14 | 1.169 | 0.005 | 6.823 | 0.005 | 0.164737 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26347) vms_mb | MB | 15 | 9070.545 | 1619.523 | 10213.355 | 10212.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26373) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26373) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26374) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26374) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26378) rss_mb | MB | 1 | 205.516 | 205.516 | 205.516 | 205.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26378) vms_mb | MB | 1 | 1618.691 | 1618.691 | 1618.691 | 1618.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26400) CPU | percent | 20 | 16.256 | 0.995 | 89.349 | 1.989 | 3.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26400) rss_mb | MB | 21 | 365.494 | 2.398 | 398.367 | 397.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26400) main thread run-queue wait | percent | 20 | 1.019 | 0.001 | 10.677 | 0.001 | 0.206264 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26400) vms_mb | MB | 21 | 9316.352 | 165.203 | 10208.125 | 10207.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26429) CPU | percent | 1 | 83.298 | 83.298 | 83.298 | 83.298 | 0.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26429) rss_mb | MB | 2 | 230.062 | 158.602 | 301.523 | 301.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26429) main thread run-queue wait | percent | 1 | 8.742 | 8.742 | 8.742 | 8.742 | 0.088157 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26429) vms_mb | MB | 2 | 1613.146 | 1499.969 | 1726.324 | 1726.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26453) CPU | percent | 11 | 20.320 | 2.983 | 73.559 | 3.979 | 2.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26453) rss_mb | MB | 12 | 373.993 | 294.992 | 395.789 | 395.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26453) main thread run-queue wait | percent | 11 | 4.022 | 0.003 | 20.642 | 0.006 | 0.445901 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26453) vms_mb | MB | 12 | 9486.028 | 1690.008 | 10212.090 | 10212.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26475) CPU | percent | 1 | 58.619 | 58.619 | 58.619 | 58.619 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26475) rss_mb | MB | 2 | 200.805 | 148.594 | 253.016 | 253.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26475) main thread run-queue wait | percent | 1 | 17.533 | 17.533 | 17.533 | 17.533 | 0.176473 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26475) vms_mb | MB | 2 | 1541.783 | 1434.469 | 1649.098 | 1649.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26487) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26487) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26488) rss_mb | MB | 1 | 5.477 | 5.477 | 5.477 | 5.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26488) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26503) CPU | percent | 12 | 24.984 | 0.995 | 87.362 | 8.943 | 3.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26503) rss_mb | MB | 13 | 357.576 | 160.480 | 392.484 | 392.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26503) main thread run-queue wait | percent | 12 | 2.499 | 0.005 | 19.601 | 0.019 | 0.307768 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26503) vms_mb | MB | 13 | 8865.795 | 1316.836 | 10210.695 | 10210.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26522) CPU | percent | 1 | 65.182 | 65.182 | 65.182 | 65.182 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26522) rss_mb | MB | 2 | 226.861 | 174.723 | 279.000 | 279.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26522) main thread run-queue wait | percent | 1 | 17.145 | 17.145 | 17.145 | 17.145 | 0.173605 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26522) vms_mb | MB | 2 | 1631.760 | 1589.973 | 1673.547 | 1673.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 26548) rss_mb | MB | 1 | 60.723 | 60.723 | 60.723 | 60.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 26548) vms_mb | MB | 1 | 903.531 | 903.531 | 903.531 | 903.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26551) CPU | percent | 15 | 20.586 | 0.995 | 83.378 | 0.995 | 3.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26551) rss_mb | MB | 16 | 371.696 | 212.848 | 394.430 | 393.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26551) main thread run-queue wait | percent | 15 | 1.018 | 0.003 | 4.851 | 0.006 | 0.153709 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26551) vms_mb | MB | 16 | 9145.223 | 1622.562 | 10216.316 | 10215.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26581) rss_mb | MB | 1 | 272.277 | 272.277 | 272.277 | 272.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26581) vms_mb | MB | 1 | 1667.309 | 1667.309 | 1667.309 | 1667.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26603) CPU | percent | 17 | 18.503 | 0.995 | 89.458 | 6.962 | 3.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26603) rss_mb | MB | 18 | 363.649 | 58.156 | 399.957 | 399.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26603) main thread run-queue wait | percent | 17 | 2.243 | 0.003 | 17.636 | 0.028 | 0.384048 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26603) vms_mb | MB | 18 | 9226.905 | 1238.512 | 10214.000 | 10213.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26622) CPU | percent | 1 | 65.519 | 65.519 | 65.519 | 65.519 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26622) rss_mb | MB | 2 | 240.926 | 193.703 | 288.148 | 288.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26622) main thread run-queue wait | percent | 1 | 19.314 | 19.314 | 19.314 | 19.314 | 0.194562 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26622) vms_mb | MB | 2 | 1648.766 | 1614.473 | 1683.059 | 1683.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26630) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26630) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26631) rss_mb | MB | 1 | 7.676 | 7.676 | 7.676 | 7.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 26631) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26671) CPU | percent | 20 | 16.244 | 0.993 | 70.490 | 9.946 | 3.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26671) rss_mb | MB | 21 | 377.084 | 199.875 | 396.449 | 395.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26671) main thread run-queue wait | percent | 20 | 1.680 | 0.001 | 14.786 | 0.015 | 0.346975 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26671) vms_mb | MB | 21 | 9393.178 | 1617.762 | 10211.723 | 10210.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26691) CPU | percent | 1 | 67.996 | 67.996 | 67.996 | 67.996 | 0.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26691) rss_mb | MB | 2 | 237.566 | 188.566 | 286.566 | 286.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26691) main thread run-queue wait | percent | 1 | 14.812 | 14.812 | 14.812 | 14.812 | 0.150307 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26691) vms_mb | MB | 2 | 1637.625 | 1593.973 | 1681.277 | 1681.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26724) CPU | percent | 17 | 17.641 | 0.995 | 75.424 | 1.986 | 3.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26724) rss_mb | MB | 18 | 374.015 | 218.512 | 394.992 | 394.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26724) main thread run-queue wait | percent | 17 | 1.016 | 0.001 | 11.071 | 0.010 | 0.173931 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26724) vms_mb | MB | 18 | 9256.937 | 1623.543 | 10208.852 | 10208.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26755) rss_mb | MB | 1 | 166.711 | 166.711 | 166.711 | 166.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26755) vms_mb | MB | 1 | 1577.723 | 1577.723 | 1577.723 | 1577.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26775) CPU | percent | 142 | 5.813 | 0.981 | 86.325 | 7.959 | 8.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26775) rss_mb | MB | 143 | 395.870 | 150.570 | 419.277 | 395.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26775) main thread run-queue wait | percent | 142 | 0.828 | 0.001 | 17.859 | 0.013 | 1.184015 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26775) vms_mb | MB | 143 | 10085.577 | 1434.465 | 10219.336 | 10198.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26798) rss_mb | MB | 1 | 208.402 | 208.402 | 208.402 | 208.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 26798) vms_mb | MB | 1 | 1619.977 | 1619.977 | 1619.977 | 1619.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26826) rss_mb | MB | 1 | 2.863 | 2.863 | 2.863 | 2.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26826) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26827) rss_mb | MB | 1 | 34.012 | 34.012 | 34.012 | 34.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26827) vms_mb | MB | 1 | 226.105 | 226.105 | 226.105 | 226.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26854) rss_mb | MB | 1 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26854) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26855) rss_mb | MB | 1 | 46.215 | 46.215 | 46.215 | 46.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26855) vms_mb | MB | 1 | 267.531 | 267.531 | 267.531 | 267.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26956) rss_mb | MB | 1 | 2.707 | 2.707 | 2.707 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26956) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26957) rss_mb | MB | 1 | 13.336 | 13.336 | 13.336 | 13.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26957) vms_mb | MB | 1 | 207.258 | 207.258 | 207.258 | 207.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26969) rss_mb | MB | 1 | 2.875 | 2.875 | 2.875 | 2.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 26969) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26970) rss_mb | MB | 1 | 13.289 | 13.289 | 13.289 | 13.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 26970) vms_mb | MB | 1 | 207.137 | 207.137 | 207.137 | 207.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26980) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26980) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 26981) rss_mb | MB | 1 | 15.688 | 15.688 | 15.688 | 15.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 26981) vms_mb | MB | 1 | 20.711 | 20.711 | 20.711 | 20.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26992) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 26992) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 26993) rss_mb | MB | 1 | 9.160 | 9.160 | 9.160 | 9.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 26993) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27025) rss_mb | MB | 1 | 1.398 | 1.398 | 1.398 | 1.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27025) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27026) rss_mb | MB | 1 | 6.785 | 6.785 | 6.785 | 6.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27026) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27042) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27042) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27043) rss_mb | MB | 1 | 10.254 | 10.254 | 10.254 | 10.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27043) vms_mb | MB | 1 | 15.270 | 15.270 | 15.270 | 15.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27047) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27047) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27048) rss_mb | MB | 1 | 16.480 | 16.480 | 16.480 | 16.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27048) vms_mb | MB | 1 | 21.844 | 21.844 | 21.844 | 21.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27056) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27056) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27057) rss_mb | MB | 1 | 14.551 | 14.551 | 14.551 | 14.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27057) vms_mb | MB | 1 | 20.082 | 20.082 | 20.082 | 20.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27064) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27064) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27065) rss_mb | MB | 1 | 9.422 | 9.422 | 9.422 | 9.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27065) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27073) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27073) rss_mb | MB | 3 | 2.641 | 2.641 | 2.641 | 2.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27073) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27073) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27074) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27074) rss_mb | MB | 3 | 10.898 | 10.898 | 10.898 | 10.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27074) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27074) vms_mb | MB | 3 | 14.891 | 14.891 | 14.891 | 14.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27075) CPU | percent | 2 | 35.168 | 0.993 | 69.343 | 0.993 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27075) rss_mb | MB | 3 | 53.947 | 30.855 | 65.746 | 65.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27075) main thread run-queue wait | percent | 2 | 0.088 | 0.054 | 0.122 | 0.054 | 0.001775 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27075) vms_mb | MB | 3 | 66.609 | 40.000 | 80.191 | 80.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27076) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27076) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27077) rss_mb | MB | 1 | 7.676 | 7.676 | 7.676 | 7.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27077) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27087) CPU | percent | 36 | 9.903 | 0.983 | 74.495 | 4.974 | 3.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27087) rss_mb | MB | 37 | 385.599 | 229.043 | 397.895 | 397.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27087) main thread run-queue wait | percent | 36 | 1.345 | 0.002 | 22.415 | 0.011 | 0.487676 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27087) vms_mb | MB | 37 | 9749.580 | 1631.785 | 10215.387 | 10214.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 27102) rss_mb | MB | 1 | 2.609 | 2.609 | 2.609 | 2.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 27102) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 27103) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 27103) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27110) CPU | percent | 1 | 48.604 | 48.604 | 48.604 | 48.604 | 0.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27110) rss_mb | MB | 2 | 204.137 | 166.570 | 241.703 | 241.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27110) main thread run-queue wait | percent | 1 | 17.658 | 17.658 | 17.658 | 17.658 | 0.178018 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27110) vms_mb | MB | 2 | 1608.789 | 1577.723 | 1639.855 | 1639.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27133) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27133) rss_mb | MB | 3 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27133) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27133) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27134) CPU | percent | 2 | 29.802 | 0.000 | 59.605 | 0.000 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27134) rss_mb | MB | 3 | 36.874 | 10.293 | 50.164 | 50.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27134) main thread run-queue wait | percent | 2 | 4.605 | 0.000 | 9.211 | 0.000 | 0.092719 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27134) vms_mb | MB | 3 | 185.737 | 14.719 | 271.246 | 271.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27138) CPU | percent | 1 | 41.736 | 41.736 | 41.736 | 41.736 | 0.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27138) rss_mb | MB | 2 | 53.047 | 40.203 | 65.891 | 65.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27138) main thread run-queue wait | percent | 1 | 0.128 | 0.128 | 0.128 | 0.128 | 0.001293 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27138) vms_mb | MB | 2 | 64.072 | 48.047 | 80.098 | 80.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27147) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27147) rss_mb | MB | 4 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27147) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27147) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27148) CPU | percent | 3 | 0.661 | 0.000 | 1.984 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27148) rss_mb | MB | 4 | 10.207 | 8.109 | 10.906 | 10.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27148) main thread run-queue wait | percent | 3 | 0.002 | 0.000 | 0.005 | 0.000 | 0.000049 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27148) vms_mb | MB | 4 | 14.452 | 13.020 | 14.930 | 14.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27149) CPU | percent | 2 | 6.447 | 0.000 | 12.894 | 0.000 | 0.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27149) rss_mb | MB | 3 | 63.767 | 59.691 | 65.805 | 65.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27149) main thread run-queue wait | percent | 2 | 0.077 | 0.000 | 0.154 | 0.000 | 0.001554 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27149) vms_mb | MB | 3 | 78.217 | 74.316 | 80.168 | 80.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27156) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27156) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27157) rss_mb | MB | 1 | 9.297 | 9.297 | 9.297 | 9.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27157) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27158) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27158) rss_mb | MB | 2 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27158) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27158) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27159) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27159) rss_mb | MB | 2 | 11.191 | 11.191 | 11.191 | 11.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27159) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27159) vms_mb | MB | 2 | 14.926 | 14.926 | 14.926 | 14.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27160) CPU | percent | 1 | 21.806 | 21.806 | 21.806 | 21.806 | 0.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27160) rss_mb | MB | 2 | 56.191 | 47.324 | 65.059 | 65.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27160) main thread run-queue wait | percent | 1 | 0.192 | 0.192 | 0.192 | 0.192 | 0.001938 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27160) vms_mb | MB | 2 | 68.061 | 56.020 | 80.102 | 80.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27162) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27162) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27163) rss_mb | MB | 1 | 21.465 | 21.465 | 21.465 | 21.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27163) vms_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27174) CPU | percent | 17 | 15.252 | 0.995 | 74.593 | 1.989 | 2.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27174) rss_mb | MB | 18 | 380.801 | 278.801 | 395.969 | 395.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27174) main thread run-queue wait | percent | 17 | 1.622 | 0.004 | 10.940 | 0.005 | 0.277720 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27174) vms_mb | MB | 18 | 9724.527 | 1674.562 | 10210.137 | 10210.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27202) CPU | percent | 1 | 67.444 | 67.444 | 67.444 | 67.444 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27202) rss_mb | MB | 2 | 220.838 | 153.645 | 288.031 | 288.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27202) main thread run-queue wait | percent | 1 | 17.324 | 17.324 | 17.324 | 17.324 | 0.174668 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27202) vms_mb | MB | 2 | 1591.146 | 1499.219 | 1683.074 | 1683.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27218) rss_mb | MB | 1 | 2.770 | 2.770 | 2.770 | 2.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27218) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27219) rss_mb | MB | 1 | 23.180 | 23.180 | 23.180 | 23.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27219) vms_mb | MB | 1 | 215.605 | 215.605 | 215.605 | 215.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27233) CPU | percent | 31 | 12.908 | 0.994 | 84.514 | 9.943 | 4.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27233) rss_mb | MB | 32 | 376.768 | 44.594 | 403.812 | 403.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27233) main thread run-queue wait | percent | 31 | 1.066 | 0.002 | 10.679 | 0.037 | 0.333076 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27233) vms_mb | MB | 32 | 9659.527 | 1174.262 | 10213.449 | 10213.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 27253) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git workspace (PID 27253) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27262) rss_mb | MB | 1 | 278.012 | 278.012 | 278.012 | 278.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27262) vms_mb | MB | 1 | 1672.809 | 1672.809 | 1672.809 | 1672.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27278) CPU | percent | 1 | 25.766 | 25.766 | 25.766 | 25.766 | 0.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27278) rss_mb | MB | 2 | 19.371 | 2.711 | 36.031 | 36.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27278) main thread run-queue wait | percent | 1 | 0.031 | 0.031 | 0.031 | 0.031 | 0.000309 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27278) vms_mb | MB | 2 | 24.160 | 3.848 | 44.473 | 44.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27283) rss_mb | MB | 1 | 14.441 | 14.441 | 14.441 | 14.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27283) vms_mb | MB | 1 | 1874.160 | 1874.160 | 1874.160 | 1874.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27287) rss_mb | MB | 1 | 1.285 | 1.285 | 1.285 | 1.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27287) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27288) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27288) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27292) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27292) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27293) rss_mb | MB | 1 | 20.898 | 20.898 | 20.898 | 20.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27293) vms_mb | MB | 1 | 25.449 | 25.449 | 25.449 | 25.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27310) CPU | percent | 7 | 39.881 | 6.962 | 69.590 | 13.925 | 2.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27310) rss_mb | MB | 8 | 347.722 | 211.387 | 386.855 | 386.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27310) main thread run-queue wait | percent | 7 | 3.699 | 0.026 | 12.225 | 0.026 | 0.261064 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27310) vms_mb | MB | 8 | 8055.031 | 1621.777 | 10195.707 | 10195.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27336) rss_mb | MB | 1 | 203.816 | 203.816 | 203.816 | 203.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27336) vms_mb | MB | 1 | 1618.480 | 1618.480 | 1618.480 | 1618.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27360) CPU | percent | 53 | 8.711 | 0.993 | 68.618 | 1.987 | 4.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27360) rss_mb | MB | 54 | 390.921 | 206.082 | 402.188 | 402.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27360) main thread run-queue wait | percent | 53 | 0.900 | 0.002 | 8.180 | 0.004 | 0.480706 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27360) vms_mb | MB | 54 | 9895.130 | 1619.238 | 10215.602 | 10215.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27381) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27381) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27382) rss_mb | MB | 1 | 7.367 | 7.367 | 7.367 | 7.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27382) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27388) rss_mb | MB | 1 | 160.727 | 160.727 | 160.727 | 160.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27388) vms_mb | MB | 1 | 1500.469 | 1500.469 | 1500.469 | 1500.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27414) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27414) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27415) rss_mb | MB | 1 | 7.070 | 7.070 | 7.070 | 7.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27415) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27446) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27446) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27447) rss_mb | MB | 1 | 18.035 | 18.035 | 18.035 | 18.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27447) vms_mb | MB | 1 | 24.184 | 24.184 | 24.184 | 24.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27465) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27465) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27466) rss_mb | MB | 1 | 10.625 | 10.625 | 10.625 | 10.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27466) vms_mb | MB | 1 | 15.297 | 15.297 | 15.297 | 15.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27481) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27481) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27482) rss_mb | MB | 1 | 21.535 | 21.535 | 21.535 | 21.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27482) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27505) CPU | percent | 19 | 16.397 | 1.987 | 81.494 | 5.968 | 3.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27505) rss_mb | MB | 20 | 369.869 | 145.105 | 395.668 | 395.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27505) main thread run-queue wait | percent | 19 | 0.811 | 0.001 | 6.333 | 0.012 | 0.155878 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27505) vms_mb | MB | 20 | 9310.035 | 1301.289 | 10186.246 | 10186.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27522) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27522) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27523) rss_mb | MB | 1 | 10.777 | 10.777 | 10.777 | 10.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27523) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27526) CPU | percent | 1 | 68.798 | 68.798 | 68.798 | 68.798 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27526) rss_mb | MB | 2 | 238.516 | 180.355 | 296.676 | 296.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27526) main thread run-queue wait | percent | 1 | 11.807 | 11.807 | 11.807 | 11.807 | 0.121844 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27526) vms_mb | MB | 2 | 1641.350 | 1591.473 | 1691.227 | 1691.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27536) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27536) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27537) rss_mb | MB | 1 | 8.695 | 8.695 | 8.695 | 8.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27537) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27549) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27549) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27550) rss_mb | MB | 1 | 10.555 | 10.555 | 10.555 | 10.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27550) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27554) CPU | percent | 21 | 16.844 | 1.986 | 75.380 | 4.973 | 3.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27554) rss_mb | MB | 22 | 373.938 | 185.969 | 393.832 | 393.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27554) main thread run-queue wait | percent | 21 | 0.766 | 0.005 | 7.338 | 0.009 | 0.162887 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27554) vms_mb | MB | 22 | 9432.317 | 1593.219 | 10213.816 | 10213.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27583) CPU | percent | 1 | 84.384 | 84.384 | 84.384 | 84.384 | 0.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27583) rss_mb | MB | 2 | 224.385 | 156.715 | 292.055 | 292.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27583) main thread run-queue wait | percent | 1 | 5.740 | 5.740 | 5.740 | 5.740 | 0.057818 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27583) vms_mb | MB | 2 | 1499.672 | 1312.633 | 1686.711 | 1686.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27610) CPU | percent | 6 | 41.383 | 3.978 | 71.485 | 3.978 | 2.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27610) rss_mb | MB | 7 | 355.387 | 262.566 | 385.332 | 385.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27610) main thread run-queue wait | percent | 6 | 5.634 | 0.017 | 18.531 | 0.017 | 0.340554 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27610) vms_mb | MB | 7 | 8952.373 | 1658.559 | 10214.270 | 10214.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27628) CPU | percent | 1 | 64.459 | 64.459 | 64.459 | 64.459 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27628) rss_mb | MB | 2 | 221.711 | 171.598 | 271.824 | 271.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27628) main thread run-queue wait | percent | 1 | 15.354 | 15.354 | 15.354 | 15.354 | 0.154825 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27628) vms_mb | MB | 2 | 1623.262 | 1579.723 | 1666.801 | 1666.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27657) CPU | percent | 19 | 19.098 | 0.995 | 85.354 | 1.989 | 3.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27657) rss_mb | MB | 20 | 370.818 | 136.023 | 395.227 | 394.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27657) main thread run-queue wait | percent | 19 | 6.528 | 0.001 | 39.536 | 0.011 | 1.255142 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27657) vms_mb | MB | 20 | 9333.569 | 1296.254 | 10214.906 | 10214.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27679) CPU | percent | 1 | 56.760 | 56.760 | 56.760 | 56.760 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27679) rss_mb | MB | 2 | 232.367 | 187.164 | 277.570 | 277.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27679) main thread run-queue wait | percent | 1 | 19.000 | 19.000 | 19.000 | 19.000 | 0.197500 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27679) vms_mb | MB | 2 | 1634.023 | 1594.473 | 1673.574 | 1673.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27689) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27689) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27690) rss_mb | MB | 1 | 9.867 | 9.867 | 9.867 | 9.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27690) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 27700) CPU | percent | 2 | 127.109 | 104.323 | 149.894 | 149.894 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 27700) rss_mb | MB | 3 | 1614.303 | 19.742 | 2785.039 | 2038.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 27700) main thread run-queue wait | percent | 2 | 15.618 | 1.623 | 29.613 | 29.613 | 0.314650 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 27700) vms_mb | MB | 3 | 1877.051 | 211.711 | 3160.988 | 2258.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27706) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27706) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27708) rss_mb | MB | 1 | 7.254 | 7.254 | 7.254 | 7.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27708) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27793) CPU | percent | 8 | 36.304 | 3.977 | 87.476 | 14.917 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27793) rss_mb | MB | 9 | 340.978 | 122.520 | 396.844 | 396.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27793) main thread run-queue wait | percent | 8 | 2.156 | 0.008 | 6.864 | 0.030 | 0.174806 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27793) vms_mb | MB | 9 | 8250.877 | 1296.254 | 10207.188 | 10207.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27817) CPU | percent | 1 | 66.309 | 66.309 | 66.309 | 66.309 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27817) rss_mb | MB | 2 | 248.348 | 193.902 | 302.793 | 302.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27817) main thread run-queue wait | percent | 1 | 4.078 | 4.078 | 4.078 | 4.078 | 0.041202 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27817) vms_mb | MB | 2 | 1670.289 | 1614.223 | 1726.355 | 1726.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27827) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27827) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27828) rss_mb | MB | 1 | 9.863 | 9.863 | 9.863 | 9.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27828) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27841) CPU | percent | 13 | 25.795 | 1.987 | 76.477 | 1.987 | 3.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27841) rss_mb | MB | 14 | 366.327 | 174.906 | 396.234 | 396.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27841) main thread run-queue wait | percent | 13 | 2.008 | 0.004 | 9.862 | 0.005 | 0.263720 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27841) vms_mb | MB | 14 | 8981.846 | 1581.719 | 10214.438 | 10214.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27865) rss_mb | MB | 1 | 208.273 | 208.273 | 208.273 | 208.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27865) vms_mb | MB | 1 | 1619.488 | 1619.488 | 1619.488 | 1619.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27886) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27886) rss_mb | MB | 2 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27886) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 27886) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27887) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27887) rss_mb | MB | 2 | 10.930 | 10.930 | 10.930 | 10.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27887) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 27887) vms_mb | MB | 2 | 14.895 | 14.895 | 14.895 | 14.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27888) CPU | percent | 1 | 61.479 | 61.479 | 61.479 | 61.479 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27888) rss_mb | MB | 2 | 49.250 | 33.465 | 65.035 | 65.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27888) main thread run-queue wait | percent | 1 | 0.312 | 0.312 | 0.312 | 0.312 | 0.003143 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 27888) vms_mb | MB | 2 | 61.426 | 42.746 | 80.105 | 80.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27891) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27891) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27892) rss_mb | MB | 1 | 7.070 | 7.070 | 7.070 | 7.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 27892) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27902) CPU | percent | 12 | 27.966 | 1.988 | 91.417 | 5.967 | 3.390000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27902) rss_mb | MB | 13 | 353.127 | 87.500 | 390.809 | 390.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27902) main thread run-queue wait | percent | 12 | 1.669 | 0.001 | 12.043 | 0.050 | 0.201993 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27902) vms_mb | MB | 13 | 8858.251 | 1283.598 | 10212.164 | 10212.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27931) rss_mb | MB | 1 | 188.758 | 188.758 | 188.758 | 188.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27931) vms_mb | MB | 1 | 1594.223 | 1594.223 | 1594.223 | 1594.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27945) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 27945) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27946) rss_mb | MB | 1 | 10.668 | 10.668 | 10.668 | 10.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 27946) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27950) CPU | percent | 9 | 32.343 | 1.989 | 79.462 | 8.954 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27950) rss_mb | MB | 10 | 352.190 | 181.070 | 394.949 | 394.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27950) main thread run-queue wait | percent | 9 | 1.862 | 0.005 | 7.478 | 0.018 | 0.168746 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27950) vms_mb | MB | 10 | 8493.094 | 1591.469 | 10213.867 | 10213.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27985) CPU | percent | 11 | 23.838 | 0.993 | 70.484 | 1.988 | 2.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27985) rss_mb | MB | 12 | 363.088 | 228.812 | 388.727 | 388.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27985) main thread run-queue wait | percent | 11 | 1.757 | 0.002 | 13.560 | 0.007 | 0.194624 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 27985) vms_mb | MB | 12 | 8783.841 | 1632.270 | 10212.223 | 10212.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28018) CPU | percent | 15 | 20.197 | 0.995 | 91.224 | 1.989 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28018) rss_mb | MB | 16 | 366.865 | 158.766 | 395.746 | 395.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28018) main thread run-queue wait | percent | 15 | 0.764 | 0.001 | 6.626 | 0.007 | 0.115407 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28018) vms_mb | MB | 16 | 9081.695 | 1315.172 | 10196.875 | 10166.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28055) CPU | percent | 6 | 39.386 | 2.984 | 83.534 | 2.984 | 2.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28055) rss_mb | MB | 7 | 351.507 | 261.359 | 380.754 | 380.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28055) main thread run-queue wait | percent | 6 | 2.219 | 0.011 | 5.456 | 0.011 | 0.134126 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28055) vms_mb | MB | 7 | 8954.438 | 1657.008 | 10207.875 | 10207.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28073) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28073) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28074) rss_mb | MB | 1 | 7.621 | 7.621 | 7.621 | 7.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28074) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28084) rss_mb | MB | 1 | 207.320 | 207.320 | 207.320 | 207.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28084) vms_mb | MB | 1 | 1619.215 | 1619.215 | 1619.215 | 1619.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28101) CPU | percent | 13 | 25.688 | 1.989 | 76.470 | 1.989 | 3.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28101) rss_mb | MB | 14 | 360.467 | 169.293 | 396.957 | 396.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28101) main thread run-queue wait | percent | 13 | 3.920 | 0.006 | 20.453 | 0.012 | 0.513721 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28101) vms_mb | MB | 14 | 8973.362 | 1578.719 | 10215.008 | 10214.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28118) CPU | percent | 1 | 64.472 | 64.472 | 64.472 | 64.472 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28118) rss_mb | MB | 2 | 243.988 | 197.844 | 290.133 | 290.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28118) main thread run-queue wait | percent | 1 | 20.349 | 20.349 | 20.349 | 20.349 | 0.205157 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28118) vms_mb | MB | 2 | 1651.273 | 1617.480 | 1685.066 | 1685.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28157) CPU | percent | 19 | 19.498 | 1.986 | 85.458 | 7.946 | 3.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28157) rss_mb | MB | 20 | 368.053 | 97.586 | 397.273 | 396.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28157) main thread run-queue wait | percent | 19 | 2.626 | 0.003 | 23.874 | 0.022 | 0.502451 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28157) vms_mb | MB | 20 | 9326.457 | 1283.598 | 10210.789 | 10210.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28174) CPU | percent | 1 | 59.621 | 59.621 | 59.621 | 59.621 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28174) rss_mb | MB | 2 | 208.842 | 158.086 | 259.598 | 259.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28174) main thread run-queue wait | percent | 1 | 16.006 | 16.006 | 16.006 | 16.006 | 0.161081 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28174) vms_mb | MB | 2 | 1577.658 | 1499.969 | 1655.348 | 1655.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28199) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28199) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 28200) rss_mb | MB | 1 | 21.523 | 21.523 | 21.523 | 21.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 28200) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28206) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28206) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 28207) rss_mb | MB | 1 | 8.672 | 8.672 | 8.672 | 8.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 28207) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28218) CPU | percent | 6 | 45.682 | 2.984 | 74.382 | 2.984 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28218) rss_mb | MB | 7 | 339.196 | 194.383 | 389.398 | 389.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28218) main thread run-queue wait | percent | 6 | 6.235 | 0.007 | 15.139 | 0.007 | 0.376517 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28218) vms_mb | MB | 7 | 7759.444 | 1614.469 | 10207.949 | 10207.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28240) CPU | percent | 1 | 40.744 | 40.744 | 40.744 | 40.744 | 0.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28240) rss_mb | MB | 2 | 187.795 | 146.715 | 228.875 | 228.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28240) main thread run-queue wait | percent | 1 | 10.604 | 10.604 | 10.604 | 10.604 | 0.106711 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28240) vms_mb | MB | 2 | 1467.604 | 1302.984 | 1632.223 | 1632.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28266) CPU | percent | 6 | 50.146 | 7.953 | 86.441 | 7.953 | 3.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28266) rss_mb | MB | 7 | 325.636 | 159.961 | 380.387 | 380.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28266) main thread run-queue wait | percent | 6 | 7.346 | 0.026 | 14.020 | 0.026 | 0.444039 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28266) vms_mb | MB | 7 | 7694.243 | 1315.965 | 10203.969 | 10203.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28284) CPU | percent | 1 | 65.405 | 65.405 | 65.405 | 65.405 | 0.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28284) rss_mb | MB | 2 | 234.113 | 188.938 | 279.289 | 279.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28284) main thread run-queue wait | percent | 1 | 19.163 | 19.163 | 19.163 | 19.163 | 0.193373 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28284) vms_mb | MB | 2 | 1634.271 | 1594.223 | 1674.320 | 1674.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28296) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28296) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28297) rss_mb | MB | 1 | 7.383 | 7.383 | 7.383 | 7.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28297) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28314) CPU | percent | 7 | 38.966 | 3.979 | 65.434 | 7.957 | 2.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28314) rss_mb | MB | 8 | 350.937 | 230.070 | 387.527 | 387.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28314) main thread run-queue wait | percent | 7 | 6.004 | 0.010 | 20.554 | 0.016 | 0.423913 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28314) vms_mb | MB | 8 | 8063.107 | 1633.059 | 10207.598 | 10207.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28332) CPU | percent | 2 | 57.514 | 56.531 | 58.497 | 56.531 | 1.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28332) rss_mb | MB | 3 | 204.676 | 81.082 | 303.801 | 303.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28332) main thread run-queue wait | percent | 2 | 19.019 | 14.000 | 24.038 | 14.000 | 0.383607 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28332) vms_mb | MB | 3 | 1547.725 | 1283.695 | 1727.867 | 1727.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28350) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28350) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28351) rss_mb | MB | 1 | 7.145 | 7.145 | 7.145 | 7.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28351) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28355) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28355) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28356) rss_mb | MB | 1 | 9.824 | 9.824 | 9.824 | 9.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28356) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28360) CPU | percent | 7 | 35.678 | 1.989 | 63.670 | 1.989 | 2.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28360) rss_mb | MB | 8 | 347.529 | 228.992 | 382.039 | 382.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28360) main thread run-queue wait | percent | 7 | 4.986 | 0.008 | 13.717 | 0.008 | 0.352963 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28360) vms_mb | MB | 8 | 8062.255 | 1632.289 | 10208.422 | 10208.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28377) CPU | percent | 1 | 56.499 | 56.499 | 56.499 | 56.499 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28377) rss_mb | MB | 2 | 199.955 | 158.609 | 241.301 | 241.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28377) main thread run-queue wait | percent | 1 | 22.056 | 22.056 | 22.056 | 22.056 | 0.222515 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28377) vms_mb | MB | 2 | 1477.324 | 1315.809 | 1638.840 | 1638.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28405) CPU | percent | 9 | 33.757 | 2.979 | 87.345 | 2.984 | 3.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28405) rss_mb | MB | 10 | 338.684 | 67.156 | 392.496 | 392.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28405) main thread run-queue wait | percent | 9 | 1.441 | 0.004 | 5.504 | 0.004 | 0.130671 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28405) vms_mb | MB | 10 | 8444.482 | 1238.512 | 10208.016 | 10208.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28433) CPU | percent | 1 | 81.324 | 81.324 | 81.324 | 81.324 | 0.820000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28433) rss_mb | MB | 2 | 164.250 | 50.648 | 277.852 | 277.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28433) main thread run-queue wait | percent | 1 | 14.541 | 14.541 | 14.541 | 14.541 | 0.146615 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28433) vms_mb | MB | 2 | 1455.705 | 1238.609 | 1672.801 | 1672.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28471) CPU | percent | 43 | 10.072 | 0.993 | 90.304 | 2.983 | 4.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28471) rss_mb | MB | 44 | 385.841 | 52.699 | 402.156 | 401.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28471) main thread run-queue wait | percent | 43 | 1.471 | 0.002 | 24.226 | 0.012 | 0.637008 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28471) vms_mb | MB | 44 | 9811.845 | 1238.512 | 10215.590 | 10214.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28500) CPU | percent | 1 | 77.513 | 77.513 | 77.513 | 77.513 | 0.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28500) rss_mb | MB | 2 | 217.383 | 140.016 | 294.750 | 294.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28500) main thread run-queue wait | percent | 1 | 14.059 | 14.059 | 14.059 | 14.059 | 0.141474 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28500) vms_mb | MB | 2 | 1492.770 | 1296.352 | 1689.188 | 1689.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 28543) CPU | percent | 3 | 135.767 | 108.419 | 172.706 | 108.419 | 4.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 28543) rss_mb | MB | 4 | 2063.058 | 421.750 | 3752.871 | 3752.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 28543) main thread run-queue wait | percent | 3 | 28.282 | 8.133 | 60.678 | 16.036 | 0.854403 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 28543) vms_mb | MB | 4 | 2365.196 | 744.273 | 4198.840 | 4198.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28560) CPU | percent | 9 | 34.165 | 0.995 | 84.374 | 0.995 | 3.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28560) rss_mb | MB | 10 | 345.886 | 145.047 | 392.586 | 392.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28560) main thread run-queue wait | percent | 9 | 1.634 | 0.008 | 8.337 | 0.008 | 0.148238 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28560) vms_mb | MB | 10 | 8456.445 | 1301.289 | 10213.621 | 10213.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28591) rss_mb | MB | 1 | 287.375 | 287.375 | 287.375 | 287.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28591) vms_mb | MB | 1 | 1682.098 | 1682.098 | 1682.098 | 1682.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28616) CPU | percent | 13 | 22.531 | 0.994 | 73.501 | 1.989 | 2.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28616) rss_mb | MB | 14 | 371.770 | 244.410 | 396.266 | 395.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28616) main thread run-queue wait | percent | 13 | 0.861 | 0.004 | 4.067 | 0.004 | 0.112766 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28616) vms_mb | MB | 14 | 8992.718 | 1641.059 | 10214.996 | 10214.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28647) rss_mb | MB | 1 | 277.605 | 277.605 | 277.605 | 277.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28647) vms_mb | MB | 1 | 1672.805 | 1672.805 | 1672.805 | 1672.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28663) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28663) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 28664) rss_mb | MB | 1 | 7.520 | 7.520 | 7.520 | 7.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 28664) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28757) CPU | percent | 10 | 32.480 | 1.987 | 69.500 | 1.987 | 3.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28757) rss_mb | MB | 11 | 356.825 | 193.168 | 394.969 | 394.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28757) main thread run-queue wait | percent | 10 | 4.737 | 0.004 | 14.462 | 0.004 | 0.477105 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28757) vms_mb | MB | 11 | 8645.368 | 1606.219 | 10212.945 | 10212.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28776) CPU | percent | 1 | 59.609 | 59.609 | 59.609 | 59.609 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28776) rss_mb | MB | 2 | 256.422 | 216.133 | 296.711 | 296.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28776) main thread run-queue wait | percent | 1 | 14.262 | 14.262 | 14.262 | 14.262 | 0.143552 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28776) vms_mb | MB | 2 | 1673.119 | 1622.988 | 1723.250 | 1723.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28784) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28784) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28785) rss_mb | MB | 1 | 9.750 | 9.750 | 9.750 | 9.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28785) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28814) CPU | percent | 14 | 18.155 | 0.990 | 77.570 | 1.975 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28814) rss_mb | MB | 15 | 377.803 | 242.840 | 402.844 | 402.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28814) main thread run-queue wait | percent | 14 | 5.051 | 0.005 | 27.897 | 0.007 | 0.713638 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28814) vms_mb | MB | 15 | 9065.206 | 1639.531 | 10206.395 | 10206.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28833) CPU | percent | 1 | 61.389 | 61.389 | 61.389 | 61.389 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28833) rss_mb | MB | 2 | 254.039 | 211.457 | 296.621 | 296.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28833) main thread run-queue wait | percent | 1 | 17.501 | 17.501 | 17.501 | 17.501 | 0.176753 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28833) vms_mb | MB | 2 | 1656.846 | 1622.723 | 1690.969 | 1690.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28843) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28843) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28844) rss_mb | MB | 1 | 9.289 | 9.289 | 9.289 | 9.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 28844) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 28858) CPU | percent | 2 | 152.097 | 129.960 | 174.234 | 174.234 | 3.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 28858) rss_mb | MB | 3 | 70.704 | 14.781 | 99.777 | 99.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 28858) main thread run-queue wait | percent | 2 | 36.062 | 26.311 | 45.813 | 45.813 | 0.727992 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 28858) vms_mb | MB | 3 | 282.214 | 208.914 | 318.863 | 318.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28872) CPU | percent | 10 | 27.700 | 1.989 | 77.380 | 2.984 | 2.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28872) rss_mb | MB | 11 | 350.691 | 166.836 | 388.328 | 388.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28872) main thread run-queue wait | percent | 10 | 1.985 | 0.004 | 11.014 | 0.008 | 0.200223 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28872) vms_mb | MB | 11 | 8644.735 | 1577.969 | 10208.172 | 10208.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28900) CPU | percent | 1 | 86.481 | 86.481 | 86.481 | 86.481 | 0.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28900) rss_mb | MB | 2 | 191.293 | 86.938 | 295.648 | 295.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28900) main thread run-queue wait | percent | 1 | 8.237 | 8.237 | 8.237 | 8.237 | 0.082867 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28900) vms_mb | MB | 2 | 1487.137 | 1283.695 | 1690.578 | 1690.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28917) CPU | percent | 21 | 13.527 | 0.994 | 80.441 | 1.990 | 2.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28917) rss_mb | MB | 22 | 378.792 | 236.137 | 393.664 | 393.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28917) main thread run-queue wait | percent | 21 | 1.718 | 0.002 | 23.587 | 0.008 | 0.363420 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28917) vms_mb | MB | 22 | 9433.983 | 1636.766 | 10213.480 | 10212.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28937) CPU | percent | 1 | 54.560 | 54.560 | 54.560 | 54.560 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28937) rss_mb | MB | 2 | 256.113 | 217.488 | 294.738 | 294.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28937) main thread run-queue wait | percent | 1 | 24.414 | 24.414 | 24.414 | 24.414 | 0.246104 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28937) vms_mb | MB | 2 | 1656.729 | 1623.730 | 1689.727 | 1689.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28962) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 28962) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 28963) rss_mb | MB | 1 | 14.492 | 14.492 | 14.492 | 14.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 28963) vms_mb | MB | 1 | 19.902 | 19.902 | 19.902 | 19.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28974) CPU | percent | 20 | 13.212 | 0.994 | 77.574 | 1.989 | 2.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28974) rss_mb | MB | 21 | 384.333 | 278.188 | 398.648 | 397.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28974) main thread run-queue wait | percent | 20 | 2.704 | 0.001 | 17.708 | 0.005 | 0.544605 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 28974) vms_mb | MB | 21 | 9796.425 | 1673.250 | 10214.047 | 10213.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29004) CPU | percent | 1 | 53.539 | 53.539 | 53.539 | 53.539 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29004) rss_mb | MB | 2 | 190.564 | 144.957 | 236.172 | 236.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29004) main thread run-queue wait | percent | 1 | 9.626 | 9.626 | 9.626 | 9.626 | 0.097093 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29004) vms_mb | MB | 2 | 1468.695 | 1301.059 | 1636.332 | 1636.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29020) CPU | percent | 2 | 160.406 | 149.772 | 171.040 | 171.040 | 3.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29020) rss_mb | MB | 3 | 78.967 | 12.160 | 113.359 | 113.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29020) main thread run-queue wait | percent | 2 | 46.390 | 34.099 | 58.681 | 58.681 | 0.933894 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29020) vms_mb | MB | 3 | 239.944 | 56.645 | 331.594 | 331.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29036) CPU | percent | 12 | 21.354 | 0.994 | 71.580 | 2.976 | 2.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29036) rss_mb | MB | 13 | 368.644 | 259.434 | 390.910 | 390.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29036) main thread run-queue wait | percent | 12 | 3.496 | 0.004 | 14.662 | 0.009 | 0.422493 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29036) vms_mb | MB | 13 | 9525.228 | 1655.238 | 10211.621 | 10211.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29056) CPU | percent | 1 | 62.466 | 62.466 | 62.466 | 62.466 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29056) rss_mb | MB | 2 | 219.900 | 169.141 | 270.660 | 270.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29056) main thread run-queue wait | percent | 1 | 8.051 | 8.051 | 8.051 | 8.051 | 0.081195 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29056) vms_mb | MB | 2 | 1622.143 | 1578.723 | 1665.562 | 1665.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29086) CPU | percent | 34 | 12.267 | 0.993 | 87.259 | 7.954 | 4.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29086) rss_mb | MB | 35 | 380.387 | 44.422 | 400.512 | 400.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29086) main thread run-queue wait | percent | 34 | 2.080 | 0.003 | 18.645 | 0.017 | 0.727451 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29086) vms_mb | MB | 35 | 9468.685 | 1174.262 | 10212.508 | 10212.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29104) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29104) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29105) rss_mb | MB | 1 | 8.500 | 8.500 | 8.500 | 8.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29105) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29110) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29110) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29111) rss_mb | MB | 1 | 8.391 | 8.391 | 8.391 | 8.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29111) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29115) rss_mb | MB | 1 | 229.648 | 229.648 | 229.648 | 229.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29115) vms_mb | MB | 1 | 1632.328 | 1632.328 | 1632.328 | 1632.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29141) CPU | percent | 1 | 156.057 | 156.057 | 156.057 | 156.057 | 1.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29141) rss_mb | MB | 2 | 73.650 | 35.609 | 111.691 | 111.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29141) main thread run-queue wait | percent | 1 | 47.142 | 47.142 | 47.142 | 47.142 | 0.474272 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29141) vms_mb | MB | 2 | 295.449 | 259.301 | 331.598 | 331.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29145) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29145) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29146) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29146) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29153) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29153) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29158) CPU | percent | 18 | 20.518 | 0.994 | 86.408 | 1.988 | 3.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29158) rss_mb | MB | 19 | 367.592 | 167.176 | 393.457 | 393.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29158) main thread run-queue wait | percent | 18 | 2.530 | 0.000 | 16.586 | 0.000 | 0.458963 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29158) vms_mb | MB | 19 | 9296.112 | 1578.219 | 10208.945 | 10208.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29176) CPU | percent | 1 | 63.513 | 63.513 | 63.513 | 63.513 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29176) rss_mb | MB | 2 | 229.855 | 187.840 | 271.871 | 271.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29176) main thread run-queue wait | percent | 1 | 16.205 | 16.205 | 16.205 | 16.205 | 0.163294 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29176) vms_mb | MB | 2 | 1630.529 | 1593.973 | 1667.086 | 1667.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 29187) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 29187) vms_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29206) CPU | percent | 7 | 34.467 | 1.990 | 82.486 | 14.920 | 2.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29206) rss_mb | MB | 8 | 360.638 | 277.801 | 394.051 | 394.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29206) main thread run-queue wait | percent | 7 | 2.146 | 0.014 | 12.297 | 0.088 | 0.151771 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29206) vms_mb | MB | 8 | 8094.661 | 1673.207 | 10212.855 | 10212.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29230) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29230) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29231) rss_mb | MB | 1 | 7.117 | 7.117 | 7.117 | 7.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29231) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29235) rss_mb | MB | 1 | 217.848 | 217.848 | 217.848 | 217.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29235) vms_mb | MB | 1 | 1624.008 | 1624.008 | 1624.008 | 1624.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29252) CPU | percent | 8 | 35.988 | 2.981 | 82.340 | 4.972 | 2.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29252) rss_mb | MB | 9 | 346.875 | 171.586 | 390.363 | 390.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29252) main thread run-queue wait | percent | 8 | 2.387 | 0.007 | 6.442 | 0.015 | 0.192299 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29252) vms_mb | MB | 9 | 8292.879 | 1579.469 | 10209.332 | 10209.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29286) CPU | percent | 48 | 7.222 | 0.993 | 71.503 | 0.995 | 3.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29286) rss_mb | MB | 49 | 394.147 | 221.512 | 406.387 | 406.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29286) main thread run-queue wait | percent | 48 | 0.651 | 0.001 | 18.079 | 0.015 | 0.314800 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29286) vms_mb | MB | 49 | 9867.377 | 1624.277 | 10221.453 | 10221.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29322) CPU | percent | 1 | 60.514 | 60.514 | 60.514 | 60.514 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29322) rss_mb | MB | 2 | 250.162 | 205.621 | 294.703 | 294.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29322) main thread run-queue wait | percent | 1 | 14.559 | 14.559 | 14.559 | 14.559 | 0.146762 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29322) vms_mb | MB | 2 | 1654.225 | 1618.727 | 1689.723 | 1689.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29387) CPU | percent | 22 | 13.050 | 0.995 | 75.510 | 4.968 | 2.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29387) rss_mb | MB | 23 | 380.329 | 259.980 | 392.797 | 392.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29387) main thread run-queue wait | percent | 22 | 1.248 | 0.002 | 18.907 | 0.019 | 0.276439 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29387) vms_mb | MB | 23 | 9472.852 | 1656.062 | 10210.258 | 10210.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29409) CPU | percent | 1 | 52.622 | 52.622 | 52.622 | 52.622 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29409) rss_mb | MB | 2 | 252.857 | 212.180 | 293.535 | 293.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29409) main thread run-queue wait | percent | 1 | 15.035 | 15.035 | 15.035 | 15.035 | 0.151427 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29409) vms_mb | MB | 2 | 1655.629 | 1622.211 | 1689.047 | 1689.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29419) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29419) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29420) rss_mb | MB | 1 | 10.461 | 10.461 | 10.461 | 10.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29420) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29434) rss_mb | MB | 1 | 131.398 | 131.398 | 131.398 | 131.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29434) vms_mb | MB | 1 | 352.160 | 352.160 | 352.160 | 352.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29443) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29443) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29444) rss_mb | MB | 1 | 10.098 | 10.098 | 10.098 | 10.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29444) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29448) CPU | percent | 8 | 43.795 | 3.971 | 86.260 | 5.967 | 3.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29448) rss_mb | MB | 9 | 318.464 | 0.000 | 391.746 | 391.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29448) main thread run-queue wait | percent | 8 | 5.524 | 0.006 | 18.811 | 0.006 | 0.445311 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29448) vms_mb | MB | 9 | 7188.840 | 160.145 | 10208.820 | 10208.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29470) CPU | percent | 1 | 60.457 | 60.457 | 60.457 | 60.457 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29470) rss_mb | MB | 2 | 232.562 | 193.699 | 271.426 | 271.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29470) main thread run-queue wait | percent | 1 | 13.708 | 13.708 | 13.708 | 13.708 | 0.138314 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29470) vms_mb | MB | 2 | 1640.623 | 1614.473 | 1666.773 | 1666.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29496) CPU | percent | 24 | 14.822 | 0.994 | 68.307 | 1.990 | 3.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29496) rss_mb | MB | 25 | 382.126 | 229.250 | 399.695 | 398.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29496) main thread run-queue wait | percent | 24 | 1.944 | 0.003 | 16.391 | 0.128 | 0.471226 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29496) vms_mb | MB | 25 | 9525.417 | 1632.047 | 10216.062 | 10215.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 29509) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 29509) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29513) CPU | percent | 2 | 58.418 | 56.308 | 60.529 | 60.529 | 1.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29513) rss_mb | MB | 3 | 186.964 | 36.516 | 295.438 | 295.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29513) main thread run-queue wait | percent | 2 | 13.985 | 13.800 | 14.171 | 14.171 | 0.282508 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29513) vms_mb | MB | 3 | 1497.367 | 1170.371 | 1689.988 | 1689.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29525) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29525) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29526) rss_mb | MB | 1 | 10.559 | 10.559 | 10.559 | 10.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29526) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 29540) rss_mb | MB | 1 | 2.668 | 2.668 | 2.668 | 2.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 29540) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 29541) rss_mb | MB | 1 | 85.398 | 85.398 | 85.398 | 85.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 29541) vms_mb | MB | 1 | 89.211 | 89.211 | 89.211 | 89.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29633) CPU | percent | 13 | 18.939 | 0.994 | 79.532 | 3.978 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29633) rss_mb | MB | 14 | 376.198 | 283.387 | 395.621 | 395.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29633) main thread run-queue wait | percent | 13 | 2.349 | 0.002 | 24.211 | 0.003 | 0.307926 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29633) vms_mb | MB | 14 | 9586.504 | 1678.598 | 10212.281 | 10212.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29653) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29653) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29654) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29654) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29655) CPU | percent | 1 | 55.527 | 55.527 | 55.527 | 55.527 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29655) rss_mb | MB | 2 | 251.588 | 213.445 | 289.730 | 289.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29655) main thread run-queue wait | percent | 1 | 26.050 | 26.050 | 26.050 | 26.050 | 0.262718 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29655) vms_mb | MB | 2 | 1654.551 | 1623.758 | 1685.344 | 1685.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29683) CPU | percent | 22 | 14.536 | 0.995 | 75.569 | 1.989 | 3.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29683) rss_mb | MB | 23 | 379.532 | 229.809 | 394.734 | 394.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29683) main thread run-queue wait | percent | 22 | 1.107 | 0.001 | 14.811 | 0.017 | 0.245509 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29683) vms_mb | MB | 23 | 9466.164 | 1632.762 | 10212.742 | 10212.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29706) CPU | percent | 1 | 34.680 | 34.680 | 34.680 | 34.680 | 0.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29706) rss_mb | MB | 2 | 178.672 | 145.789 | 211.555 | 211.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29706) main thread run-queue wait | percent | 1 | 16.656 | 16.656 | 16.656 | 16.656 | 0.168099 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29706) vms_mb | MB | 2 | 1462.365 | 1301.734 | 1622.996 | 1622.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29713) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29713) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29714) rss_mb | MB | 1 | 5.840 | 5.840 | 5.840 | 5.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29714) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29727) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29727) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 29728) rss_mb | MB | 1 | 21.168 | 21.168 | 21.168 | 21.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 29728) vms_mb | MB | 1 | 26.938 | 26.938 | 26.938 | 26.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29742) CPU | percent | 8 | 39.993 | 4.972 | 87.413 | 9.946 | 3.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29742) rss_mb | MB | 9 | 326.783 | 44.496 | 390.254 | 390.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29742) main thread run-queue wait | percent | 8 | 4.609 | 0.010 | 12.246 | 0.013 | 0.371226 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29742) vms_mb | MB | 9 | 8233.614 | 1174.262 | 10209.918 | 10209.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29760) CPU | percent | 1 | 59.524 | 59.524 | 59.524 | 59.524 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29760) rss_mb | MB | 2 | 223.104 | 176.020 | 270.188 | 270.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29760) main thread run-queue wait | percent | 1 | 17.922 | 17.922 | 17.922 | 17.922 | 0.180657 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29760) vms_mb | MB | 2 | 1628.252 | 1590.723 | 1665.781 | 1665.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 29783) rss_mb | MB | 1 | 56.828 | 56.828 | 56.828 | 56.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 29783) vms_mb | MB | 1 | 900.508 | 900.508 | 900.508 | 900.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29788) CPU | percent | 26 | 13.915 | 0.990 | 83.320 | 6.877 | 3.660000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29788) rss_mb | MB | 27 | 378.148 | 166.758 | 395.906 | 395.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29788) main thread run-queue wait | percent | 26 | 3.068 | 0.002 | 31.256 | 0.018 | 0.806326 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29788) vms_mb | MB | 27 | 9571.382 | 1577.969 | 10208.996 | 10208.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29813) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29813) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29814) rss_mb | MB | 1 | 9.258 | 9.258 | 9.258 | 9.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29814) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29822) CPU | percent | 2 | 158.149 | 145.947 | 170.351 | 170.351 | 3.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29822) rss_mb | MB | 3 | 106.828 | 64.391 | 128.758 | 128.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29822) main thread run-queue wait | percent | 2 | 49.831 | 38.263 | 61.399 | 61.399 | 1.005322 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_adapter.py (PID 29822) vms_mb | MB | 3 | 326.598 | 287.582 | 346.105 | 346.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29838) CPU | percent | 11 | 24.820 | 1.989 | 75.459 | 5.968 | 2.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29838) rss_mb | MB | 12 | 369.076 | 229.258 | 397.562 | 397.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29838) main thread run-queue wait | percent | 11 | 2.907 | 0.002 | 19.193 | 0.306 | 0.322193 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29838) vms_mb | MB | 12 | 8784.840 | 1632.305 | 10212.691 | 10212.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29859) CPU | percent | 1 | 44.640 | 44.640 | 44.640 | 44.640 | 0.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29859) rss_mb | MB | 2 | 194.721 | 160.895 | 228.547 | 228.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29859) main thread run-queue wait | percent | 1 | 14.121 | 14.121 | 14.121 | 14.121 | 0.142353 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29859) vms_mb | MB | 2 | 1474.533 | 1317.723 | 1631.344 | 1631.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29887) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29887) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29889) rss_mb | MB | 1 | 4.938 | 4.938 | 4.938 | 4.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29889) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29908) CPU | percent | 12 | 27.282 | 2.980 | 80.121 | 2.980 | 3.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29908) rss_mb | MB | 13 | 348.635 | 84.520 | 394.340 | 394.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29908) main thread run-queue wait | percent | 12 | 3.232 | 0.004 | 23.216 | 0.006 | 0.391217 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29908) vms_mb | MB | 13 | 8222.260 | 1283.598 | 10213.340 | 10213.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29928) CPU | percent | 1 | 51.520 | 51.520 | 51.520 | 51.520 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29928) rss_mb | MB | 2 | 242.514 | 206.262 | 278.766 | 278.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29928) main thread run-queue wait | percent | 1 | 27.029 | 27.029 | 27.029 | 27.029 | 0.272807 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29928) vms_mb | MB | 2 | 1646.746 | 1619.453 | 1674.039 | 1674.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29938) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29938) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29939) rss_mb | MB | 1 | 10.086 | 10.086 | 10.086 | 10.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29939) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29956) CPU | percent | 11 | 20.772 | 0.994 | 78.448 | 0.994 | 2.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29956) rss_mb | MB | 12 | 370.799 | 271.551 | 391.535 | 391.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29956) main thread run-queue wait | percent | 11 | 1.262 | 0.003 | 9.469 | 0.003 | 0.146724 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29956) vms_mb | MB | 12 | 8800.450 | 1666.730 | 10212.117 | 10212.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29973) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29973) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29974) rss_mb | MB | 1 | 7.980 | 7.980 | 7.980 | 7.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29974) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29979) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 29979) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29980) rss_mb | MB | 1 | 9.988 | 9.988 | 9.988 | 9.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 29980) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29984) CPU | percent | 1 | 63.056 | 63.056 | 63.056 | 63.056 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29984) rss_mb | MB | 2 | 133.445 | 7.566 | 259.324 | 259.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29984) main thread run-queue wait | percent | 1 | 7.658 | 7.658 | 7.658 | 7.658 | 0.082584 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 29984) vms_mb | MB | 2 | 910.455 | 165.590 | 1655.320 | 1655.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 29992) rss_mb | MB | 1 | 2.270 | 2.270 | 2.270 | 2.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 29992) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 29993) rss_mb | MB | 1 | 1.555 | 1.555 | 1.555 | 1.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 29993) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30003) CPU | percent | 24 | 11.776 | 1.985 | 75.426 | 6.962 | 2.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30003) rss_mb | MB | 25 | 385.412 | 295.363 | 397.340 | 396.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30003) main thread run-queue wait | percent | 24 | 2.021 | 0.002 | 22.348 | 0.010 | 0.489972 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30003) vms_mb | MB | 25 | 9859.672 | 1689.668 | 10210.691 | 10209.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30024) CPU | percent | 1 | 52.552 | 52.552 | 52.552 | 52.552 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30024) rss_mb | MB | 2 | 188.652 | 142.227 | 235.078 | 235.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30024) main thread run-queue wait | percent | 1 | 13.080 | 13.080 | 13.080 | 13.080 | 0.131917 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30024) vms_mb | MB | 2 | 1467.129 | 1298.430 | 1635.828 | 1635.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30036) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30036) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30037) rss_mb | MB | 1 | 7.184 | 7.184 | 7.184 | 7.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30037) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30050) CPU | percent | 2 | 40.193 | 12.884 | 67.502 | 67.502 | 0.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30050) rss_mb | MB | 3 | 31.087 | 2.664 | 64.875 | 64.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30050) main thread run-queue wait | percent | 2 | 0.311 | 0.106 | 0.517 | 0.106 | 0.006284 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30050) vms_mb | MB | 3 | 38.483 | 3.848 | 79.801 | 79.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 30051) rss_mb | MB | 1 | 22.867 | 22.867 | 22.867 | 22.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 30051) vms_mb | MB | 1 | 215.410 | 215.410 | 215.410 | 215.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30067) CPU | percent | 12 | 24.713 | 0.994 | 71.416 | 0.994 | 3.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30067) rss_mb | MB | 13 | 364.087 | 193.973 | 390.562 | 390.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30067) main thread run-queue wait | percent | 12 | 2.846 | 0.003 | 15.061 | 0.003 | 0.351047 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30067) vms_mb | MB | 13 | 8889.496 | 1614.469 | 10212.676 | 10212.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30086) CPU | percent | 1 | 57.950 | 57.950 | 57.950 | 57.950 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30086) rss_mb | MB | 2 | 213.305 | 166.910 | 259.699 | 259.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30086) main thread run-queue wait | percent | 1 | 10.974 | 10.974 | 10.974 | 10.974 | 0.111733 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30086) vms_mb | MB | 2 | 1616.408 | 1577.723 | 1655.094 | 1655.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30114) CPU | percent | 12 | 26.798 | 1.988 | 84.224 | 1.988 | 3.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30114) rss_mb | MB | 13 | 358.840 | 154.961 | 395.227 | 395.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30114) main thread run-queue wait | percent | 12 | 4.669 | 0.005 | 29.575 | 0.005 | 0.564395 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30114) vms_mb | MB | 13 | 8874.140 | 1499.465 | 10213.758 | 10213.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30134) CPU | percent | 2 | 50.650 | 46.636 | 54.663 | 46.636 | 1.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30134) rss_mb | MB | 3 | 227.410 | 145.180 | 302.152 | 302.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30134) main thread run-queue wait | percent | 2 | 18.728 | 13.677 | 23.780 | 23.780 | 0.377266 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30134) vms_mb | MB | 3 | 1554.574 | 1301.309 | 1726.836 | 1726.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30162) CPU | percent | 10 | 25.818 | 1.988 | 74.591 | 2.980 | 2.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30162) rss_mb | MB | 11 | 371.638 | 255.633 | 401.441 | 401.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30162) main thread run-queue wait | percent | 10 | 2.070 | 0.004 | 14.405 | 0.004 | 0.208588 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30162) vms_mb | MB | 11 | 8657.389 | 1651.281 | 10212.906 | 10212.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30186) CPU | percent | 1 | 37.691 | 37.691 | 37.691 | 37.691 | 0.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30186) rss_mb | MB | 2 | 177.072 | 141.168 | 212.977 | 212.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30186) main thread run-queue wait | percent | 1 | 12.624 | 12.624 | 12.624 | 12.624 | 0.127275 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30186) vms_mb | MB | 2 | 1459.824 | 1297.176 | 1622.473 | 1622.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30210) CPU | percent | 12 | 20.486 | 0.994 | 80.338 | 0.995 | 2.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30210) rss_mb | MB | 13 | 373.948 | 260.086 | 396.195 | 396.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30210) main thread run-queue wait | percent | 12 | 1.060 | 0.003 | 8.410 | 0.006 | 0.129973 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30210) vms_mb | MB | 13 | 8908.877 | 1655.859 | 10212.297 | 10212.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30234) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30234) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30235) rss_mb | MB | 1 | 8.734 | 8.734 | 8.734 | 8.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30235) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30239) rss_mb | MB | 1 | 296.281 | 296.281 | 296.281 | 296.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30239) vms_mb | MB | 1 | 1691.336 | 1691.336 | 1691.336 | 1691.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30274) CPU | percent | 26 | 11.148 | 0.995 | 80.403 | 1.976 | 2.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30274) rss_mb | MB | 27 | 387.601 | 282.355 | 400.422 | 399.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30274) main thread run-queue wait | percent | 26 | 1.671 | 0.001 | 23.569 | 0.028 | 0.437892 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30274) vms_mb | MB | 27 | 9889.941 | 1677.746 | 10216.145 | 10215.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30293) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30293) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30294) rss_mb | MB | 1 | 7.215 | 7.215 | 7.215 | 7.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30294) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30295) CPU | percent | 1 | 53.618 | 53.618 | 53.618 | 53.618 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30295) rss_mb | MB | 2 | 262.051 | 229.184 | 294.918 | 294.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30295) main thread run-queue wait | percent | 1 | 20.108 | 20.108 | 20.108 | 20.108 | 0.202513 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30295) vms_mb | MB | 2 | 1661.020 | 1632.477 | 1689.562 | 1689.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30320) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30320) rss_mb | MB | 4 | 2.578 | 2.578 | 2.578 | 2.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30320) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 30320) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 30321) CPU | percent | 3 | 4.936 | 0.000 | 14.808 | 0.000 | 0.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 30321) rss_mb | MB | 4 | 22.827 | 17.680 | 24.543 | 24.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 30321) main thread run-queue wait | percent | 3 | 1.965 | 0.000 | 5.896 | 0.000 | 0.059719 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 30321) vms_mb | MB | 4 | 215.258 | 209.867 | 217.055 | 217.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 30325) CPU | percent | 2 | 15.402 | 0.000 | 30.803 | 0.000 | 0.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 30325) rss_mb | MB | 3 | 58.887 | 45.191 | 65.734 | 65.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 30325) main thread run-queue wait | percent | 2 | 0.035 | 0.000 | 0.071 | 0.000 | 0.000710 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 30325) vms_mb | MB | 3 | 71.307 | 53.594 | 80.164 | 80.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30326) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30326) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 30327) rss_mb | MB | 1 | 20.316 | 20.316 | 20.316 | 20.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 30327) vms_mb | MB | 1 | 25.320 | 25.320 | 25.320 | 25.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30343) CPU | percent | 12 | 20.497 | 1.989 | 79.381 | 8.952 | 2.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30343) rss_mb | MB | 13 | 376.241 | 289.852 | 396.184 | 396.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30343) main thread run-queue wait | percent | 12 | 1.963 | 0.005 | 16.411 | 0.025 | 0.237993 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30343) vms_mb | MB | 13 | 9540.251 | 1684.516 | 10212.828 | 10212.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30362) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30362) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30363) rss_mb | MB | 1 | 9.855 | 9.855 | 9.855 | 9.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30363) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30367) CPU | percent | 1 | 50.555 | 50.555 | 50.555 | 50.555 | 0.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30367) rss_mb | MB | 2 | 217.680 | 180.109 | 255.250 | 255.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30367) main thread run-queue wait | percent | 1 | 19.122 | 19.122 | 19.122 | 19.122 | 0.192908 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30367) vms_mb | MB | 2 | 1621.289 | 1591.473 | 1651.105 | 1651.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30377) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30377) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30394) CPU | percent | 12 | 25.093 | 1.989 | 69.552 | 1.989 | 3.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30394) rss_mb | MB | 13 | 366.086 | 193.387 | 399.609 | 399.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30394) main thread run-queue wait | percent | 12 | 1.439 | 0.005 | 9.166 | 0.011 | 0.173704 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30394) vms_mb | MB | 13 | 8888.977 | 1614.219 | 10209.066 | 10209.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30421) CPU | percent | 1 | 80.495 | 80.495 | 80.495 | 80.495 | 0.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30421) rss_mb | MB | 2 | 234.133 | 166.281 | 301.984 | 301.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30421) main thread run-queue wait | percent | 1 | 7.289 | 7.289 | 7.289 | 7.289 | 0.073349 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30421) vms_mb | MB | 2 | 1652.131 | 1577.973 | 1726.289 | 1726.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30442) CPU | percent | 12 | 22.261 | 1.989 | 71.530 | 1.989 | 2.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30442) rss_mb | MB | 13 | 376.498 | 269.797 | 402.008 | 402.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30442) main thread run-queue wait | percent | 12 | 3.914 | 0.003 | 21.461 | 0.004 | 0.473317 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30442) vms_mb | MB | 13 | 9534.131 | 1666.020 | 10213.426 | 10213.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30459) CPU | percent | 1 | 58.482 | 58.482 | 58.482 | 58.482 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30459) rss_mb | MB | 2 | 214.855 | 167.691 | 262.020 | 262.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30459) main thread run-queue wait | percent | 1 | 15.508 | 15.508 | 15.508 | 15.508 | 0.156456 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30459) vms_mb | MB | 2 | 1618.029 | 1578.473 | 1657.586 | 1657.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30489) CPU | percent | 13 | 20.785 | 0.995 | 67.619 | 2.983 | 2.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30489) rss_mb | MB | 14 | 374.229 | 262.234 | 396.320 | 396.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30489) main thread run-queue wait | percent | 13 | 2.518 | 0.003 | 12.454 | 0.009 | 0.333008 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30489) vms_mb | MB | 14 | 9571.995 | 1657.719 | 10212.539 | 10212.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30508) CPU | percent | 1 | 57.486 | 57.486 | 57.486 | 57.486 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30508) rss_mb | MB | 2 | 211.193 | 166.617 | 255.770 | 255.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30508) main thread run-queue wait | percent | 1 | 16.743 | 16.743 | 16.743 | 16.743 | 0.168924 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30508) vms_mb | MB | 2 | 1614.531 | 1577.723 | 1651.340 | 1651.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30538) CPU | percent | 13 | 26.400 | 1.987 | 84.308 | 8.950 | 3.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30538) rss_mb | MB | 14 | 351.500 | 35.566 | 397.805 | 397.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30538) main thread run-queue wait | percent | 13 | 2.107 | 0.005 | 17.658 | 0.020 | 0.285442 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30538) vms_mb | MB | 14 | 8355.898 | 1169.414 | 10212.883 | 10212.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30564) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30564) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30565) rss_mb | MB | 1 | 9.031 | 9.031 | 9.031 | 9.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30565) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30566) CPU | percent | 1 | 57.507 | 57.507 | 57.507 | 57.507 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30566) rss_mb | MB | 2 | 127.783 | 26.402 | 229.164 | 229.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30566) main thread run-queue wait | percent | 1 | 13.931 | 13.931 | 13.931 | 13.931 | 0.147773 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30566) vms_mb | MB | 2 | 898.904 | 165.848 | 1631.961 | 1631.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 30581) rss_mb | MB | 1 | 2.039 | 2.039 | 2.039 | 2.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 30581) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 30582) rss_mb | MB | 1 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 30582) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30607) CPU | percent | 11 | 27.271 | 0.993 | 75.449 | 3.979 | 3.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30607) rss_mb | MB | 12 | 363.378 | 193.793 | 399.398 | 399.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30607) main thread run-queue wait | percent | 11 | 4.153 | 0.007 | 18.336 | 0.038 | 0.485346 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30607) vms_mb | MB | 12 | 8778.524 | 1614.469 | 10213.562 | 10213.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30684) CPU | percent | 1 | 53.270 | 53.270 | 53.270 | 53.270 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30684) rss_mb | MB | 2 | 210.295 | 167.109 | 253.480 | 253.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30684) main thread run-queue wait | percent | 1 | 15.083 | 15.083 | 15.083 | 15.083 | 0.152895 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30684) vms_mb | MB | 2 | 1613.928 | 1578.223 | 1649.633 | 1649.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30696) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30696) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30712) CPU | percent | 13 | 22.550 | 1.989 | 80.549 | 7.956 | 2.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30712) rss_mb | MB | 14 | 371.562 | 255.863 | 392.367 | 392.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30712) main thread run-queue wait | percent | 13 | 1.742 | 0.002 | 15.388 | 0.023 | 0.228081 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30712) vms_mb | MB | 14 | 8994.281 | 1652.055 | 10214.379 | 10214.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30733) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30733) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30734) rss_mb | MB | 1 | 9.062 | 9.062 | 9.062 | 9.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30734) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30740) CPU | percent | 1 | 74.549 | 74.549 | 74.549 | 74.549 | 0.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30740) rss_mb | MB | 2 | 222.482 | 158.824 | 286.141 | 286.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30740) main thread run-queue wait | percent | 1 | 9.433 | 9.433 | 9.433 | 9.433 | 0.094896 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30740) vms_mb | MB | 2 | 1590.766 | 1499.969 | 1681.562 | 1681.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30759) CPU | percent | 15 | 20.288 | 0.994 | 75.370 | 7.958 | 3.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30759) rss_mb | MB | 16 | 369.604 | 188.367 | 396.082 | 396.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30759) main thread run-queue wait | percent | 15 | 2.712 | 0.003 | 16.545 | 0.018 | 0.432494 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30759) vms_mb | MB | 16 | 9135.470 | 1594.219 | 10213.391 | 10213.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30780) CPU | percent | 1 | 56.260 | 56.260 | 56.260 | 56.260 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30780) rss_mb | MB | 2 | 211.246 | 166.848 | 255.645 | 255.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30780) main thread run-queue wait | percent | 1 | 15.465 | 15.465 | 15.465 | 15.465 | 0.156683 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30780) vms_mb | MB | 2 | 1614.771 | 1577.973 | 1651.570 | 1651.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30808) CPU | percent | 6 | 43.370 | 1.989 | 70.423 | 1.989 | 2.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30808) rss_mb | MB | 7 | 339.841 | 185.523 | 383.711 | 383.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30808) main thread run-queue wait | percent | 6 | 4.403 | 0.007 | 13.714 | 0.007 | 0.266059 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30808) vms_mb | MB | 7 | 7757.589 | 1593.219 | 10210.484 | 10210.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30832) rss_mb | MB | 1 | 199.230 | 199.230 | 199.230 | 199.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30832) vms_mb | MB | 1 | 1617.488 | 1617.488 | 1617.488 | 1617.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30858) CPU | percent | 13 | 18.480 | 0.995 | 80.546 | 0.995 | 2.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30858) rss_mb | MB | 14 | 372.909 | 266.785 | 391.973 | 391.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30858) main thread run-queue wait | percent | 13 | 2.224 | 0.003 | 21.004 | 0.007 | 0.291820 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30858) vms_mb | MB | 14 | 9586.364 | 1663.266 | 10213.426 | 10213.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 30875) rss_mb | MB | 1 | 44.844 | 44.844 | 44.844 | 44.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 30875) vms_mb | MB | 1 | 836.945 | 836.945 | 836.945 | 836.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30877) CPU | percent | 1 | 54.460 | 54.460 | 54.460 | 54.460 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30877) rss_mb | MB | 2 | 262.826 | 229.094 | 296.559 | 296.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30877) main thread run-queue wait | percent | 1 | 22.890 | 22.890 | 22.890 | 22.890 | 0.231166 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30877) vms_mb | MB | 2 | 1677.869 | 1632.238 | 1723.500 | 1723.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30905) CPU | percent | 14 | 17.594 | 0.995 | 77.536 | 8.950 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30905) rss_mb | MB | 15 | 378.386 | 272.051 | 397.457 | 397.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30905) main thread run-queue wait | percent | 14 | 2.449 | 0.004 | 19.882 | 0.011 | 0.345327 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30905) vms_mb | MB | 15 | 9628.616 | 1667.254 | 10212.609 | 10212.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30923) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 30923) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30924) rss_mb | MB | 1 | 6.992 | 6.992 | 6.992 | 6.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 30924) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30925) CPU | percent | 1 | 50.633 | 50.633 | 50.633 | 50.633 | 0.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30925) rss_mb | MB | 2 | 263.588 | 229.012 | 298.164 | 298.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30925) main thread run-queue wait | percent | 1 | 17.654 | 17.654 | 17.654 | 17.654 | 0.177825 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30925) vms_mb | MB | 2 | 1677.889 | 1631.711 | 1724.066 | 1724.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30954) CPU | percent | 12 | 24.096 | 0.995 | 72.546 | 0.995 | 2.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30954) rss_mb | MB | 13 | 365.004 | 194.023 | 397.477 | 397.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30954) main thread run-queue wait | percent | 12 | 2.720 | 0.006 | 18.516 | 0.006 | 0.329243 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30954) vms_mb | MB | 13 | 8892.549 | 1614.219 | 10213.824 | 10213.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30981) CPU | percent | 1 | 78.420 | 78.420 | 78.420 | 78.420 | 0.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30981) rss_mb | MB | 2 | 231.863 | 166.617 | 297.109 | 297.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30981) main thread run-queue wait | percent | 1 | 10.161 | 10.161 | 10.161 | 10.161 | 0.102357 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 30981) vms_mb | MB | 2 | 1634.969 | 1578.223 | 1691.715 | 1691.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31004) CPU | percent | 12 | 20.462 | 0.995 | 62.653 | 7.956 | 2.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31004) rss_mb | MB | 13 | 372.457 | 229.504 | 401.461 | 401.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31004) main thread run-queue wait | percent | 12 | 2.726 | 0.002 | 19.042 | 0.037 | 0.330145 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31004) vms_mb | MB | 13 | 8887.680 | 1631.812 | 10209.480 | 10209.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31021) CPU | percent | 1 | 54.574 | 54.574 | 54.574 | 54.574 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31021) rss_mb | MB | 2 | 196.055 | 154.871 | 237.238 | 237.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31021) main thread run-queue wait | percent | 1 | 16.005 | 16.005 | 16.005 | 16.005 | 0.161302 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31021) vms_mb | MB | 2 | 1474.250 | 1310.871 | 1637.629 | 1637.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 31044) rss_mb | MB | 1 | 59.375 | 59.375 | 59.375 | 59.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 31044) vms_mb | MB | 1 | 893.219 | 893.219 | 893.219 | 893.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31051) CPU | percent | 12 | 25.752 | 1.988 | 81.319 | 2.982 | 3.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31051) rss_mb | MB | 13 | 362.416 | 176.488 | 396.055 | 396.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31051) main thread run-queue wait | percent | 12 | 1.876 | 0.001 | 7.886 | 0.012 | 0.232092 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31051) vms_mb | MB | 13 | 8882.011 | 1590.719 | 10212.637 | 10212.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31076) CPU | percent | 1 | 62.887 | 62.887 | 62.887 | 62.887 | 0.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31076) rss_mb | MB | 2 | 238.391 | 182.746 | 294.035 | 294.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31076) main thread run-queue wait | percent | 1 | 16.758 | 16.758 | 16.758 | 16.758 | 0.178534 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31076) vms_mb | MB | 2 | 1640.768 | 1592.723 | 1688.812 | 1688.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31100) CPU | percent | 12 | 21.272 | 0.995 | 70.453 | 1.990 | 2.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31100) rss_mb | MB | 13 | 374.147 | 273.762 | 394.973 | 394.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31100) main thread run-queue wait | percent | 12 | 3.334 | 0.001 | 12.841 | 0.006 | 0.404624 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31100) vms_mb | MB | 13 | 9537.271 | 1668.723 | 10213.488 | 10213.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31119) CPU | percent | 1 | 57.555 | 57.555 | 57.555 | 57.555 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31119) rss_mb | MB | 2 | 208.879 | 164.305 | 253.453 | 253.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31119) main thread run-queue wait | percent | 1 | 19.816 | 19.816 | 19.816 | 19.816 | 0.199692 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31119) vms_mb | MB | 2 | 1611.145 | 1572.473 | 1649.816 | 1649.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31149) CPU | percent | 13 | 18.537 | 0.995 | 78.550 | 9.943 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31149) rss_mb | MB | 14 | 378.250 | 293.156 | 395.582 | 395.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31149) main thread run-queue wait | percent | 13 | 0.542 | 0.004 | 2.650 | 0.021 | 0.071319 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31149) vms_mb | MB | 14 | 9589.702 | 1688.117 | 10213.645 | 10213.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31166) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31166) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31167) rss_mb | MB | 1 | 9.871 | 9.871 | 9.871 | 9.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31167) vms_mb | MB | 1 | 13.520 | 13.520 | 13.520 | 13.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31179) rss_mb | MB | 1 | 158.012 | 158.012 | 158.012 | 158.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31179) vms_mb | MB | 1 | 1499.969 | 1499.969 | 1499.969 | 1499.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31198) CPU | percent | 13 | 27.142 | 0.994 | 86.326 | 5.936 | 3.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31198) rss_mb | MB | 14 | 362.597 | 160.172 | 396.832 | 396.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31198) main thread run-queue wait | percent | 13 | 1.124 | 0.006 | 5.444 | 0.049 | 0.147710 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31198) vms_mb | MB | 14 | 8970.442 | 1500.215 | 10213.496 | 10213.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31216) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31216) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31217) rss_mb | MB | 1 | 5.359 | 5.359 | 5.359 | 5.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31217) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31228) CPU | percent | 1 | 91.365 | 91.365 | 91.365 | 91.365 | 0.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31228) rss_mb | MB | 2 | 172.523 | 58.215 | 286.832 | 286.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31228) main thread run-queue wait | percent | 1 | 5.395 | 5.395 | 5.395 | 5.395 | 0.054324 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31228) vms_mb | MB | 2 | 1459.828 | 1238.609 | 1681.047 | 1681.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31242) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31242) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31243) rss_mb | MB | 1 | 10.109 | 10.109 | 10.109 | 10.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31243) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31247) CPU | percent | 15 | 25.149 | 1.987 | 88.217 | 1.988 | 3.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31247) rss_mb | MB | 16 | 364.590 | 154.141 | 398.562 | 398.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31247) main thread run-queue wait | percent | 15 | 2.816 | 0.004 | 15.052 | 0.021 | 0.426503 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31247) vms_mb | MB | 16 | 9116.527 | 1499.465 | 10210.363 | 10210.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31264) CPU | percent | 1 | 59.484 | 59.484 | 59.484 | 59.484 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31264) rss_mb | MB | 2 | 220.219 | 180.793 | 259.645 | 259.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31264) main thread run-queue wait | percent | 1 | 15.806 | 15.806 | 15.806 | 15.806 | 0.159427 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31264) vms_mb | MB | 2 | 1623.533 | 1591.223 | 1655.844 | 1655.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31283) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31283) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31284) rss_mb | MB | 1 | 9.000 | 9.000 | 9.000 | 9.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31284) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31295) CPU | percent | 10 | 25.609 | 0.995 | 69.498 | 0.995 | 2.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31295) rss_mb | MB | 11 | 367.842 | 235.102 | 400.168 | 400.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31295) main thread run-queue wait | percent | 10 | 2.719 | 0.004 | 13.961 | 0.007 | 0.274358 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31295) vms_mb | MB | 11 | 8652.708 | 1636.289 | 10210.363 | 10210.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31314) CPU | percent | 1 | 57.379 | 57.379 | 57.379 | 57.379 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31314) rss_mb | MB | 2 | 227.822 | 184.508 | 271.137 | 271.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31314) main thread run-queue wait | percent | 1 | 17.191 | 17.191 | 17.191 | 17.191 | 0.173770 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31314) vms_mb | MB | 2 | 1630.016 | 1592.973 | 1667.059 | 1667.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31342) CPU | percent | 13 | 20.775 | 0.993 | 63.401 | 7.953 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31342) rss_mb | MB | 14 | 370.375 | 235.223 | 395.043 | 395.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31342) main thread run-queue wait | percent | 13 | 3.478 | 0.003 | 17.745 | 0.019 | 0.465352 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31342) vms_mb | MB | 14 | 8983.261 | 1635.797 | 10210.441 | 10210.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 31355) rss_mb | MB | 1 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 31355) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31361) CPU | percent | 1 | 58.496 | 58.496 | 58.496 | 58.496 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31361) rss_mb | MB | 2 | 170.598 | 106.047 | 235.148 | 235.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31361) main thread run-queue wait | percent | 1 | 19.997 | 19.997 | 19.997 | 19.997 | 0.201690 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31361) vms_mb | MB | 2 | 1459.768 | 1283.695 | 1635.840 | 1635.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31410) CPU | percent | 12 | 22.351 | 0.994 | 65.566 | 0.994 | 2.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31410) rss_mb | MB | 13 | 364.755 | 217.379 | 392.875 | 392.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31410) main thread run-queue wait | percent | 12 | 2.786 | 0.006 | 21.710 | 0.006 | 0.337015 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31410) vms_mb | MB | 13 | 8893.061 | 1623.293 | 10212.469 | 10212.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31433) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31433) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31434) rss_mb | MB | 1 | 9.902 | 9.902 | 9.902 | 9.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31434) vms_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31435) rss_mb | MB | 1 | 205.629 | 205.629 | 205.629 | 205.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31435) vms_mb | MB | 1 | 1618.965 | 1618.965 | 1618.965 | 1618.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31459) CPU | percent | 12 | 18.797 | 0.994 | 78.563 | 3.977 | 2.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31459) rss_mb | MB | 13 | 369.670 | 279.168 | 389.332 | 389.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31459) main thread run-queue wait | percent | 12 | 1.594 | 0.002 | 11.074 | 0.027 | 0.192591 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31459) vms_mb | MB | 13 | 9539.222 | 1674.230 | 10210.402 | 10210.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31482) CPU | percent | 1 | 61.578 | 61.578 | 61.578 | 61.578 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31482) rss_mb | MB | 2 | 242.193 | 194.262 | 290.125 | 290.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31482) main thread run-queue wait | percent | 1 | 7.849 | 7.849 | 7.849 | 7.849 | 0.079029 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31482) vms_mb | MB | 2 | 1649.770 | 1614.723 | 1684.816 | 1684.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31492) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31492) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31493) rss_mb | MB | 1 | 8.219 | 8.219 | 8.219 | 8.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31493) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31503) rss_mb | MB | 1 | 1.590 | 1.590 | 1.590 | 1.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31503) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31504) rss_mb | MB | 1 | 8.027 | 8.027 | 8.027 | 8.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31504) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31508) CPU | percent | 15 | 20.191 | 0.995 | 82.373 | 1.990 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31508) rss_mb | MB | 16 | 367.921 | 155.430 | 397.637 | 397.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31508) main thread run-queue wait | percent | 15 | 2.229 | 0.003 | 14.221 | 0.014 | 0.336903 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31508) vms_mb | MB | 16 | 9122.538 | 1499.465 | 10210.043 | 10210.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31527) CPU | percent | 1 | 56.624 | 56.624 | 56.624 | 56.624 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31527) rss_mb | MB | 2 | 205.986 | 155.340 | 256.633 | 256.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31527) main thread run-queue wait | percent | 1 | 14.867 | 14.867 | 14.867 | 14.867 | 0.149655 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31527) vms_mb | MB | 2 | 1575.893 | 1499.469 | 1652.316 | 1652.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31556) CPU | percent | 26 | 11.722 | 0.993 | 75.521 | 0.993 | 3.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31556) rss_mb | MB | 27 | 387.656 | 259.664 | 400.824 | 400.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31556) main thread run-queue wait | percent | 26 | 1.223 | 0.002 | 16.847 | 0.008 | 0.320569 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31556) vms_mb | MB | 27 | 9577.887 | 1655.266 | 10212.164 | 10212.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31577) CPU | percent | 1 | 53.477 | 53.477 | 53.477 | 53.477 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31577) rss_mb | MB | 2 | 244.756 | 203.590 | 285.922 | 285.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31577) main thread run-queue wait | percent | 1 | 16.709 | 16.709 | 16.709 | 16.709 | 0.168724 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31577) vms_mb | MB | 2 | 1649.631 | 1618.477 | 1680.785 | 1680.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31588) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31588) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31589) rss_mb | MB | 1 | 10.527 | 10.527 | 10.527 | 10.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31589) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31603) rss_mb | MB | 1 | 2.707 | 2.707 | 2.707 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 31603) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31604) rss_mb | MB | 1 | 20.645 | 20.645 | 20.645 | 20.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 31604) vms_mb | MB | 1 | 212.328 | 212.328 | 212.328 | 212.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31621) CPU | percent | 7 | 39.805 | 5.951 | 76.428 | 5.968 | 2.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31621) rss_mb | MB | 8 | 355.261 | 243.645 | 394.906 | 394.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31621) main thread run-queue wait | percent | 7 | 3.805 | 0.013 | 14.724 | 0.013 | 0.268835 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31621) vms_mb | MB | 8 | 8071.546 | 1640.035 | 10213.789 | 10213.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31647) CPU | percent | 1 | 62.318 | 62.318 | 62.318 | 62.318 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31647) rss_mb | MB | 2 | 236.375 | 188.957 | 283.793 | 283.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31647) main thread run-queue wait | percent | 1 | 14.235 | 14.235 | 14.235 | 14.235 | 0.143911 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31647) vms_mb | MB | 2 | 1636.252 | 1593.973 | 1678.531 | 1678.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31671) CPU | percent | 15 | 21.176 | 0.994 | 70.481 | 0.994 | 3.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31671) rss_mb | MB | 16 | 373.840 | 214.973 | 397.215 | 396.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31671) main thread run-queue wait | percent | 15 | 0.681 | 0.001 | 3.951 | 0.005 | 0.102965 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31671) vms_mb | MB | 16 | 9140.670 | 1623.020 | 10212.523 | 10211.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31699) rss_mb | MB | 1 | 224.488 | 224.488 | 224.488 | 224.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31699) vms_mb | MB | 1 | 1627.473 | 1627.473 | 1627.473 | 1627.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31798) CPU | percent | 14 | 21.624 | 1.987 | 71.464 | 7.949 | 3.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31798) rss_mb | MB | 15 | 369.763 | 187.652 | 397.949 | 397.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31798) main thread run-queue wait | percent | 14 | 3.019 | 0.003 | 16.136 | 0.032 | 0.426434 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31798) vms_mb | MB | 15 | 9062.552 | 1594.219 | 10210.609 | 10210.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31818) CPU | percent | 1 | 57.400 | 57.400 | 57.400 | 57.400 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31818) rss_mb | MB | 2 | 215.766 | 171.273 | 260.258 | 260.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31818) main thread run-queue wait | percent | 1 | 17.015 | 17.015 | 17.015 | 17.015 | 0.171932 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31818) vms_mb | MB | 2 | 1617.896 | 1579.723 | 1656.070 | 1656.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31832) rss_mb | MB | 1 | 1.398 | 1.398 | 1.398 | 1.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31832) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31833) rss_mb | MB | 1 | 7.832 | 7.832 | 7.832 | 7.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31833) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31849) CPU | percent | 14 | 21.141 | 0.994 | 70.490 | 0.994 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31849) rss_mb | MB | 15 | 371.277 | 216.473 | 397.883 | 397.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31849) main thread run-queue wait | percent | 14 | 1.316 | 0.001 | 7.933 | 0.005 | 0.185484 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31849) vms_mb | MB | 15 | 9070.854 | 1623.254 | 10213.570 | 10213.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31880) CPU | percent | 1 | 83.312 | 83.312 | 83.312 | 83.312 | 0.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31880) rss_mb | MB | 2 | 159.119 | 29.262 | 288.977 | 288.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31880) main thread run-queue wait | percent | 1 | 8.711 | 8.711 | 8.711 | 8.711 | 0.087825 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31880) vms_mb | MB | 2 | 973.555 | 263.309 | 1683.801 | 1683.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 31892) rss_mb | MB | 1 | 2.254 | 2.254 | 2.254 | 2.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 31892) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 31893) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 31893) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31899) CPU | percent | 13 | 25.132 | 1.982 | 84.480 | 1.982 | 3.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31899) rss_mb | MB | 14 | 359.960 | 114.023 | 399.672 | 399.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31899) main thread run-queue wait | percent | 13 | 3.114 | 0.005 | 25.056 | 0.006 | 0.407788 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31899) vms_mb | MB | 14 | 8948.335 | 1283.598 | 10210.547 | 10210.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31918) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 31918) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31919) rss_mb | MB | 1 | 7.262 | 7.262 | 7.262 | 7.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 31919) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31920) CPU | percent | 1 | 43.709 | 43.709 | 43.709 | 43.709 | 0.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31920) rss_mb | MB | 2 | 262.182 | 229.500 | 294.863 | 294.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31920) main thread run-queue wait | percent | 1 | 21.163 | 21.163 | 21.163 | 21.163 | 0.213045 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31920) vms_mb | MB | 2 | 1660.543 | 1632.000 | 1689.086 | 1689.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31948) CPU | percent | 12 | 25.594 | 1.989 | 81.478 | 2.984 | 3.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31948) rss_mb | MB | 13 | 361.824 | 154.418 | 396.812 | 396.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31948) main thread run-queue wait | percent | 12 | 1.155 | 0.005 | 4.099 | 0.008 | 0.140112 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31948) vms_mb | MB | 13 | 8879.551 | 1499.465 | 10214.414 | 10214.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31978) rss_mb | MB | 1 | 229.398 | 229.398 | 229.398 | 229.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31978) vms_mb | MB | 1 | 1632.477 | 1632.477 | 1632.477 | 1632.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31997) CPU | percent | 13 | 20.699 | 0.995 | 68.560 | 0.995 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31997) rss_mb | MB | 14 | 374.942 | 254.926 | 398.164 | 398.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31997) main thread run-queue wait | percent | 13 | 2.736 | 0.003 | 17.034 | 0.004 | 0.358470 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 31997) vms_mb | MB | 14 | 8985.164 | 1650.797 | 10210.008 | 10210.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32014) CPU | percent | 1 | 57.516 | 57.516 | 57.516 | 57.516 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32014) rss_mb | MB | 2 | 212.984 | 166.895 | 259.074 | 259.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32014) main thread run-queue wait | percent | 1 | 18.429 | 18.429 | 18.429 | 18.429 | 0.185840 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32014) vms_mb | MB | 2 | 1616.525 | 1577.723 | 1655.328 | 1655.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32045) CPU | percent | 14 | 23.733 | 0.995 | 87.371 | 0.995 | 3.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32045) rss_mb | MB | 15 | 355.801 | 40.227 | 399.734 | 399.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32045) main thread run-queue wait | percent | 14 | 3.560 | 0.004 | 13.930 | 0.012 | 0.504356 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32045) vms_mb | MB | 15 | 9023.623 | 1172.289 | 10210.492 | 10210.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32062) CPU | percent | 1 | 62.512 | 62.512 | 62.512 | 62.512 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32062) rss_mb | MB | 2 | 223.119 | 175.301 | 270.938 | 270.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32062) main thread run-queue wait | percent | 1 | 9.598 | 9.598 | 9.598 | 9.598 | 0.096732 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32062) vms_mb | MB | 2 | 1628.268 | 1590.223 | 1666.312 | 1666.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 32073) rss_mb | MB | 1 | 50.621 | 50.621 | 50.621 | 50.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi-code (PID 32073) vms_mb | MB | 1 | 851.293 | 851.293 | 851.293 | 851.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32092) CPU | percent | 12 | 27.969 | 1.989 | 82.393 | 6.963 | 3.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32092) rss_mb | MB | 13 | 350.950 | 34.875 | 399.488 | 399.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32092) main thread run-queue wait | percent | 12 | 1.523 | 0.003 | 10.063 | 0.013 | 0.184316 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32092) vms_mb | MB | 13 | 8844.159 | 1168.414 | 10212.922 | 10212.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32117) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32117) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32118) rss_mb | MB | 1 | 7.969 | 7.969 | 7.969 | 7.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32118) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32122) rss_mb | MB | 1 | 261.012 | 261.012 | 261.012 | 261.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32122) vms_mb | MB | 1 | 1656.570 | 1656.570 | 1656.570 | 1656.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32141) CPU | percent | 13 | 24.131 | 0.995 | 75.490 | 4.971 | 3.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32141) rss_mb | MB | 14 | 363.334 | 188.871 | 393.969 | 393.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32141) main thread run-queue wait | percent | 13 | 4.269 | 0.006 | 18.058 | 0.009 | 0.559841 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32141) vms_mb | MB | 14 | 8980.132 | 1593.969 | 10213.066 | 10213.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32158) CPU | percent | 1 | 59.393 | 59.393 | 59.393 | 59.393 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32158) rss_mb | MB | 2 | 250.242 | 205.691 | 294.793 | 294.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32158) main thread run-queue wait | percent | 1 | 12.986 | 12.986 | 12.986 | 12.986 | 0.131182 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32158) vms_mb | MB | 2 | 1654.096 | 1618.973 | 1689.219 | 1689.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32166) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32166) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32167) rss_mb | MB | 1 | 7.324 | 7.324 | 7.324 | 7.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32167) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32172) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32172) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32173) rss_mb | MB | 1 | 6.617 | 6.617 | 6.617 | 6.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32173) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 32183) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 32183) vms_mb | MB | 1 | 0.004 | 0.004 | 0.004 | 0.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32190) CPU | percent | 14 | 24.604 | 1.988 | 88.257 | 5.966 | 3.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32190) rss_mb | MB | 15 | 356.597 | 51.266 | 399.289 | 399.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32190) main thread run-queue wait | percent | 14 | 2.261 | 0.005 | 20.594 | 0.024 | 0.319264 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32190) vms_mb | MB | 15 | 9032.780 | 1238.512 | 10216.762 | 10216.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32209) CPU | percent | 1 | 54.488 | 54.488 | 54.488 | 54.488 | 0.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32209) rss_mb | MB | 2 | 242.961 | 205.535 | 280.387 | 280.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32209) main thread run-queue wait | percent | 1 | 20.713 | 20.713 | 20.713 | 20.713 | 0.209079 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32209) vms_mb | MB | 2 | 1647.145 | 1618.977 | 1675.312 | 1675.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32220) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32220) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32239) CPU | percent | 12 | 24.636 | 0.995 | 80.328 | 1.990 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32239) rss_mb | MB | 13 | 360.706 | 163.125 | 396.066 | 396.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32239) main thread run-queue wait | percent | 12 | 1.591 | 0.002 | 7.191 | 0.006 | 0.192663 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32239) vms_mb | MB | 13 | 8883.761 | 1572.469 | 10206.379 | 10206.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32260) CPU | percent | 1 | 70.514 | 70.514 | 70.514 | 70.514 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32260) rss_mb | MB | 2 | 235.082 | 174.727 | 295.438 | 295.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32260) main thread run-queue wait | percent | 1 | 11.346 | 11.346 | 11.346 | 11.346 | 0.114239 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32260) vms_mb | MB | 2 | 1635.971 | 1581.973 | 1689.969 | 1689.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32286) CPU | percent | 15 | 16.339 | 0.994 | 69.495 | 2.984 | 2.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32286) rss_mb | MB | 16 | 381.480 | 279.918 | 399.465 | 399.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32286) main thread run-queue wait | percent | 15 | 2.177 | 0.003 | 13.337 | 0.010 | 0.329025 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32286) vms_mb | MB | 16 | 9664.357 | 1675.082 | 10212.855 | 10212.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32304) CPU | percent | 1 | 57.552 | 57.552 | 57.552 | 57.552 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32304) rss_mb | MB | 2 | 229.652 | 184.867 | 274.438 | 274.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32304) main thread run-queue wait | percent | 1 | 13.210 | 13.210 | 13.210 | 13.210 | 0.133133 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32304) vms_mb | MB | 2 | 1631.389 | 1592.973 | 1669.805 | 1669.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32334) CPU | percent | 13 | 25.055 | 0.995 | 90.430 | 0.995 | 3.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32334) rss_mb | MB | 14 | 350.596 | 0.000 | 400.172 | 400.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32334) main thread run-queue wait | percent | 13 | 3.196 | 0.003 | 15.388 | 0.008 | 0.418731 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32334) vms_mb | MB | 14 | 8867.376 | 160.145 | 10210.715 | 10210.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32353) CPU | percent | 1 | 56.518 | 56.518 | 56.518 | 56.518 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32353) rss_mb | MB | 2 | 227.838 | 186.328 | 269.348 | 269.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32353) main thread run-queue wait | percent | 1 | 9.095 | 9.095 | 9.095 | 9.095 | 0.091723 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32353) vms_mb | MB | 2 | 1629.258 | 1593.723 | 1664.793 | 1664.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32383) CPU | percent | 12 | 22.826 | 0.994 | 70.586 | 7.952 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32383) rss_mb | MB | 13 | 372.053 | 238.328 | 398.535 | 398.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32383) main thread run-queue wait | percent | 12 | 2.839 | 0.001 | 19.333 | 0.019 | 0.344316 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32383) vms_mb | MB | 13 | 8897.673 | 1638.750 | 10216.309 | 10216.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32402) CPU | percent | 1 | 55.288 | 55.288 | 55.288 | 55.288 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32402) rss_mb | MB | 2 | 230.482 | 188.992 | 271.973 | 271.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32402) main thread run-queue wait | percent | 1 | 14.294 | 14.294 | 14.294 | 14.294 | 0.144783 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32402) vms_mb | MB | 2 | 1630.600 | 1594.473 | 1666.727 | 1666.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32412) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32412) vms_mb | MB | 1 | 0.129 | 0.129 | 0.129 | 0.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32431) CPU | percent | 17 | 18.047 | 0.994 | 74.547 | 1.989 | 3.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32431) rss_mb | MB | 18 | 374.549 | 170.312 | 402.051 | 402.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32431) main thread run-queue wait | percent | 17 | 1.410 | 0.002 | 10.117 | 0.002 | 0.241882 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32431) vms_mb | MB | 18 | 9257.537 | 1579.219 | 10214.652 | 10214.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32473) CPU | percent | 1 | 70.256 | 70.256 | 70.256 | 70.256 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32473) rss_mb | MB | 2 | 222.457 | 155.711 | 289.203 | 289.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32473) main thread run-queue wait | percent | 1 | 16.114 | 16.114 | 16.114 | 16.114 | 0.162842 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32473) vms_mb | MB | 2 | 1591.508 | 1499.469 | 1683.547 | 1683.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32497) CPU | percent | 14 | 21.188 | 0.994 | 62.540 | 2.982 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32497) rss_mb | MB | 15 | 374.928 | 220.172 | 401.750 | 401.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32497) main thread run-queue wait | percent | 14 | 2.483 | 0.002 | 15.343 | 0.004 | 0.350590 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32497) vms_mb | MB | 15 | 9066.764 | 1624.289 | 10214.039 | 10214.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32516) CPU | percent | 1 | 55.531 | 55.531 | 55.531 | 55.531 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32516) rss_mb | MB | 2 | 165.291 | 101.297 | 229.285 | 229.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32516) main thread run-queue wait | percent | 1 | 17.106 | 17.106 | 17.106 | 17.106 | 0.172500 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32516) vms_mb | MB | 2 | 1457.785 | 1283.695 | 1631.875 | 1631.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32524) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32524) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32525) rss_mb | MB | 1 | 9.891 | 9.891 | 9.891 | 9.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32525) vms_mb | MB | 1 | 13.734 | 13.734 | 13.734 | 13.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32549) CPU | percent | 13 | 20.699 | 0.994 | 67.571 | 0.995 | 2.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32549) rss_mb | MB | 14 | 370.783 | 261.121 | 392.531 | 392.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32549) main thread run-queue wait | percent | 13 | 2.994 | 0.001 | 17.963 | 0.005 | 0.398107 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32549) vms_mb | MB | 14 | 9583.968 | 1656.457 | 10212.594 | 10212.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32568) CPU | percent | 1 | 57.389 | 57.389 | 57.389 | 57.389 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32568) rss_mb | MB | 2 | 212.318 | 169.258 | 255.379 | 255.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32568) main thread run-queue wait | percent | 1 | 18.281 | 18.281 | 18.281 | 18.281 | 0.184757 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32568) vms_mb | MB | 2 | 1615.045 | 1578.973 | 1651.117 | 1651.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32599) CPU | percent | 12 | 22.508 | 0.994 | 74.437 | 8.951 | 2.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32599) rss_mb | MB | 13 | 372.317 | 229.270 | 399.613 | 399.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32599) main thread run-queue wait | percent | 12 | 2.421 | 0.003 | 20.327 | 0.022 | 0.292696 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32599) vms_mb | MB | 13 | 8897.386 | 1636.039 | 10216.840 | 10216.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32620) CPU | percent | 1 | 57.545 | 57.545 | 57.545 | 57.545 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32620) rss_mb | MB | 2 | 236.479 | 194.926 | 278.031 | 278.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32620) main thread run-queue wait | percent | 1 | 15.692 | 15.692 | 15.692 | 15.692 | 0.158161 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32620) vms_mb | MB | 2 | 1643.887 | 1614.973 | 1672.801 | 1672.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32648) CPU | percent | 13 | 22.702 | 1.986 | 76.374 | 1.989 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32648) rss_mb | MB | 14 | 376.345 | 259.812 | 399.887 | 399.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32648) main thread run-queue wait | percent | 13 | 3.244 | 0.005 | 16.513 | 0.009 | 0.427266 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32648) vms_mb | MB | 14 | 8987.858 | 1656.250 | 10214.293 | 10214.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32670) CPU | percent | 1 | 57.062 | 57.062 | 57.062 | 57.062 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32670) rss_mb | MB | 2 | 209.381 | 171.727 | 247.035 | 247.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32670) main thread run-queue wait | percent | 1 | 16.856 | 16.856 | 16.856 | 16.856 | 0.171336 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32670) vms_mb | MB | 2 | 1611.271 | 1579.973 | 1642.570 | 1642.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32698) CPU | percent | 13 | 24.540 | 1.986 | 73.345 | 10.933 | 3.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32698) rss_mb | MB | 14 | 371.336 | 235.203 | 396.293 | 396.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32698) main thread run-queue wait | percent | 13 | 2.470 | 0.004 | 14.639 | 0.027 | 0.347909 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32698) vms_mb | MB | 14 | 8986.741 | 1636.023 | 10213.230 | 10213.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — env (PID 32711) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — env (PID 32711) vms_mb | MB | 1 | 0.418 | 0.418 | 0.418 | 0.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git (PID 32720) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git (PID 32720) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32724) CPU | percent | 1 | 55.231 | 55.231 | 55.231 | 55.231 | 0.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32724) rss_mb | MB | 2 | 238.807 | 197.012 | 280.602 | 280.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32724) main thread run-queue wait | percent | 1 | 20.573 | 20.573 | 20.573 | 20.573 | 0.238390 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32724) vms_mb | MB | 2 | 1646.508 | 1616.965 | 1676.051 | 1676.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 32743) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — git rev-parse (PID 32743) vms_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32746) CPU | percent | 13 | 28.705 | 0.995 | 89.217 | 6.964 | 3.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32746) rss_mb | MB | 14 | 361.448 | 161.137 | 397.988 | 397.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32746) main thread run-queue wait | percent | 13 | 1.217 | 0.002 | 9.501 | 0.224 | 0.159358 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32746) vms_mb | MB | 14 | 8362.751 | 1317.719 | 10213.684 | 10213.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32777) rss_mb | MB | 1 | 167.016 | 167.016 | 167.016 | 167.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32777) vms_mb | MB | 1 | 1577.973 | 1577.973 | 1577.973 | 1577.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32873) CPU | percent | 12 | 24.715 | 0.993 | 74.373 | 1.990 | 3.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32873) rss_mb | MB | 13 | 368.163 | 186.301 | 399.094 | 399.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32873) main thread run-queue wait | percent | 12 | 2.478 | 0.001 | 13.796 | 0.001 | 0.302379 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32873) vms_mb | MB | 13 | 8887.918 | 1593.469 | 10214.473 | 10214.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32892) CPU | percent | 1 | 53.429 | 53.429 | 53.429 | 53.429 | 0.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32892) rss_mb | MB | 2 | 214.600 | 169.879 | 259.320 | 259.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32892) main thread run-queue wait | percent | 1 | 11.824 | 11.824 | 11.824 | 11.824 | 0.119505 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32892) vms_mb | MB | 2 | 1616.914 | 1578.723 | 1655.105 | 1655.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32904) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32904) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32905) rss_mb | MB | 1 | 8.676 | 8.676 | 8.676 | 8.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32905) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 32913) rss_mb | MB | 1 | 2.270 | 2.270 | 2.270 | 2.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tar (PID 32913) vms_mb | MB | 1 | 3.730 | 3.730 | 3.730 | 3.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 32914) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — gzip (PID 32914) vms_mb | MB | 1 | 3.273 | 3.273 | 3.273 | 3.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32920) CPU | percent | 14 | 21.637 | 0.994 | 84.431 | 1.988 | 3.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32920) rss_mb | MB | 15 | 358.084 | 44.852 | 398.145 | 398.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32920) main thread run-queue wait | percent | 14 | 1.129 | 0.003 | 7.721 | 0.004 | 0.161004 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32920) vms_mb | MB | 15 | 9030.936 | 1174.262 | 10213.387 | 10213.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32945) CPU | percent | 1 | 61.500 | 61.500 | 61.500 | 61.500 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32945) rss_mb | MB | 2 | 241.592 | 188.070 | 295.113 | 295.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32945) main thread run-queue wait | percent | 1 | 8.113 | 8.113 | 8.113 | 8.113 | 0.083109 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32945) vms_mb | MB | 2 | 1641.846 | 1593.973 | 1689.719 | 1689.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32953) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32953) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32954) rss_mb | MB | 1 | 10.344 | 10.344 | 10.344 | 10.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 32954) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32969) CPU | percent | 12 | 20.855 | 0.994 | 69.618 | 4.971 | 2.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32969) rss_mb | MB | 13 | 373.481 | 252.148 | 397.156 | 397.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32969) main thread run-queue wait | percent | 12 | 2.155 | 0.002 | 22.679 | 0.028 | 0.260909 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32969) vms_mb | MB | 13 | 9529.600 | 1648.543 | 10213.613 | 10213.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32992) CPU | percent | 1 | 41.615 | 41.615 | 41.615 | 41.615 | 0.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32992) rss_mb | MB | 2 | 148.680 | 84.602 | 212.758 | 212.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32992) main thread run-queue wait | percent | 1 | 15.560 | 15.560 | 15.560 | 15.560 | 0.157039 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 32992) vms_mb | MB | 2 | 1453.092 | 1283.695 | 1622.488 | 1622.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32999) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 32999) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33000) rss_mb | MB | 1 | 7.645 | 7.645 | 7.645 | 7.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33000) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33013) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33013) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33014) rss_mb | MB | 1 | 7.797 | 7.797 | 7.797 | 7.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33014) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33018) CPU | percent | 19 | 16.981 | 0.994 | 81.454 | 6.952 | 3.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33018) rss_mb | MB | 20 | 377.130 | 166.379 | 401.805 | 401.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33018) main thread run-queue wait | percent | 19 | 1.529 | 0.003 | 13.601 | 0.013 | 0.293456 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33018) vms_mb | MB | 20 | 9349.594 | 1573.719 | 10215.637 | 10215.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33040) CPU | percent | 1 | 57.231 | 57.231 | 57.231 | 57.231 | 0.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33040) rss_mb | MB | 2 | 244.789 | 194.957 | 294.621 | 294.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33040) main thread run-queue wait | percent | 1 | 14.586 | 14.586 | 14.586 | 14.586 | 0.147816 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33040) vms_mb | MB | 2 | 1652.135 | 1614.973 | 1689.297 | 1689.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33050) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33050) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33051) rss_mb | MB | 1 | 7.320 | 7.320 | 7.320 | 7.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33051) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33069) CPU | percent | 14 | 20.789 | 0.995 | 69.564 | 7.959 | 2.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33069) rss_mb | MB | 15 | 372.279 | 188.996 | 401.578 | 401.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33069) main thread run-queue wait | percent | 14 | 2.251 | 0.002 | 13.316 | 0.024 | 0.317462 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33069) vms_mb | MB | 15 | 9066.033 | 1593.969 | 10213.680 | 10213.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33090) CPU | percent | 1 | 60.515 | 60.515 | 60.515 | 60.515 | 0.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33090) rss_mb | MB | 2 | 222.861 | 175.441 | 270.281 | 270.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33090) main thread run-queue wait | percent | 1 | 10.998 | 10.998 | 10.998 | 10.998 | 0.110866 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33090) vms_mb | MB | 2 | 1627.895 | 1590.223 | 1665.566 | 1665.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33102) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33102) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33103) rss_mb | MB | 1 | 7.676 | 7.676 | 7.676 | 7.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33103) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33119) CPU | percent | 7 | 33.119 | 3.979 | 75.584 | 11.938 | 2.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33119) rss_mb | MB | 8 | 364.607 | 272.516 | 395.586 | 395.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33119) main thread run-queue wait | percent | 7 | 1.835 | 0.008 | 7.806 | 0.038 | 0.130507 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33119) vms_mb | MB | 8 | 9120.733 | 1667.754 | 10214.953 | 10214.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33144) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33144) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33145) rss_mb | MB | 1 | 10.562 | 10.562 | 10.562 | 10.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33145) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33150) rss_mb | MB | 1 | 168.383 | 168.383 | 168.383 | 168.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33150) vms_mb | MB | 1 | 1578.473 | 1578.473 | 1578.473 | 1578.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33169) CPU | percent | 18 | 16.542 | 0.994 | 69.463 | 4.971 | 3.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33169) rss_mb | MB | 19 | 376.172 | 217.242 | 394.703 | 394.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33169) main thread run-queue wait | percent | 18 | 0.809 | 0.006 | 7.135 | 0.012 | 0.146764 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33169) vms_mb | MB | 19 | 9312.389 | 1623.293 | 10215.512 | 10215.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 33182) rss_mb | MB | 1 | 2.914 | 2.914 | 2.914 | 2.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 33182) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 33183) rss_mb | MB | 1 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash env (PID 33183) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33190) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33190) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33191) rss_mb | MB | 1 | 10.262 | 10.262 | 10.262 | 10.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33191) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33202) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33202) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33203) rss_mb | MB | 1 | 7.602 | 7.602 | 7.602 | 7.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33203) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33207) CPU | percent | 12 | 29.538 | 1.984 | 86.327 | 4.973 | 3.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33207) rss_mb | MB | 13 | 346.688 | 26.344 | 399.969 | 399.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33207) main thread run-queue wait | percent | 12 | 1.699 | 0.002 | 7.279 | 0.002 | 0.205346 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33207) vms_mb | MB | 13 | 8137.092 | 165.848 | 10215.309 | 10215.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33236) CPU | percent | 1 | 80.502 | 80.502 | 80.502 | 80.502 | 0.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33236) rss_mb | MB | 2 | 234.209 | 172.465 | 295.953 | 295.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33236) main thread run-queue wait | percent | 1 | 10.837 | 10.837 | 10.837 | 10.837 | 0.109037 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33236) vms_mb | MB | 2 | 1635.092 | 1579.973 | 1690.211 | 1690.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33255) CPU | percent | 13 | 25.721 | 1.989 | 87.222 | 3.976 | 3.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33255) rss_mb | MB | 14 | 354.165 | 47.117 | 404.105 | 404.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33255) main thread run-queue wait | percent | 13 | 3.287 | 0.005 | 19.982 | 0.018 | 0.432765 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33255) vms_mb | MB | 14 | 8923.227 | 1238.512 | 10181.730 | 10181.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33274) CPU | percent | 1 | 61.404 | 61.404 | 61.404 | 61.404 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33274) rss_mb | MB | 2 | 218.330 | 175.664 | 260.996 | 260.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33274) main thread run-queue wait | percent | 1 | 12.765 | 12.765 | 12.765 | 12.765 | 0.128887 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33274) vms_mb | MB | 2 | 1623.016 | 1589.973 | 1656.059 | 1656.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33292) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33292) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33293) rss_mb | MB | 1 | 9.297 | 9.297 | 9.297 | 9.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33293) vms_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33304) CPU | percent | 148 | 5.495 | 0.991 | 80.357 | 1.988 | 8.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33304) rss_mb | MB | 149 | 397.485 | 171.535 | 416.668 | 387.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33304) main thread run-queue wait | percent | 148 | 1.650 | 0.001 | 26.316 | 0.010 | 2.465168 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33304) vms_mb | MB | 149 | 10098.797 | 1579.469 | 10228.473 | 10203.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33321) CPU | percent | 1 | 61.489 | 61.489 | 61.489 | 61.489 | 0.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33321) rss_mb | MB | 2 | 250.568 | 206.074 | 295.062 | 295.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33321) main thread run-queue wait | percent | 1 | 11.949 | 11.949 | 11.949 | 11.949 | 0.120479 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33321) vms_mb | MB | 2 | 1654.369 | 1618.996 | 1689.742 | 1689.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33353) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33353) rss_mb | MB | 2 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33353) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33353) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33354) CPU | percent | 1 | 131.865 | 131.865 | 131.865 | 131.865 | 1.330000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33354) rss_mb | MB | 2 | 1102.213 | 233.352 | 1971.074 | 1971.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33354) main thread run-queue wait | percent | 1 | 18.309 | 18.309 | 18.309 | 18.309 | 0.184670 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33354) vms_mb | MB | 2 | 1447.199 | 700.855 | 2193.543 | 2193.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33376) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33376) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33377) rss_mb | MB | 1 | 9.668 | 9.668 | 9.668 | 9.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33377) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33405) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33405) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33406) rss_mb | MB | 1 | 7.922 | 7.922 | 7.922 | 7.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33406) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33412) rss_mb | MB | 1 | 15.770 | 15.770 | 15.770 | 15.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33412) vms_mb | MB | 1 | 208.867 | 208.867 | 208.867 | 208.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33421) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33421) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33422) rss_mb | MB | 1 | 10.129 | 10.129 | 10.129 | 10.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33422) vms_mb | MB | 1 | 14.059 | 14.059 | 14.059 | 14.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33431) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33431) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33432) rss_mb | MB | 1 | 6.859 | 6.859 | 6.859 | 6.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33432) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33439) CPU | percent | 1 | 166.511 | 166.511 | 166.511 | 166.511 | 1.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33439) rss_mb | MB | 2 | 53.504 | 24.855 | 82.152 | 82.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33439) main thread run-queue wait | percent | 1 | 51.938 | 51.938 | 51.938 | 51.938 | 0.524027 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33439) vms_mb | MB | 2 | 258.607 | 217.109 | 300.105 | 300.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33450) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33450) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33451) rss_mb | MB | 1 | 10.629 | 10.629 | 10.629 | 10.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33451) vms_mb | MB | 1 | 15.270 | 15.270 | 15.270 | 15.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33464) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33464) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33465) rss_mb | MB | 1 | 7.195 | 7.195 | 7.195 | 7.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33465) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33471) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33471) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33472) rss_mb | MB | 1 | 7.449 | 7.449 | 7.449 | 7.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33472) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33479) CPU | percent | 2 | 155.350 | 138.762 | 171.939 | 171.939 | 3.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33479) rss_mb | MB | 3 | 44.431 | 9.695 | 89.379 | 34.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33479) main thread run-queue wait | percent | 2 | 45.921 | 37.322 | 54.520 | 54.520 | 0.925113 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33479) vms_mb | MB | 3 | 190.590 | 13.500 | 307.590 | 250.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33493) rss_mb | MB | 1 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33493) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33494) rss_mb | MB | 1 | 9.297 | 9.297 | 9.297 | 9.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33494) vms_mb | MB | 1 | 13.410 | 13.410 | 13.410 | 13.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33506) CPU | percent | 1 | 174.432 | 174.432 | 174.432 | 174.432 | 1.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33506) rss_mb | MB | 2 | 89.211 | 88.398 | 90.023 | 90.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33506) main thread run-queue wait | percent | 1 | 57.121 | 57.121 | 57.121 | 57.121 | 0.576341 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33506) vms_mb | MB | 2 | 307.586 | 307.586 | 307.586 | 307.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33521) CPU | percent | 38 | 10.703 | 0.992 | 67.541 | 8.952 | 4.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33521) rss_mb | MB | 39 | 389.710 | 229.020 | 401.574 | 401.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33521) main thread run-queue wait | percent | 38 | 3.744 | 0.001 | 41.309 | 0.016 | 1.441228 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33521) vms_mb | MB | 39 | 9773.976 | 1632.031 | 10216.941 | 10216.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — env (PID 33535) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — env (PID 33535) vms_mb | MB | 1 | 0.418 | 0.418 | 0.418 | 0.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33541) CPU | percent | 1 | 52.372 | 52.372 | 52.372 | 52.372 | 0.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33541) rss_mb | MB | 2 | 217.146 | 174.836 | 259.457 | 259.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33541) main thread run-queue wait | percent | 1 | 10.418 | 10.418 | 10.418 | 10.418 | 0.105424 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33541) vms_mb | MB | 2 | 1618.777 | 1581.973 | 1655.582 | 1655.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33553) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33553) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33554) rss_mb | MB | 1 | 8.609 | 8.609 | 8.609 | 8.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33554) vms_mb | MB | 1 | 13.184 | 13.184 | 13.184 | 13.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33649) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33649) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33650) rss_mb | MB | 1 | 21.609 | 21.609 | 21.609 | 21.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33650) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33668) CPU | percent | 2 | 172.962 | 172.341 | 173.583 | 173.583 | 3.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33668) rss_mb | MB | 3 | 90.077 | 89.051 | 90.590 | 90.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33668) main thread run-queue wait | percent | 2 | 53.129 | 49.780 | 56.478 | 56.478 | 1.077768 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33668) vms_mb | MB | 3 | 307.404 | 307.402 | 307.406 | 307.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33683) CPU | percent | 24 | 15.550 | 0.991 | 80.560 | 0.995 | 3.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33683) rss_mb | MB | 25 | 375.558 | 187.293 | 392.379 | 392.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33683) main thread run-queue wait | percent | 24 | 9.463 | 0.002 | 42.876 | 0.002 | 2.291631 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33683) vms_mb | MB | 25 | 9524.662 | 1593.969 | 10213.707 | 10213.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33713) rss_mb | MB | 1 | 187.250 | 187.250 | 187.250 | 187.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33713) vms_mb | MB | 1 | 1593.973 | 1593.973 | 1593.973 | 1593.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33727) CPU | percent | 2 | 171.884 | 167.443 | 176.325 | 167.443 | 3.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33727) rss_mb | MB | 3 | 89.467 | 88.090 | 90.172 | 90.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33727) main thread run-queue wait | percent | 2 | 52.828 | 49.847 | 55.810 | 55.810 | 1.066491 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33727) vms_mb | MB | 3 | 307.401 | 307.398 | 307.402 | 307.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33734) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33734) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33735) rss_mb | MB | 1 | 9.543 | 9.543 | 9.543 | 9.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33735) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33742) CPU | percent | 3 | 157.060 | 130.148 | 172.016 | 172.016 | 4.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33742) rss_mb | MB | 4 | 68.017 | 2.879 | 90.258 | 90.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33742) main thread run-queue wait | percent | 3 | 46.693 | 38.451 | 51.492 | 51.492 | 1.409187 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33742) vms_mb | MB | 4 | 231.513 | 3.848 | 307.402 | 307.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33743) rss_mb | MB | 1 | 8.801 | 8.801 | 8.801 | 8.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33743) vms_mb | MB | 1 | 13.164 | 13.164 | 13.164 | 13.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33757) CPU | percent | 18 | 19.450 | 0.990 | 71.392 | 7.958 | 3.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33757) rss_mb | MB | 19 | 374.082 | 229.434 | 395.672 | 395.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33757) main thread run-queue wait | percent | 18 | 8.124 | 0.003 | 46.289 | 0.013 | 1.474507 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33757) vms_mb | MB | 19 | 9306.995 | 1632.277 | 10213.488 | 10213.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33777) CPU | percent | 1 | 55.489 | 55.489 | 55.489 | 55.489 | 0.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33777) rss_mb | MB | 2 | 217.912 | 174.969 | 260.855 | 260.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33777) main thread run-queue wait | percent | 1 | 11.140 | 11.140 | 11.140 | 11.140 | 0.112426 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33777) vms_mb | MB | 2 | 1623.389 | 1589.723 | 1657.055 | 1657.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33803) CPU | percent | 3 | 157.220 | 123.923 | 176.205 | 171.533 | 4.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33803) rss_mb | MB | 4 | 68.186 | 2.879 | 90.383 | 90.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33803) main thread run-queue wait | percent | 3 | 45.864 | 33.789 | 53.407 | 50.397 | 1.388620 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — bash (PID 33803) vms_mb | MB | 4 | 231.518 | 3.848 | 307.410 | 307.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33804) rss_mb | MB | 1 | 5.352 | 5.352 | 5.352 | 5.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — python stdin (PID 33804) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33825) CPU | percent | 47 | 9.865 | 0.991 | 61.669 | 7.949 | 4.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33825) rss_mb | MB | 48 | 387.576 | 220.445 | 399.148 | 399.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33825) main thread run-queue wait | percent | 47 | 3.249 | 0.002 | 38.244 | 0.031 | 1.537733 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33825) vms_mb | MB | 48 | 9857.814 | 1623.801 | 10219.363 | 10219.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33842) CPU | percent | 1 | 56.462 | 56.462 | 56.462 | 56.462 | 0.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33842) rss_mb | MB | 2 | 146.686 | 64.328 | 229.043 | 229.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33842) main thread run-queue wait | percent | 1 | 18.668 | 18.668 | 18.668 | 18.668 | 0.188457 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — kimi (PID 33842) vms_mb | MB | 2 | 1437.355 | 1238.609 | 1636.102 | 1636.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33850) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33850) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33851) rss_mb | MB | 1 | 7.078 | 7.078 | 7.078 | 7.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — lifecycle_hook.py (PID 33851) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33867) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33867) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33868) rss_mb | MB | 1 | 8.805 | 8.805 | 8.805 | 8.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33868) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33877) CPU | percent | 3 | 167.528 | 163.946 | 171.521 | 167.119 | 5.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33877) rss_mb | MB | 4 | 85.154 | 22.613 | 106.348 | 106.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33877) main thread run-queue wait | percent | 3 | 47.534 | 43.458 | 50.194 | 50.194 | 1.435674 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — build_final.py (PID 33877) vms_mb | MB | 4 | 296.391 | 215.258 | 323.438 | 323.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33889) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33889) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33890) rss_mb | MB | 1 | 18.883 | 18.883 | 18.883 | 18.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33890) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 33897) CPU | percent | 1 | 64.536 | 64.536 | 64.536 | 64.536 | 0.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 33897) rss_mb | MB | 2 | 44.348 | 25.035 | 63.660 | 63.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 33897) main thread run-queue wait | percent | 1 | 0.049 | 0.049 | 0.049 | 0.049 | 0.000497 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 33897) vms_mb | MB | 2 | 54.158 | 30.359 | 77.957 | 77.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 33906) CPU | percent | 1 | 51.604 | 51.604 | 51.604 | 51.604 | 0.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 33906) rss_mb | MB | 2 | 52.676 | 39.344 | 66.008 | 66.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 33906) main thread run-queue wait | percent | 1 | 0.302 | 0.302 | 0.302 | 0.302 | 0.003040 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — tool.py (PID 33906) vms_mb | MB | 2 | 64.051 | 47.793 | 80.309 | 80.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33915) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — sh (PID 33915) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33916) rss_mb | MB | 1 | 21.453 | 21.453 | 21.453 | 21.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-kimi_0000_0000 — agpolicy_hook.py (PID 33916) vms_mb | MB | 1 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| docker commit (PID 33951) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 33951) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 33951) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 33951) rss_mb | MB | 22 | 29.309 | 29.309 | 29.309 | 29.309 | n/a | n/a |
| docker commit (PID 33951) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 33951) vms_mb | MB | 22 | 1835.016 | 1835.016 | 1835.016 | 1835.016 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 CPU | percent | 4845 | 79.563 | 0.000 | 232.584 | 0.000 | 3888.789032 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 4845 | 1.772 | 0.000 | 50.316 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 4845 | 2.882 | 0.000 | 69.773 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io_psi_full_pct | percent of wall time stalled | 4845 | 0.067 | 0.000 | 44.608 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io_psi_some_pct | percent of wall time stalled | 4845 | 0.079 | 0.000 | 44.619 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io read MB/s | MB/s | 4845 | 0.035 | 0.000 | 90.655 | 0.000 | 169.703125 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 io write MB/s | MB/s | 4845 | 0.143 | 0.000 | 7.967 | 0.000 | 702.023438 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory | MB | 4846 | 607.689 | 32.523 | 4385.340 | 317.641 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory_psi_full_pct | percent of wall time stalled | 4845 | 0.008 | 0.000 | 18.143 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 memory_psi_some_pct | percent of wall time stalled | 4845 | 0.008 | 0.000 | 18.143 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 net rx MB/s | MB/s | 4845 | 0.092 | 0.000 | 2.169 | 0.000 | 447.722233 MB | n/a |
| sandbox sandbox_agent_lsb-kimi_0000_0000 net tx MB/s | MB/s | 4845 | 0.001 | 0.000 | 0.014 | 0.000 | 5.963037 MB | n/a |
| workload total CPU | percent | 4853 | 6.315 | 1.368 | 150.156 | 1.534 | 309.836975 CPU seconds | n/a |
| workload total memory | MB | 4854 | 9577.354 | 8563.254 | 10023.738 | 9689.426 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
