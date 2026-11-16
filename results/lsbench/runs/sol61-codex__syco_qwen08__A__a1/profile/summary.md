# agprof summary

- Duration: **1706.349 s**
- Runs: **1/1 completed**, 0 succeeded, 1 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **41 calls**, 41 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1315.299 s total wait
- Tools: **53/54 completed**, 0 failed, 1 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **157697** at 1.977 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1706276.959 / 1706276.959 ms |
| LLM latency p50 / p95 | 23507.185 / 96450.805 ms |
| LLM TTFT p50 / p95 | 14801.906 / 20134.061 ms |
| LLM input / output tokens | 2277826 / 49408 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 41 total, 41 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {"unmatched_completions": 1}
- codex: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 10/10 | 10 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 5/5 | 5 | 0 | 0 | n/a | n/a |
| mcp__agency__get_current_resources | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 19/19 | 19 | 0 | 0 | n/a | n/a |
| mcp__agency__reserve_resource | 0/1 | 0 | 0 | 1 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 7/7 | 7 | 0 | 0 | n/a | n/a |
| update_plan | 4/4 | 4 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 4.153% | 103.795% | 70.885 s | 8865.462 MB | 9087.199 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 9355 |  | 1696 | 2.586% | 103.180% | 44.160 s | 2959.802 MB | 3138.012 MB | 16115.826 MB | 16391.707 MB | 6.835938 MB | 247.949219 MB |
| vllm | 9360 |  | 1696 | 0.108% | 6.964% | 1.840 s | 1783.388 MB | 1783.469 MB | 11020.235 MB | 11022.953 MB | 0.003906 MB | 0.031250 MB |
| python | 9394 |  | 1696 | 0.000% | 0.000% | 0.000 s | 12.340 MB | 12.340 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| lsb_grid_worker | 1958 |  | 1696 | 0.000% | 0.000% | 0.000 s | 3.184 MB | 3.184 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 9395 |  | 1696 | 1.446% | 34.804% | 24.650 s | 2322.388 MB | 2322.516 MB | 21203.227 MB | 21203.242 MB | 0.000000 MB | 0.007812 MB |
| docker-init | 9613 | sandbox_agent_lsb-codex_0000_0000 | 1694 | 0.002% | 0.995% | 0.040 s | 0.531 MB | 0.531 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 9644 | sandbox_agent_lsb-codex_0000_0000 | 1694 | 0.003% | 0.995% | 0.050 s | 1.211 MB | 1.211 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 9740 | sandbox_agent_lsb-codex_0000_0000 | 2 | 58.402% | 58.402% | 0.590 s | 40.256 MB | 54.680 MB | 49.557 MB | 63.613 MB | n/a MB | n/a MB |
| bash | 9734 | sandbox_agent_lsb-codex_0000_0000 | 1694 | 25.217% | 98.342% | 429.440 s | 108.384 MB | 113.699 MB | 970.673 MB | 976.801 MB | n/a MB | n/a MB |
| getconf | 9793 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.395 MB | 0.395 MB | n/a MB | n/a MB |
| git | 9786 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.141 MB | 3.141 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 9791 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.055 MB | 3.055 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git-remote-http | 9794 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 2.547 MB | 2.547 MB | n/a MB | n/a MB |
| codex | 9757 | sandbox_agent_lsb-codex_0000_0000 | 1668 | 2.092% | 19.806% | 35.090 s | 137.292 MB | 146.215 MB | 383.528 MB | 536.984 MB | n/a MB | n/a MB |
| git-remote-http | 9833 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.988 MB | 17.988 MB | 100.590 MB | 100.590 MB | n/a MB | n/a MB |
| git | 9836 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.523 MB | 4.523 MB | 8.285 MB | 8.285 MB | n/a MB | n/a MB |
| git | 9832 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.117 MB | 3.117 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 9831 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.637 MB | 3.637 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 9848 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 31.793 MB | 31.793 MB | 37.742 MB | 37.742 MB | n/a MB | n/a MB |
| head | 9875 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.547 MB | 1.547 MB | 2.859 MB | 2.859 MB | n/a MB | n/a MB |
| rg | 9874 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 5.613 MB | 5.613 MB | n/a MB | n/a MB |
| bash | 9873 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.066 MB | 3.066 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 9883 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.461 MB | 7.461 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| python3 | 9958 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.977 MB | 9.977 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| python3 | 9985 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.914 MB | 20.914 MB | 25.633 MB | 25.633 MB | n/a MB | n/a MB |
| bash | 10031 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.660 MB | 2.660 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python | 10059 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.766 MB | 18.766 MB | 211.492 MB | 211.492 MB | n/a MB | n/a MB |
| bash | 10058 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.812 MB | 2.812 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 10087 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.469 MB | 21.469 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| python3 | 10091 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.598 MB | 13.598 MB | 19.836 MB | 19.836 MB | n/a MB | n/a MB |
| python3 | 10184 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.730 MB | 11.730 MB | 19.844 MB | 19.844 MB | n/a MB | n/a MB |
| bash | 10195 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.887 MB | 2.887 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 10196 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 45.473 MB | 45.473 MB | 267.492 MB | 267.492 MB | n/a MB | n/a MB |
| python3 | 10214 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.281 MB | 18.281 MB | 24.277 MB | 24.277 MB | n/a MB | n/a MB |
| python3 | 10219 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.629 MB | 14.629 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| python3 | 10266 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.145 MB | 8.145 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python3 | 10298 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.555 MB | 10.555 MB | 15.203 MB | 15.203 MB | n/a MB | n/a MB |
| python3 | 10319 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.277 MB | 21.277 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| python | 10333 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.633 MB | 4.633 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| bash | 10332 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.922 MB | 2.922 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 10380 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.125 MB | 0.125 MB | 0.395 MB | 0.395 MB | n/a MB | n/a MB |
| bash | 10405 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.789 MB | 2.789 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python | 10406 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.918 MB | 8.918 MB | 13.395 MB | 13.395 MB | n/a MB | n/a MB |
| python3 | 10419 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.637 MB | 7.637 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python3 | 10471 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.676 MB | 21.676 MB | 26.910 MB | 26.910 MB | n/a MB | n/a MB |
| python | 10488 | sandbox_agent_lsb-codex_0000_0000 | 2 | 128.954% | 128.954% | 1.300 s | 71.586 MB | 122.570 MB | 266.385 MB | 400.398 MB | n/a MB | n/a MB |
| bash | 10487 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.836 MB | 2.836 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python | 10551 | sandbox_agent_lsb-codex_0000_0000 | 2 | 146.269% | 146.269% | 1.480 s | 130.518 MB | 180.957 MB | 381.537 MB | 457.352 MB | n/a MB | n/a MB |
| bash | 10550 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.992 MB | 2.992 MB | 4.395 MB | 4.395 MB | n/a MB | n/a MB |
| tokio-rt-worker | 10583 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 144.098 MB | 144.098 MB | 393.488 MB | 393.488 MB | n/a MB | n/a MB |
| docker | 10619 |  | 1 | n/a% | n/a% | n/a s | 30.258 MB | 30.258 MB | 1843.270 MB | 1843.270 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.627% | 100.000% | 11886.229 MB | 12020.000 MB | 29.042 W | 59.699 W | 49514.422 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 28.571% | 203.059% | 486.613 s | 494.572 MB | 680.242 MB | 211.199219 MB | 161.843750 MB | 24.978242 MB | 1.300329 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 9502 | 1706.281 | interrupted |
| tool:mcp__agency__reserve_resource | -1 | 1500.358 | interrupted |
| harness:retire | -1 | 0.376 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 1 | 0 | 1706.277 | n/a | n/a | 211.199 | 1706276.959 | 1706276.959 | 1706276.959 |
| sync:result_wait | 1/1 | 0 | 0 | 1706.276 | 0.000 | 1706.276 | 211.199 | 1706276.082 | 1706276.082 | 1706276.082 |
| engine:execute | 1/1 | 1 | 0 | 1706.275 | 2.443 | 1703.831 | 211.199 | 1706275.254 | 1706275.254 | 1706275.254 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1680.066 | 0.003 | 1680.063 | 173.724 | 1680066.287 | 1680066.287 | 1680066.287 |
| harness:await_cli | 1/1 | 0 | 0 | 1675.479 | n/a | n/a | 48.156 | 1675479.327 | 1675479.327 | 1675479.327 |
| llm:attempt | 41/41 | 0 | 0 | 1315.299 | 5.555 | 1309.732 | 12.737 | 32080.466 | 23507.185 | 96450.805 |
| tool:Bash | 10/10 | 0 | 0 | 53.971 | n/a | n/a | 23.520 | 5397.056 | 945.209 | 25577.778 |
| agency:services_close | 1/1 | 1 | 0 | 20.001 | 0.001 | 20.000 | 0.000 | 20000.630 | 20000.630 | 20000.630 |
| tool:mcp__agency__trace | 7/7 | 0 | 0 | 11.212 | n/a | n/a | 0.000 | 1601.698 | 1979.369 | 2036.427 |
| tool:mcp__agency__patch | 19/19 | 0 | 0 | 7.924 | n/a | n/a | 0.000 | 417.063 | 410.856 | 446.900 |
| tool:mcp__agency__inspect_module_inputs | 2/2 | 0 | 0 | 4.831 | n/a | n/a | 0.000 | 2415.617 | 2415.617 | 2849.382 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.464 | 1.009 | 3.455 | 36.561 | 4464.380 | 4464.380 | 4464.380 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.464 | 1.009 | 3.455 | 36.557 | 4464.060 | 4464.060 | 4464.060 |
| tool:mcp__agency__generate | 5/5 | 0 | 0 | 3.988 | n/a | n/a | 0.000 | 797.565 | 635.916 | 1332.913 |
| tool:mcp__agency__inspect | 1/1 | 0 | 0 | 2.436 | n/a | n/a | 0.000 | 2435.880 | 2435.880 | 2435.880 |
| harness:submit | 1/1 | 0 | 0 | 1.411 | n/a | n/a | 37.539 | 1411.316 | 1411.316 | 1411.316 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.225 | n/a | n/a | 70.822 | 1225.056 | 1225.056 | 1225.056 |
| run:container_call | 11/11 | 0 | 0 | 1.182 | 0.002 | 1.180 | 0.000 | 107.483 | 56.834 | 293.041 |
| syscall:connect | 471/471 | 0 | 0 | 1.140 | n/a | n/a | 3.964 | 2.421 | 2.103 | 4.220 |
| syscall:execve | 611/611 | 0 | 0 | 1.019 | n/a | n/a | 6.098 | 1.668 | 1.215 | 2.459 |
| sandbox:create | 1/1 | 0 | 0 | 0.923 | 0.253 | 0.669 | 0.000 | 922.780 | 922.780 | 922.780 |
| syscall:sendto | 348/348 | 0 | 0 | 0.848 | n/a | n/a | 3.365 | 2.437 | 2.248 | 4.106 |
| tool:update_plan | 4/4 | 0 | 0 | 0.794 | n/a | n/a | 0.495 | 198.603 | 196.293 | 214.311 |
| harness:snapshot | 1/1 | 0 | 0 | 0.753 | n/a | n/a | 0.071 | 752.704 | 752.704 | 752.704 |
| sandbox:start | 1/1 | 0 | 0 | 0.550 | 0.003 | 0.547 | 0.000 | 549.592 | 549.592 | 549.592 |
| runtime.container_create | 1/1 | 0 | 0 | 0.549 | 0.003 | 0.547 | 0.000 | 549.437 | 549.437 | 549.437 |
| run:detect | 1/1 | 0 | 0 | 0.519 | 0.001 | 0.519 | 0.000 | 519.400 | 519.400 | 519.400 |
| teardown:discard | 1/1 | 0 | 0 | 0.411 | 0.003 | 0.408 | 0.000 | 410.586 | 410.586 | 410.586 |
| sandbox:rm | 1/1 | 0 | 0 | 0.410 | 0.002 | 0.408 | 0.000 | 410.405 | 410.405 | 410.405 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.321 | n/a | n/a | 0.000 | 320.706 | 320.706 | 320.706 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 0.294 | n/a | n/a | 0.000 | 294.046 | 294.046 | 294.046 |
| tool:mcp__agency__attention | 1/1 | 0 | 0 | 0.294 | n/a | n/a | 0.000 | 293.983 | 293.983 | 293.983 |
| tool:mcp__agency__get_current_resources | 1/1 | 0 | 0 | 0.260 | n/a | n/a | 0.163 | 260.140 | 260.140 | 260.140 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.212 | n/a | n/a | 0.000 | 212.431 | 212.431 | 212.431 |
| sandbox:update_limits | 1/1 | 0 | 0 | 0.155 | 0.001 | 0.154 | 0.000 | 154.556 | 154.556 | 154.556 |
| agency:services_start | 1/1 | 0 | 0 | 0.087 | 0.043 | 0.044 | 0.000 | 87.390 | 87.390 | 87.390 |
| harness:launch | 1/1 | 0 | 0 | 0.051 | n/a | n/a | 2.836 | 50.992 | 50.992 | 50.992 |
| agent:create | 1/1 | 0 | 0 | 0.051 | 0.010 | 0.041 | 0.000 | 50.562 | 50.562 | 50.562 |
| syscall:bind | 6/6 | 0 | 0 | 0.022 | n/a | n/a | 0.436 | 3.612 | 3.218 | 6.166 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 2.068 | 2.068 | 2.068 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.274 | 1.274 | 1.274 |
| sync:container | 11/11 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.085 | 0.074 | 0.135 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.200 | 0.200 | 0.200 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.051 | 0.051 | 0.051 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| tool:mcp__agency__reserve_resource | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1694 | 0.067 | 0.015 | 8.711 | 8.711 | 1.143494 CPU seconds | n/a |
| GPU 0 memory | MB | 1696 | 11886.229 | 11670.000 | 12020.000 | 11852.000 | n/a | n/a |
| GPU 0 power | W | 1696 | 29.042 | 28.009 | 59.699 | 28.414 | n/a | 49514.422 J |
| GPU 0 proc / 9355-771202 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 memory | MB | 1696 | 3252.033 | 3118.000 | 3382.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 9355-771202 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 estimated power | W | 1489 | 0.927 | 0.000 | 53.507 | 0.000 | n/a | n/a |
| GPU 0 proc / 9355-771202 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 utilization | percent | 1489 | 0.542 | 0.000 | 44.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 9395-774096 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 memory | MB | 1696 | 8152.196 | 8070.000 | 8156.000 | 8156.000 | n/a | n/a |
| GPU 0 proc / 9395-774096 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 estimated power | W | 186 | 0.898 | 0.000 | 59.699 | 0.000 | n/a | n/a |
| GPU 0 proc / 9395-774096 / sandbox / ~ / device / GPU-ad247edc-9af2-c436-1216-7e6cbbb47178 utilization | percent | 186 | 1.097 | 0.000 | 57.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1696 | 11404.229 | 11188.000 | 11538.000 | 11370.000 | n/a | n/a |
| GPU 0 utilization | percent | 1696 | 0.627 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1696 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1695 | 0.625 | 0.021 | 28.794 | 2.275 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1695 | 7.898 | 0.250 | 54.657 | 7.557 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1695 | 0.153 | 0.000 | 62.636 | 2.036 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1695 | 0.280 | 0.000 | 70.026 | 10.099 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1695 | 0.135 | 0.000 | 47.950 | 2.955 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1695 | 0.143 | 0.000 | 48.714 | 4.590 | n/a | n/a |
| host mem_total_mb | MB | 1696 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1696 | 6982.213 | 6440.664 | 7353.844 | 7041.203 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1695 | 0.004 | 0.000 | 3.112 | 0.093 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1695 | 0.006 | 0.000 | 5.160 | 0.123 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1695 | 0.019 | 0.000 | 15.511 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1695 | 0.010 | 0.000 | 0.703 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10031) rss_mb | MB | 1 | 2.660 | 2.660 | 2.660 | 2.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10031) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10058) rss_mb | MB | 1 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10058) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10059) rss_mb | MB | 1 | 18.766 | 18.766 | 18.766 | 18.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10059) vms_mb | MB | 1 | 211.492 | 211.492 | 211.492 | 211.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10087) rss_mb | MB | 1 | 21.469 | 21.469 | 21.469 | 21.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10087) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10091) rss_mb | MB | 1 | 13.598 | 13.598 | 13.598 | 13.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10091) vms_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10184) rss_mb | MB | 1 | 11.730 | 11.730 | 11.730 | 11.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10184) vms_mb | MB | 1 | 19.844 | 19.844 | 19.844 | 19.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10195) rss_mb | MB | 1 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10195) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10196) rss_mb | MB | 1 | 45.473 | 45.473 | 45.473 | 45.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10196) vms_mb | MB | 1 | 267.492 | 267.492 | 267.492 | 267.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10214) rss_mb | MB | 1 | 18.281 | 18.281 | 18.281 | 18.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10214) vms_mb | MB | 1 | 24.277 | 24.277 | 24.277 | 24.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10219) rss_mb | MB | 1 | 14.629 | 14.629 | 14.629 | 14.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10219) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10266) rss_mb | MB | 1 | 8.145 | 8.145 | 8.145 | 8.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10266) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10298) rss_mb | MB | 1 | 10.555 | 10.555 | 10.555 | 10.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10298) vms_mb | MB | 1 | 15.203 | 15.203 | 15.203 | 15.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10319) rss_mb | MB | 1 | 21.277 | 21.277 | 21.277 | 21.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10319) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10332) rss_mb | MB | 1 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10332) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10333) rss_mb | MB | 1 | 4.633 | 4.633 | 4.633 | 4.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10333) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10380) rss_mb | MB | 1 | 0.125 | 0.125 | 0.125 | 0.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10380) vms_mb | MB | 1 | 0.395 | 0.395 | 0.395 | 0.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10405) rss_mb | MB | 1 | 2.789 | 2.789 | 2.789 | 2.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10405) vms_mb | MB | 1 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10406) rss_mb | MB | 1 | 8.918 | 8.918 | 8.918 | 8.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10406) vms_mb | MB | 1 | 13.395 | 13.395 | 13.395 | 13.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10419) rss_mb | MB | 1 | 7.637 | 7.637 | 7.637 | 7.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10419) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10471) rss_mb | MB | 1 | 21.676 | 21.676 | 21.676 | 21.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10471) vms_mb | MB | 1 | 26.910 | 26.910 | 26.910 | 26.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10487) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10487) rss_mb | MB | 2 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10487) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10487) vms_mb | MB | 2 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10488) CPU | percent | 1 | 128.954 | 128.954 | 128.954 | 128.954 | 1.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10488) rss_mb | MB | 2 | 71.586 | 20.602 | 122.570 | 122.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10488) main thread run-queue wait | percent | 1 | 11.904 | 11.904 | 11.904 | 11.904 | 0.120010 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10488) vms_mb | MB | 2 | 266.385 | 132.371 | 400.398 | 400.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10550) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10550) rss_mb | MB | 2 | 2.992 | 2.992 | 2.992 | 2.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10550) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10550) vms_mb | MB | 2 | 4.395 | 4.395 | 4.395 | 4.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10551) CPU | percent | 1 | 146.269 | 146.269 | 146.269 | 146.269 | 1.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10551) rss_mb | MB | 2 | 130.518 | 80.078 | 180.957 | 180.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10551) main thread run-queue wait | percent | 1 | 25.241 | 25.241 | 25.241 | 25.241 | 0.255395 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 10551) vms_mb | MB | 2 | 381.537 | 305.723 | 457.352 | 457.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10583) rss_mb | MB | 1 | 144.098 | 144.098 | 144.098 | 144.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10583) vms_mb | MB | 1 | 393.488 | 393.488 | 393.488 | 393.488 | n/a | n/a |
| docker (PID 10619) rss_mb | MB | 1 | 30.258 | 30.258 | 30.258 | 30.258 | n/a | n/a |
| docker (PID 10619) vms_mb | MB | 1 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1958) CPU | percent | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1958) io read MB/s | MB/s | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1958) io write MB/s | MB/s | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1958) rss_mb | MB | 1696 | 3.184 | 3.184 | 3.184 | 3.184 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1958) main thread run-queue wait | percent | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1958) vms_mb | MB | 1696 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9355) CPU | percent | 1695 | 2.586 | 0.000 | 103.180 | 0.000 | 44.160000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 9355) io read MB/s | MB/s | 1695 | 0.004 | 0.000 | 5.070 | 0.136 | 6.835938 MB | n/a |
| Agency harness — python -m lsbench (PID 9355) io write MB/s | MB/s | 1695 | 0.145 | 0.016 | 17.763 | 0.023 | 247.949219 MB | n/a |
| Agency harness — python -m lsbench (PID 9355) rss_mb | MB | 1696 | 2959.802 | 2348.949 | 3138.012 | 3138.012 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9355) main thread run-queue wait | percent | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 9355) vms_mb | MB | 1696 | 16115.826 | 13838.812 | 16391.707 | 16341.668 | n/a | n/a |
| Python — vllm (PID 9360) CPU | percent | 1695 | 0.108 | 0.000 | 6.964 | 0.000 | 1.840000 CPU seconds | n/a |
| Python — vllm (PID 9360) io read MB/s | MB/s | 1695 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 9360) io write MB/s | MB/s | 1695 | 0.000 | 0.000 | 0.008 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 9360) rss_mb | MB | 1696 | 1783.388 | 1782.594 | 1783.469 | 1783.469 | n/a | n/a |
| Python — vllm (PID 9360) main thread run-queue wait | percent | 1695 | 0.002 | 0.000 | 0.777 | 0.002 | 0.039680 run-queue seconds | n/a |
| Python — vllm (PID 9360) vms_mb | MB | 1696 | 11020.235 | 10950.934 | 11022.953 | 11022.953 | n/a | n/a |
| Python — python -c (PID 9394) CPU | percent | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 9394) io read MB/s | MB/s | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9394) io write MB/s | MB/s | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9394) rss_mb | MB | 1696 | 12.340 | 12.340 | 12.340 | 12.340 | n/a | n/a |
| Python — python -c (PID 9394) main thread run-queue wait | percent | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 9394) vms_mb | MB | 1696 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 9395) CPU | percent | 1695 | 1.446 | 0.000 | 34.804 | 1.990 | 24.650000 CPU seconds | n/a |
| VLLM::EngineCore (PID 9395) io read MB/s | MB/s | 1695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 9395) io write MB/s | MB/s | 1695 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 9395) rss_mb | MB | 1696 | 2322.388 | 2322.266 | 2322.516 | 2322.516 | n/a | n/a |
| VLLM::EngineCore (PID 9395) main thread run-queue wait | percent | 1695 | 0.001 | 0.000 | 0.424 | 0.000 | 0.009995 run-queue seconds | n/a |
| VLLM::EngineCore (PID 9395) vms_mb | MB | 1696 | 21203.227 | 21203.227 | 21203.242 | 21203.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 9613) CPU | percent | 1693 | 0.002 | 0.000 | 0.995 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 9613) rss_mb | MB | 1694 | 0.531 | 0.531 | 0.531 | 0.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 9613) main thread run-queue wait | percent | 1693 | 0.000 | 0.000 | 0.352 | 0.000 | 0.005473 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 9613) vms_mb | MB | 1694 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 9644) CPU | percent | 1693 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 9644) rss_mb | MB | 1694 | 1.211 | 1.211 | 1.211 | 1.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 9644) main thread run-queue wait | percent | 1693 | 0.000 | 0.000 | 0.423 | 0.000 | 0.005242 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 9644) vms_mb | MB | 1694 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9734) CPU | percent | 1693 | 25.217 | 0.000 | 98.342 | 0.000 | 429.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9734) rss_mb | MB | 1694 | 108.384 | 2.973 | 113.699 | 113.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9734) main thread run-queue wait | percent | 1693 | 0.000 | 0.000 | 0.008 | 0.000 | 0.000145 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9734) vms_mb | MB | 1694 | 970.673 | 4.262 | 976.801 | 975.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 9740) CPU | percent | 1 | 58.402 | 58.402 | 58.402 | 58.402 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 9740) rss_mb | MB | 2 | 40.256 | 25.832 | 54.680 | 54.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 9740) main thread run-queue wait | percent | 1 | 0.022 | 0.022 | 0.022 | 0.022 | 0.000223 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 9740) vms_mb | MB | 2 | 49.557 | 35.500 | 63.613 | 63.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 9757) CPU | percent | 1667 | 2.092 | 0.000 | 19.806 | 3.978 | 35.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 9757) rss_mb | MB | 1668 | 137.292 | 63.707 | 146.215 | 143.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 9757) main thread run-queue wait | percent | 1667 | 0.000 | 0.000 | 0.011 | 0.000 | 0.000293 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 9757) vms_mb | MB | 1668 | 383.528 | 359.082 | 536.984 | 397.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 9786) rss_mb | MB | 1 | 3.141 | 3.141 | 3.141 | 3.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 9786) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 9791) rss_mb | MB | 1 | 3.055 | 3.055 | 3.055 | 3.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 9791) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — getconf (PID 9793) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — getconf (PID 9793) vms_mb | MB | 1 | 0.395 | 0.395 | 0.395 | 0.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 9794) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 9794) vms_mb | MB | 1 | 2.547 | 2.547 | 2.547 | 2.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 9831) rss_mb | MB | 1 | 3.637 | 3.637 | 3.637 | 3.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 9831) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 9832) rss_mb | MB | 1 | 3.117 | 3.117 | 3.117 | 3.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 9832) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 9833) rss_mb | MB | 1 | 17.988 | 17.988 | 17.988 | 17.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 9833) vms_mb | MB | 1 | 100.590 | 100.590 | 100.590 | 100.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 9836) rss_mb | MB | 1 | 4.523 | 4.523 | 4.523 | 4.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 9836) vms_mb | MB | 1 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 9848) rss_mb | MB | 1 | 31.793 | 31.793 | 31.793 | 31.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 9848) vms_mb | MB | 1 | 37.742 | 37.742 | 37.742 | 37.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9873) rss_mb | MB | 1 | 3.066 | 3.066 | 3.066 | 3.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 9873) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — rg (PID 9874) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — rg (PID 9874) vms_mb | MB | 1 | 5.613 | 5.613 | 5.613 | 5.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 9875) rss_mb | MB | 1 | 1.547 | 1.547 | 1.547 | 1.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 9875) vms_mb | MB | 1 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9883) rss_mb | MB | 1 | 7.461 | 7.461 | 7.461 | 7.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9883) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9958) rss_mb | MB | 1 | 9.977 | 9.977 | 9.977 | 9.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9958) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9985) rss_mb | MB | 1 | 20.914 | 20.914 | 20.914 | 20.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 9985) vms_mb | MB | 1 | 25.633 | 25.633 | 25.633 | 25.633 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 1693 | 28.571 | 0.171 | 203.059 | 0.217 | 486.613492 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1693 | 0.387 | 0.000 | 23.107 | 0.016 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1693 | 0.406 | 0.000 | 28.096 | 0.016 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 1693 | 0.099 | 0.000 | 48.076 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 1693 | 0.100 | 0.000 | 48.531 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 1693 | 0.124 | 0.000 | 62.620 | 0.000 | 211.199219 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 1693 | 0.095 | 0.000 | 70.026 | 0.000 | 161.843750 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 1694 | 494.572 | 41.809 | 680.242 | 350.938 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1693 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1693 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 1693 | 0.015 | 0.000 | 14.978 | 0.000 | 24.978242 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 1693 | 0.001 | 0.000 | 0.292 | 0.000 | 1.300329 MB | n/a |
| workload total CPU | percent | 1695 | 4.153 | 1.735 | 103.795 | 9.921 | 70.884802 CPU seconds | n/a |
| workload total memory | MB | 1696 | 8865.462 | 8270.773 | 9087.199 | 9087.199 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
