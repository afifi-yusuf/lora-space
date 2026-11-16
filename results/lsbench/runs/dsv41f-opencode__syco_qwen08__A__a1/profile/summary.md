# agprof summary

- Duration: **1440.175 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **113 calls**, 97 succeeded, 16 failed, 0 interrupted, n/a reported retries, 722.542 s total wait
- Tools: **95/95 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **136172** at 1.972 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1438473.767 / 1438473.767 ms |
| LLM latency p50 / p95 | 5328.636 / 15896.526 ms |
| LLM TTFT p50 / p95 | 2257.020 / 7810.718 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 113 total, 97 succeeded, 16 failed, 0 interrupted |
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
| bash | 89/89 | 89 | 0 | 0 | n/a | n/a |
| read | 4/4 | 4 | 0 | 0 | n/a | n/a |
| write | 2/2 | 2 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.801% | 117.135% | 83.907 s | 5623.596 MB | 5830.328 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| tail | 20716 | sandbox_agent_lsb-opencode_0000_0000 | 1422 | 0.001% | 0.995% | 0.020 s | 1.484 MB | 1.484 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 20808 | sandbox_agent_lsb-opencode_0000_0000 | 1422 | 33.941% | 100.314% | 485.750 s | 117.335 MB | 159.379 MB | 899.430 MB | 904.906 MB | n/a MB | n/a MB |
| lsb_grid_worker | 19988 |  | 1430 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 20295 |  | 1430 | 4.493% | 116.146% | 65.070 s | 2992.138 MB | 3177.871 MB | 15989.410 MB | 16237.227 MB | 19.781250 MB | 273.269531 MB |
| vllm | 20300 |  | 1430 | 0.158% | 11.877% | 2.270 s | 1803.887 MB | 1804.367 MB | 11040.111 MB | 11043.586 MB | 0.000000 MB | 0.035156 MB |
| python3 | 20814 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 99.816% | 99.816% | 1.010 s | 52.812 MB | 81.016 MB | 63.352 MB | 94.281 MB | n/a MB | n/a MB |
| docker-init | 20684 | sandbox_agent_lsb-opencode_0000_0000 | 1422 | 0.001% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 20403 |  | 1430 | 1.139% | 48.498% | 16.390 s | 2315.861 MB | 2322.008 MB | 21203.227 MB | 21203.242 MB | 0.132812 MB | 0.007812 MB |
| python | 20402 |  | 1430 | 0.000% | 0.000% | 0.000 s | 12.184 MB | 12.184 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| opencode | 20822 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 52.848 MB | 52.848 MB | 6431.648 MB | 6431.648 MB | n/a MB | n/a MB |
| opencode | 20835 | sandbox_agent_lsb-opencode_0000_0000 | 1080 | 5.707% | 129.152% | 62.010 s | 751.598 MB | 934.383 MB | 16536.236 MB | 16750.156 MB | n/a MB | n/a MB |
| head | 20940 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.418 MB | 0.418 MB | n/a MB | n/a MB |
| bash | 20937 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.785 MB | 2.785 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| cat | 20939 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.414 MB | 0.414 MB | n/a MB | n/a MB |
| mcp.sh | 21034 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.594 MB | 2.594 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21042 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.633 MB | 9.633 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| curl | 21076 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.973 MB | 9.973 MB | 19.137 MB | 19.137 MB | n/a MB | n/a MB |
| bash | 21067 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.758 MB | 2.758 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp.sh | 21070 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.723 MB | 2.723 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| mcp.sh | 21120 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.578 MB | 2.578 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| curl | 21126 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.922 MB | 9.922 MB | 19.137 MB | 19.137 MB | n/a MB | n/a MB |
| mcp.sh | 21170 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.852 MB | 2.852 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| curl | 21176 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.812 MB | 9.812 MB | 19.137 MB | 19.137 MB | n/a MB | n/a MB |
| mcp.sh | 21254 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.773 MB | 2.773 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 21226 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.793 MB | 2.793 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21256 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.637 MB | 0.637 MB | n/a MB | n/a MB |
| mcp.sh | 21255 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| tr | 21258 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.180 MB | 1.180 MB | 2.465 MB | 2.465 MB | n/a MB | n/a MB |
| grep | 21257 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.508 MB | 1.508 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| mcp.sh | 21279 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.668 MB | 2.668 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| curl | 21285 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.750 MB | 9.750 MB | 19.137 MB | 19.137 MB | n/a MB | n/a MB |
| mcp.sh | 21329 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.723 MB | 2.723 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| curl | 21335 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.930 MB | 9.930 MB | 19.137 MB | 19.137 MB | n/a MB | n/a MB |
| mcp.sh | 21386 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.762 MB | 2.762 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21394 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.922 MB | 9.922 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| mcp.sh | 21407 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.680 MB | 2.680 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21415 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.309 MB | 1.309 MB | 15.051 MB | 15.051 MB | n/a MB | n/a MB |
| mcp2.sh | 21438 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 21439 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.238 MB | 1.238 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| curl | 21463 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.688 MB | 9.688 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| bash | 21434 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.703 MB | 2.703 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp2.sh | 21475 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.656 MB | 2.656 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 21473 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.758 MB | 2.758 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 21476 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.238 MB | 1.238 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| curl | 21483 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.770 MB | 9.770 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| python3 | 21496 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.258 MB | 14.258 MB | 208.086 MB | 208.086 MB | n/a MB | n/a MB |
| bash | 21504 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.578 MB | 2.578 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 21510 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 922.609 MB | 922.609 MB | 2367.980 MB | 2367.980 MB | n/a MB | n/a MB |
| head | 21511 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.129 MB | 1.129 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 21520 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1838.172 MB | 1838.172 MB | 2640.855 MB | 2640.855 MB | n/a MB | n/a MB |
| python3 | 21561 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.398 MB | 9.398 MB | 13.301 MB | 13.301 MB | n/a MB | n/a MB |
| mcp2.sh | 21560 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.566 MB | 2.566 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21568 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 10.047 MB | 10.047 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| bash | 21558 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21582 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.934 MB | 9.934 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| head | 21575 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.191 MB | 1.191 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 21573 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.754 MB | 2.754 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp2.sh | 21574 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.848 MB | 2.848 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 21586 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 28.609 MB | 28.609 MB | 250.309 MB | 250.309 MB | n/a MB | n/a MB |
| python3 | 21641 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.891 MB | 12.891 MB | 207.172 MB | 207.172 MB | n/a MB | n/a MB |
| bash | 21653 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.934 MB | 2.934 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 21662 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.250 MB | 7.250 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| head | 21656 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.238 MB | 1.238 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| mcp2.sh | 21655 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.566 MB | 2.566 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21663 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.688 MB | 9.688 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| python3 | 21667 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.340 MB | 13.340 MB | 207.125 MB | 207.125 MB | n/a MB | n/a MB |
| python3 | 21675 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 94.281% | 94.281% | 0.950 s | 1092.322 MB | 2160.344 MB | 1429.359 MB | 2642.715 MB | n/a MB | n/a MB |
| python3 | 21684 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 76.429% | 76.429% | 0.770 s | 526.551 MB | 1027.586 MB | 718.287 MB | 1219.102 MB | n/a MB | n/a MB |
| python3 | 21697 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 140.852% | 175.084% | 4.250 s | 791.613 MB | 1057.594 MB | 999.536 MB | 1280.895 MB | n/a MB | n/a MB |
| curl | 21716 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.805 MB | 9.805 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| bash | 21706 | sandbox_agent_lsb-opencode_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 2.844 MB | 2.844 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp2.sh | 21709 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.723 MB | 2.723 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21725 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.840 MB | 9.840 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| mcp2.sh | 21718 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.637 MB | 2.637 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp2.sh | 21727 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.574 MB | 2.574 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21734 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.934 MB | 9.934 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| curl | 21743 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.938 MB | 9.938 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| mcp2.sh | 21736 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.723 MB | 2.723 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21752 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.801 MB | 9.801 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| mcp2.sh | 21745 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.750 MB | 2.750 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21761 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.891 MB | 9.891 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| mcp2.sh | 21754 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.766 MB | 2.766 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21770 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.986 MB | 10.062 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| mcp2.sh | 21763 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.801 MB | 2.801 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21779 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.859 MB | 9.859 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| mcp2.sh | 21772 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.770 MB | 2.770 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21789 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.891 MB | 9.891 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| mcp2.sh | 21782 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.738 MB | 2.738 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 21793 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 91.348% | 91.348% | 0.920 s | 508.031 MB | 1008.367 MB | 605.471 MB | 1199.008 MB | n/a MB | n/a MB |
| python3 | 21800 | sandbox_agent_lsb-opencode_0000_0000 | 20 | 168.425% | 174.645% | 32.250 s | 956.846 MB | 1057.559 MB | 1226.793 MB | 1280.453 MB | n/a MB | n/a MB |
| python3 | 21812 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 148.583% | 172.082% | 2.990 s | 710.646 MB | 1056.602 MB | 922.978 MB | 1278.953 MB | n/a MB | n/a MB |
| python3 | 21824 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.199 MB | 9.199 MB | 13.301 MB | 13.301 MB | n/a MB | n/a MB |
| mcp2.sh | 21823 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.777 MB | 2.777 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 21821 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.820 MB | 2.820 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21831 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.758 MB | 9.758 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| mcp2.sh | 21837 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.738 MB | 2.738 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 21847 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.828 MB | 9.828 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| python3 | 21840 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.355 MB | 9.355 MB | 13.301 MB | 13.301 MB | n/a MB | n/a MB |
| bash | 21836 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.629 MB | 2.629 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sed | 21838 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.723 MB | 1.723 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| sed | 21839 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.660 MB | 1.660 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| python3 | 21852 | sandbox_agent_lsb-opencode_0000_0000 | 54 | 170.885% | 175.337% | 91.250 s | 1043.522 MB | 1056.113 MB | 1268.295 MB | 1279.000 MB | n/a MB | n/a MB |
| python3 | 21894 | sandbox_agent_lsb-opencode_0000_0000 | 36 | 163.002% | 178.714% | 57.450 s | 1498.814 MB | 3002.746 MB | 2025.605 MB | 3227.453 MB | n/a MB | n/a MB |
| python3 | 21911 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 641.145 MB | 641.145 MB | 1670.898 MB | 1670.898 MB | n/a MB | n/a MB |
| curl | 21932 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.969 MB | 9.969 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| head | 21925 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.230 MB | 1.230 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 21922 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.656 MB | 2.656 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp2.sh | 21924 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.875 MB | 2.875 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 21936 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 27.074 MB | 27.074 MB | 250.020 MB | 250.020 MB | n/a MB | n/a MB |
| python3 | 21943 | sandbox_agent_lsb-opencode_0000_0000 | 21 | 170.085% | 174.216% | 34.280 s | 1016.276 MB | 1057.426 MB | 1252.876 MB | 1280.473 MB | n/a MB | n/a MB |
| python3 | 21954 | sandbox_agent_lsb-opencode_0000_0000 | 60 | 153.297% | 172.739% | 91.170 s | 2012.980 MB | 3002.371 MB | 3144.750 MB | 3227.418 MB | n/a MB | n/a MB |
| timeout | 21972 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.355 MB | 1.355 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 21973 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 167.256% | 175.370% | 13.470 s | 1195.747 MB | 1382.582 MB | 1460.145 MB | 1604.770 MB | n/a MB | n/a MB |
| timeout | 21982 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 21983 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 171.100% | 175.058% | 13.780 s | 1276.708 MB | 1303.008 MB | 1577.604 MB | 2156.023 MB | n/a MB | n/a MB |
| timeout | 21993 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 21994 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 165.247% | 177.285% | 5.020 s | 1004.202 MB | 1059.219 MB | 1378.108 MB | 1670.992 MB | n/a MB | n/a MB |
| python3 | 22007 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 151.869% | 174.524% | 3.060 s | 760.117 MB | 1059.086 MB | 1087.297 MB | 1280.461 MB | n/a MB | n/a MB |
| timeout | 22005 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| timeout | 22016 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 22017 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 166.169% | 174.323% | 3.350 s | 1067.315 MB | 1084.312 MB | 1572.322 MB | 2155.996 MB | n/a MB | n/a MB |
| Worker | 22029 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 247.329 MB | 736.262 MB | 5582.573 MB | 16740.023 MB | n/a MB | n/a MB |
| head | 22033 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| mcp2.sh | 22032 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.746 MB | 2.746 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 22040 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 9.691 MB | 9.691 MB | 19.145 MB | 19.145 MB | n/a MB | n/a MB |
| python3 | 22063 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 135.989% | 177.698% | 2.740 s | 709.536 MB | 1058.625 MB | 912.089 MB | 1280.492 MB | n/a MB | n/a MB |
| timeout | 22062 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.227 MB | 1.227 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| timeout | 22071 | sandbox_agent_lsb-opencode_0000_0000 | 85 | 0.000% | 0.000% | 0.000 s | 1.324 MB | 1.324 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 22072 | sandbox_agent_lsb-opencode_0000_0000 | 85 | 125.222% | 180.025% | 105.910 s | 2308.247 MB | 3224.750 MB | 3188.272 MB | 3442.715 MB | n/a MB | n/a MB |
| head | 22094 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.254 MB | 1.254 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| mcp2.sh | 22093 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.707 MB | 2.707 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 22091 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.025 MB | 2.758 MB | 3.148 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 22101 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.906 MB | 9.906 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| python3 | 22102 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2440.980 MB | 2440.980 MB | 2640.934 MB | 2640.934 MB | n/a MB | n/a MB |
| timeout | 22112 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 22114 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 105.691 MB | 105.691 MB | 700.938 MB | 700.938 MB | n/a MB | n/a MB |
| timeout | 22122 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 22123 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 158.060% | 158.060% | 1.590 s | 1034.211 MB | 1057.480 MB | 1241.215 MB | 1280.426 MB | n/a MB | n/a MB |
| timeout | 22131 | sandbox_agent_lsb-opencode_0000_0000 | 22 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 22132 | sandbox_agent_lsb-opencode_0000_0000 | 22 | 170.827% | 175.086% | 36.110 s | 1176.906 MB | 1223.566 MB | 1407.815 MB | 1445.613 MB | n/a MB | n/a MB |
| timeout | 22153 | sandbox_agent_lsb-opencode_0000_0000 | 72 | 0.000% | 0.000% | 0.000 s | 1.172 MB | 1.172 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 22154 | sandbox_agent_lsb-opencode_0000_0000 | 72 | 171.867% | 176.384% | 122.870 s | 1204.465 MB | 1223.695 MB | 1426.087 MB | 1445.598 MB | n/a MB | n/a MB |
| python3 | 22175 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 98.281% | 98.281% | 0.990 s | 517.281 MB | 1027.090 MB | 615.154 MB | 1218.363 MB | n/a MB | n/a MB |
| timeout | 22174 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| awk | 22242 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.719 MB | 1.719 MB | 3.504 MB | 3.504 MB | n/a MB | n/a MB |
| python3 | 22237 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.703 MB | 5.703 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| grep | 22240 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.398 MB | 1.398 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| mcp2.sh | 22238 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.316 MB | 1.316 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp2.sh | 22234 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.652 MB | 2.652 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sed | 22235 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.629 MB | 1.629 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| tr | 22241 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.242 MB | 1.242 MB | 2.465 MB | 2.465 MB | n/a MB | n/a MB |
| curl | 22239 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.512 MB | 9.512 MB | 18.930 MB | 18.930 MB | n/a MB | n/a MB |
| sed | 22236 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.633 MB | 1.633 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| bash | 22202 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.750 MB | 2.750 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| mcp2.sh | 22267 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.848 MB | 2.848 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 22277 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.961 MB | 9.961 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| sed | 22269 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.809 MB | 1.809 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| sed | 22268 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.762 MB | 1.762 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| python3 | 22270 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.223 MB | 9.223 MB | 13.301 MB | 13.301 MB | n/a MB | n/a MB |
| mcp2.sh | 22306 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.824 MB | 2.824 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sed | 22308 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.754 MB | 1.754 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| bash | 22305 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.625 MB | 2.625 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sed | 22307 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.668 MB | 1.668 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| python3 | 22314 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.336 MB | 9.336 MB | 13.266 MB | 13.266 MB | n/a MB | n/a MB |
| sed | 22348 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.680 MB | 1.680 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| sed | 22347 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.648 MB | 1.648 MB | 3.340 MB | 3.340 MB | n/a MB | n/a MB |
| python3 | 22354 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.098 MB | 10.098 MB | 13.312 MB | 13.312 MB | n/a MB | n/a MB |
| mcp2.sh | 22346 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.723 MB | 2.723 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 22373 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 152.042% | 170.088% | 3.060 s | 838.191 MB | 1058.656 MB | 1087.367 MB | 1280.531 MB | n/a MB | n/a MB |
| timeout | 22372 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| opencode | 22388 | sandbox_agent_lsb-opencode_0000_0000 | 302 | 10.182% | 140.255% | 30.840 s | 749.808 MB | 942.562 MB | 15529.419 MB | 16746.945 MB | n/a MB | n/a MB |
| python3 | 22435 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 172.894% | 172.894% | 1.740 s | 1041.348 MB | 1056.914 MB | 1248.881 MB | 1280.426 MB | n/a MB | n/a MB |
| timeout | 22434 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.227 MB | 1.227 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 22450 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 170.043% | 171.087% | 3.420 s | 118.724 MB | 140.016 MB | 336.415 MB | 356.082 MB | n/a MB | n/a MB |
| timeout | 22449 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 22492 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| mcp2.sh | 22520 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.625 MB | 2.625 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 22523 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.652 MB | 9.652 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| bash | 22517 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.609 MB | 2.609 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 22521 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.234 MB | 1.234 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| mcp2.sh | 22522 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.262 MB | 1.262 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| grep | 22524 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.480 MB | 1.480 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| tr | 22525 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.180 MB | 1.180 MB | 2.465 MB | 2.465 MB | n/a MB | n/a MB |
| awk | 22526 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.613 MB | 1.613 MB | 3.504 MB | 3.504 MB | n/a MB | n/a MB |
| python3 | 22539 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.336 MB | 20.336 MB | 212.074 MB | 212.074 MB | n/a MB | n/a MB |
| docker | 22649 |  | 32 | 0.000% | 0.000% | 0.000 s | 29.941 MB | 30.133 MB | 1839.001 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |
| docker | 22699 |  | 6 | 0.000% | 0.000% | 0.000 s | 31.004 MB | 31.004 MB | 1771.258 MB | 1771.258 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.319% | 100.000% | 11815.779 MB | 11870.000 MB | 29.008 W | 56.967 W | 41750.659 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-opencode_0000_0000 | 88.052% | 210.770% | 1260.209 s | 2576.444 MB | 5424.301 MB | 453.531250 MB | 1420.425781 MB | 48.347008 MB | 0.884627 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 20574 | 1440.112 | interrupted |
| harness:retire | -1 | 2.446 | interrupted |
| harness:retire | -1 | 0.296 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1438.474 | n/a | n/a | 453.531 | 1438473.767 | 1438473.767 | 1438473.767 |
| engine:execute | 1/1 | 0 | 0 | 1438.472 | 2.146 | 1436.267 | 453.531 | 1438472.265 | 1438472.265 | 1438472.265 |
| harness:attempt_rpc | 2/2 | 0 | 0 | 1396.773 | 0.058 | 1396.715 | 429.677 | 698386.559 | 698386.559 | 1051783.510 |
| harness:await_cli | 2/2 | 0 | 0 | 1353.658 | n/a | n/a | 339.334 | 676829.001 | 676829.001 | 1030695.734 |
| llm:attempt | 113/113 | 16 | 0 | 722.542 | 11.985 | 710.551 | 10.246 | 6394.177 | 5328.636 | 15896.526 |
| tool:bash | 89/89 | 0 | 0 | 492.577 | n/a | n/a | 325.614 | 5534.569 | 589.608 | 30743.539 |
| run:container_call | 13/13 | 0 | 0 | 38.237 | 0.002 | 38.234 | 0.000 | 2941.297 | 38.625 | 16258.432 |
| teardown:commit | 1/1 | 0 | 0 | 37.809 | 0.005 | 37.804 | 0.000 | 37808.668 | 37808.668 | 37808.668 |
| harness:startup_ready | 2/2 | 0 | 0 | 34.167 | n/a | n/a | 66.489 | 17083.736 | 17083.736 | 17461.486 |
| sandbox:commit | 1/1 | 0 | 0 | 31.822 | 0.003 | 31.819 | 0.000 | 31821.682 | 31821.682 | 31821.682 |
| checkpoint.total | 1/1 | 0 | 0 | 31.822 | 0.002 | 31.819 | 0.000 | 31821.511 | 31821.511 | 31821.511 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 31.821 | 0.002 | 31.819 | 0.000 | 31821.367 | 31821.367 | 31821.367 |
| sandbox:stop | 1/1 | 0 | 0 | 5.987 | 0.002 | 5.985 | 0.000 | 5986.671 | 5986.671 | 5986.671 |
| harness:submit | 2/2 | 0 | 0 | 3.667 | n/a | n/a | 0.504 | 1833.664 | 1833.664 | 2575.564 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.149 | 0.753 | 2.396 | 22.602 | 3149.373 | 3149.373 | 3149.373 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.149 | 0.753 | 2.396 | 22.596 | 3149.122 | 3149.122 | 3149.122 |
| syscall:connect | 850/850 | 0 | 0 | 1.888 | n/a | n/a | 0.763 | 2.221 | 1.787 | 4.340 |
| syscall:sendto | 690/690 | 0 | 0 | 1.661 | n/a | n/a | 0.322 | 2.407 | 1.604 | 4.680 |
| syscall:execve | 735/735 | 0 | 0 | 1.601 | n/a | n/a | 0.262 | 2.179 | 1.447 | 6.348 |
| sandbox:start | 1/1 | 0 | 0 | 0.359 | 0.002 | 0.357 | 0.000 | 359.433 | 359.433 | 359.433 |
| runtime.container_create | 1/1 | 0 | 0 | 0.359 | 0.002 | 0.357 | 0.000 | 359.292 | 359.292 | 359.292 |
| sandbox:create | 1/1 | 0 | 0 | 0.356 | 0.267 | 0.089 | 0.000 | 355.885 | 355.885 | 355.885 |
| agency:services_close | 1/1 | 0 | 0 | 0.204 | 0.002 | 0.202 | 0.000 | 203.553 | 203.553 | 203.553 |
| tool:read | 4/4 | 0 | 0 | 0.140 | n/a | n/a | 0.000 | 35.090 | 37.178 | 43.210 |
| harness:snapshot | 2/2 | 0 | 0 | 0.114 | n/a | n/a | 0.058 | 56.918 | 56.918 | 65.845 |
| agency:services_start | 1/1 | 0 | 0 | 0.071 | 0.041 | 0.030 | 0.000 | 71.428 | 71.428 | 71.428 |
| harness:launch | 2/2 | 0 | 0 | 0.063 | n/a | n/a | 0.690 | 31.402 | 31.402 | 42.598 |
| run:detect | 1/1 | 0 | 0 | 0.050 | 0.001 | 0.049 | 0.000 | 49.658 | 49.658 | 49.658 |
| agent:create | 1/1 | 0 | 0 | 0.047 | 0.007 | 0.040 | 0.000 | 47.067 | 47.067 | 47.067 |
| tool:write | 2/2 | 0 | 0 | 0.039 | n/a | n/a | 0.005 | 19.654 | 19.654 | 26.450 |
| syscall:bind | 11/11 | 0 | 0 | 0.025 | n/a | n/a | 0.062 | 2.312 | 2.199 | 3.347 |
| agency:decode_harness_result | 2/2 | 0 | 0 | 0.025 | 0.025 | 0.000 | 0.003 | 12.450 | 12.450 | 14.592 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.235 | 1.235 | 1.235 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.077 | 0.084 | 0.105 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.196 | 0.196 | 0.196 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.071 | 0.071 | 0.071 |
| harness:retire | 0/2 | 0 | 2 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1429 | 2.168 | 0.019 | 225.148 | 0.056 | 31.153537 CPU seconds | n/a |
| GPU 0 memory | MB | 1430 | 11815.779 | 11670.000 | 11870.000 | 11846.000 | n/a | n/a |
| GPU 0 power | W | 1430 | 29.008 | 27.844 | 56.967 | 28.252 | n/a | 41750.659 J |
| GPU 0 proc / 20295-1457991 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 memory | MB | 1430 | 3188.662 | 3118.000 | 3238.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 20295-1457991 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 estimated power | W | 1360 | 1.377 | 0.000 | 54.043 | 0.000 | n/a | n/a |
| GPU 0 proc / 20295-1457991 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 utilization | percent | 1360 | 0.912 | 0.000 | 46.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 20403-1459893 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 memory | MB | 1430 | 8145.117 | 8070.000 | 8150.000 | 8150.000 | n/a | n/a |
| GPU 0 proc / 20403-1459893 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 estimated power | W | 49 | 8.030 | 0.000 | 52.261 | 0.000 | n/a | n/a |
| GPU 0 proc / 20403-1459893 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 utilization | percent | 49 | 7.469 | 0.000 | 56.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1430 | 11333.779 | 11188.000 | 11388.000 | 11364.000 | n/a | n/a |
| GPU 0 utilization | percent | 1430 | 1.319 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1430 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1429 | 15.429 | 0.009 | 74.113 | 0.127 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1429 | 23.928 | 0.250 | 58.791 | 0.250 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1429 | 0.786 | 0.000 | 181.933 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1429 | 2.174 | 0.000 | 241.205 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1429 | 0.853 | 0.000 | 95.774 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1429 | 0.872 | 0.000 | 96.049 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1430 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1430 | 8126.495 | 6730.539 | 10933.051 | 7291.641 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1429 | 0.117 | 0.000 | 27.040 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1429 | 0.117 | 0.000 | 27.096 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1429 | 0.043 | 0.000 | 13.148 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1429 | 0.020 | 0.000 | 0.422 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 19988) CPU | percent | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 19988) io read MB/s | MB/s | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 19988) io write MB/s | MB/s | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 19988) rss_mb | MB | 1430 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 19988) main thread run-queue wait | percent | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 19988) vms_mb | MB | 1430 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 20295) CPU | percent | 1429 | 4.493 | 0.000 | 116.146 | 0.996 | 65.070000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 20295) io read MB/s | MB/s | 1429 | 0.013 | 0.000 | 6.031 | 0.000 | 19.781250 MB | n/a |
| Agency harness — python -m lsbench (PID 20295) io write MB/s | MB/s | 1429 | 0.190 | 0.000 | 5.009 | 0.082 | 273.269531 MB | n/a |
| Agency harness — python -m lsbench (PID 20295) rss_mb | MB | 1430 | 2992.138 | 2403.781 | 3177.871 | 3177.871 | n/a | n/a |
| Agency harness — python -m lsbench (PID 20295) main thread run-queue wait | percent | 1429 | 0.000 | 0.000 | 0.229 | 0.000 | 0.002339 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 20295) vms_mb | MB | 1430 | 15989.410 | 13924.074 | 16237.227 | 16215.254 | n/a | n/a |
| Python — vllm (PID 20300) CPU | percent | 1429 | 0.158 | 0.000 | 11.877 | 0.000 | 2.270000 CPU seconds | n/a |
| Python — vllm (PID 20300) io read MB/s | MB/s | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 20300) io write MB/s | MB/s | 1429 | 0.000 | 0.000 | 0.008 | 0.000 | 0.035156 MB | n/a |
| Python — vllm (PID 20300) rss_mb | MB | 1430 | 1803.887 | 1803.367 | 1804.367 | 1803.773 | n/a | n/a |
| Python — vllm (PID 20300) main thread run-queue wait | percent | 1429 | 0.014 | 0.000 | 0.693 | 0.000 | 0.206541 run-queue seconds | n/a |
| Python — vllm (PID 20300) vms_mb | MB | 1430 | 11040.111 | 10971.566 | 11043.586 | 11043.586 | n/a | n/a |
| Python — python -c (PID 20402) CPU | percent | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 20402) io read MB/s | MB/s | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 20402) io write MB/s | MB/s | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 20402) rss_mb | MB | 1430 | 12.184 | 12.184 | 12.184 | 12.184 | n/a | n/a |
| Python — python -c (PID 20402) main thread run-queue wait | percent | 1429 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 20402) vms_mb | MB | 1430 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 20403) CPU | percent | 1429 | 1.139 | 0.000 | 48.498 | 0.000 | 16.390000 CPU seconds | n/a |
| VLLM::EngineCore (PID 20403) io read MB/s | MB/s | 1429 | 0.000 | 0.000 | 0.132 | 0.000 | 0.132812 MB | n/a |
| VLLM::EngineCore (PID 20403) io write MB/s | MB/s | 1429 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 20403) rss_mb | MB | 1430 | 2315.861 | 2314.223 | 2322.008 | 2314.473 | n/a | n/a |
| VLLM::EngineCore (PID 20403) main thread run-queue wait | percent | 1429 | 0.002 | 0.000 | 0.311 | 0.000 | 0.021765 run-queue seconds | n/a |
| VLLM::EngineCore (PID 20403) vms_mb | MB | 1430 | 21203.227 | 21203.227 | 21203.242 | 21203.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 20684) CPU | percent | 1421 | 0.001 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 20684) rss_mb | MB | 1422 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 20684) main thread run-queue wait | percent | 1421 | 0.016 | 0.000 | 5.251 | 0.000 | 0.224960 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 20684) vms_mb | MB | 1422 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 20716) CPU | percent | 1421 | 0.001 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 20716) rss_mb | MB | 1422 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 20716) main thread run-queue wait | percent | 1421 | 0.017 | 0.000 | 5.231 | 0.000 | 0.238976 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 20716) vms_mb | MB | 1422 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 20808) CPU | percent | 1421 | 33.941 | 0.000 | 100.314 | 0.000 | 485.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 20808) rss_mb | MB | 1422 | 117.335 | 3.113 | 159.379 | 159.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 20808) main thread run-queue wait | percent | 1421 | 0.000 | 0.000 | 0.011 | 0.000 | 0.000166 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 20808) vms_mb | MB | 1422 | 899.430 | 4.262 | 904.906 | 904.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 20814) CPU | percent | 1 | 99.816 | 99.816 | 99.816 | 99.816 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 20814) rss_mb | MB | 2 | 52.812 | 24.609 | 81.016 | 81.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 20814) main thread run-queue wait | percent | 1 | 0.009 | 0.009 | 0.009 | 0.009 | 0.000094 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 20814) vms_mb | MB | 2 | 63.352 | 32.422 | 94.281 | 94.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 20822) rss_mb | MB | 1 | 52.848 | 52.848 | 52.848 | 52.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 20822) vms_mb | MB | 1 | 6431.648 | 6431.648 | 6431.648 | 6431.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 20835) CPU | percent | 1079 | 5.707 | 0.000 | 129.152 | 1.990 | 62.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 20835) rss_mb | MB | 1080 | 751.598 | 93.348 | 934.383 | 772.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 20835) main thread run-queue wait | percent | 1079 | 14.524 | 0.000 | 72.156 | 0.007 | 157.849846 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 20835) vms_mb | MB | 1080 | 16536.236 | 6567.660 | 16750.156 | 16750.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 20937) rss_mb | MB | 1 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 20937) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — cat (PID 20939) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — cat (PID 20939) vms_mb | MB | 1 | 0.414 | 0.414 | 0.414 | 0.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 20940) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 20940) vms_mb | MB | 1 | 0.418 | 0.418 | 0.418 | 0.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21034) rss_mb | MB | 1 | 2.594 | 2.594 | 2.594 | 2.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21034) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21042) rss_mb | MB | 1 | 9.633 | 9.633 | 9.633 | 9.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21042) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21067) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21067) rss_mb | MB | 3 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21067) main thread run-queue wait | percent | 2 | 0.003 | 0.000 | 0.006 | 0.000 | 0.000061 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21067) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21070) rss_mb | MB | 1 | 2.723 | 2.723 | 2.723 | 2.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21070) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21076) rss_mb | MB | 1 | 9.973 | 9.973 | 9.973 | 9.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21076) vms_mb | MB | 1 | 19.137 | 19.137 | 19.137 | 19.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21120) rss_mb | MB | 1 | 2.578 | 2.578 | 2.578 | 2.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21120) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21126) rss_mb | MB | 1 | 9.922 | 9.922 | 9.922 | 9.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21126) vms_mb | MB | 1 | 19.137 | 19.137 | 19.137 | 19.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21170) rss_mb | MB | 1 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21170) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21176) rss_mb | MB | 1 | 9.812 | 9.812 | 9.812 | 9.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21176) vms_mb | MB | 1 | 19.137 | 19.137 | 19.137 | 19.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21226) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21226) rss_mb | MB | 3 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21226) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21226) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21254) rss_mb | MB | 1 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21254) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21255) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21255) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21256) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21256) vms_mb | MB | 1 | 0.637 | 0.637 | 0.637 | 0.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 21257) rss_mb | MB | 1 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 21257) vms_mb | MB | 1 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 21258) rss_mb | MB | 1 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 21258) vms_mb | MB | 1 | 2.465 | 2.465 | 2.465 | 2.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21279) rss_mb | MB | 1 | 2.668 | 2.668 | 2.668 | 2.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21279) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21285) rss_mb | MB | 1 | 9.750 | 9.750 | 9.750 | 9.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21285) vms_mb | MB | 1 | 19.137 | 19.137 | 19.137 | 19.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21329) rss_mb | MB | 1 | 2.723 | 2.723 | 2.723 | 2.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21329) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21335) rss_mb | MB | 1 | 9.930 | 9.930 | 9.930 | 9.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21335) vms_mb | MB | 1 | 19.137 | 19.137 | 19.137 | 19.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21386) rss_mb | MB | 1 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21386) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21394) rss_mb | MB | 1 | 9.922 | 9.922 | 9.922 | 9.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21394) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21407) rss_mb | MB | 1 | 2.680 | 2.680 | 2.680 | 2.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp.sh (PID 21407) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21415) rss_mb | MB | 1 | 1.309 | 1.309 | 1.309 | 1.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21415) vms_mb | MB | 1 | 15.051 | 15.051 | 15.051 | 15.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21434) rss_mb | MB | 1 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21434) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21438) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21438) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21439) rss_mb | MB | 1 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21439) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21463) rss_mb | MB | 1 | 9.688 | 9.688 | 9.688 | 9.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21463) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21473) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21473) rss_mb | MB | 2 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21473) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21473) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21475) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21475) rss_mb | MB | 2 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21475) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21475) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21476) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21476) rss_mb | MB | 2 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21476) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21476) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21483) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21483) rss_mb | MB | 2 | 9.770 | 9.770 | 9.770 | 9.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21483) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21483) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21496) rss_mb | MB | 1 | 14.258 | 14.258 | 14.258 | 14.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21496) vms_mb | MB | 1 | 208.086 | 208.086 | 208.086 | 208.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21504) rss_mb | MB | 1 | 2.578 | 2.578 | 2.578 | 2.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21504) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21510) rss_mb | MB | 1 | 922.609 | 922.609 | 922.609 | 922.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21510) vms_mb | MB | 1 | 2367.980 | 2367.980 | 2367.980 | 2367.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21511) rss_mb | MB | 1 | 1.129 | 1.129 | 1.129 | 1.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21511) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21520) rss_mb | MB | 1 | 1838.172 | 1838.172 | 1838.172 | 1838.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21520) vms_mb | MB | 1 | 2640.855 | 2640.855 | 2640.855 | 2640.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21558) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21558) rss_mb | MB | 2 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21558) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21558) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21560) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21560) rss_mb | MB | 2 | 2.566 | 2.566 | 2.566 | 2.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21560) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21560) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21561) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21561) rss_mb | MB | 2 | 9.398 | 9.398 | 9.398 | 9.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21561) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21561) vms_mb | MB | 2 | 13.301 | 13.301 | 13.301 | 13.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21568) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21568) rss_mb | MB | 2 | 10.047 | 10.047 | 10.047 | 10.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21568) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21568) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21573) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21573) rss_mb | MB | 2 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21573) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21573) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21574) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21574) rss_mb | MB | 2 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21574) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21574) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21575) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21575) rss_mb | MB | 2 | 1.191 | 1.191 | 1.191 | 1.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21575) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21575) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21582) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21582) rss_mb | MB | 2 | 9.934 | 9.934 | 9.934 | 9.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21582) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21582) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21586) rss_mb | MB | 1 | 28.609 | 28.609 | 28.609 | 28.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21586) vms_mb | MB | 1 | 250.309 | 250.309 | 250.309 | 250.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21641) rss_mb | MB | 1 | 12.891 | 12.891 | 12.891 | 12.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21641) vms_mb | MB | 1 | 207.172 | 207.172 | 207.172 | 207.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21653) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21653) rss_mb | MB | 2 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21653) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21653) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21655) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21655) rss_mb | MB | 2 | 2.566 | 2.566 | 2.566 | 2.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21655) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21655) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21656) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21656) rss_mb | MB | 2 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21656) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21656) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21662) rss_mb | MB | 1 | 7.250 | 7.250 | 7.250 | 7.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21662) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21663) rss_mb | MB | 1 | 9.688 | 9.688 | 9.688 | 9.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21663) vms_mb | MB | 1 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21667) rss_mb | MB | 1 | 13.340 | 13.340 | 13.340 | 13.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21667) vms_mb | MB | 1 | 207.125 | 207.125 | 207.125 | 207.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21675) CPU | percent | 1 | 94.281 | 94.281 | 94.281 | 94.281 | 0.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21675) rss_mb | MB | 2 | 1092.322 | 24.301 | 2160.344 | 2160.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21675) main thread run-queue wait | percent | 1 | 4.917 | 4.917 | 4.917 | 4.917 | 0.049547 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21675) vms_mb | MB | 2 | 1429.359 | 216.004 | 2642.715 | 2642.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21684) CPU | percent | 1 | 76.429 | 76.429 | 76.429 | 76.429 | 0.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21684) rss_mb | MB | 2 | 526.551 | 25.516 | 1027.586 | 1027.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21684) main thread run-queue wait | percent | 1 | 0.025 | 0.025 | 0.025 | 0.025 | 0.000250 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21684) vms_mb | MB | 2 | 718.287 | 217.473 | 1219.102 | 1219.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21697) CPU | percent | 3 | 140.852 | 76.451 | 175.084 | 171.021 | 4.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21697) rss_mb | MB | 4 | 791.613 | 18.578 | 1057.594 | 1057.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21697) main thread run-queue wait | percent | 3 | 36.838 | 0.026 | 60.834 | 60.834 | 1.111227 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21697) vms_mb | MB | 4 | 999.536 | 211.129 | 1280.895 | 1280.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21706) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21706) rss_mb | MB | 17 | 2.844 | 2.844 | 2.844 | 2.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21706) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000006 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21706) vms_mb | MB | 17 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21709) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21709) rss_mb | MB | 2 | 2.723 | 2.723 | 2.723 | 2.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21709) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21709) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21716) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21716) rss_mb | MB | 2 | 9.805 | 9.805 | 9.805 | 9.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21716) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21716) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21718) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21718) rss_mb | MB | 2 | 2.637 | 2.637 | 2.637 | 2.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21718) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21718) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21725) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21725) rss_mb | MB | 2 | 9.840 | 9.840 | 9.840 | 9.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21725) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21725) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21727) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21727) rss_mb | MB | 2 | 2.574 | 2.574 | 2.574 | 2.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21727) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21727) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21734) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21734) rss_mb | MB | 2 | 9.934 | 9.934 | 9.934 | 9.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21734) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21734) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21736) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21736) rss_mb | MB | 2 | 2.723 | 2.723 | 2.723 | 2.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21736) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21736) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21743) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21743) rss_mb | MB | 2 | 9.938 | 9.938 | 9.938 | 9.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21743) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21743) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21745) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21745) rss_mb | MB | 2 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21745) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21745) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21752) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21752) rss_mb | MB | 2 | 9.801 | 9.801 | 9.801 | 9.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21752) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21752) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21754) rss_mb | MB | 1 | 2.766 | 2.766 | 2.766 | 2.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21754) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21761) rss_mb | MB | 1 | 9.891 | 9.891 | 9.891 | 9.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21761) vms_mb | MB | 1 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21763) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21763) rss_mb | MB | 2 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21763) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21763) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21770) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21770) rss_mb | MB | 2 | 9.986 | 9.910 | 10.062 | 10.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21770) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21770) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21772) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21772) rss_mb | MB | 2 | 2.770 | 2.770 | 2.770 | 2.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21772) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21772) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21779) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21779) rss_mb | MB | 2 | 9.859 | 9.859 | 9.859 | 9.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21779) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21779) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21782) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21782) rss_mb | MB | 2 | 2.738 | 2.738 | 2.738 | 2.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21782) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21782) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21789) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21789) rss_mb | MB | 2 | 9.891 | 9.891 | 9.891 | 9.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21789) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21789) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21793) CPU | percent | 1 | 91.348 | 91.348 | 91.348 | 91.348 | 0.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21793) rss_mb | MB | 2 | 508.031 | 7.695 | 1008.367 | 1008.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21793) main thread run-queue wait | percent | 1 | 11.182 | 11.182 | 11.182 | 11.182 | 0.112614 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21793) vms_mb | MB | 2 | 605.471 | 11.934 | 1199.008 | 1199.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21800) CPU | percent | 19 | 168.425 | 102.895 | 174.645 | 174.645 | 32.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21800) rss_mb | MB | 20 | 956.846 | 13.273 | 1057.559 | 87.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21800) main thread run-queue wait | percent | 19 | 50.823 | 11.623 | 58.644 | 53.550 | 9.730581 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21800) vms_mb | MB | 20 | 1226.793 | 207.250 | 1280.453 | 1280.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21812) CPU | percent | 2 | 148.583 | 125.084 | 172.082 | 172.082 | 2.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21812) rss_mb | MB | 3 | 710.646 | 19.113 | 1056.602 | 1056.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21812) main thread run-queue wait | percent | 2 | 35.480 | 9.397 | 61.564 | 61.564 | 0.713577 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21812) vms_mb | MB | 3 | 922.978 | 211.027 | 1278.953 | 1278.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21821) rss_mb | MB | 1 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21821) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21823) rss_mb | MB | 1 | 2.777 | 2.777 | 2.777 | 2.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21823) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21824) rss_mb | MB | 1 | 9.199 | 9.199 | 9.199 | 9.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21824) vms_mb | MB | 1 | 13.301 | 13.301 | 13.301 | 13.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21831) rss_mb | MB | 1 | 9.758 | 9.758 | 9.758 | 9.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21831) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21836) rss_mb | MB | 1 | 2.629 | 2.629 | 2.629 | 2.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21836) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21837) rss_mb | MB | 1 | 2.738 | 2.738 | 2.738 | 2.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21837) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 21838) rss_mb | MB | 1 | 1.723 | 1.723 | 1.723 | 1.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 21838) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 21839) rss_mb | MB | 1 | 1.660 | 1.660 | 1.660 | 1.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 21839) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21840) rss_mb | MB | 1 | 9.355 | 9.355 | 9.355 | 9.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21840) vms_mb | MB | 1 | 13.301 | 13.301 | 13.301 | 13.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21847) rss_mb | MB | 1 | 9.828 | 9.828 | 9.828 | 9.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21847) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21852) CPU | percent | 53 | 170.885 | 145.917 | 175.337 | 170.039 | 91.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21852) rss_mb | MB | 54 | 1043.522 | 376.172 | 1056.113 | 1056.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21852) main thread run-queue wait | percent | 53 | 59.465 | 24.832 | 78.351 | 51.527 | 31.752602 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21852) vms_mb | MB | 54 | 1268.295 | 700.934 | 1279.000 | 1279.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21894) CPU | percent | 35 | 163.002 | 96.432 | 178.714 | 170.085 | 57.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21894) rss_mb | MB | 36 | 1498.814 | 321.484 | 3002.746 | 1064.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21894) main thread run-queue wait | percent | 35 | 43.879 | 0.019 | 74.511 | 72.162 | 15.462357 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21894) vms_mb | MB | 36 | 2025.605 | 700.996 | 3227.453 | 1287.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21911) rss_mb | MB | 1 | 641.145 | 641.145 | 641.145 | 641.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21911) vms_mb | MB | 1 | 1670.898 | 1670.898 | 1670.898 | 1670.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21922) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21922) rss_mb | MB | 2 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21922) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 21922) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21924) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21924) rss_mb | MB | 2 | 2.875 | 2.875 | 2.875 | 2.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21924) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 21924) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21925) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21925) rss_mb | MB | 2 | 1.230 | 1.230 | 1.230 | 1.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21925) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 21925) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21932) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21932) rss_mb | MB | 2 | 9.969 | 9.969 | 9.969 | 9.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21932) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 21932) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21936) rss_mb | MB | 1 | 27.074 | 27.074 | 27.074 | 27.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21936) vms_mb | MB | 1 | 250.020 | 250.020 | 250.020 | 250.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21943) CPU | percent | 20 | 170.085 | 141.011 | 174.216 | 172.090 | 34.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21943) rss_mb | MB | 21 | 1016.276 | 193.285 | 1057.426 | 1057.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21943) main thread run-queue wait | percent | 20 | 61.469 | 22.037 | 73.230 | 62.297 | 12.386020 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21943) vms_mb | MB | 21 | 1252.876 | 700.949 | 1280.473 | 1280.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21954) CPU | percent | 59 | 153.297 | 101.278 | 172.739 | 148.252 | 91.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21954) rss_mb | MB | 60 | 2012.980 | 13.395 | 3002.371 | 1428.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21954) main thread run-queue wait | percent | 59 | 23.861 | 0.036 | 37.120 | 27.318 | 14.189140 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21954) vms_mb | MB | 60 | 3144.750 | 207.316 | 3227.418 | 3227.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21972) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21972) rss_mb | MB | 9 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21972) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21972) vms_mb | MB | 9 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21973) CPU | percent | 8 | 167.256 | 127.069 | 175.370 | 173.020 | 13.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21973) rss_mb | MB | 9 | 1195.747 | 100.719 | 1382.582 | 1382.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21973) main thread run-queue wait | percent | 8 | 55.688 | 12.534 | 73.139 | 49.798 | 4.483635 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21973) vms_mb | MB | 9 | 1460.145 | 701.020 | 1604.770 | 1604.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21982) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21982) rss_mb | MB | 9 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21982) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21982) vms_mb | MB | 9 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21983) CPU | percent | 8 | 171.100 | 162.767 | 175.058 | 172.058 | 13.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21983) rss_mb | MB | 9 | 1276.708 | 1223.430 | 1303.008 | 1223.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21983) main thread run-queue wait | percent | 8 | 48.252 | 36.050 | 51.233 | 49.512 | 3.885883 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21983) vms_mb | MB | 9 | 1577.604 | 1445.621 | 2156.023 | 1445.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21993) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21993) rss_mb | MB | 4 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21993) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 21993) vms_mb | MB | 4 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21994) CPU | percent | 3 | 165.247 | 144.847 | 177.285 | 173.609 | 5.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21994) rss_mb | MB | 4 | 1004.202 | 839.152 | 1059.219 | 1059.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21994) main thread run-queue wait | percent | 3 | 53.305 | 31.175 | 65.281 | 63.459 | 1.617330 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 21994) vms_mb | MB | 4 | 1378.108 | 1280.480 | 1670.992 | 1280.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22005) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22005) rss_mb | MB | 3 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22005) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22005) vms_mb | MB | 3 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22007) CPU | percent | 2 | 151.869 | 129.214 | 174.524 | 174.524 | 3.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22007) rss_mb | MB | 3 | 760.117 | 162.180 | 1059.086 | 1059.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22007) main thread run-queue wait | percent | 2 | 44.192 | 15.592 | 72.791 | 72.791 | 0.890934 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22007) vms_mb | MB | 3 | 1087.297 | 700.969 | 1280.461 | 1280.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22016) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22016) rss_mb | MB | 3 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22016) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22016) vms_mb | MB | 3 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22017) CPU | percent | 2 | 166.169 | 158.014 | 174.323 | 174.323 | 3.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22017) rss_mb | MB | 3 | 1067.315 | 1058.816 | 1084.312 | 1058.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22017) main thread run-queue wait | percent | 2 | 55.536 | 47.064 | 64.009 | 64.009 | 1.119821 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22017) vms_mb | MB | 3 | 1572.322 | 1280.484 | 2155.996 | 1280.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 22029) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 22029) rss_mb | MB | 3 | 247.329 | 2.863 | 736.262 | 2.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 22029) main thread run-queue wait | percent | 2 | 0.071 | 0.000 | 0.141 | 0.000 | 0.001425 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 22029) vms_mb | MB | 3 | 5582.573 | 3.848 | 16740.023 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22032) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22032) rss_mb | MB | 2 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22032) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22032) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 22033) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 22033) rss_mb | MB | 2 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 22033) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 22033) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22040) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22040) rss_mb | MB | 2 | 9.691 | 9.691 | 9.691 | 9.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22040) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22040) vms_mb | MB | 2 | 19.145 | 19.145 | 19.145 | 19.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22062) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22062) rss_mb | MB | 3 | 1.227 | 1.227 | 1.227 | 1.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22062) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22062) vms_mb | MB | 3 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22063) CPU | percent | 2 | 135.989 | 94.279 | 177.698 | 177.698 | 2.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22063) rss_mb | MB | 3 | 709.536 | 13.363 | 1058.625 | 1058.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22063) main thread run-queue wait | percent | 2 | 37.341 | 8.578 | 66.103 | 66.103 | 0.752315 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22063) vms_mb | MB | 3 | 912.089 | 207.281 | 1280.492 | 1280.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22071) CPU | percent | 84 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22071) rss_mb | MB | 85 | 1.324 | 1.324 | 1.324 | 1.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22071) main thread run-queue wait | percent | 84 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22071) vms_mb | MB | 85 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22072) CPU | percent | 84 | 125.222 | 99.268 | 180.025 | 173.648 | 105.910000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22072) rss_mb | MB | 85 | 2308.247 | 155.762 | 3224.750 | 155.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22072) main thread run-queue wait | percent | 84 | 17.051 | 0.001 | 61.356 | 61.356 | 14.426125 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22072) vms_mb | MB | 85 | 3188.272 | 373.562 | 3442.715 | 373.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22091) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22091) rss_mb | MB | 2 | 2.025 | 1.293 | 2.758 | 1.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22091) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22091) vms_mb | MB | 2 | 3.148 | 2.449 | 3.848 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22093) rss_mb | MB | 1 | 2.707 | 2.707 | 2.707 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22093) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 22094) rss_mb | MB | 1 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 22094) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22101) rss_mb | MB | 1 | 9.906 | 9.906 | 9.906 | 9.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22101) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22102) rss_mb | MB | 1 | 2440.980 | 2440.980 | 2440.980 | 2440.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22102) vms_mb | MB | 1 | 2640.934 | 2640.934 | 2640.934 | 2640.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22112) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22112) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22114) rss_mb | MB | 1 | 105.691 | 105.691 | 105.691 | 105.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22114) vms_mb | MB | 1 | 700.938 | 700.938 | 700.938 | 700.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22122) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22122) rss_mb | MB | 2 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22122) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22122) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22123) CPU | percent | 1 | 158.060 | 158.060 | 158.060 | 158.060 | 1.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22123) rss_mb | MB | 2 | 1034.211 | 1010.941 | 1057.480 | 1057.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22123) main thread run-queue wait | percent | 1 | 48.540 | 48.540 | 48.540 | 48.540 | 0.488285 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22123) vms_mb | MB | 2 | 1241.215 | 1202.004 | 1280.426 | 1280.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22131) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22131) rss_mb | MB | 22 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22131) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22131) vms_mb | MB | 22 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22132) CPU | percent | 21 | 170.827 | 141.153 | 175.086 | 170.077 | 36.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22132) rss_mb | MB | 22 | 1176.906 | 285.691 | 1223.566 | 1223.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22132) main thread run-queue wait | percent | 21 | 51.317 | 17.338 | 67.618 | 48.842 | 10.847050 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22132) vms_mb | MB | 22 | 1407.815 | 701.012 | 1445.613 | 1445.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22153) CPU | percent | 71 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22153) rss_mb | MB | 72 | 1.172 | 1.172 | 1.172 | 1.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22153) main thread run-queue wait | percent | 71 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22153) vms_mb | MB | 72 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22154) CPU | percent | 71 | 171.867 | 103.175 | 176.384 | 172.083 | 122.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22154) rss_mb | MB | 72 | 1204.465 | 13.793 | 1223.695 | 1223.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22154) main thread run-queue wait | percent | 71 | 60.847 | 5.043 | 78.096 | 51.337 | 43.502729 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22154) vms_mb | MB | 72 | 1426.087 | 207.359 | 1445.598 | 1445.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22174) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22174) rss_mb | MB | 2 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22174) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22174) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22175) CPU | percent | 1 | 98.281 | 98.281 | 98.281 | 98.281 | 0.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22175) rss_mb | MB | 2 | 517.281 | 7.473 | 1027.090 | 1027.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22175) main thread run-queue wait | percent | 1 | 6.036 | 6.036 | 6.036 | 6.036 | 0.060798 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22175) vms_mb | MB | 2 | 615.154 | 11.945 | 1218.363 | 1218.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22202) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22202) rss_mb | MB | 2 | 2.750 | 2.750 | 2.750 | 2.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22202) main thread run-queue wait | percent | 1 | 0.057 | 0.057 | 0.057 | 0.057 | 0.000575 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22202) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22234) rss_mb | MB | 1 | 2.652 | 2.652 | 2.652 | 2.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22234) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22235) rss_mb | MB | 1 | 1.629 | 1.629 | 1.629 | 1.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22235) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22236) rss_mb | MB | 1 | 1.633 | 1.633 | 1.633 | 1.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22236) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22237) rss_mb | MB | 1 | 5.703 | 5.703 | 5.703 | 5.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22237) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22238) rss_mb | MB | 1 | 1.316 | 1.316 | 1.316 | 1.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22238) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22239) rss_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22239) vms_mb | MB | 1 | 18.930 | 18.930 | 18.930 | 18.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 22240) rss_mb | MB | 1 | 1.398 | 1.398 | 1.398 | 1.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 22240) vms_mb | MB | 1 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 22241) rss_mb | MB | 1 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 22241) vms_mb | MB | 1 | 2.465 | 2.465 | 2.465 | 2.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — awk (PID 22242) rss_mb | MB | 1 | 1.719 | 1.719 | 1.719 | 1.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — awk (PID 22242) vms_mb | MB | 1 | 3.504 | 3.504 | 3.504 | 3.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22267) rss_mb | MB | 1 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22267) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22268) rss_mb | MB | 1 | 1.762 | 1.762 | 1.762 | 1.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22268) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22269) rss_mb | MB | 1 | 1.809 | 1.809 | 1.809 | 1.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22269) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22270) rss_mb | MB | 1 | 9.223 | 9.223 | 9.223 | 9.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22270) vms_mb | MB | 1 | 13.301 | 13.301 | 13.301 | 13.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22277) rss_mb | MB | 1 | 9.961 | 9.961 | 9.961 | 9.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22277) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22305) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22305) rss_mb | MB | 2 | 2.625 | 2.625 | 2.625 | 2.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22305) main thread run-queue wait | percent | 1 | 0.115 | 0.115 | 0.115 | 0.115 | 0.001161 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22305) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22306) rss_mb | MB | 1 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22306) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22307) rss_mb | MB | 1 | 1.668 | 1.668 | 1.668 | 1.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22307) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22308) rss_mb | MB | 1 | 1.754 | 1.754 | 1.754 | 1.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22308) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22314) rss_mb | MB | 1 | 9.336 | 9.336 | 9.336 | 9.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22314) vms_mb | MB | 1 | 13.266 | 13.266 | 13.266 | 13.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22346) rss_mb | MB | 1 | 2.723 | 2.723 | 2.723 | 2.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22346) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22347) rss_mb | MB | 1 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22347) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22348) rss_mb | MB | 1 | 1.680 | 1.680 | 1.680 | 1.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — sed (PID 22348) vms_mb | MB | 1 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22354) rss_mb | MB | 1 | 10.098 | 10.098 | 10.098 | 10.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22354) vms_mb | MB | 1 | 13.312 | 13.312 | 13.312 | 13.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22372) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22372) rss_mb | MB | 3 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22372) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22372) vms_mb | MB | 3 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22373) CPU | percent | 2 | 152.042 | 133.996 | 170.088 | 170.088 | 3.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22373) rss_mb | MB | 3 | 838.191 | 397.262 | 1058.656 | 1058.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22373) main thread run-queue wait | percent | 2 | 49.956 | 27.257 | 72.654 | 72.654 | 1.005048 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22373) vms_mb | MB | 3 | 1087.367 | 701.039 | 1280.531 | 1280.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 22388) CPU | percent | 301 | 10.182 | 0.994 | 140.255 | 0.995 | 30.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 22388) rss_mb | MB | 302 | 749.808 | 102.812 | 942.562 | 767.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 22388) main thread run-queue wait | percent | 301 | 0.981 | 0.000 | 69.252 | 0.007 | 2.970914 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 22388) vms_mb | MB | 302 | 15529.419 | 6568.164 | 16746.945 | 16746.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22434) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22434) rss_mb | MB | 2 | 1.227 | 1.227 | 1.227 | 1.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22434) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22434) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22435) CPU | percent | 1 | 172.894 | 172.894 | 172.894 | 172.894 | 1.740000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22435) rss_mb | MB | 2 | 1041.348 | 1025.781 | 1056.914 | 1056.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22435) main thread run-queue wait | percent | 1 | 40.395 | 40.395 | 40.395 | 40.395 | 0.406538 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22435) vms_mb | MB | 2 | 1248.881 | 1217.336 | 1280.426 | 1280.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22449) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22449) rss_mb | MB | 3 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22449) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — timeout (PID 22449) vms_mb | MB | 3 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22450) CPU | percent | 2 | 170.043 | 168.999 | 171.087 | 171.087 | 3.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22450) rss_mb | MB | 3 | 118.724 | 77.641 | 140.016 | 140.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22450) main thread run-queue wait | percent | 2 | 50.277 | 47.718 | 52.835 | 47.718 | 1.011208 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22450) vms_mb | MB | 3 | 336.415 | 297.082 | 356.082 | 356.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22492) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22492) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22517) rss_mb | MB | 1 | 2.609 | 2.609 | 2.609 | 2.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 22517) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22520) rss_mb | MB | 1 | 2.625 | 2.625 | 2.625 | 2.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22520) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 22521) rss_mb | MB | 1 | 1.234 | 1.234 | 1.234 | 1.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 22521) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22522) rss_mb | MB | 1 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash mcp2.sh (PID 22522) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22523) rss_mb | MB | 1 | 9.652 | 9.652 | 9.652 | 9.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 22523) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 22524) rss_mb | MB | 1 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 22524) vms_mb | MB | 1 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 22525) rss_mb | MB | 1 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 22525) vms_mb | MB | 1 | 2.465 | 2.465 | 2.465 | 2.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — awk (PID 22526) rss_mb | MB | 1 | 1.613 | 1.613 | 1.613 | 1.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — awk (PID 22526) vms_mb | MB | 1 | 3.504 | 3.504 | 3.504 | 3.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22539) rss_mb | MB | 1 | 20.336 | 20.336 | 20.336 | 20.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 22539) vms_mb | MB | 1 | 212.074 | 212.074 | 212.074 | 212.074 | n/a | n/a |
| docker commit (PID 22649) CPU | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 22649) io read MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 22649) io write MB/s | MB/s | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 22649) rss_mb | MB | 32 | 29.941 | 27.625 | 30.133 | 30.133 | n/a | n/a |
| docker commit (PID 22649) main thread run-queue wait | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 22649) vms_mb | MB | 32 | 1839.001 | 1698.938 | 1843.520 | 1843.520 | n/a | n/a |
| docker stop (PID 22699) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker stop (PID 22699) io read MB/s | MB/s | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker stop (PID 22699) io write MB/s | MB/s | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker stop (PID 22699) rss_mb | MB | 6 | 31.004 | 31.004 | 31.004 | 31.004 | n/a | n/a |
| docker stop (PID 22699) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker stop (PID 22699) vms_mb | MB | 6 | 1771.258 | 1771.258 | 1771.258 | 1771.258 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 CPU | percent | 1421 | 88.052 | 0.000 | 210.770 | 0.000 | 1260.208505 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1421 | 11.023 | 0.000 | 50.695 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1421 | 15.226 | 0.000 | 73.685 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_full_pct | percent of wall time stalled | 1421 | 0.173 | 0.000 | 94.390 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_some_pct | percent of wall time stalled | 1421 | 0.174 | 0.000 | 94.390 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io read MB/s | MB/s | 1421 | 0.317 | 0.000 | 146.069 | 0.000 | 453.531250 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io write MB/s | MB/s | 1421 | 0.962 | 0.000 | 227.290 | 0.000 | 1420.425781 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory | MB | 1422 | 2576.444 | 14.824 | 5424.301 | 1575.496 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1421 | 0.068 | 0.000 | 22.556 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1421 | 0.068 | 0.000 | 22.556 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net rx MB/s | MB/s | 1421 | 0.034 | 0.000 | 12.738 | 0.000 | 48.347008 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net tx MB/s | MB/s | 1421 | 0.001 | 0.000 | 0.068 | 0.000 | 0.884627 MB | n/a |
| workload total CPU | percent | 1429 | 5.801 | 1.360 | 117.135 | 1.388 | 83.907245 CPU seconds | n/a |
| workload total memory | MB | 1430 | 5623.596 | 5061.617 | 5830.328 | 5824.672 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
