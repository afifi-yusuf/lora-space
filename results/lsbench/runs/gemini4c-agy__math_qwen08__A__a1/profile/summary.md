# agprof summary

- Duration: **8130.766 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **152 calls**, 152 succeeded, 0 failed, 0 interrupted, n/a reported retries, 6582.570 s total wait
- Tools: **203/203 completed**, 2 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **898001** at 1.969 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 8105970.065 / 8105970.065 ms |
| LLM latency p50 / p95 | 25478.711 / 133398.401 ms |
| LLM TTFT p50 / p95 | 14940.926 / 121656.533 ms |
| LLM input / output tokens | 17937444 / 181816 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 152 total, 152 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- antigravity: {"automatic_functions": "host_only", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "unavailable", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| edit_file | 4/4 | 4 | 0 | 0 | n/a | n/a |
| manage_task | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 9/9 | 9 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 9/9 | 8 | 1 | 0 | n/a | n/a |
| mcp__agency__get_current_resources | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__submitted_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 4/4 | 4 | 0 | 0 | n/a | n/a |
| mcp__agency__top_activations | 8/8 | 8 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 24/24 | 24 | 0 | 0 | n/a | n/a |
| read_file | 34/34 | 34 | 0 | 0 | n/a | n/a |
| run_command | 90/90 | 90 | 0 | 0 | n/a | n/a |
| run_workflow | 1/1 | 0 | 1 | 0 | n/a | n/a |
| schedule | 2/2 | 2 | 0 | 0 | n/a | n/a |
| write_file | 6/6 | 6 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 17.534% | 301.395% | 1430.574 s | 5596.896 MB | 7013.289 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 8119 |  | 8077 | 0.327% | 5.967% | 26.630 s | 1787.614 MB | 1788.016 MB | 11996.550 MB | 11999.234 MB | 0.000000 MB | 0.144531 MB |
| python | 8108 |  | 8077 | 13.359% | 300.995% | 1090.020 s | 2555.859 MB | 4072.965 MB | 16275.825 MB | 21082.699 MB | 0.941406 MB | 969.074219 MB |
| python3 | 8668 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 98.447% | 98.447% | 1.000 s | 58.695 MB | 83.613 MB | 69.645 MB | 98.152 MB | n/a MB | n/a MB |
| lsb_grid_worker | 8099 |  | 8077 | 0.000% | 0.000% | 0.000 s | 3.402 MB | 3.402 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| lsb_guard.sh | 8129 |  | 8077 | 0.001% | 0.995% | 0.070 s | 3.387 MB | 3.387 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| sleep | 8132 |  | 16 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 8385 |  | 8077 | 0.049% | 4.970% | 4.010 s | 45.336 MB | 46.141 MB | 131.321 MB | 131.949 MB | 0.000000 MB | 0.402344 MB |
| VLLM::EngineCor | 8258 |  | 8077 | 3.773% | 54.493% | 307.590 s | 2346.616 MB | 2346.938 MB | 21867.676 MB | 21867.945 MB | 0.000000 MB | 0.050781 MB |
| python | 8257 |  | 8077 | 0.000% | 0.000% | 0.000 s | 12.184 MB | 12.184 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| bash | 8662 | sandbox_agent_lsb-antigravity_0000_0000 | 8053 | 38.688% | 101.216% | 3135.000 s | 109.737 MB | 149.359 MB | 971.153 MB | 973.465 MB | n/a MB | n/a MB |
| tail | 8557 | sandbox_agent_lsb-antigravity_0000_0000 | 8053 | 0.002% | 0.995% | 0.180 s | 1.473 MB | 1.473 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| docker-init | 8518 | sandbox_agent_lsb-antigravity_0000_0000 | 8053 | 0.002% | 0.995% | 0.160 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| antigravity | 8685 | sandbox_agent_lsb-antigravity_0000_0000 | 8047 | 1.448% | 74.230% | 117.240 s | 301.602 MB | 349.234 MB | 2280.872 MB | 2345.090 MB | n/a MB | n/a MB |
| sleep | 8710 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 8810 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.277 MB | 21.277 MB | 25.844 MB | 25.844 MB | n/a MB | n/a MB |
| sh | 8809 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 8841 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 8874 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 8894 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.367 MB | 1.367 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 8895 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.367 MB | 1.367 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 8915 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 8917 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9015 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9026 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9115 | sandbox_agent_lsb-antigravity_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.367 MB | 1.367 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 9113 | sandbox_agent_lsb-antigravity_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 9123 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9125 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9127 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 9303 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9304 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.676 MB | 17.676 MB | 23.020 MB | 23.020 MB | n/a MB | n/a MB |
| sleep | 9311 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 9312 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.570 MB | 1.570 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9313 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.363 MB | 7.363 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sleep | 9316 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9359 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 9369 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9370 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.473 MB | 19.473 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| python3 | 9392 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.391 MB | 9.391 MB | 13.316 MB | 13.316 MB | n/a MB | n/a MB |
| sleep | 9400 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 9489 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9490 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.301 MB | 16.301 MB | 20.848 MB | 20.848 MB | n/a MB | n/a MB |
| sleep | 9501 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 9534 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.516 MB | 9.516 MB | 13.316 MB | 13.316 MB | n/a MB | n/a MB |
| sleep | 9551 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 9553 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.496 MB | 7.496 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 9552 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 9589 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9617 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9649 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9761 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9816 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9832 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 9833 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.414 MB | 1.414 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9834 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.090 MB | 22.090 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| python3 | 9845 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.754 MB | 15.754 MB | 20.398 MB | 20.398 MB | n/a MB | n/a MB |
| sh | 9844 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 9853 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 9854 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9855 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.719 MB | 10.719 MB | 15.062 MB | 15.062 MB | n/a MB | n/a MB |
| sleep | 9865 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9961 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 10052 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10053 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.332 MB | 21.332 MB | 25.715 MB | 25.715 MB | n/a MB | n/a MB |
| sh | 10070 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.535 MB | 1.535 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10071 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.852 MB | 14.852 MB | 19.957 MB | 19.957 MB | n/a MB | n/a MB |
| sleep | 10067 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10109 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10111 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10125 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10141 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10244 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 10252 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.680 MB | 15.680 MB | 20.500 MB | 20.500 MB | n/a MB | n/a MB |
| sh | 10251 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.539 MB | 1.539 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 10260 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10261 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.043 MB | 8.043 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sleep | 10273 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10291 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10293 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10295 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10455 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10457 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 10458 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.367 MB | 1.367 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10459 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.746 MB | 7.746 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sleep | 10471 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10485 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10521 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10620 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10631 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10633 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10635 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10721 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10742 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10744 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 10751 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10752 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.738 MB | 14.738 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| python3 | 10765 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.941 MB | 7.941 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 10764 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 10778 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 10796 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.496 MB | 7.496 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sh | 10795 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.539 MB | 1.539 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10820 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.785 MB | 18.785 MB | 24.223 MB | 24.223 MB | n/a MB | n/a MB |
| sh | 10819 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 10831 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 10832 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.469 MB | 1.469 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10833 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.414 MB | 18.414 MB | 23.172 MB | 23.172 MB | n/a MB | n/a MB |
| sleep | 10920 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10942 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10945 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10947 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10949 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 10953 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.207 MB | 14.207 MB | 367.594 MB | 367.594 MB | n/a MB | n/a MB |
| python3 | 10974 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 171.645% | 180.963% | 5.180 s | 1192.136 MB | 1480.344 MB | 1566.961 MB | 1831.043 MB | n/a MB | n/a MB |
| sleep | 10994 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| pgrep | 11109 |  | 1 | n/a% | n/a% | n/a s | 3.305 MB | 3.305 MB | 10.102 MB | 10.102 MB | n/a MB | n/a MB |
| sleep | 11110 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11117 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.883 MB | 13.883 MB | 367.387 MB | 367.387 MB | n/a MB | n/a MB |
| sleep | 11132 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11137 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11138 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.863 MB | 14.863 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| python3 | 11157 | sandbox_agent_lsb-antigravity_0000_0000 | 23 | 99.751% | 100.468% | 22.080 s | 11.930 MB | 11.930 MB | 15.441 MB | 15.441 MB | n/a MB | n/a MB |
| sleep | 11165 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11178 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.691 MB | 9.691 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 11177 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.469 MB | 1.469 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11209 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11213 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.133 MB | 0.133 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python3 | 11224 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 72.250 MB | 72.250 MB | 423.473 MB | 423.473 MB | n/a MB | n/a MB |
| sleep | 11239 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11350 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11352 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.828 MB | 15.828 MB | 20.535 MB | 20.535 MB | n/a MB | n/a MB |
| sh | 11351 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11374 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11391 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11392 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.152 MB | 21.152 MB | 25.586 MB | 25.586 MB | n/a MB | n/a MB |
| sleep | 11398 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11413 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.680 MB | 14.680 MB | 19.957 MB | 19.957 MB | n/a MB | n/a MB |
| sh | 11412 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.414 MB | 1.414 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11456 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11469 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 28.434 MB | 28.434 MB | n/a MB | n/a MB |
| sleep | 11480 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11501 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.969 MB | 9.969 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sh | 11500 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11515 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.473 MB | 19.473 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| sh | 11514 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11524 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11535 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.891 MB | 20.891 MB | 25.461 MB | 25.461 MB | n/a MB | n/a MB |
| sh | 11534 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11574 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11576 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11589 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 11603 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.680 MB | 2.680 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 11613 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.379 MB | 5.379 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| sh | 11612 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11620 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.789 MB | 21.789 MB | 26.996 MB | 26.996 MB | n/a MB | n/a MB |
| sh | 11619 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.441 MB | 1.441 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11625 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1028.062 MB | 1028.062 MB | 1379.492 MB | 1379.492 MB | n/a MB | n/a MB |
| sleep | 11624 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11735 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11767 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11790 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.871 MB | 4.871 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| sh | 11789 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.367 MB | 1.367 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11794 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.852 MB | 15.852 MB | 20.500 MB | 20.500 MB | n/a MB | n/a MB |
| sh | 11793 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.500 MB | 1.500 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11808 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11810 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.039 MB | 22.039 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| sh | 11809 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 11813 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11814 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.242 MB | 19.242 MB | 24.684 MB | 24.684 MB | n/a MB | n/a MB |
| sh | 11842 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| sleep | 11853 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11855 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11876 | sandbox_agent_lsb-antigravity_0000_0000 | 152 | 177.332% | 198.918% | 269.530 s | 321.951 MB | 439.844 MB | 697.505 MB | 826.539 MB | n/a MB | n/a MB |
| sh | 11889 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.570 MB | 1.570 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11890 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 4.970% | 5.963% | 0.100 s | 14.059 MB | 20.605 MB | 19.172 MB | 25.332 MB | n/a MB | n/a MB |
| python3 | 11893 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 2.981% | 2.981% | 0.030 s | 16.586 MB | 18.852 MB | 22.451 MB | 24.816 MB | n/a MB | n/a MB |
| sh | 11892 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.570 MB | 1.570 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11900 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11901 | sandbox_agent_lsb-antigravity_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.648 MB | 1.648 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11902 | sandbox_agent_lsb-antigravity_0000_0000 | 5 | 2.237% | 2.982% | 0.090 s | 14.703 MB | 20.109 MB | 20.140 MB | 25.328 MB | n/a MB | n/a MB |
| sh | 11903 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.504 MB | 1.504 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11904 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 2.980% | 5.965% | 0.090 s | 16.493 MB | 21.371 MB | 21.753 MB | 26.988 MB | n/a MB | n/a MB |
| python3 | 11911 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 1.988% | 2.983% | 0.060 s | 13.289 MB | 18.309 MB | 18.515 MB | 24.680 MB | n/a MB | n/a MB |
| sh | 11910 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 11914 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11915 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 2.379% | 7.926% | 0.120 s | 11.577 MB | 21.184 MB | 16.747 MB | 27.121 MB | n/a MB | n/a MB |
| sleep | 12000 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12019 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12021 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12025 | sandbox_agent_lsb-antigravity_0000_0000 | 32 | 170.395% | 193.809% | 53.180 s | 140.109 MB | 162.098 MB | 518.214 MB | 543.391 MB | n/a MB | n/a MB |
| python3 | 12040 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 1.989% | 4.972% | 0.060 s | 10.582 MB | 18.156 MB | 15.326 MB | 23.172 MB | n/a MB | n/a MB |
| sh | 12039 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.535 MB | 1.535 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12056 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12074 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.469 MB | 20.469 MB | 25.062 MB | 25.062 MB | n/a MB | n/a MB |
| sh | 12073 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.363 MB | 1.363 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12080 | sandbox_agent_lsb-antigravity_0000_0000 | 37 | 173.527% | 197.148% | 62.940 s | 141.367 MB | 155.816 MB | 519.684 MB | 537.410 MB | n/a MB | n/a MB |
| sleep | 12095 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12122 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12134 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12135 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.695 MB | 21.695 MB | 26.926 MB | 26.926 MB | n/a MB | n/a MB |
| sleep | 12145 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12155 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 12170 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 12171 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 150.976% | 173.002% | 3.040 s | 735.048 MB | 1067.820 MB | 1253.733 MB | 1450.129 MB | n/a MB | n/a MB |
| sh | 12179 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12180 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.719 MB | 20.719 MB | 25.203 MB | 25.203 MB | n/a MB | n/a MB |
| sleep | 12186 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12217 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12219 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12229 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12230 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.156 MB | 10.156 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sleep | 12236 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12238 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12249 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12250 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.812 MB | 21.812 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python3 | 12262 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.992 MB | 16.992 MB | 22.184 MB | 22.184 MB | n/a MB | n/a MB |
| sh | 12261 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12272 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.715 MB | 0.715 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| sh | 12271 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.414 MB | 1.414 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12282 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.332 MB | 21.332 MB | 25.707 MB | 25.707 MB | n/a MB | n/a MB |
| sh | 12281 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.367 MB | 1.367 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12290 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12323 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.668 MB | 9.668 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sh | 12322 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12332 | sandbox_agent_lsb-antigravity_0000_0000 | 25 | 167.269% | 192.291% | 40.410 s | 142.516 MB | 162.855 MB | 519.556 MB | 554.711 MB | n/a MB | n/a MB |
| sleep | 12353 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12355 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12368 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 31.660 MB | 31.660 MB | 382.348 MB | 382.348 MB | n/a MB | n/a MB |
| sleep | 12391 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12395 | sandbox_agent_lsb-antigravity_0000_0000 | 9 | 167.660% | 184.841% | 13.500 s | 1817.419 MB | 2042.680 MB | 2193.098 MB | 2425.172 MB | n/a MB | n/a MB |
| sleep | 12410 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12414 | sandbox_agent_lsb-antigravity_0000_0000 | 10 | 180.028% | 189.865% | 16.340 s | 2004.396 MB | 2042.121 MB | 2414.178 MB | 2425.094 MB | n/a MB | n/a MB |
| sleep | 12431 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12456 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12458 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12460 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12474 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 158.361% | 187.954% | 7.970 s | 1734.832 MB | 2079.723 MB | 2107.284 MB | 2462.801 MB | n/a MB | n/a MB |
| python3 | 12483 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.402 MB | 21.402 MB | 25.715 MB | 25.715 MB | n/a MB | n/a MB |
| sh | 12482 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12485 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12494 | sandbox_agent_lsb-antigravity_0000_0000 | 11 | 172.220% | 187.941% | 17.320 s | 1898.371 MB | 2076.059 MB | 2307.620 MB | 2458.105 MB | n/a MB | n/a MB |
| sleep | 12510 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12535 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12537 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12550 | sandbox_agent_lsb-antigravity_0000_0000 | 17 | 178.395% | 194.110% | 28.720 s | 2305.304 MB | 2972.617 MB | 2688.890 MB | 3351.398 MB | n/a MB | n/a MB |
| sleep | 12570 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12581 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12587 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12588 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.152 MB | 2.152 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| sleep | 12595 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12618 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.266 MB | 9.266 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 12617 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12627 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12637 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12639 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12647 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sh | 12646 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.414 MB | 1.414 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12656 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12658 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12691 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12693 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12708 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12735 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12742 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12744 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12775 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12915 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12928 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12940 | sandbox_agent_lsb-antigravity_0000_0000 | 37 | 176.303% | 193.888% | 63.900 s | 2431.383 MB | 4260.945 MB | 2811.213 MB | 4706.426 MB | n/a MB | n/a MB |
| sleep | 12954 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12966 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12986 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.367 MB | 1.367 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12987 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.262 MB | 20.262 MB | 24.941 MB | 24.941 MB | n/a MB | n/a MB |
| sleep | 13002 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13004 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13022 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.176 MB | 21.176 MB | 25.578 MB | 25.578 MB | n/a MB | n/a MB |
| sh | 13021 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 13028 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13030 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13048 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13068 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13083 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 13087 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13088 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.578 MB | 16.578 MB | 21.848 MB | 21.848 MB | n/a MB | n/a MB |
| sleep | 13099 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13101 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13114 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13105 | sandbox_agent_lsb-antigravity_0000_0000 | 41 | 178.336% | 195.106% | 71.810 s | 2679.813 MB | 4532.699 MB | 3056.542 MB | 4911.066 MB | n/a MB | n/a MB |
| sh | 13140 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.629 MB | 1.629 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13141 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.172 MB | 22.172 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| sleep | 13150 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13156 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.039 MB | 21.039 MB | 25.316 MB | 25.316 MB | n/a MB | n/a MB |
| sh | 13155 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.570 MB | 1.570 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 13162 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13166 | sandbox_agent_lsb-antigravity_0000_0000 | 8 | 175.479% | 199.307% | 12.360 s | 1429.053 MB | 2492.008 MB | 1912.802 MB | 2873.754 MB | n/a MB | n/a MB |
| python3 | 13185 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.242 MB | 22.242 MB | 27.062 MB | 27.062 MB | n/a MB | n/a MB |
| sh | 13184 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.562 MB | 1.562 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13192 | sandbox_agent_lsb-antigravity_0000_0000 | 8 | 173.585% | 190.877% | 12.240 s | 1412.880 MB | 2492.289 MB | 1806.375 MB | 2873.762 MB | n/a MB | n/a MB |
| sleep | 13201 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13211 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.566 MB | 20.566 MB | 372.105 MB | 372.105 MB | n/a MB | n/a MB |
| sleep | 13228 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13258 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| docker | 13312 |  | 2 | 0.000% | 0.000% | 0.000 s | 30.039 MB | 30.039 MB | 1988.035 MB | 1988.035 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13452 |  | 12 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 14.289% | 100.000% | 12022.890 MB | 16228.000 MB | 35.839 W | 78.440 W | 291569.635 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-antigravity_0000_0000 | 49.609% | 217.393% | 4020.202 s | 384.457 MB | 4947.047 MB | 0.000000 MB | 471.335938 MB | 0.435779 MB | 3.677810 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 8392 | 8130.712 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 8105.970 | n/a | n/a | 0.000 | 8105970.065 | 8105970.065 | 8105970.065 |
| engine:execute | 1/1 | 0 | 0 | 8105.968 | 6.147 | 8099.792 | 0.000 | 8105968.360 | 8105968.360 | 8105968.360 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 8100.029 | 0.043 | 8099.986 | 0.000 | 8100029.263 | 8100029.263 | 8100029.263 |
| llm:attempt | 152/152 | 0 | 0 | 6582.570 | 6.487 | 6576.065 | 0.000 | 43306.381 | 25478.711 | 133398.401 |
| tool:mcp__agency__generate | 9/9 | 1 | 0 | 581.887 | n/a | n/a | 0.000 | 64654.088 | 43987.031 | 157738.731 |
| tool:run_command | 90/90 | 0 | 0 | 463.998 | n/a | n/a | 0.000 | 5155.537 | 354.084 | 29056.460 |
| tool:mcp__agency__top_activations | 8/8 | 0 | 0 | 254.193 | n/a | n/a | 0.000 | 31774.155 | 31716.162 | 32508.243 |
| tool:mcp__agency__token_stats | 4/4 | 0 | 0 | 226.573 | n/a | n/a | 0.000 | 56643.285 | 45595.674 | 123298.030 |
| tool:mcp__agency__trace | 24/24 | 0 | 0 | 62.438 | n/a | n/a | 0.000 | 2601.569 | 1260.518 | 9830.663 |
| tool:read_file | 34/34 | 0 | 0 | 14.572 | n/a | n/a | 0.000 | 428.575 | 202.379 | 258.150 |
| tool:mcp__agency__attribution | 9/9 | 0 | 0 | 10.600 | n/a | n/a | 0.000 | 1177.822 | 1105.562 | 2010.339 |
| tool:manage_task | 3/3 | 0 | 0 | 9.556 | n/a | n/a | 0.000 | 3185.361 | 345.104 | 8117.243 |
| tool:mcp__agency__attention | 3/3 | 0 | 0 | 7.341 | n/a | n/a | 0.000 | 2447.056 | 3194.517 | 3387.262 |
| tool:schedule | 2/2 | 0 | 0 | 7.048 | n/a | n/a | 0.000 | 3524.041 | 3524.041 | 6500.065 |
| syscall:connect | 1087/1087 | 0 | 0 | 3.469 | n/a | n/a | 0.000 | 3.191 | 2.142 | 4.561 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.033 | 0.692 | 2.341 | 0.000 | 3033.122 | 3033.122 | 3033.122 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.033 | 0.692 | 2.341 | 0.000 | 3032.813 | 3032.813 | 3032.813 |
| run:container_call | 13/13 | 0 | 0 | 2.499 | 0.003 | 2.496 | 0.000 | 192.211 | 33.823 | 847.651 |
| tool:write_file | 6/6 | 0 | 0 | 2.233 | n/a | n/a | 0.000 | 372.101 | 364.413 | 415.129 |
| teardown:commit | 1/1 | 0 | 0 | 2.123 | 0.004 | 2.119 | 0.000 | 2123.388 | 2123.388 | 2123.388 |
| syscall:sendto | 812/812 | 0 | 0 | 1.947 | n/a | n/a | 0.000 | 2.398 | 1.913 | 3.744 |
| sandbox:commit | 1/1 | 0 | 0 | 1.934 | 0.002 | 1.931 | 0.000 | 1933.780 | 1933.780 | 1933.780 |
| checkpoint.total | 1/1 | 0 | 0 | 1.934 | 0.002 | 1.931 | 0.000 | 1933.643 | 1933.643 | 1933.643 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.933 | 0.002 | 1.931 | 0.000 | 1933.497 | 1933.497 | 1933.497 |
| tool:mcp__agency__patch | 2/2 | 0 | 0 | 1.926 | n/a | n/a | 0.000 | 962.912 | 962.912 | 968.040 |
| syscall:execve | 1019/1019 | 0 | 0 | 1.624 | n/a | n/a | 0.000 | 1.593 | 1.242 | 1.607 |
| tool:edit_file | 4/4 | 0 | 0 | 1.407 | n/a | n/a | 0.000 | 351.667 | 349.645 | 376.212 |
| tool:run_workflow | 1/1 | 1 | 0 | 1.081 | n/a | n/a | 0.000 | 1080.917 | 1080.917 | 1080.917 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.508 | n/a | n/a | 0.000 | 507.554 | 507.554 | 507.554 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.414 | n/a | n/a | 0.000 | 414.483 | 414.483 | 414.483 |
| tool:mcp__agency__submitted_output | 1/1 | 0 | 0 | 0.377 | n/a | n/a | 0.000 | 376.561 | 376.561 | 376.561 |
| sandbox:create | 1/1 | 0 | 0 | 0.346 | 0.248 | 0.098 | 0.000 | 346.028 | 346.028 | 346.028 |
| sandbox:start | 1/1 | 0 | 0 | 0.311 | 0.002 | 0.308 | 0.000 | 310.550 | 310.550 | 310.550 |
| runtime.container_create | 1/1 | 0 | 0 | 0.310 | 0.002 | 0.308 | 0.000 | 310.413 | 310.413 | 310.413 |
| tool:mcp__agency__get_current_resources | 1/1 | 0 | 0 | 0.199 | n/a | n/a | 0.000 | 199.039 | 199.039 | 199.039 |
| sandbox:stop | 1/1 | 0 | 0 | 0.189 | 0.002 | 0.188 | 0.000 | 189.297 | 189.297 | 189.297 |
| agency:services_close | 1/1 | 0 | 0 | 0.189 | 0.001 | 0.188 | 0.000 | 188.892 | 188.892 | 188.892 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.079 | 0.079 | 0.000 | 0.000 | 78.771 | 78.771 | 78.771 |
| agency:services_start | 1/1 | 0 | 0 | 0.072 | 0.041 | 0.031 | 0.000 | 72.293 | 72.293 | 72.293 |
| run:detect | 1/1 | 0 | 0 | 0.063 | 0.001 | 0.062 | 0.000 | 62.815 | 62.815 | 62.815 |
| agent:create | 1/1 | 0 | 0 | 0.039 | 0.010 | 0.029 | 0.000 | 38.638 | 38.638 | 38.638 |
| syscall:bind | 4/4 | 0 | 0 | 0.006 | n/a | n/a | 0.000 | 1.549 | 1.428 | 2.018 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.408 | 1.408 | 1.408 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.075 | 0.075 | 0.100 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.199 | 0.199 | 0.199 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.076 | 0.076 | 0.076 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 8076 | 0.111 | 0.029 | 167.002 | 0.039 | 8.988972 CPU seconds | n/a |
| GPU 0 memory | MB | 8077 | 12022.890 | 11670.000 | 16228.000 | 11974.000 | n/a | n/a |
| GPU 0 power | W | 8077 | 35.839 | 27.666 | 78.440 | 28.260 | n/a | 291569.635 J |
| GPU 0 proc / 8108-535102 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 memory | MB | 8077 | 3276.171 | 3118.000 | 7474.000 | 3220.000 | n/a | n/a |
| GPU 0 proc / 8108-535102 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 estimated power | W | 5004 | 5.338 | 0.000 | 76.988 | 0.000 | n/a | n/a |
| GPU 0 proc / 8108-535102 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 utilization | percent | 5004 | 6.221 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 8258-536859 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 memory | MB | 8077 | 8264.718 | 8070.000 | 8272.000 | 8272.000 | n/a | n/a |
| GPU 0 proc / 8258-536859 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 estimated power | W | 2924 | 19.825 | 0.000 | 72.642 | 0.000 | n/a | n/a |
| GPU 0 proc / 8258-536859 / sandbox / ~ / device / GPU-380351fa-bdc8-ca01-7f06-66067b2ea301 utilization | percent | 2924 | 27.489 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 8077 | 11540.890 | 11188.000 | 15746.000 | 11492.000 | n/a | n/a |
| GPU 0 utilization | percent | 8077 | 14.289 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 8077 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 8076 | 3.912 | 0.017 | 82.631 | 0.101 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 8076 | 8.297 | 0.000 | 41.863 | 0.000 | n/a | n/a |
| host disk_read_mb_s | MB/s | 8076 | 0.000 | 0.000 | 0.322 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 8076 | 0.202 | 0.000 | 87.298 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 8076 | 0.005 | 0.000 | 2.508 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 8076 | 0.005 | 0.000 | 2.522 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 8077 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 8077 | 7022.855 | 6359.184 | 11690.938 | 7013.281 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 8076 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 8076 | 0.000 | 0.000 | 0.036 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 8076 | 0.007 | 0.000 | 0.793 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10052) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10052) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10053) rss_mb | MB | 1 | 21.332 | 21.332 | 21.332 | 21.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10053) vms_mb | MB | 1 | 25.715 | 25.715 | 25.715 | 25.715 | n/a | n/a |
| sleep (PID 10067) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10067) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10067) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10067) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10067) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10067) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10070) rss_mb | MB | 1 | 1.535 | 1.535 | 1.535 | 1.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10070) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10071) rss_mb | MB | 1 | 14.852 | 14.852 | 14.852 | 14.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10071) vms_mb | MB | 1 | 19.957 | 19.957 | 19.957 | 19.957 | n/a | n/a |
| sleep (PID 10109) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10109) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10109) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10109) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10109) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10109) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10111) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10111) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10111) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10111) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10111) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10111) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10125) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10125) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10125) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10125) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10125) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10125) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10141) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10141) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10141) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10141) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10141) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10141) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10244) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10244) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10244) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10244) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 10244) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10244) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10251) rss_mb | MB | 1 | 1.539 | 1.539 | 1.539 | 1.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10251) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10252) rss_mb | MB | 1 | 15.680 | 15.680 | 15.680 | 15.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10252) vms_mb | MB | 1 | 20.500 | 20.500 | 20.500 | 20.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10260) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10260) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10261) rss_mb | MB | 1 | 8.043 | 8.043 | 8.043 | 8.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10261) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sleep (PID 10273) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10273) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10273) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10273) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10273) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10273) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10291) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10291) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10291) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10291) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10291) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10291) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10293) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10293) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10293) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10293) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10293) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10293) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10295) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10295) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10295) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10295) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10295) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10295) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10455) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10455) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10455) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10455) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 10455) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10455) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10457) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10457) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10457) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10457) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 10457) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10457) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10458) rss_mb | MB | 1 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10458) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10459) rss_mb | MB | 1 | 7.746 | 7.746 | 7.746 | 7.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10459) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sleep (PID 10471) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10471) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10471) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10471) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 10471) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10471) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10485) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10485) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10485) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10485) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10485) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10485) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10521) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10521) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10521) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10521) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10521) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10521) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10620) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10620) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10620) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10620) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10620) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10620) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10631) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10631) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10631) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10631) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10631) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10631) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10633) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10633) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10633) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10633) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10633) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10633) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10635) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10635) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10635) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10635) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 10635) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10635) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10721) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10721) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10721) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10721) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 10721) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10721) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10742) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10742) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10742) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10742) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10742) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10742) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10744) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10744) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10744) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10744) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10744) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10744) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10751) rss_mb | MB | 1 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10751) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10752) rss_mb | MB | 1 | 14.738 | 14.738 | 14.738 | 14.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10752) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10764) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10764) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10765) rss_mb | MB | 1 | 7.941 | 7.941 | 7.941 | 7.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10765) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sleep (PID 10778) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10778) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10778) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10778) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10778) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10778) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10795) rss_mb | MB | 1 | 1.539 | 1.539 | 1.539 | 1.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10795) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10796) rss_mb | MB | 1 | 7.496 | 7.496 | 7.496 | 7.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10796) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10819) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10819) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10820) rss_mb | MB | 1 | 18.785 | 18.785 | 18.785 | 18.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10820) vms_mb | MB | 1 | 24.223 | 24.223 | 24.223 | 24.223 | n/a | n/a |
| sleep (PID 10831) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10831) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10831) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10831) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10831) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10831) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10832) rss_mb | MB | 1 | 1.469 | 1.469 | 1.469 | 1.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10832) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10833) rss_mb | MB | 1 | 18.414 | 18.414 | 18.414 | 18.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10833) vms_mb | MB | 1 | 23.172 | 23.172 | 23.172 | 23.172 | n/a | n/a |
| sleep (PID 10920) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10920) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10920) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10920) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10920) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10920) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10942) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10942) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10942) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10942) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 10942) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10942) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10945) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10945) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10945) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10945) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10945) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10945) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10947) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10947) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10947) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10947) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10947) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10947) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10949) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10949) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10949) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10949) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10949) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10949) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 10953) rss_mb | MB | 1 | 14.207 | 14.207 | 14.207 | 14.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 10953) vms_mb | MB | 1 | 367.594 | 367.594 | 367.594 | 367.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 10974) CPU | percent | 3 | 171.645 | 161.927 | 180.963 | 180.963 | 5.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 10974) rss_mb | MB | 4 | 1192.136 | 1096.066 | 1480.344 | 1096.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 10974) main thread run-queue wait | percent | 3 | 64.035 | 43.180 | 74.484 | 74.441 | 1.932309 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 10974) vms_mb | MB | 4 | 1566.961 | 1478.934 | 1831.043 | 1478.934 | n/a | n/a |
| sleep (PID 10994) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10994) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10994) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10994) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10994) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10994) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| pgrep (PID 11109) rss_mb | MB | 1 | 3.305 | 3.305 | 3.305 | 3.305 | n/a | n/a |
| pgrep (PID 11109) vms_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sleep (PID 11110) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11110) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11110) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11110) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 11110) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11110) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11117) rss_mb | MB | 1 | 13.883 | 13.883 | 13.883 | 13.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11117) vms_mb | MB | 1 | 367.387 | 367.387 | 367.387 | 367.387 | n/a | n/a |
| sleep (PID 11132) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11132) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11132) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11132) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11132) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11132) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11137) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11137) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11138) rss_mb | MB | 1 | 14.863 | 14.863 | 14.863 | 14.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11138) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11157) CPU | percent | 22 | 99.751 | 99.146 | 100.468 | 99.344 | 22.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11157) rss_mb | MB | 23 | 11.930 | 11.930 | 11.930 | 11.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11157) main thread run-queue wait | percent | 22 | 0.004 | 0.001 | 0.007 | 0.005 | 0.000964 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11157) vms_mb | MB | 23 | 15.441 | 15.441 | 15.441 | 15.441 | n/a | n/a |
| sleep (PID 11165) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11165) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11165) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11165) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11165) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11165) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11177) rss_mb | MB | 1 | 1.469 | 1.469 | 1.469 | 1.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11177) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11178) rss_mb | MB | 1 | 9.691 | 9.691 | 9.691 | 9.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11178) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sleep (PID 11209) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11209) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11209) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11209) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11209) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11209) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11213) rss_mb | MB | 1 | 0.133 | 0.133 | 0.133 | 0.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11213) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11224) rss_mb | MB | 1 | 72.250 | 72.250 | 72.250 | 72.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11224) vms_mb | MB | 1 | 423.473 | 423.473 | 423.473 | 423.473 | n/a | n/a |
| sleep (PID 11239) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11239) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11239) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11239) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11239) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11239) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11350) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11350) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11350) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11350) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11350) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11350) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11351) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11351) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11352) rss_mb | MB | 1 | 15.828 | 15.828 | 15.828 | 15.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11352) vms_mb | MB | 1 | 20.535 | 20.535 | 20.535 | 20.535 | n/a | n/a |
| sleep (PID 11374) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11374) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11374) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11374) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11374) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11374) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11391) rss_mb | MB | 1 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11391) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11392) rss_mb | MB | 1 | 21.152 | 21.152 | 21.152 | 21.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11392) vms_mb | MB | 1 | 25.586 | 25.586 | 25.586 | 25.586 | n/a | n/a |
| sleep (PID 11398) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11398) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11398) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11398) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11398) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11398) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11412) rss_mb | MB | 1 | 1.414 | 1.414 | 1.414 | 1.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11412) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11413) rss_mb | MB | 1 | 14.680 | 14.680 | 14.680 | 14.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11413) vms_mb | MB | 1 | 19.957 | 19.957 | 19.957 | 19.957 | n/a | n/a |
| sleep (PID 11456) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11456) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11456) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11456) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11456) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11456) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11469) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11469) vms_mb | MB | 1 | 28.434 | 28.434 | 28.434 | 28.434 | n/a | n/a |
| sleep (PID 11480) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11480) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11480) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11480) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 11480) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11480) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11500) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11500) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11501) rss_mb | MB | 1 | 9.969 | 9.969 | 9.969 | 9.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11501) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11514) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11514) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11515) rss_mb | MB | 1 | 19.473 | 19.473 | 19.473 | 19.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11515) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sleep (PID 11524) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11524) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11524) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11524) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11524) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11524) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11534) rss_mb | MB | 1 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11534) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11535) rss_mb | MB | 1 | 20.891 | 20.891 | 20.891 | 20.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11535) vms_mb | MB | 1 | 25.461 | 25.461 | 25.461 | 25.461 | n/a | n/a |
| sleep (PID 11574) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11574) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11574) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11574) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11574) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11574) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11576) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11576) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11576) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11576) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11576) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11576) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11589) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11589) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11589) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11589) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11589) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11589) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 11603) rss_mb | MB | 1 | 2.680 | 2.680 | 2.680 | 2.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 11603) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11612) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11612) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11613) rss_mb | MB | 1 | 5.379 | 5.379 | 5.379 | 5.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11613) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11619) rss_mb | MB | 1 | 1.441 | 1.441 | 1.441 | 1.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11619) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11620) rss_mb | MB | 1 | 21.789 | 21.789 | 21.789 | 21.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11620) vms_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| sleep (PID 11624) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11624) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11624) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11624) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11624) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11624) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11625) rss_mb | MB | 1 | 1028.062 | 1028.062 | 1028.062 | 1028.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11625) vms_mb | MB | 1 | 1379.492 | 1379.492 | 1379.492 | 1379.492 | n/a | n/a |
| sleep (PID 11735) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11735) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11735) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11735) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11735) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11735) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11767) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11767) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11767) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11767) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11767) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11767) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11789) rss_mb | MB | 1 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11789) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11790) rss_mb | MB | 1 | 4.871 | 4.871 | 4.871 | 4.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11790) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11793) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11793) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11794) rss_mb | MB | 1 | 15.852 | 15.852 | 15.852 | 15.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11794) vms_mb | MB | 1 | 20.500 | 20.500 | 20.500 | 20.500 | n/a | n/a |
| sleep (PID 11808) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11808) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11808) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11808) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11808) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11808) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11809) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11809) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11810) rss_mb | MB | 1 | 22.039 | 22.039 | 22.039 | 22.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11810) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11813) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11813) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11814) rss_mb | MB | 1 | 19.242 | 19.242 | 19.242 | 19.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11814) vms_mb | MB | 1 | 24.684 | 24.684 | 24.684 | 24.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11842) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11842) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sleep (PID 11853) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11853) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11853) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11853) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11853) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11853) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11855) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11855) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11855) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11855) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11855) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11855) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_dev_traces.py (PID 11876) CPU | percent | 151 | 177.332 | 61.618 | 198.918 | 185.977 | 269.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_dev_traces.py (PID 11876) rss_mb | MB | 152 | 321.951 | 33.695 | 439.844 | 271.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_dev_traces.py (PID 11876) main thread run-queue wait | percent | 151 | 71.135 | 0.078 | 84.811 | 74.216 | 108.118150 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_dev_traces.py (PID 11876) vms_mb | MB | 152 | 697.505 | 385.172 | 826.539 | 648.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11889) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11889) rss_mb | MB | 3 | 1.570 | 1.570 | 1.570 | 1.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11889) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11889) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11890) CPU | percent | 2 | 4.970 | 3.977 | 5.963 | 3.977 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11890) rss_mb | MB | 3 | 14.059 | 4.754 | 20.605 | 20.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11890) main thread run-queue wait | percent | 2 | 71.267 | 55.182 | 87.352 | 87.352 | 1.433763 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11890) vms_mb | MB | 3 | 19.172 | 10.000 | 25.332 | 25.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11892) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11892) rss_mb | MB | 2 | 1.570 | 1.570 | 1.570 | 1.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11892) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11892) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11893) CPU | percent | 1 | 2.981 | 2.981 | 2.981 | 2.981 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11893) rss_mb | MB | 2 | 16.586 | 14.320 | 18.852 | 18.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11893) main thread run-queue wait | percent | 1 | 62.853 | 62.853 | 62.853 | 62.853 | 0.632527 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11893) vms_mb | MB | 2 | 22.451 | 20.086 | 24.816 | 24.816 | n/a | n/a |
| sleep (PID 11900) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11900) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11900) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11900) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11900) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11900) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11901) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11901) rss_mb | MB | 5 | 1.648 | 1.648 | 1.648 | 1.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11901) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11901) vms_mb | MB | 5 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11902) CPU | percent | 4 | 2.237 | 0.994 | 2.982 | 1.988 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11902) rss_mb | MB | 5 | 14.703 | 5.684 | 20.109 | 20.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11902) main thread run-queue wait | percent | 4 | 55.431 | 39.666 | 70.994 | 49.017 | 2.230452 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11902) vms_mb | MB | 5 | 20.140 | 11.512 | 25.328 | 25.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11903) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11903) rss_mb | MB | 4 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11903) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11903) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11904) CPU | percent | 3 | 2.980 | 0.994 | 5.965 | 5.965 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11904) rss_mb | MB | 4 | 16.493 | 10.832 | 21.371 | 21.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11904) main thread run-queue wait | percent | 3 | 71.920 | 66.822 | 81.111 | 67.828 | 2.172593 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11904) vms_mb | MB | 4 | 21.753 | 15.301 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11910) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11910) rss_mb | MB | 4 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11910) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11910) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11911) CPU | percent | 3 | 1.988 | 0.994 | 2.983 | 1.988 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11911) rss_mb | MB | 4 | 13.289 | 9.113 | 18.309 | 18.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11911) main thread run-queue wait | percent | 3 | 66.168 | 55.709 | 74.277 | 55.709 | 1.996883 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11911) vms_mb | MB | 4 | 18.515 | 13.551 | 24.680 | 24.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11914) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11914) rss_mb | MB | 6 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11914) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11914) vms_mb | MB | 6 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11915) CPU | percent | 5 | 2.379 | 0.000 | 7.926 | 7.926 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11915) rss_mb | MB | 6 | 11.577 | 5.527 | 21.184 | 21.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11915) main thread run-queue wait | percent | 5 | 42.461 | 18.077 | 66.201 | 52.775 | 2.140052 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11915) vms_mb | MB | 6 | 16.747 | 11.512 | 27.121 | 27.121 | n/a | n/a |
| sleep (PID 12000) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12000) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12000) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12000) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12000) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12000) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12019) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12019) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12019) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12019) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12019) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12019) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12021) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12021) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12021) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12021) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12021) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12021) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — test_uncentered_read.py (PID 12025) CPU | percent | 31 | 170.395 | 59.544 | 193.809 | 179.982 | 53.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — test_uncentered_read.py (PID 12025) rss_mb | MB | 32 | 140.109 | 14.637 | 162.098 | 161.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — test_uncentered_read.py (PID 12025) main thread run-queue wait | percent | 31 | 69.085 | 0.068 | 94.143 | 80.591 | 21.561387 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — test_uncentered_read.py (PID 12025) vms_mb | MB | 32 | 518.214 | 368.770 | 543.391 | 542.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12039) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12039) rss_mb | MB | 4 | 1.535 | 1.535 | 1.535 | 1.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12039) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12039) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12040) CPU | percent | 3 | 1.989 | 0.000 | 4.972 | 4.972 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12040) rss_mb | MB | 4 | 10.582 | 7.250 | 18.156 | 18.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12040) main thread run-queue wait | percent | 3 | 48.270 | 40.590 | 55.612 | 55.612 | 1.456644 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12040) vms_mb | MB | 4 | 15.326 | 11.660 | 23.172 | 23.172 | n/a | n/a |
| sleep (PID 12056) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12056) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12056) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12056) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12056) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12056) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12073) rss_mb | MB | 1 | 1.363 | 1.363 | 1.363 | 1.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12073) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12074) rss_mb | MB | 1 | 20.469 | 20.469 | 20.469 | 20.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12074) vms_mb | MB | 1 | 25.062 | 25.062 | 25.062 | 25.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_individual_dev_points.py (PID 12080) CPU | percent | 36 | 173.527 | 57.541 | 197.148 | 186.932 | 62.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_individual_dev_points.py (PID 12080) rss_mb | MB | 37 | 141.367 | 28.594 | 155.816 | 155.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_individual_dev_points.py (PID 12080) main thread run-queue wait | percent | 36 | 69.944 | 0.069 | 87.884 | 87.884 | 25.369293 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_individual_dev_points.py (PID 12080) vms_mb | MB | 37 | 519.684 | 380.496 | 537.410 | 537.410 | n/a | n/a |
| sleep (PID 12095) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12095) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12095) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12095) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12095) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12095) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12122) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12122) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12122) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12122) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12122) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12122) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12134) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12134) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12135) rss_mb | MB | 1 | 21.695 | 21.695 | 21.695 | 21.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12135) vms_mb | MB | 1 | 26.926 | 26.926 | 26.926 | 26.926 | n/a | n/a |
| sleep (PID 12145) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12145) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12145) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12145) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12145) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12145) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12155) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12155) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12155) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12155) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12155) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12155) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12170) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12170) rss_mb | MB | 3 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12170) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12170) vms_mb | MB | 3 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12171) CPU | percent | 2 | 150.976 | 128.951 | 173.002 | 173.002 | 3.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12171) rss_mb | MB | 3 | 735.048 | 69.504 | 1067.820 | 1067.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12171) main thread run-queue wait | percent | 2 | 47.025 | 19.275 | 74.775 | 74.775 | 0.946381 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12171) vms_mb | MB | 3 | 1253.733 | 860.941 | 1450.129 | 1450.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12179) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12179) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12180) rss_mb | MB | 1 | 20.719 | 20.719 | 20.719 | 20.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12180) vms_mb | MB | 1 | 25.203 | 25.203 | 25.203 | 25.203 | n/a | n/a |
| sleep (PID 12186) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12186) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12186) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12186) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12186) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12186) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12217) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12217) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12217) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12217) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12217) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12217) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12219) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12219) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12219) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12219) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12219) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12219) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12229) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12229) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12230) rss_mb | MB | 1 | 10.156 | 10.156 | 10.156 | 10.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12230) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sleep (PID 12236) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12236) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12236) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12236) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12236) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12236) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12238) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12238) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12238) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12238) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12238) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12238) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12249) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12249) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12250) rss_mb | MB | 1 | 21.812 | 21.812 | 21.812 | 21.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12250) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12261) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12261) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12262) rss_mb | MB | 1 | 16.992 | 16.992 | 16.992 | 16.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12262) vms_mb | MB | 1 | 22.184 | 22.184 | 22.184 | 22.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12271) rss_mb | MB | 1 | 1.414 | 1.414 | 1.414 | 1.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12271) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12272) rss_mb | MB | 1 | 0.715 | 0.715 | 0.715 | 0.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12272) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12281) rss_mb | MB | 1 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12281) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12282) rss_mb | MB | 1 | 21.332 | 21.332 | 21.332 | 21.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12282) vms_mb | MB | 1 | 25.707 | 25.707 | 25.707 | 25.707 | n/a | n/a |
| sleep (PID 12290) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12290) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12290) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12290) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12290) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12290) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12322) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12322) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12323) rss_mb | MB | 1 | 9.668 | 9.668 | 9.668 | 9.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12323) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12332) CPU | percent | 24 | 167.269 | 57.556 | 192.291 | 189.260 | 40.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12332) rss_mb | MB | 25 | 142.516 | 29.449 | 162.855 | 162.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12332) main thread run-queue wait | percent | 24 | 65.942 | 0.059 | 87.662 | 82.094 | 15.929666 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12332) vms_mb | MB | 25 | 519.556 | 381.219 | 554.711 | 544.180 | n/a | n/a |
| sleep (PID 12353) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12353) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12353) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12353) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12353) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12353) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12355) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12355) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12355) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12355) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12355) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12355) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12368) rss_mb | MB | 1 | 31.660 | 31.660 | 31.660 | 31.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12368) vms_mb | MB | 1 | 382.348 | 382.348 | 382.348 | 382.348 | n/a | n/a |
| sleep (PID 12391) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12391) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12391) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12391) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12391) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12391) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12395) CPU | percent | 8 | 167.660 | 90.382 | 184.841 | 172.917 | 13.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12395) rss_mb | MB | 9 | 1817.419 | 16.504 | 2042.680 | 2042.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12395) main thread run-queue wait | percent | 8 | 66.285 | 0.026 | 87.117 | 87.117 | 5.337122 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12395) vms_mb | MB | 9 | 2193.098 | 368.504 | 2425.172 | 2425.172 | n/a | n/a |
| sleep (PID 12410) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12410) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12410) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12410) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12410) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12410) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12414) CPU | percent | 9 | 180.028 | 129.160 | 189.865 | 184.854 | 16.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12414) rss_mb | MB | 10 | 2004.396 | 1664.875 | 2042.121 | 2042.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12414) main thread run-queue wait | percent | 9 | 76.881 | 27.588 | 87.813 | 87.813 | 6.977167 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12414) vms_mb | MB | 10 | 2414.178 | 2315.938 | 2425.094 | 2425.094 | n/a | n/a |
| sleep (PID 12431) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12431) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12431) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12431) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12431) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12431) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12456) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12456) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12456) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12456) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12456) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12456) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12458) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12458) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12458) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12458) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12458) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12458) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12460) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12460) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12460) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12460) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12460) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12460) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — design_dev_lora.py (PID 12474) CPU | percent | 5 | 158.361 | 89.313 | 187.954 | 186.971 | 7.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — design_dev_lora.py (PID 12474) rss_mb | MB | 6 | 1734.832 | 25.371 | 2079.723 | 2079.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — design_dev_lora.py (PID 12474) main thread run-queue wait | percent | 5 | 55.762 | 0.023 | 81.018 | 75.743 | 2.805867 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — design_dev_lora.py (PID 12474) vms_mb | MB | 6 | 2107.284 | 376.406 | 2462.801 | 2462.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12482) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12482) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12483) rss_mb | MB | 1 | 21.402 | 21.402 | 21.402 | 21.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12483) vms_mb | MB | 1 | 25.715 | 25.715 | 25.715 | 25.715 | n/a | n/a |
| sleep (PID 12485) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12485) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12485) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12485) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12485) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12485) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12494) CPU | percent | 10 | 172.220 | 87.453 | 187.941 | 185.973 | 17.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12494) rss_mb | MB | 11 | 1898.371 | 153.176 | 2076.059 | 2076.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12494) main thread run-queue wait | percent | 10 | 66.117 | 0.024 | 82.816 | 75.005 | 6.649063 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 12494) vms_mb | MB | 11 | 2307.620 | 861.562 | 2458.105 | 2458.105 | n/a | n/a |
| sleep (PID 12510) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12510) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12510) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12510) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12510) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12510) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12535) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12535) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12535) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12535) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12535) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12535) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12537) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12537) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12537) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12537) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12537) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12537) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_dev_edits.py (PID 12550) CPU | percent | 16 | 178.395 | 80.504 | 194.110 | 183.959 | 28.720000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_dev_edits.py (PID 12550) rss_mb | MB | 17 | 2305.304 | 397.086 | 2972.617 | 2972.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_dev_edits.py (PID 12550) main thread run-queue wait | percent | 16 | 70.027 | 0.045 | 85.636 | 75.650 | 11.273615 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_dev_edits.py (PID 12550) vms_mb | MB | 17 | 2688.890 | 862.695 | 3351.398 | 3351.398 | n/a | n/a |
| sleep (PID 12570) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12570) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12570) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12570) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12570) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12570) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12581) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12581) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12581) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12581) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12581) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12581) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12587) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12587) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12588) rss_mb | MB | 1 | 2.152 | 2.152 | 2.152 | 2.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12588) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sleep (PID 12595) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12595) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12595) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12595) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12595) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12595) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12617) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12617) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12618) rss_mb | MB | 1 | 9.266 | 9.266 | 9.266 | 9.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12618) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sleep (PID 12627) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12627) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12627) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12627) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12627) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12627) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12637) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12637) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12637) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12637) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12637) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12637) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12639) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12639) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12639) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12639) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12639) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12639) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12646) rss_mb | MB | 1 | 1.414 | 1.414 | 1.414 | 1.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12646) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12647) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12647) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sleep (PID 12656) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12656) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12656) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12656) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12656) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12656) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12658) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12658) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12658) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12658) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 12658) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12658) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12691) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12691) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12691) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12691) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12691) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12691) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12693) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12693) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12693) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12693) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12693) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12693) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12708) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12708) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12708) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12708) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12708) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12708) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12735) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12735) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sleep (PID 12742) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12742) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12742) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12742) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12742) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12742) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12744) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12744) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12744) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12744) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12744) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12744) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12775) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12775) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12775) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12775) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12775) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12775) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12915) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12915) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12915) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12915) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12915) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12915) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12928) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12928) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12928) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12928) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12928) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12928) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_dev_edits.py (PID 12940) CPU | percent | 36 | 176.303 | 58.583 | 193.888 | 166.823 | 63.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_dev_edits.py (PID 12940) rss_mb | MB | 37 | 2431.383 | 14.238 | 4260.945 | 4260.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_dev_edits.py (PID 12940) main thread run-queue wait | percent | 36 | 68.988 | 0.090 | 84.947 | 59.255 | 25.002935 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_dev_edits.py (PID 12940) vms_mb | MB | 37 | 2811.213 | 367.879 | 4706.426 | 4706.426 | n/a | n/a |
| sleep (PID 12954) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12954) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12954) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12954) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12954) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12954) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12966) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12966) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12966) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12966) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12966) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12966) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12986) rss_mb | MB | 1 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12986) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12987) rss_mb | MB | 1 | 20.262 | 20.262 | 20.262 | 20.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12987) vms_mb | MB | 1 | 24.941 | 24.941 | 24.941 | 24.941 | n/a | n/a |
| sleep (PID 13002) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13002) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13002) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13002) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13002) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13002) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13004) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13004) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13004) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13004) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13004) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13004) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13021) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13021) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13022) rss_mb | MB | 1 | 21.176 | 21.176 | 21.176 | 21.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13022) vms_mb | MB | 1 | 25.578 | 25.578 | 25.578 | 25.578 | n/a | n/a |
| sleep (PID 13028) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13028) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13028) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13028) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13028) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13028) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13030) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13030) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13030) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13030) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13030) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13030) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13048) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13048) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13048) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13048) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13048) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13048) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13068) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13068) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13068) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13068) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13068) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13068) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13083) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13083) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13083) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13083) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13083) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13083) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13087) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13087) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13088) rss_mb | MB | 1 | 16.578 | 16.578 | 16.578 | 16.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13088) vms_mb | MB | 1 | 21.848 | 21.848 | 21.848 | 21.848 | n/a | n/a |
| sleep (PID 13099) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13099) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13099) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13099) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13099) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13099) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13101) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13101) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13101) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13101) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13101) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13101) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 13105) CPU | percent | 40 | 178.336 | 60.646 | 195.106 | 183.962 | 71.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 13105) rss_mb | MB | 41 | 2679.813 | 23.203 | 4532.699 | 4532.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 13105) main thread run-queue wait | percent | 40 | 70.146 | 0.023 | 86.626 | 74.610 | 28.245893 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 13105) vms_mb | MB | 41 | 3056.542 | 374.535 | 4911.066 | 4911.066 | n/a | n/a |
| sleep (PID 13114) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13114) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13114) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13114) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13114) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13114) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13140) rss_mb | MB | 1 | 1.629 | 1.629 | 1.629 | 1.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13140) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13141) rss_mb | MB | 1 | 22.172 | 22.172 | 22.172 | 22.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13141) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sleep (PID 13150) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13150) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13150) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13150) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13150) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13150) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13155) rss_mb | MB | 1 | 1.570 | 1.570 | 1.570 | 1.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13155) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13156) rss_mb | MB | 1 | 21.039 | 21.039 | 21.039 | 21.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13156) vms_mb | MB | 1 | 25.316 | 25.316 | 25.316 | 25.316 | n/a | n/a |
| sleep (PID 13162) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13162) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13162) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13162) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 13162) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13162) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — evaluate_holdout.py (PID 13166) CPU | percent | 7 | 175.479 | 123.240 | 199.307 | 186.946 | 12.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — evaluate_holdout.py (PID 13166) rss_mb | MB | 8 | 1429.053 | 26.551 | 2492.008 | 2492.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — evaluate_holdout.py (PID 13166) main thread run-queue wait | percent | 7 | 62.571 | 15.654 | 75.954 | 75.666 | 4.407154 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — evaluate_holdout.py (PID 13166) vms_mb | MB | 8 | 1912.802 | 378.105 | 2873.754 | 2873.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13184) rss_mb | MB | 1 | 1.562 | 1.562 | 1.562 | 1.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13184) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13185) rss_mb | MB | 1 | 22.242 | 22.242 | 22.242 | 22.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13185) vms_mb | MB | 1 | 27.062 | 27.062 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — evaluate_holdout.py (PID 13192) CPU | percent | 7 | 173.585 | 122.212 | 190.877 | 186.847 | 12.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — evaluate_holdout.py (PID 13192) rss_mb | MB | 8 | 1412.880 | 98.344 | 2492.289 | 2492.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — evaluate_holdout.py (PID 13192) main thread run-queue wait | percent | 7 | 65.183 | 18.913 | 82.013 | 76.766 | 4.596740 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — evaluate_holdout.py (PID 13192) vms_mb | MB | 8 | 1806.375 | 496.641 | 2873.762 | 2873.762 | n/a | n/a |
| sleep (PID 13201) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13201) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13201) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13201) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13201) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13201) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 13211) rss_mb | MB | 1 | 20.566 | 20.566 | 20.566 | 20.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 13211) vms_mb | MB | 1 | 372.105 | 372.105 | 372.105 | 372.105 | n/a | n/a |
| sleep (PID 13228) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13228) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13228) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13228) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13228) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13228) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13258) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13258) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13258) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13258) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13258) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13258) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| docker commit (PID 13312) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 13312) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 13312) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 13312) rss_mb | MB | 2 | 30.039 | 30.039 | 30.039 | 30.039 | n/a | n/a |
| docker commit (PID 13312) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 13312) vms_mb | MB | 2 | 1988.035 | 1988.035 | 1988.035 | 1988.035 | n/a | n/a |
| sleep (PID 13452) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13452) io read MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13452) io write MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13452) rss_mb | MB | 12 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13452) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13452) vms_mb | MB | 12 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 8099) CPU | percent | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 8099) io read MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 8099) io write MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 8099) rss_mb | MB | 8077 | 3.402 | 3.402 | 3.402 | 3.402 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 8099) main thread run-queue wait | percent | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 8099) vms_mb | MB | 8077 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 8108) CPU | percent | 8076 | 13.359 | 0.000 | 300.995 | 0.995 | 1090.020000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 8108) io read MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.311 | 0.000 | 0.941406 MB | n/a |
| Agency harness — python -m lsbench (PID 8108) io write MB/s | MB/s | 8076 | 0.119 | 0.000 | 57.665 | 0.027 | 969.074219 MB | n/a |
| Agency harness — python -m lsbench (PID 8108) rss_mb | MB | 8077 | 2555.859 | 1959.918 | 4072.965 | 2876.387 | n/a | n/a |
| Agency harness — python -m lsbench (PID 8108) main thread run-queue wait | percent | 8076 | 0.000 | 0.000 | 0.876 | 0.000 | 0.011891 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 8108) vms_mb | MB | 8077 | 16275.825 | 14020.020 | 21082.699 | 16531.574 | n/a | n/a |
| Python — vllm (PID 8119) CPU | percent | 8076 | 0.327 | 0.000 | 5.967 | 0.000 | 26.630000 CPU seconds | n/a |
| Python — vllm (PID 8119) io read MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 8119) io write MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.008 | 0.000 | 0.144531 MB | n/a |
| Python — vllm (PID 8119) rss_mb | MB | 8077 | 1787.614 | 1782.391 | 1788.016 | 1787.930 | n/a | n/a |
| Python — vllm (PID 8119) main thread run-queue wait | percent | 8076 | 0.004 | 0.000 | 1.511 | 0.000 | 0.304585 run-queue seconds | n/a |
| Python — vllm (PID 8119) vms_mb | MB | 8077 | 11996.550 | 11922.215 | 11999.234 | 11998.234 | n/a | n/a |
| bash lsb_guard.sh (PID 8129) CPU | percent | 8076 | 0.001 | 0.000 | 0.995 | 0.000 | 0.070000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 8129) io read MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 8129) io write MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 8129) rss_mb | MB | 8077 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| bash lsb_guard.sh (PID 8129) main thread run-queue wait | percent | 8076 | 0.000 | 0.000 | 0.117 | 0.000 | 0.002202 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 8129) vms_mb | MB | 8077 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sleep (PID 8132) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8132) io read MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8132) io write MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8132) rss_mb | MB | 16 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8132) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8132) vms_mb | MB | 16 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — python -c (PID 8257) CPU | percent | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 8257) io read MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 8257) io write MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 8257) rss_mb | MB | 8077 | 12.184 | 12.184 | 12.184 | 12.184 | n/a | n/a |
| Python — python -c (PID 8257) main thread run-queue wait | percent | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 8257) vms_mb | MB | 8077 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 8258) CPU | percent | 8076 | 3.773 | 0.000 | 54.493 | 0.000 | 307.590000 CPU seconds | n/a |
| VLLM::EngineCore (PID 8258) io read MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 8258) io write MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.004 | 0.000 | 0.050781 MB | n/a |
| VLLM::EngineCore (PID 8258) rss_mb | MB | 8077 | 2346.616 | 2339.188 | 2346.938 | 2346.938 | n/a | n/a |
| VLLM::EngineCore (PID 8258) main thread run-queue wait | percent | 8076 | 0.000 | 0.000 | 0.021 | 0.000 | 0.024674 run-queue seconds | n/a |
| VLLM::EngineCore (PID 8258) vms_mb | MB | 8077 | 21867.676 | 21860.672 | 21867.945 | 21867.945 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 8385) CPU | percent | 8076 | 0.049 | 0.000 | 4.970 | 0.000 | 4.010000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 8385) io read MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 8385) io write MB/s | MB/s | 8076 | 0.000 | 0.000 | 0.008 | 0.000 | 0.402344 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 8385) rss_mb | MB | 8077 | 45.336 | 43.852 | 46.141 | 45.566 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 8385) main thread run-queue wait | percent | 8076 | 0.001 | 0.000 | 0.504 | 0.000 | 0.112524 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 8385) vms_mb | MB | 8077 | 131.321 | 131.172 | 131.949 | 131.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 8518) CPU | percent | 8052 | 0.002 | 0.000 | 0.995 | 0.000 | 0.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 8518) rss_mb | MB | 8053 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 8518) main thread run-queue wait | percent | 8052 | 0.007 | 0.000 | 7.669 | 0.000 | 0.558783 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 8518) vms_mb | MB | 8053 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 8557) CPU | percent | 8052 | 0.002 | 0.000 | 0.995 | 0.000 | 0.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 8557) rss_mb | MB | 8053 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 8557) main thread run-queue wait | percent | 8052 | 0.008 | 0.000 | 7.951 | 0.000 | 0.615255 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 8557) vms_mb | MB | 8053 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 8662) CPU | percent | 8052 | 38.688 | 0.000 | 101.216 | 0.000 | 3135.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 8662) rss_mb | MB | 8053 | 109.737 | 3.195 | 149.359 | 149.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 8662) main thread run-queue wait | percent | 8052 | 0.000 | 0.000 | 0.006 | 0.000 | 0.000102 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 8662) vms_mb | MB | 8053 | 971.153 | 4.262 | 973.465 | 971.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 8668) CPU | percent | 1 | 98.447 | 98.447 | 98.447 | 98.447 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 8668) rss_mb | MB | 2 | 58.695 | 33.777 | 83.613 | 83.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 8668) main thread run-queue wait | percent | 1 | 0.008 | 0.008 | 0.008 | 0.008 | 0.000086 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 8668) vms_mb | MB | 2 | 69.645 | 41.137 | 98.152 | 98.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 8685) CPU | percent | 8046 | 1.448 | 0.000 | 74.230 | 5.959 | 117.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 8685) rss_mb | MB | 8047 | 301.602 | 199.090 | 349.234 | 342.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 8685) main thread run-queue wait | percent | 8046 | 0.644 | 0.000 | 70.164 | 0.038 | 52.128464 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 8685) vms_mb | MB | 8047 | 2280.872 | 1914.910 | 2345.090 | 2342.918 | n/a | n/a |
| sleep (PID 8710) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8710) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8710) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8710) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8710) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8710) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8809) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8809) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 8810) rss_mb | MB | 1 | 21.277 | 21.277 | 21.277 | 21.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 8810) vms_mb | MB | 1 | 25.844 | 25.844 | 25.844 | 25.844 | n/a | n/a |
| sleep (PID 8841) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8841) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8841) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8841) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8841) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8841) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 8874) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8874) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8874) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8874) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8874) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8874) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8894) rss_mb | MB | 1 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8894) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8895) rss_mb | MB | 1 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8895) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sleep (PID 8915) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8915) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8915) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8915) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8915) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8915) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 8917) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8917) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8917) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8917) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8917) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8917) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9015) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9015) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9015) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9015) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9015) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9015) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9026) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9026) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9026) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9026) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9026) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9026) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9113) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9113) rss_mb | MB | 5 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9113) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9113) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sleep (PID 9115) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sleep (PID 9115) rss_mb | MB | 5 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sleep (PID 9115) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sleep (PID 9115) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sleep (PID 9123) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9123) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9123) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9123) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9123) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9123) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9125) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9125) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9125) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9125) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9125) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9125) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9127) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9127) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9127) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9127) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 9127) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9127) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9303) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9303) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9304) rss_mb | MB | 1 | 17.676 | 17.676 | 17.676 | 17.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9304) vms_mb | MB | 1 | 23.020 | 23.020 | 23.020 | 23.020 | n/a | n/a |
| sleep (PID 9311) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9311) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9311) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9311) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9311) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9311) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9312) rss_mb | MB | 1 | 1.570 | 1.570 | 1.570 | 1.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9312) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9313) rss_mb | MB | 1 | 7.363 | 7.363 | 7.363 | 7.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9313) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sleep (PID 9316) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9316) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9316) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9316) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9316) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9316) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9359) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9359) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9359) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9359) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9359) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9359) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9369) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9369) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9370) rss_mb | MB | 1 | 19.473 | 19.473 | 19.473 | 19.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9370) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9392) rss_mb | MB | 1 | 9.391 | 9.391 | 9.391 | 9.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9392) vms_mb | MB | 1 | 13.316 | 13.316 | 13.316 | 13.316 | n/a | n/a |
| sleep (PID 9400) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9400) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9400) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9400) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9400) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9400) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9489) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9489) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9490) rss_mb | MB | 1 | 16.301 | 16.301 | 16.301 | 16.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9490) vms_mb | MB | 1 | 20.848 | 20.848 | 20.848 | 20.848 | n/a | n/a |
| sleep (PID 9501) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9501) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9501) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9501) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9501) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9501) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9534) rss_mb | MB | 1 | 9.516 | 9.516 | 9.516 | 9.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9534) vms_mb | MB | 1 | 13.316 | 13.316 | 13.316 | 13.316 | n/a | n/a |
| sleep (PID 9551) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9551) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9551) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9551) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9551) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9551) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9552) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9552) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9553) rss_mb | MB | 1 | 7.496 | 7.496 | 7.496 | 7.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9553) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sleep (PID 9589) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9589) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9589) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9589) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9589) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9589) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9617) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9617) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9617) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9617) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9617) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9617) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9649) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9649) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9649) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9649) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9649) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9649) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9761) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9761) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9761) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9761) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9761) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9761) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9816) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9816) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9816) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9816) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9816) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9816) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9832) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9832) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9832) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9832) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9832) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9832) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9833) rss_mb | MB | 1 | 1.414 | 1.414 | 1.414 | 1.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9833) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9834) rss_mb | MB | 1 | 22.090 | 22.090 | 22.090 | 22.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9834) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9844) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9844) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9845) rss_mb | MB | 1 | 15.754 | 15.754 | 15.754 | 15.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9845) vms_mb | MB | 1 | 20.398 | 20.398 | 20.398 | 20.398 | n/a | n/a |
| sleep (PID 9853) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9853) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9853) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9853) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9853) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9853) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9854) rss_mb | MB | 1 | 1.500 | 1.500 | 1.500 | 1.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9854) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9855) rss_mb | MB | 1 | 10.719 | 10.719 | 10.719 | 10.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9855) vms_mb | MB | 1 | 15.062 | 15.062 | 15.062 | 15.062 | n/a | n/a |
| sleep (PID 9865) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9865) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9865) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9865) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9865) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9865) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9961) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9961) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9961) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9961) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9961) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9961) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 CPU | percent | 8052 | 49.609 | 0.000 | 217.393 | 0.000 | 4020.201833 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 8052 | 3.579 | 0.000 | 75.430 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 8052 | 3.816 | 0.000 | 82.213 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io_psi_full_pct | percent of wall time stalled | 8052 | 0.000 | 0.000 | 0.120 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io_psi_some_pct | percent of wall time stalled | 8052 | 0.000 | 0.000 | 0.130 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io read MB/s | MB/s | 8052 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io write MB/s | MB/s | 8052 | 0.058 | 0.000 | 85.371 | 0.000 | 471.335938 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory | MB | 8053 | 384.457 | 25.789 | 4947.047 | 135.090 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory_psi_full_pct | percent of wall time stalled | 8052 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory_psi_some_pct | percent of wall time stalled | 8052 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 net rx MB/s | MB/s | 8052 | 0.000 | 0.000 | 0.007 | 0.000 | 0.435779 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 net tx MB/s | MB/s | 8052 | 0.000 | 0.000 | 0.041 | 0.000 | 3.677810 MB | n/a |
| workload total CPU | percent | 8076 | 17.534 | 1.298 | 301.395 | 1.316 | 1430.573615 CPU seconds | n/a |
| workload total memory | MB | 8077 | 5596.896 | 4903.668 | 7013.289 | 6057.090 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
