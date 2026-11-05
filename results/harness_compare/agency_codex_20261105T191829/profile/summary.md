# agprof summary

- Duration: **117.380 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.009 runs/s**
- LLM: **14 calls**, 14 succeeded, 0 failed, 0 interrupted, n/a reported retries, 106.138 s total wait
- Tools: **13/13 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **21432** at 1.991 Hz effective (2 Hz configured)
- GPU sampling: **unavailable** (not requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 117341.356 / 117341.356 ms |
| LLM latency p50 / p95 | 4605.075 / 19270.265 ms |
| LLM TTFT p50 / p95 | 4344.936 / 16349.853 ms |
| LLM input / output tokens | 183346 / 4325 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 14 total, 14 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {"unmatched_completions": 340}
- codex: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 5/5 | 5 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 4/4 | 4 | 0 | 0 | n/a | n/a |
| update_plan | 4/4 | 4 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 2.890% | 61.633% | 3.374 s | 171.634 MB | 201.672 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| tail | 5031 |  | 233 | 0.000% | 0.000% | 0.000 s | 1.711 MB | 1.711 MB | 5.664 MB | 5.664 MB | 0.000000 MB | 0.000000 MB |
| sshd | 4977 |  | 233 | 0.000% | 0.000% | 0.000 s | 10.266 MB | 10.266 MB | 14.406 MB | 14.406 MB | n/a MB | n/a MB |
| timeout | 5029 |  | 233 | 0.000% | 0.000% | 0.000 s | 1.816 MB | 1.816 MB | 5.641 MB | 5.641 MB | 0.000000 MB | 0.000000 MB |
| grep | 5030 |  | 233 | 0.000% | 0.000% | 0.000 s | 2.094 MB | 2.094 MB | 6.574 MB | 6.574 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 5163 | sandbox_agent_lso-codex_0000_0000 | 233 | 0.000% | 0.000% | 0.000 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python | 5039 |  | 233 | 2.836% | 59.709% | 3.310 s | 188.963 MB | 205.242 MB | 1121.189 MB | 1139.188 MB | 0.000000 MB | 33.617188 MB |
| bash | 5286 | sandbox_agent_lso-codex_0000_0000 | 233 | 5.026% | 99.636% | 5.860 s | 103.312 MB | 108.695 MB | 930.977 MB | 975.203 MB | n/a MB | n/a MB |
| tail | 5194 | sandbox_agent_lso-codex_0000_0000 | 233 | 0.000% | 0.000% | 0.000 s | 1.652 MB | 1.652 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| sshd | 5026 |  | 233 | 0.000% | 0.000% | 0.000 s | 7.004 MB | 7.004 MB | 14.656 MB | 14.656 MB | n/a MB | n/a MB |
| python3 | 5292 | sandbox_agent_lso-codex_0000_0000 | 3 | 100.387% | 101.047% | 1.020 s | 50.302 MB | 83.688 MB | 59.259 MB | 98.977 MB | n/a MB | n/a MB |
| bash | 5027 |  | 233 | 0.000% | 0.000% | 0.000 s | 3.508 MB | 3.508 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| uv | 5032 |  | 233 | 0.000% | 0.000% | 0.000 s | 31.662 MB | 31.789 MB | 406.655 MB | 406.684 MB | 0.000000 MB | 0.000000 MB |
| codex | 5326 | sandbox_agent_lso-codex_0000_0000 | 225 | 1.420% | 53.372% | 1.600 s | 144.363 MB | 149.730 MB | 433.431 MB | 504.781 MB | n/a MB | n/a MB |
| MainThread | 5318 | sandbox_agent_lso-codex_0000_0000 | 225 | 0.000% | 0.000% | 0.000 s | 48.926 MB | 48.926 MB | 1373.867 MB | 1373.867 MB | n/a MB | n/a MB |
| git-remote-http | 5406 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.566 MB | 18.566 MB | 100.594 MB | 100.594 MB | n/a MB | n/a MB |
| git | 5405 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.441 MB | 3.441 MB | 6.809 MB | 6.809 MB | n/a MB | n/a MB |
| git | 5404 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.895 MB | 3.895 MB | 14.812 MB | 14.812 MB | n/a MB | n/a MB |
| git | 5413 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.145 MB | 5.145 MB | 8.281 MB | 8.281 MB | n/a MB | n/a MB |
| git | 5426 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 25.656 MB | 25.656 MB | 34.770 MB | 34.770 MB | n/a MB | n/a MB |
| python3 | 5430 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.156 MB | 21.156 MB | 25.629 MB | 25.629 MB | n/a MB | n/a MB |
| python3 | 5506 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.023 MB | 21.023 MB | 25.371 MB | 25.371 MB | n/a MB | n/a MB |
| python3 | 5518 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.973 MB | 14.973 MB | 20.008 MB | 20.008 MB | n/a MB | n/a MB |
| python3 | 5526 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| bash | 5570 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.738 MB | 2.738 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5577 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.824 MB | 21.824 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| python3 | 5590 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.914 MB | 7.914 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python3 | 5597 | sandbox_agent_lso-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.246 MB | 11.246 MB | 14.746 MB | 14.746 MB | n/a MB | n/a MB |
| docker | 5626 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.461 MB | 30.461 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

_No GPU samples were collected._

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lso-codex_0000_0000 | 10.247% | 158.068% | 11.975 s | 250.847 MB | 277.199 MB | 0.000000 MB | 102.308594 MB | 61.502374 MB | 0.488353 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 5052 | 117.343 | interrupted |
| syscall:bind | -1 | 112.652 | interrupted |
| syscall:sendto | -1 | 112.647 | interrupted |
| syscall:sendto | -1 | 112.645 | interrupted |
| syscall:connect | -1 | 112.641 | interrupted |
| syscall:connect | -1 | 112.637 | interrupted |
| syscall:connect | -1 | 112.635 | interrupted |
| syscall:connect | -1 | 112.633 | interrupted |
| syscall:connect | -1 | 112.630 | interrupted |
| syscall:connect | -1 | 112.628 | interrupted |
| syscall:connect | -1 | 112.626 | interrupted |
| syscall:connect | -1 | 112.623 | interrupted |
| syscall:connect | -1 | 112.621 | interrupted |
| syscall:sendto | -1 | 112.617 | interrupted |
| syscall:sendto | -1 | 112.611 | interrupted |
| syscall:sendto | -1 | 112.606 | interrupted |
| syscall:sendto | -1 | 112.602 | interrupted |
| syscall:connect | -1 | 112.518 | interrupted |
| syscall:connect | -1 | 112.514 | interrupted |
| syscall:connect | -1 | 112.511 | interrupted |
| syscall:bind | -1 | 112.506 | interrupted |
| syscall:sendto | -1 | 112.505 | interrupted |
| syscall:connect | -1 | 112.503 | interrupted |
| syscall:sendto | -1 | 112.503 | interrupted |
| syscall:sendto | -1 | 112.502 | interrupted |
| syscall:connect | -1 | 112.498 | interrupted |
| syscall:sendto | -1 | 112.490 | interrupted |
| syscall:sendto | -1 | 112.465 | interrupted |
| syscall:sendto | -1 | 112.458 | interrupted |
| syscall:bind | -1 | 112.458 | interrupted |
| syscall:sendto | -1 | 112.455 | interrupted |
| syscall:sendto | -1 | 112.454 | interrupted |
| syscall:sendto | -1 | 112.454 | interrupted |
| syscall:sendto | -1 | 112.451 | interrupted |
| syscall:sendto | -1 | 112.445 | interrupted |
| syscall:sendto | -1 | 112.441 | interrupted |
| syscall:sendto | -1 | 112.441 | interrupted |
| syscall:sendto | -1 | 112.440 | interrupted |
| syscall:connect | -1 | 112.437 | interrupted |
| syscall:connect | -1 | 112.431 | interrupted |
| syscall:connect | -1 | 112.429 | interrupted |
| syscall:connect | -1 | 112.428 | interrupted |
| syscall:connect | -1 | 112.414 | interrupted |
| syscall:sendto | -1 | 112.408 | interrupted |
| syscall:sendto | -1 | 112.402 | interrupted |
| syscall:sendto | -1 | 112.399 | interrupted |
| syscall:connect | -1 | 112.387 | interrupted |
| syscall:connect | -1 | 112.382 | interrupted |
| syscall:sendto | -1 | 112.380 | interrupted |
| syscall:sendto | -1 | 112.369 | interrupted |
| syscall:bind | -1 | 112.368 | interrupted |
| syscall:sendto | -1 | 112.364 | interrupted |
| syscall:sendto | -1 | 112.359 | interrupted |
| syscall:connect | -1 | 112.355 | interrupted |
| syscall:connect | -1 | 112.343 | interrupted |
| syscall:connect | -1 | 112.342 | interrupted |
| syscall:connect | -1 | 112.334 | interrupted |
| syscall:connect | -1 | 112.334 | interrupted |
| syscall:bind | -1 | 112.331 | interrupted |
| syscall:sendto | -1 | 112.329 | interrupted |
| syscall:connect | -1 | 112.327 | interrupted |
| syscall:sendto | -1 | 112.326 | interrupted |
| syscall:connect | -1 | 112.325 | interrupted |
| syscall:connect | -1 | 112.325 | interrupted |
| syscall:connect | -1 | 112.323 | interrupted |
| syscall:connect | -1 | 112.322 | interrupted |
| syscall:connect | -1 | 112.316 | interrupted |
| syscall:sendto | -1 | 112.315 | interrupted |
| syscall:connect | -1 | 112.314 | interrupted |
| syscall:connect | -1 | 112.312 | interrupted |
| syscall:sendto | -1 | 112.311 | interrupted |
| syscall:connect | -1 | 112.309 | interrupted |
| syscall:connect | -1 | 112.306 | interrupted |
| syscall:sendto | -1 | 112.305 | interrupted |
| syscall:connect | -1 | 112.305 | interrupted |
| syscall:connect | -1 | 112.305 | interrupted |
| syscall:connect | -1 | 112.303 | interrupted |
| syscall:connect | -1 | 112.300 | interrupted |
| syscall:connect | -1 | 112.274 | interrupted |
| syscall:connect | -1 | 112.272 | interrupted |
| syscall:sendto | -1 | 112.272 | interrupted |
| syscall:connect | -1 | 112.258 | interrupted |
| syscall:connect | -1 | 112.254 | interrupted |
| syscall:connect | -1 | 112.254 | interrupted |
| syscall:connect | -1 | 112.253 | interrupted |
| syscall:bind | -1 | 112.253 | interrupted |
| syscall:connect | -1 | 112.251 | interrupted |
| syscall:connect | -1 | 112.251 | interrupted |
| syscall:sendto | -1 | 112.248 | interrupted |
| syscall:sendto | -1 | 112.245 | interrupted |
| syscall:connect | -1 | 112.244 | interrupted |
| syscall:connect | -1 | 112.243 | interrupted |
| syscall:connect | -1 | 112.243 | interrupted |
| syscall:connect | -1 | 112.241 | interrupted |
| syscall:sendto | -1 | 112.233 | interrupted |
| syscall:connect | -1 | 112.229 | interrupted |
| syscall:connect | -1 | 112.226 | interrupted |
| syscall:sendto | -1 | 112.225 | interrupted |
| syscall:connect | -1 | 112.224 | interrupted |
| syscall:connect | -1 | 112.220 | interrupted |
| syscall:connect | -1 | 112.218 | interrupted |
| syscall:sendto | -1 | 112.218 | interrupted |
| syscall:connect | -1 | 112.216 | interrupted |
| syscall:connect | -1 | 112.216 | interrupted |
| syscall:connect | -1 | 112.214 | interrupted |
| syscall:connect | -1 | 112.211 | interrupted |
| syscall:connect | -1 | 112.209 | interrupted |
| syscall:connect | -1 | 112.204 | interrupted |
| syscall:connect | -1 | 112.203 | interrupted |
| syscall:connect | -1 | 112.202 | interrupted |
| syscall:connect | -1 | 112.199 | interrupted |
| syscall:connect | -1 | 112.196 | interrupted |
| syscall:connect | -1 | 112.192 | interrupted |
| syscall:connect | -1 | 112.188 | interrupted |
| syscall:connect | -1 | 112.186 | interrupted |
| syscall:connect | -1 | 112.183 | interrupted |
| syscall:connect | -1 | 112.178 | interrupted |
| syscall:connect | -1 | 112.175 | interrupted |
| syscall:connect | -1 | 112.170 | interrupted |
| syscall:connect | -1 | 112.167 | interrupted |
| syscall:connect | -1 | 112.165 | interrupted |
| syscall:connect | -1 | 112.160 | interrupted |
| syscall:sendto | -1 | 112.156 | interrupted |
| syscall:sendto | -1 | 112.144 | interrupted |
| syscall:sendto | -1 | 112.141 | interrupted |
| syscall:connect | -1 | 112.088 | interrupted |
| syscall:connect | -1 | 112.085 | interrupted |
| syscall:connect | -1 | 112.081 | interrupted |
| syscall:sendto | -1 | 112.078 | interrupted |
| syscall:sendto | -1 | 112.075 | interrupted |
| syscall:connect | -1 | 112.074 | interrupted |
| syscall:sendto | -1 | 112.074 | interrupted |
| syscall:sendto | -1 | 112.044 | interrupted |
| syscall:sendto | -1 | 112.042 | interrupted |
| syscall:sendto | -1 | 112.037 | interrupted |
| syscall:sendto | -1 | 112.033 | interrupted |
| syscall:sendto | -1 | 112.028 | interrupted |
| syscall:sendto | -1 | 112.025 | interrupted |
| syscall:sendto | -1 | 111.996 | interrupted |
| syscall:sendto | -1 | 111.996 | interrupted |
| syscall:sendto | -1 | 111.995 | interrupted |
| syscall:sendto | -1 | 111.995 | interrupted |
| syscall:connect | -1 | 111.952 | interrupted |
| syscall:connect | -1 | 111.950 | interrupted |
| syscall:connect | -1 | 111.905 | interrupted |
| syscall:connect | -1 | 111.902 | interrupted |
| syscall:connect | -1 | 111.801 | interrupted |
| syscall:sendto | -1 | 111.656 | interrupted |
| syscall:connect | -1 | 110.947 | interrupted |
| syscall:connect | -1 | 110.945 | interrupted |
| syscall:connect | -1 | 110.942 | interrupted |
| syscall:connect | -1 | 110.938 | interrupted |
| syscall:connect | -1 | 108.294 | interrupted |
| syscall:connect | -1 | 108.292 | interrupted |
| syscall:connect | -1 | 108.165 | interrupted |
| syscall:sendto | -1 | 108.161 | interrupted |
| syscall:sendto | -1 | 108.157 | interrupted |
| syscall:connect | -1 | 108.134 | interrupted |
| syscall:connect | -1 | 108.129 | interrupted |
| syscall:connect | -1 | 108.058 | interrupted |
| syscall:sendto | -1 | 108.053 | interrupted |
| syscall:sendto | -1 | 108.049 | interrupted |
| syscall:connect | -1 | 107.985 | interrupted |
| syscall:connect | -1 | 104.263 | interrupted |
| syscall:connect | -1 | 104.259 | interrupted |
| syscall:connect | -1 | 104.183 | interrupted |
| syscall:sendto | -1 | 104.179 | interrupted |
| syscall:sendto | -1 | 104.176 | interrupted |
| syscall:connect | -1 | 104.141 | interrupted |
| syscall:connect | -1 | 104.137 | interrupted |
| syscall:connect | -1 | 104.086 | interrupted |
| syscall:connect | -1 | 104.082 | interrupted |
| syscall:connect | -1 | 104.080 | interrupted |
| syscall:connect | -1 | 104.075 | interrupted |
| syscall:connect | -1 | 104.031 | interrupted |
| syscall:connect | -1 | 104.027 | interrupted |
| syscall:connect | -1 | 103.954 | interrupted |
| syscall:sendto | -1 | 103.952 | interrupted |
| syscall:sendto | -1 | 103.947 | interrupted |
| syscall:connect | -1 | 103.880 | interrupted |
| syscall:connect | -1 | 92.059 | interrupted |
| syscall:connect | -1 | 92.056 | interrupted |
| syscall:connect | -1 | 91.983 | interrupted |
| syscall:sendto | -1 | 91.978 | interrupted |
| syscall:sendto | -1 | 91.974 | interrupted |
| syscall:connect | -1 | 91.949 | interrupted |
| syscall:connect | -1 | 91.948 | interrupted |
| syscall:connect | -1 | 91.820 | interrupted |
| syscall:connect | -1 | 91.816 | interrupted |
| syscall:connect | -1 | 91.740 | interrupted |
| syscall:sendto | -1 | 91.736 | interrupted |
| syscall:sendto | -1 | 91.732 | interrupted |
| syscall:connect | -1 | 91.646 | interrupted |
| syscall:connect | -1 | 73.349 | interrupted |
| syscall:connect | -1 | 73.348 | interrupted |
| syscall:connect | -1 | 73.275 | interrupted |
| syscall:sendto | -1 | 73.270 | interrupted |
| syscall:sendto | -1 | 73.266 | interrupted |
| syscall:connect | -1 | 73.244 | interrupted |
| syscall:connect | -1 | 73.239 | interrupted |
| syscall:connect | -1 | 73.167 | interrupted |
| syscall:sendto | -1 | 73.163 | interrupted |
| syscall:sendto | -1 | 73.161 | interrupted |
| syscall:connect | -1 | 73.091 | interrupted |
| syscall:connect | -1 | 62.795 | interrupted |
| syscall:connect | -1 | 62.791 | interrupted |
| syscall:connect | -1 | 62.719 | interrupted |
| syscall:sendto | -1 | 62.715 | interrupted |
| syscall:sendto | -1 | 62.711 | interrupted |
| syscall:connect | -1 | 62.686 | interrupted |
| syscall:connect | -1 | 62.682 | interrupted |
| syscall:connect | -1 | 62.543 | interrupted |
| syscall:connect | -1 | 62.539 | interrupted |
| syscall:connect | -1 | 62.465 | interrupted |
| syscall:sendto | -1 | 62.462 | interrupted |
| syscall:sendto | -1 | 62.457 | interrupted |
| syscall:connect | -1 | 62.388 | interrupted |
| syscall:bind | -1 | 52.762 | interrupted |
| syscall:sendto | -1 | 52.759 | interrupted |
| syscall:sendto | -1 | 52.757 | interrupted |
| syscall:connect | -1 | 52.752 | interrupted |
| syscall:connect | -1 | 52.748 | interrupted |
| syscall:connect | -1 | 52.744 | interrupted |
| syscall:connect | -1 | 52.740 | interrupted |
| syscall:connect | -1 | 52.735 | interrupted |
| syscall:sendto | -1 | 52.731 | interrupted |
| syscall:sendto | -1 | 52.724 | interrupted |
| syscall:sendto | -1 | 52.721 | interrupted |
| syscall:sendto | -1 | 52.719 | interrupted |
| syscall:sendto | -1 | 52.715 | interrupted |
| syscall:sendto | -1 | 52.710 | interrupted |
| syscall:sendto | -1 | 52.706 | interrupted |
| syscall:sendto | -1 | 52.702 | interrupted |
| syscall:sendto | -1 | 52.700 | interrupted |
| syscall:sendto | -1 | 52.697 | interrupted |
| syscall:sendto | -1 | 52.693 | interrupted |
| syscall:sendto | -1 | 52.689 | interrupted |
| syscall:sendto | -1 | 52.685 | interrupted |
| syscall:sendto | -1 | 52.682 | interrupted |
| syscall:sendto | -1 | 52.678 | interrupted |
| syscall:sendto | -1 | 52.674 | interrupted |
| syscall:sendto | -1 | 52.669 | interrupted |
| syscall:sendto | -1 | 52.665 | interrupted |
| syscall:sendto | -1 | 52.661 | interrupted |
| syscall:sendto | -1 | 52.660 | interrupted |
| syscall:connect | -1 | 41.170 | interrupted |
| syscall:connect | -1 | 41.166 | interrupted |
| syscall:connect | -1 | 41.091 | interrupted |
| syscall:sendto | -1 | 41.087 | interrupted |
| syscall:sendto | -1 | 41.083 | interrupted |
| syscall:connect | -1 | 41.059 | interrupted |
| syscall:connect | -1 | 41.055 | interrupted |
| syscall:connect | -1 | 40.924 | interrupted |
| syscall:connect | -1 | 40.920 | interrupted |
| syscall:connect | -1 | 40.842 | interrupted |
| syscall:sendto | -1 | 40.838 | interrupted |
| syscall:sendto | -1 | 40.834 | interrupted |
| syscall:connect | -1 | 40.771 | interrupted |
| syscall:connect | -1 | 30.352 | interrupted |
| syscall:connect | -1 | 30.352 | interrupted |
| syscall:connect | -1 | 30.278 | interrupted |
| syscall:sendto | -1 | 30.274 | interrupted |
| syscall:sendto | -1 | 30.270 | interrupted |
| syscall:connect | -1 | 30.247 | interrupted |
| syscall:connect | -1 | 30.243 | interrupted |
| syscall:connect | -1 | 30.171 | interrupted |
| syscall:sendto | -1 | 30.169 | interrupted |
| syscall:sendto | -1 | 30.165 | interrupted |
| syscall:connect | -1 | 30.099 | interrupted |
| syscall:connect | -1 | 20.264 | interrupted |
| syscall:connect | -1 | 20.259 | interrupted |
| syscall:connect | -1 | 20.185 | interrupted |
| syscall:sendto | -1 | 20.181 | interrupted |
| syscall:sendto | -1 | 20.177 | interrupted |
| syscall:connect | -1 | 20.152 | interrupted |
| syscall:connect | -1 | 20.148 | interrupted |
| syscall:connect | -1 | 20.001 | interrupted |
| syscall:connect | -1 | 19.997 | interrupted |
| syscall:connect | -1 | 19.923 | interrupted |
| syscall:sendto | -1 | 19.920 | interrupted |
| syscall:sendto | -1 | 19.915 | interrupted |
| syscall:connect | -1 | 19.845 | interrupted |
| syscall:connect | -1 | 17.234 | interrupted |
| syscall:connect | -1 | 17.230 | interrupted |
| syscall:connect | -1 | 17.155 | interrupted |
| syscall:sendto | -1 | 17.151 | interrupted |
| syscall:sendto | -1 | 17.146 | interrupted |
| syscall:connect | -1 | 17.132 | interrupted |
| syscall:connect | -1 | 17.097 | interrupted |
| syscall:connect | -1 | 17.095 | interrupted |
| syscall:connect | -1 | 17.023 | interrupted |
| syscall:sendto | -1 | 17.019 | interrupted |
| syscall:sendto | -1 | 17.014 | interrupted |
| syscall:connect | -1 | 16.937 | interrupted |
| syscall:connect | -1 | 14.893 | interrupted |
| syscall:connect | -1 | 14.889 | interrupted |
| syscall:connect | -1 | 14.815 | interrupted |
| syscall:sendto | -1 | 14.811 | interrupted |
| syscall:sendto | -1 | 14.806 | interrupted |
| syscall:connect | -1 | 14.760 | interrupted |
| syscall:connect | -1 | 14.758 | interrupted |
| syscall:connect | -1 | 14.683 | interrupted |
| syscall:sendto | -1 | 14.679 | interrupted |
| syscall:sendto | -1 | 14.675 | interrupted |
| syscall:connect | -1 | 14.607 | interrupted |
| syscall:connect | -1 | 12.464 | interrupted |
| syscall:connect | -1 | 12.460 | interrupted |
| syscall:connect | -1 | 12.385 | interrupted |
| syscall:sendto | -1 | 12.382 | interrupted |
| syscall:sendto | -1 | 12.376 | interrupted |
| syscall:connect | -1 | 12.329 | interrupted |
| syscall:connect | -1 | 12.325 | interrupted |
| syscall:connect | -1 | 12.251 | interrupted |
| syscall:sendto | -1 | 12.247 | interrupted |
| syscall:sendto | -1 | 12.243 | interrupted |
| syscall:connect | -1 | 12.175 | interrupted |
| syscall:connect | -1 | 6.593 | interrupted |
| syscall:connect | -1 | 6.591 | interrupted |
| syscall:connect | -1 | 6.515 | interrupted |
| syscall:sendto | -1 | 6.512 | interrupted |
| syscall:sendto | -1 | 6.510 | interrupted |
| syscall:connect | -1 | 6.496 | interrupted |
| syscall:connect | -1 | 6.460 | interrupted |
| syscall:connect | -1 | 6.457 | interrupted |
| syscall:connect | -1 | 6.384 | interrupted |
| syscall:sendto | -1 | 6.381 | interrupted |
| syscall:sendto | -1 | 6.376 | interrupted |
| syscall:connect | -1 | 6.308 | interrupted |
| syscall:connect | -1 | 3.232 | interrupted |
| syscall:connect | -1 | 3.229 | interrupted |
| syscall:connect | -1 | 3.155 | interrupted |
| syscall:sendto | -1 | 3.151 | interrupted |
| syscall:sendto | -1 | 3.147 | interrupted |
| syscall:connect | -1 | 3.123 | interrupted |
| syscall:connect | -1 | 3.119 | interrupted |
| syscall:connect | -1 | 3.037 | interrupted |
| syscall:sendto | -1 | 3.037 | interrupted |
| syscall:sendto | -1 | 3.036 | interrupted |
| syscall:connect | -1 | 2.964 | interrupted |
| syscall:connect | -1 | 0.739 | interrupted |
| syscall:connect | -1 | 0.735 | interrupted |
| harness:retire | -1 | 0.159 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:recover_rank1_edit | 1/1 | 0 | 0 | 117.341 | n/a | n/a | 0.000 | 117341.356 | 117341.356 | 117341.356 |
| sync:result_wait | 1/1 | 0 | 0 | 117.341 | 0.000 | 117.341 | 0.000 | 117340.666 | 117340.666 | 117340.666 |
| engine:execute | 1/1 | 0 | 0 | 117.340 | 0.687 | 116.653 | 0.000 | 117339.992 | 117339.992 | 117339.992 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 113.562 | 0.001 | 113.561 | 0.000 | 113561.942 | 113561.942 | 113561.942 |
| harness:await_cli | 1/1 | 0 | 0 | 111.686 | n/a | n/a | 0.000 | 111686.337 | 111686.337 | 111686.337 |
| llm:attempt | 14/14 | 0 | 0 | 106.138 | 1.038 | 105.100 | 0.000 | 7581.263 | 4605.075 | 19270.265 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 2.474 | 0.546 | 1.928 | 0.000 | 2473.722 | 2473.722 | 2473.722 |
| runtime.harness_start | 1/1 | 0 | 0 | 2.473 | 0.545 | 1.928 | 0.000 | 2473.482 | 2473.482 | 2473.482 |
| run:container_call | 13/13 | 0 | 0 | 1.315 | 0.002 | 1.313 | 0.000 | 101.172 | 26.335 | 413.765 |
| tool:Bash | 5/5 | 0 | 0 | 1.235 | n/a | n/a | 0.000 | 246.913 | 249.050 | 259.591 |
| teardown:commit | 1/1 | 0 | 0 | 1.003 | 0.004 | 0.999 | 0.000 | 1002.979 | 1002.979 | 1002.979 |
| sandbox:commit | 1/1 | 0 | 0 | 0.867 | 0.002 | 0.865 | 0.000 | 867.418 | 867.418 | 867.418 |
| checkpoint.total | 1/1 | 0 | 0 | 0.867 | 0.002 | 0.865 | 0.000 | 867.311 | 867.311 | 867.311 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 0.867 | 0.002 | 0.865 | 0.000 | 867.204 | 867.204 | 867.204 |
| syscall:execve | 263/263 | 0 | 0 | 0.658 | n/a | n/a | 0.000 | 2.503 | 2.984 | 3.509 |
| harness:startup_ready | 1/1 | 0 | 0 | 0.616 | n/a | n/a | 0.000 | 615.757 | 615.757 | 615.757 |
| tool:mcp__agency__submit_output | 4/4 | 0 | 0 | 0.531 | n/a | n/a | 0.000 | 132.874 | 132.908 | 133.917 |
| harness:snapshot | 1/1 | 0 | 0 | 0.494 | n/a | n/a | 0.000 | 494.129 | 494.129 | 494.129 |
| tool:update_plan | 4/4 | 0 | 0 | 0.431 | n/a | n/a | 0.000 | 107.695 | 106.985 | 110.809 |
| harness:submit | 1/1 | 0 | 0 | 0.406 | n/a | n/a | 0.000 | 405.977 | 405.977 | 405.977 |
| sandbox:start | 1/1 | 0 | 0 | 0.262 | 0.002 | 0.260 | 0.000 | 261.935 | 261.935 | 261.935 |
| runtime.container_create | 1/1 | 0 | 0 | 0.262 | 0.002 | 0.260 | 0.000 | 261.827 | 261.827 | 261.827 |
| sandbox:stop | 1/1 | 0 | 0 | 0.135 | 0.001 | 0.134 | 0.000 | 135.325 | 135.325 | 135.325 |
| agency:services_close | 1/1 | 0 | 0 | 0.126 | 0.001 | 0.125 | 0.000 | 126.404 | 126.404 | 126.404 |
| sandbox:create | 1/1 | 0 | 0 | 0.071 | 0.006 | 0.064 | 0.000 | 70.617 | 70.617 | 70.617 |
| agency:services_start | 1/1 | 0 | 0 | 0.046 | 0.026 | 0.020 | 0.000 | 46.207 | 46.207 | 46.207 |
| agent:create | 1/1 | 0 | 0 | 0.037 | 0.005 | 0.032 | 0.000 | 36.788 | 36.788 | 36.788 |
| run:detect | 1/1 | 0 | 0 | 0.036 | 0.001 | 0.035 | 0.000 | 35.829 | 35.829 | 35.829 |
| harness:launch | 1/1 | 0 | 0 | 0.035 | n/a | n/a | 0.000 | 34.552 | 34.552 | 34.552 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.050 | 1.050 | 1.050 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.067 | 0.074 | 0.088 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.363 | 0.363 | 0.363 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.202 | 0.202 | 0.202 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.040 | 0.040 | 0.040 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| syscall:connect | 0/204 | 0 | 204 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| syscall:sendto | 0/129 | 0 | 129 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| syscall:bind | 0/7 | 0 | 7 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 232 | 0.953 | 0.016 | 167.393 | 167.393 | 1.113393 CPU seconds | n/a |
| host cpu_count | CPUs | 233 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 232 | 0.169 | 0.024 | 5.530 | 1.377 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 232 | 3.792 | 0.000 | 46.535 | 41.053 | n/a | n/a |
| host disk_read_mb_s | MB/s | 232 | 0.096 | 0.000 | 6.417 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 232 | 1.673 | 0.000 | 144.697 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 232 | 1.515 | 0.000 | 93.109 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 232 | 1.533 | 0.000 | 93.376 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 233 | 15701.543 | 15701.543 | 15701.543 | 15701.543 | n/a | n/a |
| host mem_used_mb | MB | 233 | 1047.388 | 864.961 | 1196.852 | 1009.922 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 232 | 0.000 | 0.000 | 0.002 | 0.002 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 232 | 0.000 | 0.000 | 0.002 | 0.002 | n/a | n/a |
| host net_rx_mb_s | MB/s | 232 | 0.571 | 0.000 | 104.274 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 232 | 0.014 | 0.000 | 0.587 | 0.000 | n/a | n/a |
| sshd: ubuntu [priv] (PID 4977) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sshd: ubuntu [priv] (PID 4977) rss_mb | MB | 233 | 10.266 | 10.266 | 10.266 | 10.266 | n/a | n/a |
| sshd: ubuntu [priv] (PID 4977) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sshd: ubuntu [priv] (PID 4977) vms_mb | MB | 233 | 14.406 | 14.406 | 14.406 | 14.406 | n/a | n/a |
| sshd: ubuntu@notty (PID 5026) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sshd: ubuntu@notty (PID 5026) rss_mb | MB | 233 | 7.004 | 7.004 | 7.004 | 7.004 | n/a | n/a |
| sshd: ubuntu@notty (PID 5026) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sshd: ubuntu@notty (PID 5026) vms_mb | MB | 233 | 14.656 | 14.656 | 14.656 | 14.656 | n/a | n/a |
| bash (PID 5027) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash (PID 5027) io read MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash (PID 5027) io write MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash (PID 5027) rss_mb | MB | 233 | 3.508 | 3.508 | 3.508 | 3.508 | n/a | n/a |
| bash (PID 5027) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash (PID 5027) vms_mb | MB | 233 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| timeout (PID 5029) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| timeout (PID 5029) io read MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| timeout (PID 5029) io write MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| timeout (PID 5029) rss_mb | MB | 233 | 1.816 | 1.816 | 1.816 | 1.816 | n/a | n/a |
| timeout (PID 5029) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| timeout (PID 5029) vms_mb | MB | 233 | 5.641 | 5.641 | 5.641 | 5.641 | n/a | n/a |
| grep (PID 5030) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| grep (PID 5030) io read MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| grep (PID 5030) io write MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| grep (PID 5030) rss_mb | MB | 233 | 2.094 | 2.094 | 2.094 | 2.094 | n/a | n/a |
| grep (PID 5030) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| grep (PID 5030) vms_mb | MB | 233 | 6.574 | 6.574 | 6.574 | 6.574 | n/a | n/a |
| tail (PID 5031) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| tail (PID 5031) io read MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| tail (PID 5031) io write MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| tail (PID 5031) rss_mb | MB | 233 | 1.711 | 1.711 | 1.711 | 1.711 | n/a | n/a |
| tail (PID 5031) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| tail (PID 5031) vms_mb | MB | 233 | 5.664 | 5.664 | 5.664 | 5.664 | n/a | n/a |
| uv (PID 5032) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| uv (PID 5032) io read MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| uv (PID 5032) io write MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| uv (PID 5032) rss_mb | MB | 233 | 31.662 | 31.652 | 31.789 | 31.652 | n/a | n/a |
| uv (PID 5032) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| uv (PID 5032) vms_mb | MB | 233 | 406.655 | 406.652 | 406.684 | 406.652 | n/a | n/a |
| Agency harness — run_agency.py (PID 5039) CPU | percent | 232 | 2.836 | 0.000 | 59.709 | 1.984 | 3.310000 CPU seconds | n/a |
| Agency harness — run_agency.py (PID 5039) io read MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Agency harness — run_agency.py (PID 5039) io write MB/s | MB/s | 232 | 0.288 | 0.000 | 11.452 | 0.132 | 33.617188 MB | n/a |
| Agency harness — run_agency.py (PID 5039) rss_mb | MB | 233 | 188.963 | 132.586 | 205.242 | 205.242 | n/a | n/a |
| Agency harness — run_agency.py (PID 5039) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — run_agency.py (PID 5039) vms_mb | MB | 233 | 1121.189 | 686.137 | 1139.188 | 1114.027 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — docker-init (PID 5163) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — docker-init (PID 5163) rss_mb | MB | 233 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — docker-init (PID 5163) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.004 | 0.000 | 0.000051 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — docker-init (PID 5163) vms_mb | MB | 233 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — tail (PID 5194) CPU | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — tail (PID 5194) rss_mb | MB | 233 | 1.652 | 1.652 | 1.652 | 1.652 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — tail (PID 5194) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — tail (PID 5194) vms_mb | MB | 233 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — bash (PID 5286) CPU | percent | 232 | 5.026 | 0.000 | 99.636 | 0.000 | 5.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — bash (PID 5286) rss_mb | MB | 233 | 103.312 | 3.133 | 108.695 | 108.695 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — bash (PID 5286) main thread run-queue wait | percent | 232 | 0.000 | 0.000 | 0.015 | 0.000 | 0.000135 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — bash (PID 5286) vms_mb | MB | 233 | 930.977 | 4.258 | 975.203 | 975.172 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — python -c (PID 5292) CPU | percent | 2 | 100.387 | 99.727 | 101.047 | 99.727 | 1.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — python -c (PID 5292) rss_mb | MB | 3 | 50.302 | 11.062 | 83.688 | 83.688 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — python -c (PID 5292) main thread run-queue wait | percent | 2 | 0.009 | 0.007 | 0.010 | 0.010 | 0.000089 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — python -c (PID 5292) vms_mb | MB | 3 | 59.259 | 15.145 | 98.977 | 98.977 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — node (PID 5318) CPU | percent | 224 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — node (PID 5318) rss_mb | MB | 225 | 48.926 | 48.926 | 48.926 | 48.926 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — node (PID 5318) main thread run-queue wait | percent | 224 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — node (PID 5318) vms_mb | MB | 225 | 1373.867 | 1373.867 | 1373.867 | 1373.867 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — codex (PID 5326) CPU | percent | 224 | 1.420 | 0.000 | 53.372 | 1.987 | 1.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — codex (PID 5326) rss_mb | MB | 225 | 144.363 | 57.539 | 149.730 | 149.730 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — codex (PID 5326) main thread run-queue wait | percent | 224 | 0.000 | 0.000 | 0.064 | 0.000 | 0.000319 run-queue seconds | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — codex (PID 5326) vms_mb | MB | 225 | 433.431 | 374.227 | 504.781 | 434.535 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git safe.bareRepository=explicit (PID 5404) rss_mb | MB | 1 | 3.895 | 3.895 | 3.895 | 3.895 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git safe.bareRepository=explicit (PID 5404) vms_mb | MB | 1 | 14.812 | 14.812 | 14.812 | 14.812 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git remote-https (PID 5405) rss_mb | MB | 1 | 3.441 | 3.441 | 3.441 | 3.441 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git remote-https (PID 5405) vms_mb | MB | 1 | 6.809 | 6.809 | 6.809 | 6.809 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git-remote-https (PID 5406) rss_mb | MB | 1 | 18.566 | 18.566 | 18.566 | 18.566 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git-remote-https (PID 5406) vms_mb | MB | 1 | 100.594 | 100.594 | 100.594 | 100.594 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git (PID 5413) rss_mb | MB | 1 | 5.145 | 5.145 | 5.145 | 5.145 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git (PID 5413) vms_mb | MB | 1 | 8.281 | 8.281 | 8.281 | 8.281 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git safe.bareRepository=explicit (PID 5426) rss_mb | MB | 1 | 25.656 | 25.656 | 25.656 | 25.656 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — git safe.bareRepository=explicit (PID 5426) vms_mb | MB | 1 | 34.770 | 34.770 | 34.770 | 34.770 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5430) rss_mb | MB | 1 | 21.156 | 21.156 | 21.156 | 21.156 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5430) vms_mb | MB | 1 | 25.629 | 25.629 | 25.629 | 25.629 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5506) rss_mb | MB | 1 | 21.023 | 21.023 | 21.023 | 21.023 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5506) vms_mb | MB | 1 | 25.371 | 25.371 | 25.371 | 25.371 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5518) rss_mb | MB | 1 | 14.973 | 14.973 | 14.973 | 14.973 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5518) vms_mb | MB | 1 | 20.008 | 20.008 | 20.008 | 20.008 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5526) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5526) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — bash (PID 5570) rss_mb | MB | 1 | 2.738 | 2.738 | 2.738 | 2.738 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — bash (PID 5570) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5577) rss_mb | MB | 1 | 21.824 | 21.824 | 21.824 | 21.824 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5577) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5590) rss_mb | MB | 1 | 7.914 | 7.914 | 7.914 | 7.914 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — agpolicy_hook.py (PID 5590) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — lifecycle_hook.py (PID 5597) rss_mb | MB | 1 | 11.246 | 11.246 | 11.246 | 11.246 | n/a | n/a |
| sandbox:sandbox_agent_lso-codex_0000_0000 — lifecycle_hook.py (PID 5597) vms_mb | MB | 1 | 14.746 | 14.746 | 14.746 | 14.746 | n/a | n/a |
| docker commit (PID 5626) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 5626) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5626) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5626) rss_mb | MB | 2 | 30.461 | 30.461 | 30.461 | 30.461 | n/a | n/a |
| docker commit (PID 5626) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 5626) vms_mb | MB | 2 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 CPU | percent | 232 | 10.247 | 0.000 | 158.068 | 0.000 | 11.974820 CPU seconds | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 232 | 0.091 | 0.000 | 0.991 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 232 | 0.125 | 0.000 | 4.802 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 232 | 0.011 | 0.000 | 0.883 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 232 | 0.011 | 0.000 | 0.890 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 io read MB/s | MB/s | 232 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 io write MB/s | MB/s | 232 | 0.872 | 0.000 | 143.927 | 0.000 | 102.308594 MB | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 memory | MB | 233 | 250.847 | 7.062 | 277.199 | 104.484 | n/a | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 232 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 232 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 net rx MB/s | MB/s | 232 | 0.522 | 0.000 | 100.929 | 0.000 | 61.502374 MB | n/a |
| sandbox sandbox_agent_lso-codex_0000_0000 net tx MB/s | MB/s | 232 | 0.004 | 0.000 | 0.564 | 0.000 | 0.488353 MB | n/a |
| workload total CPU | percent | 232 | 2.890 | 0.401 | 61.633 | 0.772 | 3.373566 CPU seconds | n/a |
| workload total memory | MB | 233 | 171.634 | 108.410 | 201.672 | 201.672 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
