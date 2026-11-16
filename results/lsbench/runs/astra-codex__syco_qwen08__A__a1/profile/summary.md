# agprof summary

- Duration: **1454.500 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **42 calls**, 42 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1111.046 s total wait
- Tools: **54/54 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **135290** at 1.979 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1454444.139 / 1454444.139 ms |
| LLM latency p50 / p95 | 19695.274 / 62679.133 ms |
| LLM TTFT p50 / p95 | 11437.877 / 21249.454 ms |
| LLM input / output tokens | 2335747 / 44051 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 42 total, 42 succeeded, 0 failed, 0 interrupted |
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
| Bash | 10/10 | 10 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 6/6 | 6 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 17/17 | 17 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 7/7 | 7 | 0 | 0 | n/a | n/a |
| update_plan | 5/5 | 5 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 4.658% | 101.576% | 67.756 s | 5920.632 MB | 6096.645 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker-init | 5212 | sandbox_agent_lsb-codex_0000_0000 | 1446 | 0.001% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python | 4883 |  | 1446 | 0.000% | 0.000% | 0.000 s | 12.180 MB | 12.180 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| tail | 5242 | sandbox_agent_lsb-codex_0000_0000 | 1446 | 0.001% | 0.993% | 0.020 s | 1.484 MB | 1.484 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 5340 | sandbox_agent_lsb-codex_0000_0000 | 2 | 99.870% | 99.870% | 1.010 s | 43.354 MB | 71.449 MB | 51.213 MB | 79.883 MB | n/a MB | n/a MB |
| bash | 5334 | sandbox_agent_lsb-codex_0000_0000 | 1446 | 20.898% | 96.536% | 303.640 s | 110.887 MB | 116.449 MB | 970.753 MB | 976.762 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 4884 |  | 1446 | 1.568% | 36.750% | 22.780 s | 2323.402 MB | 2323.504 MB | 21267.148 MB | 21267.148 MB | 0.000000 MB | 0.007812 MB |
| python | 4790 |  | 1446 | 2.973% | 100.198% | 43.270 s | 3207.591 MB | 3349.656 MB | 16464.611 MB | 16811.359 MB | 76.226562 MB | 236.632812 MB |
| lsb_grid_worker | 4781 |  | 1446 | 0.000% | 0.000% | 0.000 s | 3.312 MB | 3.312 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| vllm | 4795 |  | 1446 | 0.109% | 6.915% | 1.580 s | 1803.182 MB | 1803.258 MB | 11042.512 MB | 11044.582 MB | 0.003906 MB | 0.035156 MB |
| git | 5450 | sandbox_agent_lsb-codex_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.787 MB | 3.113 MB | 6.791 MB | 6.812 MB | n/a MB | n/a MB |
| codex | 5421 | sandbox_agent_lsb-codex_0000_0000 | 1195 | 2.111% | 19.747% | 25.350 s | 151.737 MB | 159.410 MB | 391.851 MB | 587.801 MB | n/a MB | n/a MB |
| bash | 5463 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.680 MB | 2.680 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 5464 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.570 MB | 1.570 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| git-remote-http | 5503 | sandbox_agent_lsb-codex_0000_0000 | 5 | 0.497% | 0.995% | 0.020 s | 4.773 MB | 11.289 MB | 44.084 MB | 93.930 MB | n/a MB | n/a MB |
| git | 5485 | sandbox_agent_lsb-codex_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.832 MB | 2.832 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 5512 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.672 MB | 3.672 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 5513 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.141 MB | 3.141 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 5517 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.762 MB | 4.762 MB | 8.285 MB | 8.285 MB | n/a MB | n/a MB |
| git-remote-http | 5514 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.246 MB | 18.246 MB | 100.590 MB | 100.590 MB | n/a MB | n/a MB |
| git | 5525 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.250 MB | 5.250 MB | 8.664 MB | 8.664 MB | n/a MB | n/a MB |
| python3 | 5549 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.551 MB | 15.551 MB | 20.426 MB | 20.426 MB | n/a MB | n/a MB |
| python3 | 5695 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.883 MB | 16.883 MB | 22.066 MB | 22.066 MB | n/a MB | n/a MB |
| python3 | 5894 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.344 MB | 10.344 MB | 15.203 MB | 15.203 MB | n/a MB | n/a MB |
| tokio-rt-worker | 5911 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 146.879 MB | 146.879 MB | 407.051 MB | 407.051 MB | n/a MB | n/a MB |
| find | 6135 | sandbox_agent_lsb-codex_0000_0000 | 9 | 1.740% | 2.985% | 0.140 s | 2.758 MB | 2.855 MB | 4.836 MB | 4.859 MB | n/a MB | n/a MB |
| bash | 6134 | sandbox_agent_lsb-codex_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| head | 6136 | sandbox_agent_lsb-codex_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.535 MB | 1.535 MB | 2.859 MB | 2.859 MB | n/a MB | n/a MB |
| python | 6151 | sandbox_agent_lsb-codex_0000_0000 | 4 | 6.960% | 9.940% | 0.210 s | 21.967 MB | 44.234 MB | 123.803 MB | 186.578 MB | n/a MB | n/a MB |
| bash | 6150 | sandbox_agent_lsb-codex_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.699 MB | 2.699 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 6173 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.512 MB | 21.512 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python | 6223 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 53.848 MB | 53.848 MB | 164.348 MB | 164.348 MB | n/a MB | n/a MB |
| bash | 6222 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.824 MB | 2.824 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 6255 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.484 MB | 11.484 MB | 19.844 MB | 19.844 MB | n/a MB | n/a MB |
| python3 | 6301 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.070 MB | 9.070 MB | 13.488 MB | 13.488 MB | n/a MB | n/a MB |
| python3 | 6303 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.051 MB | 18.051 MB | 24.227 MB | 24.227 MB | n/a MB | n/a MB |
| bash | 6392 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6393 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.484 MB | 5.484 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| bash | 6408 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.605 MB | 2.605 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 6411 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.332 MB | 7.332 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python3 | 6420 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.914 MB | 19.914 MB | 24.988 MB | 24.988 MB | n/a MB | n/a MB |
| python3 | 6424 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.516 MB | 18.516 MB | 24.621 MB | 24.621 MB | n/a MB | n/a MB |
| python3 | 6555 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.832 MB | 9.832 MB | 13.617 MB | 13.617 MB | n/a MB | n/a MB |
| python3 | 6563 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.078 MB | 6.078 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python3 | 6588 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.164 MB | 6.164 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| python3 | 6591 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.062 MB | 18.062 MB | 24.277 MB | 24.277 MB | n/a MB | n/a MB |
| python3 | 6602 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.574 MB | 19.574 MB | 24.730 MB | 24.730 MB | n/a MB | n/a MB |
| tokio-rt-worker | 6607 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 155.199 MB | 155.199 MB | 398.164 MB | 398.164 MB | n/a MB | n/a MB |
| bash | 6618 | sandbox_agent_lsb-codex_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.973 MB | 2.973 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python | 6619 | sandbox_agent_lsb-codex_0000_0000 | 7 | 9.781% | 26.856% | 0.590 s | 48.934 MB | 126.879 MB | 241.181 MB | 409.758 MB | n/a MB | n/a MB |
| python3 | 6632 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.301 MB | 16.301 MB | 21.773 MB | 21.773 MB | n/a MB | n/a MB |
| python3 | 6688 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.324 MB | 15.324 MB | 20.426 MB | 20.426 MB | n/a MB | n/a MB |
| python3 | 6711 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.430 MB | 19.430 MB | 24.730 MB | 24.730 MB | n/a MB | n/a MB |
| python3 | 6719 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.930 MB | 17.930 MB | 23.098 MB | 23.098 MB | n/a MB | n/a MB |
| docker | 6757 |  | 120 | 0.000% | 0.000% | 0.000 s | 29.500 MB | 29.500 MB | 1835.008 MB | 1835.008 MB | 0.000000 MB | 0.000000 MB |
| docker | 6779 |  | 119 | 0.000% | 0.000% | 0.000 s | 30.207 MB | 30.207 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |
| docker | 6819 |  | 5 | 0.000% | 0.000% | 0.000 s | 30.523 MB | 30.523 MB | 1907.340 MB | 1907.340 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.711% | 91.000% | 11870.747 MB | 12122.000 MB | 29.784 W | 63.902 W | 43269.114 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 23.831% | 128.367% | 346.285 s | 289.724 MB | 452.699 MB | 55.214844 MB | 160.007812 MB | 25.255790 MB | 1.204665 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 5100 | 1454.449 | interrupted |
| harness:retire | -1 | 0.362 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1454.444 | n/a | n/a | 55.215 | 1454444.139 | 1454444.139 | 1454444.139 |
| sync:result_wait | 1/1 | 0 | 0 | 1454.443 | 0.000 | 1454.443 | 55.215 | 1454443.415 | 1454443.415 | 1454443.415 |
| engine:execute | 1/1 | 0 | 0 | 1454.443 | 1.865 | 1452.576 | 55.215 | 1454442.725 | 1454442.725 | 1454442.725 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1203.123 | 0.002 | 1203.121 | 55.205 | 1203122.766 | 1203122.766 | 1203122.766 |
| harness:await_cli | 1/1 | 0 | 0 | 1199.417 | n/a | n/a | 50.174 | 1199417.447 | 1199417.447 | 1199417.447 |
| llm:attempt | 42/42 | 0 | 0 | 1111.046 | 5.394 | 1105.650 | 12.820 | 26453.467 | 19695.274 | 62679.133 |
| teardown:commit | 1/1 | 0 | 0 | 247.472 | 0.009 | 247.463 | 0.000 | 247472.273 | 247472.273 | 247472.273 |
| sandbox:commit | 1/1 | 0 | 0 | 247.274 | 0.008 | 247.266 | 0.000 | 247273.535 | 247273.535 | 247273.535 |
| checkpoint.total | 1/1 | 0 | 0 | 247.273 | 0.008 | 247.266 | 0.000 | 247273.399 | 247273.399 | 247273.399 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 247.273 | 0.007 | 247.266 | 0.000 | 247273.260 | 247273.260 | 247273.260 |
| run:container_call | 15/15 | 2 | 0 | 245.885 | 0.003 | 245.882 | 0.000 | 16392.352 | 53.187 | 120059.006 |
| tool:Bash | 10/10 | 0 | 0 | 24.016 | n/a | n/a | 36.705 | 2401.645 | 535.963 | 8560.012 |
| tool:mcp__agency__inspect | 2/2 | 0 | 0 | 12.883 | n/a | n/a | 0.000 | 6441.457 | 6441.457 | 10392.864 |
| tool:mcp__agency__trace | 7/7 | 0 | 0 | 12.170 | n/a | n/a | 0.000 | 1738.622 | 1943.227 | 2010.527 |
| tool:mcp__agency__patch | 17/17 | 0 | 0 | 6.839 | n/a | n/a | 0.000 | 402.296 | 400.766 | 424.103 |
| tool:mcp__agency__generate | 6/6 | 0 | 0 | 5.613 | n/a | n/a | 0.003 | 935.513 | 835.464 | 1398.641 |
| tool:mcp__agency__inspect_module_inputs | 2/2 | 0 | 0 | 3.988 | n/a | n/a | 0.000 | 1993.952 | 1993.952 | 1999.958 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.176 | 0.705 | 2.471 | 0.009 | 3176.206 | 3176.206 | 3176.206 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.176 | 0.705 | 2.471 | 0.009 | 3175.900 | 3175.900 | 3175.900 |
| syscall:execve | 624/624 | 0 | 0 | 2.125 | n/a | n/a | 3.754 | 3.405 | 1.153 | 2.469 |
| tool:mcp__agency__logit_lens | 1/1 | 0 | 0 | 1.678 | n/a | n/a | 0.000 | 1678.194 | 1678.194 | 1678.194 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 1.369 | n/a | n/a | 0.000 | 1368.503 | 1368.503 | 1368.503 |
| syscall:connect | 469/469 | 0 | 0 | 1.066 | n/a | n/a | 0.234 | 2.273 | 2.050 | 4.231 |
| harness:submit | 1/1 | 0 | 0 | 1.013 | n/a | n/a | 3.996 | 1013.277 | 1013.277 | 1013.277 |
| tool:update_plan | 5/5 | 0 | 0 | 0.897 | n/a | n/a | 0.000 | 179.427 | 180.458 | 196.430 |
| harness:startup_ready | 1/1 | 0 | 0 | 0.818 | n/a | n/a | 0.871 | 818.383 | 818.383 | 818.383 |
| syscall:sendto | 346/346 | 0 | 0 | 0.814 | n/a | n/a | 0.145 | 2.353 | 2.192 | 4.017 |
| harness:snapshot | 1/1 | 0 | 0 | 0.783 | n/a | n/a | 0.000 | 782.559 | 782.559 | 782.559 |
| tool:mcp__agency__attention | 1/1 | 0 | 0 | 0.624 | n/a | n/a | 0.000 | 624.077 | 624.077 | 624.077 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.469 | n/a | n/a | 0.000 | 468.601 | 468.601 | 468.601 |
| sandbox:start | 1/1 | 0 | 0 | 0.438 | 0.002 | 0.436 | 0.000 | 438.013 | 438.013 | 438.013 |
| runtime.container_create | 1/1 | 0 | 0 | 0.438 | 0.002 | 0.436 | 0.000 | 437.870 | 437.870 | 437.870 |
| sandbox:create | 1/1 | 0 | 0 | 0.335 | 0.242 | 0.093 | 0.000 | 334.708 | 334.708 | 334.708 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.235 | n/a | n/a | 0.000 | 234.541 | 234.541 | 234.541 |
| agency:services_close | 1/1 | 0 | 0 | 0.202 | 0.000 | 0.202 | 0.000 | 202.409 | 202.409 | 202.409 |
| sandbox:stop | 1/1 | 0 | 0 | 0.198 | 0.002 | 0.197 | 0.000 | 198.465 | 198.465 | 198.465 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.042 | 0.031 | 0.000 | 73.278 | 73.278 | 73.278 |
| run:detect | 1/1 | 0 | 0 | 0.053 | 0.001 | 0.052 | 0.000 | 52.688 | 52.688 | 52.688 |
| harness:launch | 1/1 | 0 | 0 | 0.044 | n/a | n/a | 0.046 | 43.611 | 43.611 | 43.611 |
| agent:create | 1/1 | 0 | 0 | 0.036 | 0.007 | 0.030 | 0.000 | 36.226 | 36.226 | 36.226 |
| syscall:bind | 5/5 | 0 | 0 | 0.009 | n/a | n/a | 0.007 | 1.865 | 1.799 | 2.654 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.965 | 1.965 | 1.965 |
| sync:container | 15/15 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.084 | 0.063 | 0.189 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.210 | 1.210 | 1.210 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.170 | 0.170 | 0.170 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.052 | 0.052 | 0.052 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1445 | 0.800 | 0.041 | 167.666 | 30.002 | 11.627226 CPU seconds | n/a |
| GPU 0 memory | MB | 1446 | 11870.747 | 11670.000 | 12122.000 | 11844.000 | n/a | n/a |
| GPU 0 power | W | 1446 | 29.784 | 29.148 | 63.902 | 29.222 | n/a | 43269.114 J |
| GPU 0 proc / 4790-292676 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 memory | MB | 1446 | 3244.607 | 3118.000 | 3496.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 4790-292676 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 estimated power | W | 1247 | 1.317 | 0.000 | 55.065 | 0.000 | n/a | n/a |
| GPU 0 proc / 4790-292676 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 utilization | percent | 1247 | 0.729 | 0.000 | 46.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 4884-294521 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 memory | MB | 1446 | 8144.140 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 4884-294521 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 estimated power | W | 183 | 1.716 | 0.000 | 63.902 | 0.000 | n/a | n/a |
| GPU 0 proc / 4884-294521 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 utilization | percent | 183 | 1.694 | 0.000 | 59.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1446 | 11388.747 | 11188.000 | 11640.000 | 11362.000 | n/a | n/a |
| GPU 0 utilization | percent | 1446 | 0.711 | 0.000 | 91.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1446 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1445 | 0.548 | 0.124 | 4.888 | 0.958 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1445 | 7.041 | 0.248 | 42.147 | 7.888 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1445 | 1.188 | 0.000 | 204.822 | 8.448 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1445 | 0.332 | 0.000 | 67.914 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1445 | 14.068 | 0.000 | 98.285 | 37.085 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1445 | 14.207 | 0.000 | 98.819 | 37.223 | n/a | n/a |
| host mem_total_mb | MB | 1446 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1446 | 7275.410 | 6743.730 | 7461.230 | 7402.965 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1445 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1445 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1445 | 0.023 | 0.000 | 16.440 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1445 | 0.011 | 0.000 | 0.637 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4781) CPU | percent | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4781) io read MB/s | MB/s | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4781) io write MB/s | MB/s | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4781) rss_mb | MB | 1446 | 3.312 | 3.312 | 3.312 | 3.312 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4781) main thread run-queue wait | percent | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4781) vms_mb | MB | 1446 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4790) CPU | percent | 1445 | 2.973 | 0.000 | 100.198 | 0.000 | 43.270000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 4790) io read MB/s | MB/s | 1445 | 0.052 | 0.000 | 10.232 | 0.000 | 76.226562 MB | n/a |
| Agency harness — python -m lsbench (PID 4790) io write MB/s | MB/s | 1445 | 0.162 | 0.016 | 14.221 | 0.023 | 236.632812 MB | n/a |
| Agency harness — python -m lsbench (PID 4790) rss_mb | MB | 1446 | 3207.591 | 2602.914 | 3349.656 | 3349.656 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4790) main thread run-queue wait | percent | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 4790) vms_mb | MB | 1446 | 16464.611 | 14180.852 | 16811.359 | 16623.977 | n/a | n/a |
| Python — vllm (PID 4795) CPU | percent | 1445 | 0.109 | 0.000 | 6.915 | 0.000 | 1.580000 CPU seconds | n/a |
| Python — vllm (PID 4795) io read MB/s | MB/s | 1445 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 4795) io write MB/s | MB/s | 1445 | 0.000 | 0.000 | 0.008 | 0.000 | 0.035156 MB | n/a |
| Python — vllm (PID 4795) rss_mb | MB | 1446 | 1803.182 | 1802.383 | 1803.258 | 1803.258 | n/a | n/a |
| Python — vllm (PID 4795) main thread run-queue wait | percent | 1445 | 0.002 | 0.000 | 0.540 | 0.000 | 0.033630 run-queue seconds | n/a |
| Python — vllm (PID 4795) vms_mb | MB | 1446 | 11042.512 | 10971.562 | 11044.582 | 11044.582 | n/a | n/a |
| Python — python -c (PID 4883) CPU | percent | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 4883) io read MB/s | MB/s | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4883) io write MB/s | MB/s | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4883) rss_mb | MB | 1446 | 12.180 | 12.180 | 12.180 | 12.180 | n/a | n/a |
| Python — python -c (PID 4883) main thread run-queue wait | percent | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 4883) vms_mb | MB | 1446 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 4884) CPU | percent | 1445 | 1.568 | 0.000 | 36.750 | 0.995 | 22.780000 CPU seconds | n/a |
| VLLM::EngineCore (PID 4884) io read MB/s | MB/s | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 4884) io write MB/s | MB/s | 1445 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 4884) rss_mb | MB | 1446 | 2323.402 | 2323.379 | 2323.504 | 2323.504 | n/a | n/a |
| VLLM::EngineCore (PID 4884) main thread run-queue wait | percent | 1445 | 0.001 | 0.000 | 0.319 | 0.000 | 0.012755 run-queue seconds | n/a |
| VLLM::EngineCore (PID 4884) vms_mb | MB | 1446 | 21267.148 | 21267.148 | 21267.148 | 21267.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5212) CPU | percent | 1445 | 0.001 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5212) rss_mb | MB | 1446 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5212) main thread run-queue wait | percent | 1445 | 0.000 | 0.000 | 0.098 | 0.000 | 0.001480 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5212) vms_mb | MB | 1446 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5242) CPU | percent | 1445 | 0.001 | 0.000 | 0.993 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5242) rss_mb | MB | 1446 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5242) main thread run-queue wait | percent | 1445 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000732 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5242) vms_mb | MB | 1446 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5334) CPU | percent | 1445 | 20.898 | 0.000 | 96.536 | 0.000 | 303.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5334) rss_mb | MB | 1446 | 110.887 | 3.086 | 116.449 | 116.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5334) main thread run-queue wait | percent | 1445 | 0.000 | 0.000 | 0.009 | 0.000 | 0.000100 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5334) vms_mb | MB | 1446 | 970.753 | 4.262 | 976.762 | 975.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5340) CPU | percent | 1 | 99.870 | 99.870 | 99.870 | 99.870 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5340) rss_mb | MB | 2 | 43.354 | 15.258 | 71.449 | 71.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5340) main thread run-queue wait | percent | 1 | 0.008 | 0.008 | 0.008 | 0.008 | 0.000084 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5340) vms_mb | MB | 2 | 51.213 | 22.543 | 79.883 | 79.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5421) CPU | percent | 1194 | 2.111 | 0.000 | 19.747 | 4.976 | 25.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5421) rss_mb | MB | 1195 | 151.737 | 101.805 | 159.410 | 157.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5421) main thread run-queue wait | percent | 1194 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000014 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5421) vms_mb | MB | 1195 | 391.851 | 363.352 | 587.801 | 397.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5450) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5450) rss_mb | MB | 6 | 2.787 | 1.531 | 3.113 | 3.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5450) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000009 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5450) vms_mb | MB | 6 | 6.791 | 6.684 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5463) rss_mb | MB | 1 | 2.680 | 2.680 | 2.680 | 2.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5463) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5464) rss_mb | MB | 1 | 1.570 | 1.570 | 1.570 | 1.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5464) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5485) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5485) rss_mb | MB | 5 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5485) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5485) vms_mb | MB | 5 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5503) CPU | percent | 4 | 0.497 | 0.000 | 0.995 | 0.995 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5503) rss_mb | MB | 5 | 4.773 | 0.129 | 11.289 | 11.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5503) main thread run-queue wait | percent | 4 | 0.006 | 0.001 | 0.015 | 0.004 | 0.000227 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5503) vms_mb | MB | 5 | 44.084 | 3.227 | 93.930 | 93.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5512) rss_mb | MB | 1 | 3.672 | 3.672 | 3.672 | 3.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5512) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5513) rss_mb | MB | 1 | 3.141 | 3.141 | 3.141 | 3.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5513) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5514) rss_mb | MB | 1 | 18.246 | 18.246 | 18.246 | 18.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5514) vms_mb | MB | 1 | 100.590 | 100.590 | 100.590 | 100.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 5517) rss_mb | MB | 1 | 4.762 | 4.762 | 4.762 | 4.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 5517) vms_mb | MB | 1 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5525) rss_mb | MB | 1 | 5.250 | 5.250 | 5.250 | 5.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5525) vms_mb | MB | 1 | 8.664 | 8.664 | 8.664 | 8.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5549) rss_mb | MB | 1 | 15.551 | 15.551 | 15.551 | 15.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5549) vms_mb | MB | 1 | 20.426 | 20.426 | 20.426 | 20.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5695) rss_mb | MB | 1 | 16.883 | 16.883 | 16.883 | 16.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5695) vms_mb | MB | 1 | 22.066 | 22.066 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5894) rss_mb | MB | 1 | 10.344 | 10.344 | 10.344 | 10.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5894) vms_mb | MB | 1 | 15.203 | 15.203 | 15.203 | 15.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5911) rss_mb | MB | 1 | 146.879 | 146.879 | 146.879 | 146.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5911) vms_mb | MB | 1 | 407.051 | 407.051 | 407.051 | 407.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6134) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6134) rss_mb | MB | 9 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6134) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6134) vms_mb | MB | 9 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 6135) CPU | percent | 8 | 1.740 | 0.000 | 2.985 | 0.995 | 0.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 6135) rss_mb | MB | 9 | 2.758 | 2.562 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 6135) main thread run-queue wait | percent | 8 | 0.007 | 0.000 | 0.015 | 0.005 | 0.000571 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 6135) vms_mb | MB | 9 | 4.836 | 4.730 | 4.859 | 4.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 6136) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 6136) rss_mb | MB | 9 | 1.535 | 1.535 | 1.535 | 1.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 6136) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 6136) vms_mb | MB | 9 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6150) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6150) rss_mb | MB | 4 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6150) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6150) vms_mb | MB | 4 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6151) CPU | percent | 3 | 6.960 | 4.974 | 9.940 | 4.974 | 0.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6151) rss_mb | MB | 4 | 21.967 | 9.699 | 44.234 | 44.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6151) main thread run-queue wait | percent | 3 | 0.006 | 0.000 | 0.010 | 0.010 | 0.000185 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6151) vms_mb | MB | 4 | 123.803 | 47.855 | 186.578 | 186.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6173) rss_mb | MB | 1 | 21.512 | 21.512 | 21.512 | 21.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6173) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6222) rss_mb | MB | 1 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6222) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6223) rss_mb | MB | 1 | 53.848 | 53.848 | 53.848 | 53.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6223) vms_mb | MB | 1 | 164.348 | 164.348 | 164.348 | 164.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6255) rss_mb | MB | 1 | 11.484 | 11.484 | 11.484 | 11.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6255) vms_mb | MB | 1 | 19.844 | 19.844 | 19.844 | 19.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6301) rss_mb | MB | 1 | 9.070 | 9.070 | 9.070 | 9.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6301) vms_mb | MB | 1 | 13.488 | 13.488 | 13.488 | 13.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6303) rss_mb | MB | 1 | 18.051 | 18.051 | 18.051 | 18.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6303) vms_mb | MB | 1 | 24.227 | 24.227 | 24.227 | 24.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6392) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6392) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6393) rss_mb | MB | 1 | 5.484 | 5.484 | 5.484 | 5.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6393) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6408) rss_mb | MB | 1 | 2.605 | 2.605 | 2.605 | 2.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6408) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6411) rss_mb | MB | 1 | 7.332 | 7.332 | 7.332 | 7.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6411) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6420) rss_mb | MB | 1 | 19.914 | 19.914 | 19.914 | 19.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6420) vms_mb | MB | 1 | 24.988 | 24.988 | 24.988 | 24.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6424) rss_mb | MB | 1 | 18.516 | 18.516 | 18.516 | 18.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6424) vms_mb | MB | 1 | 24.621 | 24.621 | 24.621 | 24.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6555) rss_mb | MB | 1 | 9.832 | 9.832 | 9.832 | 9.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6555) vms_mb | MB | 1 | 13.617 | 13.617 | 13.617 | 13.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6563) rss_mb | MB | 1 | 6.078 | 6.078 | 6.078 | 6.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6563) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6588) rss_mb | MB | 1 | 6.164 | 6.164 | 6.164 | 6.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6588) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6591) rss_mb | MB | 1 | 18.062 | 18.062 | 18.062 | 18.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6591) vms_mb | MB | 1 | 24.277 | 24.277 | 24.277 | 24.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6602) rss_mb | MB | 1 | 19.574 | 19.574 | 19.574 | 19.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6602) vms_mb | MB | 1 | 24.730 | 24.730 | 24.730 | 24.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 6607) rss_mb | MB | 1 | 155.199 | 155.199 | 155.199 | 155.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 6607) vms_mb | MB | 1 | 398.164 | 398.164 | 398.164 | 398.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6618) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6618) rss_mb | MB | 7 | 2.973 | 2.973 | 2.973 | 2.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6618) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6618) vms_mb | MB | 7 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6619) CPU | percent | 6 | 9.781 | 0.000 | 26.856 | 26.856 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6619) rss_mb | MB | 7 | 48.934 | 27.148 | 126.879 | 126.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6619) main thread run-queue wait | percent | 6 | 0.008 | 0.001 | 0.015 | 0.013 | 0.000457 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6619) vms_mb | MB | 7 | 241.181 | 138.449 | 409.758 | 409.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6632) rss_mb | MB | 1 | 16.301 | 16.301 | 16.301 | 16.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6632) vms_mb | MB | 1 | 21.773 | 21.773 | 21.773 | 21.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6688) rss_mb | MB | 1 | 15.324 | 15.324 | 15.324 | 15.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6688) vms_mb | MB | 1 | 20.426 | 20.426 | 20.426 | 20.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6711) rss_mb | MB | 1 | 19.430 | 19.430 | 19.430 | 19.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6711) vms_mb | MB | 1 | 24.730 | 24.730 | 24.730 | 24.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6719) rss_mb | MB | 1 | 17.930 | 17.930 | 17.930 | 17.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6719) vms_mb | MB | 1 | 23.098 | 23.098 | 23.098 | 23.098 | n/a | n/a |
| docker commit (PID 6757) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6757) io read MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6757) io write MB/s | MB/s | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6757) rss_mb | MB | 120 | 29.500 | 29.500 | 29.500 | 29.500 | n/a | n/a |
| docker commit (PID 6757) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6757) vms_mb | MB | 120 | 1835.008 | 1835.008 | 1835.008 | 1835.008 | n/a | n/a |
| docker commit (PID 6779) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6779) io read MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6779) io write MB/s | MB/s | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6779) rss_mb | MB | 119 | 30.207 | 30.207 | 30.207 | 30.207 | n/a | n/a |
| docker commit (PID 6779) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6779) vms_mb | MB | 119 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker commit (PID 6819) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6819) io read MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6819) io write MB/s | MB/s | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6819) rss_mb | MB | 5 | 30.523 | 30.523 | 30.523 | 30.523 | n/a | n/a |
| docker commit (PID 6819) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6819) vms_mb | MB | 5 | 1907.340 | 1907.340 | 1907.340 | 1907.340 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 1445 | 23.831 | 0.000 | 128.367 | 0.000 | 346.284778 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1445 | 0.295 | 0.000 | 3.413 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1445 | 0.304 | 0.000 | 4.470 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 1445 | 0.811 | 0.000 | 79.303 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 1445 | 0.840 | 0.000 | 82.234 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 1445 | 0.038 | 0.000 | 4.286 | 0.000 | 55.214844 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 1445 | 0.110 | 0.000 | 67.914 | 0.000 | 160.007812 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 1446 | 289.724 | 10.305 | 452.699 | 174.074 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1445 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 1445 | 0.017 | 0.000 | 15.824 | 0.000 | 25.255790 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 1445 | 0.001 | 0.000 | 0.286 | 0.000 | 1.204665 MB | n/a |
| workload total CPU | percent | 1445 | 4.658 | 1.409 | 101.576 | 1.909 | 67.756181 CPU seconds | n/a |
| workload total memory | MB | 1446 | 5920.632 | 5263.832 | 6096.645 | 6096.508 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
