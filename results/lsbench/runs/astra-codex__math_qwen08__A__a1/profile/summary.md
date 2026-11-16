# agprof summary

- Duration: **2364.636 s**
- Runs: **1/1 completed**, 0 succeeded, 1 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **48 calls**, 48 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1171.392 s total wait
- Tools: **43/44 completed**, 0 failed, 1 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **218269** at 1.971 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2364580.111 / 2364580.111 ms |
| LLM latency p50 / p95 | 15758.558 / 73296.978 ms |
| LLM TTFT p50 / p95 | 7244.958 / 22367.730 ms |
| LLM input / output tokens | 3318767 / 45237 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 48 total, 48 succeeded, 0 failed, 0 interrupted |
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
| Bash | 17/17 | 17 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 7/7 | 7 | 0 | 0 | n/a | n/a |
| mcp__agency__get_current_resources | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 4/4 | 4 | 0 | 0 | n/a | n/a |
| mcp__agency__reserve_resource | 0/1 | 0 | 0 | 1 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 5/5 | 5 | 0 | 0 | n/a | n/a |
| update_plan | 5/5 | 5 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 15.513% | 104.763% | 367.627 s | 6278.748 MB | 6623.168 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 9772 |  | 2347 | 1.058% | 5.951% | 25.060 s | 1806.204 MB | 1806.738 MB | 11047.494 MB | 11049.578 MB | 0.003906 MB | 0.128906 MB |
| docker-init | 10027 | sandbox_agent_lsb-codex_0000_0000 | 2347 | 0.002% | 0.995% | 0.050 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| lsb_grid_worker | 4633 |  | 2347 | 0.000% | 0.000% | 0.000 s | 3.422 MB | 3.422 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 9807 |  | 2347 | 0.000% | 0.000% | 0.000 s | 12.184 MB | 12.184 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| bash | 10151 | sandbox_agent_lsb-codex_0000_0000 | 2347 | 24.582% | 101.271% | 581.110 s | 112.188 MB | 118.453 MB | 972.356 MB | 976.199 MB | n/a MB | n/a MB |
| python | 9767 |  | 2347 | 3.945% | 103.502% | 93.520 s | 2735.239 MB | 3010.691 MB | 16063.801 MB | 18218.629 MB | 1.792969 MB | 430.222656 MB |
| tail | 10059 | sandbox_agent_lsb-codex_0000_0000 | 2347 | 0.002% | 0.995% | 0.050 s | 1.434 MB | 1.434 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 9808 |  | 2347 | 10.509% | 45.511% | 249.010 s | 2340.604 MB | 2341.395 MB | 21240.421 MB | 21241.309 MB | 0.000000 MB | 0.011719 MB |
| python3 | 10157 | sandbox_agent_lsb-codex_0000_0000 | 2 | 98.913% | 98.913% | 1.000 s | 55.762 MB | 83.449 MB | 66.879 MB | 98.051 MB | n/a MB | n/a MB |
| codex | 10174 | sandbox_agent_lsb-codex_0000_0000 | 2323 | 2.947% | 20.881% | 69.020 s | 135.500 MB | 142.547 MB | 376.218 MB | 569.594 MB | n/a MB | n/a MB |
| git-remote-http | 10208 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.453 MB | 19.453 MB | 100.480 MB | 100.480 MB | n/a MB | n/a MB |
| git | 10204 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.000 MB | 4.000 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 10206 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.711 MB | 3.711 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 10252 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.496 MB | 9.496 MB | 224.297 MB | 224.297 MB | n/a MB | n/a MB |
| git | 10224 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.156 MB | 4.156 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 10275 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 4.059 MB | 4.059 MB | n/a MB | n/a MB |
| python3 | 10277 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.336 MB | 21.336 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python3 | 10313 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.055 MB | 10.055 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| tokio-rt-worker | 10505 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 128.305 MB | 128.305 MB | 383.824 MB | 383.824 MB | n/a MB | n/a MB |
| python3 | 10568 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.828 MB | 20.828 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| python3 | 10681 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.668 MB | 4.668 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| tokio-rt-worker | 10789 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 133.793 MB | 133.793 MB | 387.289 MB | 387.289 MB | n/a MB | n/a MB |
| python3 | 10812 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.188 MB | 22.188 MB | 26.918 MB | 26.918 MB | n/a MB | n/a MB |
| tokio-rt-worker | 10830 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 135.383 MB | 135.383 MB | 388.004 MB | 388.004 MB | n/a MB | n/a MB |
| bash | 10839 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| python3 | 10849 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 11083 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.008 MB | 17.008 MB | 22.066 MB | 22.066 MB | n/a MB | n/a MB |
| bash | 11207 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.125 MB | 3.125 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 11213 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.359 MB | 13.359 MB | 207.160 MB | 207.160 MB | n/a MB | n/a MB |
| python | 11317 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 87.035 MB | 87.035 MB | 281.328 MB | 281.328 MB | n/a MB | n/a MB |
| bash | 11316 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.090 MB | 3.090 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 11625 | sandbox_agent_lsb-codex_0000_0000 | 4 | 91.073% | 107.397% | 2.750 s | 297.925 MB | 813.004 MB | 504.927 MB | 1008.703 MB | n/a MB | n/a MB |
| python3 | 11706 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.184 MB | 20.184 MB | 24.992 MB | 24.992 MB | n/a MB | n/a MB |
| python3 | 11807 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.156 MB | 21.156 MB | 26.844 MB | 26.844 MB | n/a MB | n/a MB |
| python3 | 11967 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.590 MB | 7.590 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python3 | 11971 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.238 MB | 8.238 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| python3 | 11983 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.730 MB | 4.730 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python | 11993 | sandbox_agent_lsb-codex_0000_0000 | 3 | 161.837% | 167.601% | 3.260 s | 233.717 MB | 381.680 MB | 634.451 MB | 801.711 MB | n/a MB | n/a MB |
| python3 | 12190 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.422 MB | 7.422 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| bash | 12191 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.113 MB | 3.113 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 12192 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 57.418 MB | 57.418 MB | 467.645 MB | 467.645 MB | n/a MB | n/a MB |
| python3 | 12281 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.812 MB | 21.812 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python | 12303 | sandbox_agent_lsb-codex_0000_0000 | 3 | 127.001% | 153.588% | 2.560 s | 283.634 MB | 416.371 MB | 620.393 MB | 823.891 MB | n/a MB | n/a MB |
| python3 | 12354 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.582 MB | 20.582 MB | 24.988 MB | 24.988 MB | n/a MB | n/a MB |
| docker | 12421 |  | 1 | n/a% | n/a% | n/a s | 24.164 MB | 24.164 MB | 1699.188 MB | 1699.188 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 34.737% | 100.000% | 11973.511 MB | 13692.000 MB | 44.368 W | 79.485 W | 104977.987 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 28.725% | 202.298% | 679.128 s | 397.539 MB | 1213.102 MB | 133.472656 MB | 176.089844 MB | 24.972915 MB | 1.411868 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 9916 | 2364.585 | interrupted |
| tool:mcp__agency__reserve_resource | -1 | 1134.142 | interrupted |
| harness:retire | -1 | 0.378 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 1 | 0 | 2364.580 | n/a | n/a | 133.473 | 2364580.111 | 2364580.111 | 2364580.111 |
| sync:result_wait | 1/1 | 0 | 0 | 2364.579 | 0.000 | 2364.579 | 133.473 | 2364579.003 | 2364579.003 | 2364579.003 |
| engine:execute | 1/1 | 1 | 0 | 2364.578 | 2.672 | 2361.898 | 133.473 | 2364578.272 | 2364578.272 | 2364578.272 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2340.678 | 0.003 | 2340.675 | 118.401 | 2340677.611 | 2340677.611 | 2340677.611 |
| harness:await_cli | 1/1 | 0 | 0 | 2337.192 | n/a | n/a | 13.966 | 2337192.290 | 2337192.290 | 2337192.290 |
| llm:attempt | 48/48 | 0 | 0 | 1171.392 | 6.232 | 1165.145 | 9.562 | 24404.004 | 15758.558 | 73296.978 |
| tool:mcp__agency__generate | 7/7 | 0 | 0 | 771.472 | n/a | n/a | 0.700 | 110210.244 | 109426.226 | 209172.638 |
| tool:Bash | 17/17 | 0 | 0 | 138.296 | n/a | n/a | 1.832 | 8135.036 | 624.055 | 51861.095 |
| tool:mcp__agency__trace | 5/5 | 0 | 0 | 53.662 | n/a | n/a | 0.086 | 10732.463 | 9182.550 | 21760.230 |
| agency:services_close | 1/1 | 1 | 0 | 20.001 | 0.001 | 20.000 | 0.004 | 20000.653 | 20000.653 | 20000.653 |
| tool:mcp__agency__inspect_module_inputs | 4/4 | 0 | 0 | 5.835 | n/a | n/a | 0.131 | 1458.761 | 1338.858 | 1945.526 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.095 | 0.735 | 2.359 | 14.203 | 3094.764 | 3094.764 | 3094.764 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.095 | 0.735 | 2.359 | 14.199 | 3094.529 | 3094.529 | 3094.529 |
| harness:submit | 1/1 | 0 | 0 | 1.416 | n/a | n/a | 26.745 | 1416.331 | 1416.331 | 1416.331 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.222 | n/a | n/a | 66.365 | 1222.194 | 1222.194 | 1222.194 |
| tool:mcp__agency__inspect | 1/1 | 0 | 0 | 1.162 | n/a | n/a | 0.000 | 1162.464 | 1162.464 | 1162.464 |
| syscall:connect | 451/451 | 0 | 0 | 1.111 | n/a | n/a | 4.171 | 2.462 | 2.133 | 4.347 |
| syscall:execve | 636/636 | 0 | 0 | 0.968 | n/a | n/a | 5.211 | 1.522 | 1.208 | 2.725 |
| tool:update_plan | 5/5 | 0 | 0 | 0.875 | n/a | n/a | 0.099 | 174.912 | 171.077 | 187.297 |
| syscall:sendto | 339/339 | 0 | 0 | 0.838 | n/a | n/a | 3.166 | 2.471 | 2.228 | 4.407 |
| harness:snapshot | 1/1 | 0 | 0 | 0.753 | n/a | n/a | 0.020 | 753.126 | 753.126 | 753.126 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.737 | n/a | n/a | 0.000 | 736.789 | 736.789 | 736.789 |
| run:container_call | 11/11 | 0 | 0 | 0.712 | 0.002 | 0.710 | 0.000 | 64.718 | 28.680 | 203.018 |
| tool:mcp__agency__get_current_resources | 2/2 | 0 | 0 | 0.450 | n/a | n/a | 0.000 | 225.075 | 225.075 | 229.859 |
| sandbox:create | 1/1 | 0 | 0 | 0.357 | 0.266 | 0.092 | 0.000 | 357.437 | 357.437 | 357.437 |
| sandbox:start | 1/1 | 0 | 0 | 0.326 | 0.002 | 0.323 | 0.000 | 325.741 | 325.741 | 325.741 |
| runtime.container_create | 1/1 | 0 | 0 | 0.326 | 0.002 | 0.323 | 0.000 | 325.597 | 325.597 | 325.597 |
| teardown:discard | 1/1 | 0 | 0 | 0.290 | 0.002 | 0.288 | 0.000 | 290.407 | 290.407 | 290.407 |
| sandbox:rm | 1/1 | 0 | 0 | 0.290 | 0.002 | 0.288 | 0.000 | 290.201 | 290.201 | 290.201 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.215 | n/a | n/a | 0.000 | 215.386 | 215.386 | 215.386 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.042 | 0.031 | 0.000 | 72.829 | 72.829 | 72.829 |
| run:detect | 1/1 | 0 | 0 | 0.050 | 0.001 | 0.049 | 0.000 | 50.006 | 50.006 | 50.006 |
| harness:launch | 1/1 | 0 | 0 | 0.044 | n/a | n/a | 1.135 | 43.725 | 43.725 | 43.725 |
| agent:create | 1/1 | 0 | 0 | 0.036 | 0.008 | 0.029 | 0.000 | 36.031 | 36.031 | 36.031 |
| sandbox:update_limits | 1/1 | 0 | 0 | 0.027 | 0.001 | 0.026 | 0.000 | 26.668 | 26.668 | 26.668 |
| syscall:bind | 10/10 | 0 | 0 | 0.025 | n/a | n/a | 0.314 | 2.500 | 2.124 | 4.031 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.000 | 2.506 | 2.506 | 2.506 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.428 | 1.428 | 1.428 |
| sync:container | 11/11 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.073 | 0.066 | 0.114 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.224 | 0.224 | 0.224 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.062 | 0.062 | 0.062 |
| tool:mcp__agency__reserve_resource | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2346 | 0.070 | 0.030 | 0.822 | 0.241 | 1.644597 CPU seconds | n/a |
| GPU 0 memory | MB | 2347 | 11973.511 | 11670.000 | 13692.000 | 11912.000 | n/a | n/a |
| GPU 0 power | W | 2347 | 44.368 | 27.533 | 79.485 | 28.473 | n/a | 104977.987 J |
| GPU 0 proc / 9767-453565 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b memory | MB | 2347 | 3318.060 | 3118.000 | 5034.000 | 3254.000 | n/a | n/a |
| GPU 0 proc / 9767-453565 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b estimated power | W | 1326 | 3.049 | 0.000 | 78.690 | 0.000 | n/a | n/a |
| GPU 0 proc / 9767-453565 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b utilization | percent | 1326 | 3.828 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 9808-455467 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b memory | MB | 2347 | 8173.451 | 8070.000 | 8176.000 | 8176.000 | n/a | n/a |
| GPU 0 proc / 9808-455467 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b estimated power | W | 987 | 53.995 | 0.000 | 72.616 | 0.000 | n/a | n/a |
| GPU 0 proc / 9808-455467 / sandbox / ~ / device / GPU-6fec05a0-512c-7744-3da7-dcd27d814c4b utilization | percent | 987 | 74.828 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2347 | 11491.511 | 11188.000 | 13210.000 | 11430.000 | n/a | n/a |
| GPU 0 utilization | percent | 2347 | 34.737 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2347 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2346 | 0.698 | 0.115 | 75.827 | 0.374 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2346 | 10.956 | 0.000 | 55.112 | 1.504 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2346 | 0.059 | 0.000 | 60.670 | 0.051 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2346 | 0.287 | 0.000 | 41.350 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2346 | 0.047 | 0.000 | 19.572 | 0.078 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2346 | 0.051 | 0.000 | 20.287 | 0.078 | n/a | n/a |
| host mem_total_mb | MB | 2347 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 2347 | 6845.257 | 6388.891 | 7743.508 | 7079.582 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2346 | 0.000 | 0.000 | 1.127 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2346 | 0.000 | 0.000 | 1.128 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2346 | 0.014 | 0.000 | 25.101 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2346 | 0.009 | 0.000 | 0.686 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 10027) CPU | percent | 2346 | 0.002 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 10027) rss_mb | MB | 2347 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 10027) main thread run-queue wait | percent | 2346 | 0.002 | 0.000 | 4.327 | 0.000 | 0.047857 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 10027) vms_mb | MB | 2347 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 10059) CPU | percent | 2346 | 0.002 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 10059) rss_mb | MB | 2347 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 10059) main thread run-queue wait | percent | 2346 | 0.002 | 0.000 | 2.894 | 0.000 | 0.035790 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 10059) vms_mb | MB | 2347 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10151) CPU | percent | 2346 | 24.582 | 0.000 | 101.271 | 0.000 | 581.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10151) rss_mb | MB | 2347 | 112.188 | 3.086 | 118.453 | 118.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10151) main thread run-queue wait | percent | 2346 | 0.000 | 0.000 | 0.007 | 0.000 | 0.000080 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10151) vms_mb | MB | 2347 | 972.356 | 4.262 | 976.199 | 975.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 10157) CPU | percent | 1 | 98.913 | 98.913 | 98.913 | 98.913 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 10157) rss_mb | MB | 2 | 55.762 | 28.074 | 83.449 | 83.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 10157) main thread run-queue wait | percent | 1 | 0.003 | 0.003 | 0.003 | 0.003 | 0.000032 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 10157) vms_mb | MB | 2 | 66.879 | 35.707 | 98.051 | 98.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10174) CPU | percent | 2322 | 2.947 | 0.000 | 20.881 | 5.967 | 69.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10174) rss_mb | MB | 2323 | 135.500 | 19.594 | 142.547 | 140.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10174) main thread run-queue wait | percent | 2322 | 0.002 | 0.000 | 4.853 | 0.000 | 0.050850 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10174) vms_mb | MB | 2323 | 376.218 | 294.938 | 569.594 | 389.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 10204) rss_mb | MB | 1 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 10204) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 10206) rss_mb | MB | 1 | 3.711 | 3.711 | 3.711 | 3.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 10206) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 10208) rss_mb | MB | 1 | 19.453 | 19.453 | 19.453 | 19.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 10208) vms_mb | MB | 1 | 100.480 | 100.480 | 100.480 | 100.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 10224) rss_mb | MB | 1 | 4.156 | 4.156 | 4.156 | 4.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 10224) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 10252) rss_mb | MB | 1 | 9.496 | 9.496 | 9.496 | 9.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 10252) vms_mb | MB | 1 | 224.297 | 224.297 | 224.297 | 224.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 10275) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 10275) vms_mb | MB | 1 | 4.059 | 4.059 | 4.059 | 4.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10277) rss_mb | MB | 1 | 21.336 | 21.336 | 21.336 | 21.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10277) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10313) rss_mb | MB | 1 | 10.055 | 10.055 | 10.055 | 10.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10313) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10505) rss_mb | MB | 1 | 128.305 | 128.305 | 128.305 | 128.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10505) vms_mb | MB | 1 | 383.824 | 383.824 | 383.824 | 383.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10568) rss_mb | MB | 1 | 20.828 | 20.828 | 20.828 | 20.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10568) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10681) rss_mb | MB | 1 | 4.668 | 4.668 | 4.668 | 4.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10681) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10789) rss_mb | MB | 1 | 133.793 | 133.793 | 133.793 | 133.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10789) vms_mb | MB | 1 | 387.289 | 387.289 | 387.289 | 387.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10812) rss_mb | MB | 1 | 22.188 | 22.188 | 22.188 | 22.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10812) vms_mb | MB | 1 | 26.918 | 26.918 | 26.918 | 26.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10830) rss_mb | MB | 1 | 135.383 | 135.383 | 135.383 | 135.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 10830) vms_mb | MB | 1 | 388.004 | 388.004 | 388.004 | 388.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10839) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 10839) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10849) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 10849) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11083) rss_mb | MB | 1 | 17.008 | 17.008 | 17.008 | 17.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11083) vms_mb | MB | 1 | 22.066 | 22.066 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 11207) rss_mb | MB | 1 | 3.125 | 3.125 | 3.125 | 3.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 11207) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 11213) rss_mb | MB | 1 | 13.359 | 13.359 | 13.359 | 13.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 11213) vms_mb | MB | 1 | 207.160 | 207.160 | 207.160 | 207.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 11316) rss_mb | MB | 1 | 3.090 | 3.090 | 3.090 | 3.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 11316) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 11317) rss_mb | MB | 1 | 87.035 | 87.035 | 87.035 | 87.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 11317) vms_mb | MB | 1 | 281.328 | 281.328 | 281.328 | 281.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_activations.py (PID 11625) CPU | percent | 3 | 91.073 | 73.454 | 107.397 | 92.367 | 2.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_activations.py (PID 11625) rss_mb | MB | 4 | 297.925 | 23.547 | 813.004 | 230.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_activations.py (PID 11625) main thread run-queue wait | percent | 3 | 5.029 | 0.120 | 11.704 | 3.264 | 0.151770 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — analyze_activations.py (PID 11625) vms_mb | MB | 4 | 504.927 | 215.590 | 1008.703 | 449.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11706) rss_mb | MB | 1 | 20.184 | 20.184 | 20.184 | 20.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11706) vms_mb | MB | 1 | 24.992 | 24.992 | 24.992 | 24.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11807) rss_mb | MB | 1 | 21.156 | 21.156 | 21.156 | 21.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11807) vms_mb | MB | 1 | 26.844 | 26.844 | 26.844 | 26.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11967) rss_mb | MB | 1 | 7.590 | 7.590 | 7.590 | 7.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11967) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11971) rss_mb | MB | 1 | 8.238 | 8.238 | 8.238 | 8.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11971) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11983) rss_mb | MB | 1 | 4.730 | 4.730 | 4.730 | 4.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 11983) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_gate.py (PID 11993) CPU | percent | 2 | 161.837 | 156.073 | 167.601 | 167.601 | 3.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_gate.py (PID 11993) rss_mb | MB | 3 | 233.717 | 49.348 | 381.680 | 381.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_gate.py (PID 11993) main thread run-queue wait | percent | 2 | 56.945 | 53.980 | 59.910 | 59.910 | 1.147105 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — derive_gate.py (PID 11993) vms_mb | MB | 3 | 634.451 | 429.934 | 801.711 | 801.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 12190) rss_mb | MB | 1 | 7.422 | 7.422 | 7.422 | 7.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 12190) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 12191) rss_mb | MB | 1 | 3.113 | 3.113 | 3.113 | 3.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 12191) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 12192) rss_mb | MB | 1 | 57.418 | 57.418 | 57.418 | 57.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 12192) vms_mb | MB | 1 | 467.645 | 467.645 | 467.645 | 467.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 12281) rss_mb | MB | 1 | 21.812 | 21.812 | 21.812 | 21.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 12281) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 12303) CPU | percent | 2 | 127.001 | 100.414 | 153.588 | 153.588 | 2.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 12303) rss_mb | MB | 3 | 283.634 | 18.160 | 416.371 | 416.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 12303) main thread run-queue wait | percent | 2 | 30.073 | 5.934 | 54.212 | 54.212 | 0.606791 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — build_adapter.py (PID 12303) vms_mb | MB | 3 | 620.393 | 213.398 | 823.891 | 823.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 12354) rss_mb | MB | 1 | 20.582 | 20.582 | 20.582 | 20.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 12354) vms_mb | MB | 1 | 24.988 | 24.988 | 24.988 | 24.988 | n/a | n/a |
| docker inspect (PID 12421) rss_mb | MB | 1 | 24.164 | 24.164 | 24.164 | 24.164 | n/a | n/a |
| docker inspect (PID 12421) vms_mb | MB | 1 | 1699.188 | 1699.188 | 1699.188 | 1699.188 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4633) CPU | percent | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4633) io read MB/s | MB/s | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4633) io write MB/s | MB/s | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4633) rss_mb | MB | 2347 | 3.422 | 3.422 | 3.422 | 3.422 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4633) main thread run-queue wait | percent | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4633) vms_mb | MB | 2347 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9767) CPU | percent | 2346 | 3.945 | 0.000 | 103.502 | 0.000 | 93.520000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 9767) io read MB/s | MB/s | 2346 | 0.001 | 0.000 | 1.042 | 0.051 | 1.792969 MB | n/a |
| Agency harness — python -m lsbench (PID 9767) io write MB/s | MB/s | 2346 | 0.181 | 0.015 | 78.755 | 0.035 | 430.222656 MB | n/a |
| Agency harness — python -m lsbench (PID 9767) rss_mb | MB | 2347 | 2735.239 | 2219.613 | 3010.691 | 3010.691 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9767) main thread run-queue wait | percent | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 9767) vms_mb | MB | 2347 | 16063.801 | 13667.859 | 18218.629 | 16473.609 | n/a | n/a |
| Python — vllm (PID 9772) CPU | percent | 2346 | 1.058 | 0.000 | 5.951 | 0.000 | 25.060000 CPU seconds | n/a |
| Python — vllm (PID 9772) io read MB/s | MB/s | 2346 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 9772) io write MB/s | MB/s | 2346 | 0.000 | 0.000 | 0.008 | 0.000 | 0.128906 MB | n/a |
| Python — vllm (PID 9772) rss_mb | MB | 2347 | 1806.204 | 1802.863 | 1806.738 | 1806.738 | n/a | n/a |
| Python — vllm (PID 9772) main thread run-queue wait | percent | 2346 | 0.015 | 0.000 | 0.730 | 0.000 | 0.362570 run-queue seconds | n/a |
| Python — vllm (PID 9772) vms_mb | MB | 2347 | 11047.494 | 10974.559 | 11049.578 | 11049.578 | n/a | n/a |
| Python — python -c (PID 9807) CPU | percent | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 9807) io read MB/s | MB/s | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9807) io write MB/s | MB/s | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9807) rss_mb | MB | 2347 | 12.184 | 12.184 | 12.184 | 12.184 | n/a | n/a |
| Python — python -c (PID 9807) main thread run-queue wait | percent | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 9807) vms_mb | MB | 2347 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 9808) CPU | percent | 2346 | 10.509 | 0.000 | 45.511 | 0.995 | 249.010000 CPU seconds | n/a |
| VLLM::EngineCore (PID 9808) io read MB/s | MB/s | 2346 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 9808) io write MB/s | MB/s | 2346 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 9808) rss_mb | MB | 2347 | 2340.604 | 2335.770 | 2341.395 | 2341.395 | n/a | n/a |
| VLLM::EngineCore (PID 9808) main thread run-queue wait | percent | 2346 | 0.012 | 0.000 | 0.359 | 0.000 | 0.296213 run-queue seconds | n/a |
| VLLM::EngineCore (PID 9808) vms_mb | MB | 2347 | 21240.421 | 21235.086 | 21241.309 | 21241.309 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 2346 | 28.725 | 0.180 | 202.298 | 0.204 | 679.127674 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2346 | 0.385 | 0.000 | 49.578 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2346 | 0.465 | 0.000 | 74.782 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 2346 | 0.022 | 0.000 | 17.818 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 2346 | 0.024 | 0.000 | 18.212 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 2346 | 0.057 | 0.000 | 60.604 | 0.000 | 133.472656 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 2346 | 0.075 | 0.000 | 37.931 | 0.000 | 176.089844 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 2347 | 397.539 | 18.625 | 1213.102 | 245.656 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2346 | 0.000 | 0.000 | 1.122 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2346 | 0.000 | 0.000 | 1.122 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 2346 | 0.011 | 0.000 | 24.280 | 0.000 | 24.972915 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 2346 | 0.001 | 0.000 | 0.142 | 0.000 | 1.411868 MB | n/a |
| workload total CPU | percent | 2346 | 15.513 | 1.434 | 104.763 | 6.460 | 367.627477 CPU seconds | n/a |
| workload total memory | MB | 2347 | 6278.748 | 5727.617 | 6623.168 | 6623.168 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
