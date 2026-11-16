# agprof summary

- Duration: **2991.583 s**
- Runs: **1/1 completed**, 0 succeeded, 1 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **62 calls**, 62 succeeded, 0 failed, 0 interrupted, n/a reported retries, 2086.505 s total wait
- Tools: **57/59 completed**, 0 failed, 2 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **277100** at 1.974 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2991511.006 / 2991511.006 ms |
| LLM latency p50 / p95 | 24009.567 / 95936.926 ms |
| LLM TTFT p50 / p95 | 14377.070 / 21315.614 ms |
| LLM input / output tokens | 6087140 / 83387 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 62 total, 62 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {"unmatched_completions": 2}
- codex: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 19/19 | 19 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 12/12 | 12 | 0 | 0 | n/a | n/a |
| mcp__agency__get_current_resources | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 6/6 | 6 | 0 | 0 | n/a | n/a |
| mcp__agency__release_resource | 0/1 | 0 | 0 | 1 | n/a | n/a |
| mcp__agency__reserve_resource | 0/1 | 0 | 0 | 1 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__top_activations | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 5/5 | 5 | 0 | 0 | n/a | n/a |
| update_plan | 5/5 | 5 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.616% | 318.142% | 168.554 s | 5729.983 MB | 6093.602 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 4718 |  | 2974 | 0.000% | 0.000% | 0.000 s | 12.188 MB | 12.188 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 5047 | sandbox_agent_lsb-codex_0000_0000 | 2974 | 0.002% | 0.995% | 0.050 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| lsb_grid_worker | 4616 |  | 2974 | 0.000% | 0.000% | 0.000 s | 3.398 MB | 3.398 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 4719 |  | 2974 | 2.803% | 52.356% | 84.030 s | 2320.943 MB | 2321.184 MB | 21204.110 MB | 21204.410 MB | 0.000000 MB | 0.019531 MB |
| bash | 5170 | sandbox_agent_lsb-codex_0000_0000 | 2974 | 23.477% | 101.467% | 702.160 s | 113.924 MB | 136.523 MB | 972.618 MB | 975.645 MB | n/a MB | n/a MB |
| python | 4625 |  | 2974 | 2.519% | 306.625% | 75.670 s | 3045.440 MB | 3352.762 MB | 16051.177 MB | 16629.652 MB | 73.949219 MB | 376.296875 MB |
| vllm | 4630 |  | 2974 | 0.294% | 6.931% | 8.830 s | 1783.994 MB | 1784.555 MB | 11014.426 MB | 11027.047 MB | 0.007812 MB | 0.082031 MB |
| python3 | 5176 | sandbox_agent_lsb-codex_0000_0000 | 2 | 100.878% | 100.878% | 1.020 s | 41.822 MB | 70.969 MB | 48.311 MB | 79.727 MB | n/a MB | n/a MB |
| tail | 5078 | sandbox_agent_lsb-codex_0000_0000 | 2974 | 0.002% | 0.995% | 0.070 s | 1.535 MB | 1.535 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| codex | 5195 | sandbox_agent_lsb-codex_0000_0000 | 2949 | 2.192% | 26.840% | 65.040 s | 152.471 MB | 162.707 MB | 377.244 MB | 550.980 MB | n/a MB | n/a MB |
| git | 5330 | sandbox_agent_lsb-codex_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.385 MB | 2.629 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 5224 | sandbox_agent_lsb-codex_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.984 MB | 2.984 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git-remote-http | 5337 | sandbox_agent_lsb-codex_0000_0000 | 5 | 1.243% | 3.977% | 0.050 s | 6.530 MB | 17.023 MB | 45.947 MB | 99.594 MB | n/a MB | n/a MB |
| git | 5351 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.750 MB | 4.750 MB | 8.285 MB | 8.285 MB | n/a MB | n/a MB |
| git | 5347 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.039 MB | 3.039 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 5346 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.629 MB | 3.629 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git-remote-http | 5348 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.910 MB | 17.910 MB | 100.590 MB | 100.590 MB | n/a MB | n/a MB |
| python3 | 5362 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.355 MB | 21.355 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| bash | 5409 | sandbox_agent_lsb-codex_0000_0000 | 16 | 0.000% | 0.000% | 0.000 s | 2.770 MB | 2.770 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| head | 5411 | sandbox_agent_lsb-codex_0000_0000 | 16 | 0.000% | 0.000% | 0.000 s | 1.457 MB | 1.457 MB | 2.859 MB | 2.859 MB | n/a MB | n/a MB |
| find | 5410 | sandbox_agent_lsb-codex_0000_0000 | 16 | 1.260% | 2.983% | 0.190 s | 2.660 MB | 2.660 MB | 4.847 MB | 4.859 MB | n/a MB | n/a MB |
| python3 | 6060 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.078 MB | 15.078 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| python3 | 6130 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.691 MB | 21.691 MB | 27.109 MB | 27.109 MB | n/a MB | n/a MB |
| python3 | 6164 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.965 MB | 7.965 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python3 | 6204 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.215 MB | 15.215 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| python | 6260 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.363 MB | 9.363 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| python | 6245 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.441 MB | 12.441 MB | 16.508 MB | 16.508 MB | n/a MB | n/a MB |
| bash | 6244 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.004 MB | 3.004 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6289 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.102 MB | 7.102 MB | 11.797 MB | 11.797 MB | n/a MB | n/a MB |
| python | 6269 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.664 MB | 12.664 MB | 16.582 MB | 16.582 MB | n/a MB | n/a MB |
| bash | 6464 | sandbox_agent_lsb-codex_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 2.938 MB | 2.938 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6467 | sandbox_agent_lsb-codex_0000_0000 | 14 | 32.188% | 170.745% | 4.210 s | 44.435 MB | 123.816 MB | 216.498 MB | 404.195 MB | n/a MB | n/a MB |
| python | 6479 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.812 MB | 12.812 MB | 16.688 MB | 16.688 MB | n/a MB | n/a MB |
| python3 | 6504 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.367 MB | 20.367 MB | 25.117 MB | 25.117 MB | n/a MB | n/a MB |
| bash | 6681 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| python3 | 6729 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.262 MB | 21.262 MB | 26.977 MB | 26.977 MB | n/a MB | n/a MB |
| python3 | 6740 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.660 MB | 7.660 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python3 | 6789 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.785 MB | 7.785 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python | 6821 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.617 MB | 12.617 MB | 16.512 MB | 16.512 MB | n/a MB | n/a MB |
| python | 6836 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.617 MB | 12.617 MB | 16.512 MB | 16.512 MB | n/a MB | n/a MB |
| bash | 6820 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.902 MB | 2.902 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 6857 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.797 MB | 8.797 MB | 13.410 MB | 13.410 MB | n/a MB | n/a MB |
| python3 | 6878 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.773 MB | 20.773 MB | 25.758 MB | 25.758 MB | n/a MB | n/a MB |
| python | 6880 | sandbox_agent_lsb-codex_0000_0000 | 2 | 8.951% | 8.951% | 0.090 s | 71.078 MB | 89.504 MB | 295.562 MB | 311.719 MB | n/a MB | n/a MB |
| python | 6943 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.164 MB | 7.164 MB | 11.793 MB | 11.793 MB | n/a MB | n/a MB |
| tail | 6934 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 6929 | sandbox_agent_lsb-codex_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.945 MB | 2.945 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6933 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.707 MB | 12.707 MB | 16.508 MB | 16.508 MB | n/a MB | n/a MB |
| python | 6971 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python | 6957 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.625 MB | 12.625 MB | 16.496 MB | 16.496 MB | n/a MB | n/a MB |
| tail | 6958 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 6998 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.781 MB | 7.781 MB | 12.949 MB | 12.949 MB | n/a MB | n/a MB |
| python | 6982 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.711 MB | 12.711 MB | 16.594 MB | 16.594 MB | n/a MB | n/a MB |
| tail | 6983 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 7033 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.426 MB | 7.426 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| tail | 7034 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 7101 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.887 MB | 18.887 MB | 24.605 MB | 24.605 MB | n/a MB | n/a MB |
| python | 7151 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.742 MB | 12.742 MB | 16.504 MB | 16.504 MB | n/a MB | n/a MB |
| python | 7163 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.141 MB | 8.141 MB | 13.039 MB | 13.039 MB | n/a MB | n/a MB |
| bash | 7150 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.896 MB | 2.938 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 7164 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.994% | 0.994% | 0.010 s | 12.707 MB | 12.707 MB | 16.389 MB | 16.422 MB | n/a MB | n/a MB |
| python | 7169 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 311.918 MB | 311.918 MB | 323.402 MB | 323.402 MB | n/a MB | n/a MB |
| python | 7181 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.707 MB | 12.707 MB | 16.422 MB | 16.422 MB | n/a MB | n/a MB |
| python | 7229 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.312 MB | 21.312 MB | 133.648 MB | 133.648 MB | n/a MB | n/a MB |
| python3 | 7261 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.422 MB | 21.422 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| python3 | 7284 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.961 MB | 14.961 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| python3 | 7305 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.641 MB | 21.641 MB | 27.164 MB | 27.164 MB | n/a MB | n/a MB |
| bash | 7345 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.555 MB | 2.555 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 7348 | sandbox_agent_lsb-codex_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.930 MB | 2.930 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 7351 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 83.316 MB | 83.316 MB | 335.918 MB | 335.918 MB | n/a MB | n/a MB |
| python | 7354 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 13.008 MB | 13.008 MB | 16.668 MB | 16.668 MB | n/a MB | n/a MB |
| tail | 7355 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.473 MB | 1.473 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 7369 | sandbox_agent_lsb-codex_0000_0000 | 3 | 99.894% | 100.440% | 2.010 s | 8.543 MB | 8.543 MB | 13.238 MB | 13.238 MB | n/a MB | n/a MB |
| python3 | 7379 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.125 MB | 20.125 MB | 24.992 MB | 24.992 MB | n/a MB | n/a MB |
| bash | 7391 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| tokio-rt-worker | 7412 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 155.844 MB | 155.844 MB | 387.215 MB | 387.215 MB | n/a MB | n/a MB |
| python3 | 7482 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.395 MB | 9.395 MB | 13.488 MB | 13.488 MB | n/a MB | n/a MB |
| python | 7485 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 73.777 MB | 73.777 MB | 337.422 MB | 337.422 MB | n/a MB | n/a MB |
| python3 | 7528 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.797 MB | 16.797 MB | 22.066 MB | 22.066 MB | n/a MB | n/a MB |
| bash | 7544 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.934 MB | 2.934 MB | 4.402 MB | 4.402 MB | n/a MB | n/a MB |
| python | 7547 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 47.805 MB | 47.805 MB | 270.051 MB | 270.051 MB | n/a MB | n/a MB |
| python | 7550 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 47.398 MB | 47.398 MB | 269.715 MB | 269.715 MB | n/a MB | n/a MB |
| tokio-rt-worker | 7642 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 159.246 MB | 159.246 MB | 394.191 MB | 394.191 MB | n/a MB | n/a MB |
| python3 | 7649 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.047 MB | 18.047 MB | 24.098 MB | 24.098 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 5.498% | 100.000% | 11884.958 MB | 12226.000 MB | 31.057 W | 74.020 W | 92900.030 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 26.896% | 211.462% | 804.484 s | 362.124 MB | 703.113 MB | 68.156250 MB | 238.828125 MB | 25.330546 MB | 1.827250 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4934 | 2991.515 | interrupted |
| tool:mcp__agency__reserve_resource | -1 | 2889.507 | interrupted |
| tool:mcp__agency__release_resource | -1 | 347.312 | interrupted |
| harness:retire | -1 | 0.372 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 1 | 0 | 2991.511 | n/a | n/a | 68.156 | 2991511.006 | 2991511.006 | 2991511.006 |
| sync:result_wait | 1/1 | 0 | 0 | 2991.510 | 0.000 | 2991.510 | 68.156 | 2991510.047 | 2991510.047 | 2991510.047 |
| engine:execute | 1/1 | 1 | 0 | 2991.509 | 2.962 | 2988.545 | 68.156 | 2991509.368 | 2991509.368 | 2991509.368 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2967.542 | 0.004 | 2967.538 | 68.146 | 2967541.971 | 2967541.971 | 2967541.971 |
| harness:await_cli | 1/1 | 0 | 0 | 2964.117 | n/a | n/a | 63.381 | 2964117.162 | 2964117.162 | 2964117.162 |
| llm:attempt | 62/62 | 0 | 0 | 2086.505 | 9.613 | 2076.884 | 19.913 | 33653.314 | 24009.567 | 95936.926 |
| tool:Bash | 19/19 | 0 | 0 | 428.255 | n/a | n/a | 50.232 | 22539.716 | 1007.042 | 105504.171 |
| tool:mcp__agency__generate | 12/12 | 0 | 0 | 157.164 | n/a | n/a | 0.000 | 13096.987 | 12394.272 | 25363.422 |
| tool:mcp__agency__token_stats | 1/1 | 0 | 0 | 22.592 | n/a | n/a | 0.000 | 22591.773 | 22591.773 | 22591.773 |
| agency:services_close | 1/1 | 1 | 0 | 20.001 | 0.001 | 20.000 | 0.000 | 20000.731 | 20000.731 | 20000.731 |
| tool:mcp__agency__top_activations | 2/2 | 0 | 0 | 11.756 | n/a | n/a | 0.000 | 5878.236 | 5878.236 | 6298.673 |
| tool:mcp__agency__trace | 5/5 | 0 | 0 | 6.052 | n/a | n/a | 0.000 | 1210.489 | 807.803 | 2310.252 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.182 | 0.721 | 2.460 | 0.010 | 3181.564 | 3181.564 | 3181.564 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.181 | 0.721 | 2.460 | 0.010 | 3181.289 | 3181.289 | 3181.289 |
| tool:mcp__agency__logit_lens | 2/2 | 0 | 0 | 2.642 | n/a | n/a | 0.000 | 1320.923 | 1320.923 | 1779.722 |
| tool:mcp__agency__patch | 6/6 | 0 | 0 | 2.542 | n/a | n/a | 0.000 | 423.720 | 419.150 | 447.196 |
| syscall:execve | 1134/1134 | 0 | 0 | 2.525 | n/a | n/a | 2.867 | 2.227 | 1.206 | 2.433 |
| tool:mcp__agency__inspect_module_inputs | 1/1 | 0 | 0 | 2.148 | n/a | n/a | 0.000 | 2147.850 | 2147.850 | 2147.850 |
| syscall:connect | 583/583 | 0 | 0 | 1.347 | n/a | n/a | 0.284 | 2.310 | 2.002 | 4.236 |
| syscall:sendto | 435/435 | 0 | 0 | 1.079 | n/a | n/a | 0.234 | 2.481 | 2.262 | 4.469 |
| harness:submit | 1/1 | 0 | 0 | 1.008 | n/a | n/a | 2.683 | 1007.956 | 1007.956 | 1007.956 |
| tool:update_plan | 5/5 | 0 | 0 | 0.925 | n/a | n/a | 0.000 | 185.083 | 181.411 | 200.330 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.872 | n/a | n/a | 0.000 | 872.142 | 872.142 | 872.142 |
| harness:startup_ready | 1/1 | 0 | 0 | 0.820 | n/a | n/a | 1.958 | 819.602 | 819.602 | 819.602 |
| run:container_call | 12/12 | 0 | 0 | 0.812 | 0.002 | 0.809 | 0.000 | 67.628 | 27.521 | 235.075 |
| harness:snapshot | 1/1 | 0 | 0 | 0.754 | n/a | n/a | 0.000 | 754.275 | 754.275 | 754.275 |
| sandbox:start | 1/1 | 0 | 0 | 0.428 | 0.002 | 0.425 | 0.000 | 427.681 | 427.681 | 427.681 |
| runtime.container_create | 1/1 | 0 | 0 | 0.428 | 0.002 | 0.425 | 0.000 | 427.529 | 427.529 | 427.529 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 0.345 | n/a | n/a | 0.000 | 344.590 | 344.590 | 344.590 |
| sandbox:create | 1/1 | 0 | 0 | 0.335 | 0.249 | 0.086 | 0.000 | 335.374 | 335.374 | 335.374 |
| teardown:discard | 1/1 | 0 | 0 | 0.259 | 0.002 | 0.257 | 0.000 | 259.040 | 259.040 | 259.040 |
| sandbox:rm | 1/1 | 0 | 0 | 0.259 | 0.002 | 0.257 | 0.000 | 258.868 | 258.868 | 258.868 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.211 | n/a | n/a | 0.000 | 211.081 | 211.081 | 211.081 |
| tool:mcp__agency__get_current_resources | 1/1 | 0 | 0 | 0.210 | n/a | n/a | 0.000 | 209.654 | 209.654 | 209.654 |
| agency:services_start | 1/1 | 0 | 0 | 0.072 | 0.041 | 0.030 | 0.000 | 71.714 | 71.714 | 71.714 |
| sandbox:update_limits | 2/2 | 0 | 0 | 0.056 | 0.001 | 0.055 | 0.000 | 27.984 | 27.984 | 28.262 |
| agent:create | 1/1 | 0 | 0 | 0.053 | 0.008 | 0.045 | 0.000 | 52.618 | 52.618 | 52.618 |
| run:detect | 1/1 | 0 | 0 | 0.047 | 0.001 | 0.047 | 0.000 | 47.403 | 47.403 | 47.403 |
| harness:launch | 1/1 | 0 | 0 | 0.044 | n/a | n/a | 0.002 | 43.595 | 43.595 | 43.595 |
| syscall:bind | 12/12 | 0 | 0 | 0.032 | n/a | n/a | 0.023 | 2.705 | 2.637 | 4.992 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.005 | 0.005 | 0.000 | 0.000 | 4.862 | 4.862 | 4.862 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.237 | 1.237 | 1.237 |
| sync:container | 12/12 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.075 | 0.081 | 0.113 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.183 | 0.183 | 0.183 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.051 | 0.051 | 0.051 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| tool:mcp__agency__release_resource | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| tool:mcp__agency__reserve_resource | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2973 | 0.077 | 0.042 | 4.566 | 0.074 | 2.310499 CPU seconds | n/a |
| GPU 0 memory | MB | 2974 | 11884.958 | 11670.000 | 12226.000 | 11950.000 | n/a | n/a |
| GPU 0 power | W | 2974 | 31.057 | 27.488 | 74.020 | 28.683 | n/a | 92900.030 J |
| GPU 0 proc / 4625-279186 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 memory | MB | 2974 | 3168.532 | 3118.000 | 3462.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 4625-279186 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 estimated power | W | 1937 | 0.825 | 0.000 | 72.386 | 0.000 | n/a | n/a |
| GPU 0 proc / 4625-279186 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 utilization | percent | 1937 | 0.620 | 0.000 | 93.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 4719-280986 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 memory | MB | 2974 | 8234.426 | 8070.000 | 8282.000 | 8282.000 | n/a | n/a |
| GPU 0 proc / 4719-280986 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 estimated power | W | 994 | 10.830 | 0.000 | 73.377 | 0.000 | n/a | n/a |
| GPU 0 proc / 4719-280986 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 utilization | percent | 994 | 14.783 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2974 | 11402.958 | 11188.000 | 11744.000 | 11468.000 | n/a | n/a |
| GPU 0 utilization | percent | 2974 | 5.498 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2974 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2973 | 0.549 | 0.023 | 51.883 | 0.214 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2973 | 7.985 | 0.000 | 93.317 | 0.251 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2973 | 0.048 | 0.000 | 4.887 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2973 | 0.246 | 0.000 | 67.915 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2973 | 1.131 | 0.000 | 79.183 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2973 | 1.175 | 0.000 | 83.467 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 2974 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 2974 | 7118.479 | 6667.867 | 7568.215 | 7392.152 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2973 | 0.013 | 0.000 | 18.808 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2973 | 0.013 | 0.000 | 1.191 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4616) CPU | percent | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4616) io read MB/s | MB/s | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4616) io write MB/s | MB/s | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4616) rss_mb | MB | 2974 | 3.398 | 3.398 | 3.398 | 3.398 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4616) main thread run-queue wait | percent | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4616) vms_mb | MB | 2974 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4625) CPU | percent | 2973 | 2.519 | 0.000 | 306.625 | 0.000 | 75.670000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 4625) io read MB/s | MB/s | 2973 | 0.025 | 0.000 | 4.949 | 0.000 | 73.949219 MB | n/a |
| Agency harness — python -m lsbench (PID 4625) io write MB/s | MB/s | 2973 | 0.126 | 0.015 | 83.116 | 0.023 | 376.296875 MB | n/a |
| Agency harness — python -m lsbench (PID 4625) rss_mb | MB | 2974 | 3045.440 | 2557.000 | 3352.762 | 3352.762 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4625) main thread run-queue wait | percent | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 4625) vms_mb | MB | 2974 | 16051.177 | 14115.852 | 16629.652 | 16508.641 | n/a | n/a |
| Python — vllm (PID 4630) CPU | percent | 2973 | 0.294 | 0.000 | 6.931 | 0.000 | 8.830000 CPU seconds | n/a |
| Python — vllm (PID 4630) io read MB/s | MB/s | 2973 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 4630) io write MB/s | MB/s | 2973 | 0.000 | 0.000 | 0.008 | 0.000 | 0.082031 MB | n/a |
| Python — vllm (PID 4630) rss_mb | MB | 2974 | 1783.994 | 1782.305 | 1784.555 | 1784.555 | n/a | n/a |
| Python — vllm (PID 4630) main thread run-queue wait | percent | 2973 | 0.009 | 0.000 | 1.181 | 0.000 | 0.262398 run-queue seconds | n/a |
| Python — vllm (PID 4630) vms_mb | MB | 2974 | 11014.426 | 10954.027 | 11027.047 | 11027.047 | n/a | n/a |
| Python — python -c (PID 4718) CPU | percent | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 4718) io read MB/s | MB/s | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4718) io write MB/s | MB/s | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4718) rss_mb | MB | 2974 | 12.188 | 12.188 | 12.188 | 12.188 | n/a | n/a |
| Python — python -c (PID 4718) main thread run-queue wait | percent | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 4718) vms_mb | MB | 2974 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 4719) CPU | percent | 2973 | 2.803 | 0.000 | 52.356 | 0.995 | 84.030000 CPU seconds | n/a |
| VLLM::EngineCore (PID 4719) io read MB/s | MB/s | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 4719) io write MB/s | MB/s | 2973 | 0.000 | 0.000 | 0.004 | 0.000 | 0.019531 MB | n/a |
| VLLM::EngineCore (PID 4719) rss_mb | MB | 2974 | 2320.943 | 2320.309 | 2321.184 | 2321.184 | n/a | n/a |
| VLLM::EngineCore (PID 4719) main thread run-queue wait | percent | 2973 | 0.006 | 0.000 | 0.731 | 0.000 | 0.179584 run-queue seconds | n/a |
| VLLM::EngineCore (PID 4719) vms_mb | MB | 2974 | 21204.110 | 21203.121 | 21204.410 | 21204.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5047) CPU | percent | 2973 | 0.002 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5047) rss_mb | MB | 2974 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5047) main thread run-queue wait | percent | 2973 | 0.001 | 0.000 | 2.282 | 0.000 | 0.025570 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5047) vms_mb | MB | 2974 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5078) CPU | percent | 2973 | 0.002 | 0.000 | 0.995 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5078) rss_mb | MB | 2974 | 1.535 | 1.535 | 1.535 | 1.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5078) main thread run-queue wait | percent | 2973 | 0.002 | 0.000 | 4.268 | 0.000 | 0.055790 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5078) vms_mb | MB | 2974 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5170) CPU | percent | 2973 | 23.477 | 0.000 | 101.467 | 0.000 | 702.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5170) rss_mb | MB | 2974 | 113.924 | 3.059 | 136.523 | 124.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5170) main thread run-queue wait | percent | 2973 | 0.000 | 0.000 | 0.019 | 0.000 | 0.000197 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5170) vms_mb | MB | 2974 | 972.618 | 4.262 | 975.645 | 973.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5176) CPU | percent | 1 | 100.878 | 100.878 | 100.878 | 100.878 | 1.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5176) rss_mb | MB | 2 | 41.822 | 12.676 | 70.969 | 70.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5176) main thread run-queue wait | percent | 1 | 0.006 | 0.006 | 0.006 | 0.006 | 0.000060 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5176) vms_mb | MB | 2 | 48.311 | 16.895 | 79.727 | 79.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5195) CPU | percent | 2948 | 2.192 | 0.000 | 26.840 | 4.976 | 65.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5195) rss_mb | MB | 2949 | 152.471 | 55.676 | 162.707 | 159.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5195) main thread run-queue wait | percent | 2948 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000045 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5195) vms_mb | MB | 2949 | 377.244 | 337.695 | 550.980 | 396.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5224) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5224) rss_mb | MB | 6 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5224) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000015 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5224) vms_mb | MB | 6 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5330) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5330) rss_mb | MB | 6 | 2.385 | 1.164 | 2.629 | 2.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5330) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000013 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5330) vms_mb | MB | 6 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5337) CPU | percent | 4 | 1.243 | 0.000 | 3.977 | 3.977 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5337) rss_mb | MB | 5 | 6.530 | 0.410 | 17.023 | 17.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5337) main thread run-queue wait | percent | 4 | 0.004 | 0.000 | 0.014 | 0.002 | 0.000154 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5337) vms_mb | MB | 5 | 45.947 | 6.016 | 99.594 | 99.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5346) rss_mb | MB | 1 | 3.629 | 3.629 | 3.629 | 3.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5346) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5347) rss_mb | MB | 1 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5347) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5348) rss_mb | MB | 1 | 17.910 | 17.910 | 17.910 | 17.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5348) vms_mb | MB | 1 | 100.590 | 100.590 | 100.590 | 100.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 5351) rss_mb | MB | 1 | 4.750 | 4.750 | 4.750 | 4.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 5351) vms_mb | MB | 1 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5362) rss_mb | MB | 1 | 21.355 | 21.355 | 21.355 | 21.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5362) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5409) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5409) rss_mb | MB | 16 | 2.770 | 2.770 | 2.770 | 2.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5409) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5409) vms_mb | MB | 16 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 5410) CPU | percent | 15 | 1.260 | 0.000 | 2.983 | 0.994 | 0.190000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 5410) rss_mb | MB | 16 | 2.660 | 2.660 | 2.660 | 2.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 5410) main thread run-queue wait | percent | 15 | 0.004 | 0.001 | 0.018 | 0.003 | 0.000663 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 5410) vms_mb | MB | 16 | 4.847 | 4.793 | 4.859 | 4.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 5411) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 5411) rss_mb | MB | 16 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 5411) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 5411) vms_mb | MB | 16 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6060) rss_mb | MB | 1 | 15.078 | 15.078 | 15.078 | 15.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6060) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6130) rss_mb | MB | 1 | 21.691 | 21.691 | 21.691 | 21.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6130) vms_mb | MB | 1 | 27.109 | 27.109 | 27.109 | 27.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6164) rss_mb | MB | 1 | 7.965 | 7.965 | 7.965 | 7.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6164) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6204) rss_mb | MB | 1 | 15.215 | 15.215 | 15.215 | 15.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6204) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6244) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6244) rss_mb | MB | 2 | 3.004 | 3.004 | 3.004 | 3.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6244) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6244) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6245) rss_mb | MB | 1 | 12.441 | 12.441 | 12.441 | 12.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6245) vms_mb | MB | 1 | 16.508 | 16.508 | 16.508 | 16.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6260) rss_mb | MB | 1 | 9.363 | 9.363 | 9.363 | 9.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6260) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6269) rss_mb | MB | 1 | 12.664 | 12.664 | 12.664 | 12.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6269) vms_mb | MB | 1 | 16.582 | 16.582 | 16.582 | 16.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6289) rss_mb | MB | 1 | 7.102 | 7.102 | 7.102 | 7.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6289) vms_mb | MB | 1 | 11.797 | 11.797 | 11.797 | 11.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6464) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6464) rss_mb | MB | 15 | 2.938 | 2.938 | 2.938 | 2.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6464) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.001 | 0.001 | 0.000010 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6464) vms_mb | MB | 15 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 6467) CPU | percent | 13 | 32.188 | 0.000 | 170.745 | 160.181 | 4.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 6467) rss_mb | MB | 14 | 44.435 | 10.840 | 123.816 | 123.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 6467) main thread run-queue wait | percent | 13 | 5.786 | 0.000 | 46.062 | 46.062 | 0.756672 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 6467) vms_mb | MB | 14 | 216.498 | 24.672 | 404.195 | 404.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6479) rss_mb | MB | 1 | 12.812 | 12.812 | 12.812 | 12.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6479) vms_mb | MB | 1 | 16.688 | 16.688 | 16.688 | 16.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6504) rss_mb | MB | 1 | 20.367 | 20.367 | 20.367 | 20.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6504) vms_mb | MB | 1 | 25.117 | 25.117 | 25.117 | 25.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6681) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6681) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6729) rss_mb | MB | 1 | 21.262 | 21.262 | 21.262 | 21.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6729) vms_mb | MB | 1 | 26.977 | 26.977 | 26.977 | 26.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6740) rss_mb | MB | 1 | 7.660 | 7.660 | 7.660 | 7.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6740) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6789) rss_mb | MB | 1 | 7.785 | 7.785 | 7.785 | 7.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6789) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6820) rss_mb | MB | 1 | 2.902 | 2.902 | 2.902 | 2.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6820) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6821) rss_mb | MB | 1 | 12.617 | 12.617 | 12.617 | 12.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6821) vms_mb | MB | 1 | 16.512 | 16.512 | 16.512 | 16.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6836) rss_mb | MB | 1 | 12.617 | 12.617 | 12.617 | 12.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6836) vms_mb | MB | 1 | 16.512 | 16.512 | 16.512 | 16.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6857) rss_mb | MB | 1 | 8.797 | 8.797 | 8.797 | 8.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6857) vms_mb | MB | 1 | 13.410 | 13.410 | 13.410 | 13.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6878) rss_mb | MB | 1 | 20.773 | 20.773 | 20.773 | 20.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6878) vms_mb | MB | 1 | 25.758 | 25.758 | 25.758 | 25.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_heads.py (PID 6880) CPU | percent | 1 | 8.951 | 8.951 | 8.951 | 8.951 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_heads.py (PID 6880) rss_mb | MB | 2 | 71.078 | 52.652 | 89.504 | 89.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_heads.py (PID 6880) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000003 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_heads.py (PID 6880) vms_mb | MB | 2 | 295.562 | 279.406 | 311.719 | 311.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6929) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6929) rss_mb | MB | 4 | 2.945 | 2.945 | 2.945 | 2.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6929) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6929) vms_mb | MB | 4 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6933) rss_mb | MB | 1 | 12.707 | 12.707 | 12.707 | 12.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6933) vms_mb | MB | 1 | 16.508 | 16.508 | 16.508 | 16.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 6934) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 6934) vms_mb | MB | 1 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6943) rss_mb | MB | 1 | 7.164 | 7.164 | 7.164 | 7.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6943) vms_mb | MB | 1 | 11.793 | 11.793 | 11.793 | 11.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6957) rss_mb | MB | 1 | 12.625 | 12.625 | 12.625 | 12.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6957) vms_mb | MB | 1 | 16.496 | 16.496 | 16.496 | 16.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 6958) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 6958) vms_mb | MB | 1 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6971) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6971) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6982) rss_mb | MB | 1 | 12.711 | 12.711 | 12.711 | 12.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 6982) vms_mb | MB | 1 | 16.594 | 16.594 | 16.594 | 16.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 6983) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 6983) vms_mb | MB | 1 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6998) rss_mb | MB | 1 | 7.781 | 7.781 | 7.781 | 7.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 6998) vms_mb | MB | 1 | 12.949 | 12.949 | 12.949 | 12.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 7033) rss_mb | MB | 1 | 7.426 | 7.426 | 7.426 | 7.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 7033) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7034) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7034) vms_mb | MB | 1 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7101) rss_mb | MB | 1 | 18.887 | 18.887 | 18.887 | 18.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7101) vms_mb | MB | 1 | 24.605 | 24.605 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7150) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7150) rss_mb | MB | 3 | 2.896 | 2.812 | 2.938 | 2.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7150) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7150) vms_mb | MB | 3 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 7151) rss_mb | MB | 1 | 12.742 | 12.742 | 12.742 | 12.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 7151) vms_mb | MB | 1 | 16.504 | 16.504 | 16.504 | 16.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7163) rss_mb | MB | 1 | 8.141 | 8.141 | 8.141 | 8.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7163) vms_mb | MB | 1 | 13.039 | 13.039 | 13.039 | 13.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 7164) CPU | percent | 1 | 0.994 | 0.994 | 0.994 | 0.994 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 7164) rss_mb | MB | 2 | 12.707 | 12.707 | 12.707 | 12.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 7164) main thread run-queue wait | percent | 1 | 0.002 | 0.002 | 0.002 | 0.002 | 0.000019 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 7164) vms_mb | MB | 2 | 16.389 | 16.355 | 16.422 | 16.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7169) rss_mb | MB | 1 | 311.918 | 311.918 | 311.918 | 311.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7169) vms_mb | MB | 1 | 323.402 | 323.402 | 323.402 | 323.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 7181) rss_mb | MB | 1 | 12.707 | 12.707 | 12.707 | 12.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 7181) vms_mb | MB | 1 | 16.422 | 16.422 | 16.422 | 16.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_neurons.py (PID 7229) rss_mb | MB | 1 | 21.312 | 21.312 | 21.312 | 21.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_neurons.py (PID 7229) vms_mb | MB | 1 | 133.648 | 133.648 | 133.648 | 133.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7261) rss_mb | MB | 1 | 21.422 | 21.422 | 21.422 | 21.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7261) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7284) rss_mb | MB | 1 | 14.961 | 14.961 | 14.961 | 14.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7284) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7305) rss_mb | MB | 1 | 21.641 | 21.641 | 21.641 | 21.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7305) vms_mb | MB | 1 | 27.164 | 27.164 | 27.164 | 27.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7345) rss_mb | MB | 1 | 2.555 | 2.555 | 2.555 | 2.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7345) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7348) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7348) rss_mb | MB | 4 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7348) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7348) vms_mb | MB | 4 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_contrasts.py (PID 7351) rss_mb | MB | 1 | 83.316 | 83.316 | 83.316 | 83.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_contrasts.py (PID 7351) vms_mb | MB | 1 | 335.918 | 335.918 | 335.918 | 335.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 7354) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 7354) rss_mb | MB | 3 | 13.008 | 13.008 | 13.008 | 13.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 7354) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — suite.py (PID 7354) vms_mb | MB | 3 | 16.668 | 16.668 | 16.668 | 16.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7355) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7355) rss_mb | MB | 3 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7355) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7355) vms_mb | MB | 3 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7369) CPU | percent | 2 | 99.894 | 99.348 | 100.440 | 100.440 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7369) rss_mb | MB | 3 | 8.543 | 8.543 | 8.543 | 8.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7369) main thread run-queue wait | percent | 2 | 0.005 | 0.004 | 0.006 | 0.004 | 0.000101 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7369) vms_mb | MB | 3 | 13.238 | 13.238 | 13.238 | 13.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7379) rss_mb | MB | 1 | 20.125 | 20.125 | 20.125 | 20.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7379) vms_mb | MB | 1 | 24.992 | 24.992 | 24.992 | 24.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7391) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7391) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7412) rss_mb | MB | 1 | 155.844 | 155.844 | 155.844 | 155.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7412) vms_mb | MB | 1 | 387.215 | 387.215 | 387.215 | 387.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7482) rss_mb | MB | 1 | 9.395 | 9.395 | 9.395 | 9.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7482) vms_mb | MB | 1 | 13.488 | 13.488 | 13.488 | 13.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_geometry.py (PID 7485) rss_mb | MB | 1 | 73.777 | 73.777 | 73.777 | 73.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_geometry.py (PID 7485) vms_mb | MB | 1 | 337.422 | 337.422 | 337.422 | 337.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7528) rss_mb | MB | 1 | 16.797 | 16.797 | 16.797 | 16.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7528) vms_mb | MB | 1 | 22.066 | 22.066 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7544) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7544) rss_mb | MB | 2 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7544) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7544) vms_mb | MB | 2 | 4.402 | 4.402 | 4.402 | 4.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 7547) rss_mb | MB | 1 | 47.805 | 47.805 | 47.805 | 47.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 7547) vms_mb | MB | 1 | 270.051 | 270.051 | 270.051 | 270.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — validate_adapter.py (PID 7550) rss_mb | MB | 1 | 47.398 | 47.398 | 47.398 | 47.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — validate_adapter.py (PID 7550) vms_mb | MB | 1 | 269.715 | 269.715 | 269.715 | 269.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7642) rss_mb | MB | 1 | 159.246 | 159.246 | 159.246 | 159.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7642) vms_mb | MB | 1 | 394.191 | 394.191 | 394.191 | 394.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7649) rss_mb | MB | 1 | 18.047 | 18.047 | 18.047 | 18.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7649) vms_mb | MB | 1 | 24.098 | 24.098 | 24.098 | 24.098 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 2973 | 26.896 | 0.121 | 211.462 | 0.162 | 804.483681 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2973 | 0.315 | 0.000 | 42.496 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2973 | 0.334 | 0.000 | 50.967 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 2973 | 0.706 | 0.000 | 81.392 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 2973 | 0.724 | 0.000 | 85.178 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 2973 | 0.023 | 0.000 | 4.390 | 0.000 | 68.156250 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 2973 | 0.080 | 0.000 | 67.915 | 0.000 | 238.828125 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 2974 | 362.124 | 10.039 | 703.113 | 220.414 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2973 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 2973 | 0.008 | 0.000 | 18.200 | 0.000 | 25.330546 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 2973 | 0.001 | 0.000 | 0.287 | 0.000 | 1.827250 MB | n/a |
| workload total CPU | percent | 2973 | 5.616 | 1.421 | 318.142 | 1.896 | 168.554492 CPU seconds | n/a |
| workload total memory | MB | 2974 | 5729.983 | 5194.098 | 6093.602 | 6093.527 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
