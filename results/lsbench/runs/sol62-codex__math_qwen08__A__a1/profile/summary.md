# agprof summary

- Duration: **1680.164 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **64 calls**, 64 succeeded, 0 failed, 0 interrupted, n/a reported retries, 865.005 s total wait
- Tools: **91/91 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **154884** at 1.974 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1652859.865 / 1652859.865 ms |
| LLM latency p50 / p95 | 11472.708 / 31168.254 ms |
| LLM TTFT p50 / p95 | 5521.279 / 6757.530 ms |
| LLM input / output tokens | 5007737 / 120599 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 64 total, 64 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- codex: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 37/37 | 37 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 19/19 | 19 | 0 | 0 | n/a | n/a |
| mcp__agency__get_current_resources | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 18/18 | 18 | 0 | 0 | n/a | n/a |
| update_plan | 5/5 | 5 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 24.643% | 269.777% | 414.279 s | 13357.427 MB | 14447.832 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VLLM::EngineCor | 4632 |  | 1668 | 12.763% | 43.700% | 214.630 s | 2341.908 MB | 2342.281 MB | 21862.725 MB | 21863.043 MB | 0.000000 MB | 0.007812 MB |
| python | 4631 |  | 1668 | 0.000% | 0.000% | 0.000 s | 12.336 MB | 12.336 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python | 4553 |  | 1668 | 10.742% | 268.255% | 180.510 s | 2541.715 MB | 3897.340 MB | 16182.196 MB | 21353.152 MB | 0.531250 MB | 1268.277344 MB |
| lsb_grid_worker | 2144 |  | 1668 | 0.000% | 0.000% | 0.000 s | 3.402 MB | 3.402 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| vllm | 4562 |  | 1668 | 1.129% | 5.945% | 18.980 s | 1805.394 MB | 1805.625 MB | 12012.418 MB | 12013.770 MB | 0.000000 MB | 0.128906 MB |
| tail | 4935 | sandbox_agent_lsb-codex_0000_0000 | 1641 | 0.002% | 0.995% | 0.030 s | 1.586 MB | 1.586 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 5037 | sandbox_agent_lsb-codex_0000_0000 | 1641 | 26.478% | 99.288% | 437.290 s | 115.433 MB | 126.492 MB | 1023.427 MB | 1048.238 MB | n/a MB | n/a MB |
| python3 | 5043 | sandbox_agent_lsb-codex_0000_0000 | 2 | 99.911% | 99.911% | 1.010 s | 55.977 MB | 83.887 MB | 67.352 MB | 97.996 MB | n/a MB | n/a MB |
| docker-init | 4895 | sandbox_agent_lsb-codex_0000_0000 | 1641 | 0.002% | 0.995% | 0.030 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| codex | 5060 | sandbox_agent_lsb-codex_0000_0000 | 1635 | 3.085% | 16.899% | 50.790 s | 140.324 MB | 153.488 MB | 393.421 MB | 539.688 MB | n/a MB | n/a MB |
| git-remote-http | 5092 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.113 MB | 11.113 MB | 20.762 MB | 20.762 MB | n/a MB | n/a MB |
| tokio-rt-worker | 5095 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 63.371 MB | 63.371 MB | 360.359 MB | 360.359 MB | n/a MB | n/a MB |
| git | 5091 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.797 MB | 3.797 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 5089 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.809 MB | 3.809 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git-remote-http | 5114 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.043 MB | 19.043 MB | 100.484 MB | 100.484 MB | n/a MB | n/a MB |
| git | 5110 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.836 MB | 3.836 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 5140 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.465 MB | 5.465 MB | 8.285 MB | 8.285 MB | n/a MB | n/a MB |
| git | 5112 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.020 MB | 4.020 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| python3 | 5185 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.473 MB | 7.473 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 5252 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.090 MB | 5.090 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| bash | 5251 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.762 MB | 2.762 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 5314 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.668 MB | 15.668 MB | 20.270 MB | 20.270 MB | n/a MB | n/a MB |
| python3 | 5340 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.523 MB | 18.523 MB | 23.176 MB | 23.176 MB | n/a MB | n/a MB |
| python | 5383 | sandbox_agent_lsb-codex_0000_0000 | 2 | 155.037% | 155.037% | 1.560 s | 129.074 MB | 136.684 MB | 266.779 MB | 274.145 MB | n/a MB | n/a MB |
| python3 | 5417 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.031 MB | 21.031 MB | 25.582 MB | 25.582 MB | n/a MB | n/a MB |
| python3 | 5452 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.508 MB | 20.508 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| bash | 5481 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.012 MB | 3.012 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5482 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.535 MB | 18.535 MB | 369.926 MB | 369.926 MB | n/a MB | n/a MB |
| python | 5501 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.434 MB | 8.434 MB | 13.016 MB | 13.016 MB | n/a MB | n/a MB |
| bash | 5500 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.008 MB | 3.008 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 5538 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.879 MB | 7.879 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python3 | 5580 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.867 MB | 20.867 MB | 25.324 MB | 25.324 MB | n/a MB | n/a MB |
| python3 | 5602 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.020 MB | 8.020 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python | 5627 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 135.617 MB | 135.617 MB | 140.875 MB | 140.875 MB | n/a MB | n/a MB |
| bash | 5615 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.062 MB | 3.062 MB | 4.379 MB | 4.379 MB | n/a MB | n/a MB |
| python | 5628 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 149.949 MB | 149.949 MB | 155.746 MB | 155.746 MB | n/a MB | n/a MB |
| python3 | 5637 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.035 MB | 21.035 MB | 25.711 MB | 25.711 MB | n/a MB | n/a MB |
| bash | 5654 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.852 MB | 2.852 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5655 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 149.340 MB | 149.340 MB | 153.613 MB | 153.613 MB | n/a MB | n/a MB |
| python | 5697 | sandbox_agent_lsb-codex_0000_0000 | 2 | 128.089% | 128.089% | 1.290 s | 133.922 MB | 178.047 MB | 261.342 MB | 321.031 MB | n/a MB | n/a MB |
| bash | 5685 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.180 MB | 3.180 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 5699 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.191 MB | 19.191 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python | 5706 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.758 MB | 9.758 MB | 13.418 MB | 13.418 MB | n/a MB | n/a MB |
| python | 5762 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 149.406 MB | 149.406 MB | 155.883 MB | 155.883 MB | n/a MB | n/a MB |
| bash | 5761 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.031 MB | 3.031 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5763 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 135.453 MB | 135.453 MB | 140.750 MB | 140.750 MB | n/a MB | n/a MB |
| python3 | 5777 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.125 MB | 22.125 MB | 26.941 MB | 26.941 MB | n/a MB | n/a MB |
| bash | 5789 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.621 MB | 2.621 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5794 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.371 MB | 15.371 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python | 5804 | sandbox_agent_lsb-codex_0000_0000 | 5 | 131.085% | 167.798% | 5.280 s | 340.418 MB | 593.715 MB | 564.712 MB | 1189.828 MB | n/a MB | n/a MB |
| python | 5913 | sandbox_agent_lsb-codex_0000_0000 | 2 | 99.420% | 99.420% | 1.000 s | 175.641 MB | 251.156 MB | 302.059 MB | 389.828 MB | n/a MB | n/a MB |
| python3 | 5926 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.113 MB | 22.113 MB | 26.945 MB | 26.945 MB | n/a MB | n/a MB |
| python3 | 5940 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.316 MB | 8.316 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python3 | 5964 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.336 MB | 19.336 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python3 | 5993 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.652 MB | 16.652 MB | 20.852 MB | 20.852 MB | n/a MB | n/a MB |
| python3 | 6006 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.254 MB | 10.254 MB | 13.738 MB | 13.738 MB | n/a MB | n/a MB |
| python | 6056 | sandbox_agent_lsb-codex_0000_0000 | 3 | 91.451% | 99.458% | 1.840 s | 111.543 MB | 135.789 MB | 117.061 MB | 140.887 MB | n/a MB | n/a MB |
| bash | 6051 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.176 MB | 3.176 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6058 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.113 MB | 21.113 MB | 172.223 MB | 172.223 MB | n/a MB | n/a MB |
| bash | 6052 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.996 MB | 2.996 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| bash | 6072 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.164 MB | 3.164 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6074 | sandbox_agent_lsb-codex_0000_0000 | 3 | 146.082% | 163.950% | 2.940 s | 164.458 MB | 265.789 MB | 503.980 MB | 950.473 MB | n/a MB | n/a MB |
| python3 | 6083 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.953 MB | 15.953 MB | 20.605 MB | 20.605 MB | n/a MB | n/a MB |
| python3 | 6084 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.395 MB | 16.395 MB | 21.852 MB | 21.852 MB | n/a MB | n/a MB |
| python | 6098 | sandbox_agent_lsb-codex_0000_0000 | 3 | 96.765% | 110.278% | 1.950 s | 139.819 MB | 251.465 MB | 301.842 MB | 429.625 MB | n/a MB | n/a MB |
| bash | 6095 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.082 MB | 3.082 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| bash | 6094 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.016 MB | 3.016 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6099 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.129 MB | 10.129 MB | 14.785 MB | 14.785 MB | n/a MB | n/a MB |
| python3 | 6102 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.633 MB | 18.633 MB | 24.332 MB | 24.332 MB | n/a MB | n/a MB |
| python3 | 6109 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.145 MB | 17.145 MB | 22.145 MB | 22.145 MB | n/a MB | n/a MB |
| python | 6138 | sandbox_agent_lsb-codex_0000_0000 | 7 | 113.338% | 170.073% | 6.840 s | 222.616 MB | 262.457 MB | 397.861 MB | 446.359 MB | n/a MB | n/a MB |
| bash | 6135 | sandbox_agent_lsb-codex_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.219 MB | 3.219 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| bash | 6134 | sandbox_agent_lsb-codex_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 3.211 MB | 3.211 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6139 | sandbox_agent_lsb-codex_0000_0000 | 4 | 103.322% | 116.256% | 3.120 s | 214.908 MB | 237.992 MB | 527.797 MB | 950.418 MB | n/a MB | n/a MB |
| python | 6498 | sandbox_agent_lsb-codex_0000_0000 | 3 | 108.346% | 118.368% | 2.180 s | 183.973 MB | 287.609 MB | 352.913 MB | 464.141 MB | n/a MB | n/a MB |
| bash | 6496 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.195 MB | 3.195 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python | 6533 | sandbox_agent_lsb-codex_0000_0000 | 11 | 161.402% | 173.827% | 16.240 s | 302.396 MB | 418.023 MB | 782.746 MB | 1050.828 MB | n/a MB | n/a MB |
| bash | 6531 | sandbox_agent_lsb-codex_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 3.066 MB | 3.066 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python3 | 6542 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.148 MB | 19.148 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python | 6557 | sandbox_agent_lsb-codex_0000_0000 | 2 | 93.406% | 93.406% | 0.940 s | 89.189 MB | 154.672 MB | 255.953 MB | 336.418 MB | n/a MB | n/a MB |
| bash | 6555 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.090 MB | 3.090 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| tokio-rt-worker | 6560 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 149.109 MB | 149.109 MB | 399.676 MB | 399.676 MB | n/a MB | n/a MB |
| python3 | 6604 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.918 MB | 14.918 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python3 | 6627 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.090 MB | 22.090 MB | 27.066 MB | 27.066 MB | n/a MB | n/a MB |
| python | 6628 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 163.121 MB | 163.121 MB | 343.570 MB | 343.570 MB | n/a MB | n/a MB |
| python3 | 6639 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.621 MB | 7.621 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python3 | 6640 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.434 MB | 7.434 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python3 | 6665 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.766 MB | 8.766 MB | 13.285 MB | 13.285 MB | n/a MB | n/a MB |
| docker | 6716 |  | 2 | 0.000% | 0.000% | 0.000 s | 28.660 MB | 28.660 MB | 1835.570 MB | 1835.570 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 40.147% | 100.000% | 11947.323 MB | 16116.000 MB | 46.745 W | 75.275 W | 78544.934 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 34.806% | 209.079% | 574.827 s | 437.748 MB | 934.926 MB | 135.183594 MB | 251.855469 MB | 24.951723 MB | 1.439794 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4765 | 1680.100 | interrupted |
| harness:retire | -1 | 0.405 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1652.860 | n/a | n/a | 135.184 | 1652859.865 | 1652859.865 | 1652859.865 |
| engine:execute | 1/1 | 0 | 0 | 1652.858 | 2.090 | 1650.768 | 135.184 | 1652858.077 | 1652858.077 | 1652858.077 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1646.973 | 0.010 | 1646.963 | 120.818 | 1646973.454 | 1646973.454 | 1646973.454 |
| harness:await_cli | 1/1 | 0 | 0 | 1643.477 | n/a | n/a | 16.768 | 1643477.325 | 1643477.325 | 1643477.325 |
| llm:attempt | 64/64 | 0 | 0 | 865.005 | 8.006 | 856.997 | 9.322 | 13515.701 | 11472.708 | 31168.254 |
| tool:mcp__agency__generate | 19/19 | 0 | 0 | 610.484 | n/a | n/a | 0.114 | 32130.747 | 11268.212 | 90897.951 |
| tool:Bash | 37/37 | 0 | 0 | 279.968 | n/a | n/a | 2.155 | 7566.708 | 791.364 | 28443.031 |
| tool:mcp__agency__trace | 18/18 | 0 | 0 | 69.055 | n/a | n/a | 0.000 | 3836.406 | 2801.871 | 10279.630 |
| tool:mcp__agency__token_stats | 1/1 | 0 | 0 | 33.795 | n/a | n/a | 0.000 | 33794.685 | 33794.685 | 33794.685 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.053 | 0.693 | 2.360 | 13.487 | 3053.184 | 3053.184 | 3053.184 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.053 | 0.693 | 2.360 | 13.483 | 3052.923 | 3052.923 | 3052.923 |
| tool:mcp__agency__attention | 1/1 | 0 | 0 | 2.620 | n/a | n/a | 0.000 | 2620.362 | 2620.362 | 2620.362 |
| run:container_call | 13/13 | 0 | 0 | 2.522 | 0.002 | 2.520 | 0.000 | 194.027 | 33.786 | 867.012 |
| tool:mcp__agency__logit_lens | 1/1 | 0 | 0 | 2.275 | n/a | n/a | 0.000 | 2274.973 | 2274.973 | 2274.973 |
| tool:mcp__agency__attribution | 2/2 | 0 | 0 | 2.254 | n/a | n/a | 0.000 | 1127.051 | 1127.051 | 1140.269 |
| teardown:commit | 1/1 | 0 | 0 | 2.129 | 0.004 | 2.124 | 0.000 | 2128.568 | 2128.568 | 2128.568 |
| tool:mcp__agency__inspect_module_inputs | 3/3 | 0 | 0 | 2.057 | n/a | n/a | 0.000 | 685.552 | 700.340 | 720.483 |
| sandbox:commit | 1/1 | 0 | 0 | 1.950 | 0.002 | 1.948 | 0.000 | 1950.104 | 1950.104 | 1950.104 |
| checkpoint.total | 1/1 | 0 | 0 | 1.950 | 0.002 | 1.948 | 0.000 | 1949.881 | 1949.881 | 1949.881 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.950 | 0.002 | 1.948 | 0.000 | 1949.715 | 1949.715 | 1949.715 |
| syscall:connect | 835/835 | 0 | 0 | 1.885 | n/a | n/a | 3.244 | 2.258 | 1.888 | 3.941 |
| syscall:execve | 1058/1058 | 0 | 0 | 1.544 | n/a | n/a | 3.486 | 1.459 | 1.201 | 2.644 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.426 | n/a | n/a | 67.093 | 1426.198 | 1426.198 | 1426.198 |
| harness:submit | 1/1 | 0 | 0 | 1.211 | n/a | n/a | 24.537 | 1210.869 | 1210.869 | 1210.869 |
| syscall:sendto | 508/508 | 0 | 0 | 1.167 | n/a | n/a | 2.430 | 2.298 | 1.956 | 3.986 |
| tool:update_plan | 5/5 | 0 | 0 | 0.785 | n/a | n/a | 1.381 | 157.095 | 154.347 | 165.243 |
| harness:snapshot | 1/1 | 0 | 0 | 0.750 | n/a | n/a | 0.001 | 750.383 | 750.383 | 750.383 |
| tool:mcp__agency__patch | 1/1 | 0 | 0 | 0.608 | n/a | n/a | 0.000 | 607.617 | 607.617 | 607.617 |
| sandbox:create | 1/1 | 0 | 0 | 0.339 | 0.247 | 0.092 | 0.000 | 338.644 | 338.644 | 338.644 |
| sandbox:start | 1/1 | 0 | 0 | 0.330 | 0.002 | 0.327 | 0.000 | 329.920 | 329.920 | 329.920 |
| runtime.container_create | 1/1 | 0 | 0 | 0.330 | 0.002 | 0.327 | 0.000 | 329.782 | 329.782 | 329.782 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.305 | n/a | n/a | 0.000 | 304.518 | 304.518 | 304.518 |
| tool:mcp__agency__get_current_resources | 1/1 | 0 | 0 | 0.210 | n/a | n/a | 0.060 | 210.266 | 210.266 | 210.266 |
| agency:services_close | 1/1 | 0 | 0 | 0.201 | 0.000 | 0.200 | 0.000 | 200.888 | 200.888 | 200.888 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.197 | n/a | n/a | 0.000 | 196.962 | 196.962 | 196.962 |
| sandbox:stop | 1/1 | 0 | 0 | 0.178 | 0.002 | 0.177 | 0.000 | 178.172 | 178.172 | 178.172 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.032 | 0.000 | 72.627 | 72.627 | 72.627 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.008 | 0.040 | 0.000 | 48.379 | 48.379 | 48.379 |
| run:detect | 1/1 | 0 | 0 | 0.048 | 0.001 | 0.047 | 0.000 | 47.926 | 47.926 | 47.926 |
| harness:launch | 1/1 | 0 | 0 | 0.045 | n/a | n/a | 1.232 | 45.383 | 45.383 | 45.383 |
| syscall:bind | 6/6 | 0 | 0 | 0.014 | n/a | n/a | 0.291 | 2.397 | 2.309 | 3.594 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.009 | 0.009 | 0.000 | 0.000 | 8.633 | 8.633 | 8.633 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.421 | 1.421 | 1.421 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.071 | 0.064 | 0.108 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.209 | 0.209 | 0.209 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.080 | 0.080 | 0.080 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1667 | 0.259 | 0.036 | 174.619 | 0.127 | 4.359906 CPU seconds | n/a |
| GPU 0 memory | MB | 1668 | 11947.323 | 11670.000 | 16116.000 | 11864.000 | n/a | n/a |
| GPU 0 power | W | 1668 | 46.745 | 27.990 | 75.275 | 28.137 | n/a | 78544.934 J |
| GPU 0 proc / 4553-359520 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 memory | MB | 1668 | 3271.141 | 3118.000 | 7438.000 | 3184.000 | n/a | n/a |
| GPU 0 proc / 4553-359520 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 estimated power | W | 698 | 8.292 | 0.000 | 75.275 | 0.000 | n/a | n/a |
| GPU 0 proc / 4553-359520 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 utilization | percent | 698 | 9.649 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 4632-361287 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 memory | MB | 1668 | 8194.181 | 8070.000 | 8198.000 | 8198.000 | n/a | n/a |
| GPU 0 proc / 4632-361287 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 estimated power | W | 948 | 44.079 | 0.000 | 72.856 | 0.000 | n/a | n/a |
| GPU 0 proc / 4632-361287 / sandbox / ~ / device / GPU-8e16919c-0cb9-2d56-f3e0-797be21943f3 utilization | percent | 948 | 61.014 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1668 | 11465.323 | 11188.000 | 15634.000 | 11382.000 | n/a | n/a |
| GPU 0 utilization | percent | 1668 | 40.147 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1668 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1667 | 0.948 | 0.049 | 68.465 | 0.154 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1667 | 7.240 | 0.000 | 37.750 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1667 | 0.081 | 0.000 | 54.627 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1667 | 0.953 | 0.000 | 195.518 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1667 | 0.095 | 0.000 | 28.980 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1667 | 0.096 | 0.000 | 29.534 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1668 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1668 | 6854.873 | 6445.004 | 9169.621 | 6945.781 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1667 | 0.023 | 0.000 | 25.166 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1667 | 0.022 | 0.000 | 1.307 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2144) CPU | percent | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2144) io read MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2144) io write MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2144) rss_mb | MB | 1668 | 3.402 | 3.402 | 3.402 | 3.402 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2144) main thread run-queue wait | percent | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2144) vms_mb | MB | 1668 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4553) CPU | percent | 1667 | 10.742 | 0.000 | 268.255 | 0.996 | 180.510000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 4553) io read MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.427 | 0.000 | 0.531250 MB | n/a |
| Agency harness — python -m lsbench (PID 4553) io write MB/s | MB/s | 1667 | 0.753 | 0.015 | 402.007 | 0.023 | 1268.277344 MB | n/a |
| Agency harness — python -m lsbench (PID 4553) rss_mb | MB | 1668 | 2541.715 | 2128.098 | 3897.340 | 2813.285 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4553) main thread run-queue wait | percent | 1667 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000008 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 4553) vms_mb | MB | 1668 | 16182.196 | 14275.895 | 21353.152 | 16379.176 | n/a | n/a |
| Python — vllm (PID 4562) CPU | percent | 1667 | 1.129 | 0.000 | 5.945 | 0.996 | 18.980000 CPU seconds | n/a |
| Python — vllm (PID 4562) io read MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 4562) io write MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.008 | 0.000 | 0.128906 MB | n/a |
| Python — vllm (PID 4562) rss_mb | MB | 1668 | 1805.394 | 1803.000 | 1805.625 | 1805.625 | n/a | n/a |
| Python — vllm (PID 4562) main thread run-queue wait | percent | 1667 | 0.001 | 0.000 | 0.202 | 0.000 | 0.011257 run-queue seconds | n/a |
| Python — vllm (PID 4562) vms_mb | MB | 1668 | 12012.418 | 11939.750 | 12013.770 | 12013.770 | n/a | n/a |
| Python — python -c (PID 4631) CPU | percent | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 4631) io read MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4631) io write MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4631) rss_mb | MB | 1668 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| Python — python -c (PID 4631) main thread run-queue wait | percent | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 4631) vms_mb | MB | 1668 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 4632) CPU | percent | 1667 | 12.763 | 0.000 | 43.700 | 1.992 | 214.630000 CPU seconds | n/a |
| VLLM::EngineCore (PID 4632) io read MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 4632) io write MB/s | MB/s | 1667 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 4632) rss_mb | MB | 1668 | 2341.908 | 2339.406 | 2342.281 | 2342.281 | n/a | n/a |
| VLLM::EngineCore (PID 4632) main thread run-queue wait | percent | 1667 | 0.002 | 0.000 | 0.021 | 0.000 | 0.027143 run-queue seconds | n/a |
| VLLM::EngineCore (PID 4632) vms_mb | MB | 1668 | 21862.725 | 21859.750 | 21863.043 | 21863.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 4895) CPU | percent | 1640 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 4895) rss_mb | MB | 1641 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 4895) main thread run-queue wait | percent | 1640 | 0.002 | 0.000 | 1.707 | 0.000 | 0.032973 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 4895) vms_mb | MB | 1641 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 4935) CPU | percent | 1640 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 4935) rss_mb | MB | 1641 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 4935) main thread run-queue wait | percent | 1640 | 0.002 | 0.000 | 1.998 | 0.000 | 0.034326 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 4935) vms_mb | MB | 1641 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5037) CPU | percent | 1640 | 26.478 | 0.000 | 99.288 | 0.000 | 437.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5037) rss_mb | MB | 1641 | 115.433 | 3.281 | 126.492 | 126.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5037) main thread run-queue wait | percent | 1640 | 0.000 | 0.000 | 0.010 | 0.000 | 0.000151 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5037) vms_mb | MB | 1641 | 1023.427 | 4.262 | 1048.238 | 1045.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5043) CPU | percent | 1 | 99.911 | 99.911 | 99.911 | 99.911 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5043) rss_mb | MB | 2 | 55.977 | 28.066 | 83.887 | 83.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5043) main thread run-queue wait | percent | 1 | 0.009 | 0.009 | 0.009 | 0.009 | 0.000090 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5043) vms_mb | MB | 2 | 67.352 | 36.707 | 97.996 | 97.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5060) CPU | percent | 1634 | 3.085 | 0.000 | 16.899 | 3.976 | 50.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5060) rss_mb | MB | 1635 | 140.324 | 20.336 | 153.488 | 151.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5060) main thread run-queue wait | percent | 1634 | 0.003 | 0.000 | 5.000 | 0.000 | 0.050334 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5060) vms_mb | MB | 1635 | 393.421 | 294.941 | 539.688 | 422.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5089) rss_mb | MB | 1 | 3.809 | 3.809 | 3.809 | 3.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5089) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5091) rss_mb | MB | 1 | 3.797 | 3.797 | 3.797 | 3.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5091) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5092) rss_mb | MB | 1 | 11.113 | 11.113 | 11.113 | 11.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5092) vms_mb | MB | 1 | 20.762 | 20.762 | 20.762 | 20.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5095) rss_mb | MB | 1 | 63.371 | 63.371 | 63.371 | 63.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5095) vms_mb | MB | 1 | 360.359 | 360.359 | 360.359 | 360.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5110) rss_mb | MB | 1 | 3.836 | 3.836 | 3.836 | 3.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5110) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5112) rss_mb | MB | 1 | 4.020 | 4.020 | 4.020 | 4.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5112) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5114) rss_mb | MB | 1 | 19.043 | 19.043 | 19.043 | 19.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5114) vms_mb | MB | 1 | 100.484 | 100.484 | 100.484 | 100.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 5140) rss_mb | MB | 1 | 5.465 | 5.465 | 5.465 | 5.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 5140) vms_mb | MB | 1 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5185) rss_mb | MB | 1 | 7.473 | 7.473 | 7.473 | 7.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5185) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5251) rss_mb | MB | 1 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5251) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5252) rss_mb | MB | 1 | 5.090 | 5.090 | 5.090 | 5.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5252) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5314) rss_mb | MB | 1 | 15.668 | 15.668 | 15.668 | 15.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5314) vms_mb | MB | 1 | 20.270 | 20.270 | 20.270 | 20.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5340) rss_mb | MB | 1 | 18.523 | 18.523 | 18.523 | 18.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5340) vms_mb | MB | 1 | 23.176 | 23.176 | 23.176 | 23.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_weights.py (PID 5383) CPU | percent | 1 | 155.037 | 155.037 | 155.037 | 155.037 | 1.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_weights.py (PID 5383) rss_mb | MB | 2 | 129.074 | 121.465 | 136.684 | 136.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_weights.py (PID 5383) main thread run-queue wait | percent | 1 | 17.621 | 17.621 | 17.621 | 17.621 | 0.177308 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_weights.py (PID 5383) vms_mb | MB | 2 | 266.779 | 259.414 | 274.145 | 274.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5417) rss_mb | MB | 1 | 21.031 | 21.031 | 21.031 | 21.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5417) vms_mb | MB | 1 | 25.582 | 25.582 | 25.582 | 25.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5452) rss_mb | MB | 1 | 20.508 | 20.508 | 20.508 | 20.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5452) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5481) rss_mb | MB | 1 | 3.012 | 3.012 | 3.012 | 3.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5481) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5482) rss_mb | MB | 1 | 18.535 | 18.535 | 18.535 | 18.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5482) vms_mb | MB | 1 | 369.926 | 369.926 | 369.926 | 369.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5500) rss_mb | MB | 1 | 3.008 | 3.008 | 3.008 | 3.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5500) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5501) rss_mb | MB | 1 | 8.434 | 8.434 | 8.434 | 8.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5501) vms_mb | MB | 1 | 13.016 | 13.016 | 13.016 | 13.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5538) rss_mb | MB | 1 | 7.879 | 7.879 | 7.879 | 7.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5538) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5580) rss_mb | MB | 1 | 20.867 | 20.867 | 20.867 | 20.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5580) vms_mb | MB | 1 | 25.324 | 25.324 | 25.324 | 25.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5602) rss_mb | MB | 1 | 8.020 | 8.020 | 8.020 | 8.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5602) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5615) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5615) rss_mb | MB | 2 | 3.062 | 3.062 | 3.062 | 3.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5615) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5615) vms_mb | MB | 2 | 4.379 | 4.379 | 4.379 | 4.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — measure_replies.py (PID 5627) rss_mb | MB | 1 | 135.617 | 135.617 | 135.617 | 135.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — measure_replies.py (PID 5627) vms_mb | MB | 1 | 140.875 | 140.875 | 140.875 | 140.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5628) rss_mb | MB | 1 | 149.949 | 149.949 | 149.949 | 149.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5628) vms_mb | MB | 1 | 155.746 | 155.746 | 155.746 | 155.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5637) rss_mb | MB | 1 | 21.035 | 21.035 | 21.035 | 21.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5637) vms_mb | MB | 1 | 25.711 | 25.711 | 25.711 | 25.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5654) rss_mb | MB | 1 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5654) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5655) rss_mb | MB | 1 | 149.340 | 149.340 | 149.340 | 149.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5655) vms_mb | MB | 1 | 153.613 | 153.613 | 153.613 | 153.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5685) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5685) rss_mb | MB | 3 | 3.180 | 3.180 | 3.180 | 3.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5685) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5685) vms_mb | MB | 3 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — inspect_features.py (PID 5697) CPU | percent | 1 | 128.089 | 128.089 | 128.089 | 128.089 | 1.290000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — inspect_features.py (PID 5697) rss_mb | MB | 2 | 133.922 | 89.797 | 178.047 | 178.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — inspect_features.py (PID 5697) main thread run-queue wait | percent | 1 | 15.453 | 15.453 | 15.453 | 15.453 | 0.155627 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — inspect_features.py (PID 5697) vms_mb | MB | 2 | 261.342 | 201.652 | 321.031 | 321.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5699) rss_mb | MB | 1 | 19.191 | 19.191 | 19.191 | 19.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5699) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5706) rss_mb | MB | 1 | 9.758 | 9.758 | 9.758 | 9.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5706) vms_mb | MB | 1 | 13.418 | 13.418 | 13.418 | 13.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5761) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5761) rss_mb | MB | 2 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5761) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5761) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — measure_replies.py (PID 5762) rss_mb | MB | 1 | 149.406 | 149.406 | 149.406 | 149.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — measure_replies.py (PID 5762) vms_mb | MB | 1 | 155.883 | 155.883 | 155.883 | 155.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5763) rss_mb | MB | 1 | 135.453 | 135.453 | 135.453 | 135.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5763) vms_mb | MB | 1 | 140.750 | 140.750 | 140.750 | 140.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5777) rss_mb | MB | 1 | 22.125 | 22.125 | 22.125 | 22.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5777) vms_mb | MB | 1 | 26.941 | 26.941 | 26.941 | 26.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5789) rss_mb | MB | 1 | 2.621 | 2.621 | 2.621 | 2.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5789) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5794) rss_mb | MB | 1 | 15.371 | 15.371 | 15.371 | 15.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5794) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — feature_geometry.py (PID 5804) CPU | percent | 4 | 131.085 | 96.296 | 167.798 | 139.053 | 5.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — feature_geometry.py (PID 5804) rss_mb | MB | 5 | 340.418 | 18.312 | 593.715 | 394.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — feature_geometry.py (PID 5804) main thread run-queue wait | percent | 4 | 7.254 | 0.028 | 16.730 | 6.188 | 0.292188 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — feature_geometry.py (PID 5804) vms_mb | MB | 5 | 564.712 | 130.016 | 1189.828 | 535.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_geometry.py (PID 5913) CPU | percent | 1 | 99.420 | 99.420 | 99.420 | 99.420 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_geometry.py (PID 5913) rss_mb | MB | 2 | 175.641 | 100.125 | 251.156 | 251.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_geometry.py (PID 5913) main thread run-queue wait | percent | 1 | 11.275 | 11.275 | 11.275 | 11.275 | 0.113406 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_geometry.py (PID 5913) vms_mb | MB | 2 | 302.059 | 214.289 | 389.828 | 389.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5926) rss_mb | MB | 1 | 22.113 | 22.113 | 22.113 | 22.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5926) vms_mb | MB | 1 | 26.945 | 26.945 | 26.945 | 26.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5940) rss_mb | MB | 1 | 8.316 | 8.316 | 8.316 | 8.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5940) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5964) rss_mb | MB | 1 | 19.336 | 19.336 | 19.336 | 19.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5964) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5993) rss_mb | MB | 1 | 16.652 | 16.652 | 16.652 | 16.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5993) vms_mb | MB | 1 | 20.852 | 20.852 | 20.852 | 20.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — lifecycle_hook.py (PID 6006) rss_mb | MB | 1 | 10.254 | 10.254 | 10.254 | 10.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — lifecycle_hook.py (PID 6006) vms_mb | MB | 1 | 13.738 | 13.738 | 13.738 | 13.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6051) rss_mb | MB | 1 | 3.176 | 3.176 | 3.176 | 3.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6051) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6052) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6052) rss_mb | MB | 3 | 2.996 | 2.996 | 2.996 | 2.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6052) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6052) vms_mb | MB | 3 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — measure_replies.py (PID 6056) CPU | percent | 2 | 91.451 | 83.443 | 99.458 | 99.458 | 1.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — measure_replies.py (PID 6056) rss_mb | MB | 3 | 111.543 | 63.051 | 135.789 | 135.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — measure_replies.py (PID 6056) main thread run-queue wait | percent | 2 | 7.789 | 0.006 | 15.572 | 0.006 | 0.156813 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — measure_replies.py (PID 6056) vms_mb | MB | 3 | 117.061 | 69.410 | 140.887 | 140.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6058) rss_mb | MB | 1 | 21.113 | 21.113 | 21.113 | 21.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6058) vms_mb | MB | 1 | 172.223 | 172.223 | 172.223 | 172.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6072) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6072) rss_mb | MB | 3 | 3.164 | 3.164 | 3.164 | 3.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6072) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6072) vms_mb | MB | 3 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6074) CPU | percent | 2 | 146.082 | 128.214 | 163.950 | 163.950 | 2.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6074) rss_mb | MB | 3 | 164.458 | 20.656 | 265.789 | 206.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6074) main thread run-queue wait | percent | 2 | 29.879 | 15.288 | 44.469 | 44.469 | 0.601360 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6074) vms_mb | MB | 3 | 503.980 | 172.004 | 950.473 | 389.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6083) rss_mb | MB | 1 | 15.953 | 15.953 | 15.953 | 15.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6083) vms_mb | MB | 1 | 20.605 | 20.605 | 20.605 | 20.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6084) rss_mb | MB | 1 | 16.395 | 16.395 | 16.395 | 16.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6084) vms_mb | MB | 1 | 21.852 | 21.852 | 21.852 | 21.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6094) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6094) rss_mb | MB | 3 | 3.016 | 3.016 | 3.016 | 3.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6094) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6094) vms_mb | MB | 3 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6095) rss_mb | MB | 1 | 3.082 | 3.082 | 3.082 | 3.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6095) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_geometry.py (PID 6098) CPU | percent | 2 | 96.765 | 83.252 | 110.278 | 110.278 | 1.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_geometry.py (PID 6098) rss_mb | MB | 3 | 139.819 | 13.922 | 251.465 | 251.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_geometry.py (PID 6098) main thread run-queue wait | percent | 2 | 14.118 | 8.979 | 19.257 | 8.979 | 0.284684 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_geometry.py (PID 6098) vms_mb | MB | 3 | 301.842 | 167.195 | 429.625 | 429.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6099) rss_mb | MB | 1 | 10.129 | 10.129 | 10.129 | 10.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6099) vms_mb | MB | 1 | 14.785 | 14.785 | 14.785 | 14.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6102) rss_mb | MB | 1 | 18.633 | 18.633 | 18.633 | 18.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6102) vms_mb | MB | 1 | 24.332 | 24.332 | 24.332 | 24.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6109) rss_mb | MB | 1 | 17.145 | 17.145 | 17.145 | 17.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6109) vms_mb | MB | 1 | 22.145 | 22.145 | 22.145 | 22.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6134) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6134) rss_mb | MB | 7 | 3.211 | 3.211 | 3.211 | 3.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6134) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6134) vms_mb | MB | 7 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6135) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6135) rss_mb | MB | 4 | 3.219 | 3.219 | 3.219 | 3.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6135) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6135) vms_mb | MB | 4 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6138) CPU | percent | 6 | 113.338 | 49.682 | 170.073 | 163.122 | 6.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6138) rss_mb | MB | 7 | 222.616 | 151.359 | 262.457 | 237.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6138) main thread run-queue wait | percent | 6 | 51.140 | 35.647 | 70.084 | 35.647 | 3.087189 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6138) vms_mb | MB | 7 | 397.861 | 305.352 | 446.359 | 421.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6139) CPU | percent | 3 | 103.322 | 89.521 | 116.256 | 89.521 | 3.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6139) rss_mb | MB | 4 | 214.908 | 163.887 | 237.992 | 237.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6139) main thread run-queue wait | percent | 3 | 60.423 | 48.832 | 68.788 | 68.788 | 1.824458 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6139) vms_mb | MB | 4 | 527.797 | 317.949 | 950.418 | 421.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6496) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6496) rss_mb | MB | 3 | 3.195 | 3.195 | 3.195 | 3.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6496) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6496) vms_mb | MB | 3 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6498) CPU | percent | 2 | 108.346 | 98.324 | 118.368 | 118.368 | 2.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6498) rss_mb | MB | 3 | 183.973 | 21.422 | 287.609 | 287.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6498) main thread run-queue wait | percent | 2 | 16.154 | 4.136 | 28.173 | 28.173 | 0.324871 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6498) vms_mb | MB | 3 | 352.913 | 172.461 | 464.141 | 464.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6531) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6531) rss_mb | MB | 11 | 3.066 | 3.066 | 3.066 | 3.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6531) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6531) vms_mb | MB | 11 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6533) CPU | percent | 10 | 161.402 | 110.231 | 173.827 | 171.073 | 16.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6533) rss_mb | MB | 11 | 302.396 | 58.723 | 418.023 | 329.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6533) main thread run-queue wait | percent | 10 | 37.456 | 6.756 | 44.085 | 41.907 | 3.768724 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6533) vms_mb | MB | 11 | 782.746 | 210.953 | 1050.828 | 986.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6542) rss_mb | MB | 1 | 19.148 | 19.148 | 19.148 | 19.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6542) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6555) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6555) rss_mb | MB | 2 | 3.090 | 3.090 | 3.090 | 3.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6555) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6555) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6557) CPU | percent | 1 | 93.406 | 93.406 | 93.406 | 93.406 | 0.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6557) rss_mb | MB | 2 | 89.189 | 23.707 | 154.672 | 154.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6557) main thread run-queue wait | percent | 1 | 0.019 | 0.019 | 0.019 | 0.019 | 0.000192 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6557) vms_mb | MB | 2 | 255.953 | 175.488 | 336.418 | 336.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 6560) rss_mb | MB | 1 | 149.109 | 149.109 | 149.109 | 149.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 6560) vms_mb | MB | 1 | 399.676 | 399.676 | 399.676 | 399.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6604) rss_mb | MB | 1 | 14.918 | 14.918 | 14.918 | 14.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6604) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6627) rss_mb | MB | 1 | 22.090 | 22.090 | 22.090 | 22.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6627) vms_mb | MB | 1 | 27.066 | 27.066 | 27.066 | 27.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_math_adapter.py (PID 6628) rss_mb | MB | 1 | 163.121 | 163.121 | 163.121 | 163.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_math_adapter.py (PID 6628) vms_mb | MB | 1 | 343.570 | 343.570 | 343.570 | 343.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6639) rss_mb | MB | 1 | 7.621 | 7.621 | 7.621 | 7.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6639) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6640) rss_mb | MB | 1 | 7.434 | 7.434 | 7.434 | 7.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6640) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6665) rss_mb | MB | 1 | 8.766 | 8.766 | 8.766 | 8.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6665) vms_mb | MB | 1 | 13.285 | 13.285 | 13.285 | 13.285 | n/a | n/a |
| docker commit (PID 6716) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6716) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6716) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6716) rss_mb | MB | 2 | 28.660 | 28.660 | 28.660 | 28.660 | n/a | n/a |
| docker commit (PID 6716) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6716) vms_mb | MB | 2 | 1835.570 | 1835.570 | 1835.570 | 1835.570 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 1640 | 34.806 | 0.000 | 209.079 | 0.000 | 574.827064 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1640 | 0.935 | 0.000 | 68.270 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1640 | 0.937 | 0.000 | 68.339 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 1640 | 0.021 | 0.000 | 17.530 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 1640 | 0.021 | 0.000 | 17.597 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 1640 | 0.082 | 0.000 | 54.627 | 0.000 | 135.183594 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 1640 | 0.152 | 0.000 | 62.604 | 0.000 | 251.855469 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 1641 | 437.748 | 19.043 | 934.926 | 275.152 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1640 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1640 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 1640 | 0.015 | 0.000 | 24.336 | 0.000 | 24.951723 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 1640 | 0.001 | 0.000 | 0.286 | 0.000 | 1.439794 MB | n/a |
| workload total CPU | percent | 1667 | 24.643 | 1.633 | 269.777 | 2.065 | 414.279142 CPU seconds | n/a |
| workload total memory | MB | 1668 | 13357.427 | 12636.926 | 14447.832 | 13820.910 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
