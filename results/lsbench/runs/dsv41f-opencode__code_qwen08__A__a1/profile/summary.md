# agprof summary

- Duration: **1126.745 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **136 calls**, 125 succeeded, 11 failed, 0 interrupted, n/a reported retries, 859.106 s total wait
- Tools: **124/124 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **106505** at 1.973 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1126677.177 / 1126677.177 ms |
| LLM latency p50 / p95 | 4741.099 / 15323.067 ms |
| LLM TTFT p50 / p95 | 2609.642 / 7472.720 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 136 total, 125 succeeded, 11 failed, 0 interrupted |
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
| bash | 111/111 | 111 | 0 | 0 | n/a | n/a |
| edit | 2/2 | 2 | 0 | 0 | n/a | n/a |
| read | 1/1 | 1 | 0 | 0 | n/a | n/a |
| write | 10/10 | 10 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.956% | 101.944% | 67.231 s | 7975.675 MB | 8626.453 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| runc:[2:INIT] | 13766 | sandbox_agent_lsb-opencode_0000_0000 | 1118 | 35.694% | 100.465% | 401.430 s | 111.483 MB | 127.516 MB | 898.303 MB | 1601.203 MB | n/a MB | n/a MB |
| docker-init | 13642 | sandbox_agent_lsb-opencode_0000_0000 | 1118 | 0.002% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 13423 |  | 1119 | 1.557% | 37.636% | 17.540 s | 2321.961 MB | 2321.961 MB | 21204.207 MB | 21204.207 MB | 0.000000 MB | 0.003906 MB |
| vllm | 13388 |  | 1119 | 0.166% | 5.959% | 1.870 s | 1803.683 MB | 1803.953 MB | 11023.687 MB | 11044.719 MB | 0.007812 MB | 0.031250 MB |
| tail | 13674 | sandbox_agent_lsb-opencode_0000_0000 | 1118 | 0.002% | 0.995% | 0.020 s | 1.430 MB | 1.430 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 13422 |  | 1119 | 0.000% | 0.000% | 0.000 s | 12.176 MB | 12.176 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| lsb_grid_worker | 4616 |  | 1119 | 0.000% | 0.000% | 0.000 s | 3.391 MB | 3.391 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 13383 |  | 1119 | 4.224% | 102.009% | 47.680 s | 3034.159 MB | 3684.949 MB | 15847.162 MB | 17349.980 MB | 1.855469 MB | 270.011719 MB |
| docker | 13743 |  | 1 | n/a% | n/a% | n/a s | 30.664 MB | 30.664 MB | 1843.266 MB | 1843.266 MB | n/a MB | n/a MB |
| python3 | 13772 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 70.614% | 70.614% | 0.710 s | 66.363 MB | 83.445 MB | 77.566 MB | 97.996 MB | n/a MB | n/a MB |
| opencode | 13780 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 48.441 MB | 48.441 MB | 6431.648 MB | 6431.648 MB | n/a MB | n/a MB |
| opencode | 13793 | sandbox_agent_lsb-opencode_0000_0000 | 1108 | 6.441% | 127.312% | 71.770 s | 768.396 MB | 941.574 MB | 16594.704 MB | 16830.266 MB | n/a MB | n/a MB |
| head | 13858 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.129 MB | 1.129 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 13855 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| grep | 13859 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 3.410 MB | 3.410 MB | n/a MB | n/a MB |
| xargs | 13857 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.730 MB | 2.730 MB | n/a MB | n/a MB |
| bash | 13865 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| grep | 13867 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.775 MB | 1.816 MB | 3.391 MB | 3.391 MB | n/a MB | n/a MB |
| xargs | 13878 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.535 MB | 1.535 MB | 2.730 MB | 2.730 MB | n/a MB | n/a MB |
| head | 13880 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.191 MB | 1.191 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 13876 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.703 MB | 2.703 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| grep | 13884 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.773 MB | 1.773 MB | 3.434 MB | 3.434 MB | n/a MB | n/a MB |
| grep | 13879 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.508 MB | 1.508 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| bash | 13890 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.824 MB | 2.824 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| ls | 13894 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.516 MB | 0.516 MB | n/a MB | n/a MB |
| xargs | 13931 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.980 MB | 0.980 MB | 2.730 MB | 2.730 MB | n/a MB | n/a MB |
| xargs | 13927 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.730 MB | 2.730 MB | n/a MB | n/a MB |
| head | 13929 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.176 MB | 1.176 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| find | 13926 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.367 MB | 2.367 MB | 4.527 MB | 4.527 MB | n/a MB | n/a MB |
| grep | 13928 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.648 MB | 1.648 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| bash | 13925 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.523 MB | 2.523 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 13937 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.746 MB | 2.746 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 13939 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.129 MB | 1.129 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| grep | 13938 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.555 MB | 7.555 MB | 9.211 MB | 9.211 MB | n/a MB | n/a MB |
| grep | 13946 | sandbox_agent_lsb-opencode_0000_0000 | 119 | 97.637% | 101.425% | 115.920 s | 14.513 MB | 14.617 MB | 16.192 MB | 16.297 MB | n/a MB | n/a MB |
| grep | 13947 | sandbox_agent_lsb-opencode_0000_0000 | 119 | 0.000% | 0.000% | 0.000 s | 1.430 MB | 1.430 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| bash | 13945 | sandbox_agent_lsb-opencode_0000_0000 | 119 | 0.000% | 0.000% | 0.000 s | 2.824 MB | 2.824 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 13948 | sandbox_agent_lsb-opencode_0000_0000 | 119 | 0.000% | 0.000% | 0.000 s | 1.238 MB | 1.238 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| find | 14024 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.227 MB | 2.227 MB | 4.270 MB | 4.270 MB | n/a MB | n/a MB |
| grep | 14025 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.613 MB | 1.613 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| bash | 14019 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.625 MB | 2.625 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 14026 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.094 MB | 1.094 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| grep | 14062 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.148 MB | 0.148 MB | 1.246 MB | 1.246 MB | n/a MB | n/a MB |
| xargs | 14061 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.398 MB | 1.398 MB | 2.730 MB | 2.730 MB | n/a MB | n/a MB |
| bash | 14055 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.617 MB | 2.617 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14084 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 10.457 MB | 10.457 MB | 13.758 MB | 13.758 MB | n/a MB | n/a MB |
| bash | 14287 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.785 MB | 2.785 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14288 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.855 MB | 20.855 MB | 25.402 MB | 25.402 MB | n/a MB | n/a MB |
| python3 | 14321 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.309 MB | 21.309 MB | 26.652 MB | 26.652 MB | n/a MB | n/a MB |
| bash | 14344 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.555 MB | 2.555 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| tail | 14346 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python3 | 14345 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 21.738 MB | 21.738 MB | 26.797 MB | 26.797 MB | n/a MB | n/a MB |
| bash | 14371 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.715 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| grep | 14374 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.723 MB | 1.723 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| python3 | 14372 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 21.234 MB | 21.234 MB | 26.633 MB | 26.633 MB | n/a MB | n/a MB |
| tr | 14397 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.465 MB | 2.465 MB | n/a MB | n/a MB |
| python3 | 14396 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 1.490% | 5.959% | 0.060 s | 20.782 MB | 21.711 MB | 25.665 MB | 26.633 MB | n/a MB | n/a MB |
| grep | 14398 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.457 MB | 1.457 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| bash | 14395 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14436 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.430 MB | 10.430 MB | 13.598 MB | 13.598 MB | n/a MB | n/a MB |
| python3 | 14504 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.320 MB | 21.320 MB | 26.656 MB | 26.656 MB | n/a MB | n/a MB |
| python3 | 14512 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.395 MB | 21.395 MB | 26.566 MB | 26.566 MB | n/a MB | n/a MB |
| grep | 14589 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.691 MB | 1.691 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| pip | 14588 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.359 MB | 21.359 MB | 26.184 MB | 26.184 MB | n/a MB | n/a MB |
| bash | 14585 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.758 MB | 2.758 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14593 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.797 MB | 9.797 MB | 19.750 MB | 19.750 MB | n/a MB | n/a MB |
| python3 | 14597 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.273 MB | 21.273 MB | 26.656 MB | 26.656 MB | n/a MB | n/a MB |
| python3 | 14604 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.133 MB | 21.133 MB | 26.660 MB | 26.660 MB | n/a MB | n/a MB |
| python3 | 14609 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.930 MB | 8.930 MB | 13.191 MB | 13.191 MB | n/a MB | n/a MB |
| python3 | 14619 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.594 MB | 21.594 MB | 26.781 MB | 26.781 MB | n/a MB | n/a MB |
| bash | 14623 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.582 MB | 2.582 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14654 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 2.486% | 4.973% | 0.050 s | 19.667 MB | 21.367 MB | 24.992 MB | 26.660 MB | n/a MB | n/a MB |
| python3 | 14662 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 1.978% | 1.978% | 0.020 s | 21.553 MB | 21.680 MB | 26.520 MB | 26.680 MB | n/a MB | n/a MB |
| python3 | 14669 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.867 MB | 22.867 MB | 214.234 MB | 214.234 MB | n/a MB | n/a MB |
| python3 | 14677 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 65.891 MB | 65.891 MB | 69.543 MB | 69.543 MB | n/a MB | n/a MB |
| python3 | 14681 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.609 MB | 18.609 MB | 24.191 MB | 24.191 MB | n/a MB | n/a MB |
| python3 | 14714 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 1.986% | 3.972% | 0.040 s | 19.780 MB | 21.293 MB | 24.986 MB | 26.656 MB | n/a MB | n/a MB |
| python3 | 14728 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 43.906 MB | 43.906 MB | 1911.180 MB | 1911.180 MB | n/a MB | n/a MB |
| bash | 14727 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.832 MB | 2.832 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 14735 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.641 MB | 2.641 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14736 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.527 MB | 9.527 MB | 14.070 MB | 14.070 MB | n/a MB | n/a MB |
| python3 | 14761 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.254 MB | 21.254 MB | 26.664 MB | 26.664 MB | n/a MB | n/a MB |
| python3 | 14770 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 35.430 MB | 35.430 MB | 228.676 MB | 228.676 MB | n/a MB | n/a MB |
| python3 | 14804 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.477 MB | 13.477 MB | 207.180 MB | 207.180 MB | n/a MB | n/a MB |
| bash | 14798 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.641 MB | 2.641 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14816 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.742 MB | 22.742 MB | 217.844 MB | 217.844 MB | n/a MB | n/a MB |
| bash | 14815 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.930 MB | 2.930 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 14840 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14841 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 21.574 MB | 21.574 MB | 26.727 MB | 26.727 MB | n/a MB | n/a MB |
| tr | 14842 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.102 MB | 1.102 MB | 2.465 MB | 2.465 MB | n/a MB | n/a MB |
| bash | 14905 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| tr | 14907 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.465 MB | 2.465 MB | n/a MB | n/a MB |
| python3 | 14906 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 21.512 MB | 21.512 MB | 26.727 MB | 26.727 MB | n/a MB | n/a MB |
| python3 | 14946 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.734 MB | 17.734 MB | 23.941 MB | 23.941 MB | n/a MB | n/a MB |
| bash | 14945 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.773 MB | 2.773 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| tail | 14957 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python3 | 14956 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 9.925% | 9.925% | 0.100 s | 14.910 MB | 21.566 MB | 19.854 MB | 26.668 MB | n/a MB | n/a MB |
| bash | 14955 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.668 MB | 2.668 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 14974 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.773 MB | 2.773 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 14975 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.988 MB | 20.988 MB | 212.000 MB | 212.000 MB | n/a MB | n/a MB |
| python3 | 14992 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.445 MB | 21.445 MB | 26.609 MB | 26.609 MB | n/a MB | n/a MB |
| python3 | 14997 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 35.191 MB | 35.191 MB | 228.535 MB | 228.535 MB | n/a MB | n/a MB |
| bash | 14996 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.828 MB | 2.828 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 15007 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.926 MB | 2.926 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 15008 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.996 MB | 21.996 MB | 213.770 MB | 213.770 MB | n/a MB | n/a MB |
| python3 | 15017 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.414 MB | 21.414 MB | 26.688 MB | 26.688 MB | n/a MB | n/a MB |
| tail | 15018 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.148 MB | 1.148 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 15016 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.949 MB | 2.949 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 15031 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 114.059 MB | 114.059 MB | 350.215 MB | 350.215 MB | n/a MB | n/a MB |
| python3 | 15045 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.512 MB | 13.512 MB | 207.203 MB | 207.203 MB | n/a MB | n/a MB |
| bash | 15044 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.012 MB | 3.012 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 15151 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.371 MB | 13.371 MB | 207.277 MB | 207.277 MB | n/a MB | n/a MB |
| python3 | 15162 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.227 MB | 21.227 MB | 26.652 MB | 26.652 MB | n/a MB | n/a MB |
| python3 | 15198 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.691 MB | 21.691 MB | 213.680 MB | 213.680 MB | n/a MB | n/a MB |
| bash | 15197 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.766 MB | 2.766 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| docker | 15293 |  | 3 | 0.000% | 0.000% | 0.000 s | 29.926 MB | 29.926 MB | 1843.512 MB | 1843.512 MB | 0.000000 MB | 0.000000 MB |
| docker | 15343 |  | 1 | n/a% | n/a% | n/a s | 31.082 MB | 31.082 MB | 1843.512 MB | 1843.512 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.093% | 100.000% | 11802.161 MB | 12136.000 MB | 29.394 W | 73.299 W | 33091.476 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-opencode_0000_0000 | 54.592% | 194.422% | 613.830 s | 1491.291 MB | 1642.434 MB | 471.917969 MB | 279.691406 MB | 24.462224 MB | 0.491752 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 13530 | 1126.682 | interrupted |
| harness:retire | -1 | 0.314 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1126.677 | n/a | n/a | 471.918 | 1126677.177 | 1126677.177 | 1126677.177 |
| sync:result_wait | 1/1 | 0 | 0 | 1126.676 | 0.000 | 1126.676 | 471.918 | 1126676.304 | 1126676.304 | 1126676.304 |
| engine:execute | 1/1 | 0 | 0 | 1126.676 | 2.119 | 1124.557 | 471.918 | 1126675.651 | 1126675.651 | 1126675.651 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1118.073 | 0.006 | 1118.066 | 404.442 | 1118072.698 | 1118072.698 | 1118072.698 |
| harness:await_cli | 1/1 | 0 | 0 | 1097.772 | n/a | n/a | 317.775 | 1097772.427 | 1097772.427 | 1097772.427 |
| llm:attempt | 136/136 | 11 | 0 | 859.106 | 16.211 | 842.890 | 10.100 | 6316.953 | 4741.099 | 15323.067 |
| tool:bash | 111/111 | 0 | 0 | 191.906 | n/a | n/a | 303.823 | 1728.885 | 392.323 | 2589.575 |
| harness:startup_ready | 1/1 | 0 | 0 | 16.480 | n/a | n/a | 56.503 | 16480.428 | 16480.428 | 16480.428 |
| run:container_call | 13/13 | 0 | 0 | 4.163 | 0.003 | 4.161 | 0.599 | 320.260 | 35.869 | 1498.345 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.082 | 0.954 | 3.128 | 66.162 | 4082.338 | 4082.338 | 4082.338 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.082 | 0.954 | 3.128 | 66.156 | 4082.090 | 4082.090 | 4082.090 |
| teardown:commit | 1/1 | 0 | 0 | 3.724 | 0.005 | 3.720 | 0.002 | 3724.407 | 3724.407 | 3724.407 |
| sandbox:commit | 1/1 | 0 | 0 | 3.392 | 0.003 | 3.389 | 0.002 | 3391.740 | 3391.740 | 3391.740 |
| checkpoint.total | 1/1 | 0 | 0 | 3.392 | 0.003 | 3.389 | 0.002 | 3391.576 | 3391.576 | 3391.576 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 3.391 | 0.002 | 3.389 | 0.002 | 3391.412 | 3391.412 | 3391.412 |
| syscall:sendto | 797/797 | 0 | 0 | 1.885 | n/a | n/a | 0.450 | 2.365 | 1.859 | 5.031 |
| harness:submit | 1/1 | 0 | 0 | 1.212 | n/a | n/a | 0.012 | 1211.934 | 1211.934 | 1211.934 |
| syscall:connect | 478/478 | 0 | 0 | 1.200 | n/a | n/a | 0.979 | 2.509 | 2.035 | 4.874 |
| syscall:execve | 365/365 | 0 | 0 | 0.785 | n/a | n/a | 0.512 | 2.150 | 1.461 | 3.395 |
| sandbox:create | 1/1 | 0 | 0 | 0.444 | 0.257 | 0.187 | 0.000 | 444.122 | 444.122 | 444.122 |
| sandbox:start | 1/1 | 0 | 0 | 0.370 | 0.002 | 0.368 | 0.000 | 370.311 | 370.311 | 370.311 |
| runtime.container_create | 1/1 | 0 | 0 | 0.370 | 0.002 | 0.368 | 0.000 | 370.167 | 370.167 | 370.167 |
| sandbox:stop | 1/1 | 0 | 0 | 0.332 | 0.002 | 0.331 | 0.000 | 332.236 | 332.236 | 332.236 |
| tool:write | 10/10 | 0 | 0 | 0.265 | n/a | n/a | 0.000 | 26.523 | 18.830 | 50.227 |
| agency:services_close | 1/1 | 0 | 0 | 0.189 | 0.002 | 0.188 | 0.001 | 189.267 | 189.267 | 189.267 |
| agency:services_start | 1/1 | 0 | 0 | 0.076 | 0.042 | 0.034 | 0.000 | 75.714 | 75.714 | 75.714 |
| run:detect | 1/1 | 0 | 0 | 0.065 | 0.001 | 0.065 | 0.000 | 65.391 | 65.391 | 65.391 |
| tool:edit | 2/2 | 0 | 0 | 0.065 | n/a | n/a | 0.000 | 32.555 | 32.555 | 37.326 |
| tool:read | 1/1 | 0 | 0 | 0.058 | n/a | n/a | 0.000 | 58.299 | 58.299 | 58.299 |
| harness:snapshot | 1/1 | 0 | 0 | 0.056 | n/a | n/a | 0.000 | 56.432 | 56.432 | 56.432 |
| harness:launch | 1/1 | 0 | 0 | 0.050 | n/a | n/a | 0.009 | 49.663 | 49.663 | 49.663 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.007 | 0.040 | 0.000 | 47.561 | 47.561 | 47.561 |
| syscall:bind | 7/7 | 0 | 0 | 0.022 | n/a | n/a | 0.103 | 3.209 | 2.562 | 5.401 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.007 | 0.007 | 0.000 | 0.000 | 6.797 | 6.797 | 6.797 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.270 | 1.270 | 1.270 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.081 | 0.082 | 0.115 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.183 | 0.183 | 0.183 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.053 | 0.053 | 0.053 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1118 | 0.407 | 0.021 | 122.880 | 122.880 | 4.574359 CPU seconds | n/a |
| GPU 0 memory | MB | 1119 | 11802.161 | 11670.000 | 12136.000 | 11830.000 | n/a | n/a |
| GPU 0 power | W | 1119 | 29.394 | 27.818 | 73.299 | 28.157 | n/a | 33091.476 J |
| GPU 0 proc / 13383-1003275 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 memory | MB | 1119 | 3209.912 | 3118.000 | 3526.000 | 3220.000 | n/a | n/a |
| GPU 0 proc / 13383-1003275 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 estimated power | W | 877 | 1.165 | 0.000 | 51.520 | 0.000 | n/a | n/a |
| GPU 0 proc / 13383-1003275 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 utilization | percent | 877 | 0.458 | 0.000 | 43.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 13423-1005358 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 memory | MB | 1119 | 8110.248 | 8070.000 | 8128.000 | 8128.000 | n/a | n/a |
| GPU 0 proc / 13423-1005358 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 estimated power | W | 226 | 6.136 | 0.000 | 72.566 | 0.000 | n/a | n/a |
| GPU 0 proc / 13423-1005358 / sandbox / ~ / device / GPU-13160344-88b1-f103-f059-fd8175c29af8 utilization | percent | 226 | 8.173 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1119 | 11320.161 | 11188.000 | 11654.000 | 11348.000 | n/a | n/a |
| GPU 0 utilization | percent | 1119 | 2.093 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1119 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1118 | 0.848 | 0.100 | 28.427 | 5.703 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1118 | 15.147 | 5.721 | 50.761 | 37.859 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1118 | 0.451 | 0.000 | 102.341 | 2.442 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1118 | 0.526 | 0.000 | 91.136 | 12.744 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1118 | 0.359 | 0.000 | 54.325 | 4.716 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1118 | 0.374 | 0.000 | 55.698 | 4.941 | n/a | n/a |
| host mem_total_mb | MB | 1119 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1119 | 7767.092 | 6942.930 | 8460.980 | 7424.047 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1118 | 0.001 | 0.000 | 1.509 | 0.011 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1118 | 0.001 | 0.000 | 1.614 | 0.013 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1118 | 0.035 | 0.000 | 11.026 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1118 | 0.035 | 0.000 | 0.490 | 0.000 | n/a | n/a |
| Agency harness — python -m lsbench (PID 13383) CPU | percent | 1118 | 4.224 | 0.000 | 102.009 | 0.000 | 47.680000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 13383) io read MB/s | MB/s | 1118 | 0.002 | 0.000 | 0.420 | 0.000 | 1.855469 MB | n/a |
| Agency harness — python -m lsbench (PID 13383) io write MB/s | MB/s | 1118 | 0.240 | 0.016 | 9.055 | 0.023 | 270.011719 MB | n/a |
| Agency harness — python -m lsbench (PID 13383) rss_mb | MB | 1119 | 3034.159 | 2573.816 | 3684.949 | 3390.676 | n/a | n/a |
| Agency harness — python -m lsbench (PID 13383) main thread run-queue wait | percent | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 13383) vms_mb | MB | 1119 | 15847.162 | 14179.859 | 17349.980 | 16649.504 | n/a | n/a |
| Python — vllm (PID 13388) CPU | percent | 1118 | 0.166 | 0.000 | 5.959 | 0.000 | 1.870000 CPU seconds | n/a |
| Python — vllm (PID 13388) io read MB/s | MB/s | 1118 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 13388) io write MB/s | MB/s | 1118 | 0.000 | 0.000 | 0.004 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 13388) rss_mb | MB | 1119 | 1803.683 | 1803.078 | 1803.953 | 1803.953 | n/a | n/a |
| Python — vllm (PID 13388) main thread run-queue wait | percent | 1118 | 0.004 | 0.000 | 0.527 | 0.000 | 0.045237 run-queue seconds | n/a |
| Python — vllm (PID 13388) vms_mb | MB | 1119 | 11023.687 | 10971.699 | 11044.719 | 11044.719 | n/a | n/a |
| Python — python -c (PID 13422) CPU | percent | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 13422) io read MB/s | MB/s | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 13422) io write MB/s | MB/s | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 13422) rss_mb | MB | 1119 | 12.176 | 12.176 | 12.176 | 12.176 | n/a | n/a |
| Python — python -c (PID 13422) main thread run-queue wait | percent | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 13422) vms_mb | MB | 1119 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 13423) CPU | percent | 1118 | 1.557 | 0.000 | 37.636 | 1.988 | 17.540000 CPU seconds | n/a |
| VLLM::EngineCore (PID 13423) io read MB/s | MB/s | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 13423) io write MB/s | MB/s | 1118 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 13423) rss_mb | MB | 1119 | 2321.961 | 2321.961 | 2321.961 | 2321.961 | n/a | n/a |
| VLLM::EngineCore (PID 13423) main thread run-queue wait | percent | 1118 | 0.001 | 0.000 | 0.229 | 0.000 | 0.015472 run-queue seconds | n/a |
| VLLM::EngineCore (PID 13423) vms_mb | MB | 1119 | 21204.207 | 21204.207 | 21204.207 | 21204.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 13642) CPU | percent | 1117 | 0.002 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 13642) rss_mb | MB | 1118 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 13642) main thread run-queue wait | percent | 1117 | 0.002 | 0.000 | 1.930 | 0.000 | 0.025671 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 13642) vms_mb | MB | 1118 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 13674) CPU | percent | 1117 | 0.002 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 13674) rss_mb | MB | 1118 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 13674) main thread run-queue wait | percent | 1117 | 0.000 | 0.000 | 0.119 | 0.000 | 0.002693 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 13674) vms_mb | MB | 1118 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| docker exec (PID 13743) rss_mb | MB | 1 | 30.664 | 30.664 | 30.664 | 30.664 | n/a | n/a |
| docker exec (PID 13743) vms_mb | MB | 1 | 1843.266 | 1843.266 | 1843.266 | 1843.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — runc (PID 13766) CPU | percent | 1117 | 35.694 | 0.000 | 100.465 | 0.000 | 401.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — runc (PID 13766) rss_mb | MB | 1118 | 111.483 | 2.965 | 127.516 | 127.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — runc (PID 13766) main thread run-queue wait | percent | 1117 | 0.000 | 0.000 | 0.006 | 0.000 | 0.000118 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — runc (PID 13766) vms_mb | MB | 1118 | 898.303 | 4.262 | 1601.203 | 904.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 13772) CPU | percent | 1 | 70.614 | 70.614 | 70.614 | 70.614 | 0.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 13772) rss_mb | MB | 2 | 66.363 | 49.281 | 83.445 | 83.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 13772) main thread run-queue wait | percent | 1 | 0.019 | 0.019 | 0.019 | 0.019 | 0.000191 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 13772) vms_mb | MB | 2 | 77.566 | 57.137 | 97.996 | 97.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 13780) rss_mb | MB | 1 | 48.441 | 48.441 | 48.441 | 48.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 13780) vms_mb | MB | 1 | 6431.648 | 6431.648 | 6431.648 | 6431.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 13793) CPU | percent | 1107 | 6.441 | 0.884 | 127.312 | 2.985 | 71.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 13793) rss_mb | MB | 1108 | 768.396 | 34.445 | 941.574 | 807.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 13793) main thread run-queue wait | percent | 1107 | 0.340 | 0.000 | 24.335 | 0.006 | 3.789735 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 13793) vms_mb | MB | 1108 | 16594.704 | 6358.133 | 16830.266 | 16830.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13855) rss_mb | MB | 1 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13855) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 13857) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 13857) vms_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13858) rss_mb | MB | 1 | 1.129 | 1.129 | 1.129 | 1.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13858) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13859) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13859) vms_mb | MB | 1 | 3.410 | 3.410 | 3.410 | 3.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13865) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13865) rss_mb | MB | 3 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13865) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13865) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13867) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13867) rss_mb | MB | 3 | 1.775 | 1.691 | 1.816 | 1.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13867) main thread run-queue wait | percent | 2 | 0.004 | 0.000 | 0.008 | 0.000 | 0.000080 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13867) vms_mb | MB | 3 | 3.391 | 3.391 | 3.391 | 3.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13876) rss_mb | MB | 1 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13876) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 13878) rss_mb | MB | 1 | 1.535 | 1.535 | 1.535 | 1.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 13878) vms_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13879) rss_mb | MB | 1 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13879) vms_mb | MB | 1 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13880) rss_mb | MB | 1 | 1.191 | 1.191 | 1.191 | 1.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13880) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13884) rss_mb | MB | 1 | 1.773 | 1.773 | 1.773 | 1.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13884) vms_mb | MB | 1 | 3.434 | 3.434 | 3.434 | 3.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13890) rss_mb | MB | 1 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13890) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — ls (PID 13894) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — ls (PID 13894) vms_mb | MB | 1 | 0.516 | 0.516 | 0.516 | 0.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13925) rss_mb | MB | 1 | 2.523 | 2.523 | 2.523 | 2.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13925) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — find (PID 13926) rss_mb | MB | 1 | 2.367 | 2.367 | 2.367 | 2.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — find (PID 13926) vms_mb | MB | 1 | 4.527 | 4.527 | 4.527 | 4.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 13927) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 13927) vms_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13928) rss_mb | MB | 1 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13928) vms_mb | MB | 1 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13929) rss_mb | MB | 1 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13929) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 13931) rss_mb | MB | 1 | 0.980 | 0.980 | 0.980 | 0.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 13931) vms_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13937) rss_mb | MB | 1 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13937) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13938) rss_mb | MB | 1 | 7.555 | 7.555 | 7.555 | 7.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13938) vms_mb | MB | 1 | 9.211 | 9.211 | 9.211 | 9.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13939) rss_mb | MB | 1 | 1.129 | 1.129 | 1.129 | 1.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13939) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13945) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13945) rss_mb | MB | 119 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13945) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 13945) vms_mb | MB | 119 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13946) CPU | percent | 118 | 97.637 | 20.873 | 101.425 | 100.401 | 115.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13946) rss_mb | MB | 119 | 14.513 | 2.195 | 14.617 | 14.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13946) main thread run-queue wait | percent | 118 | 0.147 | 0.001 | 11.063 | 0.009 | 0.174250 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13946) vms_mb | MB | 119 | 16.192 | 3.773 | 16.297 | 16.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13947) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13947) rss_mb | MB | 119 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13947) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 13947) vms_mb | MB | 119 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13948) CPU | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13948) rss_mb | MB | 119 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13948) main thread run-queue wait | percent | 118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 13948) vms_mb | MB | 119 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14019) rss_mb | MB | 1 | 2.625 | 2.625 | 2.625 | 2.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14019) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — find (PID 14024) rss_mb | MB | 1 | 2.227 | 2.227 | 2.227 | 2.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — find (PID 14024) vms_mb | MB | 1 | 4.270 | 4.270 | 4.270 | 4.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14025) rss_mb | MB | 1 | 1.613 | 1.613 | 1.613 | 1.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14025) vms_mb | MB | 1 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 14026) rss_mb | MB | 1 | 1.094 | 1.094 | 1.094 | 1.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 14026) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14055) rss_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14055) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 14061) rss_mb | MB | 1 | 1.398 | 1.398 | 1.398 | 1.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — xargs (PID 14061) vms_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14062) rss_mb | MB | 1 | 0.148 | 0.148 | 0.148 | 0.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14062) vms_mb | MB | 1 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14084) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14084) rss_mb | MB | 2 | 10.457 | 10.457 | 10.457 | 10.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14084) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14084) vms_mb | MB | 2 | 13.758 | 13.758 | 13.758 | 13.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14287) rss_mb | MB | 1 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14287) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 14288) rss_mb | MB | 1 | 20.855 | 20.855 | 20.855 | 20.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 14288) vms_mb | MB | 1 | 25.402 | 25.402 | 25.402 | 25.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14321) rss_mb | MB | 1 | 21.309 | 21.309 | 21.309 | 21.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14321) vms_mb | MB | 1 | 26.652 | 26.652 | 26.652 | 26.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14344) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14344) rss_mb | MB | 2 | 2.555 | 2.555 | 2.555 | 2.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14344) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14344) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14345) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14345) rss_mb | MB | 2 | 21.738 | 21.738 | 21.738 | 21.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14345) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14345) vms_mb | MB | 2 | 26.797 | 26.797 | 26.797 | 26.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 14346) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 14346) rss_mb | MB | 2 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 14346) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 14346) vms_mb | MB | 2 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14371) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14371) rss_mb | MB | 5 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14371) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14371) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14372) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14372) rss_mb | MB | 5 | 21.234 | 21.234 | 21.234 | 21.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14372) main thread run-queue wait | percent | 4 | 0.014 | 0.000 | 0.058 | 0.000 | 0.000582 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14372) vms_mb | MB | 5 | 26.633 | 26.633 | 26.633 | 26.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14374) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14374) rss_mb | MB | 5 | 1.723 | 1.723 | 1.723 | 1.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14374) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14374) vms_mb | MB | 5 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14395) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14395) rss_mb | MB | 5 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14395) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14395) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14396) CPU | percent | 4 | 1.490 | 0.000 | 5.959 | 0.000 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14396) rss_mb | MB | 5 | 20.782 | 17.066 | 21.711 | 21.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14396) main thread run-queue wait | percent | 4 | 0.040 | 0.000 | 0.158 | 0.000 | 0.001592 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_tasks.py (PID 14396) vms_mb | MB | 5 | 25.665 | 21.793 | 26.633 | 26.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14397) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14397) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14397) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14397) vms_mb | MB | 5 | 2.465 | 2.465 | 2.465 | 2.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14398) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14398) rss_mb | MB | 5 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14398) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14398) vms_mb | MB | 5 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14436) rss_mb | MB | 1 | 10.430 | 10.430 | 10.430 | 10.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14436) vms_mb | MB | 1 | 13.598 | 13.598 | 13.598 | 13.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14504) rss_mb | MB | 1 | 21.320 | 21.320 | 21.320 | 21.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14504) vms_mb | MB | 1 | 26.656 | 26.656 | 26.656 | 26.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14512) rss_mb | MB | 1 | 21.395 | 21.395 | 21.395 | 21.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14512) vms_mb | MB | 1 | 26.566 | 26.566 | 26.566 | 26.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14585) rss_mb | MB | 1 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14585) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — pip (PID 14588) rss_mb | MB | 1 | 21.359 | 21.359 | 21.359 | 21.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — pip (PID 14588) vms_mb | MB | 1 | 26.184 | 26.184 | 26.184 | 26.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14589) rss_mb | MB | 1 | 1.691 | 1.691 | 1.691 | 1.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 14589) vms_mb | MB | 1 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14593) rss_mb | MB | 1 | 9.797 | 9.797 | 9.797 | 9.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14593) vms_mb | MB | 1 | 19.750 | 19.750 | 19.750 | 19.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14597) rss_mb | MB | 1 | 21.273 | 21.273 | 21.273 | 21.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14597) vms_mb | MB | 1 | 26.656 | 26.656 | 26.656 | 26.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14604) rss_mb | MB | 1 | 21.133 | 21.133 | 21.133 | 21.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14604) vms_mb | MB | 1 | 26.660 | 26.660 | 26.660 | 26.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14609) rss_mb | MB | 1 | 8.930 | 8.930 | 8.930 | 8.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14609) vms_mb | MB | 1 | 13.191 | 13.191 | 13.191 | 13.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14619) rss_mb | MB | 1 | 21.594 | 21.594 | 21.594 | 21.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14619) vms_mb | MB | 1 | 26.781 | 26.781 | 26.781 | 26.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14623) rss_mb | MB | 1 | 2.582 | 2.582 | 2.582 | 2.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14623) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14654) CPU | percent | 2 | 2.486 | 0.000 | 4.973 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14654) rss_mb | MB | 3 | 19.667 | 16.266 | 21.367 | 21.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14654) main thread run-queue wait | percent | 2 | 0.093 | 0.000 | 0.187 | 0.000 | 0.001880 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14654) vms_mb | MB | 3 | 24.992 | 21.656 | 26.660 | 26.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14662) CPU | percent | 1 | 1.978 | 1.978 | 1.978 | 1.978 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14662) rss_mb | MB | 2 | 21.553 | 21.426 | 21.680 | 21.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14662) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14662) vms_mb | MB | 2 | 26.520 | 26.359 | 26.680 | 26.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14669) rss_mb | MB | 1 | 22.867 | 22.867 | 22.867 | 22.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14669) vms_mb | MB | 1 | 214.234 | 214.234 | 214.234 | 214.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14677) rss_mb | MB | 1 | 65.891 | 65.891 | 65.891 | 65.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14677) vms_mb | MB | 1 | 69.543 | 69.543 | 69.543 | 69.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14681) rss_mb | MB | 1 | 18.609 | 18.609 | 18.609 | 18.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14681) vms_mb | MB | 1 | 24.191 | 24.191 | 24.191 | 24.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14714) CPU | percent | 2 | 1.986 | 0.000 | 3.972 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14714) rss_mb | MB | 3 | 19.780 | 16.754 | 21.293 | 21.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14714) main thread run-queue wait | percent | 2 | 0.008 | 0.000 | 0.016 | 0.000 | 0.000161 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14714) vms_mb | MB | 3 | 24.986 | 21.645 | 26.656 | 26.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14727) rss_mb | MB | 1 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14727) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14728) rss_mb | MB | 1 | 43.906 | 43.906 | 43.906 | 43.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14728) vms_mb | MB | 1 | 1911.180 | 1911.180 | 1911.180 | 1911.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14735) rss_mb | MB | 1 | 2.641 | 2.641 | 2.641 | 2.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14735) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14736) rss_mb | MB | 1 | 9.527 | 9.527 | 9.527 | 9.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14736) vms_mb | MB | 1 | 14.070 | 14.070 | 14.070 | 14.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14761) rss_mb | MB | 1 | 21.254 | 21.254 | 21.254 | 21.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14761) vms_mb | MB | 1 | 26.664 | 26.664 | 26.664 | 26.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14770) rss_mb | MB | 1 | 35.430 | 35.430 | 35.430 | 35.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14770) vms_mb | MB | 1 | 228.676 | 228.676 | 228.676 | 228.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14798) rss_mb | MB | 1 | 2.641 | 2.641 | 2.641 | 2.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14798) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14804) rss_mb | MB | 1 | 13.477 | 13.477 | 13.477 | 13.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14804) vms_mb | MB | 1 | 207.180 | 207.180 | 207.180 | 207.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14815) rss_mb | MB | 1 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14815) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14816) rss_mb | MB | 1 | 22.742 | 22.742 | 22.742 | 22.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14816) vms_mb | MB | 1 | 217.844 | 217.844 | 217.844 | 217.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14840) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14840) rss_mb | MB | 2 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14840) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14840) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_anchored.py (PID 14841) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_anchored.py (PID 14841) rss_mb | MB | 2 | 21.574 | 21.574 | 21.574 | 21.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_anchored.py (PID 14841) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_anchored.py (PID 14841) vms_mb | MB | 2 | 26.727 | 26.727 | 26.727 | 26.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14842) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14842) rss_mb | MB | 2 | 1.102 | 1.102 | 1.102 | 1.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14842) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14842) vms_mb | MB | 2 | 2.465 | 2.465 | 2.465 | 2.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14905) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14905) rss_mb | MB | 3 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14905) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14905) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_anchored.py (PID 14906) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_anchored.py (PID 14906) rss_mb | MB | 3 | 21.512 | 21.512 | 21.512 | 21.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_anchored.py (PID 14906) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_anchored.py (PID 14906) vms_mb | MB | 3 | 26.727 | 26.727 | 26.727 | 26.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14907) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14907) rss_mb | MB | 3 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14907) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tr (PID 14907) vms_mb | MB | 3 | 2.465 | 2.465 | 2.465 | 2.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14945) rss_mb | MB | 1 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14945) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14946) rss_mb | MB | 1 | 17.734 | 17.734 | 17.734 | 17.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14946) vms_mb | MB | 1 | 23.941 | 23.941 | 23.941 | 23.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14955) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14955) rss_mb | MB | 2 | 2.668 | 2.668 | 2.668 | 2.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14955) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14955) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14956) CPU | percent | 1 | 9.925 | 9.925 | 9.925 | 9.925 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14956) rss_mb | MB | 2 | 14.910 | 8.254 | 21.566 | 21.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14956) main thread run-queue wait | percent | 1 | 0.067 | 0.067 | 0.067 | 0.067 | 0.000673 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14956) vms_mb | MB | 2 | 19.854 | 13.039 | 26.668 | 26.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 14957) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 14957) rss_mb | MB | 2 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 14957) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 14957) vms_mb | MB | 2 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14974) rss_mb | MB | 1 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14974) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14975) rss_mb | MB | 1 | 20.988 | 20.988 | 20.988 | 20.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14975) vms_mb | MB | 1 | 212.000 | 212.000 | 212.000 | 212.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14992) rss_mb | MB | 1 | 21.445 | 21.445 | 21.445 | 21.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 14992) vms_mb | MB | 1 | 26.609 | 26.609 | 26.609 | 26.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14996) rss_mb | MB | 1 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 14996) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14997) rss_mb | MB | 1 | 35.191 | 35.191 | 35.191 | 35.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 14997) vms_mb | MB | 1 | 228.535 | 228.535 | 228.535 | 228.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 15007) rss_mb | MB | 1 | 2.926 | 2.926 | 2.926 | 2.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 15007) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 15008) rss_mb | MB | 1 | 21.996 | 21.996 | 21.996 | 21.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 15008) vms_mb | MB | 1 | 213.770 | 213.770 | 213.770 | 213.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 15016) rss_mb | MB | 1 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 15016) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 15017) rss_mb | MB | 1 | 21.414 | 21.414 | 21.414 | 21.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 15017) vms_mb | MB | 1 | 26.688 | 26.688 | 26.688 | 26.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 15018) rss_mb | MB | 1 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 15018) vms_mb | MB | 1 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 15031) rss_mb | MB | 1 | 114.059 | 114.059 | 114.059 | 114.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 15031) vms_mb | MB | 1 | 350.215 | 350.215 | 350.215 | 350.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 15044) rss_mb | MB | 1 | 3.012 | 3.012 | 3.012 | 3.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 15044) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 15045) rss_mb | MB | 1 | 13.512 | 13.512 | 13.512 | 13.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — Python (PID 15045) vms_mb | MB | 1 | 207.203 | 207.203 | 207.203 | 207.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 15151) rss_mb | MB | 1 | 13.371 | 13.371 | 13.371 | 13.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 15151) vms_mb | MB | 1 | 207.277 | 207.277 | 207.277 | 207.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 15162) rss_mb | MB | 1 | 21.227 | 21.227 | 21.227 | 21.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 15162) vms_mb | MB | 1 | 26.652 | 26.652 | 26.652 | 26.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 15197) rss_mb | MB | 1 | 2.766 | 2.766 | 2.766 | 2.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 15197) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 15198) rss_mb | MB | 1 | 21.691 | 21.691 | 21.691 | 21.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 15198) vms_mb | MB | 1 | 213.680 | 213.680 | 213.680 | 213.680 | n/a | n/a |
| docker commit (PID 15293) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 15293) io read MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 15293) io write MB/s | MB/s | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 15293) rss_mb | MB | 3 | 29.926 | 29.926 | 29.926 | 29.926 | n/a | n/a |
| docker commit (PID 15293) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 15293) vms_mb | MB | 3 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| docker stop (PID 15343) rss_mb | MB | 1 | 31.082 | 31.082 | 31.082 | 31.082 | n/a | n/a |
| docker stop (PID 15343) vms_mb | MB | 1 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4616) CPU | percent | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4616) io read MB/s | MB/s | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4616) io write MB/s | MB/s | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4616) rss_mb | MB | 1119 | 3.391 | 3.391 | 3.391 | 3.391 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4616) main thread run-queue wait | percent | 1118 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4616) vms_mb | MB | 1119 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 CPU | percent | 1117 | 54.592 | 0.000 | 194.422 | 0.000 | 613.830347 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1117 | 0.508 | 0.000 | 18.962 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1117 | 0.648 | 0.000 | 27.499 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_full_pct | percent of wall time stalled | 1117 | 0.328 | 0.000 | 54.827 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_some_pct | percent of wall time stalled | 1117 | 0.337 | 0.000 | 55.956 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io read MB/s | MB/s | 1117 | 0.420 | 0.000 | 102.341 | 0.000 | 471.917969 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io write MB/s | MB/s | 1117 | 0.249 | 0.000 | 91.136 | 0.000 | 279.691406 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory | MB | 1118 | 1491.291 | 7.566 | 1642.434 | 646.555 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1117 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1117 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net rx MB/s | MB/s | 1117 | 0.022 | 0.000 | 10.691 | 0.000 | 24.462224 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net tx MB/s | MB/s | 1117 | 0.000 | 0.000 | 0.068 | 0.000 | 0.491752 MB | n/a |
| workload total CPU | percent | 1118 | 5.956 | 1.456 | 101.944 | 9.068 | 67.231362 CPU seconds | n/a |
| workload total memory | MB | 1119 | 7975.675 | 7538.379 | 8626.453 | 8295.270 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
