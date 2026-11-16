# agprof summary

- Duration: **1170.138 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **159 calls**, 111 succeeded, 48 failed, 0 interrupted, n/a reported retries, 993.999 s total wait
- Tools: **109/109 completed**, 3 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **121970** at 1.976 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1166006.946 / 1166006.946 ms |
| LLM latency p50 / p95 | 6117.112 / 11122.822 ms |
| LLM TTFT p50 / p95 | 4818.183 / 10162.961 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 159 total, 111 succeeded, 48 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- dsh: {"automatic_functions": "host_only", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "unavailable", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 62/62 | 60 | 2 | 0 | n/a | n/a |
| mcp__agency__attention | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 2/2 | 1 | 1 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 14/14 | 14 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 8/8 | 8 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 4/4 | 4 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 6/6 | 6 | 0 | 0 | n/a | n/a |
| todo_write | 4/4 | 4 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 8.133% | 179.417% | 95.184 s | 5680.946 MB | 6191.402 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 3738 |  | 1162 | 5.461% | 177.797% | 63.930 s | 2978.038 MB | 3508.164 MB | 15947.510 MB | 16818.305 MB | 4.507812 MB | 181.226562 MB |
| docker-init | 4121 | sandbox_agent_lsb-dsh_0000_0000 | 1158 | 0.003% | 0.994% | 0.030 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 4245 | sandbox_agent_lsb-dsh_0000_0000 | 1158 | 8.675% | 98.339% | 101.080 s | 111.568 MB | 122.598 MB | 964.196 MB | 976.750 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 3783 |  | 1162 | 2.419% | 40.653% | 28.300 s | 2321.293 MB | 2321.387 MB | 21204.418 MB | 21204.418 MB | 0.000000 MB | 0.003906 MB |
| tail | 4152 | sandbox_agent_lsb-dsh_0000_0000 | 1158 | 0.003% | 0.995% | 0.030 s | 1.574 MB | 1.574 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 3782 |  | 1162 | 0.000% | 0.000% | 0.000 s | 12.332 MB | 12.332 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| lsb_guard.sh | 3743 |  | 1162 | 0.001% | 0.994% | 0.010 s | 3.430 MB | 3.430 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3746 |  | 8 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4251 | sandbox_agent_lsb-dsh_0000_0000 | 2 | 58.251% | 58.251% | 0.590 s | 35.824 MB | 52.906 MB | 42.486 MB | 60.988 MB | n/a MB | n/a MB |
| vllm | 3748 |  | 1162 | 0.215% | 5.943% | 2.510 s | 1803.653 MB | 1803.711 MB | 11045.590 MB | 11046.582 MB | 0.003906 MB | 0.054688 MB |
| lsb_grid_worker | 3729 |  | 1162 | 0.000% | 0.000% | 0.000 s | 3.430 MB | 3.430 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| MainThread | 4275 | sandbox_agent_lsb-dsh_0000_0000 | 1131 | 1.315% | 113.175% | 14.970 s | 401.252 MB | 472.609 MB | 10217.563 MB | 10349.418 MB | n/a MB | n/a MB |
| sleep | 4297 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4472 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 4588 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.699 MB | 2.699 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4589 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.410 MB | 6.410 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| sleep | 4674 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4827 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4890 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4942 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4981 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5017 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5057 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5107 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5121 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.113 MB | 9.113 MB | 13.160 MB | 13.160 MB | n/a MB | n/a MB |
| bash | 5120 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.602 MB | 2.602 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5134 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.738 MB | 16.738 MB | 209.117 MB | 209.117 MB | n/a MB | n/a MB |
| bash | 5132 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.645 MB | 2.645 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 5149 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5176 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 5216 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.609 MB | 2.609 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5219 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.598 MB | 23.598 MB | 215.578 MB | 215.578 MB | n/a MB | n/a MB |
| sleep | 5227 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5280 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5337 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 5338 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.598 MB | 2.598 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5339 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2381.922 MB | 2381.922 MB | 2640.797 MB | 2640.797 MB | n/a MB | n/a MB |
| bash | 5362 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.766 MB | 2.766 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5377 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.172 MB | 9.172 MB | 13.309 MB | 13.309 MB | n/a MB | n/a MB |
| bash | 5375 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.918 MB | 2.918 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 5386 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| date | 5404 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.812 MB | 0.812 MB | 2.387 MB | 2.387 MB | n/a MB | n/a MB |
| bash | 5403 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.715 MB | 2.715 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 5424 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5437 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 246.758 MB | 246.758 MB | 701.023 MB | 701.023 MB | n/a MB | n/a MB |
| sleep | 5461 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5471 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 954.285 MB | 954.285 MB | 1672.656 MB | 1672.656 MB | n/a MB | n/a MB |
| bash | 5470 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.805 MB | 2.805 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 5541 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5553 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.145 MB | 17.145 MB | 209.605 MB | 209.605 MB | n/a MB | n/a MB |
| bash | 5552 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.746 MB | 2.746 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5594 | sandbox_agent_lsb-dsh_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.918 MB | 17.918 MB | 210.047 MB | 210.047 MB | n/a MB | n/a MB |
| docker | 5650 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.594 MB | 30.594 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5666 |  | 21 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 3.454% | 100.000% | 11838.429 MB | 12386.000 MB | 28.652 W | 72.925 W | 33489.148 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-dsh_0000_0000 | 11.399% | 187.135% | 132.849 s | 526.355 MB | 2949.680 MB | 16.097656 MB | 97.058594 MB | 0.001045 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4011 | 1170.074 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1166.007 | n/a | n/a | 16.098 | 1166006.946 | 1166006.946 | 1166006.946 |
| engine:execute | 1/1 | 0 | 0 | 1166.005 | 1.962 | 1164.043 | 16.098 | 1166005.311 | 1166005.311 | 1166005.311 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1139.368 | 0.002 | 1139.366 | 3.719 | 1139368.136 | 1139368.136 | 1139368.136 |
| llm:attempt | 159/159 | 48 | 0 | 993.999 | 16.232 | 977.763 | 0.369 | 6251.567 | 6117.112 | 11122.822 |
| tool:mcp__agency__generate | 14/14 | 0 | 0 | 34.126 | n/a | n/a | 0.000 | 2437.550 | 2072.218 | 4679.936 |
| run:container_call | 13/13 | 0 | 0 | 22.515 | 0.002 | 22.513 | 0.000 | 1731.920 | 35.995 | 8859.605 |
| teardown:commit | 1/1 | 0 | 0 | 22.082 | 0.004 | 22.078 | 0.000 | 22082.097 | 22082.097 | 22082.097 |
| sandbox:commit | 1/1 | 0 | 0 | 21.895 | 0.002 | 21.893 | 0.000 | 21895.186 | 21895.186 | 21895.186 |
| checkpoint.total | 1/1 | 0 | 0 | 21.895 | 0.002 | 21.893 | 0.000 | 21895.046 | 21895.046 | 21895.046 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 21.895 | 0.002 | 21.893 | 0.000 | 21894.863 | 21894.863 | 21894.863 |
| tool:mcp__agency__logit_lens | 8/8 | 0 | 0 | 17.301 | n/a | n/a | 0.000 | 2162.567 | 2248.252 | 3844.741 |
| tool:bash | 62/62 | 2 | 0 | 15.674 | n/a | n/a | 0.170 | 252.802 | 104.516 | 852.785 |
| tool:mcp__agency__token_stats | 4/4 | 0 | 0 | 6.586 | n/a | n/a | 0.000 | 1646.605 | 1353.337 | 2785.540 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.903 | 0.898 | 3.005 | 12.323 | 3903.366 | 3903.366 | 3903.366 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.903 | 0.898 | 3.005 | 12.323 | 3903.069 | 3903.069 | 3903.069 |
| tool:mcp__agency__inspect_module_inputs | 3/3 | 0 | 0 | 2.389 | n/a | n/a | 0.000 | 796.413 | 1055.472 | 1067.057 |
| tool:mcp__agency__trace | 6/6 | 0 | 0 | 0.947 | n/a | n/a | 0.000 | 157.787 | 147.357 | 289.147 |
| syscall:execve | 206/206 | 0 | 0 | 0.687 | n/a | n/a | 0.014 | 3.335 | 1.195 | 9.055 |
| syscall:connect | 366/366 | 0 | 0 | 0.640 | n/a | n/a | 0.002 | 1.749 | 1.518 | 2.708 |
| tool:mcp__agency__inspect | 2/2 | 0 | 0 | 0.559 | n/a | n/a | 0.000 | 279.437 | 279.437 | 291.238 |
| sandbox:start | 1/1 | 0 | 0 | 0.366 | 0.002 | 0.364 | 0.000 | 366.476 | 366.476 | 366.476 |
| runtime.container_create | 1/1 | 0 | 0 | 0.366 | 0.002 | 0.364 | 0.000 | 366.321 | 366.321 | 366.321 |
| sandbox:create | 1/1 | 0 | 0 | 0.363 | 0.261 | 0.102 | 0.000 | 363.336 | 363.336 | 363.336 |
| tool:mcp__agency__attention | 2/2 | 0 | 0 | 0.275 | n/a | n/a | 0.000 | 137.362 | 137.362 | 156.195 |
| tool:mcp__agency__attribution | 2/2 | 1 | 0 | 0.243 | n/a | n/a | 0.000 | 121.270 | 121.270 | 136.978 |
| sandbox:stop | 1/1 | 0 | 0 | 0.187 | 0.001 | 0.185 | 0.000 | 186.640 | 186.640 | 186.640 |
| agency:services_close | 1/1 | 0 | 0 | 0.123 | 0.001 | 0.122 | 0.000 | 122.949 | 122.949 | 122.949 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.119 | n/a | n/a | 0.000 | 119.043 | 119.043 | 119.043 |
| agency:services_start | 1/1 | 0 | 0 | 0.072 | 0.041 | 0.031 | 0.000 | 72.270 | 72.270 | 72.270 |
| run:detect | 1/1 | 0 | 0 | 0.060 | 0.001 | 0.059 | 0.000 | 59.641 | 59.641 | 59.641 |
| tool:todo_write | 4/4 | 0 | 0 | 0.058 | n/a | n/a | 0.000 | 14.504 | 14.499 | 16.515 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.008 | 0.041 | 0.000 | 48.318 | 48.318 | 48.318 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.043 | n/a | n/a | 0.000 | 42.558 | 42.558 | 42.558 |
| syscall:sendto | 2/2 | 0 | 0 | 0.004 | n/a | n/a | 0.001 | 1.953 | 1.953 | 2.338 |
| syscall:bind | 1/1 | 0 | 0 | 0.002 | n/a | n/a | 0.000 | 2.116 | 2.116 | 2.116 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.552 | 1.552 | 1.552 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.220 | 1.220 | 1.220 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.073 | 0.071 | 0.115 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.175 | 0.175 | 0.175 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.062 | 0.062 | 0.062 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1161 | 0.659 | 0.016 | 50.414 | 0.095 | 7.694317 CPU seconds | n/a |
| GPU 0 memory | MB | 1162 | 11838.429 | 11670.000 | 12386.000 | 11824.000 | n/a | n/a |
| GPU 0 power | W | 1162 | 28.652 | 26.964 | 72.925 | 26.993 | n/a | 33489.148 J |
| GPU 0 proc / 3738-115814 / sandbox / ~ / device / GPU-7aab9b37-c575-bde2-f3e6-7e47477b360e memory | MB | 1162 | 3228.091 | 3118.000 | 3804.000 | 3206.000 | n/a | n/a |
| GPU 0 proc / 3738-115814 / sandbox / ~ / device / GPU-7aab9b37-c575-bde2-f3e6-7e47477b360e estimated power | W | 780 | 1.898 | 0.000 | 63.059 | 0.000 | n/a | n/a |
| GPU 0 proc / 3738-115814 / sandbox / ~ / device / GPU-7aab9b37-c575-bde2-f3e6-7e47477b360e utilization | percent | 780 | 0.754 | 0.000 | 49.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 3783-118238 / sandbox / ~ / device / GPU-7aab9b37-c575-bde2-f3e6-7e47477b360e memory | MB | 1162 | 8128.337 | 8070.000 | 8136.000 | 8136.000 | n/a | n/a |
| GPU 0 proc / 3783-118238 / sandbox / ~ / device / GPU-7aab9b37-c575-bde2-f3e6-7e47477b360e estimated power | W | 368 | 5.849 | 0.000 | 72.196 | 0.000 | n/a | n/a |
| GPU 0 proc / 3783-118238 / sandbox / ~ / device / GPU-7aab9b37-c575-bde2-f3e6-7e47477b360e utilization | percent | 368 | 7.859 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1162 | 11356.429 | 11188.000 | 11904.000 | 11342.000 | n/a | n/a |
| GPU 0 utilization | percent | 1162 | 3.454 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1162 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1161 | 0.762 | 0.029 | 29.239 | 0.284 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1161 | 4.828 | 0.251 | 47.607 | 0.500 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1161 | 1.434 | 0.000 | 212.121 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1161 | 0.308 | 0.000 | 47.565 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1161 | 0.627 | 0.000 | 54.723 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1161 | 0.631 | 0.000 | 54.913 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1162 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1162 | 7324.467 | 6688.848 | 9855.891 | 7232.594 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1161 | 0.000 | 0.000 | 0.031 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1161 | 0.000 | 0.000 | 0.031 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1161 | 0.017 | 0.000 | 0.253 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1161 | 0.034 | 0.000 | 0.902 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3729) CPU | percent | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 3729) io read MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3729) io write MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3729) rss_mb | MB | 1162 | 3.430 | 3.430 | 3.430 | 3.430 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3729) main thread run-queue wait | percent | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 3729) vms_mb | MB | 1162 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3738) CPU | percent | 1161 | 5.461 | 0.000 | 177.797 | 0.995 | 63.930000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 3738) io read MB/s | MB/s | 1161 | 0.004 | 0.000 | 1.724 | 0.000 | 4.507812 MB | n/a |
| Agency harness — python -m lsbench (PID 3738) io write MB/s | MB/s | 1161 | 0.155 | 0.015 | 3.556 | 0.023 | 181.226562 MB | n/a |
| Agency harness — python -m lsbench (PID 3738) rss_mb | MB | 1162 | 2978.038 | 2342.062 | 3508.164 | 3280.598 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3738) main thread run-queue wait | percent | 1161 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000007 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 3738) vms_mb | MB | 1162 | 15947.510 | 13795.871 | 16818.305 | 16260.211 | n/a | n/a |
| bash lsb_guard.sh (PID 3743) CPU | percent | 1161 | 0.001 | 0.000 | 0.994 | 0.000 | 0.010000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 3743) io read MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3743) io write MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3743) rss_mb | MB | 1162 | 3.430 | 3.430 | 3.430 | 3.430 | n/a | n/a |
| bash lsb_guard.sh (PID 3743) main thread run-queue wait | percent | 1161 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000011 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 3743) vms_mb | MB | 1162 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sleep (PID 3746) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3746) io read MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3746) io write MB/s | MB/s | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3746) rss_mb | MB | 8 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3746) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3746) vms_mb | MB | 8 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — vllm (PID 3748) CPU | percent | 1161 | 0.215 | 0.000 | 5.943 | 0.000 | 2.510000 CPU seconds | n/a |
| Python — vllm (PID 3748) io read MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 3748) io write MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.008 | 0.000 | 0.054688 MB | n/a |
| Python — vllm (PID 3748) rss_mb | MB | 1162 | 1803.653 | 1802.961 | 1803.711 | 1803.711 | n/a | n/a |
| Python — vllm (PID 3748) main thread run-queue wait | percent | 1161 | 0.001 | 0.000 | 0.167 | 0.000 | 0.017454 run-queue seconds | n/a |
| Python — vllm (PID 3748) vms_mb | MB | 1162 | 11045.590 | 10974.562 | 11046.582 | 11046.582 | n/a | n/a |
| Python — python -c (PID 3782) CPU | percent | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 3782) io read MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3782) io write MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3782) rss_mb | MB | 1162 | 12.332 | 12.332 | 12.332 | 12.332 | n/a | n/a |
| Python — python -c (PID 3782) main thread run-queue wait | percent | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 3782) vms_mb | MB | 1162 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 3783) CPU | percent | 1161 | 2.419 | 0.000 | 40.653 | 2.985 | 28.300000 CPU seconds | n/a |
| VLLM::EngineCore (PID 3783) io read MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 3783) io write MB/s | MB/s | 1161 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 3783) rss_mb | MB | 1162 | 2321.293 | 2321.262 | 2321.387 | 2321.387 | n/a | n/a |
| VLLM::EngineCore (PID 3783) main thread run-queue wait | percent | 1161 | 0.001 | 0.000 | 0.668 | 0.000 | 0.013537 run-queue seconds | n/a |
| VLLM::EngineCore (PID 3783) vms_mb | MB | 1162 | 21204.418 | 21204.418 | 21204.418 | 21204.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 4121) CPU | percent | 1157 | 0.003 | 0.000 | 0.994 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 4121) rss_mb | MB | 1158 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 4121) main thread run-queue wait | percent | 1157 | 0.005 | 0.000 | 4.874 | 0.000 | 0.053223 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — docker-init (PID 4121) vms_mb | MB | 1158 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 4152) CPU | percent | 1157 | 0.003 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 4152) rss_mb | MB | 1158 | 1.574 | 1.574 | 1.574 | 1.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 4152) main thread run-queue wait | percent | 1157 | 0.004 | 0.000 | 4.329 | 0.000 | 0.044911 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — tail (PID 4152) vms_mb | MB | 1158 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4245) CPU | percent | 1157 | 8.675 | 0.000 | 98.339 | 0.000 | 101.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4245) rss_mb | MB | 1158 | 111.568 | 3.008 | 122.598 | 120.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4245) main thread run-queue wait | percent | 1157 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000113 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4245) vms_mb | MB | 1158 | 964.196 | 4.262 | 976.750 | 975.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4251) CPU | percent | 1 | 58.251 | 58.251 | 58.251 | 58.251 | 0.590000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4251) rss_mb | MB | 2 | 35.824 | 18.742 | 52.906 | 52.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4251) main thread run-queue wait | percent | 1 | 0.026 | 0.026 | 0.026 | 0.026 | 0.000268 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python -c (PID 4251) vms_mb | MB | 2 | 42.486 | 23.984 | 60.988 | 60.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 4275) CPU | percent | 1130 | 1.315 | 0.000 | 113.175 | 0.994 | 14.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 4275) rss_mb | MB | 1131 | 401.252 | 93.020 | 472.609 | 408.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 4275) main thread run-queue wait | percent | 1130 | 0.168 | 0.000 | 12.041 | 0.004 | 1.912552 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — deepseek-harness-sdk-runtime-linux-x64 (PID 4275) vms_mb | MB | 1131 | 10217.563 | 1490.711 | 10349.418 | 10235.809 | n/a | n/a |
| sleep (PID 4297) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4297) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4297) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4297) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4297) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4297) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4472) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4472) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4472) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4472) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4472) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4472) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4588) rss_mb | MB | 1 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 4588) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 4589) rss_mb | MB | 1 | 6.410 | 6.410 | 6.410 | 6.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 4589) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sleep (PID 4674) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4674) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4674) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4674) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4674) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4674) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4827) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4827) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4827) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4827) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4827) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4827) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4890) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4890) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4890) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4890) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4890) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4890) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4942) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4942) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4942) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4942) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4942) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4942) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4981) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4981) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4981) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4981) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4981) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4981) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5017) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5017) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5017) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5017) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5017) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5017) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5057) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5057) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5057) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5057) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5057) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5057) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5107) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5107) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5107) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5107) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5107) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5107) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5120) rss_mb | MB | 1 | 2.602 | 2.602 | 2.602 | 2.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5120) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5121) rss_mb | MB | 1 | 9.113 | 9.113 | 9.113 | 9.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5121) vms_mb | MB | 1 | 13.160 | 13.160 | 13.160 | 13.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5132) rss_mb | MB | 1 | 2.645 | 2.645 | 2.645 | 2.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5132) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5134) rss_mb | MB | 1 | 16.738 | 16.738 | 16.738 | 16.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5134) vms_mb | MB | 1 | 209.117 | 209.117 | 209.117 | 209.117 | n/a | n/a |
| sleep (PID 5149) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5149) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5149) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5149) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5149) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5149) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5176) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5176) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5176) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5176) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5176) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5176) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5216) rss_mb | MB | 1 | 2.609 | 2.609 | 2.609 | 2.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5216) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5219) rss_mb | MB | 1 | 23.598 | 23.598 | 23.598 | 23.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5219) vms_mb | MB | 1 | 215.578 | 215.578 | 215.578 | 215.578 | n/a | n/a |
| sleep (PID 5227) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5227) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5227) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5227) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5227) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5227) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5280) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5280) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5280) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5280) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5280) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5280) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5337) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5337) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5337) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5337) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5337) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5337) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5338) rss_mb | MB | 1 | 2.598 | 2.598 | 2.598 | 2.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5338) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5339) rss_mb | MB | 1 | 2381.922 | 2381.922 | 2381.922 | 2381.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5339) vms_mb | MB | 1 | 2640.797 | 2640.797 | 2640.797 | 2640.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5362) rss_mb | MB | 1 | 2.766 | 2.766 | 2.766 | 2.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5362) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5375) rss_mb | MB | 1 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5375) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5377) rss_mb | MB | 1 | 9.172 | 9.172 | 9.172 | 9.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5377) vms_mb | MB | 1 | 13.309 | 13.309 | 13.309 | 13.309 | n/a | n/a |
| sleep (PID 5386) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5386) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5386) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5386) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5386) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5386) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash gen (PID 5403) rss_mb | MB | 1 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash gen (PID 5403) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — date (PID 5404) rss_mb | MB | 1 | 0.812 | 0.812 | 0.812 | 0.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — date (PID 5404) vms_mb | MB | 1 | 2.387 | 2.387 | 2.387 | 2.387 | n/a | n/a |
| sleep (PID 5424) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5424) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5424) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5424) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5424) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5424) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — build_adapter.py (PID 5437) rss_mb | MB | 1 | 246.758 | 246.758 | 246.758 | 246.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — build_adapter.py (PID 5437) vms_mb | MB | 1 | 701.023 | 701.023 | 701.023 | 701.023 | n/a | n/a |
| sleep (PID 5461) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5461) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5461) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5461) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5461) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5461) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5470) rss_mb | MB | 1 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5470) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5471) rss_mb | MB | 1 | 954.285 | 954.285 | 954.285 | 954.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5471) vms_mb | MB | 1 | 1672.656 | 1672.656 | 1672.656 | 1672.656 | n/a | n/a |
| sleep (PID 5541) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5541) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5541) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5541) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5541) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5541) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5552) rss_mb | MB | 1 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — bash (PID 5552) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5553) rss_mb | MB | 1 | 17.145 | 17.145 | 17.145 | 17.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — python stdin (PID 5553) vms_mb | MB | 1 | 209.605 | 209.605 | 209.605 | 209.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — build_adapter.py (PID 5594) rss_mb | MB | 1 | 17.918 | 17.918 | 17.918 | 17.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-dsh_0000_0000 — build_adapter.py (PID 5594) vms_mb | MB | 1 | 210.047 | 210.047 | 210.047 | 210.047 | n/a | n/a |
| docker commit (PID 5650) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 5650) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5650) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 5650) rss_mb | MB | 22 | 30.594 | 30.594 | 30.594 | 30.594 | n/a | n/a |
| docker commit (PID 5650) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 5650) vms_mb | MB | 22 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| sleep (PID 5666) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5666) io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5666) io write MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5666) rss_mb | MB | 21 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5666) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5666) vms_mb | MB | 21 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 CPU | percent | 1157 | 11.399 | 0.000 | 187.135 | 0.000 | 132.848880 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1157 | 0.476 | 0.000 | 22.654 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1157 | 0.583 | 0.000 | 28.865 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io_psi_full_pct | percent of wall time stalled | 1157 | 0.046 | 0.000 | 20.951 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io_psi_some_pct | percent of wall time stalled | 1157 | 0.046 | 0.000 | 20.951 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io read MB/s | MB/s | 1157 | 0.014 | 0.000 | 7.370 | 0.000 | 16.097656 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 io write MB/s | MB/s | 1157 | 0.083 | 0.000 | 46.576 | 0.000 | 97.058594 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory | MB | 1158 | 526.355 | 12.684 | 2949.680 | 123.145 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1157 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1157 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 net rx MB/s | MB/s | 1157 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001045 MB | n/a |
| sandbox sandbox_agent_lsb-dsh_0000_0000 net tx MB/s | MB/s | 1157 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 1161 | 8.133 | 1.532 | 179.417 | 2.335 | 95.184072 CPU seconds | n/a |
| workload total memory | MB | 1162 | 5680.946 | 5084.227 | 6191.402 | 6001.723 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
