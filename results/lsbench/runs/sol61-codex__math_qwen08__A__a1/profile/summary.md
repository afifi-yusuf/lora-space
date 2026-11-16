# agprof summary

- Duration: **3342.122 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **62 calls**, 62 succeeded, 0 failed, 0 interrupted, n/a reported retries, 2319.210 s total wait
- Tools: **61/61 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **308769** at 1.969 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 3342048.552 / 3342048.552 ms |
| LLM latency p50 / p95 | 27110.116 / 105647.253 ms |
| LLM TTFT p50 / p95 | 14056.608 / 21478.867 ms |
| LLM input / output tokens | 5838988 / 84914 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 62 total, 62 succeeded, 0 failed, 0 interrupted |
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
| Bash | 13/13 | 13 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 8/8 | 8 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 4/4 | 4 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 11/11 | 11 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 9/9 | 9 | 0 | 0 | n/a | n/a |
| update_plan | 8/8 | 8 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 14.911% | 104.561% | 499.572 s | 10381.409 MB | 10783.602 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 15673 |  | 3320 | 0.857% | 6.954% | 28.720 s | 1803.858 MB | 1804.113 MB | 11044.867 MB | 11046.496 MB | 0.007812 MB | 0.148438 MB |
| lsb_grid_worker | 4781 |  | 3320 | 0.000% | 0.000% | 0.000 s | 3.168 MB | 3.168 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 15668 |  | 3320 | 4.414% | 104.497% | 147.880 s | 3701.106 MB | 4076.535 MB | 17194.747 MB | 19721.711 MB | 2.191406 MB | 421.640625 MB |
| VLLM::EngineCor | 15708 |  | 3320 | 9.634% | 43.520% | 322.670 s | 2335.641 MB | 2336.141 MB | 21239.751 MB | 21240.004 MB | 0.000000 MB | 0.019531 MB |
| docker | 15984 |  | 1 | n/a% | n/a% | n/a s | 30.148 MB | 30.148 MB | 1843.324 MB | 1843.324 MB | n/a MB | n/a MB |
| python | 15707 |  | 3320 | 0.000% | 0.000% | 0.000 s | 12.188 MB | 12.188 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 16043 | sandbox_agent_lsb-codex_0000_0000 | 3318 | 0.002% | 1.990% | 0.070 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 16173 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 38.066 MB | 38.066 MB | 44.809 MB | 44.809 MB | n/a MB | n/a MB |
| bash | 16167 | sandbox_agent_lsb-codex_0000_0000 | 3318 | 25.819% | 98.519% | 862.280 s | 116.067 MB | 124.461 MB | 973.627 MB | 976.938 MB | n/a MB | n/a MB |
| tail | 16075 | sandbox_agent_lsb-codex_0000_0000 | 3318 | 0.002% | 0.995% | 0.080 s | 1.148 MB | 1.148 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| codex | 16190 | sandbox_agent_lsb-codex_0000_0000 | 3312 | 3.166% | 21.888% | 105.670 s | 138.617 MB | 148.762 MB | 377.193 MB | 507.070 MB | n/a MB | n/a MB |
| git-remote-http | 16227 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.266 MB | 18.266 MB | 99.594 MB | 99.594 MB | n/a MB | n/a MB |
| git | 16226 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.441 MB | 3.441 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 16221 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.680 MB | 3.680 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 16264 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.793 MB | 3.793 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 16269 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.383 MB | 5.383 MB | 8.285 MB | 8.285 MB | n/a MB | n/a MB |
| git-remote-http | 16266 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.254 MB | 18.254 MB | 100.484 MB | 100.484 MB | n/a MB | n/a MB |
| git | 16265 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.645 MB | 3.645 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| python3 | 16291 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.969 MB | 21.969 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| rg | 16302 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.629 MB | 0.629 MB | 5.617 MB | 5.617 MB | n/a MB | n/a MB |
| bash | 16299 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.984 MB | 2.984 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 16310 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.215 MB | 15.215 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| tokio-rt-worker | 16465 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 130.668 MB | 130.668 MB | 387.449 MB | 387.449 MB | n/a MB | n/a MB |
| python3 | 16596 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.750 MB | 19.750 MB | 24.730 MB | 24.730 MB | n/a MB | n/a MB |
| python3 | 16607 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.855 MB | 9.855 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| python3 | 16643 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.273 MB | 16.273 MB | 21.773 MB | 21.773 MB | n/a MB | n/a MB |
| python3 | 16658 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.965 MB | 14.965 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| python3 | 16679 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.391 MB | 18.391 MB | 24.383 MB | 24.383 MB | n/a MB | n/a MB |
| tokio-rt-worker | 16697 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 136.645 MB | 136.645 MB | 391.348 MB | 391.348 MB | n/a MB | n/a MB |
| python3 | 16711 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.695 MB | 14.695 MB | 19.887 MB | 19.887 MB | n/a MB | n/a MB |
| tokio-rt-worker | 16813 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 137.371 MB | 137.371 MB | 392.250 MB | 392.250 MB | n/a MB | n/a MB |
| python | 16889 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.594 MB | 22.594 MB | 133.945 MB | 133.945 MB | n/a MB | n/a MB |
| bash | 16888 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.840 MB | 2.840 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 16943 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.664 MB | 6.664 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| bash | 16957 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.086 MB | 3.086 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 16958 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 72.000 MB | 72.000 MB | 209.512 MB | 209.512 MB | n/a MB | n/a MB |
| tokio-rt-worker | 16990 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 140.324 MB | 140.324 MB | 387.289 MB | 387.289 MB | n/a MB | n/a MB |
| python3 | 17000 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.887 MB | 6.887 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python3 | 17017 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.750 MB | 17.750 MB | 23.098 MB | 23.098 MB | n/a MB | n/a MB |
| tokio-rt-worker | 17621 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 138.340 MB | 138.340 MB | 383.453 MB | 383.453 MB | n/a MB | n/a MB |
| python3 | 17696 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.715 MB | 21.715 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python3 | 17734 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.461 MB | 20.461 MB | 25.117 MB | 25.117 MB | n/a MB | n/a MB |
| python3 | 17745 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.121 MB | 14.121 MB | 19.887 MB | 19.887 MB | n/a MB | n/a MB |
| tokio-rt-worker | 17773 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 139.926 MB | 139.926 MB | 385.332 MB | 385.332 MB | n/a MB | n/a MB |
| bash | 18063 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.008 MB | 3.008 MB | 4.398 MB | 4.398 MB | n/a MB | n/a MB |
| python | 18064 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 91.105 MB | 91.105 MB | 239.059 MB | 239.059 MB | n/a MB | n/a MB |
| python3 | 18142 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.848 MB | 6.848 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python3 | 18151 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.094 MB | 17.094 MB | 22.066 MB | 22.066 MB | n/a MB | n/a MB |
| python3 | 18183 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.430 MB | 16.430 MB | 21.773 MB | 21.773 MB | n/a MB | n/a MB |
| python3 | 18239 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.918 MB | 9.918 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| python3 | 18278 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.977 MB | 14.977 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| python3 | 18306 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.371 MB | 9.371 MB | 13.488 MB | 13.488 MB | n/a MB | n/a MB |
| python | 18321 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 25.602 MB | 25.602 MB | 138.750 MB | 138.750 MB | n/a MB | n/a MB |
| bash | 18320 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.941 MB | 2.941 MB | 4.395 MB | 4.395 MB | n/a MB | n/a MB |
| python3 | 18335 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.496 MB | 21.496 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python3 | 18347 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.484 MB | 20.484 MB | 25.246 MB | 25.246 MB | n/a MB | n/a MB |
| python3 | 18358 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.637 MB | 16.637 MB | 22.109 MB | 22.109 MB | n/a MB | n/a MB |
| tokio-rt-worker | 18370 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 145.227 MB | 145.227 MB | 390.590 MB | 390.590 MB | n/a MB | n/a MB |
| docker | 18405 |  | 3 | 0.000% | 0.000% | 0.000 s | 30.367 MB | 30.367 MB | 1843.504 MB | 1843.504 MB | 0.000000 MB | 0.000000 MB |
| docker | 18521 |  | 1 | n/a% | n/a% | n/a s | 5.914 MB | 5.914 MB | 69.043 MB | 69.043 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 28.416% | 100.000% | 12014.371 MB | 13984.000 MB | 42.905 W | 74.810 W | 143482.129 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 29.628% | 180.677% | 989.611 s | 471.082 MB | 557.168 MB | 167.191406 MB | 228.621094 MB | 25.047380 MB | 2.130117 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 15933 | 3342.054 | interrupted |
| harness:retire | -1 | 0.381 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 3342.049 | n/a | n/a | 167.191 | 3342048.552 | 3342048.552 | 3342048.552 |
| sync:result_wait | 1/1 | 0 | 0 | 3342.048 | 0.000 | 3342.048 | 167.191 | 3342048.251 | 3342048.251 | 3342048.251 |
| engine:execute | 1/1 | 0 | 0 | 3342.047 | 3.377 | 3338.665 | 167.191 | 3342046.875 | 3342046.875 | 3342046.875 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 3334.073 | 0.006 | 3334.067 | 147.950 | 3334073.048 | 3334073.048 | 3334073.048 |
| harness:await_cli | 1/1 | 0 | 0 | 3330.605 | n/a | n/a | 34.839 | 3330604.924 | 3330604.924 | 3330604.924 |
| llm:attempt | 62/62 | 0 | 0 | 2319.210 | 9.952 | 2309.254 | 7.568 | 37406.617 | 27110.116 | 105647.253 |
| tool:mcp__agency__generate | 8/8 | 0 | 0 | 868.532 | n/a | n/a | 0.379 | 108566.546 | 96532.222 | 188345.263 |
| tool:mcp__agency__trace | 9/9 | 0 | 0 | 89.218 | n/a | n/a | 0.000 | 9913.163 | 4369.928 | 24586.978 |
| tool:mcp__agency__inspect_module_inputs | 11/11 | 0 | 0 | 14.134 | n/a | n/a | 0.000 | 1284.951 | 1136.354 | 2095.774 |
| tool:Bash | 13/13 | 0 | 0 | 9.546 | n/a | n/a | 21.833 | 734.319 | 671.968 | 1365.360 |
| run:container_call | 13/13 | 0 | 0 | 3.957 | 0.002 | 3.955 | 0.000 | 304.414 | 56.793 | 1392.479 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.541 | 0.779 | 2.763 | 17.953 | 3541.471 | 3541.471 | 3541.471 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.541 | 0.778 | 2.763 | 17.947 | 3541.213 | 3541.213 | 3541.213 |
| teardown:commit | 1/1 | 0 | 0 | 3.328 | 0.004 | 3.324 | 0.000 | 3328.200 | 3328.200 | 3328.200 |
| sandbox:commit | 1/1 | 0 | 0 | 3.129 | 0.003 | 3.126 | 0.000 | 3128.827 | 3128.827 | 3128.827 |
| checkpoint.total | 1/1 | 0 | 0 | 3.129 | 0.002 | 3.126 | 0.000 | 3128.664 | 3128.664 | 3128.664 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 3.128 | 0.002 | 3.126 | 0.000 | 3128.494 | 3128.494 | 3128.494 |
| tool:mcp__agency__inspect | 4/4 | 0 | 0 | 1.511 | n/a | n/a | 0.000 | 377.639 | 389.824 | 456.760 |
| tool:update_plan | 8/8 | 0 | 0 | 1.452 | n/a | n/a | 0.363 | 181.561 | 184.039 | 192.668 |
| harness:submit | 1/1 | 0 | 0 | 1.428 | n/a | n/a | 28.155 | 1427.596 | 1427.596 | 1427.596 |
| syscall:connect | 595/595 | 0 | 0 | 1.408 | n/a | n/a | 4.275 | 2.367 | 1.951 | 4.109 |
| tool:mcp__agency__patch | 3/3 | 0 | 0 | 1.336 | n/a | n/a | 0.000 | 445.171 | 456.806 | 460.540 |
| syscall:execve | 791/791 | 0 | 0 | 1.308 | n/a | n/a | 6.566 | 1.653 | 1.161 | 2.215 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.224 | n/a | n/a | 68.535 | 1224.445 | 1224.445 | 1224.445 |
| syscall:sendto | 474/474 | 0 | 0 | 1.096 | n/a | n/a | 3.361 | 2.313 | 2.137 | 4.010 |
| tool:mcp__agency__attribution | 3/3 | 0 | 0 | 0.920 | n/a | n/a | 0.000 | 306.512 | 307.757 | 308.236 |
| harness:snapshot | 1/1 | 0 | 0 | 0.797 | n/a | n/a | 0.171 | 796.530 | 796.530 | 796.530 |
| sandbox:create | 1/1 | 0 | 0 | 0.764 | 0.247 | 0.517 | 0.000 | 763.985 | 763.985 | 763.985 |
| sandbox:start | 1/1 | 0 | 0 | 0.557 | 0.002 | 0.555 | 0.000 | 557.344 | 557.344 | 557.344 |
| runtime.container_create | 1/1 | 0 | 0 | 0.557 | 0.002 | 0.555 | 0.000 | 557.203 | 557.203 | 557.203 |
| run:detect | 1/1 | 0 | 0 | 0.451 | 0.001 | 0.450 | 0.000 | 450.819 | 450.819 | 450.819 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.368 | n/a | n/a | 0.000 | 368.429 | 368.429 | 368.429 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.222 | n/a | n/a | 0.000 | 222.194 | 222.194 | 222.194 |
| sandbox:stop | 1/1 | 0 | 0 | 0.199 | 0.002 | 0.198 | 0.000 | 199.114 | 199.114 | 199.114 |
| agency:services_close | 1/1 | 0 | 0 | 0.150 | 0.001 | 0.149 | 0.000 | 149.524 | 149.524 | 149.524 |
| agency:services_start | 1/1 | 0 | 0 | 0.088 | 0.043 | 0.045 | 0.000 | 88.399 | 88.399 | 88.399 |
| agent:create | 1/1 | 0 | 0 | 0.052 | 0.009 | 0.043 | 0.000 | 52.121 | 52.121 | 52.121 |
| harness:launch | 1/1 | 0 | 0 | 0.045 | n/a | n/a | 1.737 | 45.435 | 45.435 | 45.435 |
| syscall:bind | 13/13 | 0 | 0 | 0.043 | n/a | n/a | 0.241 | 3.283 | 2.920 | 5.711 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.000 | 3.842 | 3.842 | 3.842 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.266 | 1.266 | 1.266 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.069 | 0.071 | 0.092 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.166 | 0.166 | 0.166 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.062 | 0.062 | 0.062 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 3318 | 0.156 | 0.011 | 138.185 | 138.185 | 5.197238 CPU seconds | n/a |
| GPU 0 memory | MB | 3320 | 12014.371 | 11670.000 | 13984.000 | 11886.000 | n/a | n/a |
| GPU 0 power | W | 3320 | 42.905 | 29.227 | 74.810 | 29.421 | n/a | 143482.129 J |
| GPU 0 proc / 15668-1058323 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 memory | MB | 3320 | 3352.010 | 3118.000 | 5320.000 | 3220.000 | n/a | n/a |
| GPU 0 proc / 15668-1058323 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 estimated power | W | 1835 | 3.840 | 0.000 | 74.810 | 0.000 | n/a | n/a |
| GPU 0 proc / 15668-1058323 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 utilization | percent | 1835 | 4.613 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 15708-1060383 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 memory | MB | 3320 | 8180.361 | 8070.000 | 8184.000 | 8184.000 | n/a | n/a |
| GPU 0 proc / 15708-1060383 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 estimated power | W | 1427 | 41.796 | 0.000 | 72.934 | 0.000 | n/a | n/a |
| GPU 0 proc / 15708-1060383 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 utilization | percent | 1427 | 57.947 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 3320 | 11532.371 | 11188.000 | 13502.000 | 11404.000 | n/a | n/a |
| GPU 0 utilization | percent | 3320 | 28.416 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 3320 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 3319 | 0.635 | 0.090 | 8.444 | 5.373 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 3319 | 10.917 | 5.556 | 46.819 | 40.633 | n/a | n/a |
| host disk_read_mb_s | MB/s | 3319 | 0.084 | 0.000 | 62.001 | 1.021 | n/a | n/a |
| host disk_write_mb_s | MB/s | 3319 | 0.222 | 0.000 | 65.681 | 10.692 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 3319 | 0.084 | 0.000 | 49.157 | 2.404 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 3319 | 0.090 | 0.000 | 54.562 | 2.694 | n/a | n/a |
| host mem_total_mb | MB | 3320 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 3320 | 7798.037 | 6354.188 | 8205.867 | 8059.863 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 3319 | 0.001 | 0.000 | 1.881 | 0.151 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 3319 | 0.001 | 0.000 | 2.015 | 0.162 | n/a | n/a |
| host net_rx_mb_s | MB/s | 3319 | 0.011 | 0.000 | 24.066 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 3319 | 0.013 | 0.000 | 1.169 | 0.000 | n/a | n/a |
| Agency harness — python -m lsbench (PID 15668) CPU | percent | 3319 | 4.414 | 0.000 | 104.497 | 0.994 | 147.880000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 15668) io read MB/s | MB/s | 3319 | 0.001 | 0.000 | 0.831 | 0.070 | 2.191406 MB | n/a |
| Agency harness — python -m lsbench (PID 15668) io write MB/s | MB/s | 3319 | 0.126 | 0.015 | 65.214 | 0.027 | 421.640625 MB | n/a |
| Agency harness — python -m lsbench (PID 15668) rss_mb | MB | 3320 | 3701.106 | 2213.988 | 4076.535 | 4073.969 | n/a | n/a |
| Agency harness — python -m lsbench (PID 15668) main thread run-queue wait | percent | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 15668) vms_mb | MB | 3320 | 17194.747 | 13667.992 | 19721.711 | 17461.594 | n/a | n/a |
| Python — vllm (PID 15673) CPU | percent | 3319 | 0.857 | 0.000 | 6.954 | 0.000 | 28.720000 CPU seconds | n/a |
| Python — vllm (PID 15673) io read MB/s | MB/s | 3319 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 15673) io write MB/s | MB/s | 3319 | 0.000 | 0.000 | 0.008 | 0.000 | 0.148438 MB | n/a |
| Python — vllm (PID 15673) rss_mb | MB | 3320 | 1803.858 | 1800.738 | 1804.113 | 1804.113 | n/a | n/a |
| Python — vllm (PID 15673) main thread run-queue wait | percent | 3319 | 0.014 | 0.000 | 0.680 | 0.000 | 0.461405 run-queue seconds | n/a |
| Python — vllm (PID 15673) vms_mb | MB | 3320 | 11044.867 | 10972.477 | 11046.496 | 11046.496 | n/a | n/a |
| Python — python -c (PID 15707) CPU | percent | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 15707) io read MB/s | MB/s | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 15707) io write MB/s | MB/s | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 15707) rss_mb | MB | 3320 | 12.188 | 12.188 | 12.188 | 12.188 | n/a | n/a |
| Python — python -c (PID 15707) main thread run-queue wait | percent | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 15707) vms_mb | MB | 3320 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 15708) CPU | percent | 3319 | 9.634 | 0.000 | 43.520 | 0.000 | 322.670000 CPU seconds | n/a |
| VLLM::EngineCore (PID 15708) io read MB/s | MB/s | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 15708) io write MB/s | MB/s | 3319 | 0.000 | 0.000 | 0.004 | 0.000 | 0.019531 MB | n/a |
| VLLM::EngineCore (PID 15708) rss_mb | MB | 3320 | 2335.641 | 2331.766 | 2336.141 | 2336.141 | n/a | n/a |
| VLLM::EngineCore (PID 15708) main thread run-queue wait | percent | 3319 | 0.015 | 0.000 | 0.429 | 0.000 | 0.500317 run-queue seconds | n/a |
| VLLM::EngineCore (PID 15708) vms_mb | MB | 3320 | 21239.751 | 21236.246 | 21240.004 | 21240.004 | n/a | n/a |
| docker inspect (PID 15984) rss_mb | MB | 1 | 30.148 | 30.148 | 30.148 | 30.148 | n/a | n/a |
| docker inspect (PID 15984) vms_mb | MB | 1 | 1843.324 | 1843.324 | 1843.324 | 1843.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 16043) CPU | percent | 3317 | 0.002 | 0.000 | 1.990 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 16043) rss_mb | MB | 3318 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 16043) main thread run-queue wait | percent | 3317 | 0.000 | 0.000 | 0.050 | 0.000 | 0.001547 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 16043) vms_mb | MB | 3318 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 16075) CPU | percent | 3317 | 0.002 | 0.000 | 0.995 | 0.000 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 16075) rss_mb | MB | 3318 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 16075) main thread run-queue wait | percent | 3317 | 0.000 | 0.000 | 0.255 | 0.000 | 0.006043 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 16075) vms_mb | MB | 3318 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16167) CPU | percent | 3317 | 25.819 | 0.000 | 98.519 | 0.000 | 862.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16167) rss_mb | MB | 3318 | 116.067 | 2.977 | 124.461 | 124.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16167) main thread run-queue wait | percent | 3317 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000194 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16167) vms_mb | MB | 3318 | 973.627 | 4.262 | 976.938 | 973.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 16173) rss_mb | MB | 1 | 38.066 | 38.066 | 38.066 | 38.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 16173) vms_mb | MB | 1 | 44.809 | 44.809 | 44.809 | 44.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16190) CPU | percent | 3311 | 3.166 | 0.000 | 21.888 | 5.972 | 105.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16190) rss_mb | MB | 3312 | 138.617 | 25.289 | 148.762 | 145.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16190) main thread run-queue wait | percent | 3311 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000073 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16190) vms_mb | MB | 3312 | 377.193 | 343.035 | 507.070 | 394.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 16221) rss_mb | MB | 1 | 3.680 | 3.680 | 3.680 | 3.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 16221) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 16226) rss_mb | MB | 1 | 3.441 | 3.441 | 3.441 | 3.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 16226) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 16227) rss_mb | MB | 1 | 18.266 | 18.266 | 18.266 | 18.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 16227) vms_mb | MB | 1 | 99.594 | 99.594 | 99.594 | 99.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 16264) rss_mb | MB | 1 | 3.793 | 3.793 | 3.793 | 3.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 16264) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 16265) rss_mb | MB | 1 | 3.645 | 3.645 | 3.645 | 3.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 16265) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 16266) rss_mb | MB | 1 | 18.254 | 18.254 | 18.254 | 18.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 16266) vms_mb | MB | 1 | 100.484 | 100.484 | 100.484 | 100.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 16269) rss_mb | MB | 1 | 5.383 | 5.383 | 5.383 | 5.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 16269) vms_mb | MB | 1 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16291) rss_mb | MB | 1 | 21.969 | 21.969 | 21.969 | 21.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16291) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16299) rss_mb | MB | 1 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16299) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — rg (PID 16302) rss_mb | MB | 1 | 0.629 | 0.629 | 0.629 | 0.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — rg (PID 16302) vms_mb | MB | 1 | 5.617 | 5.617 | 5.617 | 5.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16310) rss_mb | MB | 1 | 15.215 | 15.215 | 15.215 | 15.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16310) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16465) rss_mb | MB | 1 | 130.668 | 130.668 | 130.668 | 130.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16465) vms_mb | MB | 1 | 387.449 | 387.449 | 387.449 | 387.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16596) rss_mb | MB | 1 | 19.750 | 19.750 | 19.750 | 19.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16596) vms_mb | MB | 1 | 24.730 | 24.730 | 24.730 | 24.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16607) rss_mb | MB | 1 | 9.855 | 9.855 | 9.855 | 9.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16607) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16643) rss_mb | MB | 1 | 16.273 | 16.273 | 16.273 | 16.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16643) vms_mb | MB | 1 | 21.773 | 21.773 | 21.773 | 21.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16658) rss_mb | MB | 1 | 14.965 | 14.965 | 14.965 | 14.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16658) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16679) rss_mb | MB | 1 | 18.391 | 18.391 | 18.391 | 18.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16679) vms_mb | MB | 1 | 24.383 | 24.383 | 24.383 | 24.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16697) rss_mb | MB | 1 | 136.645 | 136.645 | 136.645 | 136.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16697) vms_mb | MB | 1 | 391.348 | 391.348 | 391.348 | 391.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16711) rss_mb | MB | 1 | 14.695 | 14.695 | 14.695 | 14.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16711) vms_mb | MB | 1 | 19.887 | 19.887 | 19.887 | 19.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16813) rss_mb | MB | 1 | 137.371 | 137.371 | 137.371 | 137.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16813) vms_mb | MB | 1 | 392.250 | 392.250 | 392.250 | 392.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16888) rss_mb | MB | 1 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16888) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 16889) rss_mb | MB | 1 | 22.594 | 22.594 | 22.594 | 22.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 16889) vms_mb | MB | 1 | 133.945 | 133.945 | 133.945 | 133.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16943) rss_mb | MB | 1 | 6.664 | 6.664 | 6.664 | 6.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 16943) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16957) rss_mb | MB | 1 | 3.086 | 3.086 | 3.086 | 3.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 16957) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 16958) rss_mb | MB | 1 | 72.000 | 72.000 | 72.000 | 72.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 16958) vms_mb | MB | 1 | 209.512 | 209.512 | 209.512 | 209.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16990) rss_mb | MB | 1 | 140.324 | 140.324 | 140.324 | 140.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 16990) vms_mb | MB | 1 | 387.289 | 387.289 | 387.289 | 387.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17000) rss_mb | MB | 1 | 6.887 | 6.887 | 6.887 | 6.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17000) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17017) rss_mb | MB | 1 | 17.750 | 17.750 | 17.750 | 17.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17017) vms_mb | MB | 1 | 23.098 | 23.098 | 23.098 | 23.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 17621) rss_mb | MB | 1 | 138.340 | 138.340 | 138.340 | 138.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 17621) vms_mb | MB | 1 | 383.453 | 383.453 | 383.453 | 383.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17696) rss_mb | MB | 1 | 21.715 | 21.715 | 21.715 | 21.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17696) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17734) rss_mb | MB | 1 | 20.461 | 20.461 | 20.461 | 20.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17734) vms_mb | MB | 1 | 25.117 | 25.117 | 25.117 | 25.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17745) rss_mb | MB | 1 | 14.121 | 14.121 | 14.121 | 14.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 17745) vms_mb | MB | 1 | 19.887 | 19.887 | 19.887 | 19.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 17773) rss_mb | MB | 1 | 139.926 | 139.926 | 139.926 | 139.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 17773) vms_mb | MB | 1 | 385.332 | 385.332 | 385.332 | 385.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 18063) rss_mb | MB | 1 | 3.008 | 3.008 | 3.008 | 3.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 18063) vms_mb | MB | 1 | 4.398 | 4.398 | 4.398 | 4.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 18064) rss_mb | MB | 1 | 91.105 | 91.105 | 91.105 | 91.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 18064) vms_mb | MB | 1 | 239.059 | 239.059 | 239.059 | 239.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18142) rss_mb | MB | 1 | 6.848 | 6.848 | 6.848 | 6.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18142) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18151) rss_mb | MB | 1 | 17.094 | 17.094 | 17.094 | 17.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18151) vms_mb | MB | 1 | 22.066 | 22.066 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18183) rss_mb | MB | 1 | 16.430 | 16.430 | 16.430 | 16.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18183) vms_mb | MB | 1 | 21.773 | 21.773 | 21.773 | 21.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18239) rss_mb | MB | 1 | 9.918 | 9.918 | 9.918 | 9.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18239) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18278) rss_mb | MB | 1 | 14.977 | 14.977 | 14.977 | 14.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18278) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18306) rss_mb | MB | 1 | 9.371 | 9.371 | 9.371 | 9.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18306) vms_mb | MB | 1 | 13.488 | 13.488 | 13.488 | 13.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 18320) rss_mb | MB | 1 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 18320) vms_mb | MB | 1 | 4.395 | 4.395 | 4.395 | 4.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 18321) rss_mb | MB | 1 | 25.602 | 25.602 | 25.602 | 25.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 18321) vms_mb | MB | 1 | 138.750 | 138.750 | 138.750 | 138.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18335) rss_mb | MB | 1 | 21.496 | 21.496 | 21.496 | 21.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18335) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18347) rss_mb | MB | 1 | 20.484 | 20.484 | 20.484 | 20.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18347) vms_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18358) rss_mb | MB | 1 | 16.637 | 16.637 | 16.637 | 16.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 18358) vms_mb | MB | 1 | 22.109 | 22.109 | 22.109 | 22.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 18370) rss_mb | MB | 1 | 145.227 | 145.227 | 145.227 | 145.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 18370) vms_mb | MB | 1 | 390.590 | 390.590 | 390.590 | 390.590 | n/a | n/a |
| docker commit (PID 18405) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 18405) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 18405) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 18405) rss_mb | MB | 3 | 30.367 | 30.367 | 30.367 | 30.367 | n/a | n/a |
| docker commit (PID 18405) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 18405) vms_mb | MB | 3 | 1843.504 | 1843.504 | 1843.504 | 1843.504 | n/a | n/a |
| docker inspect (PID 18521) rss_mb | MB | 1 | 5.914 | 5.914 | 5.914 | 5.914 | n/a | n/a |
| docker inspect (PID 18521) vms_mb | MB | 1 | 69.043 | 69.043 | 69.043 | 69.043 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4781) CPU | percent | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4781) io read MB/s | MB/s | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4781) io write MB/s | MB/s | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4781) rss_mb | MB | 3320 | 3.168 | 3.168 | 3.168 | 3.168 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4781) main thread run-queue wait | percent | 3319 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4781) vms_mb | MB | 3320 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 3317 | 29.628 | 0.000 | 180.677 | 0.000 | 989.610700 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 3317 | 0.343 | 0.000 | 5.084 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 3317 | 0.361 | 0.000 | 8.491 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 3317 | 0.032 | 0.000 | 37.718 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 3317 | 0.035 | 0.000 | 41.287 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 3317 | 0.050 | 0.000 | 61.005 | 0.000 | 167.191406 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 3317 | 0.068 | 0.000 | 62.834 | 0.000 | 228.621094 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 3318 | 471.082 | 27.715 | 557.168 | 311.984 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 3317 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 3317 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 3317 | 0.007 | 0.000 | 23.241 | 0.000 | 25.047380 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 3317 | 0.001 | 0.000 | 0.281 | 0.000 | 2.130117 MB | n/a |
| workload total CPU | percent | 3319 | 14.911 | 1.554 | 104.561 | 9.963 | 499.571587 CPU seconds | n/a |
| workload total memory | MB | 3320 | 10381.409 | 8854.258 | 10783.602 | 10774.680 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
