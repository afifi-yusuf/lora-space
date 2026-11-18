# agprof summary

- Duration: **1230.191 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **85 calls**, 85 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1033.785 s total wait
- Tools: **76/76 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **113920** at 1.978 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1222665.410 / 1222665.410 ms |
| LLM latency p50 / p95 | 11355.478 / 24936.472 ms |
| LLM TTFT p50 / p95 | 5582.326 / 8250.690 ms |
| LLM input / output tokens | 7466801 / 137754 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 85 total, 85 succeeded, 0 failed, 0 interrupted |
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
| Bash | 32/32 | 32 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 14/14 | 14 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 5/5 | 5 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 6/6 | 6 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 9/9 | 9 | 0 | 0 | n/a | n/a |
| update_plan | 5/5 | 5 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 8.684% | 202.183% | 106.936 s | 10143.392 MB | 10906.668 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bash | 4782 | sandbox_agent_lsb-codex_0000_0000 | 1214 | 26.434% | 99.376% | 322.700 s | 116.675 MB | 133.504 MB | 992.370 MB | 1046.672 MB | n/a MB | n/a MB |
| lsb_grid_worker | 2151 |  | 1222 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 4378 |  | 1222 | 3.747% | 57.398% | 46.130 s | 2326.140 MB | 2326.254 MB | 21893.599 MB | 21893.738 MB | 0.000000 MB | 0.007812 MB |
| tail | 4680 | sandbox_agent_lsb-codex_0000_0000 | 1214 | 0.002% | 0.995% | 0.020 s | 1.562 MB | 1.562 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 4377 |  | 1222 | 0.000% | 0.000% | 0.000 s | 12.336 MB | 12.336 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 4327 |  | 1222 | 0.378% | 6.927% | 4.650 s | 1784.157 MB | 1784.355 MB | 11988.649 MB | 11992.234 MB | 0.003906 MB | 0.070312 MB |
| python | 4318 |  | 1222 | 4.546% | 200.935% | 55.980 s | 2750.032 MB | 3346.336 MB | 16028.144 MB | 17676.465 MB | 0.003906 MB | 943.152344 MB |
| python3 | 4788 | sandbox_agent_lsb-codex_0000_0000 | 2 | 99.901% | 99.901% | 1.010 s | 55.289 MB | 84.262 MB | 66.043 MB | 98.051 MB | n/a MB | n/a MB |
| docker-init | 4640 | sandbox_agent_lsb-codex_0000_0000 | 1214 | 0.002% | 0.995% | 0.030 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| codex | 4805 | sandbox_agent_lsb-codex_0000_0000 | 1208 | 2.594% | 28.851% | 31.530 s | 146.454 MB | 158.738 MB | 398.181 MB | 568.730 MB | n/a MB | n/a MB |
| git | 4883 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.059 MB | 4.059 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 4884 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.445 MB | 3.445 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 4888 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.344 MB | 1.344 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git-remote-http | 4885 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.645 MB | 18.645 MB | 100.590 MB | 100.590 MB | n/a MB | n/a MB |
| git | 4906 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 28.086 MB | 28.086 MB | 35.523 MB | 35.523 MB | n/a MB | n/a MB |
| python3 | 4938 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.074 MB | 18.074 MB | 23.176 MB | 23.176 MB | n/a MB | n/a MB |
| python3 | 4959 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.281 MB | 9.281 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| python3 | 4971 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.887 MB | 15.887 MB | 20.539 MB | 20.539 MB | n/a MB | n/a MB |
| python3 | 5046 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.625 MB | 6.625 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| MainThread | 5069 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 52.660 MB | 52.660 MB | 1373.953 MB | 1373.953 MB | n/a MB | n/a MB |
| bash | 5055 | sandbox_agent_lsb-codex_0000_0000 | 3 | 3.975% | 5.962% | 0.080 s | 11.038 MB | 14.992 MB | 13.999 MB | 18.766 MB | n/a MB | n/a MB |
| python | 5092 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.055 MB | 10.055 MB | 13.582 MB | 13.582 MB | n/a MB | n/a MB |
| python | 5101 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.781 MB | 9.781 MB | 13.379 MB | 13.379 MB | n/a MB | n/a MB |
| python3 | 5115 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.352 MB | 7.352 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| tokio-rt-worker | 5195 | sandbox_agent_lsb-codex_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 8.831 MB | 31.734 MB | 81.130 MB | 388.621 MB | n/a MB | n/a MB |
| python | 5222 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.570 MB | 10.570 MB | 13.582 MB | 13.582 MB | n/a MB | n/a MB |
| python | 5207 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 14.953 MB | 14.953 MB | 18.766 MB | 18.766 MB | n/a MB | n/a MB |
| python | 5231 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.156 MB | 7.156 MB | 11.668 MB | 11.668 MB | n/a MB | n/a MB |
| python | 5237 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.906 MB | 14.906 MB | 18.766 MB | 18.766 MB | n/a MB | n/a MB |
| python | 5251 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.375 MB | 9.375 MB | 13.375 MB | 13.375 MB | n/a MB | n/a MB |
| python | 5272 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.125 MB | 7.125 MB | 11.793 MB | 11.793 MB | n/a MB | n/a MB |
| python | 5258 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.891 MB | 14.891 MB | 18.766 MB | 18.766 MB | n/a MB | n/a MB |
| bash | 5338 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.090 MB | 3.090 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5339 | sandbox_agent_lsb-codex_0000_0000 | 2 | 2.982% | 2.982% | 0.030 s | 13.535 MB | 15.008 MB | 17.115 MB | 18.766 MB | n/a MB | n/a MB |
| awk | 5340 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.918 MB | 1.918 MB | 3.875 MB | 3.875 MB | n/a MB | n/a MB |
| python | 5361 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.750 MB | 8.750 MB | 13.211 MB | 13.211 MB | n/a MB | n/a MB |
| python | 5386 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.852 MB | 8.852 MB | 13.199 MB | 13.199 MB | n/a MB | n/a MB |
| awk | 5367 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.922 MB | 1.922 MB | 3.875 MB | 3.875 MB | n/a MB | n/a MB |
| python | 5366 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.160 MB | 15.160 MB | 19.031 MB | 19.031 MB | n/a MB | n/a MB |
| bash | 5455 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| awk | 5510 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.945 MB | 1.945 MB | 3.875 MB | 3.875 MB | n/a MB | n/a MB |
| python | 5509 | sandbox_agent_lsb-codex_0000_0000 | 2 | 2.976% | 2.976% | 0.030 s | 14.938 MB | 15.125 MB | 19.035 MB | 19.035 MB | n/a MB | n/a MB |
| bash | 5483 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.902 MB | 2.902 MB | 4.379 MB | 4.379 MB | n/a MB | n/a MB |
| python | 5533 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.734 MB | 8.734 MB | 13.090 MB | 13.090 MB | n/a MB | n/a MB |
| tokio-rt-worker | 5537 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 142.617 MB | 142.617 MB | 392.367 MB | 392.367 MB | n/a MB | n/a MB |
| python3 | 5574 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.289 MB | 21.289 MB | 25.840 MB | 25.840 MB | n/a MB | n/a MB |
| python | 5611 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 60.207 MB | 60.207 MB | 173.938 MB | 173.938 MB | n/a MB | n/a MB |
| python | 5637 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 72.816 MB | 72.816 MB | 77.270 MB | 77.270 MB | n/a MB | n/a MB |
| bash | 5636 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.883 MB | 2.883 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5655 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 110.465 MB | 110.465 MB | 251.910 MB | 251.910 MB | n/a MB | n/a MB |
| python3 | 5675 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.359 MB | 17.359 MB | 22.145 MB | 22.145 MB | n/a MB | n/a MB |
| python3 | 5708 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.191 MB | 16.191 MB | 20.852 MB | 20.852 MB | n/a MB | n/a MB |
| python | 5829 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 28.578 MB | 28.578 MB | 179.992 MB | 179.992 MB | n/a MB | n/a MB |
| bash | 5806 | sandbox_agent_lsb-codex_0000_0000 | 4 | 1.658% | 4.973% | 0.050 s | 5.933 MB | 14.824 MB | 7.984 MB | 18.766 MB | n/a MB | n/a MB |
| python | 5832 | sandbox_agent_lsb-codex_0000_0000 | 2 | 170.913% | 170.913% | 1.810 s | 256.279 MB | 271.395 MB | 610.900 MB | 624.527 MB | n/a MB | n/a MB |
| python | 5854 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.504 MB | 8.504 MB | 13.098 MB | 13.098 MB | n/a MB | n/a MB |
| python3 | 5862 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.398 MB | 15.398 MB | 20.402 MB | 20.402 MB | n/a MB | n/a MB |
| python | 5907 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 77.258 MB | 77.258 MB | 262.172 MB | 262.172 MB | n/a MB | n/a MB |
| bash | 5884 | sandbox_agent_lsb-codex_0000_0000 | 3 | 128.723% | 174.020% | 2.590 s | 243.794 MB | 425.328 MB | 466.784 MB | 778.203 MB | n/a MB | n/a MB |
| python3 | 5947 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.523 MB | 18.523 MB | 24.176 MB | 24.176 MB | n/a MB | n/a MB |
| bash | 5991 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.078 MB | 3.078 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 5992 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 75.504 MB | 75.504 MB | 227.230 MB | 227.230 MB | n/a MB | n/a MB |
| python3 | 6004 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.930 MB | 10.930 MB | 15.188 MB | 15.188 MB | n/a MB | n/a MB |
| python | 6062 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.852 MB | 9.852 MB | 13.508 MB | 13.508 MB | n/a MB | n/a MB |
| python | 6054 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.992% | 0.992% | 0.010 s | 14.977 MB | 15.039 MB | 18.766 MB | 18.766 MB | n/a MB | n/a MB |
| bash | 6045 | sandbox_agent_lsb-codex_0000_0000 | 3 | 2.484% | 4.969% | 0.050 s | 6.997 MB | 14.922 MB | 9.094 MB | 18.766 MB | n/a MB | n/a MB |
| python | 6070 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.316 MB | 10.316 MB | 13.582 MB | 13.582 MB | n/a MB | n/a MB |
| python | 6087 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.027 MB | 10.027 MB | 13.496 MB | 13.496 MB | n/a MB | n/a MB |
| python | 6113 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 73.242 MB | 73.242 MB | 216.234 MB | 216.234 MB | n/a MB | n/a MB |
| bash | 6109 | sandbox_agent_lsb-codex_0000_0000 | 2 | 46.635% | 46.635% | 0.470 s | 38.857 MB | 74.516 MB | 110.213 MB | 216.168 MB | n/a MB | n/a MB |
| python | 6147 | sandbox_agent_lsb-codex_0000_0000 | 7 | 165.990% | 171.992% | 10.020 s | 233.216 MB | 302.398 MB | 660.515 MB | 736.297 MB | n/a MB | n/a MB |
| python3 | 6197 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.621 MB | 7.621 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python3 | 6198 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.793 MB | 7.793 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 6225 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.148 MB | 15.148 MB | 19.027 MB | 19.027 MB | n/a MB | n/a MB |
| bash | 6212 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.137 MB | 3.137 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python | 6228 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.668 MB | 7.668 MB | 11.938 MB | 11.938 MB | n/a MB | n/a MB |
| python | 6242 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 33.730 MB | 33.730 MB | 413.145 MB | 413.145 MB | n/a MB | n/a MB |
| python3 | 6368 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.363 MB | 19.363 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python3 | 6369 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.098 MB | 16.098 MB | 20.539 MB | 20.539 MB | n/a MB | n/a MB |
| python | 6405 | sandbox_agent_lsb-codex_0000_0000 | 2 | 133.221% | 133.221% | 1.340 s | 170.268 MB | 293.191 MB | 584.219 MB | 740.195 MB | n/a MB | n/a MB |
| bash | 6403 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.008 MB | 3.008 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 6412 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.121 MB | 19.121 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python3 | 6453 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 6460 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.656 MB | 20.656 MB | 25.195 MB | 25.195 MB | n/a MB | n/a MB |
| bash | 6484 | sandbox_agent_lsb-codex_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.448 MB | 2.938 MB | 3.916 MB | 4.375 MB | n/a MB | n/a MB |
| python | 6500 | sandbox_agent_lsb-codex_0000_0000 | 5 | 166.318% | 173.027% | 6.690 s | 237.797 MB | 356.340 MB | 658.030 MB | 786.293 MB | n/a MB | n/a MB |
| python | 6535 | sandbox_agent_lsb-codex_0000_0000 | 5 | 159.588% | 173.077% | 6.420 s | 183.980 MB | 269.129 MB | 613.740 MB | 737.090 MB | n/a MB | n/a MB |
| bash | 6522 | sandbox_agent_lsb-codex_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.141 MB | 3.141 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| bash | 6570 | sandbox_agent_lsb-codex_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.930 MB | 2.930 MB | 4.371 MB | 4.371 MB | n/a MB | n/a MB |
| python | 6583 | sandbox_agent_lsb-codex_0000_0000 | 4 | 158.691% | 169.043% | 4.790 s | 163.444 MB | 244.230 MB | 529.040 MB | 675.371 MB | n/a MB | n/a MB |
| docker | 6667 |  | 2 | 0.000% | 0.000% | 0.000 s | 29.379 MB | 29.379 MB | 1843.199 MB | 1843.199 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8.076% | 100.000% | 11946.250 MB | 12716.000 MB | 32.412 W | 73.978 W | 39841.970 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 35.656% | 202.817% | 435.376 s | 288.392 MB | 702.184 MB | 0.273438 MB | 275.003906 MB | 25.268136 MB | 1.332813 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4509 | 1230.129 | interrupted |
| harness:retire | -1 | 0.402 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1222.665 | n/a | n/a | 0.273 | 1222665.410 | 1222665.410 | 1222665.410 |
| engine:execute | 1/1 | 0 | 0 | 1222.664 | 1.838 | 1220.825 | 0.273 | 1222663.729 | 1222663.729 | 1222663.729 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1216.767 | 0.011 | 1216.756 | 0.273 | 1216767.061 | 1216767.061 | 1216767.061 |
| harness:await_cli | 1/1 | 0 | 0 | 1213.114 | n/a | n/a | 0.273 | 1213113.818 | 1213113.818 | 1213113.818 |
| llm:attempt | 85/85 | 0 | 0 | 1033.785 | 10.920 | 1022.861 | 0.123 | 12162.180 | 11355.478 | 24936.472 |
| tool:Bash | 32/32 | 0 | 0 | 265.309 | n/a | n/a | 0.080 | 8290.893 | 810.426 | 29511.826 |
| tool:mcp__agency__generate | 14/14 | 0 | 0 | 94.030 | n/a | n/a | 0.000 | 6716.440 | 4569.321 | 20486.432 |
| tool:mcp__agency__trace | 9/9 | 0 | 0 | 14.475 | n/a | n/a | 0.000 | 1608.290 | 1689.398 | 2410.600 |
| tool:mcp__agency__logit_lens | 5/5 | 0 | 0 | 6.963 | n/a | n/a | 0.000 | 1392.569 | 1031.417 | 2475.050 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.059 | 0.685 | 2.374 | 0.000 | 3058.781 | 3058.781 | 3058.781 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.059 | 0.684 | 2.374 | 0.000 | 3058.528 | 3058.528 | 3058.528 |
| run:container_call | 13/13 | 0 | 0 | 2.541 | 0.003 | 2.539 | 0.000 | 195.493 | 33.659 | 866.853 |
| tool:mcp__agency__patch | 6/6 | 0 | 0 | 2.479 | n/a | n/a | 0.004 | 413.102 | 394.564 | 487.062 |
| syscall:connect | 1166/1166 | 0 | 0 | 2.284 | n/a | n/a | 0.009 | 1.959 | 1.776 | 3.511 |
| tool:mcp__agency__token_stats | 1/1 | 0 | 0 | 2.253 | n/a | n/a | 0.000 | 2253.177 | 2253.177 | 2253.177 |
| teardown:commit | 1/1 | 0 | 0 | 2.133 | 0.004 | 2.129 | 0.000 | 2133.247 | 2133.247 | 2133.247 |
| syscall:execve | 1412/1412 | 0 | 0 | 1.997 | n/a | n/a | 0.006 | 1.414 | 1.138 | 2.405 |
| sandbox:commit | 1/1 | 0 | 0 | 1.928 | 0.002 | 1.925 | 0.000 | 1927.768 | 1927.768 | 1927.768 |
| checkpoint.total | 1/1 | 0 | 0 | 1.928 | 0.002 | 1.925 | 0.000 | 1927.638 | 1927.638 | 1927.638 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.927 | 0.002 | 1.925 | 0.000 | 1927.496 | 1927.496 | 1927.496 |
| tool:mcp__agency__inspect_module_inputs | 1/1 | 0 | 0 | 1.921 | n/a | n/a | 0.000 | 1920.641 | 1920.641 | 1920.641 |
| harness:submit | 1/1 | 0 | 0 | 1.008 | n/a | n/a | 0.000 | 1007.855 | 1007.855 | 1007.855 |
| syscall:sendto | 439/439 | 0 | 0 | 0.990 | n/a | n/a | 0.002 | 2.256 | 1.954 | 4.006 |
| harness:startup_ready | 1/1 | 0 | 0 | 0.819 | n/a | n/a | 0.000 | 818.659 | 818.659 | 818.659 |
| harness:snapshot | 1/1 | 0 | 0 | 0.806 | n/a | n/a | 0.000 | 805.696 | 805.696 | 805.696 |
| tool:update_plan | 5/5 | 0 | 0 | 0.794 | n/a | n/a | 0.000 | 158.887 | 159.954 | 162.247 |
| sandbox:create | 1/1 | 0 | 0 | 0.362 | 0.273 | 0.089 | 0.000 | 361.507 | 361.507 | 361.507 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.346 | n/a | n/a | 0.000 | 345.841 | 345.841 | 345.841 |
| sandbox:start | 1/1 | 0 | 0 | 0.342 | 0.002 | 0.339 | 0.000 | 341.811 | 341.811 | 341.811 |
| runtime.container_create | 1/1 | 0 | 0 | 0.342 | 0.002 | 0.339 | 0.000 | 341.670 | 341.670 | 341.670 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 0.308 | n/a | n/a | 0.000 | 308.228 | 308.228 | 308.228 |
| sandbox:stop | 1/1 | 0 | 0 | 0.205 | 0.002 | 0.204 | 0.000 | 205.238 | 205.238 | 205.238 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.198 | n/a | n/a | 0.000 | 197.603 | 197.603 | 197.603 |
| agency:services_close | 1/1 | 0 | 0 | 0.166 | 0.001 | 0.166 | 0.000 | 166.158 | 166.158 | 166.158 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.032 | 0.000 | 72.989 | 72.989 | 72.989 |
| run:detect | 1/1 | 0 | 0 | 0.052 | 0.001 | 0.051 | 0.000 | 51.674 | 51.674 | 51.674 |
| agent:create | 1/1 | 0 | 0 | 0.047 | 0.007 | 0.040 | 0.000 | 46.706 | 46.706 | 46.706 |
| harness:launch | 1/1 | 0 | 0 | 0.046 | n/a | n/a | 0.000 | 46.399 | 46.399 | 46.399 |
| syscall:bind | 5/5 | 0 | 0 | 0.011 | n/a | n/a | 0.000 | 2.183 | 1.786 | 3.892 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.009 | 0.009 | 0.000 | 0.000 | 9.392 | 9.392 | 9.392 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.283 | 1.283 | 1.283 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.073 | 0.075 | 0.107 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.176 | 0.176 | 0.176 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.063 | 0.063 | 0.063 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1221 | 0.329 | 0.041 | 155.829 | 0.074 | 4.047712 CPU seconds | n/a |
| GPU 0 memory | MB | 1222 | 11946.250 | 11670.000 | 12716.000 | 11990.000 | n/a | n/a |
| GPU 0 power | W | 1222 | 32.412 | 27.684 | 73.978 | 28.409 | n/a | 39841.970 J |
| GPU 0 proc / 4318-158715 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 memory | MB | 1222 | 3174.191 | 3118.000 | 3914.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 4318-158715 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 estimated power | W | 821 | 1.751 | 0.000 | 60.924 | 0.000 | n/a | n/a |
| GPU 0 proc / 4318-158715 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 utilization | percent | 821 | 1.000 | 0.000 | 52.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 4378-160503 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 memory | MB | 1222 | 8290.059 | 8070.000 | 8322.000 | 8322.000 | n/a | n/a |
| GPU 0 proc / 4378-160503 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 estimated power | W | 388 | 16.758 | 0.000 | 73.978 | 0.000 | n/a | n/a |
| GPU 0 proc / 4378-160503 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 utilization | percent | 388 | 22.307 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1222 | 11464.250 | 11188.000 | 12234.000 | 11508.000 | n/a | n/a |
| GPU 0 utilization | percent | 1222 | 8.076 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1222 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1221 | 1.339 | 0.045 | 55.993 | 0.118 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1221 | 5.439 | 0.125 | 31.857 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1221 | 0.002 | 0.000 | 1.329 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1221 | 1.046 | 0.000 | 137.637 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1221 | 0.045 | 0.000 | 9.489 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1221 | 0.045 | 0.000 | 9.533 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1222 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1222 | 7006.460 | 6429.297 | 7798.422 | 7214.496 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1221 | 0.034 | 0.000 | 24.930 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1221 | 0.046 | 0.000 | 1.443 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2151) CPU | percent | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2151) io read MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2151) io write MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2151) rss_mb | MB | 1222 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2151) main thread run-queue wait | percent | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2151) vms_mb | MB | 1222 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4318) CPU | percent | 1221 | 4.546 | 0.000 | 200.935 | 0.000 | 55.980000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 4318) io read MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Agency harness — python -m lsbench (PID 4318) io write MB/s | MB/s | 1221 | 0.767 | 0.000 | 261.157 | 0.035 | 943.152344 MB | n/a |
| Agency harness — python -m lsbench (PID 4318) rss_mb | MB | 1222 | 2750.032 | 2159.680 | 3346.336 | 3132.289 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4318) main thread run-queue wait | percent | 1221 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000028 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 4318) vms_mb | MB | 1222 | 16028.144 | 14275.898 | 17676.465 | 16562.652 | n/a | n/a |
| Python — vllm (PID 4327) CPU | percent | 1221 | 0.378 | 0.000 | 6.927 | 0.000 | 4.650000 CPU seconds | n/a |
| Python — vllm (PID 4327) io read MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 4327) io write MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.008 | 0.000 | 0.070312 MB | n/a |
| Python — vllm (PID 4327) rss_mb | MB | 1222 | 1784.157 | 1782.605 | 1784.355 | 1784.355 | n/a | n/a |
| Python — vllm (PID 4327) main thread run-queue wait | percent | 1221 | 0.000 | 0.000 | 0.222 | 0.000 | 0.005544 run-queue seconds | n/a |
| Python — vllm (PID 4327) vms_mb | MB | 1222 | 11988.649 | 11919.215 | 11992.234 | 11992.234 | n/a | n/a |
| Python — python -c (PID 4377) CPU | percent | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 4377) io read MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4377) io write MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4377) rss_mb | MB | 1222 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| Python — python -c (PID 4377) main thread run-queue wait | percent | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 4377) vms_mb | MB | 1222 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 4378) CPU | percent | 1221 | 3.747 | 0.000 | 57.398 | 0.996 | 46.130000 CPU seconds | n/a |
| VLLM::EngineCore (PID 4378) io read MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 4378) io write MB/s | MB/s | 1221 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 4378) rss_mb | MB | 1222 | 2326.140 | 2325.379 | 2326.254 | 2326.254 | n/a | n/a |
| VLLM::EngineCore (PID 4378) main thread run-queue wait | percent | 1221 | 0.000 | 0.000 | 0.017 | 0.000 | 0.003653 run-queue seconds | n/a |
| VLLM::EngineCore (PID 4378) vms_mb | MB | 1222 | 21893.599 | 21892.738 | 21893.738 | 21893.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 4640) CPU | percent | 1213 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 4640) rss_mb | MB | 1214 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 4640) main thread run-queue wait | percent | 1213 | 0.007 | 0.000 | 6.032 | 0.000 | 0.082479 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 4640) vms_mb | MB | 1214 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 4680) CPU | percent | 1213 | 0.002 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 4680) rss_mb | MB | 1214 | 1.562 | 1.562 | 1.562 | 1.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 4680) main thread run-queue wait | percent | 1213 | 0.007 | 0.000 | 5.762 | 0.000 | 0.081082 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 4680) vms_mb | MB | 1214 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4782) CPU | percent | 1213 | 26.434 | 0.000 | 99.376 | 0.000 | 322.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4782) rss_mb | MB | 1214 | 116.675 | 3.078 | 133.504 | 133.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4782) main thread run-queue wait | percent | 1213 | 0.000 | 0.000 | 0.009 | 0.000 | 0.000120 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 4782) vms_mb | MB | 1214 | 992.370 | 4.262 | 1046.672 | 1045.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 4788) CPU | percent | 1 | 99.901 | 99.901 | 99.901 | 99.901 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 4788) rss_mb | MB | 2 | 55.289 | 26.316 | 84.262 | 84.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 4788) main thread run-queue wait | percent | 1 | 0.012 | 0.012 | 0.012 | 0.012 | 0.000124 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 4788) vms_mb | MB | 2 | 66.043 | 34.035 | 98.051 | 98.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 4805) CPU | percent | 1207 | 2.594 | 0.000 | 28.851 | 4.970 | 31.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 4805) rss_mb | MB | 1208 | 146.454 | 43.730 | 158.738 | 152.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 4805) main thread run-queue wait | percent | 1207 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000017 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 4805) vms_mb | MB | 1208 | 398.181 | 331.352 | 568.730 | 402.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 4883) rss_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 4883) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 4884) rss_mb | MB | 1 | 3.445 | 3.445 | 3.445 | 3.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 4884) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 4885) rss_mb | MB | 1 | 18.645 | 18.645 | 18.645 | 18.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 4885) vms_mb | MB | 1 | 100.590 | 100.590 | 100.590 | 100.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 4888) rss_mb | MB | 1 | 1.344 | 1.344 | 1.344 | 1.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 4888) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 4906) rss_mb | MB | 1 | 28.086 | 28.086 | 28.086 | 28.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 4906) vms_mb | MB | 1 | 35.523 | 35.523 | 35.523 | 35.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4938) rss_mb | MB | 1 | 18.074 | 18.074 | 18.074 | 18.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4938) vms_mb | MB | 1 | 23.176 | 23.176 | 23.176 | 23.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4959) rss_mb | MB | 1 | 9.281 | 9.281 | 9.281 | 9.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4959) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4971) rss_mb | MB | 1 | 15.887 | 15.887 | 15.887 | 15.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 4971) vms_mb | MB | 1 | 20.539 | 20.539 | 20.539 | 20.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5046) rss_mb | MB | 1 | 6.625 | 6.625 | 6.625 | 6.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5046) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5055) CPU | percent | 2 | 3.975 | 1.987 | 5.962 | 1.987 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5055) rss_mb | MB | 3 | 11.038 | 3.129 | 14.992 | 14.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5055) main thread run-queue wait | percent | 2 | 0.005 | 0.002 | 0.008 | 0.002 | 0.000095 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5055) vms_mb | MB | 3 | 13.999 | 4.465 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — node (PID 5069) rss_mb | MB | 1 | 52.660 | 52.660 | 52.660 | 52.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — node (PID 5069) vms_mb | MB | 1 | 1373.953 | 1373.953 | 1373.953 | 1373.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5092) rss_mb | MB | 1 | 10.055 | 10.055 | 10.055 | 10.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5092) vms_mb | MB | 1 | 13.582 | 13.582 | 13.582 | 13.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5101) rss_mb | MB | 1 | 9.781 | 9.781 | 9.781 | 9.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5101) vms_mb | MB | 1 | 13.379 | 13.379 | 13.379 | 13.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5115) rss_mb | MB | 1 | 7.352 | 7.352 | 7.352 | 7.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5115) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5195) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5195) rss_mb | MB | 5 | 8.831 | 3.105 | 31.734 | 3.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5195) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000003 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5195) vms_mb | MB | 5 | 81.130 | 4.258 | 388.621 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5207) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5207) rss_mb | MB | 2 | 14.953 | 14.953 | 14.953 | 14.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5207) main thread run-queue wait | percent | 1 | 0.002 | 0.002 | 0.002 | 0.002 | 0.000015 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5207) vms_mb | MB | 2 | 18.766 | 18.766 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5222) rss_mb | MB | 1 | 10.570 | 10.570 | 10.570 | 10.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5222) vms_mb | MB | 1 | 13.582 | 13.582 | 13.582 | 13.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5231) rss_mb | MB | 1 | 7.156 | 7.156 | 7.156 | 7.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5231) vms_mb | MB | 1 | 11.668 | 11.668 | 11.668 | 11.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5237) rss_mb | MB | 1 | 14.906 | 14.906 | 14.906 | 14.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5237) vms_mb | MB | 1 | 18.766 | 18.766 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5251) rss_mb | MB | 1 | 9.375 | 9.375 | 9.375 | 9.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5251) vms_mb | MB | 1 | 13.375 | 13.375 | 13.375 | 13.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5258) rss_mb | MB | 1 | 14.891 | 14.891 | 14.891 | 14.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5258) vms_mb | MB | 1 | 18.766 | 18.766 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5272) rss_mb | MB | 1 | 7.125 | 7.125 | 7.125 | 7.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5272) vms_mb | MB | 1 | 11.793 | 11.793 | 11.793 | 11.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5338) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5338) rss_mb | MB | 3 | 3.090 | 3.090 | 3.090 | 3.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5338) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5338) vms_mb | MB | 3 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5339) CPU | percent | 1 | 2.982 | 2.982 | 2.982 | 2.982 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5339) rss_mb | MB | 2 | 13.535 | 12.062 | 15.008 | 15.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5339) main thread run-queue wait | percent | 1 | 0.006 | 0.006 | 0.006 | 0.006 | 0.000058 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5339) vms_mb | MB | 2 | 17.115 | 15.465 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5340) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5340) rss_mb | MB | 2 | 1.918 | 1.918 | 1.918 | 1.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5340) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5340) vms_mb | MB | 2 | 3.875 | 3.875 | 3.875 | 3.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5361) rss_mb | MB | 1 | 8.750 | 8.750 | 8.750 | 8.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5361) vms_mb | MB | 1 | 13.211 | 13.211 | 13.211 | 13.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5366) rss_mb | MB | 1 | 15.160 | 15.160 | 15.160 | 15.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5366) vms_mb | MB | 1 | 19.031 | 19.031 | 19.031 | 19.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5367) rss_mb | MB | 1 | 1.922 | 1.922 | 1.922 | 1.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5367) vms_mb | MB | 1 | 3.875 | 3.875 | 3.875 | 3.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5386) rss_mb | MB | 1 | 8.852 | 8.852 | 8.852 | 8.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5386) vms_mb | MB | 1 | 13.199 | 13.199 | 13.199 | 13.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5455) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5455) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5483) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5483) rss_mb | MB | 2 | 2.902 | 2.902 | 2.902 | 2.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5483) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5483) vms_mb | MB | 2 | 4.379 | 4.379 | 4.379 | 4.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5509) CPU | percent | 1 | 2.976 | 2.976 | 2.976 | 2.976 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5509) rss_mb | MB | 2 | 14.938 | 14.750 | 15.125 | 15.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5509) main thread run-queue wait | percent | 1 | 0.005 | 0.005 | 0.005 | 0.005 | 0.000046 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 5509) vms_mb | MB | 2 | 19.035 | 19.035 | 19.035 | 19.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5510) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5510) rss_mb | MB | 2 | 1.945 | 1.945 | 1.945 | 1.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5510) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — awk (PID 5510) vms_mb | MB | 2 | 3.875 | 3.875 | 3.875 | 3.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5533) rss_mb | MB | 1 | 8.734 | 8.734 | 8.734 | 8.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5533) vms_mb | MB | 1 | 13.090 | 13.090 | 13.090 | 13.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5537) rss_mb | MB | 1 | 142.617 | 142.617 | 142.617 | 142.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5537) vms_mb | MB | 1 | 392.367 | 392.367 | 392.367 | 392.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5574) rss_mb | MB | 1 | 21.289 | 21.289 | 21.289 | 21.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5574) vms_mb | MB | 1 | 25.840 | 25.840 | 25.840 | 25.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 5611) rss_mb | MB | 1 | 60.207 | 60.207 | 60.207 | 60.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 5611) vms_mb | MB | 1 | 173.938 | 173.938 | 173.938 | 173.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5636) rss_mb | MB | 1 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5636) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5637) rss_mb | MB | 1 | 72.816 | 72.816 | 72.816 | 72.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5637) vms_mb | MB | 1 | 77.270 | 77.270 | 77.270 | 77.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 5655) rss_mb | MB | 1 | 110.465 | 110.465 | 110.465 | 110.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 5655) vms_mb | MB | 1 | 251.910 | 251.910 | 251.910 | 251.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5675) rss_mb | MB | 1 | 17.359 | 17.359 | 17.359 | 17.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5675) vms_mb | MB | 1 | 22.145 | 22.145 | 22.145 | 22.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5708) rss_mb | MB | 1 | 16.191 | 16.191 | 16.191 | 16.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5708) vms_mb | MB | 1 | 20.852 | 20.852 | 20.852 | 20.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5806) CPU | percent | 3 | 1.658 | 0.000 | 4.973 | 4.973 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5806) rss_mb | MB | 4 | 5.933 | 2.969 | 14.824 | 14.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5806) main thread run-queue wait | percent | 3 | 0.281 | 0.000 | 0.842 | 0.842 | 0.008468 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5806) vms_mb | MB | 4 | 7.984 | 4.391 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 5829) rss_mb | MB | 1 | 28.578 | 28.578 | 28.578 | 28.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 5829) vms_mb | MB | 1 | 179.992 | 179.992 | 179.992 | 179.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — native_subspace.py (PID 5832) CPU | percent | 1 | 170.913 | 170.913 | 170.913 | 170.913 | 1.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — native_subspace.py (PID 5832) rss_mb | MB | 2 | 256.279 | 241.164 | 271.395 | 271.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — native_subspace.py (PID 5832) main thread run-queue wait | percent | 1 | 59.899 | 59.899 | 59.899 | 59.899 | 0.634345 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — native_subspace.py (PID 5832) vms_mb | MB | 2 | 610.900 | 597.273 | 624.527 | 624.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5854) rss_mb | MB | 1 | 8.504 | 8.504 | 8.504 | 8.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5854) vms_mb | MB | 1 | 13.098 | 13.098 | 13.098 | 13.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5862) rss_mb | MB | 1 | 15.398 | 15.398 | 15.398 | 15.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5862) vms_mb | MB | 1 | 20.402 | 20.402 | 20.402 | 20.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5884) CPU | percent | 2 | 128.723 | 83.425 | 174.020 | 174.020 | 2.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5884) rss_mb | MB | 3 | 243.794 | 2.984 | 425.328 | 425.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5884) main thread run-queue wait | percent | 2 | 29.124 | 6.568 | 51.680 | 51.680 | 0.585845 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5884) vms_mb | MB | 3 | 466.784 | 4.398 | 778.203 | 778.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 5907) rss_mb | MB | 1 | 77.258 | 77.258 | 77.258 | 77.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 5907) vms_mb | MB | 1 | 262.172 | 262.172 | 262.172 | 262.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5947) rss_mb | MB | 1 | 18.523 | 18.523 | 18.523 | 18.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5947) vms_mb | MB | 1 | 24.176 | 24.176 | 24.176 | 24.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5991) rss_mb | MB | 1 | 3.078 | 3.078 | 3.078 | 3.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5991) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5992) rss_mb | MB | 1 | 75.504 | 75.504 | 75.504 | 75.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 5992) vms_mb | MB | 1 | 227.230 | 227.230 | 227.230 | 227.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6004) rss_mb | MB | 1 | 10.930 | 10.930 | 10.930 | 10.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6004) vms_mb | MB | 1 | 15.188 | 15.188 | 15.188 | 15.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6045) CPU | percent | 2 | 2.484 | 0.000 | 4.969 | 4.969 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6045) rss_mb | MB | 3 | 6.997 | 3.035 | 14.922 | 14.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6045) main thread run-queue wait | percent | 2 | 0.004 | 0.000 | 0.008 | 0.008 | 0.000078 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6045) vms_mb | MB | 3 | 9.094 | 4.258 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 6054) CPU | percent | 1 | 0.992 | 0.992 | 0.992 | 0.992 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 6054) rss_mb | MB | 2 | 14.977 | 14.914 | 15.039 | 15.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 6054) main thread run-queue wait | percent | 1 | 0.002 | 0.002 | 0.002 | 0.002 | 0.000019 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_suite.py (PID 6054) vms_mb | MB | 2 | 18.766 | 18.766 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6062) rss_mb | MB | 1 | 9.852 | 9.852 | 9.852 | 9.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6062) vms_mb | MB | 1 | 13.508 | 13.508 | 13.508 | 13.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6070) rss_mb | MB | 1 | 10.316 | 10.316 | 10.316 | 10.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6070) vms_mb | MB | 1 | 13.582 | 13.582 | 13.582 | 13.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6087) rss_mb | MB | 1 | 10.027 | 10.027 | 10.027 | 10.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6087) vms_mb | MB | 1 | 13.496 | 13.496 | 13.496 | 13.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6109) CPU | percent | 1 | 46.635 | 46.635 | 46.635 | 46.635 | 0.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6109) rss_mb | MB | 2 | 38.857 | 3.199 | 74.516 | 74.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6109) main thread run-queue wait | percent | 1 | 0.799 | 0.799 | 0.799 | 0.799 | 0.008052 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6109) vms_mb | MB | 2 | 110.213 | 4.258 | 216.168 | 216.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 6113) rss_mb | MB | 1 | 73.242 | 73.242 | 73.242 | 73.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — contrast_readout.py (PID 6113) vms_mb | MB | 1 | 216.234 | 216.234 | 216.234 | 216.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — circuit_survey.py (PID 6147) CPU | percent | 6 | 165.990 | 159.999 | 171.992 | 167.899 | 10.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — circuit_survey.py (PID 6147) rss_mb | MB | 7 | 233.216 | 135.191 | 302.398 | 257.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — circuit_survey.py (PID 6147) main thread run-queue wait | percent | 6 | 46.165 | 37.033 | 52.997 | 47.830 | 2.786838 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — circuit_survey.py (PID 6147) vms_mb | MB | 7 | 660.515 | 545.066 | 736.297 | 687.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6197) rss_mb | MB | 1 | 7.621 | 7.621 | 7.621 | 7.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6197) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6198) rss_mb | MB | 1 | 7.793 | 7.793 | 7.793 | 7.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6198) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6212) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6212) rss_mb | MB | 2 | 3.137 | 3.137 | 3.137 | 3.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6212) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6212) vms_mb | MB | 2 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_short.py (PID 6225) rss_mb | MB | 1 | 15.148 | 15.148 | 15.148 | 15.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — check_short.py (PID 6225) vms_mb | MB | 1 | 19.027 | 19.027 | 19.027 | 19.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6228) rss_mb | MB | 1 | 7.668 | 7.668 | 7.668 | 7.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6228) vms_mb | MB | 1 | 11.938 | 11.938 | 11.938 | 11.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6242) rss_mb | MB | 1 | 33.730 | 33.730 | 33.730 | 33.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6242) vms_mb | MB | 1 | 413.145 | 413.145 | 413.145 | 413.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6368) rss_mb | MB | 1 | 19.363 | 19.363 | 19.363 | 19.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6368) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6369) rss_mb | MB | 1 | 16.098 | 16.098 | 16.098 | 16.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6369) vms_mb | MB | 1 | 20.539 | 20.539 | 20.539 | 20.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6403) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6403) rss_mb | MB | 2 | 3.008 | 3.008 | 3.008 | 3.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6403) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6403) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6405) CPU | percent | 1 | 133.221 | 133.221 | 133.221 | 133.221 | 1.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6405) rss_mb | MB | 2 | 170.268 | 47.344 | 293.191 | 293.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6405) main thread run-queue wait | percent | 1 | 34.786 | 34.786 | 34.786 | 34.786 | 0.349889 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6405) vms_mb | MB | 2 | 584.219 | 428.242 | 740.195 | 740.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6412) rss_mb | MB | 1 | 19.121 | 19.121 | 19.121 | 19.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6412) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6453) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6453) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6460) rss_mb | MB | 1 | 20.656 | 20.656 | 20.656 | 20.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6460) vms_mb | MB | 1 | 25.195 | 25.195 | 25.195 | 25.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6484) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6484) rss_mb | MB | 6 | 2.448 | 0.000 | 2.938 | 2.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6484) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6484) vms_mb | MB | 6 | 3.916 | 1.621 | 4.375 | 4.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6500) CPU | percent | 4 | 166.318 | 157.075 | 173.027 | 172.048 | 6.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6500) rss_mb | MB | 5 | 237.797 | 110.922 | 356.340 | 356.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6500) main thread run-queue wait | percent | 4 | 44.392 | 36.749 | 48.464 | 48.454 | 1.785620 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6500) vms_mb | MB | 5 | 658.030 | 491.770 | 786.293 | 786.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6522) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6522) rss_mb | MB | 5 | 3.141 | 3.141 | 3.141 | 3.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6522) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6522) vms_mb | MB | 5 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6535) CPU | percent | 4 | 159.588 | 133.117 | 173.077 | 166.090 | 6.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6535) rss_mb | MB | 5 | 183.980 | 42.980 | 269.129 | 255.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6535) main thread run-queue wait | percent | 4 | 47.602 | 33.809 | 54.996 | 54.686 | 1.914881 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6535) vms_mb | MB | 5 | 613.740 | 423.805 | 737.090 | 688.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6570) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6570) rss_mb | MB | 4 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6570) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6570) vms_mb | MB | 4 | 4.371 | 4.371 | 4.371 | 4.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 6583) CPU | percent | 3 | 158.691 | 141.933 | 169.043 | 169.043 | 4.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 6583) rss_mb | MB | 4 | 163.444 | 23.012 | 244.230 | 244.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 6583) main thread run-queue wait | percent | 3 | 42.335 | 32.049 | 48.675 | 46.281 | 1.277748 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 6583) vms_mb | MB | 4 | 529.040 | 215.023 | 675.371 | 675.371 | n/a | n/a |
| docker commit (PID 6667) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6667) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6667) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6667) rss_mb | MB | 2 | 29.379 | 29.379 | 29.379 | 29.379 | n/a | n/a |
| docker commit (PID 6667) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6667) vms_mb | MB | 2 | 1843.199 | 1843.199 | 1843.199 | 1843.199 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 1213 | 35.656 | 0.000 | 202.817 | 0.000 | 435.375801 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1213 | 1.280 | 0.000 | 55.313 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1213 | 1.291 | 0.000 | 55.354 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 1213 | 0.005 | 0.000 | 0.904 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 1213 | 0.005 | 0.000 | 0.910 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 1213 | 0.000 | 0.000 | 0.113 | 0.000 | 0.273438 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 1213 | 0.225 | 0.000 | 67.877 | 0.000 | 275.003906 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 1214 | 288.392 | 18.219 | 702.184 | 122.008 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1213 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1213 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 1213 | 0.021 | 0.000 | 24.145 | 0.000 | 25.268136 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 1213 | 0.001 | 0.000 | 0.280 | 0.000 | 1.332813 MB | n/a |
| workload total CPU | percent | 1221 | 8.684 | 1.552 | 202.183 | 1.857 | 106.936271 CPU seconds | n/a |
| workload total memory | MB | 1222 | 10143.392 | 9396.379 | 10906.668 | 10691.301 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
