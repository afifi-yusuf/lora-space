# agprof summary

- Duration: **540.088 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.002 runs/s**
- LLM: **23 calls**, 23 succeeded, 0 failed, 0 interrupted, n/a reported retries, 410.950 s total wait
- Tools: **84/84 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **49417** at 1.99 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 514485.489 / 514485.489 ms |
| LLM latency p50 / p95 | 15875.763 / 37770.749 ms |
| LLM TTFT p50 / p95 | 5369.966 / 6520.738 ms |
| LLM input / output tokens | 1897362 / 69861 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 23 total, 23 succeeded, 0 failed, 0 interrupted |
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
| Bash | 16/16 | 16 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 8/8 | 8 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 34/34 | 34 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 14/14 | 14 | 0 | 0 | n/a | n/a |
| update_plan | 5/5 | 5 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 8.976% | 101.655% | 48.444 s | 12887.669 MB | 14091.980 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| tail | 5416 | sandbox_agent_lsb-codex_0000_0000 | 511 | 0.000% | 0.000% | 0.000 s | 1.543 MB | 1.543 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 5520 | sandbox_agent_lsb-codex_0000_0000 | 511 | 29.545% | 93.981% | 151.580 s | 111.381 MB | 119.770 MB | 962.484 MB | 974.684 MB | n/a MB | n/a MB |
| python | 5117 |  | 537 | 0.000% | 0.000% | 0.000 s | 12.207 MB | 12.207 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 5067 |  | 537 | 0.157% | 9.933% | 0.850 s | 1795.629 MB | 1795.660 MB | 12001.729 MB | 12004.312 MB | 0.000000 MB | 0.039062 MB |
| lsb_grid_worker | 2203 |  | 537 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 5058 |  | 537 | 7.186% | 101.191% | 38.790 s | 2964.863 MB | 3881.004 MB | 16494.553 MB | 17578.219 MB | 0.101562 MB | 2822.714844 MB |
| docker-init | 5377 | sandbox_agent_lsb-codex_0000_0000 | 511 | 0.002% | 0.995% | 0.010 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 5118 |  | 537 | 1.598% | 40.724% | 8.620 s | 2326.909 MB | 2326.996 MB | 21892.727 MB | 21892.727 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5526 | sandbox_agent_lsb-codex_0000_0000 | 2 | 98.913% | 98.913% | 1.000 s | 60.027 MB | 83.789 MB | 70.373 MB | 98.051 MB | n/a MB | n/a MB |
| codex | 5543 | sandbox_agent_lsb-codex_0000_0000 | 504 | 2.614% | 15.910% | 13.230 s | 139.664 MB | 151.691 MB | 406.654 MB | 524.211 MB | n/a MB | n/a MB |
| git-remote-http | 5592 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.176 MB | 19.176 MB | 100.590 MB | 100.590 MB | n/a MB | n/a MB |
| git | 5590 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.848 MB | 3.848 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 5588 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.344 MB | 4.344 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 5620 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.750 MB | 5.750 MB | 8.285 MB | 8.285 MB | n/a MB | n/a MB |
| python3 | 5664 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.199 MB | 21.199 MB | 25.836 MB | 25.836 MB | n/a MB | n/a MB |
| python3 | 5708 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.836 MB | 21.836 MB | 27.074 MB | 27.074 MB | n/a MB | n/a MB |
| python3 | 5765 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.809 MB | 5.809 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| python3 | 5773 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.125 MB | 19.125 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python3 | 5786 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.402 MB | 19.402 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| python3 | 5877 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.180 MB | 22.180 MB | 27.059 MB | 27.059 MB | n/a MB | n/a MB |
| python3 | 5897 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.004 MB | 19.004 MB | 24.387 MB | 24.387 MB | n/a MB | n/a MB |
| python3 | 5934 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.855 MB | 14.855 MB | 20.000 MB | 20.000 MB | n/a MB | n/a MB |
| python3 | 5951 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.078 MB | 8.078 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python3 | 6119 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.625 MB | 7.625 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| bash | 6121 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.891 MB | 2.891 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 6125 | sandbox_agent_lsb-codex_0000_0000 | 3 | 178.497% | 179.965% | 3.590 s | 1072.233 MB | 1088.148 MB | 1452.527 MB | 1468.527 MB | n/a MB | n/a MB |
| python3 | 6172 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.352 MB | 15.352 MB | 20.109 MB | 20.109 MB | n/a MB | n/a MB |
| python | 6211 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.426 MB | 21.426 MB | 133.184 MB | 133.184 MB | n/a MB | n/a MB |
| python3 | 6229 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.496 MB | 20.496 MB | 24.934 MB | 24.934 MB | n/a MB | n/a MB |
| python | 6253 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.828 MB | 21.828 MB | 133.586 MB | 133.586 MB | n/a MB | n/a MB |
| bash | 6245 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.129 MB | 3.129 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 6260 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.020 MB | 17.020 MB | 22.145 MB | 22.145 MB | n/a MB | n/a MB |
| python | 6340 | sandbox_agent_lsb-codex_0000_0000 | 4 | 157.652% | 167.107% | 4.760 s | 173.767 MB | 239.977 MB | 513.932 MB | 593.484 MB | n/a MB | n/a MB |
| python | 6370 | sandbox_agent_lsb-codex_0000_0000 | 5 | 145.820% | 162.950% | 5.870 s | 130.135 MB | 196.293 MB | 475.177 MB | 523.805 MB | n/a MB | n/a MB |
| python3 | 6383 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.176 MB | 21.176 MB | 25.453 MB | 25.453 MB | n/a MB | n/a MB |
| python3 | 6388 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.680 MB | 10.680 MB | 15.031 MB | 15.031 MB | n/a MB | n/a MB |
| python3 | 6391 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.465 MB | 13.465 MB | 19.820 MB | 19.820 MB | n/a MB | n/a MB |
| bash | 6424 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.840 MB | 2.840 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 6432 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.008 MB | 11.008 MB | 15.215 MB | 15.215 MB | n/a MB | n/a MB |
| python3 | 6444 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.133 MB | 22.133 MB | 26.984 MB | 26.984 MB | n/a MB | n/a MB |
| python3 | 6450 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.605 MB | 7.605 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| python | 6453 | sandbox_agent_lsb-codex_0000_0000 | 5 | 155.113% | 160.146% | 6.240 s | 152.748 MB | 341.215 MB | 488.077 MB | 687.609 MB | n/a MB | n/a MB |
| python3 | 6475 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.203 MB | 16.203 MB | 20.715 MB | 20.715 MB | n/a MB | n/a MB |
| python3 | 6491 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.297 MB | 10.297 MB | 13.785 MB | 13.785 MB | n/a MB | n/a MB |
| python | 6501 | sandbox_agent_lsb-codex_0000_0000 | 3 | 169.460% | 172.022% | 3.430 s | 207.562 MB | 340.895 MB | 545.576 MB | 665.016 MB | n/a MB | n/a MB |
| bash | 6493 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.023 MB | 3.023 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python3 | 6516 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.184 MB | 22.184 MB | 27.059 MB | 27.059 MB | n/a MB | n/a MB |
| python3 | 6538 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.602 MB | 7.602 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| docker | 6573 |  | 2 | 0.000% | 0.000% | 0.000 s | 29.078 MB | 29.078 MB | 1907.004 MB | 1907.004 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2.099% | 100.000% | 11847.404 MB | 11896.000 MB | 29.849 W | 52.695 W | 16091.772 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 42.211% | 206.194% | 216.624 s | 426.368 MB | 1492.832 MB | 135.324219 MB | 156.601562 MB | 24.967742 MB | 0.771499 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 5249 | 540.036 | interrupted |
| harness:retire | -1 | 0.380 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 514.485 | n/a | n/a | 135.324 | 514485.489 | 514485.489 | 514485.489 |
| engine:execute | 1/1 | 0 | 0 | 514.484 | 1.340 | 513.142 | 135.324 | 514483.786 | 514483.786 | 514483.786 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 508.795 | 0.005 | 508.790 | 123.273 | 508795.114 | 508795.114 | 508795.114 |
| harness:await_cli | 1/1 | 0 | 0 | 504.366 | n/a | n/a | 17.799 | 504365.562 | 504365.562 | 504365.562 |
| llm:attempt | 23/23 | 0 | 0 | 410.950 | 3.074 | 407.876 | 7.385 | 17867.399 | 15875.763 | 37770.749 |
| tool:Bash | 16/16 | 0 | 0 | 26.537 | n/a | n/a | 2.670 | 1658.581 | 532.788 | 5267.099 |
| tool:mcp__agency__trace | 14/14 | 0 | 0 | 24.597 | n/a | n/a | 0.039 | 1756.963 | 1490.876 | 4196.636 |
| tool:mcp__agency__patch | 34/34 | 0 | 0 | 12.730 | n/a | n/a | 0.000 | 374.411 | 372.169 | 391.878 |
| tool:mcp__agency__generate | 8/8 | 0 | 0 | 4.290 | n/a | n/a | 0.406 | 536.214 | 505.398 | 740.162 |
| tool:mcp__agency__logit_lens | 2/2 | 0 | 0 | 3.235 | n/a | n/a | 0.000 | 1617.441 | 1617.441 | 2163.234 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.021 | 0.686 | 2.335 | 11.243 | 3021.340 | 3021.340 | 3021.340 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.021 | 0.686 | 2.335 | 11.240 | 3020.993 | 3020.993 | 3020.993 |
| run:container_call | 13/13 | 0 | 0 | 2.432 | 0.002 | 2.429 | 0.000 | 187.070 | 33.520 | 825.970 |
| teardown:commit | 1/1 | 0 | 0 | 2.063 | 0.004 | 2.059 | 0.000 | 2063.092 | 2063.092 | 2063.092 |
| sandbox:commit | 1/1 | 0 | 0 | 1.882 | 0.002 | 1.880 | 0.000 | 1882.297 | 1882.297 | 1882.297 |
| checkpoint.total | 1/1 | 0 | 0 | 1.882 | 0.002 | 1.880 | 0.000 | 1882.135 | 1882.135 | 1882.135 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.882 | 0.002 | 1.880 | 0.000 | 1881.984 | 1881.984 | 1881.984 |
| syscall:connect | 656/656 | 0 | 0 | 1.473 | n/a | n/a | 2.947 | 2.245 | 2.034 | 3.825 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.223 | n/a | n/a | 59.190 | 1223.183 | 1223.183 | 1223.183 |
| harness:submit | 1/1 | 0 | 0 | 1.210 | n/a | n/a | 28.705 | 1210.351 | 1210.351 | 1210.351 |
| syscall:execve | 678/678 | 0 | 0 | 0.959 | n/a | n/a | 3.449 | 1.414 | 1.251 | 2.486 |
| syscall:sendto | 424/424 | 0 | 0 | 0.932 | n/a | n/a | 2.847 | 2.199 | 1.996 | 3.791 |
| tool:update_plan | 5/5 | 0 | 0 | 0.869 | n/a | n/a | 1.565 | 173.806 | 166.495 | 199.491 |
| harness:snapshot | 1/1 | 0 | 0 | 0.761 | n/a | n/a | 0.130 | 761.421 | 761.421 | 761.421 |
| tool:mcp__agency__attention | 2/2 | 0 | 0 | 0.540 | n/a | n/a | 0.000 | 270.067 | 270.067 | 289.104 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.345 | n/a | n/a | 0.000 | 345.054 | 345.054 | 345.054 |
| sandbox:create | 1/1 | 0 | 0 | 0.343 | 0.252 | 0.091 | 0.000 | 343.020 | 343.020 | 343.020 |
| sandbox:start | 1/1 | 0 | 0 | 0.304 | 0.002 | 0.301 | 0.000 | 303.607 | 303.607 | 303.607 |
| runtime.container_create | 1/1 | 0 | 0 | 0.303 | 0.002 | 0.301 | 0.000 | 303.474 | 303.474 | 303.474 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 0.273 | n/a | n/a | 0.000 | 272.710 | 272.710 | 272.710 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.203 | n/a | n/a | 0.000 | 202.831 | 202.831 | 202.831 |
| sandbox:stop | 1/1 | 0 | 0 | 0.181 | 0.002 | 0.179 | 0.000 | 180.567 | 180.567 | 180.567 |
| agency:services_close | 1/1 | 0 | 0 | 0.123 | 0.000 | 0.123 | 0.000 | 122.881 | 122.881 | 122.881 |
| agency:services_start | 1/1 | 0 | 0 | 0.072 | 0.041 | 0.031 | 0.000 | 72.256 | 72.256 | 72.256 |
| run:detect | 1/1 | 0 | 0 | 0.049 | 0.001 | 0.048 | 0.000 | 48.606 | 48.606 | 48.606 |
| harness:launch | 1/1 | 0 | 0 | 0.044 | n/a | n/a | 2.333 | 43.535 | 43.535 | 43.535 |
| agent:create | 1/1 | 0 | 0 | 0.037 | 0.008 | 0.029 | 0.000 | 36.516 | 36.516 | 36.516 |
| syscall:bind | 4/4 | 0 | 0 | 0.008 | n/a | n/a | 0.286 | 1.900 | 1.532 | 3.216 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.000 | 4.150 | 4.150 | 4.150 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.462 | 1.462 | 1.462 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.075 | 0.087 | 0.099 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.229 | 0.229 | 0.229 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.081 | 0.081 | 0.081 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 536 | 0.642 | 0.038 | 171.412 | 0.067 | 3.462469 CPU seconds | n/a |
| GPU 0 memory | MB | 537 | 11847.404 | 11670.000 | 11896.000 | 11864.000 | n/a | n/a |
| GPU 0 power | W | 537 | 29.849 | 28.293 | 52.695 | 28.328 | n/a | 16091.772 J |
| GPU 0 proc / 5058-402729 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb memory | MB | 537 | 3203.929 | 3118.000 | 3246.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 5058-402729 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb estimated power | W | 427 | 4.098 | 0.000 | 51.574 | 0.000 | n/a | n/a |
| GPU 0 proc / 5058-402729 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb utilization | percent | 427 | 2.136 | 0.000 | 46.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 5118-404508 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb memory | MB | 537 | 8161.475 | 8070.000 | 8168.000 | 8168.000 | n/a | n/a |
| GPU 0 proc / 5118-404508 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb estimated power | W | 110 | 2.345 | 0.000 | 46.877 | 0.000 | n/a | n/a |
| GPU 0 proc / 5118-404508 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb utilization | percent | 110 | 1.536 | 0.000 | 35.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 537 | 11365.404 | 11188.000 | 11414.000 | 11382.000 | n/a | n/a |
| GPU 0 utilization | percent | 537 | 2.099 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 537 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 536 | 1.694 | 0.072 | 75.935 | 0.086 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 536 | 6.110 | 0.000 | 26.568 | 0.250 | n/a | n/a |
| host disk_read_mb_s | MB/s | 536 | 0.255 | 0.000 | 53.594 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 536 | 5.643 | 0.000 | 212.282 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 536 | 0.890 | 0.000 | 70.941 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 536 | 0.896 | 0.000 | 71.064 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 537 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 537 | 7265.665 | 6406.008 | 8468.152 | 7125.547 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 536 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 536 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 536 | 0.057 | 0.000 | 24.620 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 536 | 0.025 | 0.000 | 1.026 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2203) CPU | percent | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2203) io read MB/s | MB/s | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2203) io write MB/s | MB/s | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2203) rss_mb | MB | 537 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2203) main thread run-queue wait | percent | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2203) vms_mb | MB | 537 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 5058) CPU | percent | 536 | 7.186 | 0.000 | 101.191 | 0.996 | 38.790000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 5058) io read MB/s | MB/s | 536 | 0.000 | 0.000 | 0.074 | 0.000 | 0.101562 MB | n/a |
| Agency harness — python -m lsbench (PID 5058) io write MB/s | MB/s | 536 | 5.227 | 0.015 | 369.275 | 0.023 | 2822.714844 MB | n/a |
| Agency harness — python -m lsbench (PID 5058) rss_mb | MB | 537 | 2964.863 | 2091.727 | 3881.004 | 3028.535 | n/a | n/a |
| Agency harness — python -m lsbench (PID 5058) main thread run-queue wait | percent | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 5058) vms_mb | MB | 537 | 16494.553 | 14212.023 | 17578.219 | 16547.727 | n/a | n/a |
| Python — vllm (PID 5067) CPU | percent | 536 | 0.157 | 0.000 | 9.933 | 0.000 | 0.850000 CPU seconds | n/a |
| Python — vllm (PID 5067) io read MB/s | MB/s | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 5067) io write MB/s | MB/s | 536 | 0.000 | 0.000 | 0.008 | 0.000 | 0.039062 MB | n/a |
| Python — vllm (PID 5067) rss_mb | MB | 537 | 1795.629 | 1794.785 | 1795.660 | 1795.660 | n/a | n/a |
| Python — vllm (PID 5067) main thread run-queue wait | percent | 536 | 0.002 | 0.000 | 0.467 | 0.000 | 0.008902 run-queue seconds | n/a |
| Python — vllm (PID 5067) vms_mb | MB | 537 | 12001.729 | 11931.293 | 12004.312 | 12004.312 | n/a | n/a |
| Python — python -c (PID 5117) CPU | percent | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 5117) io read MB/s | MB/s | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 5117) io write MB/s | MB/s | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 5117) rss_mb | MB | 537 | 12.207 | 12.207 | 12.207 | 12.207 | n/a | n/a |
| Python — python -c (PID 5117) main thread run-queue wait | percent | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 5117) vms_mb | MB | 537 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 5118) CPU | percent | 536 | 1.598 | 0.000 | 40.724 | 1.992 | 8.620000 CPU seconds | n/a |
| VLLM::EngineCore (PID 5118) io read MB/s | MB/s | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 5118) io write MB/s | MB/s | 536 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 5118) rss_mb | MB | 537 | 2326.909 | 2326.621 | 2326.996 | 2326.996 | n/a | n/a |
| VLLM::EngineCore (PID 5118) main thread run-queue wait | percent | 536 | 0.000 | 0.000 | 0.003 | 0.000 | 0.000141 run-queue seconds | n/a |
| VLLM::EngineCore (PID 5118) vms_mb | MB | 537 | 21892.727 | 21892.727 | 21892.727 | 21892.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5377) CPU | percent | 510 | 0.002 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5377) rss_mb | MB | 511 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5377) main thread run-queue wait | percent | 510 | 0.013 | 0.000 | 6.750 | 0.000 | 0.067999 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 5377) vms_mb | MB | 511 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5416) CPU | percent | 510 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5416) rss_mb | MB | 511 | 1.543 | 1.543 | 1.543 | 1.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5416) main thread run-queue wait | percent | 510 | 0.013 | 0.000 | 6.522 | 0.000 | 0.068603 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 5416) vms_mb | MB | 511 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5520) CPU | percent | 510 | 29.545 | 0.000 | 93.981 | 0.000 | 151.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5520) rss_mb | MB | 511 | 111.381 | 3.250 | 119.770 | 115.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5520) main thread run-queue wait | percent | 510 | 0.000 | 0.000 | 0.011 | 0.000 | 0.000132 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 5520) vms_mb | MB | 511 | 962.484 | 4.262 | 974.684 | 973.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5526) CPU | percent | 1 | 98.913 | 98.913 | 98.913 | 98.913 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5526) rss_mb | MB | 2 | 60.027 | 36.266 | 83.789 | 83.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5526) main thread run-queue wait | percent | 1 | 0.008 | 0.008 | 0.008 | 0.008 | 0.000084 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 5526) vms_mb | MB | 2 | 70.373 | 42.695 | 98.051 | 98.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5543) CPU | percent | 503 | 2.614 | 0.000 | 15.910 | 1.989 | 13.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5543) rss_mb | MB | 504 | 139.664 | 60.082 | 151.691 | 148.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5543) main thread run-queue wait | percent | 503 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 5543) vms_mb | MB | 504 | 406.654 | 356.367 | 524.211 | 405.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5588) rss_mb | MB | 1 | 4.344 | 4.344 | 4.344 | 4.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 5588) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5590) rss_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 5590) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5592) rss_mb | MB | 1 | 19.176 | 19.176 | 19.176 | 19.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 5592) vms_mb | MB | 1 | 100.590 | 100.590 | 100.590 | 100.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 5620) rss_mb | MB | 1 | 5.750 | 5.750 | 5.750 | 5.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 5620) vms_mb | MB | 1 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5664) rss_mb | MB | 1 | 21.199 | 21.199 | 21.199 | 21.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5664) vms_mb | MB | 1 | 25.836 | 25.836 | 25.836 | 25.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5708) rss_mb | MB | 1 | 21.836 | 21.836 | 21.836 | 21.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5708) vms_mb | MB | 1 | 27.074 | 27.074 | 27.074 | 27.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5765) rss_mb | MB | 1 | 5.809 | 5.809 | 5.809 | 5.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5765) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5773) rss_mb | MB | 1 | 19.125 | 19.125 | 19.125 | 19.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5773) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5786) rss_mb | MB | 1 | 19.402 | 19.402 | 19.402 | 19.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5786) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5877) rss_mb | MB | 1 | 22.180 | 22.180 | 22.180 | 22.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5877) vms_mb | MB | 1 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5897) rss_mb | MB | 1 | 19.004 | 19.004 | 19.004 | 19.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5897) vms_mb | MB | 1 | 24.387 | 24.387 | 24.387 | 24.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5934) rss_mb | MB | 1 | 14.855 | 14.855 | 14.855 | 14.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5934) vms_mb | MB | 1 | 20.000 | 20.000 | 20.000 | 20.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5951) rss_mb | MB | 1 | 8.078 | 8.078 | 8.078 | 8.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 5951) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6119) rss_mb | MB | 1 | 7.625 | 7.625 | 7.625 | 7.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6119) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6121) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6121) rss_mb | MB | 3 | 2.891 | 2.891 | 2.891 | 2.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6121) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6121) vms_mb | MB | 3 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6125) CPU | percent | 2 | 178.497 | 177.029 | 179.965 | 177.029 | 3.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6125) rss_mb | MB | 3 | 1072.233 | 1060.508 | 1088.148 | 1060.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6125) main thread run-queue wait | percent | 2 | 80.577 | 77.996 | 83.157 | 83.157 | 1.620580 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6125) vms_mb | MB | 3 | 1452.527 | 1440.527 | 1468.527 | 1440.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6172) rss_mb | MB | 1 | 15.352 | 15.352 | 15.352 | 15.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6172) vms_mb | MB | 1 | 20.109 | 20.109 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — diagnose.py (PID 6211) rss_mb | MB | 1 | 21.426 | 21.426 | 21.426 | 21.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — diagnose.py (PID 6211) vms_mb | MB | 1 | 133.184 | 133.184 | 133.184 | 133.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6229) rss_mb | MB | 1 | 20.496 | 20.496 | 20.496 | 20.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6229) vms_mb | MB | 1 | 24.934 | 24.934 | 24.934 | 24.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6245) rss_mb | MB | 1 | 3.129 | 3.129 | 3.129 | 3.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6245) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — diagnose.py (PID 6253) rss_mb | MB | 1 | 21.828 | 21.828 | 21.828 | 21.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — diagnose.py (PID 6253) vms_mb | MB | 1 | 133.586 | 133.586 | 133.586 | 133.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6260) rss_mb | MB | 1 | 17.020 | 17.020 | 17.020 | 17.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6260) vms_mb | MB | 1 | 22.145 | 22.145 | 22.145 | 22.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — geometry.py (PID 6340) CPU | percent | 3 | 157.652 | 143.038 | 167.107 | 167.107 | 4.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — geometry.py (PID 6340) rss_mb | MB | 4 | 173.767 | 45.324 | 239.977 | 221.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — geometry.py (PID 6340) main thread run-queue wait | percent | 3 | 31.154 | 28.501 | 33.199 | 33.199 | 0.940643 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — geometry.py (PID 6340) vms_mb | MB | 4 | 513.932 | 346.504 | 593.484 | 574.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 6370) CPU | percent | 4 | 145.820 | 120.173 | 162.950 | 139.281 | 5.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 6370) rss_mb | MB | 5 | 130.135 | 82.496 | 196.293 | 135.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 6370) main thread run-queue wait | percent | 4 | 24.929 | 18.329 | 30.339 | 21.666 | 1.003538 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 6370) vms_mb | MB | 5 | 475.177 | 432.504 | 523.805 | 485.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6383) rss_mb | MB | 1 | 21.176 | 21.176 | 21.176 | 21.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6383) vms_mb | MB | 1 | 25.453 | 25.453 | 25.453 | 25.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6388) rss_mb | MB | 1 | 10.680 | 10.680 | 10.680 | 10.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6388) vms_mb | MB | 1 | 15.031 | 15.031 | 15.031 | 15.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6391) rss_mb | MB | 1 | 13.465 | 13.465 | 13.465 | 13.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6391) vms_mb | MB | 1 | 19.820 | 19.820 | 19.820 | 19.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6424) rss_mb | MB | 1 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6424) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6432) rss_mb | MB | 1 | 11.008 | 11.008 | 11.008 | 11.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6432) vms_mb | MB | 1 | 15.215 | 15.215 | 15.215 | 15.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6444) rss_mb | MB | 1 | 22.133 | 22.133 | 22.133 | 22.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6444) vms_mb | MB | 1 | 26.984 | 26.984 | 26.984 | 26.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6450) rss_mb | MB | 1 | 7.605 | 7.605 | 7.605 | 7.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6450) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 6453) CPU | percent | 4 | 155.113 | 145.185 | 160.146 | 160.146 | 6.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 6453) rss_mb | MB | 5 | 152.748 | 33.152 | 341.215 | 143.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 6453) main thread run-queue wait | percent | 4 | 33.271 | 21.168 | 43.200 | 43.200 | 1.338417 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — construct.py (PID 6453) vms_mb | MB | 5 | 488.077 | 332.445 | 687.609 | 486.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6475) rss_mb | MB | 1 | 16.203 | 16.203 | 16.203 | 16.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6475) vms_mb | MB | 1 | 20.715 | 20.715 | 20.715 | 20.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6491) rss_mb | MB | 1 | 10.297 | 10.297 | 10.297 | 10.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6491) vms_mb | MB | 1 | 13.785 | 13.785 | 13.785 | 13.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6493) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6493) rss_mb | MB | 3 | 3.023 | 3.023 | 3.023 | 3.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6493) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 6493) vms_mb | MB | 3 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6501) CPU | percent | 2 | 169.460 | 166.898 | 172.022 | 166.898 | 3.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6501) rss_mb | MB | 3 | 207.562 | 134.723 | 340.895 | 147.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6501) main thread run-queue wait | percent | 2 | 41.812 | 36.144 | 47.480 | 36.144 | 0.846845 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 6501) vms_mb | MB | 3 | 545.576 | 481.777 | 665.016 | 489.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6516) rss_mb | MB | 1 | 22.184 | 22.184 | 22.184 | 22.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 6516) vms_mb | MB | 1 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — lifecycle_hook.py (PID 6538) rss_mb | MB | 1 | 7.602 | 7.602 | 7.602 | 7.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — lifecycle_hook.py (PID 6538) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| docker commit (PID 6573) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6573) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6573) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6573) rss_mb | MB | 2 | 29.078 | 29.078 | 29.078 | 29.078 | n/a | n/a |
| docker commit (PID 6573) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6573) vms_mb | MB | 2 | 1907.004 | 1907.004 | 1907.004 | 1907.004 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 510 | 42.211 | 0.000 | 206.194 | 0.000 | 216.624258 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 510 | 1.668 | 0.000 | 71.189 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 510 | 1.701 | 0.000 | 75.623 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 510 | 0.058 | 0.000 | 14.626 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 510 | 0.058 | 0.000 | 14.630 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 510 | 0.264 | 0.000 | 53.594 | 0.000 | 135.324219 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 510 | 0.305 | 0.000 | 68.870 | 0.000 | 156.601562 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 511 | 426.368 | 25.809 | 1492.832 | 254.590 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 510 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 510 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 510 | 0.049 | 0.000 | 23.785 | 0.000 | 24.967742 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 510 | 0.002 | 0.000 | 0.313 | 0.000 | 0.771499 MB | n/a |
| workload total CPU | percent | 536 | 8.976 | 1.640 | 101.655 | 2.005 | 48.443930 CPU seconds | n/a |
| workload total memory | MB | 537 | 12887.669 | 11204.961 | 14091.980 | 13475.348 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
